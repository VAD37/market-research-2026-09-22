# Agent Payments Protocol (AP2) — GitHub repository, Google Cloud announcement, and FIDO Alliance donation

```yaml
source:          Google (google-agentic-commerce/AP2 GitHub org; cloud.google.com/blog; blog.google)
url_or_doc_id:   https://github.com/google-agentic-commerce/AP2 ; https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol ; https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/
published:       Google Cloud announcement 2025-09-17; repo pushed_at 2026-06-17T01:24:46Z per GitHub API; FIDO-donation blog post 2026-04-28
pull_date:       2026-09-22
pull_method:     fetch (GitHub REST API + raw.githubusercontent.com for the repo) and browser extension (get_page_text, for blog.google — plain fetch of blog.google renders a JS shell)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — the protocol's own repository and Google's own announcement/donation posts)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Google — AI Mode, Gemini app (via UCP integration); names ChatGPT/OpenAI ACP and MCP as protocols AP2 layers under/alongside
metric_kind:     none
supersedes:      none
captured:        README.md full; docs/overview.md full; docs/ap2/specification.md sections 1-2 (roles, agentic/non-agentic); CONTRIBUTING.md full (FIDO donation notice); cloud.google.com announcement full page text (extracted); blog.google FIDO-donation post full page text
```

## Verbatim

### github.com/google-agentic-commerce/AP2 — repo metadata (GitHub API)

Description: "Building a Secure and Interoperable Future for AI-Driven Payments." License: Apache License 2.0. Homepage: `https://ap2-protocol.org/`. Stargazers: 3,187 at pull time.

### README.md (excerpt)

"# Agent Payments Protocol (AP2)

This repository contains code samples and demos of the Agent Payments Protocol.

## About the Samples

These samples use Agent Development Kit (ADK) and Gemini 3.1 Flash Lite Preview. The Agent Payments Protocol doesn't require the use of either.

## Navigating the Repository

- `docs/` — specification, flows, FAQ, and MkDocs sources.
- `code/` — all source code, organized by artifact: `code/sdk/` (the AP2 SDK, Python at `code/sdk/python/ap2/`), `code/samples/` (reference implementations), `code/web-client/` (demo web client, Vite + React).

### Installing the AP2 Types Package

The protocol's core objects are defined under `code/sdk/python/ap2/` — Pydantic models in `models/` and `sdk/generated/`, canonical JSON schemas in `schemas/`. A PyPI package will be published at a later time. Until then: `uv pip install git+https://github.com/google-agentic-commerce/AP2.git@main`"

### CONTRIBUTING.md (full — governance statement)

"# How to Contribute

**The core specification has been donated to FIDO** (https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/). Please get involved to continue to develop the specification.

**Contributions to this repo going forward are to the samples and sdk only.**

## Before you begin

### Sign our Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License Agreement (CLA)... Visit https://cla.developers.google.com/ to see your current agreements or to sign a new one.

### Review our Community Guidelines

This project follows Google's Open Source Community Guidelines.

## Contribution process

### Code Reviews

All submissions, including submissions by project members, require review. We use GitHub pull requests for this purpose."

### docs/overview.md (Executive Summary and Guiding Principles, full)

"# Executive Summary

AI agents will redefine the landscape of digital commerce... this shift exposes a fundamental challenge: the world's existing payments infrastructure was not designed for a future where autonomous, non-human agents act on a user's behalf, or transact with each other... This creates ambiguity around transaction liability, and threatens adoption of agentic commerce.

Without a common, trusted protocol, the industry faces the prospect of a fragmented and insecure ecosystem... To address this gap, this protocol proposes an open, interoperable protocol for agent payments. **This protocol, designed as an extension for emerging agent-to-agent (A2A), model-context protocols (MCP), and Universal Commerce Protocol (UCP), establishes a secure and reliable framework for AI-driven commerce.**

## Section 2: Guiding Principles for a Trusted Agent Economy

### 2.1 Openness and Interoperability

This protocol is proposed as a non-proprietary, open extension for existing and future agent-to-agent (A2A), model-context protocol (MCP), and Universal Commerce Protocol (UCP). The goal is to provide a common, interoperable payments layer that can be adopted by any ecosystem player.

### 2.2 User Control and Privacy by Design

The user must always be the ultimate authority... Through Selective Disclosure, agents involved in the shopping process are prevented from accessing sensitive payment card industry (PCI) data which is handled exclusively by the specialized entities and the secure elements of the payment infrastructure.

### 2.3 Verifiable Intent, Not Inferred Action

Trust in an AI Agent system cannot be based only on interpreting the ambiguous, probabilistic outputs of a large language model. Transactions must be anchored to deterministic, non-repudiable proof of intent from all parties.

### 2.4 Clear Transaction Accountability

A primary objective of this protocol is to provide supporting evidence that helps payment networks establish accountability and liability principles.

## Section 3: Architectural Overview

The agent payments ecosystem consists of the following key roles: **Shopping Agent (SA)** — performs product discovery, builds checkout, executes purchase. **Credential Provider (CP)** — source of Payment Credentials, verifies agent authorization, scopes the credential. **Merchant (M)** — source of the Checkout, owns the catalog, fulfills orders. **Merchant Payment Processor (MPP)** — processes payments, verifies the Payment Credential has been authorized for this Checkout. **Trusted Surface (TS)** — a UI surface trusted to get informed user consent before creating a user-signed Mandate. **Network and Issuer** — provider of the payment network and issuer of payment credentials."

### docs/ap2/specification.md — Agentic Payment Protocol (v0.2), sections 1-2

"# Agentic Payment Protocol (v0.2)

The Agentic Payment Protocol (AP2) provides a protocol to secure Agent-performed payment transactions. It makes use of the Agent Authorization model.

**AP2 operates as a security feature within a Commerce Protocol. The exact details of the Commerce Protocol (e.g., catalog APIs, checkout updates, and specific APIs for communication between the different roles) are outside the scope of AP2. AP2 is designed explicitly to be compatible with the Universal Commerce Protocol (UCP) and integrates seamlessly.**

## Roles

AP2 considers five roles: Shopping Agent (SA); Credential Provider (CP); Merchant (M) — 'responsible for providing and completing the Checkout... responsible for the integrity of the inventory, pricing, and any merchant discounts'; Merchant Payment Processor (MPP); Trusted Surface (TS).

> Note: While AP2 defines five roles, it is possible for a single entity to play multiple (or even all) of the roles.

Roles MAY always delegate their responsibilities to another party.

## Agentic vs Non-Agentic

A role is Agentic when communication to or from the Role is handled by a non-deterministic LLM. A role is Non-Agentic if communication is handled using deterministic code that verifies authenticity and correctness, and no processing is delegated to an LLM.

MAY be agentic or non-agentic: Merchant; Merchant Payment Processor; Credential Provider. MUST be non-agentic: Trusted Surface."

### cloud.google.com — "Powering AI commerce with the new Agent Payments Protocol (AP2)" (2025-09-17, extracted full text)

Byline: Stavan Parikh (VP/GM, Payments, Google) and Rao Surapaneni (VP/GM, Business Applications Platform, Google Cloud).

"Google announced the Agent Payments Protocol (AP2), an open protocol developed with leading payments and technology companies to securely initiate and transact agent-led payments across platforms. The protocol extends the Agent2Agent (A2A) protocol and Model Context Protocol (MCP), establishing a payment-agnostic framework for users, merchants, and payments providers to transact with confidence across all payment methods."

**Partner organizations named (60+ listed, verbatim order as extracted):** Adyen, American Express, Ant International, Coinbase, Etsy, Forter, Intuit, JCB, Mastercard, Mysten Labs, Paypal, Revolut, Salesforce, ServiceNow, UnionPay International, Worldpay, Accenture, Adobe, Airwallex, BHN, BVNK, Checkout.com, Confluent, Crossmint, Dell, Deloitte, DLocal, Ebanx, Eigen Labs, Fiuu, Gr4vy, Gravitee, Global Fashion Group, JusPay, KCP, Lightspark, ManusAI, Mesh, Nexi, Okta, Payoneer, PwC, Shopee, 1Password.

Governance/access, as stated on the page: "Open Protocol" — described as open and collaborative; complete technical specification, documentation, and reference implementations available in the public GitHub repository (`goo.gle/ap2`); commitment to evolving the protocol through standards bodies; an A2A x402 extension for cryptocurrency/stablecoin payments developed with Coinbase, Ethereum Foundation, MetaMask and others. No explicit licence, fee, or settlement language on this announcement page (licence is stated in the repo itself — Apache 2.0, see above).

### blog.google — "We're donating Agent Payments Protocol to the FIDO Alliance to support the future of secure, agentic payments" (2026-04-28, full page text)

Byline: Stavan Parikh, VP/GM, Payments.

"For agentic technology to scale, it needs to work for everyone. That's why over the last few months, we've shared new open commerce and payments standards to serve as the building blocks for the future of AI shopping. Now, to help further scale this technology and promote industry-wide innovation, **we're donating the Agent Payments Protocol (AP2) to the FIDO Alliance**, a renowned industry association focused on creating open standards. **Transitioning ownership to the FIDO Alliance ensures AP2 remains platform-agnostic and community-led, while accelerating adoption of secure agentic payments.**

Today on GitHub, we're also releasing AP2 v.0.2, which introduces critical updates for autonomous transactions, including "Human Not Present" payments, which will allow agents to securely execute payments autonomously — like securing and purchasing limited-run tickets the moment they're on sale — based on pre-authorized user instructions.

AP2 is also helping to drive industry standards like **Verifiable Intent**, a new, AP2-compatible standard co-developed with Mastercard and also being donated to FIDO, that creates a tamper-proof log of user-authorized agent actions to ensure accountability.

With growing support from leaders across the industry, AP2 establishes the open, collaborative foundation for agents to transact safely across any platform."

## Pull notes — mechanical only

- Repo files fetched via `curl` against `raw.githubusercontent.com` and `api.github.com` — plain fetch works for the whole `google-agentic-commerce/AP2` repo.
- `cloud.google.com` blog post was extracted via `WebFetch` (converts to markdown, ran cleanly). `blog.google` required the Chrome extension (`claude-in-chrome`, `get_page_text`) — a new tab was opened for this session (tab id not reused from other agents' open tabs in the shared browser group; closed after use), navigated directly to the URL, and the `<article>` element's text extracted; a plain `WebFetch` of `blog.google` on this same URL was not attempted a second time after the browser extraction succeeded.
- **Governance finding, the most load-bearing fact in this file:** AP2's own `CONTRIBUTING.md`, fetched live from the `main` branch on 2026-09-22, states the specification was donated to FIDO Alliance and that the GitHub repo going forward covers only "samples and sdk," not the specification itself. This is dated 2026-04-28 per the companion blog post — i.e., **Google no longer controls the AP2 specification's governance as of this pull date; the FIDO Alliance does.** No FIDO Alliance page was fetched in this pull (out of `channels.md`'s owners'-own-domain scope for this cluster, since FIDO Alliance is not one of the named engines/rails/platforms in the task — recorded as `unknown — checked github.com/google-agentic-commerce/AP2, cloud.google.com, blog.google 2026-09-22` for what FIDO's own governance process now looks like).
- `docs/ap2/specification.md` is 401 lines; only sections 1 ("Roles") and 2 ("Agentic vs Non-Agentic") are reproduced verbatim above. The remainder of the file (not reproduced) covers Section 3 verification responsibilities per role, and points to the linked `checkout_mandate.md`, `payment_mandate.md`, `flows.md`, `agent_authorization.md`, and `security_and_privacy_considerations.md` files in the same `docs/ap2/` directory — none of those five linked files were fetched in this pull; their existence is recorded from the repo tree listing (`docs/ap2/agent_authorization.md`, `docs/ap2/checkout_mandate.md`, `docs/ap2/flows.md`, `docs/ap2/implementation_considerations.md`, `docs/ap2/payment_mandate.md`, `docs/ap2/security_and_privacy_considerations.md` — file sizes not captured, GitHub Trees API returned paths only for this subdirectory in the query used).
- No fee, commission, or settlement-cut clause found anywhere in the AP2 repo docs read (README, overview.md, specification.md sections 1-2, CONTRIBUTING.md) or on either Google blog post. AP2 is a security/authorization-mandate layer over an underlying commerce protocol (explicitly "outside the scope of AP2" per specification.md); no page names a fee. Recorded `unknown — checked github.com/google-agentic-commerce/AP2, cloud.google.com/blog, blog.google 2026-09-22`.
- Partner list above is reproduced exactly as extracted by `WebFetch` from the live `cloud.google.com` page; not independently re-verified against a second capture of the same page (no discrepancy expected since this is a static historical blog post, but not re-fetched a second time in this session).
