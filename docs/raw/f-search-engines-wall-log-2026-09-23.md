# P16-c1 — search-channel wall log, 2026-09-23 (measured-by-us)

```yaml
source:          P16-c1 agent, this repo — HTTP responses observed while searching for budget-line surveys and 2026 ad forecasts
url_or_doc_id:   endpoints listed below
published:       2026-09-23
pull_date:       2026-09-23
pull_method:     fetch (curl with contact User-Agent) and Playwright MCP browser where stated
pull_purpose:    evidence about a number — records which channels were checked, for the `unknown — checked` cells
tier:            1
tier_reason:     measured by us (status codes), not a claim about the market
source_label:    measured-by-us
lane:            F, E
sub_market:      n/a
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        status per endpoint
```

## Verbatim — observed responses

| Channel | Endpoint | Result | Note |
|---|---|---|---|
| WebSearch (tool) | — | refused: "this session has used its web search budget (200 of 200 WebSearch calls)" | 0 calls available to this agent |
| DuckDuckGo html | https://html.duckduckgo.com/html/?q=… | HTTP 403 (curl, WebFetch, mcp fetch) | body: "If this persists, please email us" |
| DuckDuckGo lite | https://lite.duckduckgo.com/lite/ (GET and POST) | HTTP 403 | |
| DuckDuckGo (browser) | https://duckduckgo.com/?q=… | redirected to /static-pages/home-error/418.html | Playwright |
| Mojeek | https://www.mojeek.com/search?q=… | HTTP 403 | |
| Yahoo | https://search.yahoo.com/search?p=… | HTTP 307 → 500 | |
| Startpage | https://www.startpage.com/do/search?q=… | HTTP 200, 22 KB, zero result links | JS shell |
| Bing (curl, mkt=en-US) | https://www.bing.com/search?q=… | HTTP 200; results in Chinese, Korean, Vietnamese; off-topic | geolocated; setlang/cc ignored |
| Bing (browser, mkt=en-US) | same | rendered; results off-topic (Microsoft Forms pages for "survey") | Playwright |
| Google (browser) | https://www.google.com/search?q=… | redirected to /sorry/index (CAPTCHA) | wall, not solved |
| Brave Search (curl) | https://search.brave.com/search?q=… | first query HTTP 200 with results; every later query HTTP 200, 74,100-byte JS shell, zero results | one usable result list obtained |
| Brave Search (browser) | same | page title "Captcha - Brave Search" | wall, not solved |
| Search Engine Land site search | https://searchengineland.com/?s=… | HTTP 403 | |
| Marketing Dive site search | https://www.marketingdive.com/search/?q=… | HTTP 403 | |
| PPC Land site search | https://ppc.land/search/?q=… | HTTP 404 | |
| EDGAR full-text search | https://efts.sec.gov/LATEST/search-index?q=… | HTTP 200 throughout | the working channel; log in `f-edgar-fts-budget-line-queries-2026-09-23.md` |
| sec.gov Archives, browse-edgar atom | — | HTTP 200 throughout | |
| iab.com | report landing | HTTP 200; body gated "Claim your free account" | not registered |
| gartner.com | newsroom | HTTP 200 (403 in Pass 6) | |
| magnaglobal.com | site | HTTP 200; 2024 forecast page 404 | |

## Pull notes — mechanical only

- Queries attempted on the walled engines (nothing usable returned): "generative engine optimization" budget survey 2026; "AI visibility" budget survey marketers 2026; Gartner CMO Spend Survey 2026; agency survey clients "AI search" budget; earnings call shift paid search to AI search; WPP Media This Year Next Year 2026; MAGNA June 2026; dentsu 2026 (the last two resolved through the one Brave result list).
