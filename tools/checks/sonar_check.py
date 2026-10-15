"""The `sonar` check: SonarCloud's quality gate for this pull request, read from
SonarCloud's public API -- the bot's own comment is evidence, this is the verdict.

SonarCloud is free only for public projects. A private repository passes with that
recorded; its code is still covered by the `security` check.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

import common as c

API = "https://sonarcloud.io/api"
WAIT_S = 600


def get(path: str):
    req = urllib.request.Request(API + path, headers={"User-Agent": "harithkavish-checks"})
    token = os.environ.get("SONAR_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def main() -> None:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if os.environ.get("REPO_PRIVATE") == "true":
        c.verdict("sonar", "PASS", [], ["private repository: SonarCloud is not available on the free plan; "
                                        "covered by the security check instead"])
    key = repo.replace("/", "_")
    number = c.pr().get("number")
    q = {"projectKey": key}
    if number:
        q["pullRequest"] = str(number)
    url = "/qualitygates/project_status?" + urllib.parse.urlencode(q)
    deadline = time.time() + WAIT_S
    while True:
        try:
            status = get(url)["projectStatus"]
            break
        except urllib.error.HTTPError as e:
            if e.code == 404 and time.time() < deadline:
                time.sleep(20)       # analysis of this pull request not published yet
                continue
            c.verdict("sonar", "FAIL", [f"SonarCloud has no analysis for `{key}`"
                                        + (f" pull request #{number}" if number else "")
                                        + f" (HTTP {e.code}). Import the repository in SonarCloud "
                                          "(organisation harithkavish, Automatic Analysis)."])
    failed = [f"{x['metricKey']}: {x.get('actualValue')} (needs {x.get('comparator')} {x.get('errorThreshold')})"
              for x in status.get("conditions") or [] if x.get("status") == "ERROR"]
    link = f"https://sonarcloud.io/dashboard?id={key}" + (f"&pullRequest={number}" if number else "")
    if status.get("status") == "OK":
        c.verdict("sonar", "PASS", [], [f"quality gate passed -- {link}"])
    c.verdict("sonar", "FAIL", failed or [f"quality gate status {status.get('status')}"], [link])


if __name__ == "__main__":
    main()
