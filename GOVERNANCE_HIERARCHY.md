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

### Standards vs. Protocols

The distinction matters, because misfiling is the main way governance rots.

- A **standard** describes a required *state*. "Every repository has a description."
- A **protocol** describes a required *procedure*. "This is how a repository is onboarded."

If it can be checked at rest, it is a standard. If it only makes sense as a sequence of
steps someone performs, it is a protocol. When a rule has both a state and a procedure,
the state goes in the standard and the procedure goes in the protocol, and each links to
the other rather than restating it.

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

Initial enforcement targets, not yet implemented: protected production branches, required
pull requests, and automated repository-metadata and design-system validation.
