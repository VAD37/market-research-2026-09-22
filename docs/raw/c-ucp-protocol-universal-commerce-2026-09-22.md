# Universal Commerce Protocol (UCP) — GitHub repository (spec, licence, multi-org governance councils)

```yaml
source:          Universal-Commerce-Protocol/ucp (GitHub org "Universal-Commerce-Protocol"; central governance file lives in the sibling ".github" repo of the same org)
url_or_doc_id:   https://github.com/Universal-Commerce-Protocol/ucp ; https://github.com/Universal-Commerce-Protocol/.github/blob/main/MAINTAINERS.md ; https://ucp.dev
published:       repo pushed_at 2026-09-22T01:42:00Z per GitHub API (updated same day as this pull); "Copyright 2026 UCP Authors" in file headers
pull_date:       2026-09-22
pull_method:     fetch (GitHub REST API + raw.githubusercontent.com)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — the protocol's own governing repository)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Google — AI Mode, Gemini app (originating engine); governance councils separately name Amazon, Microsoft, Meta as members (see below) — cross-reference c-google-ucp-merchant-guide-2026-09-22.md and c-google-ucp-merchant-agentic-2026-09-22.md, already landed, not re-pulled here
metric_kind:     none
supersedes:      none
captured:        README.md full; LICENSE (Apache-2.0, confirmed identical to c-acp file, not reproduced a third time); MAINTAINERS.md (ucp repo, full) and the central .github/MAINTAINERS.md (full — all five councils); CONTRIBUTING.md (central .github repo) excerpt on the Enhancement Proposal process
```

## Verbatim

### Repository metadata (GitHub API)

Description: "Specification and documentation for the Universal Commerce Protocol (UCP)". License: Apache License 2.0. Homepage: `https://ucp.dev`. Stargazers: 3,388 at pull time. `archived: false`.

### README.md (full)

"<!-- Copyright 2026 UCP Authors. Licensed under the Apache License, Version 2.0 -->

# Universal Commerce Protocol (UCP)

**An open standard enabling interoperability between various commerce entities to facilitate seamless commerce integrations.**

Documentation: https://ucp.dev | Specification: https://ucp.dev/specification/overview | Discussions: github.com/Universal-Commerce-Protocol/ucp/discussions

## Overview

The Universal Commerce Protocol (UCP) addresses a fragmented commerce landscape by providing a standardized common language and functional primitives. It enables platforms (like AI agents and apps), businesses, Payment Service Providers (PSPs), and Credential Providers (CPs) to communicate effectively, ensuring secure and consistent commerce experiences across the web.

With UCP, businesses can: **Declare** supported capabilities to enable autonomous discovery by platforms. **Facilitate** secure checkout sessions, with or without human intervention. **Offer** personalized shopping experiences through standardized data exchange.

## Why UCP?

- **Standardize Interaction:** Provide a uniform way for platforms to interact with businesses, regardless of the underlying backend.
- **Modularize Commerce:** Breakdown commerce into distinct **Capabilities** (e.g., Checkout, Order) and **Extensions** (e.g., Discounts, Fulfillment).
- **Enable Agentic Commerce:** Designed from the ground up to support AI agents acting on behalf of users to discover products, fill carts, and complete purchases securely.
- **Enhance Security:** Support for advanced security patterns like AP2 mandates and verifiable credentials.

### Key Features

- **Composable Architecture:** UCP defines **Capabilities** (such as 'Checkout' or 'Identity Linking') that businesses implement.
- **Dynamic Discovery:** Businesses declare their supported Capabilities in a standardized profile.
- **Transport Agnostic:** Businesses can offer Capabilities via REST APIs, MCP (Model Context Protocol), or A2A, depending on their infrastructure.
- **Built on Standards:** UCP leverages existing open standards for payments, identity, and security wherever applicable.
- **Developer Friendly:** A comprehensive set of SDKs and libraries.

## Key Capabilities

The initial release focuses on: **Checkout** — cart management and tax calculation, with or without human intervention. **Identity Linking** — enables platforms to obtain authorization to perform actions on a user's behalf via OAuth 2.0. **Order** — webhook-based updates for order lifecycle events. **Payment Token Exchange** — protocols for PSPs and Credential Providers to securely exchange payment tokens and credentials.

## Contributing

- **Contribution Guide:** See CONTRIBUTING.md (in the `.github` repo) for details.
- **Maintainers:** See the central MAINTAINERS.md (in the `.github` repo) for the list of project maintainers.

## About

**UCP is an open-source project under the Apache License 2.0 and is open to contributions from the community.**"

### MAINTAINERS.md — Universal-Commerce-Protocol/.github repo (full — five governance bodies, verbatim membership as of 2026-09-22)

"# UCP Maintainers

## Shopping Tech Council

The Shopping Tech Council is responsible for the technical direction and overall design of the protocol for Shopping Domain.

| Name            | Company    |
| :-------------- | :--------- |
| Amit Handa*    | Google     |
| Anurag Sinha    | Google     |
| Daniel Wyckoff  | Shopify    |
| Drew Olson      | Google     |
| Gil Greenberg   | Shopify    |
| Greg Smith      | Google     |
| Ilya Grigorik   | Shopify    |
| Imran Hoosain   | Etsy       |
| James Andersen  | Meta       |
| Jing Li         | Google     |
| Jordan Williams | Amazon     |
| Lee Richmond    | Shopify    |
| Maxime Najim    | Target     |
| Patrick Jordan  | Microsoft  |
| Prasad Wangikar | Stripe     |
| Scot DeDeo      | Salesforce |
| Uddhav Kambli   | Wayfair    |

*Standing Governing Council (GC) member participating per GOVERNANCE.md rules.

## Food Tech Council

Responsible for the technical direction and design of the protocol for the Food Ordering Domain. Members: Amit Handa* (Google), Andrew Mackowski (Google), Jing Li (Google), Johnny Li (Square), Jon Hines (Toast), Luke Wulf (DoorDash), Malvi Hemani (Google), Nimish Sheth (Uber Eats), Niranjan Manjunath (Google), Teresa Qin (Google), Travis McPhail (Google), plus 6 open seats 'to be elected.'

## Lodging Tech Council

Members: Akhil Kavuri (Expedia), Alice Laic (Booking.com), Amit Handa* (Google), Chenlu Zhang (Trip.com), Colm Gallagher (Google), Devesh Arora (Marriott), Igor Levit (Google), Jing Li (Google), Lee Graham (Hilton), Niranjan Manjunath (Google), Ryan Adler-Levine (Google), Sean P. Carapella (Amadeus), Wishy Arora (Google), plus 4 open seats.

## Payments Tech Council

The Payments Tech Council is responsible for the technical direction and overall design of the protocol for Payments Domain. Members: Archana Malhotra (Google), Daniel Wyckoff (Shopify), Drew Olson (Google), Ed Siok (PayPal), Fabrice Cheng (Coinbase), Harsh Mehta (Global Payments), Ilya Grigorik* (Shopify), Jose Mendez (Adyen NV), Prasad Wangikar (Stripe), Prateek Dudeja (Google), Rose Wiegley (Shopify), Steven Chen (Ant International), Vita Valeikaite (Shopify), plus 4 open seats.

## Governance Council

The Governance Council is responsible for the overall adoption and health of the protocol. Members: Amit Handa (Google), Ilya Grigorik (Shopify), Twum Djin (Stripe), plus 2 open seats."

### CONTRIBUTING.md — Universal-Commerce-Protocol/.github repo (excerpt, governance process)

"# How to Contribute

We would love to accept your patches and contributions to this project.

### Sign our Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License Agreement (CLA)... Visit https://cla.developers.google.com/.

## Contribution Process

### Significant Changes

Any significant change to the protocol requires a formal **Enhancement Proposal** and will require **Tech Council (TC) approval**. Because a change to the protocol requires the entire adopting ecosystem to implement the change, we consider significant changes to include: Core Schema Modifications; Protocol Changes; New API Endpoints; Backwards Incompatibility.

An Enhancement Proposal is a living artifact that tracks a proposal through its lifecycle:
- **Proposal:** Anyone can submit; idea is proposed and debated.
- **Provisional:** TC majority vote to accept; enters working draft iteration.
- **Implemented:** TC majority vote to finalize; code complete and merged."

## Pull notes — mechanical only

- Fetched via `curl` against `raw.githubusercontent.com` and `api.github.com`; no browser needed.
- Governance model differs structurally from ACP's single Technical Steering Committee: UCP splits governance into **five separate bodies** — four vertical Tech Councils (Shopping, Food, Lodging, Payments) plus an overarching Governance Council — each with its own named seat-holders from named companies. This directly answers "who controls it / who can change it" for UCP: no single company; a named multi-company council structure, contribution-license-gated (Google CLA) and Enhancement-Proposal/TC-majority-vote gated for any significant change.
- Companies named across the five UCP councils (deduplicated, as they appear): Google, Shopify, Etsy, Meta, Amazon, Target, Microsoft, Stripe, Salesforce, Wayfair, Square, Toast, DoorDash, Uber Eats, Expedia, Booking.com, Trip.com, Marriott, Hilton, Amadeus, PayPal, Coinbase, Global Payments, Adyen NV, Ant International. This is the UCP "partner list" requested by the task, sourced from the protocol's own maintainers file rather than a marketing page.
- A `GOVERNANCE.md` file is referenced by the `MAINTAINERS.md` footnote ("* Standing Governing Council (GC) member participating per GOVERNANCE.md rules") but was not located at the expected path in either the `ucp` or `.github` repo trees fetched in this pull; recorded `unknown — checked Universal-Commerce-Protocol/ucp and Universal-Commerce-Protocol/.github repo trees 2026-09-22` — the footnote confirms a formal governance document exists and is referenced, but its content was not captured.
- No fee, commission, or settlement clause found in README.md, MAINTAINERS.md, or the CONTRIBUTING.md excerpt read. UCP defines "Payment Token Exchange" as a capability (PSPs and Credential Providers exchange tokens) but states no fee percentage in these files — consistent with the already-landed `c-google-ucp-merchant-guide-2026-09-22.md` and `c-google-ucp-merchant-agentic-2026-09-22.md`, both of which likewise found no pricing/fee language on Google's own UCP merchant pages.
- Cross-reference, not re-pulled: `c-google-ucp-merchant-guide-2026-09-22.md`, `c-google-ucp-merchant-agentic-2026-09-22.md`, and `c-google-merchant-ucp-checkout-2026-09-22.md` (all already landed under P2-c4) cover Google's own UCP merchant-facing pages (FAQ, checkout eligibility, country scope, `native_commerce(checkout_eligibility)` attribute, "select merchants... early access program" gating language) — this file covers the protocol's own GitHub repository and multi-org governance instead, which those three did not.
