# OLAPLEX Inc. — Greenhouse job board, full postings check (S1, negative)

```yaml
source:          OLAPLEX Inc., own career site via Greenhouse
url_or_doc_id:   https://boards-api.greenhouse.io/v1/boards/olaplexcareers/jobs?content=true ; board id found via https://olaplex.com/pages/careers
published:       undated (live board as of pull date)
pull_date:       2026-09-23
pull_method:     fetch (curl, Greenhouse's public jobs JSON API, no login)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — S1 "3 (employer's own posting)"; recorded here as a checked-negative, not a positive finding
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full jobs array, title and location fields, from the Greenhouse public API
```

## Query — verbatim

`GET https://boards-api.greenhouse.io/v1/boards/olaplexcareers/jobs?content=true` — Greenhouse board id `olaplexcareers` located from a link on `olaplex.com/pages/careers` (`boards-api.greenhouse.io/v1/boards/olaplexcareers?callback=parseBoard`).

## Verbatim

Full title list, 8 of 8 open postings, 2026-09-23:

> "AR Manager (Remote Role)" — United States
> "Director of Trade Marketing & Events, Pro Americas (Hybrid Role - New York)" — New York
> "Field Sales Manager, West (California - OC/LA Area)" — California
> "Packaging Design Production Artist (Hybrid Role - New York)" — New York
> "Project Manager, Packaging Design & Artwork (Hybrid Role - New York)" — New York
> "Regional Account Manager, Texas (Remote Role)" — Texas
> "Regional Education Manager, APAC (Singapore)" — Singapore
> "Sales and Marketing Brand Manager, APAC" — Singapore

None names SEO, AEO, GEO, AI search, AI visibility, or any marketing-technology/digital-growth title. No posting body opened beyond the title list — none of the 8 titles is a plausible match for the signal.

## Pull notes — mechanical only

- Public Greenhouse JSON endpoint, no browser, no login, no CAPTCHA. HTTP 200.
- Contrast: Olaplex was separately confirmed mid-market (278 employees, filed 10-K, `f-edgar-sk-headcount-midmarket-olaplex-beautyhealth-2026-09-23.md`) and carries a genuine llms.txt artifact (`f-signal-sk-S12-llms-txt-midmarket-2026-09-23.md`). This pull closes S1 for Olaplex specifically as checked, nothing found — the cell's S1 spend signal rests on Beauty Health / Hydrafacial only (`f-signal-sk-S1-hydrafacial-workday-geo-aeo-2026-09-23.md`), not on Olaplex.
