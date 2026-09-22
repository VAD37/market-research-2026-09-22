# Similarweb — customers / case studies for AI Brand Visibility (screened)

```yaml
source:          Similarweb Ltd.
url_or_doc_id:   https://aisearch.similarweb.com/ai-brand-visibility/ (only testimonial found); https://www.similarweb.com/corp/customer-stories/ (404); https://www.similarweb.com/corp/customers/ (404); https://www.similarweb.com/corp/case-studies/ (404)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            7
tier_reason:     downgraded from table default — the one item found is a single-line, unattributed-to-a-brand testimonial with no metric, no baseline, no date; discard-on-sight per trust-rubric.md ("no n, no date window, or no method"); not graded, filed only as evidence of what is and is not available
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        the one testimonial found on the feature page; three guessed customer-story index URLs, all 404
feature:         AI Brand Visibility — customer/case-study screening
```

## Verbatim

The only customer-attributed content found on `aisearch.similarweb.com/ai-brand-visibility/` naming AI Brand Visibility specifically is: "With AI searches on the rise... I get asked a lot of questions on the regular by senior company executives. Similarweb has enabled me to quickly and easily answer these questions with compelling visuals." — Jon Baldwin, Senior SEO Content Manager. **No company/brand name, no metric, no baseline, no date window.** **Not graded — discarded per trust-rubric.md's "no n, no date window, or no method" criterion.**

Three guessed URL patterns for a Similarweb customer-stories index — `similarweb.com/corp/customer-stories/`, `similarweb.com/corp/customers/`, `similarweb.com/corp/case-studies/` — all returned HTTP 404. The global navigation on every Similarweb page pulled this cluster lists a "Customer Stories" nav item, but its underlying href was not present in any static HTML captured (likely client-side/JS-routed), and it was not resolved via a browser render this pull (time-budgeted against this cluster's five other vendors and four held-name checks).

## Pull notes — mechanical only

- Fetched via `curl` with a browser User-Agent string for the successful pull; three HTTP 404s recorded for the guessed customer-story index paths.
- **Case studies screened: 1** (the one testimonial). **Cleared: 0.** This is the thinnest case-study evidence found for any of the five incumbents in this P3-c4 cluster — BrightEdge, Muck Rack, Quattr, and Semrush all disclosed named, quantified customer case studies; Similarweb did not, on the pages reached this session.
- `unknown — checked aisearch.similarweb.com/ai-brand-visibility, similarweb.com/corp/customer-stories (404), similarweb.com/corp/customers (404), similarweb.com/corp/case-studies (404), similarweb.com/corp/pricing (no case-study link found) 2026-09-22` — a proper customer-story index for AI Brand Visibility, if one exists, was not located this pull via direct-fetch-preferred discovery; the claude-in-chrome extension was not connected and the Playwright browser fallback was not invoked for this specific check (used instead for Semrush's JS-rendered case studies, which were the higher-priority target given their evidence density).
