# OpenAI Help Center — Ads in ChatGPT: The Basics (format, pricing, measurement)

```yaml
source:          OpenAI Help Center
url_or_doc_id:   https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics
published:       undated — no date on page; page states "Updated: 5 days ago" relative to pull time
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, advertiser-facing wording)
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Ads in ChatGPT: The Basics

An introduction to the ChatGPT Ads experience for advertisers, including ad format, delivery, pricing, and measurement.

Updated: 5 days ago

Ads in ChatGPT help advertisers reach users as they explore, compare, and decide within a single conversational experience. By considering the context of the current conversation and, when ads personalization is enabled, select signals from a user's broader ChatGPT experience, ChatGPT Ads create opportunities to deliver relevant, helpful messages aligned with what users are trying to accomplish.

Who may see ads

We do not show ads to users on Plus, Pro, or any Business plan, or to any accounts identified as belonging to users under 18, based on account-level age information and age prediction where available.

Ad format

Ads appear below ChatGPT responses. Each ad includes:

Advertiser name

Favicon (advertiser logo)

Title (headline)

Copy (description)

Landing page

Image asset (creative)

See below for an example ad unit.

[note: example ad unit is an image, not captured]

Selection and delivery

Our ads system selects and delivers ads based on expected relevance and outcomes. It considers multiple signals, including the context and intent of the current conversation, the ad's landing page, title, copy, advertiser-provided context hints, and, when ads personalization is enabled, select signals from a user's broader ChatGPT experience.

At the ad group level, advertisers can provide context hints that describe the conversations, topics, or keywords where their products or services may be relevant. These hints help guide ad matching, but they are not exact-match keywords and do not guarantee delivery in specific conversations.

Pricing

ChatGPT Ads supports impression and valid-click billing. Choose Views for impression-based buying, Clicks to optimize for traffic, or Conversions to optimize toward a supported standard conversion event. Conversion-optimized campaigns with click billing (oCPC) charge for valid clicks, not conversions. For eligibility and other conversion-optimized billing options, see Conversion-optimized Campaigns.

Advertisers set a maximum bid at the ad-group level: a maximum CPM bid for Reach campaigns or a maximum CPC bid for Clicks campaigns. For CPC campaigns, we recommend starting with a maximum bid of $3–$5 USD per click. Ads Manager may also provide bid-strength guidance to indicate whether a bid is likely to be competitive or may limit delivery.

We use a relevance-weighted, second-price auction to select among eligible ads. Our system aims to maximize both advertiser and user value.

Tracking and measurement

Ads Manager Beta reporting currently includes impressions, clicks, spend, click-through rate (CTR), average CPC, average CPM, and conversions.

To measure conversions from ChatGPT Ads, advertisers can set up conversion measurement in Ads Manager Beta. For step-by-step guidance, visit our measurement documentation.

Advertisers can also track traffic from ChatGPT Ads by adding static tracking parameters (e.g. UTM parameters) to landing page URLs. These parameters persist on ad clicks and can be used in existing analytics tools to understand traffic from ChatGPT Ads.

Impressions, clicks, and CTR can appear within minutes. Spend reporting can take longer, so a displayed spend of zero does not necessarily mean no charges have accrued. Reporting times can vary.

Brand safety

OpenAI's policy is to place ads only near chats that are safe, appropriate, and aligned with user trust and brand safety. Our safeguards are designed to prevent ads from appearing in sensitive user contexts or brand-unsafe environments, including the contexts outlined in our Ads Policies.

## Pull notes — mechanical only

- Loaded via Chrome extension (help.openai.com flagged 403→ext per channels.md C2).
- **Price figure disclosed verbatim**: "For CPC campaigns, we recommend starting with a maximum bid of $3–$5 USD per click." This is a recommended starting maximum bid, not a fixed or floor price — auction is "relevance-weighted, second-price."
- Billing/pricing models named: CPM (Reach campaigns, impression billing), CPC (Clicks campaigns, valid-click billing), oCPC (conversion-optimized campaigns, "charge for valid clicks, not conversions").
- Confirms UTM-style tracking parameters supported on ad landing pages: "advertisers can also track traffic from ChatGPT Ads by adding static tracking parameters (e.g. UTM parameters) to landing page URLs" — relevant to citation/attribution tracking (lane A/E crossover), though this article frames it for paid, not organic, traffic.
- Links to a further page "Ads Policies" (anchor text "Ads Policies", href not resolved by get_page_text) — a target for further pull in this cluster.
- Auction mechanic disclosed: "relevance-weighted, second-price auction."
