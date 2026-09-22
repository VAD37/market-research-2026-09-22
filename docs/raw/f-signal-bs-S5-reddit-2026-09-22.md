# Reddit — access attempt (blocked), S5 community thread volume

```yaml
source:          Reddit (r/SEO, r/PPC, r/bigseo)
url_or_doc_id:   https://www.reddit.com/r/SEO/search.json?q=%22AI%20visibility%22%20SaaS&restrict_sr=1
published:       n/a — access attempt, not a successful pull
pull_date:       2026-09-22
pull_method:     fetch (curl, plain and with a browser User-Agent; no browser extension, no login)
pull_purpose:    evidence about a number
tier:            n/a — no content retrieved
tier_reason:     access blocked
source_label:    n/a
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP error response only
```

## Verbatim

`curl -s -o /dev/null -w "%{http_code}"` on `https://www.reddit.com/r/SEO/search.json?q=%22AI%20visibility%22%20SaaS&restrict_sr=1`: `403`

`curl` with a Chrome-120 browser User-Agent on the same URL: `403`

## Pull notes — mechanical only

- **Recorded per task instruction: reddit.com unreachable — checked r/SEO `.json` search endpoint, plain and browser-User-Agent fetch, both 403 — 2026-09-22.**
- Matches `channels.md` C39's own note ("JSON API blocked in predecessor sessions") — this session reproduces the same block with a fresh attempt rather than inheriting the prior finding.
- r/PPC and r/bigseo were not separately tried given the identical domain-level block observed on r/SEO; recorded as covered by the same result.
