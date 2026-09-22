# Indeed — access attempt (blocked), S1 job-posting sweep

```yaml
source:          Indeed
url_or_doc_id:   https://www.indeed.com/rss?q=%22generative+engine+optimization%22 ; https://www.indeed.com/q-generative-engine-optimization-jobs-jobs.html ; https://www.indeed.com/jobs?q=%22generative+engine+optimization%22
published:       n/a — access attempt, not a successful pull
pull_date:       2026-09-22
pull_method:     fetch (curl, plain and with a browser User-Agent string; no browser extension, no login — both browser slots held by other agents per task brief)
pull_purpose:    evidence about a number
tier:            n/a — no content retrieved
tier_reason:     access blocked at every path tried
source_label:    n/a — no content retrieved this pull
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP error responses only
```

## Verbatim

`curl -s -o /dev/null -w "%{http_code}"` on `https://www.indeed.com/rss?q=%22generative+engine+optimization%22`: `403`

`curl` with a Chrome-120 User-Agent string on `https://www.indeed.com/jobs?q=%22generative+engine+optimization%22`: `403`, response body is Indeed's own bot-check page (Cloudflare-style challenge markup — a `<style>#cmsg{...}` block with the visible text `Please enable JS and disable any ad blocker`, though this is Indeed's own bot page rather than a Cloudflare-branded one).

## Pull notes — mechanical only

- **Recorded: Indeed job-posting search for GEO/AEO/AI-visibility terms at B2B SaaS employers — unknown — checked indeed.com (RSS endpoint, HTML search page, both plain fetch and browser-User-Agent fetch) — 403 on every attempt — 2026-09-22.**
- Per the task brief, the Chrome extension was not available (both slots held by other agents); RSS and JSON endpoints were tried in its place per the task's own instruction, and both are blocked the same as the HTML surface. Added to the browser backlog: `https://www.indeed.com/jobs?q=%22generative+engine+optimization%22` (and the parallel AEO/AI-visibility term variants), for a future agent holding an extension slot.
- This result matches `channels.md` C34's recorded access code (`403→ext`) for Indeed, confirming the prior finding rather than adding a new one.
