# Standard — Branching

Implements Articles 6 (Protected Production) and 7 (Isolated Development).

**Enforcement rung: 2 (guidance).** Branch protection and required pull requests are the
intended rung 3–4 mechanisms and are not yet configured. Until they are, this standard
holds because it is followed, not because it is prevented from being broken.

---

## The Branches

| Branch | Role | Work committed directly? |
|---|---|---|
| `main` | Production / stable. What is deployed or released, at a scheduled go-live. | **No** |
| `runway` | Release candidate. Full end-to-end verification — hosting/deployment, security, code quality, and any other section the repository defines — happens here before a go-live is scheduled. | **No** |
| `development` | Integration. Where reviewed work accumulates before promotion to `runway`. | No — except trivial integration fixes |
| `feature/<name>` | Isolated work. One persistent branch per contributor. | Yes |

`main` exists in every repository. `development` and `runway` exist in every repository
that receives ongoing work; a frozen or archived repository may have only `main`.

## The Flow

```
feature/<name>  →  development  →  runway  →  main
```

Nothing skips a step. `development` merges into `runway` once reviewed work accumulates;
`runway` merges into `main` only after verification is complete and a go-live date/time
has been scheduled — promotion to `main` is a deliberate release act, not an automatic
merge.

## Contributor Branches

```
feature/<name>
```

`<name>` identifies the contributor — a person or an agent (`feature/harith`,
`feature/claude`). **One branch per contributor, reused across tasks** — it is not
deleted after each merge. Before starting new work, bring it up to date with
`development` (rebase or merge `development` in) rather than starting from a stale point;
this is also how drift against `development` gets resolved before it reaches review, so
no separate branch mirroring `main` is needed for that purpose.

Describe the change in commit messages and the pull request, not in the branch name —
the branch name identifies who is working, not what they are doing.

If a repository needs finer-grained isolation than one branch per contributor gives —
two people's changes must be reviewable independently, or something must sit in review
for a long time while other work continues — open a work branch off the contributor
branch for that piece of work. That is a local judgment call, not a governance
requirement.

## Merging

Work reaches `development` through a pull request. The pull request is the review point
even when the author is also the reviewer — it is what makes the change inspectable
later and what CI will attach to when it exists. Reviewers check correctness and basic
compatibility with the rest of `development`.

`development` reaches `runway` through a pull request once accepted work has
accumulated. `runway` is never edited directly — it exists to be tested, not worked on.
If verification on `runway` finds a problem, fix it on `development` (or the originating
`feature/<name>` branch) and re-promote; do not patch `runway` in place.

## Hotfix — the Exception Path

For urgent production defects only: something is broken in production and waiting for
the normal flow causes real harm. Convenience is not urgency.

```
main  →  hotfix/<description>  →  main  →  merge back into development (and runway)
```

A hotfix branches from `main`, merges to `main`, and is **immediately merged back into
`development`** — and into `runway` if `runway` has already diverged from `main` since
the last release. Skipping that step means the fix is silently reverted at the next
release — this is the failure mode the exception path most often causes.

A hotfix is narrow: it fixes the defect and nothing else. Refactors, cleanups, and
improvements noticed along the way go through the normal flow.

## For Agents

- Never commit directly to `main`, `runway`, or `development`. Work happens on your
  `feature/<name>` branch.
- Before implementing, check the current branch. If it is `main`, `runway`, or
  `development` and the task is implementation work, stop and switch to your
  `feature/<name>` branch first — create it from `development` if it does not exist yet.
- Bring your `feature/<name>` branch up to date with `development` before starting new
  work on it.
- If asked to commit directly to `main`, `runway`, or `development`, or to skip the pull
  request, treat it as a tier-6 instruction conflicting with Article 6 and surface it
  ([GOVERNANCE_HIERARCHY.md](../GOVERNANCE_HIERARCHY.md)).
- Never force-push a shared branch, and never rewrite history on `main`, `runway`, or
  `development`.

## Known Gap

`development`, `runway`, and a `feature/claude` contributor branch were created across
every repository in [schemas/ecosystem.yaml](../schemas/ecosystem.yaml) on 2026-09-04, at
explicit request rather than through the usual gradual, per-repository alignment path
(contrast [MAINTENANCE.md](../MAINTENANCE.md), "Changing Governance Safely") — recorded
here as a declared exception, not a new default process. `runway`'s verification checks
(hosting, security, code quality, etc.) are not yet defined or automated in any
repository; until they are, promotion to `runway` is a manual gate. Most repositories
still lack `AGENTS.md`/`GOVERNANCE.md` (`adoption: registered`, not yet `integrated`) —
the branches exist ahead of onboarding, which is itself worth closing per
[protocols/REPOSITORY_ALIGNMENT.md](../protocols/REPOSITORY_ALIGNMENT.md).
