# G2 — StackAdapt reviews/product page — admission-rule second source

```yaml
source:          G2 (g2.com) — third-party software review site, independent of StackAdapt
url_or_doc_id:   https://www.g2.com/products/stackadapt/reviews
published:       page title states "StackAdapt Reviews 2026"; no further date on page
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text) — plain fetch to g2.com returned HTTP 403 (channels.md C37/C38's documented 403→ext pattern, matching this repo's prior clusters)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     table default for a vendor/agency study drops to 5 without a stated n/date/method on the aggregate "Pricing Insights" figures; the company-description paragraph itself is analyst/review-site framing, not filed or audited
source_label:    analyst-derived
lane:            B
sub_market:      paid placement
engine:          n/a — review-site page, not an assistant engine
metric_kind:     none
supersedes:      none
captured:        full page text (main content region)
```

## Verbatim

"StackAdapt Reviews & Product Details"

"StackAdapt is the leading technology company that empowers marketers to reach, engage, and convert audiences with precision. With **465 billion automated optimizations per second**, the AI-powered StackAdapt Marketing Platform seamlessly connects brand and performance marketing to drive measurable results across the entire customer journey."

"**StackAdapt is headquartered in Toronto, Canada.** We have teams and support across North America, EMEA, APAC, and LATAM."

"Solution Type: All-in-One" / "Languages Supported: German, English, French, Spanish" / "Used by Gen3 Marketing and 2 others"

"**Value at a Glance** — Averages based on real user reviews. **Time to Implement: 1 month**"

"**Pricing Insights** — Averages based on real user reviews. **Time to Implement: 1 month. Return on Investment: 7 months. Average Discount: 6%.**"

"StackAdapt Comparisons" — The Trade Desk (4.4/5, 186 reviews), Basis (4.5/5, 287 reviews), Google Marketing Platform (4.1/5, 300 reviews).

"StackAdapt Integrations (20)" — named integrations include Adsquare, AgencyAnalytics, Data 360 (formerly Salesforce Data Cloud), Data Studio, Dun & Bradstreet Reports, Freshpaint, Google Ads, Google Analytics, Hightouch, and more (list truncated on page, "Show More Integrations").

"Categories on G2: Display Advertising, Cross-Channel Advertising, Native Advertising" (plus "Show More").

## Pull notes — mechanical only

- Loaded via the Chrome extension (`claude-in-chrome`), `get_page_text`, in a dedicated new tab; the tab was closed immediately after this pull. Plain HTTP fetch to this same URL first returned `status code 403` — consistent with `channels.md`'s documented `403→ext` pattern for g2.com.
- **Admission-rule role**: this is the second, independent-of-StackAdapt source required by this task's admission rule, alongside source 1 (`docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md`, OpenAI's own ads-partner page naming StackAdapt as a "technology partner"). G2 is a third-party review aggregator with no disclosed ownership stake in StackAdapt; this satisfies the admission rule's explicit "a review-site category page" example of an acceptable independent source.
- "6% Average Discount" and "7 months ROI" are G2's own survey-derived averages ("Averages based on real user reviews"), no n or date window stated on this page — usable as evidence of category noise / existence of a pricing-insight product, not as a hard number, per `trust-rubric.md`.
- No dollar price figure of any kind appears on this G2 page — G2's own pricing display for StackAdapt is limited to the survey-derived time/ROI/discount averages above, consistent with `b-stackadapt-pricing-2026-09-22.md`'s finding that StackAdapt discloses no public dollar rate card.
