# Decisions

> **Record, not authority.** A decision here governs how this programme works. A decision
> that changes a rule for the ecosystem takes effect only when it lands in the doctrine, a
> standard, a protocol or a schema under [MAINTENANCE.md](../../MAINTENANCE.md).

IDs are permanent. A decision that is reversed keeps its entry and gains a line naming
what superseded it; entries are not deleted.

---

## Made — within the programme's delegated scope

Each is reversible and changes no rule.

### DEC-001 — Programme records live in `docs/program/` and carry no authority

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

The brief asked for eight tracking files in the governance repository. Classified with
[GOVERNANCE_MAP.md](../../GOVERNANCE_MAP.md): they are not doctrine, standard, protocol,
schema or maintenance. They are dated records of one body of work, which makes them
**implementation documentation of this repository** (destination 7, tier 5). They go in
`docs/` rather than at the root because files at the root of this repository are read as
governance; a status file next to `MASTER_DOCTRINE.md` would invite exactly the authority
confusion the tier model exists to prevent.

*What would reverse it:* the owner deciding programme tracking is a governance category of
its own — which would need a map entry first ([GOVERNANCE_MAP.md](../../GOVERNANCE_MAP.md)
§ Introducing a New Category).

### DEC-002 — The brief is routed through the existing process, not executed as a document list

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

The brief is a task instruction: tier 6, the lowest authority
([GOVERNANCE_HIERARCHY.md](../../GOVERNANCE_HIERARCHY.md)). Read literally, it asks for
some forty new documents. MAINTENANCE ranks "add a new document" last, and only for a
concern no document owns. The brief itself asks to preserve valid rules, avoid
duplication, and prefer proportionate governance — so the two point the same way, and no
conflict needs resolving. Every requested item is judged in the
[gap register](GAP-REGISTER.md) and either pointed at existing coverage, routed to an
existing document, proposed as a new document with its justification, or marked "not now"
with the trigger that would change that.

### DEC-003 — External standards are references, not certification targets

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

The [standards register](STANDARDS-REGISTER.md) uses ISO, IEC, IEEE, NIST and similar
publications to find what governance has missed, and to name things consistently. Nothing
here claims conformance to or certification against any of them. Pursuing certification
would be an owner decision with cost, and is the trigger that would make a management-system
manual worth writing.

### DEC-004 — The registry stays the authority on membership; the inventory is a measurement

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

[REPOSITORY-INVENTORY.md](REPOSITORY-INVENTORY.md) does not replace
`schemas/ecosystem.yaml`. Where they disagree, the disagreement is a finding (GAP-M01,
GAP-M02). The inventory is not kept current by hand; it is re-measured.

### DEC-005 — Identifier convention for programme records

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

| Prefix | Record |
|---|---|
| `GAP-<area><nn>` | A gap (areas A–H from the brief; M for measured) |
| `DEC-<nnn>` / `DEC-P<nn>` | A decision made / pending with the owner |
| `REF-<nn>` | An external reference in the standards register |
| `CAP-<nn>` | A GitHub capability |
| `RM-<nn>` | A roadmap item |
| `LOG-<nnn>` | An implementation log entry |

Repositories are keyed by `owner/name` for reading and by GitHub's numeric repository id
for stability across renames. A proposal for ecosystem-wide traceability identifiers
(Phase 5) is separate, and would go through MAINTENANCE.

### DEC-006 — GitHub settings change only when the change is protective, reversible and uncontested

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

The brief asks for GitHub features to be configured. A setting is changed by the programme
without a further question only when all three hold: it reduces risk, it can be switched
back, and it brings a repository in line with what the rest of the ecosystem already has.
Anything that opens a new channel to outsiders, creates pull-request volume, costs money or
Actions minutes, or changes who can do what is an owner decision (DEC-P07, P08, P09).
First use: LOG-005.

### DEC-007 — Vulnerability detail is not published in this repository

**2026-11-18 · Claude (agent) · initiated by HarithKavish**

This repository is public. Aggregate counts are published; which repository carries which
open advisory is not. A per-repository list of unpatched critical advisories against live
services is what [standards/SECURITY.md](../../standards/SECURITY.md) § Reporting keeps out
of public issues and commit messages, and a public status file is no different. Detail goes
to the owner directly.

---

## Pending — needs the owner

Each states the recommendation and why. None is acted on until answered.

| ID | Question | Recommendation | Blocks |
|---|---|---|---|
| DEC-P01 | Membership of the 12 undecided repositories | Per repository in [the inventory](REPOSITORY-INVENTORY.md#undecided-membership): 6 covered; 2 more covered if DEC-P02 brings the organisation in; 1 excluded; 3 genuinely the owner's call (`hermes-agent`, `interstellar`, `miracleexim`) | GAP-M01; RM-03 |
| DEC-P02 | Is the organisation `harithkavishtechnologies` part of the ecosystem? If yes: require two-factor authentication, restrict repository creation, and widen the registry's scope from "the account" to "the account and its organisations" | Yes — it serves `harithkavish.com/login` and `/dashboard` | GAP-A03, GAP-M13 |
| DEC-P03 | Licensing intent. Today 71 of 72 repositories grant no licence, which by default means **all rights reserved** — a legitimate choice, but currently an unrecorded one, and for public repositories it is often unintended | Decide per class: content sites and apps — state "all rights reserved" explicitly; anything meant for reuse (`design-system`, `agent-toolkit`, `mcp-registry-mcp-server`) — choose an open licence deliberately. Agents will not choose a licence | GAP-M05 |
| DEC-P04 | Mission, vision, values, and whether the ecosystem is an organisation with a charter or a personal portfolio governed like one | Owner writes it; one paragraph each is enough | GAP-A01, GAP-A02 |
| DEC-P05 | Jurisdiction: where the owner operates and where users of surfaces that store personal data are (`account`, `auth`, `diary`, `memory-diary`, and others the manifests will name) | Record it; then identify applicable privacy law and its obligations — legal advice if any surface has real outside users | GAP-B08, GAP-G04 |
| DEC-P06 | Does any surface carry a commitment to anyone — users, a client, a course? | If none: state "no SLAs exist" in the operations standard and allow only internal SLO targets | GAP-F03 |
| DEC-P07 | Turn on private vulnerability reporting for public covered repositories, and add a `SECURITY.md` that points to it | Yes. It gives outside finders a private route, which SECURITY § Reporting already demands of insiders | GAP-M07 |
| DEC-P08 | Turn on CodeQL default setup for public covered repositories | Yes for repositories with application code; free on public repositories. Adds a check and an alert stream | GAP-M08 |
| DEC-P09 | Dependabot security updates | Turn on one repository at a time, highest exposure first. Every update is a pull request, and every pull request runs automated review **at a per-review cost** — 462 alerts would mean hundreds of paid reviews. Group updates (`dependabot.yml` groups) before enabling widely | GAP-M06 |
| DEC-P10 | Excluded repositories that are public, vulnerable and in one case live | Bring `SkinNet-Analyzer` into scope, or take it private / offline; archive coursework that is not meant to run | GAP-M17 |
| DEC-P11 | The governance backlog: promotion PR #100 (`runway`→`main`, open since 2026-10-28) and PRs #97, #98, #101, #103, #104; creating the policy App and its credentials | Review and merge #100 first: it carries the policy engine to `main`, the only branch scheduled workflows run from | GAP-M04, GAP-M15 |
| DEC-P12 | Grant the agent token the scopes the audit lacks: `admin:org`, `read:project`, `read:packages`, `user` (`gh auth refresh -h github.com -s admin:org,read:project,read:packages,user`) | Read scopes only; `admin:org` only if DEC-P02 is yes | CAP-05, CAP-13, CAP-16, CAP-18 |
| DEC-P13 | ~~Is `enforce_admins` meant to be on?~~ **Withdrawn the same day — already decided.** [standards/BRANCHING.md](../../standards/BRANCHING.md) § Bypass records the owner's decision of 2026-10-15: no bypass for anyone, the owner included. Measured state (on, 65 of 65 protected repositories) matches it; only GOVERNANCE_HIERARCHY and CONCERNS are stale | Correct the stale documents (RM-09) | — |
