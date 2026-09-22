# Microsoft Advertising — Agentic Commerce / UCP adoption statement (about.ads.microsoft.com)

```yaml
source:          Microsoft Advertising (about.ads.microsoft.com)
url_or_doc_id:   https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce
published:       undated — no revision date on page
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text, javascript_tool for FAQ accordion expansion)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — Microsoft's own advertising/merchant solutions page)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Microsoft Copilot
metric_kind:     none
supersedes:      none
captured:        page text: hero/stats section, "Improve product visibility in Copilot" section, "Enable Copilot Checkout" section, partner names, eligibility statement; two FAQ accordion answers expanded and captured (UCP definition; fee question — see Pull notes for why the fee answer was not recovered)
```

## Scope note

This is a narrow, deliberately scoped pull. Per this task's own instructions, another agent is live on Microsoft/Amazon platform-primary pulls (`docs/raw/*microsoft*`, `*amazon*`, cluster P2-c6 "Microsoft Merchant Center feed docs"), which this task must not duplicate. This file captures **only** the protocol-adoption statement on this page (that Microsoft Merchant Center will support Google's Universal Commerce Protocol, and Copilot Checkout's eligibility/gating language) — it does not cover Merchant Center feed-attribute mechanics, onboarding steps, or store-settings configuration, which are left to the P2-c6 cluster.

## Verbatim

### about.ads.microsoft.com/en/solutions/technology/agentic-commerce (excerpt — protocol-relevant sections only)

"Agentic Commerce

AI is reshaping how people discover, evaluate, and buy products. Shopping journeys are moving from clicks to conversations...

Microsoft is building human-first, merchant-friendly agentic commerce—so brands can participate directly in AI-led shopping journeys, with accurate product truth, consistent brand voice, and a frictionless path to purchase.

## Improve product visibility in Copilot

Be present, accurate, and chosen when shopping intent forms. The foundation of agentic commerce is trusted product truth. The first step is to improve product visibility in Microsoft Merchant Center (MMC) with a UCP-ready feed. **MMC will support Universal Commerce Protocol (UCP)**, enabling richer signals (returns/support policies) so AI can assess products with confidence.

## Enable Copilot Checkout

### What is Copilot Checkout?

Copilot Checkout lets shoppers complete purchases directly inside Microsoft Copilot, enabling AI-powered shopping experiences. Instead of sending customers out to a website and risking drop-off, Copilot Checkout: Keeps the entire decision-to-purchase flow in one place; Preserves the merchant as merchant of record; Uses the merchant's existing payments, fraud, tax, fulfillment, and reconciliation systems.

Merchants keep the customer relationship, the data, and full control—while gaining a new, high-intent acquisition surface.

### Trusted agentic commerce partner

PayPal, Shopify, Stripe.

**PayPal:** PayPal's Store Sync is a single integration that makes merchant products discoverable and ready to purchase across AI platforms including Microsoft Copilot... all authenticated via PayPal-issued JWT tokens and backed by Orders API v2. For merchants on other processors: through a single integration to PayPal's Cart API, merchants can sync their product catalog... and — with an open, protocol-agnostic approach — instantly reach AI shopping agents across ecosystems like Microsoft Copilot.

### Copilot Checkout eligibility requirements

**Region & language:** Only English-language merchants who sell to US buyers are eligible at this time (supporting USD).

[* footnote on the page, next to 'Copilot Checkout' in the store-settings step: 'Pilot only to select customers']"

### FAQ (accordion, expanded via script; two of eleven questions' answers recovered)

**Q: What is Universal Commerce Protocol (UCP)?**
A: "UCP is a complementary layer to Merchant Center feeds that turns product data into executable commerce actions. Feeds primarily enable discovery (products showing up in AI responses), while UCP enables transactions (checkout and post-purchase actions within AI experiences like Copilot). For additional information on UCP, see Universal Commerce Protocol - Universal Commerce Protocol (UCP)."

**Q: Does Microsoft take a commission or affiliate fee on transactions completed via Copilot Checkout?**
A: [not recovered — see Pull notes]

Other FAQ questions listed but not expanded/read in this pull (question text only, from the collapsed accordion list): "Where can I find more information on how to onboard via Microsoft Merchant Center (MMC)?"; "What information do you use to surface my product in your organic results?"; "What surfaces is Copilot Checkout live on?"; "When will you expand to other countries and languages?"; "If my business is currently a Stripe or PayPal payments customer are we automatically integrated into Copilot Checkout?"; "If one brand in an organization is onboarded, are all brands onboarded? E.g. If GAP is onboard does that mean Old Navy is also onboarded?"; "Does Copilot Checkout support multiple payment service providers (PSPs) per merchant today?"; "How is the PSP selected for a merchant?"; "Can a merchant switch PSPs after onboarding?"; "If I onboard via my PSP (PayPal or Stripe), is there any additional work required with Microsoft?"; "Is a Microsoft Merchant Center (MMC) account required?"

## Pull notes — mechanical only

- **Possible overlap, not read to check:** `docs/method/STATE.md`'s "Landed" table (read before this pull, as required) shows cluster P2-c6 ("Microsoft and Amazon platform primary") already landed and committed, producing among other files `docs/raw/b-microsoft-agentic-commerce-2026-09-22.md` — a filename strongly suggesting the same source URL as this file (`about.ads.microsoft.com/en/solutions/technology/agentic-commerce`), pulled under lane `b` (paid) rather than this file's lane `c` (agentic commerce protocol) framing. Per this task's explicit instruction, that file was **not read** to check for duplication. This file's own scope was kept deliberately narrow — the UCP-adoption statement and Copilot Checkout gating/eligibility language only, not ad-format, billing, or feed-attribute mechanics — consistent with the task's carve-out ("pull only the protocol spec page itself and leave the merchant-feed docs to that agent"). Any overlap between the two files is left for the compiling pass to reconcile; this file does not assume or deny what P2-c6's file contains.
- Accessed via the Chrome extension, `get_page_text`; FAQ answers are collapsed accordions not exposed by `get_page_text` directly, so `javascript_tool` was used to click each `[aria-expanded]` button by matching its question text, then re-read `document.body.innerText` around the matched question string. This recovered the UCP-definition answer cleanly. The fee-question button reported `aria-expanded="true"` after the click (confirmed by a follow-up query for expanded buttons), but no answer text appeared adjacent to the question in `document.body.innerText` on the next read — the click may have fired before the answer's DOM content finished rendering, or the answer renders in a way not captured by `innerText` (e.g. an iframe or a delayed async fetch). Not retried a third time in this pull; recorded as `unknown — checked about.ads.microsoft.com/en/solutions/technology/agentic-commerce 2026-09-22, FAQ question present but answer not recovered` rather than as an absence of Microsoft stating a fee.
- **No separate Microsoft-authored commerce protocol found.** This page's only protocol-relevant statement is adoption of Google's Universal Commerce Protocol ("MMC will support Universal Commerce Protocol (UCP)"), consistent with UCP's own governance file (`c-ucp-protocol-universal-commerce-2026-09-22.md`) naming Patrick Jordan of Microsoft on UCP's Shopping Tech Council. Microsoft is a UCP adopter/co-governor, not an independent protocol owner, for agentic commerce.
- **Gating language found:** "Pilot only to select customers" (footnoted against the Copilot Checkout store-setting step); "Only English-language merchants who sell to US buyers are eligible at this time." No open self-serve enrollment is described on this page; onboarding runs through Microsoft Merchant Center account setup and, per the PayPal/Shopify/Stripe partner blurbs, through those payment partners' own integrations.
- Did not fetch Microsoft Merchant Center's feed-attribute documentation, the "Get started" or "Get the playbook" linked pages, or any `learn.microsoft.com`/`ads.microsoft.com` merchant-feed configuration page — those are explicitly out of this task's scope per the task's own Microsoft/Amazon carve-out and are left to the P2-c6 cluster.
