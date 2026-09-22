# EMARKETER — "US Search Advertising Forecast 2026" (search-ad-spend proxy, gated)

```yaml
source:          EMARKETER — author Nate Elliott
url_or_doc_id:   https://www.emarketer.com/content/us-search-advertising-forecast-2026
published:       2026-05-14
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool; page fetched cleanly, no 403, but report body is subscription-gated — only the site navigation shell and report table-of-contents rendered)
pull_purpose:    evidence about a number
tier:            n/a — no number reached this pull; page recorded for its topic and table of contents only, see caveat below
tier_reason:     table default would be tier 4-5 (EMARKETER named-analyst report) but no figure was reachable to tier at all — full text is subscription-gated
source_label:    analyst-derived
lane:            E
sub_market:      organic recommendation — this is the "share of search or SEO budget, analyst-derived" proxy plan.md Pass 6 names explicitly
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        site navigation shell plus the report's own table of contents (section headings only) — no body figures reached; the report itself was not purchased or otherwise unlocked
```

## Verbatim

Report title and byline, as rendered on the gated landing page: "US Search Advertising Forecast 2026. Spending Grows Consistently as Amazon and AI Offset Traditional Search's Deceleration. Report by Nate Elliott | May 14, 2026."

Table of contents (section headings, the only content this pull reached):

> "Executive Summary
> Search ad spending continues to show strong linear growth
> Traditional search is losing ground as Google's lead slips
> Amazon is now the biggest driver of search advertising growth
> AI is starting to drive search ad spending
> Recommendations for brands"

No dollar figure, percentage, or date-window figure is reachable in this captured content — the report body sits behind EMARKETER's subscription paywall ("Does my company subscribe? ... Become a Client ... Get a Demo ... Pricing").

## Pull notes — mechanical only

- Fetched cleanly via plain fetch, no 403 — this is a **paywall**, not a fetch block: the page loads fully but its report body is gated behind an EMARKETER subscription, distinct from the robots.txt-level 403 blocks recorded elsewhere in this cluster (Gartner, Grand View Research).
- This file is filed specifically because plan.md's Pass 6 detail names "share of search or SEO budget, analyst-derived" as the one required proxy category, and this report's own section heading — "AI is starting to drive search ad spending" — is the closest-matching, most directly on-point EMARKETER product located for that proxy in this task. No number behind that heading was reachable.
- `unknown — checked emarketer.com/content/us-search-advertising-forecast-2026 2026-09-22` for every figure this report might carry (total US search ad spend, AI's stated share or dollar contribution, and any SEO-budget-shift statistic).
- See the companion pulls in this cluster for the two other EMARKETER report pages attempted this task: `e-market-size-emarketer-aiads-paid-2026-09-22.md` (also gated at the primary, relayed via PPC Land) and `e-market-size-emarketer-openai-paid-2026-09-22.md` (a short-form news item, not gated, fetched in full).
- **Browser backlog**: `emarketer.com/content/us-search-advertising-forecast-2026` — needs an authenticated or subscription-holding browser session to reach the report body; not reachable by this fetch-only task's access.
