# Protocol — Repository Onboarding

How a **new** repository joins the HarithKavish ecosystem.

For an existing repository that already has code and history, use
[REPOSITORY_ALIGNMENT.md](REPOSITORY_ALIGNMENT.md) instead — that path has to account for
what is already there.

**Outcome:** any agent entering the repository later can discover, without being told,
that HarithKavish governance applies and where to find it.

---

## Principle

The repository carries a **pointer**, not a copy.

Two small files make the repository self-describing. Governance itself stays in one place
and is read from there (Article 3). If onboarding ever involves copying doctrine,
standards, or design tokens into the repository, it is being done wrong.

---

## The Two Files

| File | Answers | Audience |
|---|---|---|
| `AGENTS.md` | *How do I work here?* | Agents, first contact |
| `GOVERNANCE.md` | *What governs this repository?* | Agents and humans |

`AGENTS.md` is the entry point and holds repository-specific working rules.
`GOVERNANCE.md` declares membership, points outward, and records exceptions.

Keep them separate. Merging them produces one file that is both too long to read first
and too short to hold local rules.

---

## Steps

### 1. Create the repository

Name it per [standards/REPOSITORY.md](../standards/REPOSITORY.md): lowercase, hyphenated,
named for the thing. Where it serves a subdomain, the name matches the subdomain label.

### 2. Create the branches

Create `main`, then `development` from it ([standards/BRANCHING.md](../standards/BRANCHING.md)).
Do this before any implementation work, so the first feature branch has somewhere to
start from.

### 3. Add `GOVERNANCE.md`

```markdown
# Governance

This repository is part of the **HarithKavish ecosystem** and is governed by
[HarithKavish Governance](https://github.com/HarithKavish/harithkavish-governance).

Governance is read from that repository. It is not copied here.

## Start here

Agents: read [AGENTS.md](AGENTS.md) first, then follow
[AGENT_BOOTSTRAP.md](https://github.com/HarithKavish/harithkavish-governance/blob/main/AGENT_BOOTSTRAP.md).

## This repository

- **Role:** <website | application | shared library | service | infrastructure>
- **Surface:** <live URL, or "none">
- **Production branch:** `main`
- **Development branch:** `development`

## Especially applicable

<Link only the standards this repository actually touches. Delete the rest.>

- [REPOSITORY](https://github.com/HarithKavish/harithkavish-governance/blob/main/standards/REPOSITORY.md)
- [BRANCHING](https://github.com/HarithKavish/harithkavish-governance/blob/main/standards/BRANCHING.md)
- [DESIGN_SYSTEM](https://github.com/HarithKavish/harithkavish-governance/blob/main/standards/DESIGN_SYSTEM.md)
- [DEVELOPMENT](https://github.com/HarithKavish/harithkavish-governance/blob/main/standards/DEVELOPMENT.md)
- [SECURITY](https://github.com/HarithKavish/harithkavish-governance/blob/main/standards/SECURITY.md)

## Declared exceptions

<Article 10. Every deviation from governance is recorded here, with the reason and what
would end it. "None." is a valid and expected entry for a new repository.>

None.
```

### 4. Add `AGENTS.md`

```markdown
# Agent Instructions

This repository is part of the **HarithKavish ecosystem**.

**Before changing anything**, read
[AGENT_BOOTSTRAP.md](https://github.com/HarithKavish/harithkavish-governance/blob/main/AGENT_BOOTSTRAP.md)
and follow it. See [GOVERNANCE.md](GOVERNANCE.md) for what governs this repository.

Do not begin implementation work before discovery is complete.

## Hard stops

A reminder, not the rule. These restate doctrine articles so an agent that reads nothing
else still has the guardrails. Governance is authoritative; if these ever disagree with
it, governance wins.

- Do not commit to the production branch (Article 6).
- Do not commit secrets or credentials (Article 5, SECURITY).
- Do not redefine design foundations locally (Article 4).
- Do not copy governance or the design system into this repository (Article 3).
- Do not act outside the scope you were given (Article 9).

## About this repository

<One paragraph: what this is and what it does.>

## Working here

<Repository-specific rules only — the things that are true HERE and are not already
covered by global governance. Setup, commands, and architecture belong in README.md or
docs/, not in this file. If this section is empty, say so rather than restating global
rules.>
```

### 5. Add `README.md`

Per [standards/REPOSITORY.md](../standards/REPOSITORY.md). It serves humans and describes
how the repository works. It does not restate governance — it links to `GOVERNANCE.md`.

### 6. Set repository metadata

Per [standards/REPOSITORY.md](../standards/REPOSITORY.md):

- **About description** — one sentence.
- **Homepage URL** — if there is a live surface.
- **Topics** — recommended.
- **Social preview image** — create it, commit the source at `.github/social-preview.png`,
  and upload it in repository settings. The upload has no API and must be done by a
  human; say so explicitly rather than reporting the item as complete.

### 7. Add automated PR review

Add `.github/workflows/claude-review.yml` per
[standards/DEVELOPMENT.md § Automated Review](../standards/DEVELOPMENT.md#automated-review),
and set the `CLAUDE_CODE_OAUTH_TOKEN` secret on the repository. Use the workflow content
from an existing ecosystem-member repository rather than writing it from scratch — it
carries a permissions requirement (`id-token: write`) that fails silently, with no review
posted and no visible error, when it is missing.

### 8. Register the repository

Add an entry to [schemas/ecosystem.yaml](../schemas/ecosystem.yaml) in the governance
repository. A repository that is not registered is not discoverable as a member.

This is a change to the governance repository and follows its own branching rules.

### 9. Verify

- [ ] `main` and `development` exist
- [ ] `AGENTS.md`, `GOVERNANCE.md`, `README.md` present at the root
- [ ] About description set
- [ ] Social preview committed, and the manual upload either done or explicitly flagged
- [ ] Homepage URL set, if applicable
- [ ] `claude-review.yml` present and `CLAUDE_CODE_OAUTH_TOKEN` set
- [ ] Registered in `schemas/ecosystem.yaml`
- [ ] Nothing from governance or the design system was copied in

---

## Notes

**`AGENTS.md` may already exist.** Some toolchains generate and re-write blocks inside it
— Next.js maintains its own delimited section, for example. Add the governance content
alongside such a block; do not replace the file and do not delete a machine-managed
section, which will simply be regenerated.

**The `Hard stops` block is the one deliberate restatement in this system.** It is
anchored to doctrine articles rather than to standards, because doctrine is the tier least
likely to change, and it declares itself subordinate. Do not extend it with
standard-level detail — branch names, token values, file paths — which would go stale in
every repository at once.

**Keep both files short.** They are read first, on every task. Length here is paid for
repeatedly. Anything that grows past a screen probably belongs in `README.md`, in `docs/`,
or — if it is global — in governance, under [MAINTENANCE.md](../MAINTENANCE.md).
