# SparkToro — "New Research from Similarweb: How AI Brand Mentions Influence Direct Visits & Traditional Search Queries"

```yaml
source:          SparkToro (blog, authored by Rand Fishkin, covering Similarweb research)
url_or_doc_id:   https://sparktoro.com/blog/new-research-from-similarweb-how-ai-brand-mentions-influence-direct-visits-traditional-search-queries/
published:       2026-06-29
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default — SparkToro is reporting on Similarweb's own clickstream-panel study ("The Downstream Impact of AI Visibility"); method (clickstream panel, 7-day window) is named, but the underlying Similarweb report itself was not independently pulled, so this file is a pointer-with-figures rather than the Similarweb primary
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a — brand-level effect, not engine-share
metric_kind:     traffic
supersedes:      none
captured:        section extract via fetch tool (AI-summarized from source HTML)
```

## Verbatim (as extracted)

### Research referenced

Similarweb's "The Downstream Impact of AI Visibility" — examined whether AI brand mentions have real impact on marketing.

### Industries studied

Finance, travel, and beauty.

### Key findings

AI recommendations were followed by measurable increases in direct website visits for the recommended brand. Examples given:
- American Express: visitors 7.2% more likely to visit their site after an AI recommendation
- Capital One: 14.2% increase

### Measurement methodology (as stated)

Similarweb analyzed "clickstream panel data" tracking user behavior "within seven days" of AI mentions, comparing recommended vs. non-mentioned brands.

### Critical context (source's own framing)

Study focused on "big brands" (examples: Sephora, American Express, Capital One). Fishkin notes "traditional search engines are still about a hundred times more popular" overall, and cautions results may not generalize to smaller or lesser-known brands.

### Unanswered questions (source's own framing)

Gaps noted regarding counterfactual scenarios, smaller-brand performance, and comparative impact versus other channels (Google rankings, social media visibility).

## Pull notes — mechanical only

- Access: plain fetch succeeded (200).
- This is not an assistant-share figure (visits/referral share by engine); it is a brand-mention-to-traffic causal-adjacent claim. Filed in this cluster because it is a clickstream-panel-method pull surfaced by the P2-c1 query book (`site:sparktoro.com clickstream methodology`), and because H1 ("referral from AI assistants converts above organic search") is directly adjacent to this finding. Not used as an engine-share row in the summary table; noted in caveats instead.
- "A hundred times more popular" (traditional search vs. AI assistants) is the source's own rough figure, not a percentage with a stated base — flagged, not treated as a discard-on-sight case since it is qualitative framing rather than the headline statistic.
