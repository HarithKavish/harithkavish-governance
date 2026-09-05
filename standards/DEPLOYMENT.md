# Standard — Deployment

Implements Article 5 (Repository Integrity) and Article 6 (Protected Production).

Governance defines how a change reaches `main`
([BRANCHING.md](BRANCHING.md)) and what a correct change looks like
([DEVELOPMENT.md](DEVELOPMENT.md)). This standard covers what happens **after**: how the
contents of a production branch become a live surface, and how what was shipped stays
identifiable afterwards.

**Enforcement rung: 2 (guidance).** Nothing validates a deployment path today. Requiring
a status check before a deployment, and validating the Pages build type, are rung-4
mechanisms if they are built.

---

## Deployment Happens In A Workflow

**Every surface deploys through a workflow committed in its repository.**

A platform setting is not a deployment mechanism. It is invisible in the repository,
absent from history, unreviewable in a pull request, and changeable by anyone with
settings access without leaving a trace. A repository whose deployment exists only as a
setting cannot answer the question Article 5 requires it to answer — how does this reach
production — from its own surface.

Concretely, on this ecosystem's platform:

- A repository serving GitHub Pages has a build type of **workflow**, not a branch
  source. The workflow builds the surface and publishes it through the Pages deployment
  action.
- Nothing reaches a live surface by a path that is not declared in the repository.

### The Test

> Can a reader determine how this repository reaches production by reading the
> repository?

If the answer requires opening the platform settings, the deployment is outside the
workflow and this standard is not met.

**Building in a workflow is not sufficient on its own.** A workflow that builds output
and pushes it to a branch, where a *setting* then publishes that branch, still fails the
test: the step that actually reaches users is the setting. Publication is the part that
must be declared, not merely the build.

## Deployment Is Visible

A repository states where its current surface came from. A reader — human or agent —
should be able to establish, without guessing, which commit is live and when it was
deployed.

Workflow-based deployment gives this for free: the deployment history is the workflow run
history, and it is attached to a commit. This is a second reason a setting is inadequate.
A branch-served surface has no deployment record at all, only a branch that changed at
some point.

## Releases And Artifacts

**A repository that produces a versioned consumable tags its releases.**

A versioned consumable is something another person or system installs, downloads, or
depends on at a specific version — an installable package, a mobile build, an editor
extension, a distributed library, a published bundle. If a consumer could reasonably ask
which version they have, the repository tags releases and attaches the built artifact to
the release.

**A content surface does not.** A site whose current state is the only state anyone wants
gains nothing from a release per change, and a release stream nobody consumes is noise
that hides the releases that matter.

**Test:** does anything outside this repository depend on a *specific version* of what it
produces? Then it tags. If the answer is only ever give me the current one, it does not.

Where a workflow already builds an artifact, that artifact is attached to a release rather
than left only in the run's temporary storage — build outputs expire, releases do not.

## Known Gap — Migration

At the time this standard was written, the ecosystem did not meet it. Of 27 covered
repositories: **6** deployed by workflow, **13** served GitHub Pages from a branch
setting, and **8** had no live surface. Two were mid-pattern — `store` built in
a workflow and published a branch by setting, and `sites` carried a Pages
workflow while its Pages build type was still the branch source, which is either a dead
workflow or an unfinished migration.

**A second, distinct case: hosted-service integrations.** Three repositories
(`account`, `forge`, `my_chatgpt`) deploy through a hosting
provider connected directly to the repository, which builds and publishes on push without
any workflow in the repository. This fails the same test for the same reason, and fails it
harder: the build configuration, the environment, and the credentials all live in a
third-party dashboard rather than in the repository, so the deployment cannot be reviewed,
reverted, or reproduced from the repository at all. Bringing these inside the workflow
means the provider's own git integration is disabled and the deployment is driven from a
workflow instead.

`account` is additionally deployed twice — as a project Pages site and through a
hosting provider — with neither path declared. Which of the two is intended to be the
live surface is itself undetermined, and is resolved before either is migrated.

**Declared exception (Article 10).** Migrating the 13 branch-served repositories at
once deviates from [MAINTENANCE.md](../MAINTENANCE.md), which prefers changes the
ecosystem absorbs gradually over changes that touch every repository at once. The owner
chose the immediate migration explicitly, on 2026-09-05, having been shown the count and
the risk. The deviation is bounded to the migration itself: those repositories change how
they publish and nothing else. It ends when they have migrated, at which point this
section records the completed state rather than a pending one.

The three hosted-service repositories are **not** covered by that decision. Moving a
deployment off a provider's git integration changes build environment and credentials, not
merely publication, so it is scoped and decided separately rather than folded into the
Pages migration.

Migration is **separate scoped work** and is not performed as part of adopting this
standard ([MAINTENANCE.md](../MAINTENANCE.md): a governance change modifies no repository).
These are live public surfaces; each migration is verified to still serve before the next
begins.

---

## Compliance Check

- [ ] The surface deploys through a workflow committed in the repository
- [ ] Pages build type is workflow, not a branch source
- [ ] No path reaches production that is not declared in the repository
- [ ] Which commit is live, and when it deployed, is determinable without opening settings
- [ ] A repository producing a versioned consumable tags releases and attaches artifacts
- [ ] A content surface is not carrying release ceremony it has no consumer for
