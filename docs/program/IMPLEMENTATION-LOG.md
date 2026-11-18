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
