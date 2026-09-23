# Wayback Machine — G2 "Answer Engine Optimization (AEO)" and "AI Search Visibility Optimization Tools" category listing counts, and Capterra "AI Search Visibility Software", per capture date

```yaml
source:          web.archive.org captures of G2.com category pages and one Capterra category page; CDX API for the capture list
url_or_doc_id:   http://web.archive.org/cdx/search/cdx?url=www.g2.com/categories/answer-engine-optimization-aeo&output=json&filter=statuscode:200&collapse=timestamp:6 ; same for www.g2.com/categories/ai-search-visibility-optimization-tools and www.capterra.com/ai-search-visibility-software/ ; captures fetched as http://web.archive.org/web/<timestamp>id_/<url>
published:       each capture's own timestamp, below
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"); gzip bodies decompressed; the "N Listings in <category> Available" string read from the archived HTML by regex; page <title> read the same way
pull_purpose:    evidence about a number
tier:            5
tier_reason:     the count is G2's own listing count at that date (vendor-reported by the review site); a Wayback capture is the page's claim at that date, not an independent measurement; the CDX collapse to one capture per month is our selection
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none — extends docs/raw/f-g2-capterra-S4-repull-2026-09-23.md (live counts 632 and 541 on 2026-09-23) with dated history
captured:        capture list (one per month, status 200) and, per fetched capture, the listing-count string and page title
verbatim:        full for the strings quoted
```

## CDX capture list — one capture per calendar month, status 200 (`collapse=timestamp:6`)

### www.g2.com/categories/answer-engine-optimization-aeo — 6 captures

| timestamp | statuscode | digest | length |
|---|---|---|---|
| 20251114153222 | 200 | IKIKR745UQZSG6KG2CYZDUINC7ZIISCK | 174147 |
| 20251203151547 | 200 | KX4KNIHLWNEKVUWNEVLTEOPSG7AWW3FH | 176846 |
| 20260113150325 | 200 | EXDGQDGGNP3DWAPJSYFW2HJ2URWGVAD2 | 182409 |
| 20260724192332 | 200 | WI24UBFVJHKOCGT74SOVKDSJ7YYMX5WM | 86279 |
| 20260805090405 | 200 | PUOUXWWUFWRCVRH2FE5M2SMFEHFK3YJU | 102152 |
| 20260914055858 | 200 | FPHB3R66GJ2XQ5GKRH2PIJFLG2SGQG3X | 102334 |

[note: no capture between 2026-01-13 and 2026-07-24 in the collapsed list.]

### www.g2.com/categories/ai-search-visibility-optimization-tools — 3 captures

| timestamp | statuscode | digest | length |
|---|---|---|---|
| 20260722090128 | 200 | AOOSPAOSCT63BXEGWN3WGUPLXS5LNDMH | 77599 |
| 20260801064317 | 200 | MZG6OBXMUIHUKEEEPM5CN6ZIQEFEPD6O | 81459 |
| 20260917180323 | 200 | AHLJNOP5VBYI2OTPKN4FFFZVK33JXHBD | 101233 |

### www.capterra.com/ai-search-visibility-software/ — 1 capture

| timestamp | statuscode | digest | length |
|---|---|---|---|
| 20260803221116 | 200 | RXTXO2B6S3NQIY2NQTUXH5WZL3HWRYEH | 121275 |

### www.g2.com/categories/generative-engine-optimization-geo — CDX returned no JSON (empty response); no capture list.

## Listing counts read from each fetched capture — verbatim strings

| Capture (UTC) | Page title, verbatim | Listing-count string, verbatim | "Updated" string on page |
|---|---|---|---|
| 2025-11-14 15:32:22 | Best Answer Engine Optimization (AEO) Tools: User Reviews from November 2025 | 160 Listings in Answer Engine Optimization (AEO) Available | — |
| 2025-12-03 15:15:47 | Best Answer Engine Optimization (AEO) Tools: User Reviews from December 2025 | 216 Listings in Answer Engine Optimization (AEO) Available | — |
| 2026-01-13 15:03:25 | Best Answer Engine Optimization (AEO) Tools: User Reviews from January 2026 | 159 Listings in Answer Engine Optimization (AEO) Available | — |
| 2026-07-24 19:23:32 | Best Answer Engine Optimization (AEO) Tools: User Reviews from July 2026 | 458 Listings in Answer Engine Optimization (AEO) Available | Updated April 9, 2026 |
| 2026-08-05 09:04:05 | Best Answer Engine Optimization (AEO) Tools: User Reviews from August 2026 | 477 Listings in Answer Engine Optimization (AEO) Available | Updated April 9, 2026 |
| 2026-09-14 05:58:58 | Best Answer Engine Optimization (AEO) Tools: User Reviews from September 2026 | 618 Listings in Answer Engine Optimization (AEO) Available | Updated April 9, 2026 |
| 2026-09-23 (live, browser, `f-g2-capterra-S4-repull-2026-09-23.md`) | Best Answer Engine Optimization (AEO) Tools: User Reviews from September 2026 | 632 Listings in Answer Engine Optimization (AEO) Available | Updated April 9, 2026 |
| 2026-07-22 09:01:28 | Best AI Search Visibility Optimization Tools Software: User Reviews from July 2026 | 246 Listings in AI Search Visibility Optimization Tools Available | Updated March 24, 2026 |
| 2026-08-01 06:43:17 | Best AI Search Visibility Optimization Tools Software: User Reviews from August 2026 | 288 Listings in AI Search Visibility Optimization Tools Available | Updated March 24, 2026 |
| 2026-09-17 18:03:23 | Best AI Search Visibility Optimization Tools Software: User Reviews from September 2026 | 521 Listings in AI Search Visibility Optimization Tools Available | Updated March 24, 2026 |
| 2026-09-23 (live, browser, same raw as above) | Best AI Search Visibility Optimization Tools Software: User Reviews from September 2026 | 541 Listings in AI Search Visibility Optimization Tools Available | Updated March 24, 2026 |
| 2026-08-03 22:11:16 (Capterra) | Best AI Search Visibility Software 2026 \| Capterra | no listing-count string on the page; highest pagination link `?page=5` | — |
| 2026-09-23 (Capterra live, browser, same raw) | Best AI Search Visibility Software 2026 \| Capterra | "Page 1 of 9"; page 9 holds 36 profiles | — |

[note: the 2026-01-13 AEO count (159) is lower than the 2025-12-03 count (216); both are what the archived pages state. The archived HTML of the three 2025–Jan-2026 captures is ~1.24 MB decompressed against ~0.6–0.69 MB for the 2026-07 onward captures — the page template changed between those dates.]

## Pull notes — mechanical only

- CDX calls returned JSON on the first try for every URL except the GEO category slug, which returned an empty body (no captures or unsupported URL).
- First fetch batch saved gzip-encoded bodies (magic bytes 1f8b); decompressed with gunzip before parsing. Second batch fetched with `--compressed`.
- Only one capture per month was fetched (the first status-200 capture the CDX `collapse=timestamp:6` returned); intra-month captures not examined.
- Counts read by regex `([\d,]+)\s+Listings? in ([^\n]{3,80})`; each capture returned the same string twice (page header and a repeated block); recorded once.
- No login, no CAPTCHA (archive.org serves the pages without the DataDome wall that g2.com live returns to curl — HTTP 403 on 2026-09-23, 1,704 bytes).
