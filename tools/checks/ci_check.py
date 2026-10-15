"""The `ci` check: the repository's own build and tests, as its manifest declares them
(project.yaml `verify.build` / `verify.test`). A repository with neither says why in
`verify.none_reason`; saying nothing is a FAIL, because "no tests" and "forgot to declare
the tests" must not look the same.
"""
from __future__ import annotations

import subprocess

import common as c


def main() -> None:
    m, err = c.manifest()
    if m is None:
        c.verdict("ci", "FAIL", [f".project/project.yaml {'is ' + err if err else 'is missing'}: "
                                 "nothing declares how to build or test this repository"])
    v = m.get("verify") or {}
    steps = [(k, v.get(k)) for k in ("build", "test") if v.get(k)]
    if not steps:
        if v.get("none_reason"):
            c.verdict("ci", "PASS", [], [f"no build or tests, declared: {v['none_reason']}"])
        c.verdict("ci", "FAIL", ["verify.build and verify.test are both empty and verify.none_reason "
                                 "does not say why"])
    findings, passed = [], []
    for name, cmd in steps:
        print(f"::group::{name}: {cmd}")
        r = subprocess.run(cmd, shell=True, cwd=c.REPO)
        print("::endgroup::")
        (passed if r.returncode == 0 else findings).append(
            f"{name} `{cmd}` {'succeeded' if r.returncode == 0 else f'failed (exit {r.returncode})'}")
    c.verdict("ci", "FAIL" if findings else "PASS", findings, passed)


if __name__ == "__main__":
    main()
