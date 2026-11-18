# Implementation Roadmap

> **Record, not authority.** Order of work for the programme. Each item that changes a rule
> is its own pull request under [MAINTENANCE.md](../../MAINTENANCE.md); each item that
> changes a repository is scoped work under
> [protocols/REPOSITORY_ALIGNMENT.md](../../protocols/REPOSITORY_ALIGNMENT.md).

## How it is ordered

1. **Exposure first.** Live services carrying critical advisories outrank any document.
2. **Then what unblocks the most.** The policy engine automates manifests, rulesets and
   promotions across every repository; deploying it once is worth more than doing its work
   by hand thirty times.
3. **Small, reversible, separately reviewable steps.** No pull request changes more than one
   rule; no batch touches many repositories at once
   ([MAINTENANCE.md](../../MAINTENANCE.md) § Changing Governance Safely).
4. **Owner decisions do not stall independent work.** Each item names what it waits for.

Status values: `todo` · `doing` · `blocked (DEC-Pnn)` · `done (date, evidence)`.

---

## Wave 0 — Unblock (owner)

| ID | Item | Closes | Waits for | Status |
|---|---|---|---|---|
| RM-01 | Review and merge governance promotion PR #100, so `main` carries the policy engine; create the policy App and its two secrets; decide when `POLICY_APPLY` leaves dry-run | GAP-M04 | DEC-P11 | blocked (DEC-P11) |
| RM-02 | Answer membership for the 12 undecided repositories and the organisation | GAP-M01, A03, M13 | DEC-P01, DEC-P02 | blocked |
| RM-03 | Record those answers in `schemas/ecosystem.yaml`, correct the 6 stale adoption values, refresh `last_account_reconciliation` | GAP-M01, M02 | RM-02. Agent edits to the registry have been refused before; may need the owner to commit | blocked (RM-02) |

## Wave 1 — Exposure

| ID | Item | Closes | Waits for | Status |
|---|---|---|---|---|
| RM-04 | Triage open Dependabot alerts in covered repositories, **identity and personal-data services first**, then other live services, then the rest. One repository per pull request, on `feature/claude` → `development`, with the repository's own tests run | GAP-M06 | Nothing — repository work | todo |
| RM-05 | Private vulnerability reporting + `SECURITY.md` in public covered repositories with live surfaces | GAP-M07 | DEC-P07 | blocked (DEC-P07) |
| RM-06 | CodeQL default setup on public covered repositories with application code | GAP-M08 | DEC-P08 | blocked (DEC-P08) |
| RM-07 | Decide the excluded-but-live repositories | GAP-M17 | DEC-P10 | blocked (DEC-P10) |
| RM-08 | Organisation: require 2FA, restrict repository creation | GAP-M13 | DEC-P02 | blocked (DEC-P02) |

## Wave 2 — Make governance true again

Authority documents that describe a world that no longer exists are the most dangerous
documents in the repository: they are obeyed.

| ID | Item | Destination | Closes | Waits for | Status |
|---|---|---|---|---|---|
| RM-09 | Re-measure and correct "What Is Actually Enforced"; fix the `enforce_admins` statement; fix CONCERNS' "zero repositories have branch protection"; correct BRANCHING's claim that rulesets already replaced classic protection | `GOVERNANCE_HIERARCHY.md`, `CONCERNS.md`, `standards/BRANCHING.md` | GAP-M12 | — | doing — [PR #106](https://github.com/HarithKavish/harithkavish-governance/pull/106) |
| RM-10 | Onboarding verification includes the security baseline: Dependabot alerts on; secret scanning and push protection on (public repositories) | `protocols/REPOSITORY_ONBOARDING.md` step 9 | GAP-M14 | — | todo |

## Wave 3 — Phase 1 normative changes

Each is one pull request into this repository, classified in its description per the
template.

| ID | Item | Proposed destination | Closes | Waits for | Status |
|---|---|---|---|---|---|
| RM-11 | A public repository **declares** its licensing intent — a licence, or an explicit "all rights reserved" | Improve `standards/REPOSITORY.md` | GAP-M05, E04 | DEC-P03 (the rule can land before every repository's answer) | todo |
| RM-12 | Lifecycle statuses and data classifications given definitions and permitted transitions | Improve `standards/PROJECT.md` | GAP-D05, G02 | — | todo |
| RM-13 | Vulnerability response: what "treat advisories as work" requires, by severity, and how it is checked | Improve `standards/SECURITY.md` § Dependencies; crosswalk SSDF RV (REF-20) | GAP-E06, M06 | — | todo |
| RM-14 | Crosswalk SECURITY.md against NIST CSF 2.0 (REF-18); file what is missing in its proper destination | Analysis first; changes per finding | GAP-B05 | — | todo |
| RM-15 | **Operations**: service levels (commitment vs internal target, never invented), monitoring, backup with demonstrated restore, continuity and key-person risk | New `standards/OPERATIONS.md` — justified in its PR against all seven destinations | GAP-B06, B10, F03, F06, F08 | DEC-P06 informs one section; the rest can proceed | todo |
| RM-16 | **Incident and problem management**: declare, stabilise, record, review, feed findings into MAINTENANCE | New `protocols/INCIDENT.md`; security exposures keep SECURITY § Reporting's sequencing | GAP-F04 | RM-15 | todo |
| RM-17 | **Retiring a surface**: DNS, credentials revoked, personal data deleted or exported, repository archived, registry updated | New protocol; ISO/IEC/IEEE 12207 disposal (REF-15) as checklist | GAP-D07 | — | todo |
| RM-18 | Decision rights in one table: owner, coding agent, reviewing agent, Jarvis's App, policy engine | Classify in the PR — consolidation of rules now spread across five documents | GAP-A06 | — | todo |
| RM-19 | Platform-and-asset register: providers, plans, limits, costs, domains, signing keys, renewal dates — names and dates only, never secrets | Schema + a short rule; FinOps (REF-23) | GAP-G05, G06 | — | todo |
| RM-20 | **AI systems as products**: model choice, evaluation, autonomy limits, human oversight, logging, data sent to providers | New standard; ISO/IEC 42001 (REF-10) and NIST AI RMF (REF-19) as references | GAP-B09, H01 | DEC-P01 for `jarvis`, `hermes-agent` | blocked (DEC-P01) |
| RM-21 | Architecture review: when a change needs review beyond its diff | New protocol | GAP-C09 | RM-12 | todo |
| RM-22 | Organisation charter, mission, vision, values | Governance README | GAP-A01, A02 | DEC-P04 | blocked (DEC-P04) |
| RM-23 | Privacy obligations | Per DEC-P05 | GAP-B08, G04 | DEC-P05 | blocked (DEC-P05) |

## Wave 4 — Phase 2 and 3: baseline and GitHub configuration

| ID | Item | Closes | Waits for | Status |
|---|---|---|---|---|
| RM-24 | Repository baseline decided per class — which of `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `CHANGELOG.md`, `CITATION.cff`, `CODEOWNERS` apply to a content site, an app, a service, a library. **No boilerplate in repositories it does not fit** | Phase 2 | RM-11, RM-15 | todo |
| RM-25 | Rulesets via the policy engine, public repositories first | CAP-02 | RM-01 | blocked (RM-01) |
| RM-26 | Dependabot configuration (`groups:`, `target-branch: development`) one repository at a time | CAP-08 | DEC-P09 | blocked (DEC-P09) |
| RM-27 | Wikis off where empty | CAP-15 | Check each is empty | todo |
| RM-28 | Social previews | CAP-01, GAP-M09 | Owner (no API) | blocked (owner) |

## Wave 5 — Phase 4: per repository

Processed one at a time, highest exposure first. Each repository: audit → manifest
(`.project/`, drafted by the policy engine where live) → applicable baseline → settings →
verify its own build and deploy still work → pull request → registry and inventory updated.

**Order:** identity services (`account`, `auth`) → services storing personal data →
other live services and applications with released artifacts → live websites →
shared libraries → infrastructure → registered-only surfaces. Precise order is set from the
alert triage in RM-04 and kept off this public file (DEC-007).

Structural gaps (missing `feature/claude`, `runway`, protection, `pr-gate.yml`; GAP-M11) are
closed in each repository as a precondition the first time a task touches it, per
[AGENT_BOOTSTRAP.md](../../AGENT_BOOTSTRAP.md) step 7 — not as a separate sweep.

## Wave 6 — Phases 5 and 6

| ID | Item | Waits for | Status |
|---|---|---|---|
| RM-29 | Traceability identifiers across manifest components, requirements, decisions, releases and incidents — extending the manifest schema rather than inventing a parallel register | Manifests adopted (Wave 5) | todo |
| RM-30 | Delivery measures (DORA, REF-24) computed from GitHub data | A baseline | todo |
| RM-31 | Maturity assessment: ad hoc → documented → standardised → measured → optimised, per area A–H, with evidence | Waves 1–5 | todo |
| RM-32 | Re-run the inventory; compare with 2026-11-18 | Each wave | todo |
