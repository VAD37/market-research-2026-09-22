# Ten B2B SaaS domains — /llms.txt presence check — measured by us

```yaml
source:          measured-by-us — direct HTTP request to each domain's /llms.txt path
url_or_doc_id:   https://hubspot.com/llms.txt ; https://salesforce.com/llms.txt ; https://atlassian.com/llms.txt ; https://asana.com/llms.txt ; https://monday.com/llms.txt ; https://notion.so/llms.txt ; https://slack.com/llms.txt ; https://zoominfo.com/llms.txt ; https://docusign.com/llms.txt ; https://dropbox.com/llms.txt
published:       n/a — live site check, not a dated publication
pull_date:       2026-09-22
pull_method:     fetch (curl, this session's Bash tool, no browser extension)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default for S12 — measured-by-us, output in raw/
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page (or full 404 page) for each of the ten domains
prompt_set:      n/a | runs_n: 10 domains | surface: n/a (static file check) | region: n/a
```

## Verbatim

Method: `curl -s -o /dev/null -w "%{http_code}" -L "https://<domain>/llms.txt"` (follows redirects), cross-checked with `-D -` header dump and a content sample where the code was ambiguous. Domain sample: ten public B2B SaaS company root domains, chosen for name recognition and public status/scale (not drawn from any vendor's own customer list, per the task's own-domain requirement, not a target-customer inference).

| # | Domain | Final HTTP code | Content-Type | Result |
|---|---|---|---|---|
| 1 | hubspot.com | 200 | text/plain; charset=x-macroman | Present. Opens: "# HubSpot / > HubSpot is an AI-powered customer platform connecting marketing, sales, service, content, data, commerce, and AI in one system built around Smart CRM..." |
| 2 | salesforce.com | 200 | text/plain; charset=UTF-8 | Present. Body is a curated link list, e.g. "- [AI Agent Course: Free Online Training](https://www.salesforce.com/agentforce/ai-agent-course/): Explore AI agent courses..." |
| 3 | atlassian.com | 200 | text/plain; charset=utf-8 | Present (content not sampled beyond header/content-type check) |
| 4 | asana.com | 200 | text/plain; charset=UTF-8 | Present (content not sampled beyond header/content-type check) |
| 5 | monday.com | 200 | text/plain; charset=utf-8 | Present (content not sampled beyond header/content-type check) |
| 6 | notion.so | 200 | text/plain; charset=utf-8 | Present (content not sampled beyond header/content-type check) |
| 7 | slack.com | 200 | text/plain;charset=utf-8 | Present (content not sampled beyond header/content-type check) |
| 8 | zoominfo.com | 200 | text/plain; charset=utf-8 | Present. Opens: "# ZoomInfo LLM Information / Last updated: March 2026 / This file provides official information about ZoomInfo for large language models, AI crawlers, and automated systems. ## Company: ZoomInfo Technologies Inc. Ticker Symbol: NASDAQ: GTM ... Employees: 3,000+ Customers: 35,000+" |
| 9 | docusign.com | 404 | text/html; charset=utf-8 | Absent. Real 404 page confirmed (title "The requested page could not be found (404) \| Docusign", canonical `https://www.docusign.com/404`) — not a soft-404 or redirect artefact |
| 10 | dropbox.com | 200 | text/plain | Present (content not sampled beyond header/content-type check) |

Two domains substituted mid-sample and recorded here for completeness, not counted in the ten: **zendesk.com** — `https://zendesk.com/llms.txt` returns 301 to `https://www.zendesk.com/llms.txt`, and the `www.` host then refuses the TLS handshake to this client (curl exit code 35, SSL connect error) on every retry — access blocked, not a content result, so excluded from the ten and not substituted with a re-check. **box.com** — 403 on `/llms.txt`, same treatment, excluded.

Result: **9 of 10 sampled domains carry a `/llms.txt` file (200, real text content); 1 of 10 (docusign.com) returns a genuine 404.** Share of sampled domains carrying the artifact: 90% (9/10), or 9/12 (75%) if the two access-blocked domains (zendesk.com, box.com) are counted as attempted-and-inconclusive rather than dropped.

## Pull notes — mechanical only

- All ten target domains resolved and responded without needing the browser extension; `curl -L` followed the `http -> https` and bare-domain -> `www.` redirects transparently for every domain except zendesk.com, which loops or blocks at the `www.` host specifically (SSL handshake failure, not an HTTP-level redirect or 404).
- Content-Type `text/plain` (vs. `text/html`) was used as a secondary check against a soft-404 (some sites return HTTP 200 with an HTML "not found" page instead of a proper 404 status); every 200 in the table above carried a genuine `text/plain` content-type, and the one 404 (docusign.com) carried `text/html` with an explicit "could not be found" title, confirmed by direct content inspection.
- No browser extension or Playwright used for this pull — per this task's fetch-only constraint. Bash/curl only.
- This sample is not vertical-scoped by design (the task specifies "ten public SaaS company domains," not ten specifically-B2B-SaaS-vertical-tagged domains) — all ten are recognised B2B SaaS vendors (CRM, project management, communication, e-signature, cloud storage, sales/marketing intelligence), so the sample is read as B2B SaaS vertical evidence, sub-market organic recommendation (the artifact is an unpaid on-property signalling mechanism, not paid or transactional), buyer size unassigned at the artifact level (the check is per-domain, not per-buyer-size; these are all themselves large public/late-stage companies, so if forced onto the buyer-size bands per `demand-signals.md` — HubSpot, Salesforce, ZoomInfo, Atlassian, Asana, monday.com, Notion, Slack, Dropbox are all disclosed at headcount well over 1,000 per public filings/company pages (not independently re-verified in this pull) — Enterprise band; Docusign (the one 404) is also Enterprise-band by the same public-record reputation, so the one absence is not attributable to company size in this sample).
