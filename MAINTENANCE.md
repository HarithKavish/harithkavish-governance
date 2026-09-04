# Governance Maintenance

How governance itself is changed.

Read this **before** creating, modifying, moving, merging, or removing any rule in this
repository. Governance systems do not fail because rules are wrong. They fail because
rules accumulate in the wrong places until nobody can tell what is authoritative.

This document exists to prevent that.

**Scope.** This document governs **how** a governance change is made: searching for
existing coverage, applying it, verifying it, and letting it propagate.

**Where** content belongs is not decided here. That is the routing layer,
[GOVERNANCE_MAP.md](GOVERNANCE_MAP.md). The two are used together — classify with the
map, change with this document.

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

**Classify before writing. Do not choose a document because it is related to the topic.**

Run the classification sequence in [GOVERNANCE_MAP.md](GOVERNANCE_MAP.md). It decides
between the seven destinations — doctrine, standard, protocol, schema, maintenance,
repository-specific, and implementation — and it holds the test for each.

Two outcomes are frequently correct and frequently missed:

- The requirement belongs in **a repository**, not in central governance.
- The requirement is **layered**, and its parts belong in different documents. Decompose
  it rather than filing it whole.

State the classification and the destination before you write anything.

---

## Step 3 — Apply the Change

Write it into the destination the map identified. Write it **once**, in one place;
everywhere else links to it.

Apply the smallest change that satisfies the requirement. Prefer sharpening existing
wording over appending new wording — a document that grows only by addition eventually
says the same thing three ways.

If applying it reveals that the classification was wrong, stop and reclassify. Do not
force it into the destination you already started editing.

---

## Protecting the Doctrine

The Master Doctrine must stay concise. It is the one document every agent reads on every
task; every line added to it is paid for on every future task in the ecosystem.

What may and may not enter the doctrine is defined in
[GOVERNANCE_MAP.md](GOVERNANCE_MAP.md). This section is the ongoing watch on it.

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

### The Timestamp Is Updated In The Change, Not After It

[schemas/governance.yaml](schemas/governance.yaml) records when governance last changed.
Every governance change updates it, in the same commit as the change itself.

**Do not defer it because further changes are expected.** Pending work is the most common
reason a timestamp is left for later, and it is exactly why it goes stale: the
repositories reading it cannot see an intention to update it soon, only the value sitting
there now. Every repository uses that value to decide whether it has fallen behind
(Article 2), so a lagging timestamp does not merely fail to inform them — it tells them
they are current when they are not.

No category of governance change is exempt. A typo fix in a standard updates it too,
because a repository cannot know the edit was cosmetic without reading the diff, and
sparing it that reading is the entire purpose of the timestamp.

### Before committing a governance change

- [ ] The requirement is not already covered elsewhere.
- [ ] It is filed at the correct destination, by the classification sequence in
      [GOVERNANCE_MAP.md](GOVERNANCE_MAP.md).
- [ ] It is stated exactly once; other documents link rather than restate.
- [ ] It does not contradict a higher tier.
- [ ] The doctrine did not grow procedural content.
- [ ] Every document it affects still has one clear responsibility.
- [ ] If a new category was introduced, it satisfies every condition in
      [GOVERNANCE_MAP.md](GOVERNANCE_MAP.md) under "Introducing a New Category".
- [ ] [schemas/governance.yaml](schemas/governance.yaml) carries this change's
      timestamp, set in this change and not deferred.
- [ ] Links resolve, and nothing points at something that was removed.
- [ ] If it is not yet enforced, it does not claim to be
      ([GOVERNANCE_HIERARCHY.md](GOVERNANCE_HIERARCHY.md)).

---

## For Agents

When asked to "add a rule," do not begin by writing one.

Given a governance modification task, work in this order:

1. Read [AGENT_BOOTSTRAP.md](AGENT_BOOTSTRAP.md) — establish where you are.
2. Read this document — the change process.
3. Read [GOVERNANCE_MAP.md](GOVERNANCE_MAP.md) — the routing logic.
4. **Classify** the requested change.
5. **Check whether equivalent content already exists** (Step 1).
6. **Identify the destination** the classification points to.
7. **Apply the minimal change** there.
8. **Check for duplication and contradiction** against the checklist above.

Report the classification and the destination *before* writing. If the correct answer is
"this already exists" or "this belongs in your repository, not in governance," say so —
that is a successful outcome, not a failure to complete the task.
