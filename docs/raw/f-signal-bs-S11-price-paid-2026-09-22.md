# S11 disclosed price actually paid, B2B SaaS buyer — search and existing-raw check

```yaml
source:          DuckDuckGo HTML search; cross-check against this repo's Pass 4 B2B SaaS case files
url_or_doc_id:   https://html.duckduckgo.com/html/?q=%22we+pay%22+OR+%22we%27re+paying%22+%22AI+visibility%22+OR+GEO+OR+AEO+tool+SaaS+per+month ; docs/raw/e-case-quattr-cloudeagle-2026-09-22.md ; docs/raw/e-case-census-c2-2026-09-22.md ; e-case-census-c4-2026-09-22.md
published:       n/a — search attempt, not a dated publication
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent, DuckDuckGo HTML endpoint; plus a manual re-check of already-pulled Pass 4 case files for a price-paid figure)
pull_purpose:    evidence about a number
tier:            n/a — no qualifying disclosure found
tier_reason:     no source found stating a price a B2B SaaS buyer actually paid for an AI-visibility/GEO/AEO tool
source_label:    n/a
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        zero-result search page; grep of the cited case file for price/contract-value language
```

## Verbatim

DuckDuckGo HTML search, query `"we pay" OR "we're paying" "AI visibility" OR GEO OR AEO tool SaaS per month`: HTTP 200, **zero results returned** (no `result__a` / `result__snippet` blocks present in the response).

Direct string search on `docs/raw/e-case-quattr-cloudeagle-2026-09-22.md` (the one B2B SaaS-tagged Pass-4 case already on file, Quattr / CloudEagle, Bronze grade) for `price paid`, `paid $`, `contract value`, `per month`, `/mo`, `annual (contract|fee)`: **no match** — the case describes traffic and citation-share lift, not a disclosed vendor fee.

## Pull notes — mechanical only

- **Result: `none — checked DuckDuckGo HTML search (zero results) and this repo's existing B2B SaaS Pass-4 case files (docs/raw/e-case-quattr-cloudeagle-2026-09-22.md, and the B2B SaaS-tagged rows in e-case-census-c2 and e-case-census-c4) — 2026-09-22.`**
- Consistent with the catalogue's own note that S10/S11 "reach tier 2 but are rare. Expect most cells to have neither" (`demand-signals.md`). The three B2B SaaS Pass-4 cases already on file (Quattr/CloudEagle Bronze; RankPrompt/Humand Bronze; Rankscale/"AI SMS Platform" Fools gold) are all vendor case studies reporting **outcome metrics** (traffic, citation share, visibility percentage), never a disclosed fee — matching this repo's `templates/customer-segment.md` warning that "a vendor list price is not a willingness-to-pay observation."
- Vendor list prices for AI-visibility tools generally (Profound, Peec, Scrunch, Otterly, etc., per `a-vendor-census-c1`–`c4`) are **asking prices**, already out of scope for S11 by definition, and not re-cited here.
- No cell moved.
