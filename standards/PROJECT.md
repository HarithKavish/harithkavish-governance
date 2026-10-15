# Standard — Project Manifest

Implements Article 5 (Repository Integrity).

Every repository describes itself — what it is for, what it covers, what it runs on, what
it must never do — in one structured place that people, agents and review bots all read.
The README tells a human how to start; the manifest tells everything else what the
project *is*.

**Enforcement rung: 4 once the policy engine is live** (`tools/policy/`): a missing,
invalid or contradicted manifest fails the `policy` check, which every protected branch
requires ([BRANCHING.md](BRANCHING.md)). Until then, rung 2.

---

## Where It Lives

```
.project/
  project.yaml        the structured manifest — schemas/project.schema.json
  overview.md         purpose, users, scope and non-goals, in prose
  architecture.md     components, data flow, the paths each component owns
  decisions.md        why it is built this way: one entry per significant decision
  risks.md            what could go wrong, what is sensitive, what must be checked
```

`project.yaml` is required. The four documents are required once the project has
anything to say in them; an empty one says so in a line rather than being absent. Detail
belongs here, not in the README — the README links to `.project/overview.md`.

## What the Manifest Declares

| Section | Says | Read by |
|---|---|---|
| `project` | name, one-line purpose, status, owner | everything |
| `scope` | what it covers and, as importantly, what it does not | agents planning a feature; the reviewer judging whether a change belongs |
| `surface` | live URLs per stage (`development`, `runway`, `main`) | the `live-surface` verifier |
| `components` | each part, its responsibility and the paths it owns | agents (where to change what); the reviewer (which component a diff touches) |
| `infra` | every platform it runs on or depends on — Cloudflare, Vercel, GitHub Pages, MongoDB Atlas, Render, Android, the Oracle VM — with the resource names | the verifiers: what applies, and what to check it against |
| `data` | what it stores, classification, personal data, retention | the reviewer and the security check |
| `secrets` | every secret **by name** and where it is held — never a value | the security check: a secret used but not declared is a finding |
| `depends_on` | other repositories and external services it needs | agents; impact of a change |
| `verify` | how to build and test it; what proves a deployment works | the `ci` check and the `release` gate |
| `risks` | the specific things a reviewer must look at in this project | the reviewer's prompt |

The schema is the authority on field names and types; this table is the reason each
section exists.

## Declared Matches Detected

The manifest is checked against the repository, not trusted:

- infrastructure **detected but not declared** — a `wrangler.toml` with no
  `infra.cloudflare` — fails `policy`: an undeclared platform has no verifier and no
  review context, which is exactly how an unverified deploy reaches production;
- infrastructure **declared but not detected** fails too: the manifest is stale, and a
  stale manifest misleads every reader at once.

Detection rules are in [schemas/policy.yaml](../schemas/policy.yaml) under `verifiers`.

## How It Is Used

- **Agents** read `.project/` before planning work in the repository, after
  `AGENTS.md`. A feature is placed in the component that owns its paths; a feature
  outside `scope` is raised, not quietly built.
- **The code reviewer** receives the manifest and the components the diff touches, and
  checks the change against `scope`, `risks`, `data` and `secrets`.
- **Verifiers** run for what `infra` and `surface` declare, against the resource names
  declared there.
- **The ecosystem registry** ([schemas/ecosystem.yaml](../schemas/ecosystem.yaml)) keeps
  membership; the manifest keeps everything else about the project. They do not repeat
  each other.

## Changing It

The manifest changes in the same pull request as the change that makes it untrue —
a new platform, a new secret, a new component. A pull request that adds infrastructure
without updating the manifest fails `policy`.

## Compliance Check

- [ ] `.project/project.yaml` present and valid against `schemas/project.schema.json`
- [ ] Declared infrastructure matches detected infrastructure
- [ ] Every secret the code reads is declared by name; no value anywhere in the repository
- [ ] `overview.md`, `architecture.md`, `decisions.md`, `risks.md` present
- [ ] README links to `.project/overview.md`
