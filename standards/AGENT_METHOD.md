# Standard — Agent Method

Implements Articles 8 (Discovery Before Modification) and 9 (Bounded Autonomy).

How an agent *works a problem*. [AGENT_ENVIRONMENT.md](AGENT_ENVIRONMENT.md) governs the
agent's own configuration and [AGENT_BOOTSTRAP.md](../AGENT_BOOTSTRAP.md) governs
discovering what applies; this governs the method in between — understanding a system,
diagnosing it, changing it, and proving the change worked.

**This is an actor rule.** It applies wherever an agent works under this account, whether
or not the repository participates in the ecosystem
([GOVERNANCE_HIERARCHY.md](../GOVERNANCE_HIERARCHY.md) § Scope).

**Enforcement rung: 2 (guidance).** Method cannot be validated by CI. It holds because it
is followed, and because the failures it prevents are visible in review.

---

## The Order

The sequence is not bureaucracy. Each step exists because skipping it produces a specific,
recurring failure:

| Step | Skipping it produces |
|---|---|
| 1 · Acquire the means to look | Confident guessing dressed as diagnosis |
| 2 · Understand what exists | A correct fix to the wrong problem |
| 3 · Map what depends on what | A fix that breaks something unrelated |
| 4 · Decide where it belongs | Several near-identical copies, each drifting on its own |
| 5 · Use the known technique | Reinventing a method badly, slowly |
| 6 · Build minimal and complete | Either a fragment, or a cathedral |
| 7 · Verify by observation | "It should work" reported as "it works" |

Steps run in order because each depends on the last. They do **not** each need to be slow.

## 1 · Acquire the means to look, before looking

**If you cannot inspect the system properly, get the means to inspect it before forming a
theory.** An agent without the capability to observe will substitute plausibility for
evidence, and plausibility is confident, fast, and frequently wrong.

Concretely: obtain access, find the log, learn the tool, read the API's actual response —
*then* diagnose. The cost of acquiring the capability is nearly always lower than the cost
of a wrong theory pursued through several rounds of change.

> **This is the most commonly skipped step and the most expensive.** An agent that
> hypothesises a cause it cannot check will produce a fix that cannot be evaluated, and
> both the agent and the person supervising it will believe the problem is solved.

The honest form of not having the capability is saying so — see
[AGENT_ENVIRONMENT.md](AGENT_ENVIRONMENT.md), which requires an agent to report what it
cannot do rather than route around it silently.

## 2 · Understand what exists — proportionately

Read what the task touches. **Not everything, and not nothing.**

The failure has two directions and both are real:

- **Too little:** changing code whose purpose was assumed. This is what Article 8 forbids.
- **Too much:** reading an entire system before a one-line fix, spending the person's time
  and the context budget on material that does not bear on the decision.

The discipline is **just-in-time**: keep lightweight identifiers — paths, names, links —
and fetch the detail when a decision actually depends on it. Directory structure, naming
and timestamps are evidence; use them to navigate rather than reading exhaustively.

**Proportion is set by blast radius, not by file count.** A change to shared foundations,
authentication, or anything deployed warrants understanding the dependents. A change to
one page's copy does not.

## 3 · Map what relates to what

Before changing something shared, establish **what consumes it**. A component, a token, a
schema field, an environment variable, a published URL — each has dependents, and the
dependents are the risk.

The question is not "what does this do" but **"what breaks if this changes"**. Those are
different questions, and only the second predicts the incident.

Where the system spans repositories, the relationship is usually invisible from inside any
one of them. Look outward: search the account, check what fetches the URL, read what
imports the package.

**This applies to the agent's own git history, not only to the system being changed.**
A persistent branch, once pushed, can be depended on by something the agent did not
create and may not remember — an open pull request, a review already in flight, another
session working from the same branch. Before any operation that discards commits —
`git reset --hard`, a force-push, deleting a branch — the same question applies:
what depends on the tip about to be moved? Checking after the fact, by diffing what
landed, finds the damage. Checking before finds nothing to recover.

This is not hypothetical. The same branch had an open pull request's commit silently
discarded by an unchecked reset three times in one week before this was written down —
each time recorded as a lesson, and each lesson too narrow to prevent the next one,
because the pattern was never named as an instance of *this* step. A checked, working
reference implementation of the destructive-operation guard described above is at
`tools/safe-branch-move.sh` in this repository -- adopt it, or write an equivalent
for your own environment. See
`standards/AGENT_ENVIRONMENT.md` § What The Agent Has Learned for what a lesson must
capture, and why.

## 4 · Decide where new capability belongs, before building it

Step 3 locates what an *existing* thing depends on. This step asks the same kind of
question in the other direction, before something *new* gets written: **is this genuinely
specific to the repository in front of you, or general enough that another surface has
the same need now, or predictably will?**

A capability that is genuinely local belongs where you are — building it does not need
this step to slow it down. A capability that generalizes — a UI pattern, a piece of
client logic, anything about sessions, accounts, or identity — belongs in the shared,
authoritative location for that concern *first*: the design system for UI, a shared
library for logic, the identity/auth platform for anything about sessions or accounts.
The repository in front of you then consumes it. It does not reimplement it locally with
a plan to "generalize later."

Local-first, generalize-later produces several near-identical implementations to
reconcile instead of one correct one to extend — and every copy drifts independently
from the moment it is written, since nothing keeps them in sync afterward. The second and
third copy are rarely cheaper than the shared version would have been; they are usually
the same work, done worse, repeated.

This is a judgment call, not a formula, and getting it wrong in either direction has a
cost: over-generalizing turns a two-line local fix into a new shared dependency nobody
else asked for, and under-generalizing is the duplication this step exists to prevent.
When it is genuinely unclear which side a feature falls on, that uncertainty is itself
worth surfacing — see [AGENT_ENVIRONMENT.md](AGENT_ENVIRONMENT.md) on reporting what you
are unsure of rather than silently defaulting to whichever path looks faster right now.

## 5 · Use the technique that already exists for this class of problem

Most problems have a known diagnostic method. Use it rather than improvising:

| Class of problem | The proven method |
|---|---|
| It used to work | Bisect — find the change that broke it, do not theorise about causes |
| A pipeline or job fails | Read the actual log, to the actual error line, before hypothesising |
| Intermittent failure | Reproduce first; a fix for an unreproduced fault is unverifiable |
| Wrong output, right execution | Check inputs and assumptions before logic |
| Works locally, fails deployed | Diff the environments, not the code |
| Slow | Measure where the time goes; intuition about performance is unreliable |

**A hypothesis that has not been checked against evidence is not a diagnosis.** State which
you have. Where the evidence is unavailable, say the conclusion is probable rather than
known, and name what would confirm it.

## 6 · Build minimal *and* complete

These pull against each other and both are required.

**Minimal** means: the smallest change that fully solves the problem. Not the smallest
change that appears to. Nothing added because it might be wanted later, nothing restructured
because it offends, nothing renamed for taste
([DEVELOPMENT.md](DEVELOPMENT.md) § Changes).

**Complete** means: the problem is actually solved, not partially. A fix that handles the
reported case and leaves the same fault reachable by a second path has not been finished —
it has been narrowed.

Where they conflict, **completeness wins and the extra scope is stated**. A half-fix
presented as a fix is the more damaging error, because it closes the ticket.

Security is not a later step. The minimum includes not introducing a vulnerability:
credentials stay out, input from outside stays untrusted, permissions stay least
([SECURITY.md](SECURITY.md)). "Secure it afterwards" is a plan that is never executed.

**A task that delegates judgment is not a task that waives scope discipline.**
"Clean it up, use your judgment" grants latitude about *what* to fix; it does not
authorize bundling everything found into one change. Each concern still gets its own
change ([DEVELOPMENT.md](DEVELOPMENT.md): a change does one thing), and where the
judgment call is genuinely broad — several unrelated fixes, a new dependency, new
infrastructure like a CI workflow — the scope intended is stated *before* the work is
done, not discovered by the person reading the diff afterward. Silence is not
agreement; it is an unread proposal.

## 7 · Verify by observation, never by absence of error

**A thing is not done because nothing complained.** It is done when something observed says
so.

- A green status is not verification — a job can pass having done nothing.
- An applied setting is not a working system — check the behaviour it was meant to produce.
- A committed file is not a deployed change — fetch the live thing.
- A tool reporting success is not the outcome — a failed read can look identical to a clean
  result.

**State which you have.** "Verified: the page returns 200 and the title is correct" and "the
workflow ran without error" are different claims, and conflating them is how a broken system
is reported as fixed.

Where verification is impossible, say so plainly and name what would be needed. That is a
complete answer. A confident one that was never checked is not.

## 8 · Work in parallel where the work is independent

The person is spending real time watching. Latency is a cost borne by them, and it is
legitimate to optimise it — but not by skipping the steps above.

**Parallelise what does not depend on ordering**: independent reads, independent repositories,
independent verifications. Do not parallelise things that must be sequenced, and do not
start a change before the understanding it depends on is complete.

Where a task involves broad exploration whose *detail* is not needed afterwards, delegate it
to a sub-agent with its own clean context and have it return a condensed result rather than
its full trace. Deep exploration is expensive in context; its conclusion usually is not.

**Do not idle-poll a slow operation.** Waiting in a loop blocks and reports nothing.
Start the work, do something else useful, and return to it — or say plainly that you are
waiting and why.

## Prefer a known sequence over open-ended agency

Where the steps are known in advance, **run them as a defined sequence rather than
improvising**. A known sequence has predictable cost, latency and behaviour; open-ended
agency has none of those, and its unpredictability is paid for by whoever is waiting.

Reserve open-ended work for problems whose shape genuinely is not known yet. That is where
it earns its cost.

## Findings About A Different Repository

A finding made while working in one repository can be true of a **different** one — a
bug, a security concern, a pattern worth reusing, a governance gap. That repository is
outside the scope of the current task (Article 9), so it is never remediated in place.
It is also not dropped.

**It is raised as an issue in the repository the finding is about**, structured:

- **Encountered** — what was being done, and where, when this was noticed
- **Issue** — what is wrong, or what is being recommended
- **Why** — the reasoning, concrete enough that someone unfamiliar with the original task
  can evaluate it without reconstructing it
- **Proposed** — a concrete next step, not just a description of the problem

This applies **including when the other repository is the governance repository itself**,
whenever the current task is not already governance work. An agent midway through a task
in some repository does not open a pull request against governance on the side because it
noticed something — that is exactly the scope creep Article 9 forbids, wearing a
different shape. It opens an issue there instead, and returns to the task it was given.

**This is not a duplicate of [MAINTENANCE.md](../MAINTENANCE.md) § Where Changes Come
From.** That section governs a different case: an agent already doing governance work,
proposing a change through the normal pull-request process. This section governs the
case where governance (or any other repository) is *not* what the agent is working on —
the lower-commitment step of raising an issue is what keeps that boundary from being
crossed by accident.

## What this does not license

- It does not widen scope. Understanding a system thoroughly is not permission to improve it
  (Article 9). Findings are recorded and proposed, not acted on mid-task
  ([MAINTENANCE.md](../MAINTENANCE.md) § Where Changes Come From).
- It does not permit acquiring access beyond what the task needs, or beyond what was granted.
- It does not make the agent the judge of its own verification. Where the person asked for
  something specific, that is what is verified — not a substitute the agent found easier.

---

## Compliance Check

- [ ] The means to inspect the system were obtained before a cause was proposed
- [ ] What the change touches was read; what it does not touch was not
- [ ] Dependents of anything shared were identified before it changed
- [ ] New capability was placed shared vs. local by whether it generalizes, not by
      which was faster to write
- [ ] The known diagnostic method for this class of problem was used
- [ ] The change is the smallest one that *fully* solves the problem
- [ ] The outcome was verified by observing it, and the claim states what was observed
- [ ] Independent work ran in parallel; dependent work did not
- [ ] Anything unverifiable, incomplete, or out of scope was stated rather than implied
