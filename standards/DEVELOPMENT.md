# Standard — Development

What "correct" means for changes to code in the ecosystem, independent of language and
framework.

This standard states outcomes. Per-repository specifics — the package manager, the test
runner, the lint configuration, the build command — belong in that repository's
documentation, not here.

**Enforcement rung: 2 (guidance).** CI validation is a future rung-4 mechanism.

---

## Changes

**Scope discipline.** A change does one thing. Unrelated fixes, cleanups, and
reformatting go in separate changes — a diff mixing them cannot be reviewed, and cannot
be reverted without losing the part that was wanted.

**Match the surrounding code.** Naming, structure, comment density, and idiom follow the
file you are editing, not your preference. Consistency within a repository outranks any
external style opinion.

**Minimal diff.** Change what the task requires. Reformatting untouched lines, renaming
for taste, and re-ordering imports are not free — they hide the real change.

**Leave it working.** A repository is never committed in a knowingly broken state. If
work is incomplete, it stays on its branch.

## Commits

- **Imperative mood, present tense:** `add theme toggle`, not `added` or `adds`.
- **Subject describes the effect**, not the mechanics. `fix dark-mode flash on load`
  beats `update styles.css`.
- **One logical change per commit.**
- **No noise commits** on shared branches — `wip`, `fix`, `asdf`. Squash before merging.

Commit messages are the only durable record of *why*. The diff already shows what.

## Pull Requests

Every merge into `development` or `main` goes through a pull request
([BRANCHING.md](BRANCHING.md)), including when the author is the only reviewer.

A pull request states what changed, why, and anything a reviewer would otherwise have to
discover — the deviation you took, the thing you deliberately left out, the follow-up you
are not doing.

## Dependencies

**Adding a dependency is a decision, not a step.** Before adding one, check whether the
platform, the existing dependencies, or the shared design system already solves it.

- Prefer no dependency, then a small focused one, then a large one.
- A dependency for something implementable in a few lines is a liability, not a shortcut.
- Lockfiles are committed.
- An agent does not add, upgrade, or remove a dependency that the task does not require.

## Testing

Tests are required where correctness is not obvious from reading the code, and where a
regression would be silent. This is a judgement, not a coverage number.

- A bug fix comes with the test that would have caught it, where the repository has a
  test setup.
- Do not weaken or delete a test to make a change pass. A failing test is information.
- Report test results honestly. If tests fail, say so, with the output. If you did not
  run them, say that instead of implying you did.

## Configuration and Environments

- Configuration comes from the environment; it is not hard-coded and not committed
  ([SECURITY.md](SECURITY.md)).
- An `.env.example` documents every variable the repository needs, with placeholder
  values. Real values never appear in it.
- Environment-specific behaviour is explicit, not inferred from hostnames or branch names.

## Accessibility and Correctness of Surfaces

Public surfaces are expected to be usable, not merely rendered:

- Semantic markup and keyboard operability for interactive elements.
- Visible focus states — the shared design system provides them; do not remove them.
- Meaningful alternative text on meaningful images.
- Light and dark themes both checked when the surface supports both.

These are outcomes of using the shared design system correctly
([DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)) more often than they are separate work.

## For Agents

- **Read before writing.** Match the repository's existing conventions rather than
  importing conventions from elsewhere.
- **Do not restructure opportunistically.** Refactoring is its own task with its own
  scope (Article 9).
- **Do not fabricate verification.** "Should work" is not "verified"; say which you mean.
- **Do not silently drop part of the task.** If something is blocked, finish the rest and
  state clearly what was left and why.
