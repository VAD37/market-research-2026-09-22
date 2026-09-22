# Amazon Ads — Agentic shopping is here. What does that mean for advertisers?

```yaml
source:          Amazon Ads (advertising.amazon.com)
url_or_doc_id:   https://advertising.amazon.com/library/news/agentic-shopping-advertising
published:       2026-06-11
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, own news article)
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Amazon shopping assistant — page names it "Alexa for Shopping" (merge of "Rufus" and "Alexa+")
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

NEWS

Agentic shopping is here. What does that mean for advertisers?

June 11, 2026

Last month, Amazon brought together two powerful AI experiences—Rufus, our expert shopping assistant used by over 300 million customers in 2025, and Alexa+, our personalized AI assistant available across hundreds of millions of devices—into a single, unified experience: Alexa for Shopping.

Customers can now use Alexa for Shopping to ask questions directly in the main Amazon search bar, create personalized shopping guides for big purchases, get category and product insights in search results and on product pages, generate dynamic product comparisons, view up to a full year of price history, and automate deal-finding, cart-building, and routine purchases based on personalized insights.

The combination of deep product expertise and seamless personalization makes Alexa for Shopping the best AI assistant for shopping on Amazon and other stores from across the web.

Across Amazon, advertising helps shoppers more easily discover new products and brands that best serve their needs. As we continue to innovate with AI assistants, there will be many opportunities for advertising to aid the shopper's experience. Today, advertisers can be part of the conversation through sponsored ads and Sponsored Products and Sponsored Brands prompts on Alexa for Shopping. On Alexa+, where customers can complete everyday tasks across shopping, entertainment, and local services right from their home, we have introduced Alexa+ Conversational Ads and Prime Video Sponsored Tiles.

The advertiser benefits of our agentic and conversational experiences are wide-ranging:

Conversational ads that work: On Amazon, customers already engage with ads conversationally—asking questions, comparing products, and completing purchases within the same conversation. It's not a future state; it's a current state.
Trillions of signals across shopping, browsing, and purchasing lead to the most relevant and useful ads: Conversational ads are uniquely positioned to understand customer intent because they can respond to what shoppers are actively asking for in the moment. Driven by our first-party signals, Amazon Ads offers the ability for advertisers to engage shoppers with highly relevant recommendations and products that align with their needs, preferences, and shopping goals—making discovery feel more natural and useful.
Intent-rich conversations, not passive scrolling: When a customer tells Alexa they need the best lamp for their kid's room, that's a fundamentally engaging advertising moment. The customer has expressed intent, context, and preference in natural language.
Commerce completion built in: Unlike advertising on surfaces that end at a click-through to a website, Alexa can complete the transaction. This closes the distance from ad impression to purchase and helps customers quickly and easily get what they want.
Closed-loop measurement: Amazon has spent years developing the most comprehensive measurement solutions to help advertisers understand the impact of their investments. Advertisers benefit from these today for our agentic offerings as they do for all our solutions. It's closed-loop measurement that tracks impressions all the way to conversions.
Task completion by design: Alexa was designed as a virtual assistant that completes tasks for customers—from turning on lights and locking doors, to booking meal reservations. The ad experience helps customers accomplish something: find the right product, compare options, make a purchase. That's not just a principle we state; it's how the product is built.
A privacy foundation built on a track record: Amazon's approach to agentic advertising is grounded in over a decade of building ad technology and Alexa experiences with customer trust as a product feature.

Conversational ad types available within Alexa for Shopping

Sponsored ads in Alexa for Shopping surface relevant products and brands within natural conversation, giving advertisers visibility at the moment of decision. Existing sponsored ads campaigns are automatically eligible to serve in Alexa for Shopping, helping advertisers seamlessly reach engaged audiences during relevant conversations with Alexa for Shopping, without additional campaign setup.

Sponsored Products and Sponsored Brands prompts are AI-powered conversational ads that appear in shopping results and product pages, opening product-related conversations with Alexa for Shopping. They act as a virtual product expert—engaging shoppers with relevant product or brand information to help decision-making. Nearly 20% of shoppers who interact with a prompt continue the conversation about that brand, and adding prompts to a Sponsored Brands ad drives a 6% increase in conversions. Existing sponsored ads campaigns are automatically eligible to be optimized as a prompt.

Prompts can appear on an Amazon product detail page. When clicked, they open a conversation with Alexa for Shopping.

Conversational ad types available with Alexa+ and Alexa-enabled devices

Alexa+ Conversational Ads were the industry's first conversational ad experience. They introduce brand messaging into personalized, natural dialogue on Alexa-enabled devices. These ads surface when relevant to a customer's conversation and intent, available in audio, static. Advertisers with sponsored ads campaigns are automatically enrolled.

In response to the query "show me mirrorless cameras," a sponsored product appears in the results. Customers can ask Alexa+ for more information about any displayed product or tell Alexa to "add it to my cart."

Prime Video Sponsored Tiles are conversational entertainment ads on eligible Echo Show devices, integrating sponsored film and TV content into entertainment-related voice queries. Customers can subscribe to channels or buy and rent titles directly through voice or touch.

Prime Video Sponsored Tiles appear in response to a customer asking Alexa+ for movie & TV show recommendations.

Agentic experiences throughout our advertising offering

Not only do we offer conversational and agentic ad formats, but we also make it easier to create, launch, and optimize full-funnel campaigns using Amazon Ads AI-powered tools—from Creative Agent that produces professional ads in hours, to Ads Agent that turns weeks of campaign setup and targeting into minutes, to Amazon MCP server that connects external AI agents to Amazon Ads API via simple prompts with no custom coding required—lowering the barrier for advertisers to build agentic workflows that benefit from Amazon's full campaign and measurement capabilities.

All these agentic and conversational experiences are available today, and we will continue to innovate—across these and our wider offering—to drive impactful results and the best outcomes for brands.

## Pull notes — mechanical only

- Chrome extension `get_page_text` returned full article on first load.
- **Rename/merge stated in Amazon's own words**: "Last month, Amazon brought together two powerful AI experiences—Rufus... and Alexa+... into a single, unified experience: Alexa for Shopping." Published 2026-06-11, "last month" implies the merge occurred ~May 2026 — consistent with the 2026-05-13 date found via search and captured in `a-amazon-alexa-for-shopping-rename-2026-09-22.md`.
- **Three distinct named ad-format families identified on this page, kept separate, not merged**:
  1. "Sponsored ads" (generic Sponsored Products/Sponsored Brands) — surface in Alexa for Shopping conversationally, auto-eligible, no separate setup.
  2. "Sponsored Products prompts" / "Sponsored Brands prompts" — appear on shopping results/product pages, open a Rufus/Alexa-for-Shopping dialog when clicked (billing basis per `b-amazon-sponsored-prompts-ga-2026-09-22.md`: CPC).
  3. "Alexa+ Conversational Ads" — audio/static ad format inside Alexa+ voice/device conversations, described as "the industry's first conversational ad experience," auto-enrolled for advertisers with sponsored ads campaigns.
  4. "Prime Video Sponsored Tiles" — conversational entertainment ad format on Echo Show devices, surfaced in response to movie/TV recommendation queries to Alexa+.
- Performance figures: "Nearly 20% of shoppers who interact with a prompt continue the conversation about that brand" and "adding prompts to a Sponsored Brands ad drives a 6% increase in conversions" — both stated with no n, date window, or method disclosed on this page (company-stated, unqualified).
- No CPC/CPM figure, no billing-model name for Alexa+ Conversational Ads or Prime Video Sponsored Tiles disclosed on this page (only "Sponsored Products prompts"/"Sponsored Brands prompts" billing is documented, in the companion pull).
- "Rufus, our expert shopping assistant used by over 300 million customers in 2025" — a usage figure distinct from and higher than the "250 million" figure found elsewhere (`a-amazon-rufus-announcement-2026-09-22.md`, `a-amazon-alexa-for-shopping-rename-2026-09-22.md`); kept side by side, not reconciled, per root `CLAUDE.md`.
