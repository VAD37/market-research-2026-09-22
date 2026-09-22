# Microsoft Advertising — Agentic Commerce solutions page (incl. expanded FAQ)

```yaml
source:          Microsoft Advertising (about.ads.microsoft.com)
url_or_doc_id:   https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, own solutions page)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Microsoft Copilot
metric_kind:     none
supersedes:      none
captured:        full page, plus FAQ accordion panels force-expanded via page script (not visible to plain get_page_text)
```

## Verbatim

Agentic Commerce

AI is reshaping how people discover, evaluate, and buy products. Shopping journeys are moving from clicks to conversations. Enabling agentic commerce scenarios will help you become more discoverable & close sales.

This shift isn't theoretical. It's already happening:

Microsoft is building human‑first, merchant‑friendly agentic commerce—so brands can participate directly in AI‑led shopping journeys, with accurate product truth, consistent brand voice, and a frictionless path to purchase.

84% — AI‑driven revenue per visit grew year‑over‑year as shopping discovery moved into AI‑assisted experiences.1

72% — of consumers expect agentic shopping experiences from retailers in the next 12 months.2

800% — AI‑driven traffic surged year‑over‑year during peak shopping moments like Black Friday.3

Improve product visibility in Copilot

Be present, accurate, and chosen when shopping intent forms. The foundation of agentic commerce is trusted product truth. The first step is to improve product visibility in Microsoft Merchant Center (MMC) with a UCP-ready feed. MMC will support Universal Commerce Protocol (UCP), enabling richer signals (returns/support policies) so AI can assess products with confidence.

Following these steps in MMC to get started:

01 — Add new store settings in Microsoft Merchant Center: Return policy, customer support, Copilot Checkout.*

02 — Update your feed with attributes needed for UCP: These additional feed attributes include: native checkout eligibility for products, product warnings if needed, and Merchant Item ID (unique ID).

Enable Copilot Checkout

What is Copilot Checkout?

Copilot Checkout lets shoppers complete purchases directly inside Microsoft Copilot, enabling AI-powered shopping experiences.

Instead of sending customers out to a website and risking drop‑off, Copilot Checkout:

Keeps the entire decision‑to‑purchase flow in one place
Preserves the merchant as merchant of record
Uses the merchant's existing payments, fraud, tax, fulfillment, and reconciliation systems

Merchants keep the customer relationship, the data, and full control—while gaining a new, high‑intent acquisition surface.

Trusted agentic commerce partners: PayPal, Shopify, Stripe

PayPal's Store Sync is a single integration that makes merchant products discoverable and ready to purchase across AI platforms including Microsoft Copilot, connecting your store to customers wherever they shop. PayPal orchestrates the AI agent interaction and payment processing while the merchant's API handles product validation, pricing, shipping, and order fulfillment, all authenticated via PayPal-issued JWT tokens and backed by Orders API v2. Reference PayPal's developer docs to learn more.

For merchants on other processors: Through a single integration to PayPal's Cart API, merchants can sync their product catalog, connect their store for real-time cart validation and fulfillment, and — with an open, protocol-agnostic approach — instantly reach AI shopping agents across ecosystems like Microsoft Copilot. PayPal powers the entire journey from discovery to purchase, backed by 25 years of trusted commerce and payments relationships with hundreds of millions of consumers and merchants.

Copilot Checkout eligibility requirements — Region & language: Only English‑language merchants who sell to US buyers are eligible at this time (supporting USD).

Frequently asked questions — question text plus expanded answer, extracted via page script from each FAQ item's `aria-controls` panel:

Q: Where can I find more information on how to onboard via Microsoft Merchant Center (MMC)?
A: Please visit Microsoft Merchant Center Help page for step-by-step commerce onboarding guidance.

Q: What is Universal Commerce Protocol (UCP)?
A: UCP is a complementary layer to Merchant Center feeds that turns product data into executable commerce actions. Feeds primarily enable discovery (products showing up in AI responses), while UCP enables transactions (checkout and post‑purchase actions within AI experiences like Copilot). For additional information on UCP, see Universal Commerce Protocol - Universal Commerce Protocol (UCP)

Q: What information do you use to surface my product in your organic results?
A: We leverage both information found on the web and from a merchant's feed in the Microsoft Merchant Center.

Q: What surfaces is Copilot Checkout live on?
A: Copilot Checkout is available on Copilot.com and the Copilot mobile app, with plans to expand to additional surfaces soon.

Q: When will you expand to other countries and languages?
A: We are excited to expand this to other regions and other markets as soon as we are able; however, we cannot provide a timeline at this time.

Q: If my business is currently a Stripe or PayPal payments customer are we automatically integrated into Copilot Checkout?
A: No, the experience is "opt-in" presently and requires additional support from Stripe and PayPal.

Q: If one brand in an organization is onboarded, are all brands onboarded? E.g. If GAP is onboard does that mean Old Navy is also onboarded?
A: No. Onboarding is confirmed at the domain level - organizations can select which domains to include when working with their checkout partner (i.e. Stripe/PayPal)

Q: Does Copilot Checkout support multiple payment service providers (PSPs) per merchant today?
A: Today, Copilot Checkout supports a single PSP checkout partner per merchant.

Q: How is the PSP selected for a merchant?
A: By default, the PSP that comple[note: truncated by page-script extraction; remaining text of this one answer not captured]

Q: Does Microsoft take a commission or affiliate fee on transactions completed via Copilot Checkout?
A: No. Today, Microsoft does not take a commission or affiliate fee. Merchants remain the merchant of record, and payments are processed on existing rails (e.g., Shopify, Stripe, PayPal).

Q: Is a Microsoft Merchant Center (MMC) account required?
A: Yes. To onboard to Copilot Checkout, you must have an MMC account. A product feed is required to power product discovery and checkout.

[1] August 2025, Adobe Digital Insights, cited via Mi3

[2] September 2025, Rebuilding Web, Microsoft Research

[3] November 2025, "AI help drives record $11.8 billion in Black Friday online spending," Reuters

[*] Pilot only to select customers

## Pull notes — mechanical only

- `get_page_text` on first load surfaced only the FAQ question titles, not their answers (accordion panels hidden from the extraction, same failure mode `b-google-ai-overviews-ads-2026-09-22.md` and `c-google-ucp-merchant-guide-2026-09-22.md` recorded on Google pages in P2-c4). Recovered via `javascript_tool`: located each FAQ `<button>` by its question text, read its `aria-controls` target element's `innerText` directly from the DOM — this is the same underlying answer text the accordion reveals, unedited.
- One answer (PSP selection) was truncated by the tool's own output-length limit during JS extraction, not by the page; marked `[note: truncated by page-script extraction]` above rather than guessed at.
- **Key pricing/billing finding for H12**: Microsoft states plainly, in its own words, that it does **not** currently take a commission or affiliate fee on Copilot Checkout transactions — no percentage, no take-rate, because the answer is that none is charged as of this pull date.
- Feed vs. UCP distinction stated explicitly in Microsoft's own words: "Feeds primarily enable discovery... while UCP enables transactions."
- Country/eligibility: stated on this page as "Only English‑language merchants who sell to US buyers are eligible at this time (supporting USD)" — differs from the `c-microsoft-copilot-checkout-brand-agents-2026-09-22.md` blog post's broader framing ("expanding across the Copilot ecosystem") because the blog post does not itself restate a country list; both are kept side by side, not reconciled.
- Three stat footnotes (84%, 72%, 800%) are attributed to named third parties (Adobe Digital Insights via Mi3; Microsoft Research; Reuters) rather than left as bare Microsoft claims — captured verbatim with their footnote source.
