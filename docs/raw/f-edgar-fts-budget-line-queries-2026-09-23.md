# EDGAR full-text search — budget-line query log, filings 2026-01-01 to 2026-09-23

```yaml
source:          SEC EDGAR full-text search API (efts.sec.gov), hit lists as returned
url_or_doc_id:   https://efts.sec.gov/LATEST/search-index?q=<phrase>&dateRange=custom&startdt=2026-01-01&enddt=2026-09-23[&forms=…][&ciks=…]
published:       2026-09-23 (query date)
pull_date:       2026-09-23
pull_method:     fetch (curl with contact User-Agent; JSON parsed; first 20–25 hits per query listed; totals as returned)
pull_purpose:    evidence about a number — which filers state an AI-surface marketing action in 2026; feeds the "budget line" cells
tier:            2
tier_reason:     index of filed documents; each opened filing has its own raw file
source_label:    filed
lane:            F (S7 filings signal), E
sub_market:      organic recommendation; paid placement
engine:          as named per filing
metric_kind:     none (counts of filings)
supersedes:      none
captured:        hit totals and first-page hit lists
```

## Verbatim — hit totals

| Query (phrase) | Filter | Total hits | Hits opened (raw file) |
|---|---|---|---|
| "generative engine optimization" | none | 42 | Direct Digital 8-K 2026-08-12 (`f-agency-directdigital-8k-q2-2026-2026-09-23.md`); Semrush 10-K (`b-semrush-10k-2025-geo-demand-2026-09-23.md`); Coty 10-K 2026-08-20 (in repo, `f-signal-sk-S7-coty-10k-2026-09-22.md`); TechTarget 8-K 2026-05-07, Adobe 10-Qs, Change Agents, Onfolio — not opened |
| "answer engine optimization" | none | 14 | HubSpot 10-K (`f-signal-bs-S7-hubspot-10k-xfunnel-2026-09-23.md`); Rent the Runway 8-K (`f-rentrunway-8k-aeo-2026-09-23.md`); Duluth 10-K (`f-duluth-10k-aeo-2026-09-23.md`); Yext 8-K 2026-06-02, Similarweb 20-F, Locafy 6-K, Rezolve 6-K, Tailored Brands S-1 — not opened |
| "ChatGPT ads" | none | 3 | Criteo 8-K 2026-08-05 (in repo, `e-case-criteo-earnings-release-2026-08-05-2026-09-22.md`); Eightco 8-K, LiveRamp DEFA14A — not opened |
| "AI search" "marketing spend" | none | 33 | Yelp Q4 2025 letter (opened: data licensing with OpenAI, no budget line); 1-800-Flowers 10-K (opened: generic search-marketing risk only) |
| "AI search" | forms=8-K | 23 | Stagwell 8-K 2026-03-10 (`f-agency-stagwell-8k-q4-2025-2026-09-23.md`); Yext 8-K 2026-09-01 (`a-yext-8k-q2-fy2027-goshine-2026-09-23.md`); Revolve 8-K 2026-06-03 (opened: on-site AI search only) |
| "marketing budgets" "AI search" | none | 17 | TechTarget 10-K (`f-signal-bs-S7-techtarget-10k-2025-2026-09-23.md`); Amplitude 10-K (opened: vendor "AI Visibility" product launch 2025-10, no budget line) |
| "shift" "search engine optimization" "AI platforms" | none | 59 | eHealth 10-K (`f-signal-hr-S7-ehealth-10k-2025-2026-09-23.md`); LegalZoom 10-Q (`f-signal-hr-S7-legalzoom-10q-q2-2026-2026-09-23.md`); ZipRecruiter 10-Qs, Innodata, Adobe — not opened |
| "AI search" | ciks = Coty, e.l.f., Estée Lauder, Ulta, Sally Beauty, Olaplex | 0 | — |
| "AI platforms" OR "answer engines" OR "AI assistants" OR "agentic" | ciks = the six above + Kohl's | 4 | Coty 8-K 2026-08-19 (`f-signal-sk-S7-coty-8k-q4-fy2026-2026-09-23.md`); Coty 10-K (in repo); Ulta 10-K 2026-03-26 (opened: AI and agentic-commerce risk factor only); Kohl's 8-K — not opened, outside vertical |
| "AI search" | ciks = HubSpot, ZoomInfo, Semrush, TechTarget, Sprout Social, Zoom | 3 | Semrush 10-K; TechTarget 10-K; TechTarget ARS (not opened) |
| "AI search" | ciks = LendingTree, EverQuote, SelectQuote, GoHealth, MediaAlpha, Lemonade, Root, one mistyped CIK | 0 | — |
| "AI platforms" OR "answer engines" OR "AI-generated responses" | ciks = the above + eHealth, Oscar | 3 | eHealth 10-K 2026-02-26, 10-Q 2026-05-07 (not opened), 10-Q 2026-08-05 (`f-signal-hr-S7-ehealth-10q-q2-2026-2026-09-23.md`) |
| "AI search" OR "ChatGPT" | ciks = Omnicom, IPG | 0 | — |
| "Search and news advertising" | forms=10-K | 1 | Microsoft 10-K FY2026 (`b-microsoft-10k-fy2026-search-advertising-2026-09-23.md`) |

## Pull notes — mechanical only

- CIKs used: Coty 0001024305; e.l.f. 0001600033; Estée Lauder 0001001250; Ulta 0001403568; Sally Beauty 0001368458; Olaplex 0001530721; Kohl's 0000885639; HubSpot 0001404655; ZoomInfo 0001794515; Semrush 0001831840; TechTarget 0002018064; Sprout 0001645590; Zoom 0001108524; LendingTree 0001434621; EverQuote 0001625278; SelectQuote 0001794783; GoHealth 0001808220; MediaAlpha 0001818093; Lemonade 0001691421; Root 0001640428; eHealth 0001333493; Oscar 0001580808; Omnicom 0000029989; IPG 0000051644; 0001080667 was typed in the high-CPA list in place of Progressive (0000080661) — Progressive therefore unchecked.
- Every query returned HTTP 200. Hit lists beyond the first page were not paged.
