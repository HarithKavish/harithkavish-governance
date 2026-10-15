#!/usr/bin/env python3
"""Policy engine: make every repository the account owns match schemas/policy.yaml.

WHY THIS EXISTS

GitHub only enforces rules account-wide for organizations on a paid plan; on a personal
account every repository is configured one at a time, and a repository created tomorrow
starts with nothing. Governance said every repository must have development, runway and
main, protected, with gates -- and on 2026-10-15 29 of 66 had the gate, 34 had no
required check at all, and one working branch had no protection. Rules that depend on
somebody remembering to set them up do not hold. This is the somebody.

Each pass, for every repository:

  inspect   branches, default branch, rulesets, legacy branch protection, the governed
            workflows, the project manifest, and which platforms the code uses
  plan      the actions that close the gap -- nothing is changed yet
  apply     (--apply) create missing branches, set the default branch, create or update
            the governance-<branch> rulesets with NO bypass, and retire legacy branch
            protection once the ruleset covers it

A check is only made required once something in that repository produces it; the
report lists every check that is policy but not yet required, and why. Requiring a check
nothing reports would freeze every merge.

    python tools/policy/engine.py                  # dry run, all repositories
    python tools/policy/engine.py --repo jarvis    # one repository
    python tools/policy/engine.py --apply          # make it so
    python tools/policy/engine.py --json report.json

Token: GH_TOKEN (the policy App's installation token in Actions; `gh auth token` locally
for a dry run).
"""
from __future__ import annotations

import argparse
import base64
import fnmatch
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
POLICY = yaml.safe_load((ROOT / "schemas" / "policy.yaml").read_text(encoding="utf-8"))
API = "https://api.github.com"
ACTIONS_APP_ID = 15368          # GitHub Actions: the app every workflow check is reported by
GOVERNED_WORKFLOWS = ["claude-review.yml", "pr-gate.yml", "governance.yml"]
# check name -> the workflow file in the repository that produces it
PRODUCERS = {
    "gate": "pr-gate.yml",
    "policy": "governance.yml",
    "ci": "governance.yml",
    "security": "governance.yml",
    "sonar": "governance.yml",
    "release": "governance.yml",
}


# --- GitHub ---------------------------------------------------------------------------

class GitHub:
    def __init__(self, token: str, apply: bool):
        self.token = token
        self.apply = apply

    def call(self, method: str, path: str, body=None, ok404=False):
        url = path if path.startswith("http") else API + path
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "harithkavish-policy-engine",
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            if e.code == 404 and ok404:
                return None
            detail = e.read().decode(errors="replace")[:300]
            raise RuntimeError(f"{method} {path}: HTTP {e.code} {detail}") from None

    def get(self, path, ok404=False):
        return self.call("GET", path, ok404=ok404)

    def paged(self, path):
        out, page = [], 1
        sep = "&" if "?" in path else "?"
        while True:
            chunk = self.get(f"{path}{sep}per_page=100&page={page}")
            items = chunk if isinstance(chunk, list) else chunk.get("repositories", [])
            out += items
            if len(items) < 100:
                return out
            page += 1


# --- inspection -----------------------------------------------------------------------

@dataclass
class Repo:
    name: str
    private: bool
    archived: bool
    empty: bool
    default: str
    branches: set = field(default_factory=set)
    rulesets: dict = field(default_factory=dict)        # name -> full ruleset
    legacy: dict = field(default_factory=dict)          # branch -> protection
    files: set = field(default_factory=set)             # paths on the default branch
    workflows: dict = field(default_factory=dict)       # governed workflow -> blob sha
    manifest: dict | None = None
    manifest_error: str | None = None
    detected: dict = field(default_factory=dict)        # verifier -> evidence
    ahead: dict = field(default_factory=dict)           # "development->runway" -> commits
    pushers: list = field(default_factory=list)         # workflows that push commits
    actions: list = field(default_factory=list)
    notes: list = field(default_factory=list)


TEMPLATES = Path(__file__).with_name("templates")


def canonical_workflows(gh: GitHub) -> dict:
    """The workflow blobs governance distributes (tools/policy/templates/): what every
    repository's copy must equal, compared by git blob hash."""
    out = {}
    for wf in GOVERNED_WORKFLOWS:
        data = (TEMPLATES / wf).read_bytes().replace(b"\r\n", b"\n")
        out[wf] = subprocess.run(["git", "hash-object", "--stdin"], input=data,
                                 capture_output=True, check=True).stdout.decode().strip()
    return out


def detect(repo: Repo, gh: GitHub, owner: str) -> None:
    """Which platforms the code uses, by the detection rules in policy.yaml."""
    for name, v in POLICY["verifiers"].items():
        evidence = []
        for pat in v.get("detect") or []:
            if any(c in pat for c in "*/.") and not pat.startswith(("mongodb+srv", '"')):
                hits = [f for f in repo.files if fnmatch.fnmatch(f, pat) or f == pat]
                evidence += hits[:3]
        if name == "mongodb-atlas":
            # content signals: only look in dependency manifests, which are small
            for f in [x for x in repo.files if x.split("/")[-1] in
                      ("package.json", "requirements.txt", "pyproject.toml")][:8]:
                body = read_file(gh, owner, repo, f) or ""
                if any(s in body for s in ("mongodb", "pymongo", "motor", "mongoose")):
                    evidence.append(f)
        if evidence:
            repo.detected[name] = sorted(set(evidence))[:3]


def read_file(gh: GitHub, owner: str, repo: Repo, path: str) -> str | None:
    meta = gh.get(f"/repos/{owner}/{repo.name}/contents/{urllib.parse.quote(path)}?ref={repo.default}",
                  ok404=True)
    if not meta or meta.get("encoding") != "base64":
        return None
    return base64.b64decode(meta["content"]).decode("utf-8", errors="replace")


def inspect(gh: GitHub, owner: str, raw: dict) -> Repo:
    r = Repo(name=raw["name"], private=raw["private"], archived=raw["archived"],
             empty=raw.get("size", 0) == 0 and not raw.get("pushed_at"),
             default=raw["default_branch"])
    base = f"/repos/{owner}/{r.name}"
    try:
        r.branches = {b["name"] for b in gh.paged(f"{base}/branches")}
    except RuntimeError as e:
        if "409" in str(e):          # empty repository
            r.empty = True
            return r
        raise
    if not r.branches:
        r.empty = True
        return r
    for rs in gh.get(f"{base}/rulesets") or []:
        r.rulesets[rs["name"]] = gh.get(f"{base}/rulesets/{rs['id']}")
    for b in POLICY["branches"]["protected"]:
        if b in r.branches:
            p = gh.get(f"{base}/branches/{b}/protection", ok404=True)
            if p:
                r.legacy[b] = p
    tree = gh.get(f"{base}/git/trees/{urllib.parse.quote(r.default)}?recursive=1", ok404=True) or {}
    r.files = {t["path"] for t in tree.get("tree", []) if t["type"] == "blob"
               and "node_modules/" not in t["path"]}
    for t in tree.get("tree", []):
        if t["path"].startswith(".github/workflows/") and t["path"].split("/")[-1] in GOVERNED_WORKFLOWS:
            r.workflows[t["path"].split("/")[-1]] = t["sha"]
    if ".project/project.yaml" in r.files:
        try:
            r.manifest = yaml.safe_load(read_file(gh, owner, r, ".project/project.yaml") or "") or {}
        except yaml.YAMLError as e:
            r.manifest_error = str(e)[:200]
    detect(r, gh, owner)
    # With no bypass, a workflow that pushes straight to a protected branch will fail.
    for f in sorted(x for x in r.files if x.startswith(".github/workflows/")
                    and x.split("/")[-1] not in GOVERNED_WORKFLOWS):
        body = read_file(gh, owner, r, f) or ""
        if "git push" in body or "add-and-commit" in body or "git-auto-commit" in body:
            r.pushers.append(f.split("/")[-1])
    for a, b in (("development", "runway"), ("runway", "main")):
        if a in r.branches and b in r.branches:
            cmp = gh.get(f"{base}/compare/{b}...{a}", ok404=True) or {}
            r.ahead[f"{a}->{b}"] = cmp.get("ahead_by", 0)
    return r


# --- planning -------------------------------------------------------------------------

def produced_checks(r: Repo) -> set:
    present = {f.split("/")[-1] for f in r.files if f.startswith(".github/workflows/")}
    return {check for check, wf in PRODUCERS.items() if wf in present}


def desired_ruleset(branch: str, checks: list[str]) -> dict:
    stage = POLICY["stages"][branch]
    rules = POLICY["ruleset"]["rules"]
    out = []
    if rules.get("deletion"):
        out.append({"type": "deletion"})
    if rules.get("non_fast_forward"):
        out.append({"type": "non_fast_forward"})
    if rules.get("creation"):
        out.append({"type": "creation"})
    pr = rules["pull_request"]
    out.append({"type": "pull_request", "parameters": {
        "required_approving_review_count": pr["required_approving_review_count"],
        "dismiss_stale_reviews_on_push": pr["dismiss_stale_reviews_on_push"],
        "require_code_owner_review": False,
        "require_last_push_approval": False,
        "required_review_thread_resolution": pr["required_review_thread_resolution"],
        "allowed_merge_methods": [stage["merge_method"]],
    }})
    if checks:
        out.append({"type": "required_status_checks", "parameters": {
            "strict_required_status_checks_policy": False,
            "required_status_checks": [{"context": c, "integration_id": ACTIONS_APP_ID} for c in checks],
        }})
    return {
        "name": f"{POLICY['ruleset']['prefix']}-{branch}",
        "target": "branch",
        "enforcement": "active",
        "bypass_actors": [],
        "conditions": {"ref_name": {"include": [f"refs/heads/{branch}"], "exclude": []}},
        "rules": out,
    }


def normalise(rs: dict) -> dict:
    """The parts of a ruleset that policy decides, in a comparable form."""
    rules = {}
    for rule in rs.get("rules", []):
        params = dict(rule.get("parameters") or {})
        if rule["type"] == "required_status_checks":
            params["required_status_checks"] = sorted(
                (c["context"], c.get("integration_id")) for c in params.get("required_status_checks", []))
            params.pop("do_not_enforce_on_create", None)
        if rule["type"] == "pull_request":
            params = {k: params.get(k) for k in ("required_approving_review_count",
                      "dismiss_stale_reviews_on_push", "require_code_owner_review",
                      "require_last_push_approval", "required_review_thread_resolution",
                      "allowed_merge_methods")}
        rules[rule["type"]] = params
    return {"enforcement": rs.get("enforcement"), "bypass": rs.get("bypass_actors") or [],
            "include": rs.get("conditions", {}).get("ref_name", {}).get("include"), "rules": rules}


def plan(r: Repo, canonical: dict) -> None:
    if r.empty:
        r.actions.append(("seed", "repository is empty: commit a README so branches can exist"))
        return
    if r.archived:
        r.notes.append("archived: rulesets apply, but nothing can be pushed until it is unarchived")
    protected = POLICY["branches"]["protected"]
    source = "main" if "main" in r.branches else r.default
    for b in protected:
        if b not in r.branches:
            r.actions.append(("branch", f"create {b} from {source}"))
    if r.default != POLICY["branches"]["default"]:
        r.actions.append(("default", f"default branch {r.default} -> {POLICY['branches']['default']}"))

    have = produced_checks(r)
    for b in protected:
        want_checks = [c for c in POLICY["stages"][b]["required_checks"] if c in have]
        missing = [c for c in POLICY["stages"][b]["required_checks"] if c not in have]
        if missing:
            r.notes.append(f"{b}: not yet required (nothing produces them here): {', '.join(missing)}")
        want = desired_ruleset(b, want_checks)
        cur = r.rulesets.get(want["name"])
        if cur is None:
            r.actions.append(("ruleset", f"create {want['name']} (checks: {', '.join(want_checks) or 'none yet'})"))
        elif normalise(cur) != normalise(want):
            r.actions.append(("ruleset", f"update {want['name']}: drifted from policy"))
        if cur and cur.get("bypass_actors"):
            r.notes.append(f"{want['name']} had bypass actors: {cur['bypass_actors']} -- removed by update")
    for b, prot in r.legacy.items():
        r.actions.append(("legacy", f"retire classic protection on {b} once {POLICY['ruleset']['prefix']}-{b} is active"))

    for wf in GOVERNED_WORKFLOWS:
        if wf not in r.workflows:
            r.actions.append(("workflow", f"add {wf} (by pull request)"))
        elif canonical.get(wf) and r.workflows[wf] != canonical[wf]:
            r.actions.append(("workflow", f"{wf} differs from governance's copy (by pull request)"))

    if r.manifest is None:
        r.actions.append(("manifest", ".project/project.yaml missing (drafted by pull request)"
                          + (f"; invalid: {r.manifest_error}" if r.manifest_error else "")))
    else:
        declared = set((r.manifest.get("infra") or {}).keys())
        key = {v["declares"].split(".", 1)[1]: n for n, v in POLICY["verifiers"].items()
               if v["declares"].startswith("infra.")}
        declared_verifiers = {key.get(k, k) for k in declared}
        for v in sorted(set(r.detected) - declared_verifiers):
            r.actions.append(("manifest", f"{v} detected ({', '.join(r.detected[v])}) but not declared"))
        for v in sorted(declared_verifiers - set(r.detected) - {"oracle-vm"}):
            r.notes.append(f"{v} declared but not detected -- stale manifest?")
    for wf in r.pushers:
        r.notes.append(f"workflow {wf} pushes commits: if it targets development/runway/main it "
                       "will be refused once the rulesets are active -- change it to open a PR")
    for pair, n in r.ahead.items():
        if n:
            r.notes.append(f"{pair}: {n} commit(s) awaiting promotion")


# --- applying -------------------------------------------------------------------------

def apply(gh: GitHub, owner: str, r: Repo) -> list[str]:
    done = []
    base = f"/repos/{owner}/{r.name}"
    kinds = {k for k, _ in r.actions}
    if r.archived or r.empty:
        return [f"skipped: {'archived' if r.archived else 'empty'} -- needs a human"]
    if "branch" in kinds:
        src = "main" if "main" in r.branches else r.default
        sha = gh.get(f"{base}/git/ref/heads/{urllib.parse.quote(src)}")["object"]["sha"]
        for b in POLICY["branches"]["protected"]:
            if b not in r.branches:
                gh.call("POST", f"{base}/git/refs", {"ref": f"refs/heads/{b}", "sha": sha})
                r.branches.add(b)
                done.append(f"created {b} at {sha[:7]}")
    if "default" in kinds:
        gh.call("PATCH", base, {"default_branch": POLICY["branches"]["default"]})
        done.append(f"default branch -> {POLICY['branches']['default']}")
    have = produced_checks(r)
    active = set()
    for b in POLICY["branches"]["protected"]:
        want = desired_ruleset(b, [c for c in POLICY["stages"][b]["required_checks"] if c in have])
        cur = r.rulesets.get(want["name"])
        if cur is None:
            gh.call("POST", f"{base}/rulesets", want)
            done.append(f"created {want['name']}")
        elif normalise(cur) != normalise(want):
            gh.call("PUT", f"{base}/rulesets/{cur['id']}", want)
            done.append(f"restored {want['name']}")
        active.add(b)
    for b in list(r.legacy):
        if b in active:
            gh.call("DELETE", f"{base}/branches/{b}/protection")
            done.append(f"retired classic protection on {b}")
    return done


# --- main -----------------------------------------------------------------------------

def token() -> str:
    t = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--repo", action="append", help="limit to these repositories")
    ap.add_argument("--json", help="write the full report here")
    a = ap.parse_args()

    owner = POLICY["scope"]["owner"]
    gh = GitHub(token(), a.apply)
    try:   # an App installation token lists what it is installed on (all repositories)
        listed = gh.paged("/installation/repositories")
    except RuntimeError:   # a user token, for a local dry run
        listed = gh.paged("/user/repos?affiliation=owner&visibility=all")
    raw = [x for x in listed
           if x["owner"]["login"] == owner and x["name"] not in POLICY["scope"]["exclude"]]
    if a.repo:
        raw = [x for x in raw if x["name"] in a.repo]
    canonical = canonical_workflows(gh)

    report, compliant = [], 0
    for x in sorted(raw, key=lambda x: x["name"].lower()):
        try:
            r = inspect(gh, owner, x)
            plan(r, canonical)
            done = apply(gh, owner, r) if a.apply and r.actions else []
        except Exception as e:  # one broken repository must not stop the pass
            print(f"!! {x['name']}: {e}", file=sys.stderr)
            report.append({"repo": x["name"], "error": str(e)})
            continue
        compliant += not r.actions
        report.append({"repo": r.name, "private": r.private, "default": r.default,
                       "actions": [f"{k}: {v}" for k, v in r.actions], "notes": r.notes,
                       "detected": r.detected, "done": done})
        mark = "OK " if not r.actions else f"{len(r.actions):2d} "
        print(f"{mark} {r.name}{' (private)' if r.private else ''}")
        for k, v in r.actions:
            print(f"      - {k}: {v}")
        for d in done:
            print(f"      + {d}")
    print(f"\n{compliant}/{len(report)} repositories compliant"
          f"{'' if a.apply else ' (dry run: nothing changed)'}")
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
