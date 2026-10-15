"""The `policy` check: is this change allowed to reach its target, and is the repository
still described truthfully?

  - the head branch is one the target accepts (standards/BRANCHING.md: development <-
    feature/hotfix/Dependabot, runway <- development, main <- runway/hotfix)
  - the governed workflows are byte-identical to governance's templates
  - .project/project.yaml exists, is valid against schemas/project.schema.json, and the
    platforms it declares match the ones detected (standards/PROJECT.md)
"""
from __future__ import annotations

import fnmatch
import json
import subprocess

import common as c


def blob(path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return subprocess.run(["git", "hash-object", "--stdin"], input=data,
                          capture_output=True, check=True).stdout.decode().strip()


def main() -> None:
    pol = c.policy()
    base, head = c.base_ref(), c.head_ref()
    findings, passed = [], []

    stage = pol["stages"].get(base)
    if stage is None:
        passed.append(f"target `{base or '?'}` is not a protected branch: no source rule")
    elif any(fnmatch.fnmatch(head, pat) for pat in stage["accepts_from"]):
        passed.append(f"`{head}` -> `{base}` is an allowed promotion path")
    else:
        findings.append(f"`{base}` accepts changes only from {', '.join(stage['accepts_from'])}, "
                        f"not from `{head}`. Open the change against the right branch.")

    tdir = c.GOV / "tools" / "policy" / "templates"
    for t in sorted(tdir.glob("*.yml")):
        mine = c.REPO / ".github" / "workflows" / t.name
        if not mine.exists():
            findings.append(f"governed workflow `{t.name}` is missing")
        elif blob(mine) != blob(t):
            findings.append(f"governed workflow `{t.name}` differs from governance's copy -- "
                            "governed workflows change in governance, not here")
        else:
            passed.append(f"`{t.name}` matches governance")

    m, err = c.manifest()
    if err:
        findings.append(f".project/project.yaml is {err}")
    elif m is None:
        findings.append(".project/project.yaml is missing (standards/PROJECT.md)")
    else:
        try:
            import jsonschema
            schema = json.loads((c.GOV / "schemas" / "project.schema.json").read_text(encoding="utf-8"))
            errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(m), key=lambda e: list(e.path))
            for e in errors[:8]:
                where = "/".join(str(p) for p in e.path) or "(top level)"
                findings.append(f"project.yaml {where}: {e.message}")
            if not errors:
                passed.append("project.yaml is valid")
        except ImportError:
            findings.append("jsonschema is not installed in the check environment")
        det, dec = c.detected(), c.declared(m)
        for v in sorted(set(det) - dec):
            findings.append(f"`{v}` is used ({', '.join(det[v])}) but not declared in project.yaml infra -- "
                            "an undeclared platform gets no verifier")
        for v in sorted(dec - set(det) - {"oracle-vm", "live-surface"}):
            findings.append(f"`{v}` is declared in project.yaml but nothing in the repository uses it -- "
                            "is the manifest stale?")
        if not (set(det) ^ (dec - {"oracle-vm", "live-surface"})):
            passed.append(f"declared platforms match detected: {', '.join(sorted(det)) or 'none'}")

    c.verdict("policy", "FAIL" if findings else "PASS", findings, passed)


if __name__ == "__main__":
    main()
