# SOCi — Genius Local Search Agent product page, pricing check, and customer teasers

```yaml
source:          SOCi Inc.
url_or_doc_id:   https://www.soci.ai/products/genius-search/; https://www.soci.ai/pricing/
published:       undated on both pages
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from table default (5, vendor case study) for the four named customer-story teasers — no baseline figures, no absolute dates, no independent measurer for any of the four; product page itself is tier 3 (platform primary)
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          OpenAI named as an integration partner; no specific engine named per customer result
metric_kind:     visibility (local-rank, AI-recommendation-rate claims); traffic (direction requests, website visits)
supersedes:      none
captured:        full text of the product page; pricing page confirmed to carry no dollar figure
feature:         "Genius Local Search Agent" — SOCi's AI-visibility/local-SEO agent product, feeding the "AI Visibility Snapshot" and "2026 Local Visibility Index" evidence captured in `a-soci-roster-clear-2026-09-22.md`
```

## Verbatim

"Agentic AI Local SEO Software for Multi-Location Brands — Get Found Everywhere Customers Search, Including AI." "Accurate isn't the same as recommended. Local Search Agent is trained on your business and optimizes every location continuously so you don't just show up in local search, you get chosen when customers ask AI where to go." "Local Search Agent structures categories, attributes, descriptions, and Q&A the way answer engines actually parse them – so your locations become the source AI cites." "Tracks visibility across apps — See where your brand surfaces across search, maps, and AI-driven discovery, benchmarked location by location."

Aggregate comparative claims (vendor-measured, no stated n or date window): "2x more visible — Brands using agent-managed programs reach twice the local search and AI visibility of self-managed programs." "**10% lift in AI visibility** — Agents increase how often AI platforms recommend a brand's locations, in a channel where only 1.2% of locations get recommended at all." [note: the "1.2%" figure matches the ChatGPT-recommendation-rate figure from the LVI study in `a-soci-roster-clear-2026-09-22.md`, confirming both pages draw on the same underlying data.] "30% more local action — Website visits and direction requests rose an average of 30% after agents took over."

Four named customer-result teasers: "Increased Visibility — Scooter's Coffee boosted direction requests 38% YoY and grew local rankings 27% with Genius Agents." "Built to Scale — Across 1,300+ locations, Genius Agents keep Smoothie King's lean team running local marketing without missing a beat." "With SOCi's AI-powered platform, Liberty Tax grew locations ranking in the local '3-pack' from 60% to 90% and review volume grew 120%." "Genius Agents helped Priderock Capital Management improve placement in the local 3-pack for terms like 'apartments near me' +127%, delivering significant gains in local discoverability." Each links to a "Learn More" full story, not opened this pull (screened, not graded — see pull notes).

Integrations named: OpenAI, Google, Apple Maps, Google Maps, Bing, Olo.

## Evidence grading (on intake, from the teaser text only — full stories not opened)

**evidence_grade: Fools gold, all four** (on intake). Scooter's Coffee: brand named, metric named (direction requests, local rankings), percentage given (38% YoY, 27%) — "YoY" implies a one-year window but no absolute calendar dates or starting baseline count; no independent measurer. Liberty Tax: brand and metric named, before/after percentages given (60%→90% local 3-pack; +120% review volume) but no date window at all. Priderock: brand and metric named (+127%) but no baseline, no date window. Smoothie King: no quantified before/after metric at all, scale-only claim. None of the four names an engine specifically (all describe "local search"/"3-pack" results, which is Google Maps/local-pack visibility, not necessarily LLM-answer visibility) — flagged, since this cluster's remit is AI-visibility evidence and these read as adjacent local-SEO claims rather than LLM-recommendation claims specifically; the LVI study in the companion file is the stronger, more directly on-topic AI-visibility evidence for SOCi.

## Pull notes — mechanical only

- Both pages fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML.
- `not disclosed — checked soci.ai/pricing 2026-09-22` — no dollar figure anywhere on the pricing page; sales-led ("Get a Free Demo" / "Get Demo" are the only calls to action found across every SOCi page pulled this cluster). No price delta computable.
- The four "Learn More" full customer-story pages were not opened this pull (time-budgeted against the four held-name checks still remaining in this cluster); counted as screened, not graded beyond the teaser text above.
