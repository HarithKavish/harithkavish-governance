# Gap Register

> **Record, not authority.** A gap listed here is a finding. Closing one that needs a rule
> goes through [MAINTENANCE.md](../../MAINTENANCE.md) and lands in the destination
> [GOVERNANCE_MAP.md](../../GOVERNANCE_MAP.md) assigns — never in this folder.

Opened 2026-11-18. IDs are permanent: a closed gap keeps its ID and gains a closing date and
the evidence that closed it. IDs are never reused.

## How each requested area was judged

The programme brief asked for governance across eight areas (A–H). Each requested item was
checked against what this repository already says, **before** anything was proposed,
because restating an existing rule in a second place is the failure
[MAINTENANCE.md](../../MAINTENANCE.md) exists to prevent.

| Status | Meaning |
|---|---|
| **Covered** | Existing governance answers it. Nothing is added; the pointer is the answer. |
| **Partial** | It has a home, and the rule there is incomplete. Improve that document. |
| **Adoption** | The rule exists and repositories do not meet it yet. Repository work, not governance work. |
| **No home** | No document owns the concern. A new document may be justified, and must pass the map's tests in its own pull request. |
| **Owner** | Needs a fact or decision only the owner holds. An agent will not write it. |
| **Not now** | Deliberately not created: disproportionate for a one-owner ecosystem today. The trigger that would change this is named. |

The "not now" judgements rest on one fact about the ecosystem as measured: **one human
owner, AI agents acting under that owner's account, no outside contributors on any sampled
repository, and no contractual customers on record.** Several requested items — a quality
manual, a RACI across departments, a capability map — are tools for coordinating many people.
Building them for one person produces documents nobody needs to read, which this repository
treats as a cost, not a neutral act.

---

## A — Foundation

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-A01 | Organisational charter | Doctrine Art. 1 (authority), README (purpose of the governance repository) | Owner | A charter states why the organisation exists. That is the owner's to write; DEC-P04 |
| GAP-A02 | Mission, vision, values | None | Owner | DEC-P04. Destination when written: README (description), not the doctrine — the doctrine holds principles for repositories and actors, and a mission is neither |
| GAP-A03 | Scope and applicability | Art. 1, Art. 5; [GOVERNANCE_HIERARCHY.md](../../GOVERNANCE_HIERARCHY.md) § Scope; [AGENT_BOOTSTRAP.md](../../AGENT_BOOTSTRAP.md) step 3; `schemas/ecosystem.yaml` | Partial | Scope is defined as "the HarithKavish account". An organisation, `harithkavishtechnologies`, now holds live surfaces of the primary domain and sits outside that definition. DEC-P02, then sharpen REPOSITORY.md § Ecosystem Registry |
| GAP-A04 | Governance model | The five tiers; MAP / MAINTENANCE / HIERARCHY | Covered | — |
| GAP-A05 | Authority, ownership, accountability | HIERARCHY (owner override, recorded); `project.owner` in the manifest | Covered (rule) / Adoption (0/33 manifests) | — |
| GAP-A06 | Roles, responsibilities, RACI, decision authority | Scattered: BRANCHING (who merges where), SECURITY (one identity per actor), AGENT_ENVIRONMENT, HOLD approval in the release gate | Partial | The decision rights are real and are spread across five documents: owner, coding agent, reviewing agent, Jarvis's App identity, policy engine. Consolidate into one decision-rights table; classify its destination in that pull request. A department-style RACI is **not now** — trigger: a second human contributor |

## B — Management systems

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-B01 | Integrated management system structure | The tier model is the management system: principle → requirement → process → data, with document control | Covered | A separate IMS manual would restate it. **Not now** — trigger: a certification goal (DEC-003) |
| GAP-B02 | Policy and standards hierarchy | [GOVERNANCE_HIERARCHY.md](../../GOVERNANCE_HIERARCHY.md) | Covered | — |
| GAP-B03 | Document control and approval | MAINTENANCE (process, timestamp, append-only changelog), PR template, branch protection | Covered (rule) / Adoption | CODEOWNERS in 2/33 repositories; changelog append-only is rung 2. See GAP-M10 |
| GAP-B04 | Quality management | DEVELOPMENT (testing, review), BRANCHING release gate (`ci`, `sonar`, verifiers) | Partial | No quality objective is measured. Phase 6 proposes DORA-style delivery measures from GitHub data. A QMS manual: **not now** |
| GAP-B05 | Information security management | [standards/SECURITY.md](../../standards/SECURITY.md) (rung 2), manifests (`data`, `secrets`, `risks`) | Partial | Map SECURITY.md against NIST CSF 2.0 functions (REF-18) to find omitted areas rather than guess them. No ISMS certification (DEC-003) |
| GAP-B06 | Service management | None | No home | See GAP-F03/F04/F08: one operations standard plus an incident protocol is the smallest change that covers them |
| GAP-B07 | Risk and compliance management | Per-repository `.project/risks.md` | Partial | Nothing collects risk across repositories, or says how risk is rated. Ecosystem-level register: classify in its own pull request (data → schema; method → standard) |
| GAP-B08 | Privacy | SECURITY § Data (minimisation), IDENTITY (what an application may hold), manifest `data[].classification` includes `personal` | Partial / Owner | Which privacy law applies depends on the owner's jurisdiction and users' locations, neither recorded (DEC-P05). Until then, governance can require only what it already does |
| GAP-B09 | AI governance | AGENT_ENVIRONMENT, AGENT_METHOD, SECURITY § Agents — agents **as actors** | Partial | Nothing governs AI systems **as products**: model choice, evaluation, autonomy limits, human oversight, logging, data sent to model providers. The ecosystem runs such systems (an assistant with autonomy policy, a model router). Blocked on DEC-P01 for `jarvis` and `hermes-agent`; reference REF-17, REF-19 |
| GAP-B10 | Business continuity | None. Manifest `verify.rollback` covers deploy rollback only | No home | Fold into the operations standard: backup, verified restore, key-person and lockout risk (single owner; single private network path to the VM) |

## C — Enterprise architecture

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-C01 | Architecture principles | Doctrine Arts. 3, 4, 6, 7; IDENTITY § The Three Roles | Covered | — |
| GAP-C02 | Business and organisational architecture | None | Not now | Trigger: more than one team or line of business |
| GAP-C03 | Information and data architecture | IDENTITY (who owns which identity data); manifest `data` | Partial / Adoption | An ecosystem data view is derivable from manifests once they exist (GAP-M03). Not written by hand |
| GAP-C04 | Application and software architecture | `.project/architecture.md` per repository | Covered (rule) / Adoption (0/33) | — |
| GAP-C05 | Infrastructure and technology architecture | Manifest `infra` (Cloudflare, Vercel, Pages, Atlas, Render, Android, Oracle VM) | Covered (rule) / Adoption | As GAP-C03 |
| GAP-C06 | Integration, security, identity architecture | IDENTITY, SECURITY | Covered | — |
| GAP-C07 | Current, target, transition architecture | IDENTITY § Current State / § Getting There; DEPLOYMENT § Known Gap | Partial | Exists per concern, which is the right grain. No ecosystem-wide target view is needed until manifests make one derivable |
| GAP-C08 | Architecture decision records | `.project/decisions.md` per repository; CHANGELOG for governance | Covered (rule) / Adoption | — |
| GAP-C09 | Architecture review procedure | The code reviewer checks a diff against manifest `scope` and `components` | No home | GOVERNANCE_MAP names "architecture review" as an example protocol, and none exists. Candidate protocol: when a change needs review beyond the diff (new component, new platform, new data class) |

## D — Portfolio and lifecycle

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-D01 | Product, service, project governance | Registry (membership), manifest (everything else) | Covered | — |
| GAP-D02 | Business capability register | None | Not now | Trigger: products overlapping enough that a capability view would prevent duplicate builds. Today DESIGN_SYSTEM's cross-surface check does that job for UI |
| GAP-D03 | System and application inventory | Registry + manifests; this programme's [inventory](REPOSITORY-INVENTORY.md) | Covered (rule) / Adoption | — |
| GAP-D04 | Feature and requirements registers | Manifest `scope.covers` / `scope.excludes`; issues | Partial | Requirement-level IDs are Phase 5 (traceability); proposed there, not here |
| GAP-D05 | Lifecycle definitions | Manifest `project.status`: `active`, `maintenance`, `frozen`, `archived`, `exercise`; registry `adoption: retired` | Partial | The values exist; their meanings and permitted transitions are not written. Improve [standards/PROJECT.md](../../standards/PROJECT.md) |
| GAP-D06 | Roadmap and prioritisation | Per-repository issues | Not now (centrally) | Repository-specific by the map's own test |
| GAP-D07 | Deprecation and retirement | Registry `retired`; MAINTENANCE § Retiring Rules (rules only) | No home | Nothing says how a **surface** is retired: DNS, credentials revoked, stored personal data deleted or exported, repository archived, registry updated. One retirement has already happened (`harith-design-system`). Candidate protocol |

## E — Engineering

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-E01 | SDLC | BRANCHING, DEVELOPMENT, DEPLOYMENT, PROJECT | Covered | — |
| GAP-E02 | Requirements engineering | Manifest `scope`; issue triage | Partial | See GAP-D04 |
| GAP-E03 | Coding conventions | DEVELOPMENT (principles); language conventions are repository-specific by the map's test | Covered | — |
| GAP-E04 | Repository conventions | [standards/REPOSITORY.md](../../standards/REPOSITORY.md) | Partial | Licensing is not addressed at all (GAP-M05) |
| GAP-E05 | Testing and QA | DEVELOPMENT § Testing; release gate `ci`, `sonar` | Covered | — |
| GAP-E06 | Secure development | SECURITY; release gate `security` | Partial | Vulnerability **response** is unstated: "treat advisories as work" has no expectation of time or triage, and 1,674 alerts are open (GAP-M06). Map against SSDF RV practices (REF-20) |
| GAP-E07 | CI/CD | BRANCHING gates; DEPLOYMENT; `schemas/policy.yaml` | Covered (rule) / Adoption | The policy engine that enforces it is undeployed (GAP-M04) |
| GAP-E08 | Configuration management | DEVELOPMENT § Configuration and Environments; manifest | Covered | — |
| GAP-E09 | Change and release management | BRANCHING § The Release Gate; DEPLOYMENT § Releases And Artifacts | Covered | — |
| GAP-E10 | Dependency and version management | DEVELOPMENT and SECURITY § Dependencies | Partial | No version scheme for versioned consumables (DEPLOYMENT requires tags, not their form); no Dependabot configuration anywhere |

## F — Service and operations

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-F01 | Service catalogue | Registry `surface`; manifest `surface` per stage | Partial | Derivable from manifests; not hand-written |
| GAP-F02 | Service ownership | `project.owner` | Covered | — |
| GAP-F03 | SLA / SLO / SLI / OLA framework | None | No home / Owner | A framework that **distinguishes a commitment from an internal target** and forbids inventing either. Whether any commitment exists is DEC-P06; until answered there are no SLAs, only proposed SLOs |
| GAP-F04 | Incident and problem management | SECURITY § Reporting (security exposures only); BRANCHING § Hotfix | No home | Operational incidents have happened and were handled without a record format or review. Candidate protocol: declare, stabilise, record, review, feed findings to MAINTENANCE |
| GAP-F05 | Service requests | None | Not now | Trigger: a surface with outside users who can ask for something |
| GAP-F06 | Monitoring and observability | Manifest `surface.health`; the `live-surface` verifier at release | Partial | Checked at release, not continuously. Operations standard |
| GAP-F07 | Support and escalation | None (`SUPPORT.md` in 0/72) | Not now | Same trigger as GAP-F05 |
| GAP-F08 | Backup, recovery, disaster recovery | None | No home | At least one loss of local agent data with no backup is on record (2026-10-15). Operations standard: what is backed up, where, and that restore has been **demonstrated** |
| GAP-F09 | Operational runbooks | Repository `docs/` (6/33) | Covered (rule: repository-specific) | — |

## G — Organisational controls

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-G01 | Cybersecurity and access control | SECURITY (one identity per actor, least privilege), IDENTITY | Partial | The organisation does not require two-factor authentication (GAP-M13) |
| GAP-G02 | Data classification | Manifest `data[].classification`: `public`, `internal`, `personal`, `sensitive`, `secret` | Covered (rule) / Adoption | The five values have no written definitions. Improve PROJECT.md alongside GAP-D05 |
| GAP-G03 | Enterprise risk | See GAP-B07 | Partial | — |
| GAP-G04 | Legal and regulatory compliance | None | Owner | Jurisdiction (DEC-P05) and licensing intent (DEC-P03). Third-party licence compatibility of dependencies is unchecked |
| GAP-G05 | Vendor and contract management | Manifest `infra` names platforms per repository | Partial | No ecosystem view of suppliers, plans, limits and exit paths. Limits have already caused outages: Actions minutes exhausted (2026-10); a database quota on one hosting account blocked every database on it |
| GAP-G06 | Financial and asset management | None | No home | Assets that matter — domains, signing keys, provider accounts — and recurring costs, including the per-review cost of automated review. Proportionate form: one platform-and-asset register, FinOps-informed (REF-23) |
| GAP-G07 | Audit and evidence management | CHANGELOG; HIERARCHY § What Is Actually Enforced (measured 2026-09-05) | Partial | The enforcement measurement is a one-off and is now wrong in places (GAP-M12). Needs a cadence; the policy engine's dry run is the natural source |
| GAP-G08 | Knowledge management | CONCERNS.md; AGENT_ENVIRONMENT § What The Agent Has Learned; repository docs | Covered | — |
| GAP-G09 | Organisational performance | None | Not now → Phase 6 | DORA measures from GitHub data (REF-24) once there is a baseline to compare against |
| GAP-G10 | Continual improvement | MAINTENANCE § Where Changes Come From | Covered | — |

## H — Future readiness

| ID | Requested | Existing coverage | Status | Proposed action |
|---|---|---|---|---|
| GAP-H01 | AI system governance | See GAP-B09 | Partial | — |
| GAP-H02 | Research and innovation | Workbench and lab repositories exist | Not now | — |
| GAP-H03 | Technology evaluation | DEVELOPMENT ("adding a dependency is a decision"); AGENT_METHOD § 4 | Covered | — |
| GAP-H04 | Scalability and modernisation | None | Not now | Repository-specific |
| GAP-H05 | Sustainability and lifecycle planning | Lifecycle values (GAP-D05) | Partial | — |

---

## M — Measured gaps (from the 2026-11-18 inventory)

These are facts about the ecosystem as it is, not about the documents.

| ID | Finding | Evidence | Action | Priority | Owner needed |
|---|---|---|---|---|---|
| GAP-M01 | 12 repositories have no membership decision; 3 sit in an organisation the registry's scope does not cover | [Inventory](REPOSITORY-INVENTORY.md#undecided-membership) | DEC-P01, DEC-P02, then registry PR | High | Yes |
| GAP-M02 | Registry adoption values out of date in 6 entries | [Inventory](REPOSITORY-INVENTORY.md#registry-drift) | Registry correction PR | Low | Registry edits by agents have been refused before; may need the owner |
| GAP-M03 | `.project/project.yaml` in 0 of 33 covered repositories | Inventory `Gov` column | Policy engine adoption PRs draft them (GAP-M04) | High | No |
| GAP-M04 | The policy engine is built and not running. `main` is 20 commits behind `development`; the promotion PR #100 has been open since 2026-10-28; no policy App or its credentials exist; `POLICY_APPLY` is dry-run | Branch comparison; PR list | DEC-P11 | High | Yes |
| GAP-M05 | No licence in 71 of 72 repositories; the one present is unrecognised (`NOASSERTION`). REPOSITORY.md does not mention licensing | Inventory | DEC-P03, then improve REPOSITORY.md: a public repository **declares** its licensing intent, whatever it is | Medium | Yes |
| GAP-M06 | 1,674 open Dependabot alerts in 19 repositories (76 critical); 462 (23 critical) in covered repositories. Security updates disabled everywhere; no `dependabot.yml` anywhere | Dependabot API, paginated. Per-repository detail withheld from this public file (DEC-007) | Repository remediation, identity and personal-data services first; DEC-P09 for automation | **Highest** | For automation only |
| GAP-M07 | Private vulnerability reporting off on all 60 public repositories; `SECURITY.md` in 1 of 33. An outside finder has no documented private route | API | DEC-P07 | High | Yes |
| GAP-M08 | CodeQL default setup not configured on any of 60 public repositories, where it is free | API | DEC-P08 | Medium | Yes |
| GAP-M09 | Custom social preview in 0 of 33 covered (2 of 72 overall); required since 2026-08-28. No API exists for the upload | GraphQL `usesCustomOpenGraphImage` | Manual, owner | Low | Yes |
| GAP-M10 | CODEOWNERS in 2 of 33 | Inventory | Repository work; only meaningful once there is someone other than the owner to route review to | Low | No |
| GAP-M11 | Branch topology incomplete: `feature/claude` missing in 8 covered repositories; `jarvis-labs` has no `runway` and no protection; `pr-gate.yml` missing in 4 covered. BRANCHING § Every Repository requires the branches and protection on **every** repository the account owns; 4 personal repositories have no protection (`gallery`, `interstellar`, `temp-poem-site`, `jarvis-labs`) | Inventory | Established per repository when a task touches it ([AGENT_BOOTSTRAP.md](../../AGENT_BOOTSTRAP.md) step 7) | Medium | No |
| GAP-M12 | Authority documents describe enforcement that no longer matches reality. HIERARCHY says `enforce_admins` is off — it is on in every protected repository (32 of 33 covered; 65 of 65 account-wide). CONCERNS says "Zero repositories have branch protection" — 65 of 72 have it | Protection API | Correct both under MAINTENANCE. The intent is not in question: BRANCHING § Bypass records the owner's no-bypass decision of 2026-10-15, and reality matches it. Also stale: BRANCHING says rulesets from the policy engine replaced classic protection on 2026-10-15 — there are 0 rulesets, because the engine has not run (GAP-M04) | High — "dead governance is worse than missing governance" | No |
| GAP-M13 | Organisation `harithkavishtechnologies`: two-factor requirement off, any member may create repositories, no teams, no rulesets visible | Org API | DEC-P02 | Medium | Yes |
| GAP-M14 | Newly created repositories miss baseline security settings. `continuum` had secret scanning and push protection off (the only public repository of 60), and the six newest repositories had Dependabot alerts off. Nothing checks a new repository's security settings at creation | API | **Settings fixed 2026-11-18** (LOG-005, LOG-008). The cause stays open until onboarding checks it (RM-10) | Low (settings) / Medium (cause) | No |
| GAP-M15 | 54 open pull requests account-wide; 6 in this repository, the oldest from 2026-10-16 | PR API | DEC-P11 | Medium | Yes |
| GAP-M16 | 10 repositories publish Pages from a branch, all excluded or undecided | Pages API | Follows DEC-P01; excluded repositories are exempt from DEPLOYMENT | Low | Via DEC-P01 |
| GAP-M17 | Excluded repositories that are public, vulnerable, and in one case live | Inventory § Excluded, but exposed | DEC-P10 | High | Yes |
