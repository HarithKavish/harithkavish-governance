"""The `security` check (standards/BRANCHING.md, the runway minimum):

  - a secret scan over the commits this pull request adds (gitleaks) -- any finding FAILs;
  - a dependency scan of the repository's lockfiles (osv-scanner) -- a HIGH or CRITICAL
    advisory FAILs, lower ones are listed;
  - a secret the code reads that the manifest does not declare is listed.

gitleaks and osv-scanner are installed by governance.yml before this runs.
"""
from __future__ import annotations

import json
import os
import subprocess

import common as c

BLOCKING = {"HIGH", "CRITICAL"}


def secrets_scan(findings, passed):
    base = (c.pr().get("base") or {}).get("sha")
    head = (c.pr().get("head") or {}).get("sha") or "HEAD"
    args = ["gitleaks", "detect", "--no-banner", "--redact", "--report-format", "json",
            "--report-path", "/tmp/gitleaks.json", "--source", str(c.REPO)]
    if base:
        args += ["--log-opts", f"{base}..{head}"]
    r = subprocess.run(args, capture_output=True, text=True)
    try:
        leaks = json.load(open("/tmp/gitleaks.json"))
    except (OSError, ValueError):
        leaks = []
    if r.returncode not in (0, 1):
        findings.append(f"gitleaks could not run: {r.stderr.strip()[:200]}")
    for l in leaks[:10]:
        findings.append(f"secret ({l.get('RuleID')}) committed in `{l.get('File')}` line {l.get('StartLine')} "
                        f"({l.get('Commit', '')[:7]}) -- rotate it, then remove it from history")
    if not leaks and r.returncode == 0:
        passed.append("no secrets in the commits this change adds")


def severity(vuln: dict) -> str:
    s = (vuln.get("database_specific") or {}).get("severity") or ""
    return s.upper() if isinstance(s, str) else ""


def dependency_scan(findings, passed):
    r = subprocess.run(["osv-scanner", "scan", "source", "-r", "--format", "json", str(c.REPO)],
                       capture_output=True, text=True)
    try:
        data = json.loads(r.stdout or "{}")
    except ValueError:
        findings.append(f"osv-scanner output unreadable: {r.stderr.strip()[:200]}")
        return
    blocking, other = [], 0
    for res in data.get("results") or []:
        for pkg in res.get("packages") or []:
            name = (pkg.get("package") or {}).get("name")
            ver = (pkg.get("package") or {}).get("version")
            for v in pkg.get("vulnerabilities") or []:
                sev = severity(v)
                if sev in BLOCKING:
                    blocking.append(f"{sev} {v.get('id')} in {name} {ver} ({(res.get('source') or {}).get('path', '')})")
                else:
                    other += 1
    findings += blocking[:15]
    if len(blocking) > 15:
        findings.append(f"... and {len(blocking) - 15} more HIGH/CRITICAL advisories")
    if not blocking:
        passed.append("no HIGH or CRITICAL dependency advisories"
                      + (f" ({other} lower-severity advisories -- see the osv-scanner log)" if other else ""))


def undeclared_secrets(findings, passed):
    m, _ = c.manifest()
    names = {s["name"] for s in (m or {}).get("secrets") or [] if isinstance(s, dict) and "name" in s}
    used = set()
    for f in c.repo_files():
        governed = {t.name for t in (c.GOV / "tools" / "policy" / "templates").glob("*.yml")}
        if (f.startswith(".github/workflows/") and f.endswith((".yml", ".yaml"))
                and f.split("/")[-1] not in governed):   # governance's own optional secrets
            body = (c.REPO / f).read_text(encoding="utf-8", errors="replace")
            import re
            used |= set(re.findall(r"secrets\.([A-Za-z_][A-Za-z0-9_]*)", body))
    used -= {"GITHUB_TOKEN"}
    missing = sorted(used - names)
    if missing:
        findings.append("secrets used by workflows but not declared in project.yaml: " + ", ".join(missing))
    else:
        passed.append(f"every workflow secret is declared ({len(used)})")


def main() -> None:
    findings, passed = [], []
    secrets_scan(findings, passed)
    dependency_scan(findings, passed)
    undeclared_secrets(findings, passed)
    c.verdict("security", "FAIL" if findings else "PASS", findings, passed)


if __name__ == "__main__":
    main()
