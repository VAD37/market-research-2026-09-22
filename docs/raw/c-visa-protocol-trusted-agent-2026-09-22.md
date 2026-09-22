# Visa — Trusted Agent Protocol (developer.visa.com)

```yaml
source:          Visa (developer.visa.com)
url_or_doc_id:   https://developer.visa.com/capabilities/trusted-agent-protocol/overview ; /docs-getting-started ; /trusted-agent-protocol-specifications
published:       undated — no revision date on any of the three pages; product marked "in the process of development and deployment" on the overview page
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text and javascript_tool innerText extraction; the specifications page renders through a JS docs framework not captured by get_page_text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — Visa's own developer documentation)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          n/a — payments rail (card network), not an assistant engine; page names Cloudflare, Akamai as ecosystem partners and Adyen, Ant International, Checkout.com, Coinbase, CyberSource, Nuvei, Shopify, Stripe, Worldpay as early feedback partners (per Visa press release, not re-pulled here — see Pull notes)
metric_kind:     none
supersedes:      none
captured:        overview page full text; getting-started page full text; specifications page — table of contents/section headers plus the Introduction paragraph and the gating statement, not the full ~42,000-character technical body (signature construction, ID token claims)
```

## Verbatim

### developer.visa.com/capabilities/trusted-agent-protocol/overview (full)

"Trusted Agent Protocol

Enhancing Visa Intelligent Commerce to improve merchant visibility.

**Available for use by:** Merchants, Independent Developers. **Regional availability:** N. America, Asia-Pacific, Europe, CEMEA, LAC.

Visa is introducing enhancements to Visa Intelligent Commerce to improve transparency, safety, and merchant visibility in agentic commerce transactions.

As AI agents help customers browse merchant sites, discover products, compare prices, and make selections, the commerce journey begins long before checkout. Agents play a key role in shaping the shopping experience from the very first interaction. Historically, merchants and their proxies (CDNs and bot mitigation services, etc.) have classified automated web traffic as bots and have typically blocked such traffic. As agent usage grows, merchants will need tools and controls to distinguish trusted, commerce-focused agents from malicious bots. Recognizing trusted agents allows merchants to engage with the same customers coming through a different medium to streamline and enhance these agent interactions.

New specifications include details related to signatures that are specific to the merchant and purpose, and are time bound, cannot be replayed or relayed.

*This product is in the process of development and deployment. Depictions are representations of potential features and sequences. May not be available in all markets.*

**Verifiable Information — Agent Intent:** An indication that the agent is a Visa trusted agent with an intent to retrieve additional details about, or purchase, a specific product or service from the merchant.

**Consumer Recognition:** Agents can pass multiple consumer related data elements — Customer with Merchant Account (via verifiable token ID or loyalty account); Prior Interactions (device identifiers); Location Parameters (country/postal code); Wallet Address (for crypto).

**Payment Information:** Merchants may support different payment methods for agentic commerce. — **Key Entry:** pass a hashed Visa Intelligent Commerce payment credential, allowing merchants to validate authenticity; agents can pass card metadata for accurate card art/descriptions. **API or Protocol based:** for merchants using APIs/protocols, pass all required payment information (token, shipping/billing address). **IOUs:** information needed to manage balances and settlements between agents and merchants, 'bringing merchants supplemental content revenue beyond traditional models like ads and upsells.'

Details on how agents generate these signatures are available in the Visa Intelligent Commerce Client Implementation Guide **for onboarded agents**. Visa's Trusted Agent Protocol outlines merchant processes like key retrieval, signature verification, and best practices for merchants handling agent messages containing these signatures and acting on their contents.

**By accessing these materials, you are agreeing to the terms and conditions outlined in the Product Terms.**

Trusted Agent Protocol — Materials detailing Visa's Trusted Agent Protocol. Merchants may read this material for more details on how to implement the Trusted Agent Protocol in adherence with Visa's policies. By accessing, downloading, or using this material, you agree to the terms and conditions outlined in the Trusted Agent Protocol Product Terms. [Learn More]

Sample Code Implementation of Trusted Agent Protocol — A sample implementation of Visa's Trusted Agent Protocol to give both merchants and agents guidance on how to conduct signature-based authentication in agentic commerce. By using, downloading, viewing, or installing this code from the GitHub repository, you agree to the terms and conditions outlined in the Trusted Agent Protocol Product Terms. [GitHub Repository]"

### developer.visa.com/capabilities/trusted-agent-protocol/docs-getting-started (full)

"Getting Started with Visa's Trusted Agent Protocol

Welcome to the developer platform for the Trusted Agent Protocol! This content is provided for merchants and infrastructure providers who want to securely recognize and transact with **Visa-approved AI agents**. As agentic traffic and commerce become more prevalent, Visa's Trusted Agent Protocol provides a verifiable, cryptographic standard to help merchants differentiate legitimate agents from nefarious bots or web crawlers.

Two key resources: **The Trusted Agent Protocol** — 'the official rulebook that details the technical processes for recognizing a Visa-approved agent, including the cryptographic standards (RFC9421), required message signature fields, and the process for validating an agent's intent.' **Sample Code Implementation** — practical code examples demonstrating the use of public keys and how to construct `signature_base` strings.

The core of the protocol is simple: a trusted agent will include a message signature in its request to your server. A merchant's primary task is to validate this signature. To do this, a merchant system will need to reconstruct the `signature_base` string using attributes from the request and then use the agent's public key to verify the signature."

### developer.visa.com/capabilities/trusted-agent-protocol/trusted-agent-protocol-specifications (table of contents and Introduction paragraph)

Table of contents, as rendered in the page's sidebar: Introduction; Trust Model; Agent Recognition Signature; Example Agent Verification for Payments; Signature Verification; Consumer Recognition; Contextual Data (`contextualData`); Payment (Verification Steps; Card Metadata `cardMetadata`; Payment Credential Hash `credentialHash`; Payment Object `payload`; Browsing IOU `browsingIOU`); Additional Information; Public Keys Retrieval Service (Public Key Retrieval; Public Key Retrieval Definition); ID Token (Token Header; Token Claims; Public Claims; Standard ID Token Claims; Private Claims); Sample Code to Create Signature Base.

Opening statement: "By accessing, downloading, or using this specification, you agree to the terms and conditions outlined in the Visa Trusted Agent Protocol Product Terms."

Introduction (partial, extracted in two passes): "This material outlines the next phase of Agentic Commerce – focusing on how Merchants can recognize when an [agent is a Visa Trusted Agent]... [while] Agents could have bi-lateral agreements with Merchants and interact through authenticated, secure interfaces, this protocol is applicable to the scenario when the Agent is initially unknown to the Merchant. That is, this protocol is intended for those scenarios [where the Agent is initially unknown] and includes an Agent interacting with a Merchant website or message protocols exposed by a Merchant — and an agent is directed by the user with an intent for commerce.

As agentic commerce becomes more prevalent, we believe this recognition will become necessary, as Merchants (or their Site Protection Providers) will/could confuse these Agent interactions with bots (web crawlers, etc.) or nefarious actors that could be attempting to degrade the Merchant services, be a product reseller of limited-edition releases, or be trying to actively attack the Merchant property. Additionally, it is envisaged that Merchants should have a mechanism to request payment for access to certain informat[ion]..."

## Pull notes — mechanical only

- Accessed via the Chrome extension (`claude-in-chrome`), a fresh tab created for this session (not reused from another agent's open tabs in the shared browser group) and closed after use.
- The overview and getting-started pages loaded cleanly to `get_page_text`. The specifications page did not — `get_page_text` returned "No text content found. Page may contain only images, videos, or canvas-based content." despite `document.body.innerText.length` reporting 42,272 characters live in the DOM; text was recovered instead via `javascript_tool` reading `document.body.innerText` in slices. One slice attempt (roughly chars 6000-14000) was blocked by the extension's own output filter with the message `[BLOCKED: Cookie/query string data]` — plausibly a false-positive trigger on token/signature-related technical vocabulary in the spec body (this is a signature/ID-token specification, so terms resembling session or auth tokens appear throughout); a second slice at a different offset succeeded and is quoted above. The full ~42,000-character body (covering `contextualData`, `cardMetadata`, `credentialHash`, the `payload` object, `browsingIOU`, the Public Keys Retrieval Service, and full ID Token claim definitions) was not fully recovered verbatim in this pull; the table of contents above stands as the record of its scope, per the task's "record the file list... rather than the whole [document]" instruction for long specs.
- **Access/gating finding:** no login wall was hit on any of the three pages — the full specification text (to the extent extracted) loaded without authentication. The gate is contractual, not technical: every page states "by accessing... you are agreeing to the terms and conditions outlined in the [Trusted Agent] Product Terms" (a click-through/browse-wrap licence, not fetched in this pull — its own URL was not located on these three pages). Separately, the deeper "Visa Intelligent Commerce Client Implementation Guide" (which documents how agents themselves generate the signatures) is stated to be available "for onboarded agents" only — a second, narrower gate on top of the publicly-readable merchant-facing specification.
- No fee, commission, or settlement-cut clause found in the text captured. The protocol frames "IOUs" as a mechanism for "managing balances and settlements between agents and merchants," including a claim that this could bring merchants "supplemental content revenue beyond traditional models like ads and upsells" — but no percentage or flat fee is stated on any of the three pages read. Recorded `unknown — checked developer.visa.com/capabilities/trusted-agent-protocol/{overview,docs-getting-started,trusted-agent-protocol-specifications} 2026-09-22`.
- Visa's own newsroom press releases (`usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html` and later releases naming early-feedback partners Adyen, Ant International, Checkout.com, Coinbase, CyberSource, Nuvei, Shopify, Stripe, Worldpay, and a later Akamai integration announcement) were found via web search but **not fetched as a raw pull in this file** — found via search snippets only. Recorded here as `unknown — checked developer.visa.com only 2026-09-22; usa.visa.com press releases seen only via search-result snippet, not independently pulled`.
- The Trusted Agent Protocol sample-code GitHub repository (linked from the overview page) was not located/fetched in this pull.
