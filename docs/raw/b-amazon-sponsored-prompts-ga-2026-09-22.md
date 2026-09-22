# Amazon Ads — Sponsored Products prompts and Sponsored Brands prompts (GA launch announcement)

```yaml
source:          Amazon Ads (advertising.amazon.com)
url_or_doc_id:   https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts
published:       2026-03-10
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, own launch announcement)
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Amazon shopping assistant — page names it "Rufus"
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

LAUNCH ANNOUNCEMENT

Sponsored Products prompts and Sponsored Brands prompts

March 10, 2026

SPONSORED PRODUCTS PROMPTS AND SPONSORED BRANDS PROMPTS AND REPORTING ARE NOW GENERALLY AVAILABLE

We're excited to announce that Sponsored Products prompts and Sponsored Brands prompts are officially moving from open beta to general availability in the U.S. on March 25, 2026.

What launched?

We're introducing Sponsored Products prompts and Sponsored Brands prompts, a new AI-powered enhancement to your existing campaigns that automatically engages shoppers with relevant product information. Prompts can appear in shopping results and product detail pages on Amazon. When clicked, prompts may open a dialog in Rufus or respond to the customer directly on the page where the prompt appeared. Prompts leverage Amazon's first-party signals from your detail pages, Brand Store, campaign data, and more to surface your product expertise at key decision moments.

Meet your 24/7 virtual product expert. Using Amazon's first-party insights, prompts engage shoppers with relevant, contextual information when and where they're ready to buy—no extra work required.

Why is it important?

Shoppers often have specific questions that aren't immediately answered by a product detail page alone. Sponsored Products prompts and Sponsored Brands prompts address this by functioning as a 24/7 virtual product expert—automatically surfacing relevant details before shoppers even need to ask questions, and deepening shopper confidence at key moments in their shopping journey.

Advertiser experience:

Sponsored Products and Sponsored Brands campaigns will be automatically enrolled in prompts and leverage existing campaign parameters (e.g., campaign targeting) without any additional setup required. Sellers and vendors can review and manage prompts directly in the Ads Console or via API. Within each campaign, you can navigate to the prompts via Campaign → Ad Group → Ads → Prompts tab, where all prompts are listed if they have received a click. This view displays the prompt text, the associated ad, and key performance metrics such as impressions, clicks, and orders.

Sponsored Products prompts and Sponsored Brands prompts were introduced in November 2025 in open beta. As we move to general availability in the U.S., we will begin to charge for these ads as part of your CPC bidding and billing parameters. If you'd like to pause a prompt, you can do so at any time in Ad Console.

Where is the feature available?
North America: United States

Who can use it?
This feature is available to U.S. Amazon advertisers using Sponsored Products and Sponsored Brands campaigns (excluding authors and publishers).

Where do I access it?
Prompts are automatically enabled for existing Sponsored Products and Sponsored Brands campaigns, with performance metrics and pause controls accessible through the Ads Console and via API. Prompts reports are also available, which provide performance metrics at the individual prompt level. To access it, navigate to Reports in the Ads Console, select Create report, set the report category to Sponsored Products, and choose Prompts as the report type. Select your preferred time unit and report period, then run the report. The Prompts report includes prompt text, associated ad, impressions, clicks, click-through rate, cost per click, spend, sales, ACOS, ROAS, and 7-day orders and units.

## Pull notes — mechanical only

- Chrome extension `get_page_text` returned the full page on first load.
- **This page names the assistant "Rufus"** throughout ("prompts may open a dialog in Rufus") — published 2026-03-10, before the Rufus-to-"Alexa for Shopping" rename dated 2026-05-13 per `a-amazon-alexa-for-shopping-rename-2026-09-22.md`. Recorded as the source states it, not normalised; no evidence this specific announcement page was updated post-rename.
- **Billing basis, stated verbatim**: "we will begin to charge for these ads as part of your CPC bidding and billing parameters" — CPC, tied to the underlying Sponsored Products/Sponsored Brands campaign's own bid, not a separate rate card. Confirms GA pricing switched on as of the 2026-03-25 GA date named on this page (open beta November 2025 – March 2026 was unbilled).
- Eligibility stated precisely: "available to U.S. Amazon advertisers using Sponsored Products and Sponsored Brands campaigns (excluding authors and publishers)"; geography: "North America: United States" only.
- Format: prompt-style suggested questions/product info surfaced "in shopping results and product detail pages on Amazon" — clicking opens either a Rufus dialog or an on-page response, not always a chat-surface interaction.
- Reporting metrics named verbatim: "impressions, clicks, click-through rate, cost per click, spend, sales, ACOS, ROAS, and 7-day orders and units" — confirms CPC as the billing/reporting unit.
- No specific CPC dollar figure, rate card, or minimum bid disclosed on this page.
