"""Phase 0 collector: read-only inventory of every repository the gh token can reach.

Usage:  py -3 collect_inventory.py <output.json>

Write the output OUTSIDE any repository: it contains per-repository security data (open
Dependabot alert counts) that must not be committed to a public repository (DEC-007).
Makes no changes anywhere -- every call is a GET.
"""
import json, subprocess, sys, os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor


def gh(args, ok_codes=(0,)):
    p = subprocess.run(["gh"] + args, capture_output=True, text=True, encoding="utf-8")
    if p.returncode not in ok_codes:
        return None, (p.stderr or p.stdout).strip()[:300]
    try:
        return json.loads(p.stdout) if p.stdout.strip() else {}, None
    except json.JSONDecodeError:
        return p.stdout, None

FILES = ["README.md", "readme.md", "LICENSE", "LICENSE.md", "LICENSE.txt", "SECURITY.md",
         ".github/SECURITY.md", "CONTRIBUTING.md", ".github/CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
         ".github/CODE_OF_CONDUCT.md", "SUPPORT.md", "CHANGELOG.md", "CITATION.cff",
         "AGENTS.md", "GOVERNANCE.md", "CLAUDE.md", ".github/CODEOWNERS", "CODEOWNERS",
         ".github/dependabot.yml", ".github/pull_request_template.md", ".project/project.yaml",
         ".github/workflows/claude-review.yml", ".github/workflows/pr-gate.yml",
         ".github/workflows/governance.yml", "docs"]

def alias(path):
    return "f_" + "".join(c if c.isalnum() else "_" for c in path)

def gql_for(owner, name, branch_expr):
    files = "\n".join(
        f'{alias(p)}: object(expression: "{branch_expr}:{p}") {{ __typename }}' for p in FILES)
    return f'''query {{ repository(owner: "{owner}", name: "{name}") {{
      nameWithOwner description homepageUrl visibility isArchived isFork isTemplate isMirror
      createdAt pushedAt updatedAt diskUsage
      parent {{ nameWithOwner }}
      defaultBranchRef {{ name target {{ ... on Commit {{ committedDate history(first:0) {{ totalCount }} }} }} }}
      primaryLanguage {{ name }}
      languages(first: 6, orderBy: {{field: SIZE, direction: DESC}}) {{ nodes {{ name }} }}
      licenseInfo {{ spdxId name }}
      repositoryTopics(first: 20) {{ nodes {{ topic {{ name }} }} }}
      hasIssuesEnabled hasWikiEnabled hasDiscussionsEnabled hasProjectsEnabled
      deleteBranchOnMerge autoMergeAllowed
      isSecurityPolicyEnabled
      hasVulnerabilityAlertsEnabled
      openGraphImageUrl usesCustomOpenGraphImage
      issues(states: OPEN) {{ totalCount }}
      pullRequests(states: OPEN) {{ totalCount }}
      releases {{ totalCount }}
      latestRelease {{ tagName publishedAt }}
      tags: refs(refPrefix: "refs/tags/", first: 0) {{ totalCount }}
      branches: refs(refPrefix: "refs/heads/", first: 100) {{ totalCount nodes {{ name }} }}
      branchProtectionRules(first: 20) {{ nodes {{ pattern requiresApprovingReviews requiredApprovingReviewCount requiresStatusChecks requiredStatusCheckContexts isAdminEnforced allowsForcePushes allowsDeletions }} }}
      workflows: object(expression: "{branch_expr}:.github/workflows") {{ ... on Tree {{ entries {{ name }} }} }}
      {files}
    }} }}'''

def collect(full):
    owner, name = full.split("/")
    rec = {"full_name": full, "errors": []}
    data, err = gh(["api", "graphql", "-f", "query=" + gql_for(owner, name, "HEAD")])
    if err:
        rec["errors"].append("graphql:" + err); return rec
    r = data["data"]["repository"]
    present = [p for p in FILES if r.get(alias(p))]
    for p in FILES: r.pop(alias(p), None)
    r["files_default"] = present
    rec.update(r)
    branches = [n["name"] for n in r["branches"]["nodes"]]
    if "development" in branches:
        d, err = gh(["api", "graphql", "-f", "query=" + gql_for(owner, name, "development")])
        if not err:
            dr = d["data"]["repository"]
            rec["files_development"] = [p for p in FILES if dr.get(alias(p))]
            rec["workflows_development"] = [e["name"] for e in ((dr.get("workflows") or {}).get("entries") or [])]
    # REST: security settings (admin only), rulesets, pages, PVR, code scanning default setup
    repo, err = gh(["api", f"repos/{full}"])
    if repo:
        rec["security_and_analysis"] = repo.get("security_and_analysis")
        rec["has_pages"] = repo.get("has_pages")
        rec["allow_forking"] = repo.get("allow_forking")
        rec["web_commit_signoff_required"] = repo.get("web_commit_signoff_required")
    rs, err = gh(["api", f"repos/{full}/rulesets"])
    rec["rulesets"] = [{"name": x.get("name"), "target": x.get("target"), "enforcement": x.get("enforcement")} for x in rs] if isinstance(rs, list) else ("ERR " + (err or ""))
    if rec.get("has_pages"):
        pg, err = gh(["api", f"repos/{full}/pages"])
        rec["pages"] = {"build_type": pg.get("build_type"), "cname": pg.get("cname"), "source": pg.get("source"), "html_url": pg.get("html_url")} if isinstance(pg, dict) else ("ERR " + (err or ""))
    pvr, err = gh(["api", f"repos/{full}/private-vulnerability-reporting"])
    rec["private_vulnerability_reporting"] = pvr.get("enabled") if isinstance(pvr, dict) else ("ERR " + (err or ""))
    cs, err = gh(["api", f"repos/{full}/code-scanning/default-setup"])
    rec["code_scanning_default_setup"] = cs.get("state") if isinstance(cs, dict) else ("ERR " + (err or ""))
    da, err = gh(["api", "--paginate", f"repos/{full}/dependabot/alerts?state=open&per_page=100",
                  "--jq", ".[].security_advisory.severity"])
    rec["dependabot_open_alerts"] = (dict(Counter(da.split())) if isinstance(da, str)
                                     else {} if da == {} else "ERR " + (err or ""))
    env, err = gh(["api", f"repos/{full}/environments"])
    rec["environments"] = [e["name"] for e in env.get("environments", [])] if isinstance(env, dict) else ("ERR " + (err or ""))
    return rec

def main():
    if len(sys.argv) != 2:
        sys.exit("usage: collect_inventory.py <output.json>  (write it outside the repository)")
    out = sys.argv[1]
    names, err = gh(["api", "--paginate", "user/repos?per_page=100&affiliation=owner,collaborator,organization_member",
                     "--jq", ".[].full_name"])
    names = sorted(set(names.split())) if isinstance(names, str) else []
    print(f"{len(names)} repositories", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=8) as ex:
        recs = list(ex.map(collect, names))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(recs, f, indent=1)
    print(f"wrote {out}; errors in {sum(1 for r in recs if r['errors'])}", file=sys.stderr)

if __name__ == "__main__":
    main()
