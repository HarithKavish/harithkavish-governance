# Protocol — Repository Alignment

How an **existing** repository adopts HarithKavish governance, and how a repository that
has fallen behind the current doctrine is brought back.

For a brand-new repository, use [REPOSITORY_ONBOARDING.md](REPOSITORY_ONBOARDING.md).

---

## The Rule That Governs This Protocol

**Detection is not authorization.**

An agent that discovers governance in an existing repository will find non-compliance —
these repositories predate this system, and some of them predate the design system they
are supposed to follow. That discovery does not license rewriting them.

The output of alignment is, in order: a **report**, then **only the changes that were
actually requested**. An agent that reads the doctrine and rewrites a website because it
noticed inconsistencies has violated Article 9 more seriously than the inconsistencies
violated anything.

---

## Phase 0 — Decide Membership

Alignment presumes the repository is a member. Often that has never actually been
decided, and deciding is the first step — not something inferred on the way past.

**When this phase applies.** The repository is under the ecosystem account and appears
nowhere in [schemas/ecosystem.yaml](../schemas/ecosystem.yaml) — neither as a participant
nor as an excluded one. That absence is an open question, not an answer (Article 5). It
happens most often with a repository created recently enough that nobody has classified
it yet.

### 1. Establish that it really is unrecorded

Look the repository up by name in the registry. Absent from both lists means undecided.
Present in either means the decision already exists — follow it, and if it looks wrong,
report that rather than re-deciding it yourself.

### 2. Ask the owner

**Do not decide membership on the owner behalf.** Put the question plainly, with what you
observed and what you would recommend:

- what the repository appears to be — website, application, service, shared library, or
  none of those
- whether it has a live surface
- whether it reads as an ecosystem surface or as a learning exercise, experiment, or
  one-off

Recommend an answer; do not act on the recommendation until it is confirmed. A repository
that is a member gains real obligations, and one that is not should never acquire them
through an agent assumption.

### 3. Record the answer

Both answers are results, and both are recorded — an unrecorded "no" is
indistinguishable from never having asked, which is the condition this phase exists to
remove.

- **Covered** → add it to `repositories` with its role, surface, adoption state, and
  the date of the decision.
- **Not covered** → add it to `excluded` with the reason and the date.

This is a change to the governance repository and follows its own branching rules
([MAINTENANCE.md](../MAINTENANCE.md), [standards/BRANCHING.md](../standards/BRANCHING.md)).
Raise it as a pull request; do not commit the registry change directly.

### 4. Then continue — or stop

- **Covered** → continue to Phase 1. Registration is not onboarding: the repository still
  has no `AGENTS.md` or `GOVERNANCE.md` until that work is done, and that work is
  scoped separately (Article 9).
- **Not covered** → stop. Governance does not apply. Do not add governance files to a
  repository that was just recorded as outside the ecosystem.

### Running it across the account

The same decision applies at account scale: list every repository under the account,
compare against the registry, and treat every name in neither list as undecided, through
steps 2–4. Record the date of the reconciliation itself, so the next run knows how far
back it is looking.

The expected finding is repositories created since the last reconciliation. Finding none
is also a result worth dating.

---

## Phase 1 — Assess

Change nothing during this phase.

1. **Inspect the repository.** Remote, branches, root files, working tree state.
2. **Check for existing integration.** Do `AGENTS.md` and `GOVERNANCE.md` exist? Do they
   reference HarithKavish governance? Partial integration is common — a repository may
   have `AGENTS.md` written by a toolchain with no governance content in it.
3. **Record the branch structure.** Which branches exist? Is there a `development`
   branch? Is work currently happening directly on `main`?
4. **Record the architecture.** Framework, build, deployment target, entry points, how
   the repository is actually organized.
5. **Record the design situation.** Does it consume the shared design system, an old
   version of it, or its own styles? Are there local colours, type scales, or spacing
   values? Are there local components that duplicate shared primitives?
6. **Record the metadata state.** Description, social preview, homepage, README, topics.
7. **Check registration.** Is it listed in
   [schemas/ecosystem.yaml](../schemas/ecosystem.yaml)?

## Phase 2 — Compare

Compare what you recorded against the applicable governance. Read only the standards the
repository actually touches ([AGENT_BOOTSTRAP.md](../AGENT_BOOTSTRAP.md)).

For each gap, capture: what governance requires, what the repository does, and which
class the fix falls into.

## Phase 3 — Classify Every Gap

This is the step that keeps alignment safe. Each gap is exactly one of:

### Class A — Governance metadata integration

Adding the discovery layer. Additive, reversible, and touches nothing the product does.

- Adding `AGENTS.md` and `GOVERNANCE.md`
- Registering the repository in `schemas/ecosystem.yaml`
- Setting the About description, homepage, and topics
- Committing a social preview source image

**Permitted when adoption was requested.** This is what "adopt governance" means.

### Class B — Immediate safe compliance

Small, low-risk, behaviour-preserving corrections.

- Creating a `development` branch from `main`
- Adding `.env` to `.gitignore` (where no secret is already committed)
- Adding a missing `.env.example` with placeholder values
- Correcting a README that misstates how the repository works

**Permitted when adoption was requested — but each is stated in the report.** No Class B
change happens silently.

If a Class B fix turns out to be entangled with product behaviour, it was not Class B.
Reclassify it as Class C and stop.

### Class C — Migration

Anything that changes what the repository is, does, or looks like.

- Migrating to the shared design system, or off local styles
- Removing or replacing local components with shared primitives
- Restructuring directories, renaming the repository
- Changing the build, framework, deployment, or dependencies
- Rewriting history, or anything touching a committed secret
- Changing anything on the production branch beyond the classes above

**Requires explicit scope. Never performed as a side effect of adoption.**

Report Class C gaps with enough detail to be scheduled — what is wrong, what it would
take, what it risks — and stop there. Each is its own task, on its own branch, with its
own review.

## Phase 4 — Report

Report before acting, and report in this shape:

```
Repository: <name>
Integration: none | partial | complete

Class A — governance metadata  (applied / to apply)
  - ...

Class B — safe compliance      (applied / to apply)
  - ...

Class C — migrations           (NOT performed — require scope)
  - <gap> — <what governance requires> — <what it would take> — <risk>

Conflicts / unclear
  - <anything governance does not settle>
```

If nothing was requested beyond assessment, this report **is** the deliverable. Stop
here.

## Phase 5 — Apply What Was Requested

Only what was asked for, on a branch, following
[standards/BRANCHING.md](../standards/BRANCHING.md).

Class A and B changes are commonly bundled into a single "adopt governance" change. Class
C changes are never bundled with them — mixing metadata integration with a design
migration produces a diff nobody can review or revert.

---

## Special Cases

**A committed secret.** Stop the alignment work. This is a security incident, not a
compliance gap: rotate first, then clean history
([standards/SECURITY.md](../standards/SECURITY.md)). Do not report it in a public issue
or a public commit message.

**Work in progress on `main`.** Do not move someone's uncommitted or unmerged work as a
side effect. Report it and let the owner decide.

**A repository that should not be aligned.** Learning exercises, archived experiments,
and one-off scratch repositories are not ecosystem surfaces. If a repository is not a
website, application, service, or shared library, say so rather than onboarding it.
Membership is a decision, not a default.

**A deviation that is correct.** Some repositories deviate for good reasons. The fix is
not to change the repository — it is to record the exception in its `GOVERNANCE.md`
(Article 10). An undeclared good decision and an undeclared bad decision look identical
from outside; declaring it is what distinguishes them.

**Doctrine drift.** When the gap exists because governance changed rather than because
the repository regressed, it is handled identically. There is no separate upgrade path,
because there are no per-repository doctrine versions (Article 2).
