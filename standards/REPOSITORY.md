# Standard — Repository

Implements Article 5 (Repository Integrity).

A repository must be understandable from its surface: what it is, what it is for, where
it sits in the ecosystem, and how to begin work in it — all before opening a source file.

**Enforcement rung: 2 (guidance), except where noted.** Metadata validation is a
future rung-4 mechanism.

---

## Required in Every Participating Repository

| Item | Where | Required |
|---|---|---|
| **About description** | Repository settings (GitHub "About") | Yes |
| **Social preview image** | Repository settings, source committed in-repo | Yes |
| **`README.md`** | Root | Yes |
| **`AGENTS.md`** | Root | Yes |
| **`GOVERNANCE.md`** | Root | Yes |
| **Topics** | Repository settings | Recommended |
| **Homepage URL** | Repository settings | Yes, if the repository has a live surface |

`AGENTS.md` and `GOVERNANCE.md` are the governance discovery entry points. Their content
and the procedure for adding them are defined in
[protocols/REPOSITORY_ONBOARDING.md](../protocols/REPOSITORY_ONBOARDING.md).

---

## About Description

Every repository has a description. An empty About field is non-compliant.

- **One sentence.** What this repository *is*, in plain language.
- **Lead with the noun.** "Shared design system for…", not "This repo contains…".
- **Name the surface** it serves when it has one — the product, or the domain.
- **Present tense, no marketing.** It is a label, not a pitch.
- **No trailing period** required; no emoji; no version numbers.

A reader scanning the account's repository list should be able to tell what each one is
without opening it. That is the whole test.

> `Shared design system for the HarithKavish ecosystem — tokens, primitives, and UI kits`

Set it on creation, not later. A repository without a description is unfinished.

## Social Preview Image

Every repository has a social preview image. This is what renders when the repository is
shared anywhere off GitHub, and the ecosystem should look like an ecosystem when that
happens.

**Content**

- Use the **website's own logo** where the repository has one. This is the primary
  requirement: the preview should identify the product at a glance.
- Where the repository has no logo of its own — a library, a tool, an internal
  service — use the ecosystem mark.
- Keep it consistent with the shared design system: its background, accent, and type
  come from the shared foundations
  ([DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)), not from an independent palette.
- Include the repository or product name as text. Logos alone are unreadable at the
  sizes these previews render.
- No screenshots of the UI. They date immediately and read as noise when scaled down.

**Format**

- `1280×640` px. This is the display size; smaller images are upscaled and look it.
- PNG. Under 1 MB.
- Legible on both light and dark backgrounds — previews are rendered on surfaces you do
  not control.

**Source file**

Commit the image so it is versioned and reproducible:

```
.github/social-preview.png
```

The committed file is the source of truth for the image. The uploaded preview is a copy
of it — if the image changes, both change.

> **Upload is manual.** GitHub exposes no API for the social preview; it is set in
> Settings → General → Social preview. An agent can create and commit the image file and
> must then state plainly that the upload remains to be done by a human. Do not report
> the requirement as satisfied because the file was committed.
>
> Existing repositories carry preview sources at inconsistent root-level paths (for
> example `HK Nexus.png`). Normalizing them to `.github/social-preview.png` is an
> alignment action, not a side effect of unrelated work.

## README

The README serves humans. It is tier 5 — implementation documentation — and it is not a
place to restate governance.

Every README states, near the top:

1. **What this is** — one paragraph.
2. **Where it lives** — the live URL, if it has one.
3. **How to run it** — the shortest path from clone to running.
4. **Ecosystem membership** — one line pointing at `AGENTS.md` / `GOVERNANCE.md`.

Do not copy doctrine, standards, or branch rules into the README. Link to `GOVERNANCE.md`
and let it point onward (Article 3).

## Naming

- Lowercase, hyphen-separated: `design-system`, not `Design_System`.
- Name the **thing**, not the technology: `store`, not `store-nextjs`.
- Where a repository serves a subdomain, the repository name matches the subdomain label:
  `blog` serves `blog.harithkavish.com`.

Existing repositories that predate this rule are not renamed for its own sake — renaming
breaks URLs, clones, and deploy hooks. It applies to new repositories.

## Structure

- Governance entry points (`AGENTS.md`, `GOVERNANCE.md`, `README.md`) at the root.
- No secrets, credentials, or `.env` files committed
  ([SECURITY.md](SECURITY.md)).
- No vendored copy of the design system or of governance (Article 3).
- Root stays legible. Prefer `.github/`, `docs/`, `assets/` over accumulating loose
  files at the top level.

## Ecosystem Registry

[schemas/ecosystem.yaml](../schemas/ecosystem.yaml) records each repository's role, its
surface, its adoption state, and the date its membership was last verified. A repository
that is not listed is not discoverable as a member.

Adding the entry is part of onboarding, not an afterthought.

**The registry is complete against the account.** Every repository under the ecosystem's
account appears in it exactly once — either as a participant, or explicitly as one
governance does not apply to. Absent is not the same as excluded: an absent repository is
one whose membership nobody has decided yet, and it is resolved under
[protocols/REPOSITORY_ALIGNMENT.md](../protocols/REPOSITORY_ALIGNMENT.md) rather than
assumed either way.

**Every decision carries a date.** Each entry records when its membership was last
verified, so a decision made once and never revisited is visibly distinct from one
confirmed recently. A repository's purpose can change; the date is what makes a stale
decision detectable instead of invisible.

**Completeness is verified, not assumed.** The registry is reconciled against the
account's actual repository list, and the date of that reconciliation is recorded.
Repositories created since the last one are the expected finding — that is what the
check is for.

> **Enforcement rung: 2 (guidance).** Nothing currently prevents a repository from being
> created without a registry entry, and no automation performs the reconciliation. Both
> are rung-4 mechanisms if they are built. Until then this holds because it is followed.

## Compliance Check

- [ ] About description set, one sentence, describes the repository
- [ ] Social preview image uploaded, and its source committed at `.github/social-preview.png`
- [ ] `README.md` present and current
- [ ] `AGENTS.md` and `GOVERNANCE.md` present
- [ ] Homepage URL set, if there is a live surface
- [ ] Listed in `schemas/ecosystem.yaml`
- [ ] No secrets committed
- [ ] No vendored governance or design system
