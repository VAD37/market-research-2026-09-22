# Upwork (blocked) and Freelancer.com (reached, no data in static HTML) — S1/S6 sweep

```yaml
source:          Upwork; Freelancer.com
url_or_doc_id:   https://www.upwork.com/ab/feed/jobs/rss?q=generative%20engine%20optimization ; https://www.upwork.com/nx/jobs/search/?q=generative%20engine%20optimization ; https://www.freelancer.com/jobs/generative-engine-optimization/
published:       n/a — access attempt / live listing page, not a dated publication
pull_date:       2026-09-22
pull_method:     fetch (curl, plain and with a browser User-Agent string; no browser extension, no login)
pull_purpose:    evidence about a number
tier:            n/a — no usable content retrieved from either source
tier_reason:     Upwork blocked outright; Freelancer.com returned a client-rendered shell with no server-side job data
source_label:    n/a
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP error response (Upwork); empty/shell HTML page (Freelancer.com)
```

## Verbatim

`curl -s -o /dev/null -w "%{http_code}"` on `https://www.upwork.com/ab/feed/jobs/rss?q=generative%20engine%20optimization`: `403`, response titled "Challenge - Upwork" (bot-challenge page).

`curl` with a browser User-Agent on `https://www.upwork.com/nx/jobs/search/?q=generative%20engine%20optimization`: `403`, same challenge page.

`curl` with a browser User-Agent on `https://www.freelancer.com/jobs/generative-engine-optimization/`: `200`. Body is a 2,388-line HTML document; no `__NEXT_DATA__`, `window.__INITIAL_STATE__`, or any JSON block containing a job title, budget, or bid count was found in the static response — the visible strings present are template class names only (`"projects"`, `"ProjectBanner"`, `"ProjectManager"`), consistent with a JavaScript-rendered single-page application that requires a browser to populate.

## Pull notes — mechanical only

- **Recorded: Upwork job-posting/rate-card search for GEO/AEO/AI-visibility terms — unknown — checked upwork.com (RSS feed, HTML search page) — 403 on both — 2026-09-22.** Matches `channels.md` C66's recorded access code (`403→ext`) for Upwork.
- Freelancer.com is reachable (200) but not usable without a browser: added to the browser backlog as `https://www.freelancer.com/jobs/generative-engine-optimization/` (and the AEO/AI-visibility variants) for a future agent holding an extension or Playwright slot.
- Both sources feed S1 (job/gig postings) and S6 (posted freelance rates as an asking-price proxy) per `channels.md`'s signal-coverage table; this pull closes neither for the B2B SaaS vertical.
