# Standard — Design System

Implements Article 4 (Shared Design Language).

This repository **governs** the design system. It does not contain it. Token values,
component source, and usage examples live in the design system repository and are read
from there — copying them here would create a second source of truth (Article 3).

**Enforcement rung: 2 (guidance).** Automated design-token and component checks are a
future rung-4 mechanism.

---

## The Authoritative Source

| | |
|---|---|
| **Repository** | [HarithKavish/design-system](https://github.com/HarithKavish/design-system) |
| **Contains** | Design tokens, component primitives, UI kits, brand guidelines |
| **Deleted** | `harith-design-system` — the former v1.0.0 repository. Retired to a pointer, then removed on 2026-09-06 once confirmed nothing consumed it. |

Read the design system repository directly for current tokens and components. Any token
value quoted outside that repository is a copy, and copies go stale.

## The Layers

Design foundations are layered by how shared they are:

| Layer | Examples | Authority |
|---|---|---|
| **Foundations** | Colour, typography, spacing, radius, elevation, motion | Shared system **only** |
| **Primitives** | Buttons, cards, panels, inputs, headers, footers | Shared system |
| **Composed patterns** | Page shells, article layouts, catalogue grids | Shared where reused |
| **Product surfaces** | A screen unique to one product | Repository-local |

The rule tightens as you go up. Foundations are never redefined locally.

---

## When a Repository Must Use the Shared System

Use the shared system when the thing being built:

- Is a **public surface** of the ecosystem — anything a visitor sees.
- Uses any **foundation** — a colour, a font size, a spacing value, a radius, a shadow.
- Reproduces a **primitive** that already exists in the shared system.
- Is **shell chrome** — header, navigation, footer, theme toggle. These are what make
  separate sites read as one ecosystem, and they are the first thing to drift.

Consume foundations through the system's tokens rather than literal values. A hard-coded
hex, font stack, or spacing number in a product repository is a defect even when it
happens to match — it will not follow the next change.

## Before Adding Or Changing A Design Element

The question is not only whether the system already has this. It is whether anyone else
needs it.

Before a surface adds a new design element, or changes one in a way others might want:

1. **Check the shared system.** If it is there, use it.
2. **Check the other surfaces.** Would another website or application in the ecosystem
   plausibly need the same thing? Two surfaces solving one problem separately is the
   failure this ecosystem exists to prevent, and it is far cheaper to notice before the
   second implementation than after.
3. **If it is shareable, raise it in the design system** as a pull request there, and
   consume the result. Not a local build with a note to promote it later — the note is
   rarely acted on, and the local copy then becomes the thing that has to be removed.
4. **If it is genuinely local, build it locally** from shared foundations, and say why.

Step 2 is the one most often skipped, because it costs time before any code is written.
It is also the only step that *prevents* duplication rather than detecting it afterwards.

## When Repository-Specific Components Are Acceptable

Local components are legitimate — not a workaround — when the need is genuinely local:

- The component is **specific to one product's domain** and has no meaning elsewhere.
- It is a **composition of shared primitives**, not a replacement for them.
- It is a **prototype** not yet proven reusable.
- It is **experimental** and deliberately not stable enough to share.

A local component still uses shared foundations. Locality justifies a new component; it
never justifies a new colour, type scale, or spacing scale.

## Selective Opt-Out

A surface may disable a **specific part** of the shared system where that part genuinely
contradicts its own design — a console needing a denser table than the shared one, an
application the shared shell does not fit.

This is narrow, and it is not the same as redefining a foundation:

- **Disable a piece, not the system.** Opting out of the shared header is a decision
  about the header. Opting out of the token layer is a second visual identity, and needs
  a declared exception under **Never** below.
- **Name what is disabled and why**, in that repository's `GOVERNANCE.md` under
  declared exceptions (Article 10). An opt-out nobody wrote down is indistinguishable
  from drift.
- **State what would end it.** Most opt-outs exist because the system lacks a variant.
  That is a gap in the *system*, and recording it is what eventually closes it.
- **Foundations survive the opt-out.** Disabling the shared table does not license a
  local colour or type scale for the replacement.

An opt-out is a declared position, not a silence. A surface that simply stops using the
shared system without saying so has drifted, whatever the reason was.

### A complete redesign is a different decision

A surface deliberately outside the shared visual identity — a full redesign rather than a
set of exceptions — is legitimate. It is a declared exception under Article 10, recorded
in that repository's `GOVERNANCE.md`, stating what it departs from, why, and
what would end it.

What is not legitimate is arriving there by accumulation: disabling one piece, then
another, until nothing shared is left and nobody ever decided it. A surface heading that
way decides it deliberately and writes it down.

## When to Promote Back into the Shared System

Promote when **any** of these becomes true:

- A second repository needs the same component.
- A second repository has already built something equivalent. (Two implementations of one
  idea is the signal — act on it rather than adding a third.)
- The component expresses ecosystem identity rather than product function.
- A local prototype has stabilized and proven reusable.

Promotion is a change to the design system repository, made there, under its own rules.
The consuming repository then **removes its local copy** and consumes the shared one. A
promotion that leaves the local copy in place has created a duplicate rather than removed
one.

Promotion is out of scope for an agent that was asked to do something else. Report the
candidate; do not promote it mid-task (Article 9).

## Never

- **Redefine a foundation locally.** No repository-local colour palette, type scale,
  spacing scale, or shadow set. If a foundation is missing, it is missing from the
  *system* — raise it there.
- **Fork the design system.** Consume it. A fork is a second source of truth.
- **Quote token values into other repositories' documentation.** Link instead.
- **Restyle a shared primitive from outside.** Overriding a shared component's internals
  in a consuming repository produces drift that is invisible until it breaks. Either the
  component needs a variant — in the system — or the usage is wrong.
- **Introduce a second visual identity** for a subset of the ecosystem without a declared
  exception (Article 10).

## Framework Independence

This standard is deliberately framework-agnostic. The ecosystem currently spans static
HTML, React, and Next.js repositories, and the design system publishes both component
source and a plain CSS/JS distribution for surfaces that have no build step.

The requirement is that a surface derives from the shared foundations. **How** it consumes
them — imported components, the published distribution, or a build-time pipeline — is an
implementation detail of that repository, and belongs in that repository's documentation.

## For Agents

Before writing any UI code:

1. Check whether the design system already provides the component. If it does, use it.
2. Check whether a foundation covers the value you are about to hard-code. It almost
   certainly does.
3. If you must build locally, build it from shared foundations and note why it is local.
4. If you notice a promotion candidate or a drift, **report it**. Do not migrate the
   repository as a side effect of the task you were given.
