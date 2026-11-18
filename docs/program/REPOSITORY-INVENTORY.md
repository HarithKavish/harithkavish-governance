# Repository Inventory — snapshot 2026-11-18

> **Record, not authority.** Membership and role are decided in
> [schemas/ecosystem.yaml](../../schemas/ecosystem.yaml); everything else about a project
> is declared in its own `.project/project.yaml` ([standards/PROJECT.md](../../standards/PROJECT.md)).
> This file is a dated measurement of what GitHub reported on the day. Where it disagrees
> with the registry, that disagreement is a finding in [GAP-REGISTER.md](GAP-REGISTER.md),
> not a correction to the registry.

## How it was measured

Read-only `gh` queries against every repository the authenticated account can reach
(`user/repos?affiliation=owner,collaborator,organization_member`, paginated), using
[collect_inventory.py](collect_inventory.py). No setting or file was changed by the
collection. Per repository: GraphQL metadata (visibility, default branch, languages,
licence, topics, branches, classic protection rules, releases, tags, open issues and pull
requests, presence of governance files on the default branch and on `development`) and
REST settings (security and analysis, rulesets, Pages, private vulnerability reporting,
CodeQL default setup, environments, open Dependabot alerts, paginated).

**Not measurable with the current token** — needs scopes only the owner can grant
(`gh auth refresh -s admin:org,read:project,read:packages,user`): the personal account's
plan, organisation custom properties and organisation rulesets, Projects, Packages.

## Totals

| | Count |
|---|---|
| Repositories reachable | **72** — 69 under `HarithKavish`, 3 under the organisation `harithkavishtechnologies` |
| Visibility | 60 public · 12 private |
| Registry: covered | 33 (6 `integrated`, 27 `registered`) |
| Registry: excluded | 27 |
| Registry: **undecided** (in neither list) | **12** — see [below](#undecided-membership) |
| In the registry but not found on GitHub | 0 |
| Archived · forks · templates | 0 · 0 · 0 |
| Open Dependabot alerts (all 72) | **1,674** in 19 repositories — 76 critical, 673 high |
| Open Dependabot alerts (covered 33) | **462** in 13 repositories — 23 critical |

**Per-repository vulnerability detail is deliberately not published here.** This repository
is public, and a table of which live services carry unpatched critical advisories is the
kind of exposure [standards/SECURITY.md](../../standards/SECURITY.md) § Reporting keeps out
of public view. The owner sees it in each repository's Security tab; it was reported to the
owner directly (DEC-007).

## Legend

- **Gov** — `A` `AGENTS.md`, `G` `GOVERNANCE.md`, `P` `.project/project.yaml`, on the default
  branch or `development`; `·` absent.
- **Branches** — `D` `development`, `R` `runway`, `F` `feature/claude`; `·` absent.
- **BPR** — number of classic branch protection rules. No repository has a ruleset.
- **Pages** — `workflow` (published by a workflow), `legacy` (published from a branch), `–` none.
- **ID** — GitHub's numeric repository id. It survives renames, so it is the stable key for
  traceability; `owner/name` is the readable key.
- **Lifecycle** is not shown: no repository yet declares `project.status` in a manifest, and
  this inventory does not infer one.

| Repository | ID | Registry | Role | Vis | Default | Language | Last push | Gov | Branches | BPR | Pages | Releases |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `HarithKavish/diary` | 1363519614 | integrated | website | public | development | TypeScript | 2026-10-14 | AG· | DRF | 3 | workflow | 0 |
| `HarithKavish/forge-gateway` | 1366541482 | integrated | service | public | development | TypeScript | 2026-10-14 | AG· | DRF | 3 | – | 0 |
| `HarithKavish/harithkavish-governance` | 1349310541 | integrated | governance | public | main | Shell | 2026-11-17 | ··· | DRF | 3 | – | 0 |
| `HarithKavish/keyboard` | 1393634056 | integrated | application | public | development | Java | 2026-10-16 | AG· | DRF | 3 | – | 1 |
| `HarithKavish/mcp-registry-mcp-server` | 1124905831 | integrated | service | public | development | JavaScript | 2026-10-20 | AG· | DRF | 3 | – | 0 |
| `HarithKavish/memory-diary` | 1373004221 | integrated | application | public | development | TypeScript | 2026-11-03 | AG· | DRF | 3 | – | 4 |
| `HarithKavish/about` | 1159563352 | registered | website | public | development | CSS | 2026-10-09 | ·G· | DRF | 3 | workflow | 0 |
| `HarithKavish/account` | 1330199118 | registered | application | public | development | TypeScript | 2026-10-31 | A·· | DRF | 3 | – | 0 |
| `HarithKavish/admin` | 1354772229 | registered | application | public | development | JavaScript | 2026-10-08 | AG· | DR· | 3 | workflow | 0 |
| `HarithKavish/agent-toolkit` | 1376173802 | registered | infrastructure | private | development | Python | 2026-10-23 | AG· | DRF | 3 | – | 0 |
| `HarithKavish/ai-lab` | 1120665077 | registered | application | public | development | JavaScript | 2026-10-18 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/api` | 1163496614 | registered | website | public | development | HTML | 2026-10-08 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/auth` | 1330539666 | registered | service | public | development | TypeScript | 2026-10-31 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/blog` | 1170130397 | registered | website | public | development | HTML | 2026-10-15 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/converse` | 1115316102 | registered | application | public | development | JavaScript | 2026-10-08 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/design-system` | 1348916106 | registered | shared-library | public | development | JavaScript | 2026-10-08 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/forge` | 1329820403 | registered | application | public | development | TypeScript | 2026-10-26 | ··· | DRF | 3 | – | 0 |
| `HarithKavish/harith-lab` | 1022640506 | registered | application | private | development | CSS | 2026-10-08 | ··· | DRF | 3 | – | 0 |
| `HarithKavish/HarithKavish` | 529572116 | registered | website | public | development | CSS | 2026-10-10 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/harithkavish.github.io` | 1010176525 | registered | website | public | development | JavaScript | 2026-10-19 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/jarvis-labs` | 1435433895 | registered | infrastructure | private | development | — | 2026-10-30 | AG· | D·F | 0 | – | 0 |
| `HarithKavish/my_chatgpt` | 1152451892 | registered | application | private | development | TypeScript | 2026-10-31 | ··· | DRF | 3 | – | 11 |
| `HarithKavish/nexus` | 1328774348 | registered | website | public | development | HTML | 2026-11-13 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/realmora` | 1356278699 | registered | application | public | development | HTML | 2026-10-10 | AG· | DRF | 3 | – | 0 |
| `HarithKavish/ReWeb` | 1334012866 | registered | application | public | development | Kotlin | 2026-10-19 | ··· | DRF | 3 | – | 1 |
| `HarithKavish/search` | 1282390637 | registered | website | public | development | JavaScript | 2026-10-08 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/secrets-vault` | 1367075891 | registered | infrastructure | public | development | PowerShell | 2026-09-17 | ··· | DRF | 3 | – | 0 |
| `HarithKavish/sites` | 1175855952 | registered | website | public | development | HTML | 2026-10-19 | ··· | DR· | 3 | workflow | 0 |
| `HarithKavish/store` | 1179049282 | registered | website | public | development | Kotlin | 2026-10-16 | ··· | DRF | 3 | workflow | 2 |
| `HarithKavish/Timeline` | 1340673880 | registered | application | public | development | TypeScript | 2026-10-08 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/vm` | 1327975606 | registered | application | public | development | TypeScript | 2026-10-10 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/vr` | 1328282171 | registered | website | public | development | TypeScript | 2026-10-20 | ··· | DRF | 3 | workflow | 0 |
| `HarithKavish/vr-engine` | 1296862404 | registered | service | public | development | Python | 2026-10-08 | ··· | DRF | 3 | – | 0 |
| `HarithKavish/continuum` | 1441216513 | UNDECIDED | — | public | development | TypeScript | 2026-11-13 | AG· | DRF | 3 | workflow | 0 |
| `HarithKavish/gallery` | 1421775671 | UNDECIDED | — | private | development | Java | 2026-11-13 | AG· | D·F | 0 | – | 1 |
| `HarithKavish/hermes-agent` | 1361873026 | UNDECIDED | — | private | main | Python | 2026-11-06 | A·· | ··F | 1 | – | 0 |
| `HarithKavish/interstellar` | 1417318811 | UNDECIDED | — | public | main | HTML | 2026-10-13 | ··· | ··· | 0 | legacy | 0 |
| `HarithKavish/jarvis` | 1360577577 | UNDECIDED | — | private | development | Python | 2026-11-13 | ··· | DRF | 3 | – | 0 |
| `HarithKavish/music` | 1398584208 | UNDECIDED | — | private | development | Java | 2026-11-03 | AG· | DRF | 3 | – | 1 |
| `HarithKavish/newsfeed-timeline` | 1398471866 | UNDECIDED | — | public | development | Kotlin | 2026-11-01 | AG· | DRF | 3 | – | 0 |
| `HarithKavish/task-broker` | 1374243734 | UNDECIDED | — | public | development | PowerShell | 2026-10-31 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/temp-poem-site` | 1411460866 | UNDECIDED | — | public | master | HTML | 2026-10-11 | ··· | ··· | 0 | legacy | 0 |
| `harithkavishtechnologies/dashboard` | 1421095764 | UNDECIDED | — | private | main | JavaScript | 2026-10-15 | ··· | ··· | 0 | – | 0 |
| `harithkavishtechnologies/login` | 1421058991 | UNDECIDED | — | private | main | JavaScript | 2026-10-15 | ··· | ··· | 0 | – | 0 |
| `harithkavishtechnologies/miracleexim` | 1416707156 | UNDECIDED | — | private | main | TypeScript | 2026-10-18 | ··· | ··· | 0 | – | 0 |
| `HarithKavish/AgroCloud-Finance-Pro` | 748950893 | excluded | — | public | development | Java | 2026-10-30 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/Algorithms` | 786211454 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/copilot_test_for_auto-create_auto-push_and_auto-deploy_in_github_pages` | 1010022294 | excluded | — | public | development | CSS | 2026-10-11 | ··· | DR· | 3 | legacy | 0 |
| `HarithKavish/d1_p1-Welcome` | 604768020 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d1_p2-Name` | 604770418 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d1_p3-Color_Game` | 604772503 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d2_p1-Value_Annotation` | 604775684 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d3_p1-Get_Post` | 605938335 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d4_p1-Put_Delete` | 605971314 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d5_p1-CRUD_Operations` | 609279559 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/d6_p1-Pagination_And_Sorting-` | 609283805 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/eg1-hello` | 604497305 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/eg2-message_controller` | 604778101 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/eg3-student_getter_setter` | 604781079 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/eg4-Get_Post_Put_Delete` | 605980584 | excluded | — | public | development | Java | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/Hands-on_-_Cloud_Computing_using_AWS` | 631667186 | excluded | — | public | development | — | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/Hands-on_-_Software_Testing_using_Selenium` | 636071461 | excluded | — | public | development | Java | 2026-10-09 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/jarvis-github-control` | 1341690229 | excluded | — | public | development | CSS | 2026-10-08 | ··· | DR· | 3 | legacy | 0 |
| `HarithKavish/Land-Sale-Website` | 1019027260 | excluded | — | private | development | JavaScript | 2026-10-08 | ··· | DR· | 3 | legacy | 0 |
| `HarithKavish/megha_malar_dance_academy` | 1191707863 | excluded | — | public | development | HTML | 2026-10-19 | ··· | DR· | 3 | legacy | 0 |
| `HarithKavish/Multi-Object-Detection-using-YOLO` | 820577193 | excluded | — | public | development | Python | 2026-10-15 | ··· | DRF | 3 | legacy | 0 |
| `HarithKavish/name-to-horizontal-and-vertical-names-using-numbers` | 529642673 | excluded | — | public | development | Python | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/Online-Tutoring-Platform` | 663814895 | excluded | — | public | development | JavaScript | 2026-10-08 | ··· | DR· | 3 | legacy | 0 |
| `HarithKavish/Road-Contract-App` | 611180227 | excluded | — | public | development | JavaScript | 2026-10-08 | ··· | DR· | 3 | legacy | 0 |
| `HarithKavish/Script_-_First_Terminal_App` | 529596651 | excluded | — | public | development | Python | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/Script_-_Project_Akio` | 529853463 | excluded | — | public | development | Python | 2026-10-08 | ··· | DR· | 3 | – | 0 |
| `HarithKavish/SkinNet-Analyzer` | 957780408 | excluded | — | public | development | Python | 2026-10-26 | ··· | DR· | 3 | legacy | 0 |

## Undecided membership

Twelve repositories are in neither registry list. Under Article 5 that is an open
question, resolved by asking the owner
([protocols/REPOSITORY_ALIGNMENT.md](../../protocols/REPOSITORY_ALIGNMENT.md) § Phase 0).
The column on the right is **a recommendation from the evidence, not a decision** — it is
tracked as DEC-P01 and DEC-P02 in [DECISIONS.md](DECISIONS.md).

| Repository | Evidence | Recommended |
|---|---|---|
| `HarithKavish/continuum` | Public, live at `continuum.harithkavish.com`, `AGENTS.md` + `GOVERNANCE.md`, full branch set and protection. Registration already proposed in governance PR #103 | covered · website · integrated |
| `HarithKavish/gallery` | Private Android app with `AGENTS.md` + `GOVERNANCE.md`, a release | covered · application · integrated |
| `HarithKavish/music` | Private Android app with `AGENTS.md` + `GOVERNANCE.md`, a release, full branch set and protection | covered · application · integrated |
| `HarithKavish/newsfeed-timeline` | Public Android app with `AGENTS.md` + `GOVERNANCE.md`; onboarded 2026-09-30 but the registration step was refused to the agent doing it | covered · application · integrated |
| `HarithKavish/jarvis` | Private GitOps repository for the Jarvis agent system; full branch set and protection, no `AGENTS.md`/`GOVERNANCE.md` | covered · infrastructure · registered |
| `HarithKavish/task-broker` | Public local tool delegating agent subtasks; `development` + `runway`, protected | covered · infrastructure · registered |
| `HarithKavish/hermes-agent` | Private copy of an upstream project carrying Jarvis patches; upstream history on `main`, 34 inherited workflows (disabled for Actions minutes). The branch flow cannot apply as written | owner decision — covered with a declared branching exception, or excluded with a note |
| `HarithKavish/interstellar` | Public static site, Pages from a branch, no branch set | owner decision — website or excluded |
| `HarithKavish/temp-poem-site` | Public, described as temporary, Pages from a branch | excluded |
| `harithkavishtechnologies/login` | Private; serves `harithkavish.com/login` (Cloudflare Worker + D1) | covered, **once DEC-P02 brings the organisation into scope** |
| `harithkavishtechnologies/dashboard` | Private; serves `harithkavish.com/dashboard` (Cloudflare Worker + D1) | as `login` |
| `harithkavishtechnologies/miracleexim` | Private, no description, TypeScript, one workflow. Purpose and ownership of the work are not evident from the repository | owner decision — the inventory cannot classify it |

## Registry drift

Facts on GitHub that the registry does not reflect. Each is a correction to propose under
[MAINTENANCE.md](../../MAINTENANCE.md), not something this inventory changes.

| Repository | Registry says | GitHub shows |
|---|---|---|
| `realmora`, `admin`, `agent-toolkit`, `jarvis-labs` | `registered` | `AGENTS.md` and `GOVERNANCE.md` present → meets `integrated` |
| `account` | `registered` | `AGENTS.md` only |
| `about` | `registered` | `GOVERNANCE.md` only |
| registry header | `last_account_reconciliation: 2026-09-06` | 12 repositories created or left unrecorded since |
| registry scope | "every repository under the HarithKavish account" | an organisation, `harithkavishtechnologies`, created 2026-10-13, holds live surfaces of the primary domain |

## Excluded, but exposed

Exclusion lifts the repository rules, not the risk. Five excluded repositories are public
and carry open Dependabot alerts, including critical ones, and at least one of them,
`SkinNet-Analyzer`, serves a live surface used from `harithkavish.com`. Whether a live,
public, vulnerable repository should stay outside the repository rules is DEC-P10.
