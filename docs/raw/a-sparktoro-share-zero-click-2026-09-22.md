# SparkToro — "In 2026, Less than One Third of Google Searches Still Send a Click"

```yaml
source:          SparkToro (blog, authored by Rand Fishkin)
url_or_doc_id:   https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
published:       2026-06-09
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default for clickstream panel with method named (Similarweb desktop/mobile panel, Jan-Apr 2026 US window, session-definition stated); no panel size/recruitment disclosed in this article, held at 4 not 5 because the date window, population and a technical definition (10-second inactivity session end) are all stated
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          Google (AI Mode)
metric_kind:     traffic
supersedes:      none
captured:        section extract via fetch tool (AI-summarized from source HTML)
```

## Verbatim (as extracted)

### Key statistic

"In the first four months of 2026, a whopping 68.01% of Google searches ended without a click."

### Historical comparison (source's own figures, some attributed to earlier panels)

- ~49% (2019)
- 60.45% (2024)
- 68.01% (2026)
- "representing a 33.8% increase over the decade" [note: this specific percent-change framing is the source's own characterization]

### AI traffic data

"Only 0.34% of searches routed to AI Mode during January-April 2026," though Google reported AI Mode surpassed 1 billion monthly users by I/O 2026 with query volumes "doubling quarterly."

### Methodology details (as stated)

- Data source: Similarweb's desktop and mobile web panel
- Time window: January–April 2026 (US)
- Panel composition: mobile/desktop split estimated at roughly 2/3 mobile, 1/3 desktop
- Mobile session definition: 10 seconds of inactivity marks session end
- Note: data excludes Google's mobile search app, "where zero-click features are more aggressive"

### Secondary finding cited

Ahrefs tracked traffic to 75,000+ opted-in domains, showing an 8-percentage-point decline (approximately 22% drop) from June 2025 to May 2026. [note: Ahrefs not independently pulled in this cluster; recorded here as the source's own citation]

## Pull notes — mechanical only

- Access: plain fetch succeeded (200).
- The 0.34% Google AI Mode query-share figure here matches the figure already captured in `a-similarweb-share-zero-click-marketing-2026-09-22.md` (same underlying Similarweb data, same Jan–Apr 2026 window) — the two pulls corroborate rather than conflict; kept as separate raw files per one-file-per-pull rule.
- "1 billion+ monthly users" and "doubling quarterly" for AI Mode are Google's own company-stated figures as relayed by this source, not Similarweb panel data — labeled company-stated in the summary table, not vendor-reported.
