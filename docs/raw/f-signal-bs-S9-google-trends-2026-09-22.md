# Google Trends — access method note, S9 search interest

```yaml
source:          Google Trends (trends.google.com)
url_or_doc_id:   https://trends.google.com/trends/explore?q=%22generative%20engine%20optimization%22,%22AI%20visibility%22,%22answer%20engine%20optimization%22
published:       n/a — access-method check, not a successful data pull
pull_date:       2026-09-22
pull_method:     fetch (curl, plain and with a browser User-Agent; no browser extension — both slots held by other agents per task brief)
pull_purpose:    evidence about a number
tier:            n/a — no data retrieved
tier_reason:     Google Trends' explore UI and its underlying widget/multiline data endpoints are not served to a plain HTTP client; the site requires a browser session (cookies, a signed `req` token per query fetched via an initial page load) that this fetch-only task cannot produce
source_label:    n/a
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP response codes and content type only
```

## Verbatim

`curl -s -o /dev/null -w "%{http_code}"` on `https://trends.google.com/trends/explore?q=%22generative+engine+optimization%22`: `200`, but `Content-Type: text/html` — the response is the Trends single-page-app shell (a React/Angular client bootstrap), not chart data. Google Trends' data endpoints (`trends.google.com/trends/api/explore` and `.../api/widgetdata/multiline`) require a `req=` parameter containing a token minted by the SPA's own JavaScript from an initial page load plus a `google_abuse_exemption`/session cookie pair; neither can be constructed from a bare `curl` request without executing that JavaScript.

## Pull notes — mechanical only

- **Recorded per the task brief's own instruction: "Google Trends is browser-only — record method or unknown."** Method recorded: the page itself returns HTTP 200 to a plain fetch, but the chart/interest data behind it is served only through a token-gated API that this session's tools (curl, WebFetch, no browser extension) cannot construct.
- Matches `channels.md` C45's listed access code (`200`) for the page shell itself, while confirming (not contradicting) that the underlying series data is not obtainable the same way — `channels.md` does not distinguish the page-shell response from the data-endpoint response, and this pull adds that distinction.
- Added to the browser backlog: `https://trends.google.com/trends/explore?q=%22generative%20engine%20optimization%22,%22AI%20visibility%22,%22answer%20engine%20optimization%22&geo=US` (and an EU-geo variant), for a future agent holding the browser extension.
- **Result for the census: `unknown — checked trends.google.com (page-shell reachable, data API token-gated, no browser session available) 2026-09-22`.** No cell moved.
