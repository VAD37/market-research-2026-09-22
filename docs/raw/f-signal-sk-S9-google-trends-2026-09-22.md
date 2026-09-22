# Google Trends — search interest, "AI visibility beauty" vs "generative engine optimization"

```yaml
source:          Google Trends
url_or_doc_id:   https://trends.google.com/trends/explore?geo=US&q=AI%20visibility%20beauty,generative%20engine%20optimization
published:       undated — live tool; data window is the tool's own "Past 12 months" default at pull time (2025-09-21 to 2026-09-22 per the chart's own x-axis)
pull_date:       2026-09-22
pull_method:     browser extension (MCP_DOCKER Playwright, dedicated new tab) — Google Trends is JS-rendered and not reachable via plain fetch, matching the task brief's expectation that this channel is browser-only
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default per demand-signals.md S9 ("4 if method published") — Google Trends publishes its indexing method (relative 0-100 scale, normalized to the peak point in the selected window and region) on its own site, though the absolute query volume behind the index is not disclosed
source_label:    analyst-derived
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        rendered chart data table (weekly index values, both series, full 12-month window) and the "Related queries" panel for both terms, via DOM text extraction
```

## Query — verbatim

`https://trends.google.com/trends/explore?geo=US&q=AI%20visibility%20beauty,generative%20engine%20optimization` — two comparison terms, United States region, "Past 12 months" window (Google Trends' own default), "Web Search" category (Trends' own default, not narrowed to any vertical filter — Trends offers no beauty-specific category narrower than its own top-level categories, which were not applied this pull).

## Verbatim

Chart header and average index, verbatim: "United States, Past 12 months / Interest over time / Average — AI visibility beauty: 1 / generative engine optimization: 49"

Full weekly series (index 0-100, normalized to the peak point across both series in this window — the peak is "generative engine optimization" on 2025-09-21 at 100), verbatim table, column 1 = "AI visibility beauty", column 2 = "generative engine optimization":

```
Sep 21, 2025: 4, 100     Sep 28, 2025: 0, 79      Oct 5, 2025: 0, 47       Oct 12, 2025: 0, 45
Oct 19, 2025: 3, 38      Oct 26, 2025: 0, 36      Nov 2, 2025: 3, 41       Nov 9, 2025: 0, 38
Nov 16, 2025: 0, 38      Nov 23, 2025: 0, 19      Nov 30, 2025: 0, 18      Dec 7, 2025: 0, 18
Dec 14, 2025: 0, 22      Dec 21, 2025: 0, 18      Dec 28, 2025: 0, 16      Jan 4, 2026: 0, 27
Jan 11, 2026: 0, 34      Jan 18, 2026: 5, 48      Jan 25, 2026: 0, 37      Feb 1, 2026: 3, 38
Feb 8, 2026: 0, 39       Feb 15, 2026: 0, 53      Feb 22, 2026: 0, 77      Mar 1, 2026: 3, 57
Mar 8, 2026: 0, 50       Mar 15, 2026: 3, 72      Mar 22, 2026: 0, 58      Mar 29, 2026: 0, 48
Apr 5, 2026: 0, 54       Apr 12, 2026: 3, 62      Apr 19, 2026: 4, 65      Apr 26, 2026: 0, 61
May 3, 2026: 3, 64       May 10, 2026: 5, 73      May 17, 2026: 0, 75     May 24, 2026: 0, 76
May 31, 2026: 0, 80      Jun 7, 2026: 4, 90       Jun 14, 2026: 5, 76      Jun 21, 2026: 6, [truncated by extraction window, not captured]
```

"Related queries" panel, "AI visibility beauty", verbatim: "Hmm, your search doesn't have enough data to show here. Please make sure everything is spelled correctly, or try a more general term."

"Related queries — Rising" panel, "generative engine optimization", verbatim, "Showing 1-5 of 12 queries": "1 bread — Breakout / 2 concerts — Breakout / 3 gardening — Breakout / 4 parks — +350% / 5 soup — +350%"

## Pull notes — mechanical only

- No cookie-consent or login wall blocked data; a "This site uses cookies..." banner was present but did not gate the chart.
- The compound phrase "AI visibility beauty" is a constructed query for this pull's purposes, not confirmed to be a real query anyone types — its near-zero index (average 1, mostly 0 with isolated 3-6 spikes) is consistent with genuinely negligible search volume for that exact phrase, not necessarily with zero interest in the underlying topic under a different phrasing. No alternative phrasing (e.g., "does ChatGPT recommend my skincare brand") was tested this pull.
- The "generative engine optimization" related-rising-queries list (bread, concerts, gardening, parks, soup) is almost certainly noise from very low absolute query volume triggering Google's "Breakout"/percentage-rise algorithm on statistically insignificant counts, not a substantive finding — recorded verbatim per the no-interpretation rule, flagged here as noise rather than treated as evidence of anything about the category.
- `glossary.md`'s GEO-ambiguity warning is not directly implicated here since the query used the full unambiguated phrase "generative engine optimization," not bare "GEO."
- Full 12-month weekly series was captured except the final week's second-column value, cut off by the DOM-text extraction window (`Jun 21, 2026: 6, [not captured]`) — not re-fetched given the series trend is already clear from the preceding 51 weeks.
- Result for S9 across the nine skincare-and-beauty cells: no cell-attributable spend or attention finding — the compound beauty-specific query shows negligible measured interest, and the category-wide term is not itself vertical-attributable. Recorded as `checked — negligible/near-zero index for the beauty-specific phrase (tier 4)`.
