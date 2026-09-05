# HarithKavish Master Doctrine

The highest governance authority in the HarithKavish ecosystem.

This document states **principles only**. It does not contain commands, file paths,
branch names, framework instructions, workflows, or repository-specific rules. Those
belong in [standards](standards/), [protocols](protocols/), or the repositories
themselves. Anything procedural that appears here is a defect — see
[MAINTENANCE.md](MAINTENANCE.md).

There is **one current doctrine**. It applies to every participating repository.

---

## Article 1 — Governance Authority

The HarithKavish governance repository is the authoritative source for how repositories,
humans, and agents operate within this ecosystem. Where a repository's local practice
conflicts with governance, governance prevails. A document at a lower tier may extend a
higher tier but may never silently contradict it.

Authority tiers and conflict resolution are defined in
[GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md).

## Article 2 — One Current Doctrine

The doctrine is global and singular. Repositories do not pin, fork, or carry their own
version of it; they comply with the doctrine as it currently stands.

Because the doctrine can change after a repository was last touched, compliance is
brought about **deliberately**. A repository that detects it has fallen behind reports
the gap and closes it as scoped work. It does not silently rewrite itself to catch up.

## Article 3 — Single Source of Truth

Every shared concern — design language, governance, identity, shared infrastructure —
has exactly one authoritative home. Other repositories reference that home; they do not
copy it, vendor it, or maintain a parallel version of it.

Duplication of a shared concern is treated as a defect, not a convenience. Where a copy
is genuinely unavoidable, it is declared as an exception under Article 10 and carries a
pointer back to its source.

## Article 4 — Shared Design Language

All public surfaces in the ecosystem derive their visual and interaction language from
the shared design system. Repositories consume shared foundations; they do not redefine
them independently.

Local, repository-specific components are legitimate when a need is genuinely local.
When a local solution proves reusable, it is promoted back into the shared system rather
than re-invented elsewhere. Boundaries and promotion criteria live in
[standards/DESIGN_SYSTEM.md](standards/DESIGN_SYSTEM.md).

## Article 5 — Repository Integrity

Every participating repository is self-describing. Without opening a single source file,
a human or an agent must be able to learn what the repository is, what it is for, where
it fits in the ecosystem, which governance applies to it, how it reaches production,
and how to begin work in it.

A repository that cannot be understood from its own surface is non-compliant regardless
of the quality of the code inside it.

Where a repository fits is a decision, not a default. Every repository under the
ecosystem's account is either a participant or explicitly not one, and that answer is
recorded and kept current. A repository whose membership has never been decided is an
open question, not a silent exclusion; it is resolved by asking the owner, never by an
agent assuming either answer.

Integrity also bounds what a repository may hold: it never contains a credential, a
secret, or personal data. What enters a repository is effectively permanent, so this is
a property of the repository, not of any single commit. Concrete requirements live in
[standards/REPOSITORY.md](standards/REPOSITORY.md) and
[standards/SECURITY.md](standards/SECURITY.md).

## Article 6 — Protected Production

Each repository has one branch that represents its production or stable state. That
branch is protected. Change reaches it through review and integration, never through
direct implementation work.

## Article 7 — Isolated Development

Implementation work happens in isolation from the production branch and integrates
through a designated development branch. Exceptional paths — such as urgent production
fixes — are permitted, but they are explicit, narrow, and reconciled back into the
normal flow rather than becoming a second habit.

Branch names, flow, and the exception path live in
[standards/BRANCHING.md](standards/BRANCHING.md).

## Article 8 — Discovery Before Modification

No agent or human modifies a repository before discovering the governance and the
repository context that apply to the work. Assumption is not discovery, and training
data is not discovery.

Discovery is progressive: read what the task requires, not everything that exists. The
procedure is defined in [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md).

## Article 9 — Bounded Autonomy

An agent acts within the scope it was given. Discovering non-compliance is **not**
authorization to remediate it.

Governance metadata may be added safely. Substantive changes to architecture, design, or
structure require the scope to have been requested. Where an agent finds a gap outside
its scope, it reports the gap and stops; it does not expand the task to close it.

## Article 10 — Explicit Exception

Deviation from governance is permitted and sometimes correct. Silent deviation is not.

An exception is written down where the deviation lives, states what is deviated from,
why, and what would end it. An undeclared deviation is a defect even when the underlying
decision was sound.

## Article 11 — Enforcement Follows Governance

These documents guide humans and agents; they do not, by themselves, prevent anything.
Rules that matter are expected to descend over time from guidance into infrastructure —
branch protection, review requirements, and automated validation.

Governance is therefore written so that enforcement can be added later without rewriting
the rule. The enforcement ladder is described in
[GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md).

## Article 12 — Governance Maintenance

Governance is itself governed. Rules are created, moved, merged, and retired through the
process in [MAINTENANCE.md](MAINTENANCE.md), which decides the tier a rule belongs to
before it is written.

This doctrine is expected to stay approximately its current size. Growth belongs in the
tiers below it. Improving or consolidating an existing article is preferred over adding
a new one.
