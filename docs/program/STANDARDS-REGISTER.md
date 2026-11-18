# Standards and Reference Register

> **Record, not authority.** Listing a publication here adopts nothing. It records what was
> consulted, its status on the date checked, and what the programme proposes to use it for.
> Governance cites a reference only where a standard here in `standards/` actually draws on
> it.

**Research date: 2026-11-18.** Statuses move: ISO 9001, ISO/IEC/IEEE 12207, ArchiMate, COBIT
and ITIL all published new editions in 2026, and several more are in revision. Re-check before
relying on any row older than six months.

**Copyright.** Most ISO, IEC and IEEE texts are paid and copyrighted. This register names them
and summarises their purpose. It reproduces none of their requirements, and nothing in this
repository may quote them beyond a title.

## Verification marks

| Mark | Meaning |
|---|---|
| **V** | Status verified on 2026-11-18 against the publisher's own page, or against two independent sources where the publisher's page could not be read (ISO's catalogue refuses automated requests) |
| **S** | Verified on 2026-11-18 against secondary sources only. Treat the detail as provisional |
| **C** | Carried forward from earlier knowledge (mid-2026). **Not** re-verified in this session; no revision was known then |

## Adoption decisions

| Decision | Meaning |
|---|---|
| **Reference** | Used to find gaps and to name things consistently. No conformance claimed (DEC-003) |
| **Crosswalk** | Worth a deliberate mapping against existing governance, as a later task (named in the roadmap) |
| **Monitor** | A revision is under way; wait for it before mapping |
| **Not applicable** | Does not fit the ecosystem as it stands; the reason is stated |

All decisions below are **proposed** by the programme. Adopting a reference binds nothing;
the owner may strike any row.

---

## Governance, management systems and risk

| ID | Reference | Publisher | Edition and status (2026-11-18) | Mark | Purpose | Applicability here | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| REF-01 | ISO 37000 — Governance of organizations: Guidance | ISO | 2021, current | C | Principles for governing bodies: purpose, accountability, oversight | Vocabulary for authority and accountability (GAP-A05, A06). Written for boards; most of it has no counterpart in a one-owner ecosystem | Reference | iso.org catalogue |
| REF-02 | COBIT — Enterprise governance of information and technology | ISACA | **COBIT 7** announced for 27 Oct 2026, replacing COBIT 2019; certification programme for 2019 being retired | S | Governance and management objectives for enterprise IT | Its objectives list is a useful checklist of what IT governance covers. Content of COBIT 7 not reviewed | Monitor | [ISACA COBIT 7](https://www.isaca.org/campaigns/cobit-7-teaser), [ISACA COBIT](https://www.isaca.org/resources/cobit) |
| REF-03 | ISO 9001 — Quality management systems: Requirements | ISO | **2026, edition 6, published 16 Sep 2026**; replaces 2015 (+Amd 1:2024). Transition for 2015 certificates about three years | V | Requirements for a QMS | Quality objectives and measurement (GAP-B04). Certification not pursued | Reference | [iso.org/standard/9001](https://www.iso.org/standard/9001) |
| REF-04 | ISO/IEC 20000-1 — Service management system requirements | ISO/IEC | 2018 (edition 3) + Amd 1:2024 (climate); no new edition found. Related: ISO/IEC TS 20000-18:2026 | V | Requirements for an SMS | Shape of the operations standard (GAP-F03, F04, F08) | Reference | iso.org catalogue; [JTC 1/SC 40 news](https://committee.iso.org/sites/jtc1sc40/home/news.html) |
| REF-05 | ISO/IEC 27001 — Information security management systems: Requirements | ISO/IEC | 2022 + Amd 1:2024 | C | ISMS requirements and Annex A controls (via ISO/IEC 27002) | Crosswalk SECURITY.md against Annex A themes after REF-18 | Reference | iso.org catalogue |
| REF-06 | ISO/IEC 27701 — Privacy information management | ISO/IEC | **2025, now a standalone standard** (Oct 2025), no longer an extension of 27001 | V | Privacy management requirements for controllers and processors | Only after DEC-P05 establishes which privacy law applies | Monitor | [DNV](https://www.dnv.us/assurance/Management-Systems/new-iso/transition/revision-of-isoiec-27701/), [Kiwa](https://www.kiwa.com/en/nl/about-kiwa/news/isoiec-277012025-published-updated-privacy-standard-offers-organizations-more-guidance) |
| REF-07 | ISO 22301 — Business continuity management systems | ISO | 2019 + Amd 1:2024 | C | BCMS requirements | Backup, restore and key-person risk inside the operations standard (GAP-B10, F08) | Reference | iso.org catalogue |
| REF-08 | ISO 31000 — Risk management: Guidelines | ISO | **2018 current; revision at DIS stage** (DIS registered 3 Nov 2026, 12-week ballot) | V | Risk principles, framework, process | Rating method for an ecosystem risk register (GAP-B07) | Monitor | [ISO/DIS 31000](https://www.iso.org/standard/88574.html), [TC 262 news](https://committee.iso.org/sites/tc262/home/news.html) |
| REF-09 | ISO 37301 — Compliance management systems | ISO | 2021 + Amd 1:2024 | C | Compliance obligations, controls, monitoring | Premature: there is no recorded obligation to manage yet (DEC-P05) | Not applicable — revisit after DEC-P05 | iso.org catalogue |
| REF-10 | ISO/IEC 42001 — AI management system | ISO/IEC | 2023 (edition 1), no amendment; adopted in Europe as EN ISO/IEC 42001:2026 (identical text). Certification-body rules: ISO/IEC 42006:2025 | V | Requirements for managing AI systems responsibly | AI systems as products (GAP-B09) | Reference | [OECD.AI entry](https://oecd.ai/en/dashboards/policy-initiatives/information-technology-%E2%80%94-artificial-intelligence-%E2%80%94-management-system-isoiec-42001), iso.org catalogue |

## Architecture and life cycle

| ID | Reference | Publisher | Edition and status | Mark | Purpose | Applicability here | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| REF-11 | TOGAF Standard | The Open Group | 10th Edition (2022) | C | Enterprise architecture method and content framework | Vocabulary only. A full ADM cycle is disproportionate for the ecosystem | Reference | [opengroup.org/togaf](https://www.opengroup.org/togaf) |
| REF-12 | ArchiMate Specification | The Open Group | **ArchiMate 4, April 2026** (doc C260); 42 concepts, down from 60 in 3.2 | V | Architecture modelling language | Only if architecture diagrams become shared artefacts; manifests are the source today | Not applicable — revisit if diagrams are needed | [Open Group announcement](https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification) |
| REF-13 | ISO/IEC/IEEE 42010 — Architecture description | ISO/IEC/IEEE | 2022 | C | What an architecture description must contain: stakeholders, concerns, viewpoints | Checklist for `.project/architecture.md` content | Reference | iso.org catalogue |
| REF-14 | ISO/IEC/IEEE 15288 — System life cycle processes | ISO/IEC/IEEE | 2023 | C | System life-cycle process set | Life-cycle stage vocabulary (GAP-D05, D07) | Reference | iso.org catalogue |
| REF-15 | ISO/IEC/IEEE 12207 — Software life cycle processes | ISO/IEC/IEEE | **2026, edition 2 (April 2026)**, replaces 2017; adds concept and system definition, more agile coverage | S | Software life-cycle process set incl. operation, maintenance, disposal | Disposal process informs the retirement protocol (GAP-D07) | Reference | [ANSI blog](https://blog.ansi.org/ansi/iso-iec-ieee-12207-2026-software-life-cycle/) |
| REF-16 | ISO/IEC/IEEE 29148 — Requirements engineering | ISO/IEC/IEEE | 2018 current; edition 3 in draft | S | Requirements processes and information items | Phase 5 requirement identifiers (GAP-D04) | Monitor | [ISO draft, edition 3](https://www.iso.org/standard/94091.html) |
| REF-17 | ISO/IEC 25010 — Product quality model | ISO/IEC | 2023 | C | Quality characteristics (incl. safety, interaction capability) | Vocabulary for what the reviewer and gates assess | Reference | iso.org catalogue |

## Security, AI risk and software assurance

| ID | Reference | Publisher | Edition and status | Mark | Purpose | Applicability here | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| REF-18 | NIST Cybersecurity Framework | NIST | 2.0 (Feb 2024); Govern, Identify, Protect, Detect, Respond, Recover | C | Outcome-based security functions | **Crosswalk SECURITY.md first** — the framework is free and outcome-shaped, which suits this governance's style. Detect, Respond and Recover look thinnest today | Crosswalk | [nist.gov/cyberframework](https://www.nist.gov/cyberframework) |
| REF-19 | NIST AI Risk Management Framework | NIST | AI RMF 1.0 (AI 100-1, Jan 2023) + Generative AI Profile (AI 600-1, Jul 2024). A revision is announced; no draft as of late Oct 2026 | S | Govern, Map, Measure, Manage for AI risk | AI systems governance (GAP-B09), alongside REF-10 | Reference | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| REF-20 | NIST SP 800-218 — Secure Software Development Framework | NIST | **v1.1 final (Feb 2022)**. v1.2 (SP 800-218 Rev. 1) **initial public draft, 17 Dec 2025**, comments closed 30 Jan 2026, no final yet | V | Secure development practices: PO, PS, PW, RV | Crosswalk SECURITY.md + DEVELOPMENT.md; RV (respond to vulnerabilities) is the evident hole (GAP-E06, M06) | Crosswalk | [SP 800-218 final](https://csrc.nist.gov/pubs/sp/800/218/final), [Rev. 1 draft](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) |

## Service, delivery, finance

| ID | Reference | Publisher | Edition and status | Mark | Purpose | Applicability here | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| REF-21 | ITIL | PeopleCert (Axelos) | **ITIL (Version 5)** released 2026, alongside ITIL 4; no ITIL 4 retirement date on PeopleCert's page | V (name) / S (dates) | Service management practices; Version 5 adds an AI governance module | Practice names for incident, problem, change. Most ITIL practice is sized for service desks | Reference | [PeopleCert ITIL](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1) |
| REF-22 | Site Reliability Engineering; The Site Reliability Workbook | Google | 2016; 2018 (free online) | C | SLIs, SLOs, error budgets, postmortems | The SLO model for the operations standard: internal targets, distinct from commitments | Reference | [sre.google/books](https://sre.google/books/) |
| REF-23 | FinOps Framework | FinOps Foundation | **2026 update**: deeper guidance on Scopes; adds Executive Strategy Alignment | S | Cloud and technology cost management | A light platform-and-asset register with limits and costs (GAP-G05, G06) | Reference | [FinOps Framework](https://www.finops.org/framework/), [2026 update](https://www.finops.org/insights/2026-finops-framework/) |
| REF-24 | DORA research | DORA (Google Cloud) | 2025 *State of AI-assisted Software Development* (Sep 2025); no 2026 report found | V | Delivery measures: throughput and instability | Phase 6 measures from GitHub data (GAP-G09) | Reference | [DORA 2025 report](https://dora.dev/research/2025/dora-report/) |

## Platform

| ID | Reference | Publisher | Status | Mark | Purpose | Applicability here | Decision | Source |
|---|---|---|---|---|---|---|---|---|
| REF-25 | GitHub Docs — rulesets, security features, plans | GitHub | Live documentation. Rulesets: public repositories on Free; private need Pro/Team/Enterprise | V | What each GitHub capability does and which plan has it | The [capability matrix](GITHUB-CAPABILITY-MATRIX.md) | Reference | [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) |

## Legal and regulatory

**No legal or regulatory reference is listed, deliberately.** Which laws apply depends on
where the owner operates and where the users of personal-data surfaces are, and neither is
recorded (DEC-P05). Listing laws before that is guessing, and a guessed obligation is worse
than a recorded unknown: it gets complied with in place of the real one. When DEC-P05 is
answered, the applicable privacy, consumer and AI laws are added here from their official
sources, with the obligations each imposes.
