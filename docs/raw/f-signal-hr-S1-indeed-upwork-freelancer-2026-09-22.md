# Indeed, Upwork, Freelancer — S1 job/gig postings, access record, high-CPA regulated vertical

```yaml
source:          Indeed (indeed.com), Upwork (upwork.com), Freelancer (freelancer.com)
url_or_doc_id:   see per-channel rows below
published:       n/a — access-path record, not a content pull for Indeed/Upwork
pull_date:       2026-09-22
pull_method:     fetch (direct curl, no browser extension, no login)
pull_purpose:    evidence about category noise (access-path record) for Indeed and Upwork; evidence about a number for Freelancer (a genuine but near-empty result)
tier:            n/a for Indeed/Upwork (nothing retrieved); 6 for Freelancer (marketing/noise-level page, no n, no date-filtered listing)
tier_reason:     Freelancer's category page returned "Showing 1 to 1 of 1 entries" with no vertical or buyer-size tagging and a tag cloud of stale, undated 2008-era SEO gig titles — not usable as an S1 number
source_label:    n/a
lane:            F
sub_market:      n/a — no qualifying content retrieved
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP status only for Indeed and Upwork (body was a 403 challenge page in both cases); Freelancer's rendered HTML shell (result-count line and tag-cloud block) — the actual project listing itself is not present in the static HTML (client-side rendered)
vertical:        high-CPA regulated — targeted query used `generative engine optimization insurance` (Indeed) and `generative engine optimization` (Upwork, Freelancer); no vertical-tagged content reached for any of the three
cell:            n/a — no attributable signal
query:           `https://www.indeed.com/jobs?q=generative+engine+optimization+insurance`; `https://www.indeed.com/rss?q=generative+engine+optimization+insurance`; `https://www.upwork.com/nx/search/jobs/?q=generative%20engine%20optimization`; `https://www.upwork.com/ab/feed/jobs/rss?q=generative%20engine%20optimization`; `https://www.freelancer.com/jobs/generative-engine-optimization/`
```

## Access results, this agent's own checks, 2026-09-22

| Channel | URL tried | Method | Result |
|---|---|---|---|
| Indeed, main search | `indeed.com/jobs?q=generative+engine+optimization+insurance` | direct fetch, no extension | **403** |
| Indeed, legacy RSS endpoint | `indeed.com/rss?q=generative+engine+optimization+insurance` | direct fetch | **403** — response body is an HTML challenge/error shell (27,610 bytes), not RSS/XML |
| Upwork, main search | `upwork.com/nx/search/jobs/?q=generative%20engine%20optimization` | direct fetch | **403** |
| Upwork, guessed RSS path | `upwork.com/ab/feed/jobs/rss?q=generative%20engine%20optimization` | direct fetch | **403** |
| Freelancer, category/search page | `freelancer.com/jobs/generative-engine-optimization/` | direct fetch | **200** — but "Showing 1 to 1 of 1 entries" (page's own result-count string); the one live project entry is rendered client-side and not present in the static HTML this agent's fetch retrieves; the page's "Other jobs related to Generative Engine Optimization (GEO)" tag cloud lists ~25 unrelated, undated gig titles from what appears to be a long-running evergreen SEO category page ("ahmedabad search engine optimization", "pakistan search engine optimization", "search engine optimization joomla15" — none dated, none insurance/card/supplement-tagged) |

Per the task's instruction, indeed.com and upwork.com are confirmed 403 to this agent's fetch-only access (no Chrome extension slot held by this agent). No browser-extension retry was attempted, consistent with the task's fetch-only scope; this is recorded as a **browser backlog** item, not resolved this pull.

Freelancer.com is reachable but returns essentially no usable signal for this vertical: one total entry on its GEO category page, un-attributed to insurance, cards, or supplements, and no buyer-size information anywhere on the page.

## Caveats

- `channels.md` C34 (Indeed) already records `403→ext` as the expected access code; this pull reconfirms it on 2026-09-22 and additionally confirms the RSS-endpoint workaround also 403s.
- `channels.md` C66 already records Upwork as `403→ext`; this pull reconfirms it and additionally confirms a guessed RSS path also 403s.
- Freelancer.com's category page is architecturally closer to an evergreen SEO landing page (undated related-job tag cloud, generic "Recommended Articles" content-marketing blocks) than a live, filterable gig-search results page reachable without JavaScript execution; its "1 of 1 entries" figure is recorded as-is and not treated as a real S1 count.
- This file is a negative/access-blocked record. It does not substitute for a Chrome-extension pull of Indeed or Upwork, which remains unresolved for this cluster.
