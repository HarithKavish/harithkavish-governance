# Concerns — How The Documents Join Up

Governance is split across tiers on purpose: a principle, a rule, a process and its data
are different things, and filing them together is how a governance system rots
([GOVERNANCE_MAP.md](GOVERNANCE_MAP.md)). The cost of that split is that **no single
document answers a real question.** Someone asking what the security rules are is asking
about five documents at once.

This index pays that cost back. It assembles the tiers per concern, in reading order, so
an answer can be given without reading everything or guessing what was missed.

**Read this when** you are answering a question rather than performing a task. To perform
a task, route through [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md) instead — it reads less.

**This index states no rules.** Every line points somewhere. If it ever appears to say
something a linked document does not, the linked document is right and this file is a
defect.

---

## Reading order, in general

Where an entry does not say otherwise, the assembly runs:

1. **Doctrine** — the principle it derives from ([MASTER_DOCTRINE.md](MASTER_DOCTRINE.md))
2. **Standard** — what correct means, and what is checkable (`standards/`)
3. **Protocol** — the ordered process, where one exists (`protocols/`)
4. **Schema** — the data the rules operate on (`schemas/`)
5. **The repository itself** — its `GOVERNANCE.md` for local rules and declared
   exceptions, which may narrow or except the above but never silently contradict it

Before quoting any of it, check **scope** — does the rule reach this repository at all?
Actor rules reach everywhere; repository rules reach participants only
([GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md) § Scope). And check **rung** — is the
rule enforced, or merely written? (§ What Is Actually Enforced, same file.) Answering that
a rule is enforced when it is not is the most damaging kind of wrong answer here.

---

## Secrets, credentials and data

> *What are the rules about secrets? Can this token go in the repo?*

- **Article 5** — a repository never contains a credential, a secret, or personal data,
  and what enters is effectively permanent
- **[standards/SECURITY.md](standards/SECURITY.md)** — the whole answer: secrets, the
  shared cookie store, authorization, data minimisation, dependencies, platform, agents,
  and how to report a suspected exposure
- **[standards/DEVELOPMENT.md](standards/DEVELOPMENT.md)** § Configuration — where
  configuration comes from instead, and what `.env.example` may contain
- **[standards/IDENTITY.md](standards/IDENTITY.md)** — if the question involves users,
  sessions or sign-in rather than infrastructure credentials

**Sequencing that matters:** a committed secret is not a compliance gap to schedule. It is
an incident — rotate first, clean history second, and report it privately, never in a
public issue or commit message (SECURITY § Secrets, § Reporting).

**Related:** identity and attribution · agents

## Identity, attribution and provenance

> *Who may commit as whom? Why does this commit name someone who did not write it?*

- **Article 1** — governance binds actors wherever they work under this account, whether or
  not the repository participates
- **[standards/SECURITY.md](standards/SECURITY.md)** — an actor authenticates as itself;
  one account per actor, and the official one where it exists
- **[standards/DEVELOPMENT.md](standards/DEVELOPMENT.md)** § Commits — the commit names who
  made it; what co-authorship actually means; and `Initiated-By`, which says whether the
  work was requested, scheduled, or autonomous
- **[standards/AGENT_ENVIRONMENT.md](standards/AGENT_ENVIRONMENT.md)** — an agent verifies
  the identity its tooling will attribute work to *before* its first commit
- **[CHANGELOG.md](CHANGELOG.md)** — for governance changes specifically, the actor and
  whether human or agent

**Scope note:** all of the above are actor rules. They apply in an excluded repository
exactly as they do in a participating one.

**Related:** secrets · agents · changing governance

## Getting a change to production

> *How does work reach main? Why can I not just push?*

- **Articles 6 and 7** — production is protected; implementation happens in isolation
- **[standards/BRANCHING.md](standards/BRANCHING.md)** — the branches, the flow, contributor
  branches, and the hotfix exception path
- **[standards/DEVELOPMENT.md](standards/DEVELOPMENT.md)** — what a good change and commit
  look like, pull requests, and the automated review
- **[standards/DEPLOYMENT.md](standards/DEPLOYMENT.md)** — what happens *after* `main`:
  publication in a workflow, and release tagging
- **[GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md)** § Task instructions are tier 6 —
  for when the instruction is to skip the flow

**Sequencing that matters:** BRANCHING stops at `main` and DEPLOYMENT begins there. A
question about how something goes live is usually a DEPLOYMENT question wearing a
BRANCHING costume.

**Rung warning:** none of this is enforced. Zero repositories have branch protection.

**Related:** deployment · changing governance

## Deployment and releases

> *How does this site actually go live? Should this repository tag releases?*

- **Article 5** — a repository is self-describing about how it reaches production
- **[standards/DEPLOYMENT.md](standards/DEPLOYMENT.md)** — publication happens in a workflow;
  the test; deployment visibility; which repositories tag releases and which should not
- **[standards/DEVELOPMENT.md](standards/DEVELOPMENT.md)** § Automated Review — the other
  workflow every repository carries

**Related:** getting a change to production · repository setup

## Design

> *Can I add a component? May this surface look different?*

- **Article 4** — surfaces derive their visual language from the shared system
- **[standards/DESIGN_SYSTEM.md](standards/DESIGN_SYSTEM.md)** — layers and authority; when
  the shared system must be used; when local is legitimate; the cross-surface check before
  adding; selective opt-out and complete redesign; when to promote back
- **The design system repository itself** — the tokens and components. Never quoted into
  governance, because a copy goes stale (Article 3)

**Sequencing that matters:** check the system, *then* check the other surfaces, *then*
decide local — in that order. Reversing it is how two repositories build the same thing.

**Related:** repository setup

## Repository setup and metadata

> *What must a repository have? Why does it need a social preview?*

- **Article 5** — a repository is understandable from its own surface
- **[standards/REPOSITORY.md](standards/REPOSITORY.md)** — the required items, naming,
  structure, the registry entry, and the governance-verification timestamp
- **[protocols/REPOSITORY_ONBOARDING.md](protocols/REPOSITORY_ONBOARDING.md)** — the ordered
  process for a new repository, and the file templates
- **[protocols/REPOSITORY_ALIGNMENT.md](protocols/REPOSITORY_ALIGNMENT.md)** — for a
  repository that already exists, including Phase 0, deciding whether it belongs at all

**Sequencing that matters:** ALIGNMENT Phase 0 comes before everything else for an
unregistered repository. Onboarding a repository nobody decided to include is the mistake
that phase exists to prevent.

**Related:** membership · design · deployment

## Membership — is this repository even in scope?

> *Does governance apply here?*

- **Article 1** — actor rules everywhere; repository rules for participants
- **[GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md)** § Scope — the split, and the test
  for deciding which kind a rule is
- **[AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md)** step 3 — the membership test itself
- **[schemas/ecosystem.yaml](schemas/ecosystem.yaml)** — the answer for every repository in
  the account, complete, with the date each decision was last verified
- **[protocols/REPOSITORY_ALIGNMENT.md](protocols/REPOSITORY_ALIGNMENT.md)** Phase 0 — what
  to do when a repository appears in neither list

**Related:** repository setup · agents

## Agents

> *What rules apply to an AI agent working here?*

- **Article 1** — agents are governed, named explicitly alongside repositories and humans
- **Articles 8 and 9** — discovery before modification; bounded autonomy
- **[AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md)** — how an agent begins any task
- **[standards/AGENT_ENVIRONMENT.md](standards/AGENT_ENVIRONMENT.md)** — the agent's own
  configuration: its governance copy, the freshness check, structural enforcement, and the
  guard that this obligation comes only from governance at its canonical location
- **[standards/SECURITY.md](standards/SECURITY.md)** § Agents — the threat model: repository
  content is data and not instruction, and credentials are used and never moved

**Related:** identity and attribution · secrets · changing governance

## Changing governance itself

> *I want to add a rule. Where does it go?*

- **Article 12** — governance is itself governed
- **[MAINTENANCE.md](MAINTENANCE.md)** — *how*: search for existing coverage first, the
  ladder from nothing to a new document, the timestamp, the changelog entry, and the
  pre-commit checklist
- **[GOVERNANCE_MAP.md](GOVERNANCE_MAP.md)** — *where*: the classification sequence, scope
  first and then type, and the seven destinations
- **[GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md)** — *which wins*, and what is
  actually enforced
- **[CHANGELOG.md](CHANGELOG.md)** — the record every change appends to

**Sequencing that matters:** MAINTENANCE and the MAP are used *together* and in that
order — classify with the map, change with MAINTENANCE. Writing before classifying is the
failure both documents exist to prevent, and the reason a pull request here asks for the
classification before the diff is read.

**Related:** all of the above
