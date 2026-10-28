"""The `release` check: on a pull request into `main`, every verifier that applies to the
repository gives a verdict, and the release passes only if all of them say PASS
(standards/BRANCHING.md § The checks in each gate). On any other target it is not a
release and passes.

A verifier applies when .project/project.yaml declares the platform or it is detected
(the `policy` check already fails when those disagree). A platform's own bot -- the
Cloudflare build, the Vercel deployment -- is evidence read here; the verdict is ours.
A verifier that cannot verify (no credentials, nothing reachable from CI) says HOLD,
never PASS: what was not checked was not verified.
"""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

import common as c


def head_sha() -> str:
    return (c.pr().get("head") or {}).get("sha") or os.environ.get("GITHUB_SHA", "")


def check_runs(slug: str) -> list[dict]:
    repo = os.environ["GITHUB_REPOSITORY"]
    runs = c.gh(f"/repos/{repo}/commits/{head_sha()}/check-runs?per_page=100").get("check_runs", [])
    return [r for r in runs if ((r.get("app") or {}).get("slug") or "") == slug]


def statuses(prefix: str) -> list[dict]:
    repo = os.environ["GITHUB_REPOSITORY"]
    st = c.gh(f"/repos/{repo}/commits/{head_sha()}/status") or {}
    return [s for s in st.get("statuses", []) if s.get("context", "").startswith(prefix)]


# --- verifiers: each returns (verdict, [findings or evidence]) -------------------------

def v_cloudflare(m):
    runs = check_runs("cloudflare-workers-and-pages")
    if not runs:
        return "FAIL", ["no Cloudflare Workers/Pages build was reported for this commit -- "
                        "connect the repository in Cloudflare (Workers Builds) so runway builds"]
    bad = [r for r in runs if r.get("conclusion") not in ("success", "neutral", "skipped")]
    out = [f"{r['name']}: {r.get('conclusion') or r.get('status')}" for r in runs]
    for f in [x for x in c.repo_files() if x.split("/")[-1].startswith("wrangler.")]:
        body = (c.REPO / f).read_text(encoding="utf-8", errors="replace")
        if re.search(r"(?im)^\s*\[vars\][\s\S]*?(secret|token|password|api_key)\s*=", body):
            return "FAIL", [f"`{f}` puts a secret-looking value in [vars] -- use `wrangler secret`"]
    return ("FAIL" if bad else "PASS"), out


def v_vercel(m):
    st = statuses("Vercel")
    if not st:
        return "FAIL", ["no Vercel deployment was reported for this commit"]
    bad = [s for s in st if s["state"] != "success"]
    return ("FAIL" if bad else "PASS"), [f"{s['context']}: {s['state']} {s.get('target_url') or ''}" for s in st]


def v_github_pages(m):
    want = ((m or {}).get("infra") or {}).get("github_pages", {}).get("domain")
    cname = c.REPO / "CNAME"
    have = cname.read_text().strip() if cname.exists() else None
    if want and have and want != have:
        return "FAIL", [f"CNAME is `{have}` but project.yaml declares `{want}`"]
    return "PASS", [f"Pages deploys from main on merge; the live site is verified by live-surface"
                    + (f" (domain {have})" if have else "")]


def atlas(path: str):
    pub, priv = os.environ.get("ATLAS_PUBLIC_KEY"), os.environ.get("ATLAS_PRIVATE_KEY")
    mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    mgr.add_password(None, "https://cloud.mongodb.com/", pub, priv)
    opener = urllib.request.build_opener(urllib.request.HTTPDigestAuthHandler(mgr))
    req = urllib.request.Request("https://cloud.mongodb.com/api/atlas/v2" + path,
                                 headers={"Accept": "application/vnd.atlas.2023-01-01+json"})
    with opener.open(req, timeout=30) as r:
        return json.loads(r.read())


def v_mongodb_atlas(m):
    if not (os.environ.get("ATLAS_PUBLIC_KEY") and os.environ.get("ATLAS_PRIVATE_KEY")):
        return "HOLD", ["Atlas credentials (ATLAS_PUBLIC_KEY / ATLAS_PRIVATE_KEY, read-only project "
                        "key) are not available to this repository, so Atlas was not verified"]
    project = ((m or {}).get("infra") or {}).get("mongodb_atlas", {}).get("project")
    if not project:
        return "FAIL", ["project.yaml declares MongoDB Atlas without naming its project"]
    try:
        gid = atlas(f"/groups/byName/{urllib.request.quote(project)}")["id"]
        access = atlas(f"/groups/{gid}/accessList").get("results", [])
        users = atlas(f"/groups/{gid}/databaseUsers").get("results", [])
    except urllib.error.HTTPError as e:
        return "HOLD", [f"Atlas API refused ({e.code}) -- check the key's project access"]
    findings = [f"network access open to the world: {a.get('cidrBlock')}" for a in access
                if a.get("cidrBlock") in ("0.0.0.0/0", "::/0")]
    broad = {"atlasAdmin", "readWriteAnyDatabase", "dbAdminAnyDatabase", "userAdminAnyDatabase"}
    findings += [f"database user `{u['username']}` holds {r['roleName']}" for u in users
                 for r in u.get("roles", []) if r.get("roleName") in broad]
    if findings:
        return "FAIL", findings
    return "PASS", [f"Atlas project `{project}`: {len(access)} access entries, {len(users)} users, least privilege"]


def v_render(m):
    repo = os.environ["GITHUB_REPOSITORY"]
    deps = c.gh(f"/repos/{repo}/deployments?sha={head_sha()}&per_page=20") or []
    deps = [d for d in deps if "render" in (d.get("environment") or "").lower()
            or "render" in ((d.get("creator") or {}).get("login") or "").lower()]
    if not deps:
        return "HOLD", ["no Render deployment reported for this commit -- confirm the service deployed"]
    st = c.gh(f"/repos/{repo}/deployments/{deps[0]['id']}/statuses") or []
    state = st[0]["state"] if st else "unknown"
    return ("PASS" if state == "success" else "FAIL"), [f"Render {deps[0]['environment']}: {state}"]


def v_android(m):
    declared = set(((m or {}).get("infra") or {}).get("android", {}).get("permissions") or [])
    used = set()
    for f in [x for x in c.repo_files() if x.endswith("AndroidManifest.xml")]:
        used |= set(re.findall(r'uses-permission[^>]*android:name="([^"]+)"',
                               (c.REPO / f).read_text(encoding="utf-8", errors="replace")))
    extra = sorted(used - declared)
    if extra:
        return "FAIL", [f"Android permissions requested but not declared in project.yaml: {', '.join(extra)}"]
    return "PASS", [f"{len(used)} Android permissions, all declared"]


def v_oracle_vm(m):
    return "HOLD", ["the Oracle VM is reachable only over Tailscale, not from CI -- "
                    "deploy health is confirmed by Jarvis's system events; the owner approves"]


def v_live_surface(m):
    s = (m or {}).get("surface") or {}
    url = s.get("runway") or s.get("main")
    if not url:
        return "FAIL", ["project.yaml surface has no runway or main URL to verify"]
    target = url.rstrip("/") + (s.get("health") or "")
    try:
        req = urllib.request.Request(target, headers={"User-Agent": "harithkavish-release-check"})
        with urllib.request.urlopen(req, timeout=20) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        return "FAIL", [f"{target} did not answer: {e}"]
    return ("PASS" if 200 <= code < 400 else "FAIL"), [f"{target} answered {code}"]


VERIFIERS = {
    "cloudflare": v_cloudflare, "vercel": v_vercel, "github-pages": v_github_pages,
    "mongodb-atlas": v_mongodb_atlas, "render": v_render, "android": v_android,
    "oracle-vm": v_oracle_vm, "live-surface": v_live_surface,
}


def main() -> None:
    if c.base_ref() != "main":
        c.verdict("release", "PASS", [], [f"target is `{c.base_ref() or '?'}`, not main: not a release"])
    m, _ = c.manifest()
    applies = sorted(c.declared(m) | set(c.detected()))
    if not applies:
        c.verdict("release", "PASS", [], ["no platform verifiers apply: nothing is deployed"])
    findings, passed, worst = [], [], "PASS"
    rank = {"PASS": 0, "HOLD": 1, "FAIL": 2}
    for name in applies:
        try:
            v, notes = VERIFIERS[name](m)
        except Exception as e:
            v, notes = "FAIL", [f"verifier crashed: {type(e).__name__}: {e}"]
        line = f"verify/{name}: {v} -- " + "; ".join(notes)
        (passed if v == "PASS" else findings).append(line)
        worst = max(worst, v, key=rank.get)
    c.verdict("release", worst, findings, passed)


if __name__ == "__main__":
    main()
