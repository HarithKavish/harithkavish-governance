# Governance Hierarchy

Defines **authority**: which document wins when two say different things, and what an
agent does when the hierarchy cannot resolve the conflict.

This document does not contain rules about branches, design, code, or repositories. It
contains the rules about rules.

---

## The Tiers

| # | Tier | Lives in | Answers |
|---|------|----------|---------|
| 1 | **Master Doctrine** | `MASTER_DOCTRINE.md` | What must always be true |
| 2 | **Global Standards** | `standards/` | What "correct" means for a concern |
| 3 | **Global Protocols** | `protocols/` | How a defined process is carried out |
| 4 | **Repository-Specific Rules** | `AGENTS.md`, `GOVERNANCE.md`, `CLAUDE.md` in each repo | What is true of *this* repository |
| 5 | **Implementation Documentation** | `README.md`, `docs/`, ADRs in each repo | How this repository actually works |
| 6 | **Task Instructions** | The request in front of you | What is being asked right now |

Authority decreases down the table. Specificity increases down the table.

This table defines **authority**. It does not decide where new content belongs — misfiling
is the main way governance rots, and the test for each destination lives in
[GOVERNANCE_MAP.md](GOVERNANCE_MAP.md).

Schemas (`schemas/`) carry no independent authority. A schema represents a rule stated
elsewhere, or holds data those rules operate on, and it inherits the authority of the
document it serves.

---

## Scope — Who A Rule Binds

Authority answers *which rule wins*. Scope answers a different question: *does this rule
reach here at all*. A repository outside the ecosystem is not outside every rule.

Governance divides in two (Article 1):

| | Binds | Reaches |
|---|---|---|
| **Actor rules** | How a person or an agent behaves | Every repository under the account, participating or not |
| **Repository rules** | What a repository contains, how it is built, how it ships | Participating repositories only |

**The test:** would the rule still make sense if the repository did not exist?

- *An actor uses its own identity* — yes. It is about the actor. **Universal.**
- *Every repository carries a social preview image* — no. It is about the repository.
  **Membership only.**

Actor rules are the ones that survive the repository: identity and credentials, how work
is attributed and where it came from, discovering what applies before modifying, staying
within the scope given, and not committing a secret. Repository rules are the visible
requirements — the design system, the branching flow, deployment, metadata, the registry
entry, the onboarding files.

**Why the split exists.** A learning exercise does not need a social preview image or the
shared design system, and requiring them would be ceremony nobody benefits from. But an
agent working in that same repository still needs to identify itself honestly, still needs
to say who asked for the change, and still must not commit a credential — none of which
becomes optional because the repository is small. The old model made non-participation
mean *no rules at all*, which quietly put the least-supervised repositories furthest
outside every safeguard.

A non-participating repository may therefore **ignore repository rules** and is expected
to. It may not ignore actor rules, and an actor cannot acquire an exemption by choosing to
work somewhere unregistered.

---

## Precedence

**Higher tiers constrain lower tiers.** A lower tier may:

- **Extend** — add detail, add stricter requirements, add repository-specific rules.
- **Specialize** — state how a general rule is satisfied in this particular context.
- **Declare an exception** — under Article 10, explicitly and in writing.

A lower tier may **not**:

- Silently contradict a higher tier.
- Relax a higher-tier requirement without declaring an exception.
- Restate a higher-tier rule in different words. (Restatement drifts; reference does not.)

### Task instructions are tier 6, not tier 0

A task instruction is the *lowest* authority, not the highest. "Just push it to main"
does not override Article 6.

This has one deliberate limit: the ecosystem owner may override any tier. That override
is a governance decision, so it is recorded — either as a declared exception in the
repository or as a change to governance itself under `MAINTENANCE.md`. An instruction
that conflicts with governance and is *not* recorded is treated as a conflict, and
handled below.

---

## Resolving a Conflict

1. **Identify the tiers.** Which document does each side of the conflict come from?
2. **If the tiers differ**, the higher tier wins. Proceed, and report that the lower-tier
   document is non-compliant so it can be corrected.
3. **If the tiers are equal**, the conflict is real and unresolved. Do not pick.
4. **If a task instruction conflicts with a higher tier**, do not silently comply and do
   not silently refuse. Surface it: name the rule, name the conflict, and ask whether
   this is a declared exception or a governance change.

### Never resolve a conflict by interpretation

When two documents of equal authority disagree, an agent must **stop and report** rather
than choose the reading that makes the task easiest. Silent interpretation is how two
repositories end up complying with the same rule in incompatible ways — which is the
failure this ecosystem exists to prevent.

Report a conflict as: the two documents, the two requirements, what is blocked, and the
options. Then wait.

An unresolved conflict is a signal that governance is ambiguous. Once decided, the
decision is written back into governance under `MAINTENANCE.md` so the same conflict does
not have to be resolved twice.

---

## Doctrine Changes and Propagation

The doctrine is global and current (Article 2). There are no per-repository doctrine
versions, so there is nothing to "upgrade" mechanically.

What changes is whether a repository still satisfies the current doctrine. When the
doctrine changes:

1. Repositories are **not** modified automatically.
2. The next time work is done in a repository, bootstrap discovery reads the current
   governance and may surface a gap.
3. That gap is reported and closed as scoped work, under
   [protocols/REPOSITORY_ALIGNMENT.md](protocols/REPOSITORY_ALIGNMENT.md).

Compliance across the ecosystem is therefore **gradual and deliberate**. This is
intentional: an ecosystem that self-modifies on doctrine change is an ecosystem where one
bad edit to governance rewrites every website.

---

## The Enforcement Ladder

Governance guides; infrastructure enforces. A rule becomes progressively harder to
violate as it descends this ladder:

| Rung | Mechanism | Effect |
|------|-----------|--------|
| 1 | **Doctrine** | States the principle |
| 2 | **Agent & human instructions** | Followed by anyone who reads them |
| 3 | **Repository configuration** | Encoded in the repo — templates, config, entry files |
| 4 | **CI / platform enforcement** | Cannot be bypassed by forgetting |

A rule at rung 1–2 is guidance. Only rungs 3–4 are enforcement. **A document must never
describe a rule as enforced when it is only written down.**

Standards therefore record their current rung, so the gap between intent and reality is
visible rather than assumed. Moving a rule down the ladder is a governance improvement and
does not require the rule itself to change — which is why rules are written as outcomes
rather than as instructions to a particular tool.

## What Is Actually Enforced

Governance is about doing and enforcing, not about having written something down. This
section records the gap between the two, measured rather than assumed, so it cannot be
quietly assumed away. **Measured 2026-09-05 across 26 covered repositories.**

| Rule | Written in | Rung | Reality |
|---|---|---|---|
| Production branch protected | BRANCHING | **4** | **78/78 protected** as of 2026-09-08 — `main`, `runway` and `development` across all 26 repositories. Pull request required, force-push and deletion blocked |
| Changes reach `main` via pull request | BRANCHING, DEVELOPMENT | **4** | Enforced by the same protection. Direct pushes to the three branches are refused |
| Automated review on every PR | DEVELOPMENT | 3, degraded | **Failing in 15/26.** See below — the one automated mechanism, broken and unnoticed |
| Repository metadata complete | REPOSITORY | 2 | **0/26 carry `.github/social-preview.png`**, which the standard requires |
| Changelog append-only, owner-restricted | MAINTENANCE, CHANGELOG | 2 | **0/26 have CODEOWNERS.** Anyone with write access can edit or delete history |
| Classify before writing governance | MAINTENANCE, GOVERNANCE_MAP | 2 → 3 | Was self-attested; a pull request template now requires the classification to be stated |
| Doctrine stays approximately its size | MAINTENANCE | 2 → 4 | Grew 860 → 1017 words in one day *with the rule in place*. Now checked in CI |
| Deployment declared in a workflow | DEPLOYMENT | 2 | 11 of 13 migrated; nothing prevents reverting a repository to a branch source |
| Design foundations not redefined locally | DESIGN_SYSTEM | 2 | No token or component validation exists |
| Actor identity and provenance | SECURITY, DEVELOPMENT | 2 | Nothing validates a commit author or an `Initiated-By` trailer |

### The automated review is broken

`DEVELOPMENT.md` states that every member repository carries
`claude-review.yml` and that it reviews each pull request. It does not, in 15 of
26 repositories, and has not for some time. Two causes:

1. **Missing `permissions: id-token: write` — was 11 repositories, now 1.** The
   action could not fetch an OIDC token and failed. This exact trap is *documented in
   DEVELOPMENT.md itself*, and a rollout on 2026-09-03 was meant to close it — it closed it
   in fifteen repositories, missed eleven, and nothing detected the difference. One of the
   eleven, `realmora`, was given the broken version *afterwards* by an agent
   copying an existing repository's workflow exactly as the standard instructs; the
   repository it copied was one of the unfixed ones.

   **Fixed 2026-09-05 in ten repositories**, verified by the error changing rather than by
   assuming: the OIDC failure is gone. `account` is deliberately not fixed — its
   `development` branch carries unmerged feature work, and promoting it to ship a
   one-line permission fix would ship that too.

2. **A second cause, still open, affecting every repository including the ten just fixed.**
   With the permission in place the action now authenticates and then fails inside
   execution (`result is_error:true`). Probable cause is a missing or invalid
   `CLAUDE_CODE_OAUTH_TOKEN` secret. Stated as probable, not known: repository
   secrets cannot be read through the API, so only the account owner can confirm it.

3. **A third cause, found 2026-09-08: the action refuses bot-triggered pushes by default.**
   An agent pushing through a GitHub App identity — the `jarvis-harithkavish[bot]`
   identity used throughout this ecosystem — is indistinguishable to the action from an
   untrusted bot, and it declines to run rather than review the content. This failed
   silently: no comment, no error visible on the pull request, only a failed run nobody was
   watching. **PR #29 was manually merged as a direct result** — the review that should have
   gated it had failed on this check four minutes earlier, and the merge proceeded on the
   strength of an older review of an earlier commit, not the one that shipped.

   Fixed by adding `allowed_bots: 'jarvis-harithkavish'`, scoped to the one identity
   rather than `'*'` (this is a public repository, and the action's own
   documentation warns that `'*'` lets any bot invoke it with a prompt that bot
   controls). Takes effect once on `main`, per the default-branch rule above.

   **Lesson generalised beyond this one fix:** every cause found this week — missing
   permission, missing workflow file, invalid token, now this — failed the same way: no
   error visible where anyone was looking, until someone checked the run directly. A green
   pull request and a working review are not the same fact, and this repository proved that
   to itself twice in five days.

Two lessons are worth keeping, because they generalise beyond this failure:

- **A documented trap is not a closed trap.** The failure mode was written down, and the
  written warning did not prevent eleven repositories from having it.
- **Copy-an-existing-repository is only as good as the repository copied.** The instruction
  to reuse a working workflow assumed the existing ones were working. Nothing checked.

### The first rule to reach rung 4

Branch protection was applied across all 26 repositories on 2026-09-08: pull request
required on `main`, `runway` and `development`, with
force-pushes and branch deletion refused. Approvals are set to **zero**, deliberately — the
requirement is that a change arrives through a pull request, not that a human clicks
approve, and requiring an approval would have broken the automated review's ability to
merge what it has just reviewed.

`enforce_admins` is **off**, so the owner retains an override. That is a
considered position rather than an oversight: the hotfix path in
[standards/BRANCHING.md](standards/BRANCHING.md) assumes someone can act quickly during an
incident, and a protection that cannot be lifted turns a bad hour into a worse one. It can
be turned on when the hotfix path has been exercised at least once.

**What this fixed is not hypothetical.** Before it, 20 of 26 repositories had
`development` and `runway` diverged from `main`, some by
sixty commits, because real work had gone straight to `main` for months. The
branching standard had been written, published, and read — and not followed. That divergence
is now structurally impossible rather than merely discouraged, which is the entire argument
for moving a rule down this ladder rather than restating it more firmly.

### Why the gap is recorded rather than resolved

A rule at rung 1–2 is guidance. Recording the distance to rung 3–4 is what stops the
ecosystem from believing it has enforcement it does not have — which is more dangerous
than knowing it has none, because nobody looks. This table is expected to change as rules
descend the ladder; an entry that has not moved in a long time is itself information.
