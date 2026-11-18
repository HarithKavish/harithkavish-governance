# GitHub Capability Matrix

> **Record, not authority.** What GitHub offers, what this ecosystem uses, and what the
> programme recommends. A recommendation becomes a requirement only in a standard.

**Measured 2026-11-18** across 72 repositories; "covered" means the 33 the registry covers.
Statuses use the brief's vocabulary:

| Status | Meaning |
|---|---|
| ENABLED | A switch that is on |
| CONFIGURED | Set up with deliberate settings |
| NOT CONFIGURED | Available and not set up |
| NOT AVAILABLE | The plan or visibility does not offer it |
| NOT APPLICABLE | Offered, but does not fit the ecosystem |
| BLOCKED | Cannot be measured or changed with the access the agent has |

Where repositories differ, the status is the covered majority and the count is given.

## The plan question

The personal account's plan cannot be read with the agent's token (no `user` scope). One
observation bears on it: **classic branch protection is configured, and readable, on private
repositories** (`jarvis`, `my_chatgpt`, others). GitHub's API refuses that on the Free plan,
so the account most likely has Pro-level features — although an earlier operating note
recorded a Free-plan Actions allowance. Treated as **unverified** until the owner confirms
(DEC-P12). The organisation `harithkavishtechnologies` is on **Free** (verified).

Feature availability below is stated for **public** repositories, where every relevant
feature is free, and noted separately for private ones.

---

| ID | Capability | Status (covered) | Measured | Recommended | Implications | Owner? |
|---|---|---|---|---|---|---|
| CAP-01 | **Repository metadata** — description, homepage, topics, social preview | NOT CONFIGURED (partly) | Description 31/33 · homepage 7/33 · topics 7/33 · custom social preview **0/33** | Already required by [REPOSITORY.md](../../standards/REPOSITORY.md). Fill per repository during Phase 4. Social preview has no API: manual upload in Settings | None; presentation only | Social preview: yes |
| CAP-02 | **Branch protection and rulesets** | CONFIGURED (classic, 32/33) | Classic rules on `development`, `runway`, `main`: pull request required, 0 approvals, required check `gate` (+ `review` on governance), force-push and deletion blocked, **admins enforced**. Rulesets: **0/72**. `jarvis-labs` has none | Rulesets give one auditable object per branch and tag rules; the policy engine already plans the migration ([tools/policy/](../../tools/policy/)). Let it do it, rather than by hand. Note the documentation drift on admin enforcement (GAP-M12) | A ruleset with no bypass removes the owner's emergency override — decide with DEC-P13 | Yes (P11, P13) |
| CAP-03 | **Pull request reviews and required checks** | CONFIGURED | `gate` required; automated Claude review is the reviewer of record; HOLD verdicts need owner approval | Keep. Approvals stay at 0 by design ([GOVERNANCE_HIERARCHY.md](../../GOVERNANCE_HIERARCHY.md)) | Each automated review costs money; volume-generating features (CAP-08) multiply it | — |
| CAP-04 | **Repository permissions** | CONFIGURED (single owner) | Sampled `account`, `auth`, `my_chatgpt`, `store`, `jarvis`: one collaborator each, the owner. Agents act through the owner's token or Jarvis's GitHub App | Keep. Agent access via App identity is already the [SECURITY.md](../../standards/SECURITY.md) direction | — | — |
| CAP-05 | **Teams and organisation access** | NOT CONFIGURED / BLOCKED | Organisation: 0 teams; two-factor requirement **off**; members can create repositories. Organisation settings beyond that need `admin:org` | Require 2FA; restrict repository creation (DEC-P02) | Requiring 2FA removes members without it — currently none known besides the owner | Yes |
| CAP-06 | **GitHub Actions and reusable workflows** | CONFIGURED | `claude-review.yml` 32/33, `pr-gate.yml` 29/33; canonical templates in `tools/policy/templates/`. Private-repository minutes have run out before (2026-10) | Prefer reusable workflows (`workflow_call`) from this repository over copied files where the action allows it — copied workflows drifted before. Note: the Claude review action must match the default-branch copy, which constrains this | Minutes on private repositories are finite | — |
| CAP-07 | **Environments and deployment protection** | CONFIGURED (by platforms) | 35/72 repositories have environments: `github-pages` 30, `copilot` 12, `Production` 3 — created by the platforms, not by governance | Add required reviewers or branch filters only where a deploy can harm (production backends). Not blanket | A reviewer on `github-pages` would stall every site deploy | — |
| CAP-08 | **Dependabot** — alerts, security updates, version updates | ENABLED (alerts 32/33) / NOT CONFIGURED (updates) | Alerts on 66/72. Security updates **off** everywhere. `dependabot.yml` in **0/72**. **1,674 open alerts** (detail withheld, DEC-007) | Version and security updates with `groups:` and `target-branch: development`, one repository at a time (DEC-P09) | Every update PR triggers a paid automated review | Yes |
| CAP-09 | **Dependency graph and dependency review** | ENABLED (graph, implied by alerts) / NOT CONFIGURED (review action) | Graph on wherever alerts work. No `dependency-review-action` anywhere | Add dependency review to the `runway` gate's `security` check rather than as a separate workflow | — | — |
| CAP-10 | **Secret scanning and push protection** | ENABLED (public 29/29 covered; 60/60 all public) | Was **off on `continuum`** — fixed 2026-11-18, 0 alerts found (LOG-005). Private repositories: NOT AVAILABLE without GitHub Secret Protection (paid) | Keep. Add "secret scanning on" to the onboarding verification step so a new repository cannot start without it | Push protection can block a push containing a test credential; that is the point | — |
| CAP-11 | **Code scanning (CodeQL)** | NOT CONFIGURED (0/60 public) | Default setup available, free, on every public repository. Private: NOT AVAILABLE without GitHub Code Security | Default setup on public repositories with application code (DEC-P08) | Adds a check and alerts; runs on Actions (free on public) | Yes |
| CAP-12 | **Security policy and private vulnerability reporting** | NOT CONFIGURED | `SECURITY.md` 1/33. Private vulnerability reporting **off on 60/60** public | `SECURITY.md` pointing at private reporting, in public repositories with live surfaces (DEC-P07) | Opens a channel outsiders can use. That is the purpose | Yes |
| CAP-13 | **Projects and issues** | BLOCKED (Projects) / CONFIGURED (issues) | Issues on; 10 open account-wide; an issue-triage workflow exists here. Projects cannot be read without `read:project` | Not needed for one owner; manifests and issues carry the work | — | Scope: P12 |
| CAP-14 | **Releases, tags, changelogs** | CONFIGURED where applicable | 7/72 have releases (`store`, `keyboard`, `memory-diary`, `my_chatgpt`, `ReWeb`, `gallery`, `music`) — the versioned consumables [DEPLOYMENT.md](../../standards/DEPLOYMENT.md) says should tag. Content sites correctly do not | Define a version scheme for consumables (GAP-E10) | — | — |
| CAP-15 | **Discussions and community** | NOT APPLICABLE | Discussions 0/72. Wiki **on** in 67/72 | Leave Discussions off. Turn wikis off: governance keeps documentation in the repository (`docs/`), and an unused wiki is an unreviewed place for content to appear | Turning a wiki off hides existing pages — check each is empty first | — |
| CAP-16 | **Packages** | BLOCKED | Needs `read:packages` | Measure after DEC-P12 | — | Scope: P12 |
| CAP-17 | **GitHub Pages** | CONFIGURED | 29 sites: 19 published by workflow (all 18 covered sites), 10 from a branch (all excluded or undecided) | Covered sites already meet [DEPLOYMENT.md](../../standards/DEPLOYMENT.md). Branch-published ones follow DEC-P01 | — | — |
| CAP-18 | **Custom properties and organisation rulesets** | BLOCKED | Organisation custom properties need `admin:org`; organisation rulesets returned 404 on the Free organisation | Custom properties would let `role`/`adoption` live on the repository and drive rulesets by property. Worth it only if the organisation becomes the ecosystem's home | — | P02, P12 |
| CAP-19 | **Audit log and insights** | NOT AVAILABLE (API) | Organisation audit-log API is Enterprise-only; the personal security log is UI-only | Evidence comes from git history, the CHANGELOG, workflow runs and this programme's measurements | — | — |
| CAP-20 | **Repository templates** | NOT CONFIGURED (0/72) | Onboarding uses the protocol's file templates, plus the policy engine's adoption pull requests | Not recommended: a template repository is copied once and drifts, which Article 3 treats as a defect. The engine's adoption pull request is the better mechanism | — | — |
| CAP-21 | **Codespaces and dev containers** | NOT APPLICABLE | Not in use | Not proportionate; work happens on the owner's machine and the VM | Costs on private repositories | — |
| CAP-22 | **Other settings found** | — | Auto-merge allowed 64/72. **Delete branch on merge: off 72/72** | Keep delete-on-merge **off**: contributor branches like `feature/claude` are persistent by design ([BRANCHING.md](../../standards/BRANCHING.md)); switching it on would delete them at every merge | — | — |
