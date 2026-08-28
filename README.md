# HarithKavish Governance

The central governance source for the HarithKavish ecosystem.

This repository is not a website and not an application. It defines how repositories,
humans, and AI agents operate across the ecosystem, so that independently evolving
projects stay architecturally and visually coherent.

**Agents start at [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md).**

---

## Using it

Tell an agent:

> Read and follow the HarithKavish governance before implementing this.

It should then discover the applicable governance, read the doctrine, read only the
standards its task touches, read the repository's own rules, and implement within those
constraints — without being walked through the ecosystem each time.

## The problem it solves

Repositories drift. Design implementations diverge, shared patterns get duplicated and
then modified independently, workflows differ per project, and agents fill the gaps with
assumptions. Each drift is individually reasonable and collectively fatal to a coherent
ecosystem.

Central governance replaces those assumptions with a single discoverable source.

## The structure

```
Master Doctrine        principles         what must always be true
      ↓
Global Standards       requirements       what "correct" means
      ↓
Global Protocols       procedures         how a process is carried out
      ↓
Repository Rules       local context      what is true of THIS repository
      ↓
Implementation         the work
```

Each tier is more specific and less authoritative than the one above it. Lower tiers
extend higher tiers; they never silently contradict them.

## The documents

| Document | Responsibility |
|---|---|
| [MASTER_DOCTRINE.md](MASTER_DOCTRINE.md) | The principles. Deliberately short. |
| [GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md) | Which document wins, and what to do when none does. |
| [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md) | How an agent begins work. The entry point. |
| [MAINTENANCE.md](MAINTENANCE.md) | How governance itself changes, without bloating. |

### Standards — what "correct" means

| | |
|---|---|
| [BRANCHING](standards/BRANCHING.md) | Branch model, flow, naming, the hotfix exception |
| [DESIGN_SYSTEM](standards/DESIGN_SYSTEM.md) | Shared vs. local components, and promotion back |
| [DEVELOPMENT](standards/DEVELOPMENT.md) | Changes, commits, dependencies, testing |
| [REPOSITORY](standards/REPOSITORY.md) | Description, social preview, README, structure |
| [SECURITY](standards/SECURITY.md) | Secrets, auth, data, and agent-specific risk |

### Protocols — how a process is carried out

| | |
|---|---|
| [REPOSITORY_ONBOARDING](protocols/REPOSITORY_ONBOARDING.md) | A new repository joins |
| [REPOSITORY_ALIGNMENT](protocols/REPOSITORY_ALIGNMENT.md) | An existing repository adopts governance |

### Registry

[schemas/ecosystem.yaml](schemas/ecosystem.yaml) — which repositories are members, what
each one is, and how far each has adopted governance.

## How repositories participate

A participating repository carries two small files — `AGENTS.md` and `GOVERNANCE.md` —
that point here. Governance is **read** from this repository, never copied into others.
That is what keeps one authoritative source from becoming many divergent ones.

Templates are in [REPOSITORY_ONBOARDING.md](protocols/REPOSITORY_ONBOARDING.md).

## Two things to know before contributing

**The doctrine is global and current.** There are no per-repository doctrine versions. But
a doctrine change modifies **no repository automatically** — repositories discover the gap
at their next bootstrap and close it as scoped work. An ecosystem that self-modifies on
doctrine change is one where a single bad edit rewrites every website.

**Guidance is not enforcement.** Nothing here prevents anything yet. Rules are expected to
descend over time into branch protection, review requirements, and CI validation. Each
standard states the rung it is currently on, so the gap between intent and reality stays
visible.

## Changing governance

Read [MAINTENANCE.md](MAINTENANCE.md) first. Classify the change before writing it — the
correct outcome is often "this already exists" or "this belongs in your repository, not
here."

The Master Doctrine is expected to stay approximately its current size. Detail belongs in
the tiers below it.
