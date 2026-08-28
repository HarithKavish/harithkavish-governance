# Governance Maintenance

How governance itself is changed.

Read this **before** creating, modifying, moving, merging, or removing any rule in this
repository. Governance systems do not fail because rules are wrong. They fail because
rules accumulate in the wrong places until nobody can tell what is authoritative.

This document exists to prevent that.

---

## The Default Answer Is Not "Add a File"

Ranked, most preferred first:

1. **Nothing** — the requirement is already covered. Find it and point at it.
2. **Improve an existing rule** — sharpen wording, close the gap, add the missing case.
3. **Consolidate** — two rules overlap; merge them into one authoritative statement.
4. **Relocate** — the rule is real but filed at the wrong tier. Move it.
5. **Add a rule to an existing document** — the concern has a home; the rule is new.
6. **Add a new document** — only when a genuinely new concern has no home at all.

Reaching option 6 should be rare. A new document must name a concern that no existing
document owns, and adding it must not make an existing document's responsibility unclear.

---

## Step 1 — Is It Already Covered?

Search before writing. If a rule already covers the requirement:

- **Adequately** → stop. Point at it. Do not restate it in a second place; two statements
  of one rule drift apart and then conflict.
- **Partially** → improve the existing rule. Do not add a second, adjacent one.
- **In the wrong place** → go to Step 3.

Restating an existing rule in a new location is the single most common way this system
would degrade. It is never the correct action.

---

## Step 2 — Classify the Change

Answer in order. The **first** tier that fits is the answer.

### 1 · Doctrine — `MASTER_DOCTRINE.md`

Only if **all** of the following are true:

- **Global** — applies to every repository, not most of them.
- **Fundamental** — other rules derive from it; it does not derive from another rule.
- **Long-term** — it would still be true after a full technology change.
- **Principle-based** — it states an outcome, not a method.
- **Not framework-, tool-, platform-, or vendor-specific.**
- **Not expressible as detail under an existing article.** Prefer sharpening an article
  over adding one.

If any answer is "no," it is not doctrine.

**Doctrine test:** could you switch every framework, host, and language in the ecosystem
and the rule still holds, unchanged? If not, it belongs lower.

### 2 · Standard — `standards/`

It defines what "correct" looks like for a concern, and it is checkable at rest.
Global in intent, but may be specific about names, values, structure, and thresholds.

Standards are where most real rules belong.

### 3 · Protocol — `protocols/`

It defines a **procedure** — an ordered process someone carries out, with a beginning, a
decision path, and an end. If it only makes sense as steps, it is a protocol.

If the rule has both a required state and a procedure, split it: state to the standard,
procedure to the protocol, each linking to the other.

### 4 · Repository-Specific Rule — the repository's own `AGENTS.md` / `GOVERNANCE.md`

It applies to one repository, or to how one repository satisfies a global rule. It does
not belong in this repository at all. This is not a lesser outcome — it is the correct
home for most rules people try to add globally.

### 5 · Implementation Detail — the repository's `README.md` or `docs/`

It describes how something works rather than what is required. Commands, setup steps,
architecture notes, and environment specifics are documentation, not governance.

Governance says what must be true. Documentation says how it currently is.

---

## Step 3 — Place It

| Classification | Destination |
|---|---|
| Doctrine | `MASTER_DOCTRINE.md` — as a sharpened existing article where possible |
| Standard | the matching file in `standards/` |
| Protocol | the matching file in `protocols/` |
| Repository rule | that repository's `AGENTS.md` or `GOVERNANCE.md` |
| Implementation detail | that repository's `README.md` or `docs/` |
| Ecosystem membership or role | `schemas/ecosystem.yaml` |

Write it **once**, in one place. Everywhere else links to it.

---

## Protecting the Doctrine

The Master Doctrine must stay concise. It is the one document every agent reads on every
task; every line added to it is paid for on every future task in the ecosystem.

**Reject from the doctrine**, absent an exceptional architectural reason:

framework-specific instructions · commands · code conventions · file paths ·
branch names · detailed workflows · tool-specific procedures · repository-specific
rules · temporary rules · task-specific instructions · anything with a version number

If detail must be referenced from an article, reference the standard that holds it. Do
not inline it.

**Signals the doctrine is decaying:** an article grew a bulleted procedure; an article
names a tool, a file, or a branch; two articles have started saying the same thing; an
article's detail could be checked by a script. Each is a prompt to move content down a
tier — not to reword it in place.

---

## Retiring Rules

Rules are removed, not left to rot. A rule is retired when it no longer applies, when it
has been absorbed into another rule, or when it has descended into infrastructure and the
written form is now redundant.

Removal is a governance change like any other: state what was removed and why, and check
that nothing still links to it.

Dead governance is worse than missing governance, because it is still obeyed.

---

## Changing Governance Safely

The doctrine is global and current (Article 2). A change here takes effect for every
repository immediately in principle — and in **no** repository automatically in practice.

Therefore, when governance changes:

1. **Do not** modify repositories as part of the governance change.
2. Repositories discover the change at their next bootstrap (`AGENT_BOOTSTRAP.md`).
3. Gaps are closed as scoped work under
   [protocols/REPOSITORY_ALIGNMENT.md](protocols/REPOSITORY_ALIGNMENT.md).

A change that would require every repository to change at once is a signal that the
change is too large. Prefer changes the ecosystem can absorb gradually.

### Before committing a governance change

- [ ] The requirement is not already covered elsewhere.
- [ ] It is filed at the correct tier, by the Step 2 test.
- [ ] It is stated exactly once; other documents link rather than restate.
- [ ] It does not contradict a higher tier.
- [ ] The doctrine did not grow procedural content.
- [ ] Every document it affects still has one clear responsibility.
- [ ] Links resolve, and nothing points at something that was removed.
- [ ] If it is not yet enforced, it does not claim to be
      ([GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md)).

---

## For Agents

When asked to "add a rule," do not begin by writing one.

Classify first. Report the classification and the destination, then write. If the correct
answer is "this already exists" or "this belongs in your repository, not in governance,"
say so — that is a successful outcome, not a failure to complete the task.
