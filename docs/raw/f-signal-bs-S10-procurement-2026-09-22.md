# SAM.gov, UK Contracts Finder, TED — procurement record check, B2B SaaS / GEO / AEO terms

```yaml
source:          SAM.gov (US federal); Contracts Finder (UK); TED (EU)
url_or_doc_id:   https://sam.gov/api/prod/sgs/v1/search/?index=opp&size=10&mode=search&q=%22generative%20engine%20optimization%22 ; same endpoint with q=%22answer%20engine%20optimization%22 ; https://www.contractsfinder.service.gov.uk/Search/Results?Keywords=generative+engine+optimization ; https://www.contractsfinder.service.gov.uk/Search/Results?Keywords=AI+visibility+SaaS ; https://ted.europa.eu/en/search/result?FT_text=generative+engine+optimization
published:       n/a — live procurement-register query, not a dated publication
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent; no browser extension)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default for S10 ("2 filed") where a real result set is returned; not achieved for any B2B SaaS-relevant hit this pull — see result below
source_label:    filed
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        SAM.gov JSON response titles (first 5 of the result set, both queries); Contracts Finder result-count HTML fragment for two different keyword strings; TED search-results page HTTP status
```

## Verbatim

**SAM.gov**, query `q=%22generative%20engine%20optimization%22`: HTTP 200. First five result titles returned: "2930-014332550, cooler, lubricating oil, engine"; "COTS Trailer/Modification Propulsion System Rocket Engine Transport Trailer (PTT2)"; "Specialized Commercial Transportation Services Propulsion System Rocket Engine (PSRE) Transport"; "6515--MC | VISN 15 Path & Lab | NEW ANATOMIC PATHOLOGY WORKFLOW | Base plus 4 | (VA-27-00002252) GS-07F-139CA"; "29--OIL PUMP ASSEMBLY,ENGI[NE]" — every title matches the literal word "engine" against mechanical/aerospace/medical procurement notices, none relevant to AI visibility, GEO, or AEO. No `totalRecords` field was present in the JSON response to quantify the full result-set size.

**SAM.gov**, query `q=%22answer%20engine%20optimization%22`: HTTP 200, same non-relevant title pattern repeated (mechanical-parts and government-services notices unrelated to the query phrase) — confirms the API's `q` parameter is not enforcing phrase-relevance filtering the way a marketing-facing search engine would.

**UK Contracts Finder**, `Keywords=generative+engine+optimization`: HTTP 200, page text: `"We've found <span class="search-result-count">672</span>"` open notices. **Contracts Finder**, `Keywords=AI+visibility+SaaS` (a materially different query string): HTTP 200, identical result-count text: `"We've found <span class="search-result-count">672</span>"`. The identical count across two unrelated keyword strings indicates the `Keywords=` GET parameter is not being applied to filter the result set by this request shape (the site's real search likely requires a session/form POST or a differently-named parameter).

**TED (EU tenders)**, `FT_text=generative+engine+optimization`: HTTP 200 (page shell returned; earlier channel documentation in `channels.md` C20 recorded `405 to plain GET`, this pull's GET returned 200 for the page itself but the result grid is not present in the static HTML — no result-count string of the Contracts Finder kind was found, consistent with a JS/AJAX-rendered results grid).

## Pull notes — mechanical only

- **Result for S10, B2B SaaS vertical: `none — checked sam.gov (API reachable, zero relevant hits across two phrase queries), contractsfinder.service.gov.uk (reachable, but Keywords filter not applied via plain GET — result count static at 672 across two different query strings, so no usable per-query result obtained), ted.europa.eu (page reachable, results grid not present in static HTML — likely JS/AJAX-rendered) — 2026-09-22.`**
- This is expected on priors: `demand-signals.md`'s own S10 bias line states "Public-sector and large-buyer only; private demand invisible here," and AI-visibility/GEO/AEO tooling is a marketing-software category with no obvious government-procurement use case — a `none` read here is not surprising, but it is checked rather than assumed.
- Contracts Finder and TED are both added to the browser backlog for a session that can execute their real (session- or JS-based) search rather than the static GET path tried here: `https://www.contractsfinder.service.gov.uk/Search/Results?Keywords=%22generative+engine+optimization%22` and `https://ted.europa.eu/en/search/result?FT_text=%22generative+engine+optimization%22` (both to be re-tried with the browser extension, since the static-GET result cannot be trusted as a true zero).
- No cell moved by this pull.
