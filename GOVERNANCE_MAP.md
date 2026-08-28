# Governance Map

**The routing layer.** It answers one question:

> I have a new requirement, rule, principle, process, configuration, or instruction.
> **Where does it belong?**

Read this when you are **changing governance**. Ordinary application work does not need
it — an agent implementing a feature routes through
[AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md) instead and never opens this file.

---

## Where This Sits

Three documents govern the governance system. They do not overlap:

| Document | Answers |
|---|---|
| **GOVERNANCE_MAP.md** (this) | **Where** does content belong? |
| [MAINTENANCE.md](MAINTENANCE.md) | **How** is a governance change made safely? |
| [GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md) | **Which wins** when two documents disagree? |

Routing, process, authority. This document classifies; it does not describe how to search
for existing coverage, how to apply a change, or which tier outranks which.

---

## The Seven Destinations

| # | Destination | Holds | Location |
|---|---|---|---|
| 1 | **Doctrine** | Fundamental, global, long-term principles | `MASTER_DOCTRINE.md` |
| 2 | **Standard** | Mandatory reusable rules and conventions | `standards/` |
| 3 | **Protocol** | Ordered operational processes | `protocols/` |
| 4 | **Schema** | Machine-readable structures and metadata | `schemas/` |
| 5 | **Maintenance** | Rules governing governance itself | `MAINTENANCE.md`, this file |
| 6 | **Repository-specific** | Rules true of one repository | That repo's `AGENTS.md` / `GOVERNANCE.md` |
| 7 | **Implementation** | How something is actually built | That repo's `README.md`, `docs/`, or code |

Destinations 6 and 7 are **outside this repository**. Routing a requirement out of central
governance is a correct and common outcome, not a failure to place it.

> **Note on structure.** Doctrine and Maintenance are single root files, not directories
> (`MASTER_DOCTRINE.md`, `MAINTENANCE.md`). They are governance *areas* with one document
> each. Standards, protocols, and schemas are directories because they hold many.

---

## The Classification Sequence

Classification runs in two gates. **Scope first, then type.**

```text
NEW REQUIREMENT
      |
      +- GATE A -- WHO does it govern? --------------------------
      |
      |   The governance system itself?  --> MAINTENANCE  (or this map,
      |                                      if it defines a category)
      |   One repository?                --> REPOSITORY-SPECIFIC
      |   One implementation?            --> IMPLEMENTATION
      |   The whole ecosystem?           --> continue to Gate B
      |
      +- GATE B -- WHAT KIND of statement is it? ----------------
          |
          |   A fundamental, tool-independent principle?  --> DOCTRINE
          |   A mandatory reusable rule or convention?    --> STANDARD
          |   An ordered sequence of actions?             --> PROTOCOL
          |   A structure software must read or validate? --> SCHEMA
          |
          +- Fits more than one? --> It is layered. DECOMPOSE it (below).
```

Within each gate, the **first** match wins.

**Why scope is asked first.** Type alone misroutes. "Classify a requirement before adding
it" is an ordered process, so a pure type ladder files it as a Protocol — but it governs
governance, so it belongs in Maintenance. Asking *who it governs* before *what kind it is*
removes that failure. This refines the ordering; it does not change the classification
logic.

---

## The Categories

Each entry defines a boundary. It does not restate the content of the documents it routes
to — follow the link for that.

### 1 · Doctrine — `MASTER_DOCTRINE.md`

> **Answers:** What fundamental principles must the HarithKavish ecosystem follow?

**Qualifies only if _every_ one is true:**

- **Global** — applies to every repository, not most of them.
- **Fundamental** — other rules derive from it; it derives from none.
- **Long-term** — still true after a complete technology change.
- **Principle-based** — states an outcome, not a method.
- **Tool-independent** — no framework, platform, or vendor.
- **Not already expressible** as detail under an existing article.

If any answer is "no," it is not doctrine.

> **Doctrine test:** could you replace every framework, host, and language in the
> ecosystem and the rule still holds, word for word? If not, it belongs lower.

**Belongs here:** shared concerns have one authoritative source · architectural integrity
is preserved · production is protected · agents discover constraints before modifying.

**Does not belong here:** commands · file paths · framework instructions · detailed
workflows · branch naming patterns · tool configuration · repository-specific rules ·
temporary requirements · anything carrying a version number.

Doctrine is read on every task in the ecosystem, so every line added is paid for
repeatedly. **Prefer sharpening an existing article over adding one.**

### 2 · Standard — `standards/`

> **Answers:** What concrete requirements must systems follow?

A mandatory, reusable rule that implements a doctrine principle. Global in intent, and
free to be specific about names, values, structures, and thresholds.

**Test: is it checkable at rest?** If you can inspect a repository at a point in time and
say compliant or not, it is a standard.

**Belongs here:** the production branch is protected · websites use the shared design
system · shared design foundations are not redefined locally · every repository has a
description.

Standards describe **requirements**, not step-by-step processes. Most real rules belong
here — this is the default destination, not doctrine.

### 3 · Protocol — `protocols/`

> **Answers:** What process must be followed?

An ordered procedure with a beginning, a decision path, and an end.

**Test: does it only make sense as a sequence?** If reordering the steps breaks it, it is
a protocol.

**Belongs here:** agent repository discovery · repository adoption · architecture review ·
incident response.

### 4 · Schema — `schemas/`

> **Answers:** How is this information represented and validated?

A machine-readable structure: configuration formats, metadata definitions, validation
structures — things software, automation, or agents parse rather than read.

**Test: does a program need to consume it?** Prose is for humans; a schema is for code.

**A schema never replaces human-readable governance.** It represents a rule that is
already stated somewhere, or it holds data that rules operate on. A schema is usually the
*companion* to a standard, not a substitute for one. If a requirement exists only as a
schema, its rule has not been written yet.

### 5 · Maintenance — `MAINTENANCE.md` and this document

> **Answers:** How does the governance system evolve without losing structure and
> discipline?

Rules about governance itself. Split between two documents:

- **This map** — what each category is for, and where content belongs.
- **`MAINTENANCE.md`** — how a change is searched for, applied, verified, and propagated.

**Belongs here:** classify before adding · avoid doctrine growth · consolidate duplicates ·
check changes for contradictions · preserve responsibility boundaries.

**Does not belong here:** ordinary application development rules. Maintenance governs the
governance repository, not the code in other repositories. A rule about how *websites* are
built is a Standard even if it feels administrative.

### 6 · Repository-Specific — that repository's `AGENTS.md` / `GOVERNANCE.md`

> **Answers:** What is true of *this* repository?

Requirements that apply to one repository. **These do not belong in central governance at
all** — they belong in the repository they govern.

**Belongs there:** repository architecture · local dependencies · project-specific
deployment · internal directory conventions · application-specific constraints.

Central governance may define **templates and requirements for** repository documentation
(see [standards/REPOSITORY.md](standards/REPOSITORY.md) and
[protocols/REPOSITORY_ONBOARDING.md](protocols/REPOSITORY_ONBOARDING.md)). It is not the
storage location for individual repositories' rules.

**Test:** would this rule be meaningless, or wrong, in a different repository? Then it is
repository-specific.

### 7 · Implementation — the owning system

> **Answers:** How is this actually built?

**Belongs there:** CSS values · component implementation · API endpoints · framework
configuration · build commands.

Governance defines constraints and expectations. It does not contain the implementation
that satisfies them. Governance says a surface must use shared design foundations; the
token values live in the design system.

**Test:** does it describe how something *works* rather than what is *required*? Then it
is implementation.

---

## Decomposing a Layered Requirement

One requirement often carries several layers. **Do not file them together.** Split them
and let each layer land where it belongs.

Worked example — production stability:

| Layer | Statement | Destination |
|---|---|---|
| Principle | Production stability must be protected | Doctrine |
| Rule | The production branch is protected | Standard |
| Process | Work follows the approved branching workflow | Protocol |
| Data | Which branch is production, per repository | Schema |

The same requirement, four homes. Each is stated **once**, and the others link to it
rather than repeat it.

**How to decompose.** Strip the requirement down: what is the principle underneath it,
and what would remain true if every tool changed? That is the doctrine layer — and often
it already exists, in which case nothing is added there. What is the checkable rule? That
is the standard. What must be *done*, in order? That is the protocol.

A requirement that cannot be decomposed is usually a single-layer requirement, which is
normal. Most are.

---

## Structural Discipline

**Topic is not destination.**

A requirement does not belong in a document because the document is *about that topic*. It
belongs where its **responsibility and classification** put it.

Branching is the standing example. Branching matters globally, so it is tempting to put
branching rules in the doctrine. That is wrong:

- The principle that production must be protected → **Doctrine**
- The concrete rule that `main` is protected and `development` integrates → **Standard**
- The step-by-step workflow for taking work through those branches → **Protocol**

Three destinations, one topic. This distinction is the point of the whole system.

The same trap in other forms:

| Tempting reasoning | Why it misroutes |
|---|---|
| "Security is critical, so it is doctrine." | Criticality is not fundamentality. Most security rules are checkable requirements → Standard. |
| "It is about the design system, so it goes in `DESIGN_SYSTEM.md`." | Only if it is a *rule*. A promotion procedure is a Protocol; a token value is Implementation. |
| "It is administrative, so it is Maintenance." | Maintenance governs *governance*. A rule about repositories is a Standard. |
| "Agents need it, so it goes in `AGENT_BOOTSTRAP.md`." | Bootstrap is the discovery *process*. The rules it routes to live in their own homes. |

---

## Introducing a New Category

Adding a new top-level governance category — a sibling of Doctrine, Standards, Protocols,
Schemas, or Maintenance — is a structural change to the whole ecosystem. It is rare, and
it is not done casually.

Before any new category is created, it must be checked **against this document** and must
satisfy all of the following.

**1 — Prove there is no overlap.** State, against each of the seven existing destinations,
why the content does not already belong there. If it fits an existing category even
awkwardly, it belongs there — an awkward fit is a wording problem, not a missing category.
Overlapping categories are worse than a crowded one, because they make routing
non-deterministic and turn every future placement into a judgement call.

**2 — Define what it is for, in this document.** A new category is not real until it has
an entry here carrying the same shape as the others:

- The question it answers.
- What belongs in it.
- What does not belong in it, especially against its nearest neighbour.
- A one-line test that decides membership.
- Its position in the classification sequence, and why it sits there.

**3 — Place it in the sequence.** Say which gate it is asked in, and in what order. A
category that cannot be reached by the sequence is unreachable in practice.

**4 — Establish its authority.** Add it to the tier table in
[GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md). A category with no defined precedence
cannot be used to resolve a conflict.

**5 — Propagate it to the ecosystem.** A new category must flow down to every repository,
or it exists only here:

- Add its routing row to [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md), so agents can discover
  and reach it.
- Add it to the document map in [README.md](README.md).
- Propagate by the normal rule — **no repository is modified as part of the change**.
  Repositories discover it at their next bootstrap and close any gap as scoped work
  ([MAINTENANCE.md](MAINTENANCE.md),
  [protocols/REPOSITORY_ALIGNMENT.md](protocols/REPOSITORY_ALIGNMENT.md)).

**6 — Perform the change under `MAINTENANCE.md`.** This document says what a new category
must satisfy. `MAINTENANCE.md` governs how the change is made and verified.

Retiring a category follows the same path in reverse: its content is relocated first, its
definition is removed here, and every reference to it is cleared.

---

## Placement Summary

| Classification | Destination |
|---|---|
| Doctrine | `MASTER_DOCTRINE.md` — as a sharpened existing article where possible |
| Standard | the matching file in `standards/` |
| Protocol | the matching file in `protocols/` |
| Schema | the matching file in `schemas/` |
| Maintenance — process | `MAINTENANCE.md` |
| Maintenance — classification | this document |
| Ecosystem membership or role | `schemas/ecosystem.yaml` |
| Repository-specific rule | that repository's `AGENTS.md` or `GOVERNANCE.md` |
| Implementation detail | that repository's `README.md`, `docs/`, or code |

Write it **once**, in one place. Everywhere else links to it.

Classification is the first half of the job. Apply the change under
[MAINTENANCE.md](MAINTENANCE.md).
