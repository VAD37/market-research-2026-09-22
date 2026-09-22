# PPC Land — "AI still under 2% but growing: Datos Q1 2026 State of Search report"

```yaml
source:          PPC Land, reporting the Datos (Semrush/Adobe) and SparkToro "State of Search" Q1 2026 report
url_or_doc_id:   https://ppc.land/ai-still-under-2-but-growing-datos-q1-2026-state-of-search-report/
published:       2026-04-28
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     trade-press pointer to a primary (Datos/SparkToro report), per trust-rubric "5 pointer" and channels.md C56 row; filed directly because the Datos primary report (`datos.live/report/...`) is form-gated with no public figures — see `a-similarweb...` pulls' caveats and the pull notes below. Underlying Datos panel itself would be tier 4 with method named ("tens of millions of active desktop users," date window, three-country population) if the primary were reachable
source_label:    analyst-derived
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Gemini, Claude, Google (AI Mode); Perplexity, Copilot, DeepSeek named but not broken out numerically
metric_kind:     traffic
supersedes:      none
captured:        section extract via fetch tool (AI-summarized from source HTML)
```

## Verbatim (as extracted)

### Publication & access

Published 2026-04-28 (early access to PPC Land on 2026-04-27). Report produced by Datos (a Semrush company) and SparkToro. Direct link to the underlying Datos report was not provided in the article.

### Methodology summary (as stated)

The report analyzed "large-scale clickstream data covering desktop behavior across the United States, the European Union, and the United Kingdom from March 2025 to March 2026" using a panel of "tens of millions of active desktop users." Specific panel size, device-count methodology and further technical measurement detail were not disclosed in this article.

### AI tool usage share by month/quarter

**Overall AI tools (combined), share of total desktop visits**
- US Q1 2025: 1.31% | US Q1 2026: 1.65%
- US January 2025: 0.41% | US March 2026: 0.93%
- EU/UK January 2025: 0.54% | EU/UK March 2026: 1.08%

**ChatGPT (US desktop users)**
- September 2025: 37.08% (peak)
- Q1 2026: 34.80%

**ChatGPT (EU/UK desktop users)**
- March 2026: 44.82%

**Gemini (US desktop users)**
- November 2025: 10.41% → March 2026: 16.06%

**Gemini (EU/UK desktop users)**
- November 2025: 12.29% → March 2026: 18.88%

**Claude (US desktop users)**
- January 2026: 3.58% → March 2026: 8.54%

**Claude (EU/UK desktop users)**
- January 2026: 3.77% → March 2026: 9.61%

**Perplexity, Copilot, DeepSeek**
- "Remained at single-digit or sub-5% levels with no significant movement" [note: source gives no per-engine percentage breakdown for these three]

### Google AI Mode (share of total desktop visits)

**US:**
- May 2025: 0.01%
- December 2025: 0.06%
- March 2026: 0.16%

**EU/UK:**
- August 2025: 0.01%
- December 2025: 0.06%
- March 2026: 0.21%

### Key finding (source's own framing)

"AI tools collectively account for less than 2% of total desktop web visits" despite substantial industry discussion about AI displacing traditional search.

## Pull notes — mechanical only

- Access: plain fetch succeeded (200).
- The primary Datos report pages (`datos.live/report/the-current-ai-landscape/`, `datos.live/report/state-of-search-q2-2026/`) were checked directly in this pull session and found form-gated with no extractable figures on the public landing page — this PPC Land item is the substitute that carries the actual numbers, per shortlist.md's "a pull that surfaces a better primary supersedes the listed one" rule, and per channels.md's description of trade press as a pointer channel to be pulled when the primary is unreachable.
- The "ChatGPT %" figures here (share of a single engine's users among desktop web population, e.g. 34.80% of US desktop users used ChatGPT) are a different metric from the StatCounter/Similarweb "share of chatbot-category traffic" figures elsewhere in this cluster — this is population penetration, not category share-of-visits. Kept distinct in the summary table, not treated as the same metric.
- The Google AI Mode figures here (0.16% US, 0.21% EU/UK, March 2026, share of total desktop visits) conflict in magnitude with the Similarweb-sourced 0.34% AI Mode query-share figure (Jan–Apr 2026, all Google searches) captured in `a-similarweb-share-zero-click-marketing-2026-09-22.md` and `a-sparktoro-share-zero-click-2026-09-22.md` — different populations (share of Google searches vs. share of total desktop web visits) and different panels (Similarweb vs. Datos); kept side by side in the summary table, never averaged.
