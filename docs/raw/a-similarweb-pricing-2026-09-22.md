# Similarweb — pricing (feature vs. base plan)

```yaml
source:          Similarweb Ltd.
url_or_doc_id:   https://aisearch.similarweb.com/ai-brand-visibility/ (self-serve AI Search plans, shown in page body); https://www.similarweb.com/corp/pricing/ (general Web Intelligence plans, enterprise/self-serve tabs)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary pricing pages
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full pricing tables on both pages
feature:         AI Brand Visibility / AEO Intelligence price and price delta against a non-AI base plan
```

## Verbatim

### Self-serve "AI Search" plans (on the AI Brand Visibility landing page itself)

**AEO Intelligence** — "Best for researchers & analysts." **$99.** 1 User; 3 months of historical data. Includes: AEO Intelligence, AI Brand Visibility, 150 tracked prompts, Sentiment Analysis, Citation Analysis, AI Traffic.

**AEO & SEO & Competitive Intel** ("Most Popular") — "Best for marketers & SEO managers." **$333.** 1 User; 6 months of historical data. All of the above, plus: SEO Intelligence, Organic Search Overview, Keyword Research, Rank Tracker, Site Audit & Backlinks, Competitive Intelligence, Website Performance, Traffic & Engagement, Customer Demographics, Marketing Channels Overview, Competitor Alerts.

**AEO & SEO & Ads & Competitive Intel** — "Best for performance marketers." **$542.** 1 User; 6 months of historical data. All of the above, plus: Ad Intelligence, Creative & Campaign Insights, Search/Display/Social Insights, Advertiser Demand Signals, Ad Spend.

No billing period (monthly/annual) is labelled next to these three figures on this page; no currency symbol beyond "$" is shown.

### General pricing page (`similarweb.com/corp/pricing/`)

Two audience tabs: "Entrepreneurs" and "Businesses & Enterprises." The page defaults to "Businesses & Enterprises," which shows module names with no dollar figures, every module gated behind "Talk to sales" / "Contact sales": Competitive Intel Suite, Strategic SEO Suite, Ads Intel Suite, and **"Gen AI Intel Suite" (AI Traffic Trends, AI Brand Visibility, Top Landing Pages, Prompt Analysis)** — all custom-quoted. FAQ, verbatim: "How do I buy a Similarweb package? If you're interested in our solutions for businesses and enterprises, please contact our sales team to discuss a custom package tailored to your needs. You can also start a free trial or try one of our self-service packages for individuals, entrepreneurs, and small teams."

## Pull notes — mechanical only

- Both pages fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML.
- **No self-serve base plan without AI Brand Visibility was found.** The cheapest self-serve tier reached this pull ($99, "AEO Intelligence") already bundles AI Brand Visibility, Sentiment Analysis, Citation Analysis, and AI Traffic — there is no lower-priced "SEO only, no AEO" self-serve tier shown on either page pulled to compute a clean delta against. `unknown — checked aisearch.similarweb.com/ai-brand-visibility, similarweb.com/corp/pricing, similarweb.com/corp/entrepreneurs/pricing (404) 2026-09-22` for a self-serve non-AI base tier.
- On the enterprise/"Businesses & Enterprises" side, the base "Web Intelligence" platform and the "Gen AI Intel Suite" add-on module are both priced "Talk to sales" — **price and price delta not disclosed — checked similarweb.com/corp/pricing 2026-09-22.**
- This differs structurally from Semrush (clean, disclosed dollar delta between a base plan and an AI-visibility-inclusive plan, see `a-semrush-pricing-2026-09-22.md`) and from BrightEdge/Muck Rack/Quattr (no public price at all): Similarweb discloses a self-serve AI-inclusive price ($99) but not a matching non-AI baseline to subtract it from, and its enterprise tier discloses neither.
