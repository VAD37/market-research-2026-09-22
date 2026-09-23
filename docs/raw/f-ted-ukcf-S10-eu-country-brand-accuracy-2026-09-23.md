# TED Search API v3 and UK Contracts Finder — S10 procurement: buyer country of every GEO-term notice; brand-accuracy ("AI reputation") queries

```yaml
source:          TED — Tenders Electronic Daily, Search API v3 (api.ted.europa.eu, anonymous); UK Contracts Finder REST API v2 (contractsfinder.service.gov.uk, anonymous)
url_or_doc_id:   POST https://api.ted.europa.eu/v3/notices/search {"query":"FT~\"<term>\"","scope":"ALL","limit":20,"fields":["publication-number","buyer-name","buyer-country","notice-title","publication-date"]} ; POST https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json {"searchCriteria":{"keyword":"<term>"},"size":20}
published:       TED notices 2025-06-06 to 2026-08-03 (publication-date per notice)
pull_date:       2026-09-23
pull_method:     fetch (curl POST, JSON)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     filed procurement records, table default for S10 (demand-signals.md "2 filed"); counts and fields as the registers return them
source_label:    filed
lane:            F
sub_market:      organic recommendation (GEO-term notices); n/a for the brand-accuracy queries (0 hits)
engine:          n/a
metric_kind:     none
supersedes:      none (extends docs/raw/f-ted-S10-repull2-2026-09-23.md, which holds the notice-XML context for the KKH and Hessen notices; no notice XML fetched here — the XML endpoint is WAF-walled on curl per that file)
captured:        API result counts; per-notice publication-number | buyer-country | publication-date | buyer-name | notice-title (English label) for every hit
```

## TED — call log

| # | query sent | HTTP | result |
|---|---|---|---|
| 1 | `FT~"AI reputation" OR FT~"KI-Reputation" OR FT~"réputation IA"` with fields list | 400 "Bad Request" (no detail) | request rejected — top-level OR / fields combination; not a WAF page |
| 2 | `FT~"AI reputation"` without fields | 400 "Validation error … field: fields … must not be empty" | API requires a fields list |
| 3 | `FT~"generative engine optimization"` with fields | 200 | totalNoticeCount 14 |
| 4 | `FT~"generative engine optimisation"` with fields | 200 | totalNoticeCount 1 |
| 5 | `FT~"Perplexity"` with fields | 200 | totalNoticeCount 6 |

[note: the brief allowed one try against the TED wall. Calls 1–2 were malformed requests answered by the API's validator, not by the AWS WAF "Human Verification" page recorded in the R-BLOCKED-2 file; the API itself answered anonymously on every call. A well-formed "AI reputation" query was not re-sent after call 2; its count is `unknown — API validation error on the two attempts, 2026-09-23`.]

## Verbatim — `FT~"generative engine optimization"`, all 14 notices

```
8523-2026   | ['DEU','DEU'] | 2026-01-08 | Land Hessen, vertreten durch die Hessische Zentrale für Datenverarbeitung; Justus-Liebig-Universität Gießen | Germany – IT services: consulting, software development, Internet and support – Webrelaunch Justus-Liebig-Universität Gießen
10938-2026  | ['DEU','DEU'] | 2026-01-08 | same buyers | same title family
30103-2026  | ['DEU','DEU'] | 2026-01-15 | same buyers | same title family
66176-2026  | ['DEU']       | 2026-01-29 | Kaufmännische Krankenkasse - KKH | Germany – Advertising and marketing services – Beschaffung einer Marketing-Agentur
70496-2026  | ['DEU','DEU'] | 2026-01-30 | Land Hessen / JLU Gießen | Webrelaunch …
106693-2026 | ['DEU','DEU'] | 2026-02-13 | Land Hessen / JLU Gießen | Webrelaunch …
129991-2026 | ['DEU','DEU'] | 2026-02-24 | Land Hessen / JLU Gießen | Webrelaunch …
240216-2026 | ['DEU','DEU'] | 2026-04-09 | Land Hessen / JLU Gießen | Webrelaunch …
275528-2026 | ['DEU']       | 2026-04-22 | Berlin Tourismus & Kongress GmbH | Germany – IT services: consulting, software development, Internet and support – Leistungen zu Website…
366557-2026 | ['DEU']       | 2026-05-28 | NRW.BANK AöR | Germany – Business services: law, marketing, consulting, recruitment, printing and security – RV Cor…
462463-2026 | ['DEU']       | 2026-07-06 | Berlin Tourismus & Kongress GmbH | Germany – IT services …
464049-2026 | ['DEU']       | 2026-07-06 | Bundesinstitut für Öffentliche Gesundheit (BIÖG) | Germany – IT services …
522860-2026 | ['DEU']       | 2026-07-29 | Kaufmännische Krankenkasse - KKH | Germany – Advertising and marketing services – Beschaffung einer Marketing-Agentur
533563-2026 | ['DEU']       | 2026-08-03 | Kaufmännische Krankenkasse - KKH | Germany – Advertising and marketing services – Beschaffung einer Marketing-Agentur
```

buyer-country tally: DEU 14 of 14. FRA, ESP, ITA, NLD, GBR: 0.

## Verbatim — `FT~"generative engine optimisation"`, 1 notice

```
352987-2026 | ['IRL'] | 2026-05-22 | An Post_391 | Ireland – IT services: consulting, software development, Internet and support – 0041 - Qualification…
```

## Verbatim — `FT~"Perplexity"`, 6 notices

```
368261-2025 | ['DEU'] | 2025-06-06 | Land Hessen, vertreten durch die Hessische Zentrale für Datenverarbeitung | Germany – IT services … – Penetrationstest-Lei…
440086-2025 | ['DEU'] | 2025-07-07 | KfW Bankengruppe | Germany – World wide web (www) site design services – Suchmaschinenoptimierung für Online-Medien der…
447779-2025 | ['DEU'] | 2025-07-09 | KfW Bankengruppe | same
693873-2025 | ['DEU'] | 2025-10-21 | Land Hessen … | Penetrationstest…
2571-2026   | ['DEU'] | 2026-01-05 | KfW Bankengruppe | Suchmaschinenoptimierung für Online-Medien der…
366557-2026 | ['DEU'] | 2026-05-28 | NRW.BANK AöR | Business services … – RV Cor…
```

buyer-country tally: DEU 6 of 6.

## UK Contracts Finder — call log and counts

| keyword sent | HTTP | hitCount |
|---|---|---|
| `"generative engine optimisation"` | 200 | 0 |
| `"AI visibility"` | 200 | 0 |
| `"generative engine optimization"` | 200 | 0 |
| `"answer engine optimisation"` | 200 | 0 |
| `"AI reputation"` | 200 | 0 |
| `ChatGPT visibility` (unquoted) | 200 | 759 (token match on either word; noticeList entries returned title/organisation/date fields as null in this call — not a category hit list) |

[note: `docs/customers/high-cpa-regulated.md` recorded UK Contracts Finder as "unknown (UK CF, TED)" on 2026-09-22; the anonymous REST endpoint answered on 2026-09-23.]

## Pull notes — mechanical only

- TED API responses carried multilingual `notice-title` objects; the English label is reproduced where present, else the first label. buyer-country is the API's ISO-3 list, duplicated when a notice names two buyers.
- No notice XML or PDF was opened in this pull (curl is WAF-walled on `ted.europa.eu/en/notice/<id>/xml`).
- Contracts Finder search_notices returned facet blocks (byRegion, byType, byStatus) alongside hitCount; not reproduced.
