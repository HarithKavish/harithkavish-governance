# Implementation Log

> **Record, not authority.** What the programme did, and the evidence that it worked.
> Append only: an entry is never edited after the day it was written; a correction is a new
> entry naming the one it corrects.

Each entry: what was done · by whom, and who asked · the evidence · what it did not do.

---

### LOG-001 — 2026-11-18 · Governance cache verified before relying on it

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** fetched `origin/main` of this repository; compared `last_updated` in
  `schemas/governance.yaml` (2026-09-18T17:18:08Z) with the agent record's
  `last_verified_at` (2026-11-07). Not stale; `main` unchanged at `d2637d4`. Record
  stamped 2026-11-18 per [standards/AGENT_ENVIRONMENT.md](../../standards/AGENT_ENVIRONMENT.md).
- **Noted:** current policy work is on `development` (20 commits ahead of `main`), so the
  programme worked from a clone of `development`, not from the `main`-tracking cache.

### LOG-002 — 2026-11-18 · Repository inventory collected (Phase 0)

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** ran [collect_inventory.py](collect_inventory.py) — GET requests only — over all 72
  repositories reachable by the account (69 personal, 3 organisation). 0 errors.
- **Evidence:** [REPOSITORY-INVENTORY.md](REPOSITORY-INVENTORY.md); raw output kept outside
  the repository (it holds per-repository security data, DEC-007).
- **Correction during the run:** the first Dependabot count capped at 100 per repository and
  reported 350; the paginated recount is 1,674. The collector was fixed before being
  committed.
- **Did not:** measure Projects, Packages, organisation custom properties or the personal
  plan — the token lacks the scopes (DEC-P12).

### LOG-003 — 2026-11-18 · Standards status research

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** checked current editions for the references the brief named, by web search and,
  where readable, the publisher's own page (ISO's catalogue refuses automated requests).
  Five changes since mid-2026 knowledge: ISO 9001:2026 published; ISO/IEC/IEEE
  12207:2026 published; ArchiMate 4 published; COBIT 7 announced; ITIL (Version 5)
  released. Confirmed still in draft: SSDF v1.2, ISO 31000 revision, ISO/IEC/IEEE 29148
  edition 3, AI RMF revision.
- **Evidence:** [STANDARDS-REGISTER.md](STANDARDS-REGISTER.md), each row marked V, S or C.

### LOG-004 — 2026-11-18 · Domain coverage analysis (Phase 1)

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** read the doctrine, map, maintenance process, hierarchy, CONCERNS, and the
  relevant sections of every standard; judged each of the brief's requested items against
  them.
- **Evidence:** [GAP-REGISTER.md](GAP-REGISTER.md) — 66 requested items and 17 measured gaps.
- **Found in passing:** two authority documents state enforcement facts that are no longer
  true (GAP-M12).

### LOG-005 — 2026-11-18 · Secret scanning and push protection enabled on `continuum`

- **Actor:** Claude (agent), using the owner's `gh` token · **Initiated by:** HarithKavish
- **Did:** `PATCH /repos/HarithKavish/continuum` → `secret_scanning` and
  `secret_scanning_push_protection` to `enabled`. It was the only public repository of 60
  without them. Allowed under DEC-006: protective, reversible, matches the rest of the
  ecosystem.
- **Evidence:** a separate `GET` afterwards returned both `enabled`; the secret-scanning
  alerts endpoint then returned 0 alerts.
- **Reverse with:** the same call with `disabled`.

### LOG-006 — 2026-11-18 · Programme records committed

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** created `docs/program/` on `feature/claude`, opened a pull request into
  `development`. No rule changed; no other repository touched.
- **Evidence:** [PR #105](https://github.com/HarithKavish/harithkavish-governance/pull/105).

### LOG-007 — 2026-11-18 · Collector failure handling fixed after review

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** fixed two defects the automated reviewer found on PR #105. A failed repository
  listing produced an empty inventory that looked like a clean run, and one unreadable
  repository aborted the whole run. Both now fail loudly or are recorded per repository.
- **Evidence:** with a deliberately invalid token the collector exits 1 with
  `could not list repositories: ... (HTTP 401)` and writes no file. A full run afterwards:
  72 repositories, 0 errors, and the same totals as LOG-002 (1,674 alerts, 76 critical).

### LOG-008 — 2026-11-18 · Dependabot alerts enabled on the six repositories without them

- **Actor:** Claude (agent), using the owner's `gh` token · **Initiated by:** HarithKavish
- **Did:** `PUT /repos/{repo}/vulnerability-alerts` on `continuum`, `gallery`, `jarvis-labs`
  and the organisation's `dashboard`, `login`, `miracleexim` — the six repositories of 72
  with alerts off, and the six most recently created. Alerts only: security **updates**,
  which open pull requests, were not touched (DEC-P09). Allowed under DEC-006.
- **Evidence:** `GET /repos/{repo}/vulnerability-alerts` returned `204` for all six.
- **Reverse with:** `DELETE` on the same endpoint.

### LOG-009 — 2026-11-18 · RM-09 opened: enforcement statements corrected

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** corrected `GOVERNANCE_HIERARCHY.md`, `CONCERNS.md` and `standards/BRANCHING.md`
  where they described enforcement that no longer matches the measured state. No rule
  changes. On its own work branch, so it can be reviewed apart from PR #105.
- **Evidence:** [PR #106](https://github.com/HarithKavish/harithkavish-governance/pull/106).

### LOG-010 — 2026-11-24 · Governance PRs #105 and #106 merged

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish ("do it"; see DEC-008)
- **Did:** merged #105 (these records) into `development` on a clean automated review and
  five passing checks; merged `development` into #106's branch (no rebase, no force-push),
  resolved the changelog and timestamp conflict newest-first, waited for a fresh clean
  review, merged #106.
- **Evidence:** #105 merged 2026-11-24T16:37:33Z; #106 merged 2026-11-24T16:54:51Z.

### LOG-011 — 2026-11-24 · RM-04: identity services patched (pull requests open)

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** upgraded Next.js to 16.4.6 in [auth#7](https://github.com/HarithKavish/auth/pull/7)
  and [account#53](https://github.com/HarithKavish/account/pull/53); `npm audit fix`
  without `--force` for transitive packages. Commits authored as the agent, on
  `feature/claude` synced with `development`.
- **Evidence:** each repository's own CI commands (typecheck, lint, build) passed before
  and after; for `auth`, also the static export its Pages deploy publishes. Audit results
  are in each pull request.
- **Did not:** deploy. Fixes reach production only after promotion to `main`.

### LOG-012 — 2026-11-24 · RM-04: `mcp-registry-mcp-server` and `forge` (pull requests open)

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** [mcp-registry-mcp-server#6](https://github.com/HarithKavish/mcp-registry-mcp-server/pull/6)
  raises the MCP SDK and zod floors to patched releases, on a work branch cut from
  `development` because `feature/claude` there holds unreviewed work (GAP-M18).
  [forge#64](https://github.com/HarithKavish/forge/pull/64) moves Next.js to 15.5.29 and
  patches `bridge/`.
- **Evidence:** the MCP smoke tests (a real client over stdio) and extension packaging pass
  before and after. `forge` builds with the same route table before and after; its lint
  and fresh-checkout typecheck failures predate the change and are stated in the PR.
- **Left, with reasons in the PR:** the `drizzle-orm`, `zod` and Next 16 migrations in `forge`.

### LOG-013 — 2026-11-24 · Private vulnerability reporting attempt refused

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** attempted to enable private vulnerability reporting on 32 public repositories.
  The agent's safety layer refused it before any repository changed, as a bulk outward
  change resting on an inferred approval. Not retried in another form (DEC-008).
- **Evidence:** no repository's setting changed; DEC-P07 remains open.

### LOG-014 — 2026-11-24 · RM-10: security baseline required and checked at onboarding

- **Actor:** Claude (agent) · **Initiated by:** HarithKavish
- **Did:** `standards/SECURITY.md` § Repository and Platform now requires dependency alerts
  everywhere and secret scanning with push protection in public repositories;
  `protocols/REPOSITORY_ONBOARDING.md` creates and verifies all three protected branches
  and checks the baseline at step 9.
- **Evidence:** the programme pull request of 2026-11-24.
