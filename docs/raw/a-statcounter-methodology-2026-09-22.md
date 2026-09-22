# StatCounter Global Stats — FAQ / methodology

```yaml
source:          StatCounter Global Stats
url_or_doc_id:   https://gs.statcounter.com/faq
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary (own docs/method page), not itself a share figure — table default for this kind of page per trust-rubric tier 3 ("own docs, changelog, pricing page"); recorded here to justify the tier held for the two StatCounter share pulls in this cluster
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          n/a — method page covers all engines StatCounter tracks
metric_kind:     none
supersedes:      none
captured:        section extract via fetch tool (AI-summarized from source HTML)
```

## Verbatim (as extracted)

### Page views, not unique visitors

StatCounter tracks "page views" rather than unique visitors. A page view occurs each time someone loads a page on one of their member websites. Preferred because it accounts for frequency of use and multi-browser usage by individuals — e.g. someone loading 500 pages in one browser vs. one page in another gets weighted accordingly.

### Network & sample size

Data is analyzed from "more than 1 million sites globally" with StatCounter's tracking code installed. Monthly volume includes "over 3 billion page views" (July 2022 example cited: 5.3 billion global pageviews, 1 billion from the US alone). Sites "cover various activities and geographic locations" to achieve randomness.

### AI chatbot measurement — explicit limitation stated by the source

StatCounter "cannot directly measure AI chatbot queries." Instead it tracks "search engine referrals" — clicks from search results/chat answers to websites. For Bing Chat specifically it monitors referral clicks to websites; data shows "less than 1/100 of 1 percent" traffic from Bing Chat, noting users are less likely to click source links since chatbots provide direct answers.

### Caveats stated by the source

Individual website statistics "can be skewed due to the type of person who visits that site" and may not reflect global patterns. No artificial weighting is applied, though bot activity is removed and Chrome prerendering is adjusted for.

### Data collection mechanism

Statcounter is a web analytics service that relies on a tracking code installed on individual partner sites — no toolbar-based collection. Statcounter tracks the activity of third parties (site visitors) on member websites, "not solely on the activity of members," intended to reduce self-selection bias and approximate a random sample.

## Pull notes — mechanical only

- Access: plain fetch succeeded (200).
- This page is the closest thing to a published method statement StatCounter offers; it explicitly says the "AI chatbot market share" series is a **referral-click measurement**, not a direct usage panel — this is the method disclosure the trust-rubric tier depends on. It is a page-view/tag-network method, not a recruited demographic panel, which the summary table should carry alongside the figures it backs.
