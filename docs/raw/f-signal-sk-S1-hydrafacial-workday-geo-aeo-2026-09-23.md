# Hydrafacial / The Beauty Health Company — Workday career site, "Senior Manager, Performance & Organic Growth Marketing" (S1)

```yaml
source:          The Beauty Health Company (Hydrafacial), own career site via Workday
url_or_doc_id:   https://beautyhealth.wd12.myworkdayjobs.com/wday/cxs/beautyhealth/BeautyHealthCareer/job/United-States-of-America/Senior-Manager--Performance---Organic-Growth-Marketing_JR101647 (API); public page https://beautyhealth.wd12.myworkdayjobs.com/BeautyHealthCareer/job/United-States-of-America/Senior-Manager--Performance---Organic-Growth-Marketing_JR101647 ; posting id JR101647
published:       undated on the page (posting live as of pull date)
pull_date:       2026-09-23
pull_method:     fetch (curl, direct POST/GET against the Workday CXS JSON jobs API — no browser, no login)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — S1 "3 (employer's own posting)"
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a — no AI assistant named by the posting; "AI-driven search" is generic
metric_kind:     none
supersedes:      none
captured:        full jobPostingInfo.jobDescription field from the Workday CXS job-detail JSON response
```

## Query — verbatim

Job list: `POST https://beautyhealth.wd12.myworkdayjobs.com/wday/cxs/beautyhealth/BeautyHealthCareer/jobs` with body `{"appliedFacets":{},"limit":20,"offset":0,"searchText":""}` (and `offset:20` for the second page) — 39 total postings returned across two pages, no search filter applied so as not to miss non-obvious titles; every title read.
Job detail: `GET https://beautyhealth.wd12.myworkdayjobs.com/wday/cxs/beautyhealth/BeautyHealthCareer/job/United-States-of-America/Senior-Manager--Performance---Organic-Growth-Marketing_JR101647`.

## Verbatim

> "WHY THIS ROLE MATTERS The Senior Manager, Performance & Organic Growth Marketing will lead performance marketing across Paid Media and SEO/AEO for Hydrafacial and SkinStylus, with a primary focus on driving qualified device leads and supporting consumer demand."

> "WHAT YOU'LL DO ... Develop and execute SEO, AEO, and GEO strategies that increase brand visibility across traditional and AI-driven search and generate qualified organic traffic. ..."

> "WHAT WE'RE LOOKING FOR Required 7+ years of experience in digital or performance marketing with demonstrated experience driving B2B or B2B2C growth. ... Experience with SEO and emerging AI-driven search strategies, including AEO and/or GEO. ..."

> "Base Pay: $121,000- 143,000/annually + bonus"

> "About Us Hydrafacial is a global category-creating company focused on bringing innovative products to market and delivering beauty health experiences..."

Full 39-posting title list (two pages, `offset=0` and `offset=20`) read for other GEO/AEO/AI-visibility duties: none found besides this one role. Other titles are production, logistics, quality, business development, training, tax, sales and one other marketing role ("Marketing Specialist (German speaking)", no AI-search wording in its own description, not separately opened beyond the title list).

## Pull notes — mechanical only

- Workday's `wday/cxs` endpoint is a JSON API, no browser rendering needed; `POST` with an empty `searchText` returns the full unfiltered board, paginated — used instead of a keyword search so a duty-only mention (not in the title) would not be missed.
- Company name on the posting is "Hydrafacial" (consumer/professional brand); the SEC-filed legal entity and 10-K headcount (613 employees, `f-edgar-sk-headcount-midmarket-olaplex-beautyhealth-2026-09-23.md`) is "The Beauty Health Company" (NASDAQ: SKIN) — Hydrafacial and SkinStylus are Beauty Health's two named product/brand lines; same employer, mapped to the SEC-filed headcount per the boundary rule's filing-first proxy order.
- No login, no CAPTCHA, no paywall. HTTP 200 on both calls.
