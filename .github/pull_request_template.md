<!--
This template exists because classification was self-attested and drifted anyway: the
doctrine grew by 18% in a single day with MAINTENANCE.md's rule already in place. Stating
the classification here moves it from something an author remembers to something a
reviewer can see before reading the diff.

Fill this in before the diff is read, not after. If you cannot answer section 1, the
change has not been classified yet — classify it (GOVERNANCE_MAP.md), then come back.
-->

## 1 — Classification

> `GOVERNANCE_MAP.md`, scope first and then type.

- **Gate A — who does it govern?** <!-- governance itself / one repository / one implementation / the whole ecosystem -->
- **Gate B — what kind of statement is it?** <!-- doctrine / standard / protocol / schema -->
- **Destination:** <!-- the exact file -->

If the requirement is layered, decompose it and list each layer with its own destination.

## 2 — Existing coverage

> `MAINTENANCE.md` Step 1. The default answer is not "add a file".

- **Searched:** <!-- where you looked -->
- **Found:** <!-- what already covers this, wholly or partly -->
- **Therefore:** <!-- nothing / improve existing / consolidate / relocate / add a rule / add a document -->

Reaching "add a document" should be rare, and needs a concern no existing document owns.

## 3 — Contradictions

Governance must not assert two models at once.

- [ ] I searched for statements that now contradict this change, and repaired them **in this pull request**
- **Repaired:** <!-- list them, or "none found — and here is what I searched for" -->

## 4 — Required by every governance change

- [ ] `schemas/governance.yaml` carries **this change's** timestamp, set in this change and not deferred
- [ ] `CHANGELOG.md` has an entry naming the actor, whether human or agent, and who initiated it
- [ ] Every relative link resolves; both schemas parse
- [ ] The doctrine gained no procedural content, and preferably no words
- [ ] Each requirement is stated **once**; everything else links rather than restates
- [ ] Nothing claims to be enforced that is not — the rung is stated honestly

## 5 — Provenance

- **Actor:** <!-- who made this change -->
- **Initiated by:** <!-- a handle if requested / schedule / autonomous -->

## 6 — What this does not do

<!--
State what you deliberately left out, what you could not verify, and what remains broken
after this lands. A gap that is written down gets fixed; a gap that is implied does not.
-->
