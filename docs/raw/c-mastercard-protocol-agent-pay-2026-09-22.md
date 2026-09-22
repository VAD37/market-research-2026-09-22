# Mastercard — Agent Pay (mastercard.com and developer.mastercard.com)

```yaml
source:          Mastercard (mastercard.com; developer.mastercard.com)
url_or_doc_id:   https://www.mastercard.com/us/en/business/artificial-intelligence/mastercard-agent-pay.html ; https://developer.mastercard.com/mastercard-checkout-solutions/documentation/use-cases/agent-pay/
published:       undated — no revision date on either page
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — Mastercard's own marketing and developer-documentation pages)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          n/a — payments rail (card network), not an assistant engine; page names Stripe, Google, Ant International's Antom as collaboration partners (per search-result snippet of a Mastercard press page, not independently pulled — see Pull notes)
metric_kind:     none
supersedes:      none
captured:        marketing page (mastercard.com) full text; developer documentation page (developer.mastercard.com) full text
```

## Verbatim

### mastercard.com/us/en/business/artificial-intelligence/mastercard-agent-pay.html (full)

"MASTERCARD AGENT PAY

Powering the next frontier of commerce

Bringing smarter, more secure and more personal payments experiences to every agentic transaction.

## Introducing Mastercard Agent Pay

Mastercard's new infrastructure for enabling secure, scalable and trusted payments in agentic commerce.

**Trust** — We're reimagining trust for the agentic era — anchored in Mastercard's industry-leading standards.
**Security** — Creating a world where agent-led payments are secure, seamless and future-ready.
**Visibility** — Enabling insight, personalization and confidence in every transaction.

## A new level of trusted AI-powered commerce

**Built for trust, engineered for scale** — Works seamlessly across existing payment networks — no friction, just instant global scalability.
**Designed for what's next** — Together with industry leaders, we're creating scalable solutions, unlocking the power of AI.
**Made for you and your customers** — Supports both consumer and business use cases.

## Setting the standard for agentic payments

**Know your agent** — Only registered agents can transact — governed and traceable with Mastercard network tokens — setting new standards for trust and accountability.
**Interface standards** — We're building the future of agentic commerce with a universal data exchange protocol enabling seamless, scalable personalization.
**Verifiable intent** — Purpose-built for agentic commerce, ensuring every transaction is verified by authenticated user intent and explicit consent before an action is taken.
**Agent Pay for Machines** — Enables trusted devices and AI-powered agents to securely initiate, authenticate, and complete payments on behalf of users and businesses."

Cited statistics (footnoted, all third-party, not Mastercard-measured): 800M active OpenAI users (PYMNTS, Apr 2025); "Agentic AI is expected to handle up to 20% of e-commerce tasks in 2025" (PYMNTS, Dec 2024); "39% of U.S. consumers have used generative AI for online shopping, and 53% plan to do so in 2025" (Adobe Blog, Mar 2025).

No technical specification, schema, API reference, licence text, or fee/commission language appears anywhere on this marketing page.

### developer.mastercard.com/mastercard-checkout-solutions/documentation/use-cases/agent-pay/ (full)

"Mastercard Agent Pay

As the digital economy evolves, a new frontier is emerging through agentic commerce, where AI agents can assist consumers with the buying process (agent-assisted commerce) as well as autonomously find and buy products, guided by the consumer's intent (autonomous agentic commerce)...

## Overview

Mastercard Agent Pay is a **Remote Commerce Tokenization Program** designed to support the emerging landscape of Agentic Commerce. It enables AI Agents to securely initiate and complete transactions using Mastercard's advanced technologies, including: Network tokenization via Mastercard Digital Enablement Service (MDES); Strong authentication through Mastercard Payment Passkeys; Fraud and cybersecurity solutions tailored for agent-mediated environments; Mastercard Agent Pay Acceptance Framework supporting Merchants in agentic commerce.

## Participants and Interactions

| Role | Description |
| --- | --- |
| Consumer | The end user who interacts with the Integrator to initiate and complete transactions. Also authorizes the use of their card. |
| Agentic Commerce Provider | AI Agents are systems that include many functions... responsible for the components that serve commerce functions. |
| Agentic Commerce Enabler | Agentic Commerce Providers may choose to work with third parties who manage the technical integration to network services... When a Mastercard Agent Pay implementation uses an Agentic Commerce Enabler, **both the Enabler and Provider(s) must be registered in the appropriate roles.** |
| Mastercard | Enables and governs the Mastercard Agent Pay program, serving as the platform through which integrations and transactions are facilitated. |
| Merchant | Sells goods/services. Accepts transaction payloads and submits purchase authorization requests. |
| Issuer | The financial institution that issues the payment credentials and authorizes transactions. |

## Workflow

| Step | Description |
| --- | --- |
| Credential Enrollment | Enroll tokenize credentials |
| Identity and Verification (ID&V) | Verify the cardholder's identity |
| Bind | Set up authentication methods and bind the authenticator to a credential |
| Intent Creation | Capture consumer purchase intent |
| Authentication | Authenticate consumer intent |
| Checkout | Perform checkout and receive tokenized payload |

## Good to know

**Integrator Registration:** All integrators must be registered with Mastercard, with roles determined by the services provided. Most Agentic Commerce Providers and Enablers register as Token Requestors. Mastercard representatives can guide the registration process.

**Agentic Tokens and Identifiers:** Integrators must use Agentic Tokens for enhanced security and transaction quality, supporting: Digital Secure Remote Payment (DSRP) — maximum security for merchants accepting enhanced token data; Dynamic Token Verification Code (DTVC) — compatibility for merchants not yet supporting DSRP. Agentic Commerce Identifiers: Digital Service Provider ID and Digital Commerce Solution Indicators help issuers and acquirers identify agentic transactions."

## Pull notes — mechanical only

- Both pages accessed via the Chrome extension, `get_page_text`, in the same tab used for Visa (navigated in sequence, tab created fresh for this session and closed after use).
- Unlike Visa's Trusted Agent Protocol and Google's UCP, **no machine-readable schema, API reference, field-level payload definition, or downloadable specification document was found for Mastercard Agent Pay** on either page pulled, nor via a follow-up web search for `developer.mastercard.com` technical documentation. What exists publicly is a conceptual role/workflow description (quoted above in full) plus a marketing landing page — not implementation-level detail (no request/response schema, no signature construction steps, no error codes). This is a direct, load-bearing finding for H8: **a merchant cannot implement Mastercard Agent Pay from the public text alone** — the page itself states "All integrators must be registered with Mastercard... Mastercard representatives can guide the registration process," naming registration-with-Mastercard, not a published spec, as the path to implementation.
- Mastercard's own AI/developer hub (`developer.mastercard.com/ai/`) was also checked; it documents a generic "Mastercard Developers Agent Toolkit" (an MCP server for discovering Mastercard's API catalog) — a developer-productivity tool, not the Agent Pay protocol itself. Not reproduced here as out of scope for this file's target.
- A `developer.mastercard.com` search for "agent pay" surfaced Mastercard Track "Buyer Payment Agent" and "Supplier Payment Agent" product documentation pages (B2B payables automation, a different, pre-existing Mastercard Track product line) — checked via search-result titles only, not fetched, and not treated as part of the Agent Pay consumer-agentic-commerce program described above; recorded as a naming-collision caveat, not as additional Agent Pay documentation.
- No fee, commission, or settlement-cut figure found on either page. Recorded `unknown — checked mastercard.com/us/en/business/artificial-intelligence/mastercard-agent-pay.html, developer.mastercard.com/mastercard-checkout-solutions/documentation/use-cases/agent-pay/, developer.mastercard.com/ai/ 2026-09-22`.
- Partner names (Stripe, Google, Ant International's Antom) and geographic-rollout claims (Australia, Latin America and the Caribbean, Asia-Pacific expansion) surfaced only in web-search-result snippets of other Mastercard newsroom pages (`mastercard.com/news/...`), not independently fetched as a raw pull in this file — recorded as search-snippet-only, not verbatim-captured, per this cluster's channel scope (own-domain pulls, not trade-press pointers).
