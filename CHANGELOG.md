# Governance Changelog

The record of what changed in this repository, when, and who changed it.

**Append only.** Entries are added at the top. An existing entry is not edited and not
removed, including one that turns out to be wrong — a correction is a new entry that says
what it corrects. Only the repository owner may alter or remove history here.

**Why this exists when git history already does.** Git records the change; this records
the *decision* — what it was for, and whether a human or an agent made it. Git author
fields also carry whatever identity the committing machine happened to be configured
with, which is not always the actor. This file states the actor explicitly, so an
attribution error is visible rather than silent.

**Every governance change appends here, in the same change**, alongside the
`schemas/governance.yaml` timestamp. See
[MAINTENANCE.md](MAINTENANCE.md).

**Enforcement rung: 2 (guidance).** Nothing currently prevents this file being edited or
an entry being removed. Append-only protection and owner-restricted history are rung 3-4
mechanisms — branch protection and CODEOWNERS — and are not configured yet. Until they
are, this holds because it is followed.

Format, newest first:

```
## YYYY-MM-DDTHH:MM:SSZ — <one-line summary>
- **Actor:** <name> (<human | agent>)
- **Change:** <what changed, and where>
- **Why:** <the decision, not the diff>
```

---

## 2026-09-05T21:14:22Z — One identity per actor, and what co-authorship means
- **Actor:** Claude (agent), acting for the repository owner
- **Change:** standards/SECURITY.md gains one-identity-per-actor and use-the-official-one;
  standards/DEVELOPMENT.md defines co-authorship as genuinely shared work in one commit.
- **Why:** the owner corrected two things. This agent had minted its own per-version
  identity (claude-opus-5@users.noreply.github.com) rather than using the canonical
  Anthropic one — exactly the fragmentation the new rule forbids, since an identity that
  changes per model release makes continuous work look like strangers'. And the co-author
  trailer was being applied as a disclosure stamp rather than reserved for commits that
  genuinely contain two actors' work.
- **Corrects:** the entries below record this agent as *Claude Opus 5*. That naming was
  wrong under the rule added here. Per the append-only rule those entries are left as
  written; the actor in all of them is **Claude**.


## 2026-09-05T21:08:11Z — Omit the co-author trailer when the actor is the author
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** standards/DEVELOPMENT.md, Commits.
- **Why:** the owner observed a commit naming Claude as both author and co-author, under
  two different addresses. The trailer exists to credit a contributor who is not the
  author; once the agent authors its own commits the trailer credits the same actor twice
  and reads as two contributors. Disclosure is already served, more strongly, by the
  author field.

## 2026-09-05T21:03:01Z — Changelog and actor attribution
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** this file; the append-and-record rule in MAINTENANCE.md; commit attribution
  in standards/DEVELOPMENT.md; authenticate-as-yourself in standards/SECURITY.md; verify
  your configured identity before acting in standards/AGENT_ENVIRONMENT.md.
- **Why:** raised after the owner noticed governance commits authored as *Jarvis*. They
  were this agent — the VM git config named a different actor and it was inherited without
  being checked, so roughly twenty commits across the ecosystem misattribute the work. The
  history is not being rewritten: those commits are merged and shared, and rewriting shared
  history is worse than the misattribution. The rules exist so the next agent checks first.

## 2026-09-05T20:50:59Z — Design system: cross-surface check and declared opt-outs
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** `standards/DESIGN_SYSTEM.md` gains a before-adding cross-surface
  check and a bounded selective opt-out; `schemas/ecosystem.yaml` drops the
  deleted `harith-design-system` entry.
- **Why:** promotion was purely reactive, triggered only once a duplicate already existed;
  and a surface previously had no middle ground between using a shared piece and declaring
  a whole second identity.

## 2026-09-05T19:27:18Z — Mark mcp-registry-mcp-server as integrated
- **Actor:** HarithKavish (human)
- **Change:** `schemas/ecosystem.yaml` adoption state and notes for that
  repository.
- **Why:** it was onboarded — AGENTS.md and GOVERNANCE.md added — so the registry no
  longer matched reality.

## 2026-09-05T13:09:47Z — Add the Deployment standard
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** new `standards/DEPLOYMENT.md`; Article 5 extended by one item;
  routing rows in `AGENT_BOOTSTRAP.md` and `README.md`.
- **Why:** nothing owned what happens between `main` and a live surface, so
  deployment could sit entirely in platform settings and be invisible to review.

## 2026-09-04T20:45:14Z — Govern the agent environment
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** new `standards/AGENT_ENVIRONMENT.md`; new
  `schemas/governance.yaml`; `MAINTENANCE.md` timestamp rule.
- **Why:** Article 1 already governed agents but nothing implemented it, and Article 2
  assumed a repository could detect it had fallen behind when nothing let it.

## 2026-09-04T18:40:00Z — Registry completeness
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** Article 5 sharpened; `standards/REPOSITORY.md` registry rules;
  `protocols/REPOSITORY_ALIGNMENT.md` Phase 0; `schemas/ecosystem.yaml`
  made complete against the account.
- **Why:** a repository could exist with no membership decision at all, indistinguishable
  from a deliberate exclusion — 26 of 54 were in that state.

---

*Entries before 2026-09-04 predate this file and are recorded only in git history.*
