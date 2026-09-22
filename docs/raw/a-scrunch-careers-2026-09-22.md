# Scrunch AI — careers

```yaml
source:          Scrunch AI, via Ashby job board
url_or_doc_id:   https://jobs.ashbyhq.com/scrunch ; https://scrunch.com/careers/ (404, redirects nowhere)
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary hiring page; downgraded from a normal tier-3 read to a bare existence check because the page is client-side-rendered and its job list did not appear in the static HTML this pull captured
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        raw HTML head/shell only — job listings render client-side and were not captured by this pull
```

## Verbatim

Page `<title>`: "Scrunch Jobs"
Page `<meta name="description">`: "Scrunch Jobs"
Page `<meta property="og:title">`: "Scrunch Jobs"

No job-listing text was present in the static HTML returned by this fetch — the page is an Ashby-hosted single-page application that loads its listing content via JavaScript after page load. The raw HTML head confirms the page is live and organization-branded (Ashby org theme assets reference "Scrunch") but carries no visible open-role count, titles, or locations in this capture.

`scrunch.com/careers/` returns HTTP 404; the "Careers" link in Scrunch's own site footer (captured on the pricing and case-studies pulls, this file's sibling pulls) points to the Ashby URL above, not to a page on scrunch.com itself.

## Pull notes — mechanical only

- `jobs.ashbyhq.com/scrunch` fetched twice: once with simplified/markdown rendering (returned only the title, no body — "Scrunch Jobs" with no further text), once with `raw: true` (returned the HTML `<head>` and inline styles, capped at 3000 characters before the job-listing script/data would have appeared).
- No browser-extension follow-up was run for this page given the low evidence value of a bare headcount-by-open-roles read relative to remaining task scope; recorded as `unknown — checked jobs.ashbyhq.com/scrunch (client-rendered, listing not captured) 2026-09-22` for the current open-role count and any team/location breakdown.
- Headcount as a point-in-time figure is available instead from Scrunch's own "About" page (`a-scrunch-funding-sitecore-acquisition-2026-09-22.md` cites it): "The team grows from 3 to 49 employees" as of the 2025 entry in that page's company-history timeline, pre-acquisition, no 2026 figure stated.
