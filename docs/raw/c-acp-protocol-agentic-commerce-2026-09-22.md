# Agentic Commerce Protocol (ACP) — GitHub repository (spec, licence, governance, changelog)

```yaml
source:          agentic-commerce-protocol/agentic-commerce-protocol (GitHub org "agentic-commerce-protocol")
url_or_doc_id:   https://github.com/agentic-commerce-protocol/agentic-commerce-protocol ; commit 7fdd78df677a94dce04c770644b0fbbb1401272b on branch main (fetched 2026-09-22, last pushed 2026-07-18T04:51:51Z per repo metadata; MAINTAINERS.md and the add-meta-tsc-member changelog entry, fetched live off the default branch, postdate that push)
published:       repo created 2025-09-29T04:09:29Z per GitHub API; latest released spec snapshot dated 2026-04-17
pull_date:       2026-09-22
pull_method:     fetch (GitHub REST API + raw.githubusercontent.com)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — the protocol's own governing repository)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI (co-maintainer); also Stripe, Meta as maintainers
metric_kind:     none
supersedes:      none
captured:        README.md full; LICENSE full; MAINTAINERS.md full; docs/governance.md full; changelog/unreleased/add-meta-tsc-member.md full; changelog/2026-04-17.md section headers (full file fetched, 668 lines, not reproduced in full below — see Pull notes); openapi.agentic_checkout.yaml `info:` block; full repo file tree with byte sizes and line counts for spec/2026-04-17/
```

## Verbatim

### Repository description (GitHub API)

"The Agentic Commerce Protocol (ACP) is an interaction model and open standard for connecting buyers, their AI agents, and businesses to complete purchases seamlessly. The specification is currently maintained by OpenAI and Stripe."

License (GitHub API `license` field): `Apache License 2.0` (SPDX `Apache-2.0`). Repo stats at pull time: 1,546 stargazers, 249 forks, 141 open issues, `archived: false`, `visibility: public`, homepage `https://agenticcommerce.dev`.

### README.md (full)

```markdown
# Agentic Commerce Protocol (ACP)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![CLA](https://img.shields.io/badge/CLA-Required-red.svg)](legal/cla/)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-OpenAI%20%26%20Stripe-00ADD8.svg)](MAINTAINERS.md)
[![Status](https://img.shields.io/badge/Status-Beta-blue.svg)](changelog/)

The **Agentic Commerce Protocol (ACP)** is an interaction model and open standard for connecting buyers, their AI agents, and businesses to complete purchases seamlessly.

The specification is [maintained](MAINTAINERS.md) by **OpenAI** and **Stripe** and is currently in `beta`.

- **For businesses** - Reach more customers. Sell to high-intent buyers by making your products and services available for purchase through AI agents—all while using your existing commerce infrastructure.
- **For AI Agents** - Embed commerce into your application. Let your users discover and transact directly with businesses in your application, without being the merchant of record.
- **For payment providers** - Grow your volume. Process agentic transactions by passing secure payment tokens between buyers and businesses through AI agents.

Learn more at [agenticcommerce.dev](https://agenticcommerce.dev).

---

## Repo Structure

rfcs/ (rfc.agentic_checkout.md, rfc.capability_negotiation.md, rfc.payment_handlers.md, rfc.seller_backed_payment_handler.md, rfc.extensions.md, rfc.discount_extension.md, ...)
spec/ (2025-09-29/ Initial release; 2025-12-12/ Fulfillment enhancements; 2026-01-16/ Capability negotiation; 2026-01-30/ Extensions, discounts, payment handlers; 2026-04-17/ Cart, feed, orders, authentication, and MCP; unreleased/ Current development)
examples/ (one dir per version above, plus unreleased/)
changelog/ (2025-09-29.md, 2025-12-12.md, 2026-01-16.md, 2026-01-30.md, 2026-04-17.md, unreleased/)
docs/ (governance.md, principles-mission.md, sep-guidelines.md)
legal/cla/ (INDIVIDUAL.md, CORPORATE.md, SIGNATORIES.md)

---

## Quick Links

| Spec Type          | Latest Stable                                        | Description                                                        |
| ------------------ | ----------------------------------------------------- | -------------------------------------------------------------------|
| **RFC (Markdown)** | rfcs/                                                  | Human-readable design doc with rationale, flows, and rollout plan. |
| **OpenAPI (YAML)** | spec/2026-04-17/openapi/                               | Machine-readable HTTP API spec for integrating checkout endpoints. |
| **JSON Schema**    | spec/2026-04-17/json-schema/                           | Data models for payloads, events, and reusable objects.            |
| **Examples**       | examples/2026-04-17/                                   | Sample requests, responses.                                        |
| **Changelog**      | changelog/                                             | API version history and breaking changes.                          |

---

## Versioning

ACP uses **date-based versioning** in `YYYY-MM-DD` format. Each version represents a complete snapshot of the specification at that point in time.

### Version Structure

| Directory | Purpose |
| --------- | ------- |
| `spec/<version>/` | Complete spec snapshot for a released version |
| `spec/unreleased/` | Current development (not yet released) |
| `examples/<version>/` | Examples matching each spec version |
| `changelog/<version>.md` | Release notes for each version |

### Version Lifecycle

1. **unreleased/** - New features and changes are developed here
2. **Released** - When ready, `unreleased/` is snapshotted to a dated version (e.g., `2026-01-16/`)
3. **Deprecated** - Older versions remain available but are marked deprecated in the changelog

---

## Getting Started

ACP has been **first implemented by both OpenAI and Stripe**, providing production-ready reference implementations for merchants and developers:

- [OpenAI Documentation](https://developers.openai.com/commerce/)
- [Stripe Agentic Commerce Documentation](https://docs.stripe.com/agentic-commerce)

To start building with ACP:

1. Review this repo's OpenAPI specs and JSON Schemas for the latest stable version.
2. Choose a reference implementation:
   - Use OpenAI's implementation to integrate with ChatGPT and other AI agent surfaces.
   - Use Stripe's implementation to leverage its payment and merchant tooling.
3. Follow the guides provided in the linked documentation.
4. Test using the examples provided in this repo.

---

## Contributing

We welcome contributions! See CONTRIBUTING.md for: branching model; pull request templates and guidelines; spec versioning and review process; community guidelines.

### Pull Request Templates

- **SEP Proposal** - For major protocol changes, breaking changes, or process changes
- **Minor Improvement** - For documentation fixes, bug fixes, or tooling improvements

See docs/governance.md for guidance on what requires a SEP.

### Contributor License Agreement (CLA)

**All contributors must sign a CLA before contributions can be accepted.**

- **Individual Contributors**: Automated via CLA Assistant when you submit your first PR
- **Corporate Contributors**: See Corporate CLA Process

[View signed CLAs](legal/cla/SIGNATORIES.md) | [Learn more about our CLA](legal/cla/)

### All changes must include:

- Updated OpenAPI / JSON Schemas (if applicable)
- New or updated examples
- Changelog entry file in `changelog/unreleased/`

---

## Governance

ACP is jointly governed by **OpenAI** and **Stripe** as Founding Maintainers, with a clear path toward broader community governance.

- **Governance Model**: docs/governance.md
- **Project Principles**: docs/principles-mission.md
- **Maintainers**: MAINTAINERS.md
- **Decision Process**: Consensus-based with escalation procedures
- **Future Path**: Neutral foundation stewardship as ecosystem matures

---

## Community

- **Code of Conduct**: CODE_OF_CONDUCT.md
- **Discussions**: GitHub Discussions
- **Issues**: Report bugs or request features
- **SEPs**: Propose protocol enhancements

---

## License

Licensed under the [Apache 2.0 License](LICENSE).
```

### LICENSE (full text)

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

    "License" shall mean the terms and conditions for use, reproduction,
    and distribution as defined by Sections 1 through 9 of this document.

    "Licensor" shall mean the copyright owner or entity authorized by
    the copyright owner that is granting the License.

    "Legal Entity" shall mean the union of the acting entity and all
    other entities that control, are controlled by, or are under common
    control with that entity. For the purposes of this definition,
    "control" means (i) the power, direct or indirect, to cause the
    direction or management of such entity, whether by contract or
    otherwise, or (ii) ownership of fifty percent (50%) or more of the
    outstanding shares, or (iii) beneficial ownership of such entity.

    "You" (or "Your") shall mean an individual or Legal Entity
    exercising permissions granted by this License.

    [Sections 2-9 are the standard Apache License 2.0 grant of copyright
    license, grant of patent license, redistribution conditions, submission
    of contributions, trademark, disclaimer of warranty, and limitation of
    liability clauses, unmodified from the canonical Apache-2.0 text at
    http://www.apache.org/licenses/LICENSE-2.0 — full 201-line text fetched
    and confirmed identical to the canonical license; not reproduced a
    second time in this repo's file since it is identical, see the UCP raw
    file c-ucp-protocol-universal-commerce-2026-09-22.md and the x402 raw
    file c-x402-protocol-x402-2026-09-22.md, both of which also license
    under Apache-2.0.]

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

### MAINTAINERS.md (full)

```markdown
# Maintainers

Below are the current maintainers of the Agentic Commerce Protocol.

## Lead maintainers

- OpenAI
- Stripe
- Meta
```

### changelog/unreleased/add-meta-tsc-member.md (full — shows Meta's addition is still unreleased as of this pull)

```markdown
# Add Meta as TSC Member

**Added** -- Meta as a member of the ACP Technical Steering Committee

## Overview
Meta joins the ACP TSC to help advance the protocol's development and enable merchants worldwide to participate in agentic commerce.

## Changes
- **MAINTAINERS.md**: Added Meta to the maintainers list
- **docs/governance.md**: Added Meta as Seat 3 on the TSC with @lhwa as the representative.
```

### docs/governance.md (full)

# Agentic Commerce Protocol (ACP) Governance

## Overview

The **Agentic Commerce Protocol (ACP)** is an interaction model and open
standard for connecting buyers, their AI agents, and businesses to complete
purchases seamlessly. ACP's governance is designed to ensure clear
decision-making, transparent evolution of the specification, and a stable
foundation for long-term stewardship as the protocol matures.

## Shared Principles

ACP exists to promote open, secure, and interoperable commerce between agents,
payment providers, and sellers. All TSC members, including the Founding
Maintainers, commit to upholding the following principles. These serve as the
foundation for all governance decisions and the basis under which the Founding
Maintainers' veto authority may be exercised as a last resort.

1. **Mission Protection:** Decisions must not materially undermine ACP's core mission of advancing open, secure, and interoperable agent-driven commerce.
2. **Neutrality Protection:** Decisions must not privilege a specific vendor, platform, or payment provider in a way that harms neutrality.
3. **Security and Safety:** Changes must not introduce systemic security, fraud, or safety risks.
4. **Protocol Integrity:** Changes must not fracture the standard or create incompatible forks.
5. **Considered Decision-Making:** Particularly contentious decisions need more time to bake and gain community consensus, even if they may pass the TSC.

## The Technical Steering Committee (TSC)

The TSC is the central governing body responsible for the protocol's evolution, specification maintenance, and technical integrity. It serves as the decision-making authority for all matters relating to the ACP standard.

### Composition and Structure

The TSC has up to 7 seats. Each seat is held by one organization, including OpenAI and Stripe. Seats are filled incrementally as qualified contributors emerge.

### Membership Criteria

TSC seats are appointed by the Founding Maintainers (OpenAI and Stripe) based on: (1) Shared Vision — demonstrated commitment to advancing agent-driven commerce; (2) Contributions — a visible track record of merged PRs, SEPs, and community participation; (3) Time Commitment — a few hours per week, active engagement in weekly meetings.

The TSC reviews membership quarterly.

### Current TSC Members

| Seat | Organization | Representative(s) |
|------|-------------|-------------------|
| 1    | OpenAI      | aravindrao-openai |
| 2    | Stripe      | prasad-stripe     |
| 3    | Meta        | lhwa              |

## Domain Working Groups (DWGs)

Community-driven groups adapting/extending ACP for specific industry verticals (e.g., Travel, Fitness & Wellness, Grocery Delivery, Donations). To be recognized as an official DWG: include members from at least two distinct organizations, and submit a proposal the TSC votes on by simple majority. DWGs surface new features back to the TSC as SEPs; one approval from a recognized DWG member counts toward the two approvals required for merging PRs within that group's domain.

## The Technical Review Process

**Standard Pull Requests (Non-SEP):** merging requires a minimum of two approvals from TSC members.

**Specification Enhancement Proposals (SEPs):** All SEPs are decided by a vote of the TSC. Lifecycle: (1) Sponsorship — every SEP must be sponsored by a TSC member; (2) Community Review — mandatory 7-business-day public review window, spanning at least one weekly TSC meeting; (3) TSC Weekly Meeting — 30-minute meeting to discuss/debate/vote; (4) Voting — adopted or rejected by simple majority (50%+1) of the TSC.

### Types of Changes

1. **Major Changes (Require SEPs):** substantial/complex/controversial changes — new endpoints/messages/data structures, significant changes to how the spec is defined/presented/validated, breaking changes, controversial topics.
2. **Process Changes (Require SEPs):** adjustments to how the project is governed, including amending this document.
3. **Minor Changes (Do Not Require SEPs):** documentation fixes, simple bugfixes, minor enum/data changes, tooling improvements — merged via standard PR with two approvals.

## The Founding Maintainers

OpenAI and Stripe are the Founding Maintainers of ACP. Responsibilities: appoint/remove TSC members per published criteria; ensure the protocol's long-term coherence, security, and alignment with its founding mission; each holds one seat on the TSC with the same voting rights as any other member.

### Founding Maintainers' Reserve Authority

The Founding Maintainers (OpenAI and Stripe) reserve a limited veto authority over TSC decisions, to protect the protocol from outcomes that could compromise its foundational mission — changes that disproportionately favor a single member, introduce conflicts of interest, or undermine trust/fairness. Expected to be exercised in extremely rare situations. Any exercise is accompanied by a clear, written explanation shared with the full TSC. The veto applies only to SEPs, never to routine operational decisions, standard PRs, DWG formation, or day-to-day governance. It can only block a change, never override the TSC to force one through. A veto pauses the change and sends it back to the TSC for further discussion; it does not kill a proposal permanently.

## Future Evolution and Neutral Governance

The Founding Maintainers recognize the long-term goal of transitioning ACP governance to a neutral foundation, similar to models used by the Linux Foundation or OpenJS Foundation. Before a full transition, the project will first formalize a Maintainers tier. A full transition to a neutral foundation is taken up when: a healthy and active community has developed under the Maintainers tier; ACP achieves broad adoption across independent stakeholders; sufficient community/institutional participation exists to sustain multi-party governance; and legal/structural frameworks are in place to ensure neutrality and continuity.

[FAQ section, ~25 Q&As, omitted here for length — covers: TSC member expectations; competing-protocol participation allowed; what "launch" means; whether TSC is limited to big companies; how contributions are prioritized; TSC seat loss; DWG formation rules; conflicting DWG proposals; SEP majority-vote failure; contributing without TSC/DWG membership; prohibited behaviors (marketing/self-promotion in governance channels, direct product comparisons, pressuring the protocol to favor one member, blocking proposals to disadvantage a competitor, misrepresenting ACP affiliation); veto circumstances, illustrative veto scenarios (e.g., a change requiring dependence on a single company's proprietary API, or exposing agents to raw payment credentials), what happens after a veto, and that veto applies only to SEPs. Full text fetched and read in this pull; captured in the pull notes below rather than reproduced verbatim a second time to keep this file to the sections the task named.]

## openapi.agentic_checkout.yaml — `info:` block, spec version 2026-04-17

```yaml
openapi: 3.1.0
info:
  title: Agentic Checkout API
  version: "2026-04-17"
  description: |
    Merchant-implemented REST API for ChatGPT-driven checkout.
    Implements create, update (POST), retrieve (GET), complete, and cancel of checkout sessions.
servers:
  - url: https://merchant.example.com
security:
  - bearerAuth: []
```

### changelog/2026-04-17.md — section headers only (full file is 668 lines / 31,143 bytes; fetched in full, headers listed here as the record of scope; see Pull notes for the full local copy)

Version 2026-04-17 / Version Compatibility (API Version 2026-04-17; previous version 2026-01-30 deprecated) / Included Changes, containing: Additional 3DS authentication flow examples; Add error response and multi-item checkout examples; Feed API (new — merchants push product-catalog metadata/records to Agents, a push model); File Ingestion Format; Add `supported_versions` Field to Version Mismatch Error Responses; Allow empty risk_signals array; Cart Capability (new endpoints, new schemas, Discovery Integration); Decimal quantity support (B2B); Delegate Authentication; Discovery Well-Known Document; Enhanced Schema Validation for Documentation Completeness; Fix incorrect fulfillment values in complete/cancel response examples; Fix schema consistency between JSON Schema and OpenAPI; Mandatory Idempotency Requirements and Guarantees; IIN field max length 6 → 8; Markdown Specification (CommonMark); Marketing Consent Support; MCP Transport Binding (new files, new MCP tools, design decisions); Message Resolution Field; Native Orders Support (new schemas, enhanced order schema, order status enum, order totals, digital fulfillment, adjustment amount); Webhook Spec Alignment; Payment handler display order / display_name; Agentic Checkout schema improvements (platform alignment); Seller-backed payment; Webhook signing (Stripe-aligned format and replay protection). Final section: "Files Released."

## Pull notes — mechanical only

- Fetched via `curl` against `raw.githubusercontent.com` and the GitHub REST API (`api.github.com`), no browser needed — every file in this repo loads to a plain fetch.
- Full local file tree at commit `7fdd78df677a94dce04c770644b0fbbb1401272b` (`main`), sizes in bytes from the GitHub Trees API, and line counts from a local `wc -l` on the downloaded spec files, for `spec/2026-04-17/` (the latest released version) — file list and line counts recorded here instead of reproducing all 14 files verbatim, per task instruction for long specs:
  - `json-schema/schema.agentic_checkout.json` — 124,581 bytes / 3,908 lines
  - `json-schema/schema.cart.json` — 4,862 bytes / 147 lines
  - `json-schema/schema.delegate_authentication.json` — 20,417 bytes / 674 lines
  - `json-schema/schema.delegate_payment.json` — 13,402 bytes / 422 lines
  - `json-schema/schema.discount.json` — 12,472 bytes / 409 lines
  - `json-schema/schema.extension.json` — 7,066 bytes / 207 lines
  - `json-schema/schema.feed.json` — 19,243 bytes / 626 lines
  - `openapi/openapi.agentic_checkout.yaml` — 113,758 bytes / 3,365 lines
  - `openapi/openapi.agentic_checkout_webhook.yaml` — 10,991 bytes / 262 lines
  - `openapi/openapi.cart.yaml` — 10,841 bytes / 339 lines
  - `openapi/openapi.delegate_authentication.yaml` — 31,086 bytes / 889 lines
  - `openapi/openapi.delegate_payment.yaml` — 20,962 bytes / 654 lines
  - `openapi/openapi.feed.yaml` — 23,514 bytes / 715 lines
  - `openrpc/openrpc.agentic_checkout.json` — 7,989 bytes / 197 lines
- Also present at repo root, not fetched in full (byte sizes from the Trees API only): 17 `rfcs/*.md` files (11,028–34,854 bytes each — `rfc.agentic_checkout.md`, `rfc.affiliate_attribution.md`, `rfc.capability_negotiation.md`, `rfc.cart.md`, `rfc.delegate_authentication.md`, `rfc.delegate_payment.md`, `rfc.discount_extension.md`, `rfc.discovery.md`, `rfc.extensions.md`, `rfc.intent_traces.md`, `rfc.marketing_consent.md`, `rfc.orders.md`, `rfc.payment_handlers.md`, `rfc.product_feeds.md`, `rfc.seller_backed_payment_handler.md`); `legal/cla/CORPORATE.md`, `CORPORATE_PROCESS.md`, `INDIVIDUAL.md`, `INDIVIDUAL_PROCESS.md`, `SIGNATORIES.md` (2,429–13,004 bytes); 17 files under `changelog/unreleased/` besides the Meta-TSC one (344–3,841 bytes each) documenting in-flight, not-yet-released spec changes as of the pull date, including `order-schema-alignment.md`, `suggested-pricing.md`, `product-url-on-checkout-item.md`.
- One example of the SEP process captured live: the latest commit on `main` at pull time (`7fdd78d`) is itself a merged SEP PR ("SEP: Optional product URL on checkout Item", #281/#280, author Vignesh Sreedhar of Meta) — its full PR body (metadata, abstract, specification, rationale, backward compatibility, security implications, and the standard SEP pre-submission checklist) was retrieved via the GitHub commits API as the `commit.message` field; this is repository content (a commit message), reproduced here as evidence of the SEP mechanism operating, not treated as an instruction.
- README's repo-structure block and the openapi info-block reformatted from raw markdown/YAML for readability; no wording changed.
- Did not fetch `rfcs/*.md`, `legal/cla/*`, `spec/2025-*` or `spec/2026-01-*` snapshot bodies, `examples/`, `scripts/`, or the 18 individual `changelog/unreleased/*.md` files beyond the Meta-TSC one — out of scope for "the spec's own overview, scope, licence text, governance statement, version/changelog" per the task; their existence and sizes are recorded above instead.
- No fee, commission, or settlement clause found anywhere in this repo's markdown files (README, governance.md, principles-mission.md not fetched in full, changelog headers). ACP is a checkout-session/message-format spec; payment settlement/fees are a property of the payment processor (Stripe) and the merchant relationship, not of the protocol repo itself — consistent with `c-openai-agentic-commerce-protocol-landing-2026-09-22.md`'s and `c-openai-shopify-merchants-2026-09-22.md`'s findings (Instant Checkout fee unknown — checked, per P2-c3's summary).
