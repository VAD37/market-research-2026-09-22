# HubSpot — SEC filing naming AEO/AI search — access attempt (blocked)

```yaml
source:          SEC EDGAR (sec.gov, efts.sec.gov, data.sec.gov); secondary attempt: ir.hubspot.com, BamSEC (bamsec.com)
url_or_doc_id:   attempted: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001404655&type=10-K ; https://www.sec.gov/Archives/edgar/data/1404655/ ; https://efts.sec.gov/LATEST/search-index?q=%22answer+engine+optimization%22&entityName=HubSpot ; https://data.sec.gov/submissions/CIK0001404655.json ; https://ir.hubspot.com/financial-information/sec-filings ; https://www.bamsec.com/companies/1404655/hubspot-inc (reached, filing index only, full text paywalled)
published:       n/a — access attempt, not a successful pull of filing text
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool) and browser extension (MCP_DOCKER Playwright fallback) — both attempted, both blocked
pull_purpose:    evidence about a number
tier:            n/a — no content retrieved; the one page that did load (BamSEC's filing index) is tier 3 as a third-party index, not the filing itself
tier_reason:     access blocked at every SEC.gov endpoint tried; BamSEC's filing-index page (not the filing text) partially corroborates filing dates already stated in `docs/raw/a-vendor-roster-2026-09-22.md` row 10
source_label:    n/a — no filing text retrieved this pull
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        error messages only; BamSEC filing-index list (dates/forms, no filing body text)
```

## Verbatim

`mcp__MCP_DOCKER__fetch` on `www.sec.gov/cgi-bin/browse-edgar?...`: `"When fetching robots.txt (https://www.sec.gov/robots.txt), received status 403 so assuming that autonomous fetching is not allowed"`

`mcp__MCP_DOCKER__fetch` on `data.sec.gov/submissions/CIK0001404655.json`: `"When fetching robots.txt (https://data.sec.gov/robots.txt), received status 403..."`

`mcp__MCP_DOCKER__fetch` on `efts.sec.gov/LATEST/search-index?...`: `"When fetching robots.txt (https://efts.sec.gov/robots.txt), received status 403..."`

`mcp__MCP_DOCKER__fetch` on `ir.hubspot.com/financial-information/sec-filings`: `"When fetching robots.txt (https://ir.hubspot.com/robots.txt), received status 403..."`

MCP_DOCKER Playwright browser, three separate navigations (`www.sec.gov/edgar/search/#/q=...`, `www.sec.gov/cgi-bin/browse-edgar?...`, `www.sec.gov/Archives/edgar/data/1404655/`): all three returned a rendered SEC.gov page titled **"SEC.gov | Your Request Originates from an Undeclared Automated Tool"** (the first attempt returned "SEC.gov | Request Rate Threshold Exceeded" instead). All four navigation attempts across two tools and three distinct sec.gov URL patterns (cgi-bin browse, Archives directory listing, EDGAR full-text search SPA) were blocked.

BamSEC filing index (https://www.bamsec.com/companies/1404655/hubspot-inc, reached successfully, full fetch tool, not blocked) — filing dates only, no body text: "10-K ended 12/31/25 FY 2025 — 02/11/26" and "DEF 14A — Definitive proxy — 04/27/26" and "ARS — Scanned paper annual report submission — 04/27/26" — these three dates **corroborate** the dates already cited (without a direct URL) in `docs/raw/a-vendor-roster-2026-09-22.md` row 10 ("SEC 10-K/ARS/DEF 14A (HUBS), filed 2026-02-11 / 2026-04-27"). BamSEC's own full-document-text search is behind a login/subscription wall not accessed this pull.

## Pull notes — mechanical only

- **Recorded: SEC filing verbatim passage naming AEO/AI search for HubSpot — unknown — checked sec.gov (cgi-bin/browse-edgar, Archives directory, EDGAR full-text-search SPA — all blocked with "Undeclared Automated Tool" / "Request Rate Threshold Exceeded"), efts.sec.gov (robots.txt 403), data.sec.gov (robots.txt 403), ir.hubspot.com (robots.txt 403), bamsec.com (filing index reached, full text paywalled) — 2026-09-22.**
- The block appears to be a session/IP-wide bot-detection response from SEC.gov (both the plain-fetch tool and the Playwright browser were blocked, across four distinct sec.gov URL shapes), not a single-page or single-tool issue.
- Per the task's roster citation, the underlying filing is known to exist (10-K filed 2026-02-11, DEF 14A filed 2026-04-27, both naming "answer engine optimization" per the roster file's EDGAR full-text-search hit) but its verbatim passage could not be retrieved by this cluster despite four access attempts across two tools. This gap is carried into the census summary's unknowns table.
