# Execution State — Governance Establishment Programme

> **Start here to continue the programme.** This folder holds the programme's records.
> They carry **no authority**: rules live only in the doctrine, `standards/`, `protocols/`
> and `schemas/`, and change only through [MAINTENANCE.md](../../MAINTENANCE.md) (DEC-001).
> Read [AGENT_BOOTSTRAP.md](../../AGENT_BOOTSTRAP.md) before acting on anything here.

**Last updated:** 2026-11-18 · Claude (agent) · initiated by HarithKavish

## The programme

The owner issued a brief on 2026-11-18 to establish governance and enterprise architecture
across every repository the account can reach: discovery, a complete governance framework
in this repository, a universal repository baseline, GitHub configuration, per-repository
adoption, traceability, and a maturity review — Phases 0 to 6.

This repository already had most of the framework the brief describes. The programme
therefore extends what exists, through the existing change process, rather than writing a
parallel one (DEC-002). The brief's own principles — preserve valid rules, avoid duplication,
stay proportionate — ask for the same.

## Records

| File | Holds |
|---|---|
| [REPOSITORY-INVENTORY.md](REPOSITORY-INVENTORY.md) | All 72 reachable repositories, measured 2026-11-18 |
| [GAP-REGISTER.md](GAP-REGISTER.md) | Every requested area judged against existing governance; measured gaps |
| [DECISIONS.md](DECISIONS.md) | Decisions made, and the 13 waiting on the owner |
| [IMPLEMENTATION-ROADMAP.md](IMPLEMENTATION-ROADMAP.md) | Ordered work, waves 0–6 |
| [STANDARDS-REGISTER.md](STANDARDS-REGISTER.md) | External references, their status on 2026-11-18, and proposed use |
| [GITHUB-CAPABILITY-MATRIX.md](GITHUB-CAPABILITY-MATRIX.md) | 22 GitHub capabilities: available, used, recommended |
| [IMPLEMENTATION-LOG.md](IMPLEMENTATION-LOG.md) | What was done, with evidence |
| [collect_inventory.py](collect_inventory.py) | The read-only collector behind the inventory |

## Phase status

| Phase | Status | Evidence / what remains |
|---|---|---|
| 0 — Discovery | **Done** 2026-11-18 | Inventory complete for what the token can see; Projects, Packages and organisation properties need scopes (DEC-P12) |
| 1 — Governance repository | **Analysis done; normative changes not started** | Gap register, decisions, standards register written. Rule changes are RM-09 to RM-23, one pull request each |
| 2 — Repository baseline | Not started | RM-24, after RM-11 and RM-15 define what the baseline must say |
| 3 — GitHub capabilities | **Assessed**; one setting changed (LOG-005) | Remaining configuration waits on DEC-P07, P08, P09, P11, P13 |
| 4 — Per-repository adoption | Not started | Wave 5; starts with RM-04 (vulnerability triage), which needs no decision |
| 5 — Traceability | Not started | RM-29 needs manifests adopted first |
| 6 — Verification and maturity | Not started | RM-30 to RM-32 |

## Blockers

1. **Thirteen owner decisions** ([DECISIONS.md](DECISIONS.md) § Pending). The five that
   unblock most: DEC-P11 (merge the policy-engine promotion), DEC-P01/P02 (membership),
   DEC-P07 (private vulnerability reporting), DEC-P13 (admin enforcement intent).
2. **Merging is the owner's.** Agents may open pull requests but merges of unreviewed or
   held pull requests are refused to them, and HOLD verdicts need the owner's approval.
3. **Registry and changelog edits** have previously been refused to agents as a safety
   measure — those files steer every later session. Expect RM-03 to need the owner's hand.
4. **Token scopes** for the parts of Phase 0 and 3 that could not be measured (DEC-P12).

## Next actions, in order

For the next session — human or agent. Each is independent of owner decisions unless marked.

1. Check the pull request that added this folder; if merged, update LOG-006 with its number.
2. **RM-09** — correct the enforcement facts in `GOVERNANCE_HIERARCHY.md` § What Is
   Actually Enforced and `CONCERNS.md` from a fresh measurement; leave the `enforce_admins`
   *intent* to DEC-P13 and say so in the text.
3. **RM-10** — add the security baseline to onboarding step 9.
4. **RM-04** — begin vulnerability triage in the identity services, one repository per
   pull request, tests run, results reported honestly.
5. **RM-12** — definitions for lifecycle statuses and data classifications in
   `standards/PROJECT.md`.
6. **RM-15**, then **RM-16** — operations standard, incident protocol.
7. As decisions arrive: act on the matching roadmap rows, then mark them done here and in
   the roadmap, with evidence in the log.

## How to resume without re-reading everything

- Read this file, then only the record the next action names.
- Governance changes: [GOVERNANCE_MAP.md](../../GOVERNANCE_MAP.md) → [MAINTENANCE.md](../../MAINTENANCE.md)
  → the pull request template's six sections. Every governance change updates
  `schemas/governance.yaml` and appends to `CHANGELOG.md` in the same change.
- Work on `feature/claude`, rebased on `development`; pull requests into `development` only
  ([standards/BRANCHING.md](../../standards/BRANCHING.md)).
- To re-measure: `py -3 docs/program/collect_inventory.py <path outside the repository>`.
  Do not commit its output.
- Update this file and the log after every milestone. Never mark a row done without the
  evidence that it is.
