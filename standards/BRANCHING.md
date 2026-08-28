# Standard — Branching

Implements Articles 6 (Protected Production) and 7 (Isolated Development).

**Enforcement rung: 2 (guidance).** Branch protection and required pull requests are the
intended rung 3–4 mechanisms and are not yet configured. Until they are, this standard
holds because it is followed, not because it is prevented from being broken.

---

## The Branches

| Branch | Role | Work committed directly? |
|---|---|---|
| `main` | Production / stable. What is deployed or released. | **No** |
| `development` | Integration. Where completed work accumulates before release. | No — except trivial integration fixes |
| `<type>/<description>` | Isolated work. Where implementation actually happens. | Yes |

`main` exists in every repository. `development` exists in every repository that receives
ongoing work; a frozen or archived repository may have only `main`.

## The Flow

```
feature/fix branch  →  development  →  main
```

Work branches start from `development` and merge back into `development`. `development`
merges into `main` at release. Nothing skips a step in the normal flow.

## Work Branch Names

```
<type>/<short-kebab-case-description>
```

| Type | For |
|---|---|
| `feature/` | New capability |
| `fix/` | Correcting broken behaviour |
| `refactor/` | Restructuring without behaviour change |
| `docs/` | Documentation only |
| `chore/` | Dependencies, config, tooling, metadata |
| `design/` | Visual or design-system work |
| `hotfix/` | Urgent production fix — see below |

Describe the change, not the ticket or the author: `fix/theme-toggle-dark-flash`, not
`fix/issue-42` or `harith/patch-1`. Keep it short; the branch is not the changelog.

## Merging

Work reaches `development` through a pull request. The pull request is the review point
even when the author is also the reviewer — it is what makes the change inspectable later
and what CI will attach to when it exists.

Delete work branches after merge. Long-lived branches diverge and stop being isolation.

## Hotfix — the Exception Path

For urgent production defects only: something is broken in production and waiting for the
normal flow causes real harm. Convenience is not urgency.

```
main  →  hotfix/<description>  →  main  →  merge back into development
```

A hotfix branches from `main`, merges to `main`, and is **immediately merged back into
`development`**. Skipping that last step means the fix is silently reverted at the next
release — this is the failure mode the exception path most often causes.

A hotfix is narrow: it fixes the defect and nothing else. Refactors, cleanups, and
improvements noticed along the way go through the normal flow.

## For Agents

- Before implementing, check the current branch. If it is `main` and the task is
  implementation work, stop and create a work branch first.
- Branch from `development` when it exists; from `main` only when it does not, or for a
  hotfix.
- Never commit directly to `main`. If asked to, treat it as a tier-6 instruction
  conflicting with Article 6 and surface it
  ([GOVERNANCE_HIERARCHY.md](../GOVERNANCE_HIERARCHY.md)).
- Never force-push a shared branch, and never rewrite history on `main` or `development`.

## Known Gap

Most repositories in the ecosystem currently have only `main`. Creating `development` in
a repository is an alignment action, carried out under
[protocols/REPOSITORY_ALIGNMENT.md](../protocols/REPOSITORY_ALIGNMENT.md) — not something
an agent does spontaneously on the way to another task (Article 9).
