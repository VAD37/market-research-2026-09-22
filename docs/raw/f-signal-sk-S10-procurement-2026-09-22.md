# Procurement and tender registers — sam.gov, Contracts Finder, TED — skincare and beauty, AI visibility terms

```yaml
source:          sam.gov (US federal), contractsfinder.service.gov.uk (UK), ted.europa.eu (EU)
url_or_doc_id:   sam.gov/api/prod/sgs/v1/search/; contractsfinder.service.gov.uk/Search/Results; ted.europa.eu/en/search/result
published:       undated — live search interfaces, no publication date
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     dropped from expected tier 2 (per demand-signals.md S10) because neither reachable endpoint performed exact-phrase matching on this pull — sam.gov's search endpoint is undocumented and returned corpus-wide token matches (tens of thousands of results) rather than phrase hits, and Contracts Finder's Keywords field likewise OR-matched individual tokens rather than the quoted phrase, so no result on either channel can be confirmed as a genuine GEO/AI-visibility/beauty procurement record at this pull
source_label:    analyst-derived
lane:            F
sub_market:      n/a — no qualifying record found in any sub-market
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        API/HTML search-result pages, top results only; full corpus not paged through
```

## Query — verbatim

sam.gov (undocumented internal search API, `sam.gov/api/prod/sgs/v1/search/?random=<ts>&q=<query>&page=0`, User-Agent `Mozilla/5.0`):
- `q="AI visibility" beauty` — `totalElements: 49567` (not a genuine phrase-match count; top hit: "99--Beauty Equipment", a 2013 salon/beauty-equipment solicitation, RFQP0318100128, unrelated to AI visibility)
- `q="generative engine optimization"` — `totalElements: 229863`
- `q="answer engine optimization"` — `totalElements: 278437`
- `q="AI search visibility"` — `totalElements: 839673`
- `q=GEO AEO beauty marketing` — `totalElements: 52279`

All five sam.gov queries returned implausibly large `totalElements` figures inconsistent with a working phrase-search index (the quoted-phrase operator was not honored by this endpoint), so none of the counts above are usable as evidence of an actual GEO/AI-visibility procurement record. `sam.gov/search/` (the documented public UI, per `channels.md` C17) was not independently reached this pull; only the internal JSON API above was queried.

contractsfinder.service.gov.uk (`Search/Results?Keywords=<query>`, User-Agent `Mozilla/5.0`):
- `Keywords="AI visibility" beauty` — page states "We've found 675 notices"; top 10 titles inspected: "Renewable Energy Certification Integration in ASEAN", "Provision of Close Quarter Combat systems - RFI/PME", "Contractor Services", "Supply of summer annual bedding plants", "CA18488 - RFQ2026/37 - Appointment of Specialist Consultancy Team ... Theatre and Conference facility in Newry City", "Childrens Playtower", "GB-London: Consultancy Required for LondonEnergy Future Transport Yard Feasibility", "Project Tullie Phase 3: Digital Installation Design", "DPS1 1417 Tree Works", "DPS1 1418 - Highway Fell Trees" — none relevant to AI visibility or beauty; the 675-count and the title list together confirm the Keywords field OR-matches individual tokens, not the quoted phrase
- `Keywords="generative engine optimization"` — page returned HTTP 200, no result-count string matched by this pull's extraction pattern; not further parsed
- `Keywords="answer engine optimization"`, `Keywords="AI search visibility"` — HTTP 200, not parsed beyond status

ted.europa.eu: `https://ted.europa.eu/en/search/result?query=AI+visibility+beauty` returned HTTP 405 on plain GET (confirmed 2026-09-22, matches the task brief's expectation). A second path, `https://ted.europa.eu/en/search/result?FT=%22AI%20visibility%22`, returned HTTP 200 but resolved to a "Page not found - TED" HTML page, not a search result. `https://ted.europa.eu/api/v3.0/notices/search?q=...` returned HTTP 404 — no working REST endpoint found at this path. No TED notice reached this pull.

## Verbatim

sam.gov `q="AI visibility" beauty` top hit, verbatim JSON fragment:

```
"title":"99--Beauty Equipment","publishDate":"2013-07-19T13:35:13-04:00","isActive":false,
"descriptions":[{"content":"AMENDMENT NOTICE:This is a combined synopsis/solicitation for commercial items prepared in accordance with the format in FAR Subpart 12.6..."}]
```

Contracts Finder result-count line, verbatim HTML: `We&rsquo;ve found <span class="search-result-count">675</span> notices`

## Pull notes — mechanical only

- sam.gov's documented public search UI (`sam.gov/search/`, `channels.md` C17) returned HTTP 200 to a bare root fetch on 2026-09-22 (checked earlier in this session per `docs/sources/channels.md`) but its actual search results render client-side; this pull used the site's own backing JSON API instead, which is undocumented and appears not to support exact-phrase queries reliably.
- No API key or authenticated session used for sam.gov or TED.
- Neither `[note: paywall]` nor `[note: login wall]` applies — every endpoint above returned a public, unauthenticated response; the failure mode is query-precision (token OR-matching), not access.
- No further paging (page=1, page=2, ...) was attempted on any channel given the top-result signal was already clearly off-topic on all three.
- Per the cell-read rule (`demand-signals.md`), no observation above names a sub-market, vertical, or buyer size for a genuine procurement record, because no genuine record was found — this file supports `none — checked sam.gov, contractsfinder.service.gov.uk, ted.europa.eu 2026-09-22` for S10 across all nine skincare-and-beauty cells.
