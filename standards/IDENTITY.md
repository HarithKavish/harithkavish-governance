# Standard — Identity

Who a person is, where that is decided, and what every other surface is allowed
to know about it.

Implements Article 3 (Single Source of Truth) for the one concern the ecosystem
cannot afford to hold in more than one place.

**Enforcement rung: 2 (guidance).** No part of this is enforced by
infrastructure yet, and most of it is not built — see *Current state* below.

---

## The Three Roles

| | Owns | Answers |
|---|---|---|
| **The account half** | The person: their account, profile, credentials, and which external identities are linked to them | *Who is this, and what is their account?* |
| **The authentication half** | Nothing about the person | *Has this person authenticated, for this application?* |
| **Every other surface** | Its own domain data, keyed by a subject it did not invent | *What does this application hold for that subject?* |

These are owners, not layers, and the boundaries between them are the point.

**The first two run in one deployable, at `account.harithkavish.com`.** That is a
deployment decision, not an ownership one: the boundary is kept in code, and
nothing about who owns what changed when the network between them went away
(canonical contract §0.5, §15). `auth.harithkavish.com` remains an alias.

A boundary held in code is as binding as one held across a network — but only
while nothing reads across it. The first query that does is the point at which
separating them again stops being a refactor.

## A HarithKavish Account Is the Identity

**Every person using the ecosystem has a HarithKavish account.** It is the only
identity there is. It exists in Account, it has a stable internal identifier,
and it outlives any particular way of signing in.

**Google — and any provider added later — is a way to prove that identity, never
a substitute for it.** Signing in with Google for the first time creates a
HarithKavish account and links that Google subject to it. It does not create a
"Google user". Someone who signs in with Google today and adds a passkey
tomorrow is one account with two ways in, not two accounts.

It follows that:

- **A provider identity is a link, not an account.** Account holds the link:
  which provider, which subject at that provider, and which account it belongs
  to. Removing the link must not remove the person.
- **A provider's identifier is never a primary key anywhere.** Not a Google
  `sub`, not an email address. Providers change subjects, people change
  addresses, and an email is a claim about a person rather than the person.
- **No surface asks a provider who someone is.** Applications ask Auth. Auth is
  the only thing in the ecosystem that talks to an external provider.

## What an Application May Hold

An application may hold **its own data**, keyed by the subject Auth issues.

An application may **not** hold:

- A password, a hash of one, or any other credential.
- A provider linkage — tokens, refresh tokens, provider account identifiers.
- A user table that is the origin of a person's identity rather than a
  reference to one.
- Any claim it did not receive from Auth in this session, treated as current.

An application **may** cache display claims — a name, a picture — provided it
treats them as a copy that can go stale, and never as the record.

**Test:** if this table were dropped, would a person cease to exist in the
ecosystem, or would only this application forget them? If the former, the table
is in the wrong place.

## Sessions

Each application keeps its own session, established from an Auth result and
verified on its own server. Sessions are not shared between applications; the
*identity* is shared, the *session* is not.

A shared client-side value — a cookie readable across subdomains — may say who a
person appears to be, so surfaces can show them consistently and avoid asking
again. **It is never evidence.** Any subdomain can write it. Authorisation is
decided from a verified session on a server, every time
([SECURITY.md](SECURITY.md)).

## Connected Accounts Are Not Login

An application that integrates with a third party — a GitHub organisation, a
Cloudflare account — holds that connection as **its own domain data**, scoped to
its own tenancy. That is unrelated to how the person signed in.

Signing in with a provider grants no authority over anything that provider hosts,
and connecting a provider is not a way to sign in. Conflating them is how a
login becomes an unintended grant.

---

## Current State

Recorded so the distance between this standard and the system is visible rather
than assumed. None of this is a criticism of the code; the pieces were built
before the boundary was written down.

| | Today | Under this standard |
|---|---|---|
| **Account** | Owns `users` (internal UUID, chosen `user_id`, Argon2id hash, names, status) and `account_events`. Account creation is real and deployed. | Same, plus linked provider identities. |
| **Auth** | Deliberately performs no authentication. Every attempt is refused, and the interface says so. | The only authenticator in the ecosystem. |
| **Forge** | Owns `users`, `accounts`, `sessions`, `verification_tokens` — including a `password_hash` column — and talks to Google directly with its own OAuth client. | Owns none of those. Keeps workspaces, projects, resources and the rest, keyed by the subject Auth issues. |
| **Static surfaces** | Talk to Google directly and keep the profile in a shared cookie for display. | Ask Auth. The shared cookie stays display-only either way. |

**Two gaps are worth naming plainly.**

Forge is currently its own identity provider. It holds credentials and provider
linkages for people who have a HarithKavish account elsewhere, which is the
duplication this standard exists to end.

**The contract now covers federated sign-in** (v1.3–v1.5): the authentication
half runs the provider flow and verifies the assertion, the account half owns
the resulting link, and a first sign-in creates a HarithKavish account. Schema
changes are authorized; nothing else is.

**Recovery lands before federation.** A federated-only account has exactly one
way in, and it is one the ecosystem does not control — a disabled provider
account is permanent lockout. An ordering constraint, not a preference.

## Getting There

The order matters, because each step removes a reason for the next one to be
hard.

1. **Account learns to hold a linked provider identity** — the table, and
   "first sign-in with a provider creates the account".
2. **The Account ↔ Auth contract covers federation**, since today it does not.
3. **The identity service authenticates for real**, Google included, and issues
   subjects — recovery first, then federation.
4. **Forge consumes Auth** and drops `users`, `accounts`, `sessions` and
   `verification_tokens`, re-keying its tenancy to the Auth subject.
5. **Static surfaces move from Google to Auth**, at which point one client
   registration serves the ecosystem.

Until step 3, surfaces talking to Google directly are a **declared deviation**
(Article 10) and not the target. They are recorded here rather than left to look
like the intended design.

## For Agents

- **Never add a credential, a provider token, or a provider identifier to an
  application's schema.** If a task appears to need one, the boundary is being
  crossed — say so.
- **Never treat a shared cookie, a claim, or an email as proof of identity.**
- **Do not resolve the federation gap by implementing something.** The contract
  is the place that decision is made ([MAINTENANCE.md](../MAINTENANCE.md)).
- A task that would give a second surface its own users table is a conflict with
  this standard: report it rather than proceeding
  ([GOVERNANCE_HIERARCHY.md](../GOVERNANCE_HIERARCHY.md)).
