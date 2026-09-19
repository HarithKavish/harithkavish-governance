# Standard — Branching

Implements Articles 6 (Protected Production) and 7 (Isolated Development).

**Enforcement rung: 4 (mechanically enforced) for `main`, `runway`, and `development` in
every repository — see [GOVERNANCE_HIERARCHY.md](../GOVERNANCE_HIERARCHY.md) § The first
rule to reach rung 4.** Branch protection (pull request required, force-push and deletion
refused) was applied ecosystem-wide on 2026-09-08. `enforce_admins` is deliberately off,
so owner/App credentials can still bypass it in a genuine incident — see that section for
why, and for the corresponding gap this creates. Everything else this standard describes
(the flow itself, contributor-branch conventions) remains rung 2: followed because it is
correct, not because anything prevents it from being broken.

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
`runway` merges into `main` only after that branch's release gate passes — see
[The Release Gate](#the-release-gate).

Promotion to `main` is a deliberate release act. **The deliberate part is the gate, not
the click.** Where every condition in a gate is mechanically evaluated, the act of
promoting may be performed by automation; where any condition is a human judgment, it
may not. A promotion that passed no configured gate is not deliberate, however carefully
the person performing it thought about it — and a promotion that passed a complete one
is not made less deliberate by nobody watching it happen.

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

## The Release Gate

A **gate** is the set of conditions that must hold before a promotion into a branch.

**The gate is the required status checks configured on the target branch.** It is not a
document, a checklist, or an intention. This is deliberate: required checks are already
a platform mechanism that cannot be bypassed by forgetting, which is the only kind of
gate worth having
([GOVERNANCE_HIERARCHY.md](../GOVERNANCE_HIERARCHY.md) — only rungs 3–4 are enforcement).

**An empty gate is a closed gate.** A branch with no required checks configured has not
declared what it verifies, and **nothing may be promoted into it automatically**. It
falls back to a human performing the promotion deliberately. Absence of a gate must
never read as absence of risk — that inversion is how an unverified change reaches
production while everyone believes a process ran.

### What each gate contains

Repositories differ, so governance sets the **minimum**; each repository adds what its
own surface needs.

Promotion into `runway` requires, at least:

- every check required on `development` still passing on the merge result
- a secret scan over the change, with no unresolved finding
- a dependency scan, with no unresolved finding of high severity or above

Promotion into `main` requires all of the above, and additionally:

- the repository's own verification suite passing **on `runway`** — its tests, its
  build, whatever it declares. A repository with no suite declares that fact rather
  than leaving the question open.
- for a repository with a live surface, evidence that the surface **actually serves**
  after deployment — a fetch of the real URL, not a green deploy job. A deployment step
  reporting success is not a working site
  ([AGENT_METHOD.md](AGENT_METHOD.md) § 7).
- a recorded rollback path — the previous release must be re-deployable without
  reconstructing it.

### Automated promotion

Automation may perform a promotion **only** when every condition in that branch's gate
is mechanically evaluated. It may never perform one on the strength of its own
assessment that the change looks correct, and it may never promote into a branch whose
gate is empty.

An agent that finds a gate unsatisfiable reports that and stops. Stopping is a complete
outcome; a promotion that skipped its gate is not recoverable by noticing afterwards.

> **Enforcement rung: 4 where a gate is configured, 2 where it is not.** The checks
> themselves are platform-enforced; *whether a repository has configured any* is
> currently nobody's automated responsibility. Reconciling configured gates against
> this minimum is a rung-4 mechanism that does not exist yet, and until it does, a
> repository can be silently gateless. That gap is why the empty-gate rule above fails
> closed rather than open.

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
- You may perform a promotion only when the target branch's gate is fully mechanical and
  passing ([The Release Gate](#the-release-gate)). A branch with no required checks has
  an empty gate, and an empty gate is closed — hand that promotion to a human and say
  why. Your own judgment that the change looks correct is not a gate.

## Known Gap

`development`, `runway`, and a `feature/claude` contributor branch were created across
every repository in [schemas/ecosystem.yaml](../schemas/ecosystem.yaml) on 2026-09-04, at
explicit request rather than through the usual gradual, per-repository alignment path
(contrast [MAINTENANCE.md](../MAINTENANCE.md), "Changing Governance Safely") — recorded
here as a declared exception, not a new default process. `runway`'s verification checks
are now **defined** — see [The Release Gate](#the-release-gate) — but as of 2026-09-19
**no repository has configured them**, so every gate in the ecosystem is empty and every
promotion is therefore manual by the fail-closed rule. Defining the minimum was the
prerequisite; configuring it per repository, and reconciling that configuration
automatically, are both still outstanding. Most repositories
still lack `AGENTS.md`/`GOVERNANCE.md` (`adoption: registered`, not yet `integrated`) —
the branches exist ahead of onboarding, which is itself worth closing per
[protocols/REPOSITORY_ALIGNMENT.md](../protocols/REPOSITORY_ALIGNMENT.md).
