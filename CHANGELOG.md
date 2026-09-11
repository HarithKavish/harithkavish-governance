# Governance Changelog

The record of what changed in this repository, when, and who changed it.

**Append only.** Entries are added at the top. An existing entry is not edited and not
removed, including one that turns out to be wrong — a correction is a new entry that says
what it corrects. Only the repository owner may alter or remove history here.

**Why this exists when git history already does.** Git records the change; this records
the *decision* — what it was for, and whether a human or an agent made it. Git author
fields also carry whatever identity the committing machine happened to be configured
with, which is not always the actor. This file states the actor explicitly, so an
attribution error is visible rather than silent.

**Every governance change appends here, in the same change**, alongside the
`schemas/governance.yaml` timestamp. See
[MAINTENANCE.md](MAINTENANCE.md).

**Enforcement rung: 2 (guidance).** Nothing currently prevents this file being edited or
an entry being removed. Append-only protection and owner-restricted history are rung 3-4
mechanisms — branch protection and CODEOWNERS — and are not configured yet. Until they
are, this holds because it is followed.

Format, newest first:

```
## YYYY-MM-DDTHH:MM:SSZ — <one-line summary>
- **Actor:** <name> (<human | agent>)
- **Initiated by:** <who asked, or "autonomous">
- **Change:** <what changed, and where>
- **Why:** <the decision, not the diff>
```

---

## 2026-09-11T18:15:32Z -- Register forge-gateway in the ecosystem registry
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** schemas/ecosystem.yaml gains an entry for the new `forge-gateway`
  repository (role: service, adoption: integrated, no surface yet — not deployed).
  Registered during its onboarding per protocols/REPOSITORY_ONBOARDING.md.
- **Why:** forge-gateway was just created and onboarded (GOVERNANCE.md/AGENTS.md/
  README.md added, main/development/feature/claude branches created) as the presence
  backend for forge's Worldview page — registering it completes onboarding step 8 and
  keeps the registry's account-wide completeness property intact. claude-review.yml was
  not added during onboarding (writing it was refused by a local permission classifier),
  so this entry records that as outstanding rather than leaving the repository silently
  non-compliant with standards/DEVELOPMENT.md's automated-review requirement.

## 2026-09-10T05:21:37Z -- Register diary in the ecosystem registry
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** schemas/ecosystem.yaml gains an entry for the new `diary` repository
  (role: website, adoption: integrated, surface diary.harithkavish.com), registered
  during its onboarding per protocols/REPOSITORY_ONBOARDING.md.
- **Why:** diary was just created and onboarded (GOVERNANCE.md/AGENTS.md added,
  development/runway/feature/claude branches created, workflow-based Pages deploy,
  custom domain set) — registering it completes onboarding step 8 and keeps the
  registry's account-wide completeness property intact.

## 2026-09-10T02:46:56Z -- Cross-repo findings raise an issue; owner-gated issue-to-PR pipeline
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** standards/AGENT_METHOD.md gains "Findings About A Different Repository"
  (raise a structured issue there, including when the repository is governance itself,
  when the current task is not already governance work) and a scope-discipline addition
  to Section 5 (delegated judgment is not license to bundle unrelated changes). new
  .github/workflows/claude-issue-triage.yml implements an owner-gated pipeline: an issue
  opened by the repository owner is implemented on feature/claude and opened as a pull
  request, reviewed and possibly merged by the existing, separate claude-review.yml run
  -- two independent sessions, no shared context. standards/DEVELOPMENT.md documents both
  the pipeline and an updated, corrected Known Gap note.
- **Why:** requested directly, following a 2026-09-09 adversarial stress test of this
  governance system using real subagents against an isolated test repository. Findings
  from that test: prompt injection via repository content was resisted (2/2 tests), but a
  vague, delegated-judgment task produced one bundled pull request touching ten files
  across unrelated concerns without pausing to ask -- a real violation of this document's
  own "a change does one thing" rule, now addressed directly. Separately and more
  seriously: a direct empirical test found that branch protection does not stop the
  credentials this agent operates under -- GitHub logged "Bypassed rule violations" and
  allowed a direct push to a protected branch anyway. That finding is recorded honestly in
  DEVELOPMENT.md's Known Gap rather than left implied by a protection setting that reads
  as sufficient but is not. The issue-triage pipeline is gated to the owner's own issues
  specifically because of what the stress test proved: an ungated version would recreate,
  for issues, the exact injection surface just verified against for pull requests.


## 2026-09-09T17:15:25Z -- Correct a stale path in the previous entry
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** CHANGELOG.md, one entry corrected: `~/bin/safe-branch-move.sh` ->
  `tools/safe-branch-move.sh`.
- **Why:** the automated review on PR #37 flagged the stale path as a non-blocking note
  while reviewing the real fix. The script's canonical location is the one committed into
  this repository; the personal-environment copy at `~/bin` is a local convenience synced
  from it, not the source. Recorded here rather than silently edited, per this file's own
  append-only rule -- the earlier entry is not altered, this one corrects it.


## 2026-09-09T16:59:59Z -- Lessons require root cause, not symptom; recurrence is a hard stop
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** standards/AGENT_METHOD.md Section 3 gains a reflexive application to the
  agent's own git operations. standards/AGENT_ENVIRONMENT.md's learning section requires
  a lesson's "why" to separate symptom from root cause, with a stated test for telling them
  apart, and strengthens recurrence into: a second occurrence of the same root cause is a
  hard stop requiring a structural fix in the same session, not a third memory entry.
- **Why:** the user asked directly whether this agent was actually consulting recorded
  lessons to avoid repeating mistakes, or whether governance was failing to enforce that.
  The honest answer, checked against evidence rather than asserted: no. A lesson written
  after the first occurrence of a branch-reset failure (2026-09-07) was too narrow -- it
  captured the specific symptom, not the general precondition -- and the same root cause
  produced a second incident the very next day (PR #29), recovered only by chance via git
  reflog. The agent had said in conversation it would correct the memory afterward, and
  had not, until asked directly two days later. Fixed at two levels: a script
  (~/bin/safe-branch-move.sh) that structurally refuses the unsafe operation rather than
  relying on memory at all, and this governance change so the general failure mode --
  recording a symptom and calling it a cause, and stating an intention to fix a memory
  without following through -- is named and required to be caught for every agent, not
  just this one.


## 2026-09-08T19:19:45Z -- Allow the automated review to run against agent-pushed commits
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** claude-review.yml gains allowed_bots; standards/DEVELOPMENT.md and the
  GOVERNANCE_HIERARCHY.md enforcement register document it.
- **Why:** the action refuses to run when the triggering push came from a bot account,
  and Jarvis pushes as jarvis-harithkavish[bot]. Every agent-pushed commit therefore
  failed this check silently -- no comment, no visible error -- discovered when PR #29
  was found to have merged on the strength of a review of an EARLIER commit, not the one
  that actually shipped. The review that should have gated the merge had failed four
  minutes before the merge happened, and nobody -- including this agent -- checked before
  merging.


## 2026-09-08T18:20:37Z — Add the Agent Method standard
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** new standards/AGENT_METHOD.md; routing rows in AGENT_BOOTSTRAP.md, README.md
  and CONCERNS.md.
- **Why:** nothing governed HOW an agent works a problem -- AGENT_ENVIRONMENT.md covers
  the agent's own configuration, AGENT_BOOTSTRAP.md covers discovering what governance
  applies, DEVELOPMENT.md covers what a good change looks like once it is being written.
  The gap was the method in between: acquiring the means to inspect a system before
  theorising about it, understanding proportionately to blast radius, mapping what depends
  on what before changing anything shared, using the known diagnostic technique for the
  class of problem rather than improvising, building minimal AND complete rather than one
  at the expense of the other, and verifying by observation rather than by absence of
  error. This is an actor rule and reaches every repository under the account regardless
  of ecosystem membership.


## 2026-09-07T22:27:24Z — Findings that generalise are proposed, not discarded
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** MAINTENANCE.md gains Where Changes Come From; AGENT_BOOTSTRAP.md and
  CONCERNS.md point at it.
- **Why:** governance said how to make a change and, via Article 9, that finding a gap is
  not licence to fix it. It said nothing about what happens to the finding afterwards, so
  a generalisable observation made mid-task had nowhere to go and was simply lost. The
  requirement that a proposal name its enforcement rung is deliberate: this ecosystem
  measured its own enforcement at almost zero, so a proposal without an enforcement path
  is a candidate for the pile rather than for changing behaviour.

## 2026-09-07T22:15:05Z — Branch protection applied: the first rule to reach rung 4
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** GOVERNANCE_HIERARCHY.md enforcement register. The repository settings
  themselves are infrastructure, not a governance change.
- **Why:** BRANCHING.md had been written, published and read, and was not being followed --
  20 of 26 repositories had development and runway diverged from main, one by sixty
  commits, because work went straight to main. Protection makes that structurally
  impossible rather than discouraged. Approvals are set to zero so the automated review can
  still merge what it reviewed; enforce_admins is off so the hotfix path still works.


## 2026-09-07T20:47:07Z — Findings are recorded at the moment, and categorised
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** standards/AGENT_ENVIRONMENT.md, What The Agent Has Learned.
- **Why:** the rule said what to record but not when, and left the record uncategorised.
  Deferring loses the detail first and then the record itself -- the sessions that go worst
  have the most to teach and are least likely to reach a write-up step. Categorising by
  scope and technology is what makes the record searchable at the moment of acting, which
  is the only moment it matters. Recurrence is now itself a finding: a pain point recorded
  three times is one worth removing rather than re-recording.


## 2026-09-06T01:44:46Z — Record the surfaces for converse and ai-lab
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** schemas/ecosystem.yaml, surface fields for two entries.
- **Why:** both serve live pages but their entries carried no surface, so the registry
  understated what is deployed. Noticed during the 2026-09-05 audit and left unfixed until
  now. Verified live before recording: both return HTTP 200.


## 2026-09-06T01:35:33Z — Automated review may merge reviewed code, into development only
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** the review prompt in claude-review.yml, and the Automated Review section of
  standards/DEVELOPMENT.md.
- **Why:** the owner asked that a passing review auto-merge. The previous gate only
  merged documentation and formatting, so a correct code change still sat waiting. Now a
  clean review merges into development. Two carve-outs were kept deliberately and are not
  what was asked for: runway and main are never auto-merged, because BRANCHING.md calls
  promotion to main a deliberate release act and nothing else gates it -- with no branch
  protection anywhere, an unrestricted rule would let a change reach production with no
  human ever seeing it. Credentials are excluded because reverting does not undo a leak.


## 2026-09-06T01:23:17Z — Automated review re-runs on new commits
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** claude-review.yml gains synchronize and ready_for_review triggers plus a
  cancelling concurrency group; standards/DEVELOPMENT.md updated to match.
- **Why:** the workflow only fired when a pull request was opened or reopened, so a
  re-review needed a manual close/reopen. Concurrency cancellation keeps the cost bounded:
  a burst of pushes reviews the settled state once rather than once per push.


## 2026-09-06T01:18:11Z — Fix a Markdown lazy-continuation defect found by automated review
- **Actor:** Claude (agent)
- **Initiated by:** automated review on PR #23
- **Change:** standards/DEVELOPMENT.md, blank line before the provenance paragraph.
- **Why:** the paragraph followed a list item with no blank line, so CommonMark treats it
  as a lazy continuation and renders it glued onto the preceding bullet. Found by the
  automated review on its first working run after being restored -- the first defect that
  mechanism has caught in this ecosystem.


## 2026-09-05T23:36:04Z — Record why a signature alone does not verify an agent commit
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** standards/SECURITY.md, the signing rule.
- **Why:** the signing key was registered correctly as a signing key with a matching
  fingerprint, and commits still reported unknown_key. Cause: the platform resolves a
  commit to an account by email, and the agent email belongs to no account, so it never
  looks at the owner keys at all. The misleading part is that it reports a key problem.
  Recorded with the resolution -- author is the agent, committer is the account whose
  credentials applied it -- so the next agent does not spend the same round-trips
  rediscovering it.


## 2026-09-05T23:13:17Z — Automated review: first cause fixed, second cause isolated
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** GOVERNANCE_HIERARCHY.md enforcement register updated with the measured
  result. Ten repositories received the missing workflow permission (a repository change,
  landed through each repository's own branching flow, not as part of a governance change).
- **Why:** the register must reflect reality or it is worse than absent. The OIDC failure
  is genuinely gone, verified by the error changing rather than assumed. A second cause
  remains and the automated review still does not work anywhere, which the register now
  says plainly rather than implying the problem was solved.


## 2026-09-05T23:04:22Z — Signed commits, agent learning, and helping the actor you work for
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** standards/SECURITY.md requires commits to be signed;
  standards/AGENT_ENVIRONMENT.md gains What The Agent Has Learned and Helping The Actor
  You Work For.
- **Why:** the owner observed that agent commits carry no verified badge. Measured: the
  machine has no GPG or SSH keys and no signing config, so every agent commit is
  verified=false, reason=unsigned. The verified ones are merge commits GitHub signs
  server-side. Identity claims who acted; only a signature makes the claim checkable,
  which is what the identity rules added earlier were missing. Separately, the owner
  observed this agent repeatedly reaching for approaches it had already seen fail in the
  same session -- so recording and consulting operational lessons is now required rather
  than left to habit.


## 2026-09-05T22:06:46Z — Enforcement register, concern index, and the first rung-4 check
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** GOVERNANCE_HIERARCHY.md gains a measured enforcement register; new
  CONCERNS.md assembles the tiers per topic for answering questions; new
  .github/pull_request_template.md requires the classification before the diff is read;
  new .github/workflows/doctrine-size.yml enforces the doctrine budget in CI.
- **Why:** governance had no honest account of what it actually enforces, and measuring
  found the answer was close to nothing: 0 of 26 repositories protect main, 0 have
  CODEOWNERS, 0 carry the required social preview, and the single automated mechanism was
  failing in 15 of 26 with nobody aware. Classification and doctrine size were both
  self-attested rules that had already been broken while written down, so both moved onto
  rungs where forgetting is not enough.


## 2026-09-05T21:37:27Z — Governance reaches actors everywhere, repositories by membership
- **Actor:** Claude (agent)
- **Initiated by:** @HarithKavish (requested)
- **Change:** Article 1 gains the scope clause; GOVERNANCE_HIERARCHY.md gains a Scope
  section defining actor rules vs repository rules and the test between them;
  standards/DEVELOPMENT.md gains commit provenance (Initiated-By). Four places that said
  the opposite were repaired in the same change: AGENT_BOOTSTRAP.md step 3, the
  non-member GOVERNANCE.md template, the excluded vocabulary in schemas/ecosystem.yaml,
  and standards/REPOSITORY.md.
- **Why:** non-participation used to mean no rules at all, which put the least supervised
  repositories furthest outside every safeguard. A learning exercise genuinely does not
  need a social preview image or the design system; an agent working in it still needs to
  identify itself honestly, say who asked, and not commit a credential.


## 2026-09-05T21:14:22Z — One identity per actor, and what co-authorship means
- **Actor:** Claude (agent), acting for the repository owner
- **Change:** standards/SECURITY.md gains one-identity-per-actor and use-the-official-one;
  standards/DEVELOPMENT.md defines co-authorship as genuinely shared work in one commit.
- **Why:** the owner corrected two things. This agent had minted its own per-version
  identity (claude-opus-5@users.noreply.github.com) rather than using the canonical
  Anthropic one — exactly the fragmentation the new rule forbids, since an identity that
  changes per model release makes continuous work look like strangers'. And the co-author
  trailer was being applied as a disclosure stamp rather than reserved for commits that
  genuinely contain two actors' work.
- **Corrects:** the entries below record this agent as *Claude Opus 5*. That naming was
  wrong under the rule added here. Per the append-only rule those entries are left as
  written; the actor in all of them is **Claude**.


## 2026-09-05T21:08:11Z — Omit the co-author trailer when the actor is the author
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** standards/DEVELOPMENT.md, Commits.
- **Why:** the owner observed a commit naming Claude as both author and co-author, under
  two different addresses. The trailer exists to credit a contributor who is not the
  author; once the agent authors its own commits the trailer credits the same actor twice
  and reads as two contributors. Disclosure is already served, more strongly, by the
  author field.

## 2026-09-05T21:03:01Z — Changelog and actor attribution
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** this file; the append-and-record rule in MAINTENANCE.md; commit attribution
  in standards/DEVELOPMENT.md; authenticate-as-yourself in standards/SECURITY.md; verify
  your configured identity before acting in standards/AGENT_ENVIRONMENT.md.
- **Why:** raised after the owner noticed governance commits authored as *Jarvis*. They
  were this agent — the VM git config named a different actor and it was inherited without
  being checked, so roughly twenty commits across the ecosystem misattribute the work. The
  history is not being rewritten: those commits are merged and shared, and rewriting shared
  history is worse than the misattribution. The rules exist so the next agent checks first.

## 2026-09-05T20:50:59Z — Design system: cross-surface check and declared opt-outs
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** `standards/DESIGN_SYSTEM.md` gains a before-adding cross-surface
  check and a bounded selective opt-out; `schemas/ecosystem.yaml` drops the
  deleted `harith-design-system` entry.
- **Why:** promotion was purely reactive, triggered only once a duplicate already existed;
  and a surface previously had no middle ground between using a shared piece and declaring
  a whole second identity.

## 2026-09-05T19:27:18Z — Mark mcp-registry-mcp-server as integrated
- **Actor:** HarithKavish (human)
- **Change:** `schemas/ecosystem.yaml` adoption state and notes for that
  repository.
- **Why:** it was onboarded — AGENTS.md and GOVERNANCE.md added — so the registry no
  longer matched reality.

## 2026-09-05T13:09:47Z — Add the Deployment standard
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** new `standards/DEPLOYMENT.md`; Article 5 extended by one item;
  routing rows in `AGENT_BOOTSTRAP.md` and `README.md`.
- **Why:** nothing owned what happens between `main` and a live surface, so
  deployment could sit entirely in platform settings and be invisible to review.

## 2026-09-04T20:45:14Z — Govern the agent environment
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** new `standards/AGENT_ENVIRONMENT.md`; new
  `schemas/governance.yaml`; `MAINTENANCE.md` timestamp rule.
- **Why:** Article 1 already governed agents but nothing implemented it, and Article 2
  assumed a repository could detect it had fallen behind when nothing let it.

## 2026-09-04T18:40:00Z — Registry completeness
- **Actor:** Claude Opus 5 (agent), acting for the repository owner
- **Change:** Article 5 sharpened; `standards/REPOSITORY.md` registry rules;
  `protocols/REPOSITORY_ALIGNMENT.md` Phase 0; `schemas/ecosystem.yaml`
  made complete against the account.
- **Why:** a repository could exist with no membership decision at all, indistinguishable
  from a deliberate exclusion — 26 of 54 were in that state.

---

*Entries before 2026-09-04 predate this file and are recorded only in git history.*
