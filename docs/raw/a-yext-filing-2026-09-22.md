# Yext — SEC filing naming AI visibility/GoShine — access attempt (blocked at SEC.gov; company-IR-site copy obtained instead)

```yaml
source:          attempted: SEC EDGAR (sec.gov) for the 8-K exhibit / 10-Q named in `docs/raw/a-vendor-roster-2026-09-22.md` row 14; obtained instead: Yext's own Investor Relations site republication of the same earnings release
url_or_doc_id:   attempted: https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex991q2fy27earningsrelease.htm (blocked); obtained: https://investors.yext.com/news-events/press-releases/detail/391/yext-announces-second-quarter-fiscal-2027-results
published:       2026-09-01, 8:00 am EDT
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool) — SEC.gov direct access blocked; investors.yext.com successfully fetched instead
pull_purpose:    evidence about a number
tier:            3
tier_reason:     company's own Investor Relations site republication of the earnings-release exhibit — platform primary, not a tier-2 direct pull of the SEC document itself (SEC.gov access blocked, see below). The page itself states this release has an associated "10-Q Filing (HTML, PDF, XBRL, ZIP)" as a "Related Document," confirming the same text was filed with the SEC the same day, but that filed copy was not independently retrieved this session.
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        error message for the direct SEC URL; full bullet list and opening paragraphs of the IR-site copy (full text already captured in `a-yext-launch-2026-09-22.md`, cited here rather than re-pasted)
```

## Verbatim

`mcp__MCP_DOCKER__fetch` on `https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex991q2fy27earningsrelease.htm`: `"When fetching robots.txt (https://www.sec.gov/robots.txt), received status 403 so assuming that autonomous fetching is not allowed, the user can try manually fetching by using the fetch prompt"`

This is the same SEC.gov-wide block encountered for HubSpot's filing (see `a-hubspot-filing-2026-09-22.md`) — confirming the block is domain-wide for this session, not specific to one filer or document.

**The company's own Investor Relations copy of the same release was successfully retrieved** (`investors.yext.com/news-events/press-releases/detail/391/...`) and states, verbatim, in its bullet list: **"Completed acquisition of GoShine, expanding the Yext platform to brand-level visibility optimization for AI search"** — full text reproduced in `a-yext-launch-2026-09-22.md`. That page's own UI shows "Related Documents: 10-Q Filing — HTML PDF XBRL ZIP" for this same release, confirming an associated SEC 10-Q/8-K exists for the same date (2026-09-01) but was not independently opened this session.

## Pull notes — mechanical only

- **Recorded: direct SEC-filed passage — unknown — checked sec.gov (Archives, direct document URL cited by `a-vendor-roster-2026-09-22.md` row 14) — blocked via robots.txt 403, 2026-09-22.** The company's own IR-site republication of the identical earnings-release text was obtained instead and is treated as the best available substitute this session, tiered one level lower (3, company-stated) than a direct SEC pull would have rated (2, filed), per the same approach taken for HubSpot in this cluster.
- Per the roster file, this same passage was originally sourced by a prior pass via `efts.sec.gov` full-text search (row 14: "SEC 8-K / Q2 FY27 earnings release (YEXT), filed 2026, `sec.gov/Archives/edgar/data/1614178/000162828026059706/ex991q2fy27earningsrelease.htm`, read 2026-09-22") — that prior pull evidently succeeded before this session's SEC-wide block took effect (or used a different access method not available to this task). This task's own direct attempt at the identical URL failed.
