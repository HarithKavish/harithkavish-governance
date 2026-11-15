"""Shared by the governed checks (tools/checks/*.py), which run inside each repository's
governance.yml with governance itself checked out at .governance/.

Every check ends in one verdict, like the code reviewer:
  PASS  verified
  FAIL  something is wrong -- the job fails, nothing merges until it is fixed
  HOLD  correct as far as can be checked, but it needs the owner -- the job fails until
        the owner has approved the pull request, then passes (standards/BRANCHING.md)
"""
from __future__ import annotations

import fnmatch
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

GOV = Path(os.environ.get("GOVERNANCE_DIR", ".governance"))
REPO = Path(os.environ.get("REPO_DIR", "."))


def policy() -> dict:
    import yaml
    return yaml.safe_load((GOV / "schemas" / "policy.yaml").read_text(encoding="utf-8"))


def event() -> dict:
    try:
        return json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    except (KeyError, OSError, ValueError):
        return {}


def pr() -> dict:
    return event().get("pull_request") or {}


def base_ref() -> str:
    return (pr().get("base") or {}).get("ref") or os.environ.get("GITHUB_BASE_REF", "")


def head_ref() -> str:
    return (pr().get("head") or {}).get("ref") or os.environ.get("GITHUB_HEAD_REF", "")


def manifest() -> tuple[dict | None, str | None]:
    """(manifest, error). Missing is (None, None)."""
    import yaml
    p = REPO / ".project" / "project.yaml"
    if not p.exists():
        return None, None
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}, None
    except yaml.YAMLError as e:
        return None, f"not valid YAML: {str(e)[:200]}"


def repo_files() -> list[str]:
    out = subprocess.run(["git", "-C", str(REPO), "ls-files"], capture_output=True, text=True).stdout
    return [f for f in out.splitlines() if "node_modules/" not in f]


def detected() -> dict[str, list[str]]:
    """Which platforms the repository uses, by policy.yaml's detection rules."""
    files = repo_files()
    out = {}
    for name, v in policy()["verifiers"].items():
        ev = []
        for pat in v.get("detect") or []:
            if pat.startswith(("mongodb+srv", '"')):
                continue
            ev += [f for f in files if f == pat or fnmatch.fnmatch(f, pat)][:3]
        if name == "mongodb-atlas":
            for f in [x for x in files if x.split("/")[-1] in ("package.json", "requirements.txt", "pyproject.toml")][:8]:
                body = (REPO / f).read_text(encoding="utf-8", errors="replace")
                if any(s in body for s in ("mongodb", "pymongo", "motor", "mongoose")):
                    ev.append(f)
        if ev:
            out[name] = sorted(set(ev))[:3]
    return out


def declared(m: dict | None) -> set[str]:
    """Verifier names the manifest declares (infra.* and surface)."""
    if not m:
        return set()
    key = {v["declares"].split(".", 1)[1]: n for n, v in policy()["verifiers"].items()
           if v["declares"].startswith("infra.")}
    out = {key.get(k, k) for k in (m.get("infra") or {})}
    if (m.get("surface") or {}).get("main"):
        out.add("live-surface")
    return out


def gh(path: str):
    req = urllib.request.Request("https://api.github.com" + path, headers={
        "Authorization": f"Bearer {os.environ.get('GH_TOKEN', '')}",
        "Accept": "application/vnd.github+json", "User-Agent": "harithkavish-checks"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read() or b"null")


def owner_approved() -> bool:
    """Return True if the owner has approved the pull request as it stands.
    Adopts the established pattern from pr-gate: the owner raising a change IS
    the owner's say-so (GitHub forbids self-approval). Otherwise the owner's
    LATEST non-COMMENTED review decides -- a later CHANGES_REQUESTED or
    DISMISSED on the same head withdraws an earlier approval, and a bare
    comment is not a verdict. The latest review must be APPROVED at the PR
    head SHA, so stale approvals don't count either. A failed API call logs
    the reason and fails safe instead of silently returning False."""
    repo, number = os.environ.get("GITHUB_REPOSITORY", ""), pr().get("number")
    if not repo or not number:
        return False
    owner = repo.split("/")[0]
    # The review's commit_id is the head SHA the review was submitted against;
    # pull_request.head.sha is that same SHA in both trigger events. GITHUB_SHA
    # is the merge commit on pull_request events and would never match.
    head_sha = (pr().get("head") or {}).get("sha", "")
    # The owner raising it is the owner's decision (pr-gate #93 pattern)
    author = pr().get("user", {}).get("login", "")
    if author == owner:
        return True
    try:
        # The API returns reviews oldest-first, so the last owner review in
        # the list is the latest. Fetch every page: the latest one can sit
        # beyond the first 100 on a long-running pull request.
        reviews: list = []
        page = 1
        while True:
            batch = gh(f"/repos/{repo}/pulls/{number}/reviews?per_page=100&page={page}") or []
            reviews += batch
            if len(batch) < 100:
                break
            page += 1
    except Exception as e:
        print(f"::error::owner_approved: GitHub API error: {e}")
        return False
    mine = [r for r in reviews
            if r["user"]["login"] == owner and r["state"] != "COMMENTED"]
    if not mine:
        return False
    latest = mine[-1]
    return latest["state"] == "APPROVED" and latest.get("commit_id") == head_sha


def verdict(check: str, v: str, findings: list[str], passed: list[str] | None = None) -> None:
    """Write the verdict to the job summary and exit accordingly. Never returns."""
    lines = [f"VERDICT: {v}", "", f"### {check}"]
    if findings:
        lines += ["", "**Findings**", *[f"- {f}" for f in findings]]
    if passed:
        lines += ["", "**Checked**", *[f"- {p}" for p in passed]]
    text = "\n".join(lines) + "\n"
    print(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(text)
    if v == "PASS":
        sys.exit(0)
    if v == "HOLD":
        if owner_approved():
            print("HOLD, and the owner has approved: passing.")
            sys.exit(0)
        print("::error::HOLD -- it passes once the owner approves this pull request.")
        sys.exit(1)
    print(f"::error::{check}: FAIL -- {findings[0] if findings else 'see the summary'}")
    sys.exit(1)
