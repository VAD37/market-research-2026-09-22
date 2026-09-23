# Adobe Digital Insights — Quarterly AI Traffic Report, Q2 2026 (April 2026 report) — Wayback pull rate-limited (wall held this session)

```yaml
source:          Adobe Digital Insights (Adobe); Internet Archive Wayback Machine (attempted mirror)
url_or_doc_id:   https://business.adobe.com/resources/sdk/.2026-q2-ai-traffic-report/q2-2026-adi-ai-sourced-traffic-insights.pdf ; Wayback capture https://web.archive.org/web/20260819152425/https://business.adobe.com/resources/sdk/.2026-q2-ai-traffic-report/q2-2026-adi-ai-sourced-traffic-insights.pdf
published:       2026-04 (per the existing pull's cover page)
pull_date:       2026-09-23
pull_method:     fetch (curl) — direct domain, and Wayback `id_` raw-content URL, nine attempts total across ~3 minutes
pull_purpose:    evidence about a number
tier:            n/a — not pulled, wall held
tier_reason:     n/a
source_label:    n/a
lane:            C
sub_market:      agentic commerce
engine:          n/a
metric_kind:     n/a
supersedes:      none — does not supersede c-adobe-analytics-q2-2026-traffic-report-2026-09-22.md (that pull's browser-extension screenshot capture stands unchanged); this file records a same-day re-attempt via a different method that did not succeed
captured:        n/a — 0 bytes of PDF content; only HTTP error bodies
```

## Verbatim

Not applicable — wall held, no content retrieved.

## Pull notes — mechanical only

- Direct domain (`business.adobe.com/...pdf`) — `curl --max-time 20`: connection timeout (HTTP code `000`), consistent with the existing raw file's note and the repull-audit-2 probe ("business.adobe.com times out").
- Wayback availability API (`archive.org/wayback/available?url=...`) confirmed a capture exists: `20260819152425`, status 200.
- Wayback CDX search (`web.archive.org/cdx/search/cdx`) returned **HTTP 429 Too Many Requests** on first attempt.
- Wayback raw-content fetch (`web.archive.org/web/20260819152425id_/...pdf`) returned **HTTP 429** on every attempt: 1 immediate + 8 retries at 15-second intervals (background loop, ~2 minutes) + 2 further manual attempts (~25s and ~30s apart) = **11 total attempts across roughly 3 minutes, all HTTP 429**, response body a small HTML "Too Many Requests" nginx error page (162 bytes) each time.
- This contradicts the repull-audit-2 probe from earlier the same day ("Wayback id_ PDF 200, 2.28 MB") — the audit's own caveat anticipated this ("Probes are one request each from one IP on 2026-09-23... may revert"). Read as Wayback-side rate limiting against this session's IP/request volume (this session made many other `web.archive.org` and general internet requests earlier), not a change in the underlying capture's availability (the `available` API still reports it as `available: true`).
- Row status recorded `unknown-checked` in the queue CSV: wall holds for this session; a later session or a longer cooldown between Wayback requests may succeed where this one did not.
