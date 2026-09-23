# CourtListener — LTL LED, LLC (dba Wolf River Electric) v. Google LLC, D. Minn. 0:25-cv-02394: docket metadata (business defamation claim over an AI Overview)

```yaml
source:          CourtListener (Free Law Project) REST API v4, search endpoint, RECAP docket records
url_or_doc_id:   https://www.courtlistener.com/api/rest/v4/search/?q=%22Wolf+River+Electric%22&type=r ; https://www.courtlistener.com/api/rest/v4/search/?q=%22LTL+LED%22+Google&type=r ; docket id 70504071 (https://www.courtlistener.com/docket/70504071/ltl-led-llc-v-google-llc/ — HTTP 403 on curl) ; https://www.courtlistener.com/api/rest/v4/docket-entries/?docket=70504071 (HTTP 401, authentication required)
published:       docket dateFiled 2025-06-09; dateTerminated 2026-02-26 (per API fields)
pull_date:       2026-09-23
pull_method:     fetch (curl, anonymous; search endpoint open, docket page and entries walled)
pull_purpose:    evidence about a number (existence of a filed business-side complaint about an AI answer; no amount)
tier:            2
tier_reason:     filed court docket metadata (PACER/RECAP mirror); table default for filed. The complaint text itself was not reached — only docket fields
source_label:    filed
lane:            F
sub_market:      organic recommendation
engine:          Google AI Overviews (per the suit's public description; the docket fields below do not name the product)
metric_kind:     none
supersedes:      none (`docs/method/STATE.md` unknowns table records "courtlistener.com (WAF challenge blocked search)" on 2026-09-22; the API search endpoint answered on 2026-09-23)
captured:        API search results, selected fields verbatim
```

## Verbatim — search `"Wolf River Electric"`, type=r: count 15; first 8 results (caseName | court | dateFiled | docketNumber)

```
AiDigital Operating, LLC v. Wolf River Electric | District Court, S.D. New York | 2026-06-03 | 1:26-cv-04677
Roberts v. LTL LED, LLC dba Wolf River Electric | United States Bankruptcy Court, D. Delaware | 2025-12-29 | 25-52479
Roberts v. LTL LED, LLC | District Court, D. Minnesota | 2026-08-05 | 0:26-cv-03525
SunPower Corporation | United States Bankruptcy Court, D. Delaware | 2024-08-05 | 24-11649
LTL LED, LLC v. Google LLC | District Court, D. Minnesota | 2025-06-09 | 0:25-cv-02394
von Brandenfels v. LTL LED, LLC | District Court, D. Minnesota | 2026-02-20 | 0:26-cv-01559
The Burlington Insurance Company v. Ltl Led LLC | District Court, W.D. Wisconsin | 2026-07-01 | 3:26-cv-00608
National Liability & Fire Insurance Company v. LTL LED, LLC | District Court, W.D. Wisconsin | 2026-02-20 | 3:26-cv-00134
```

## Verbatim — search `"LTL LED" Google`, type=r: count 2; the Google docket record, fields as returned

```json
{"caseName": "LTL LED, LLC v. Google LLC", "court": "District Court, D. Minnesota", "court_id": "mnd", "dateFiled": "2025-06-09", "docketNumber": "0:25-cv-02394", "docket_id": 70504071, "suitNature": "320 Assault Libel & Slander", "cause": "28:1441 Petition for Removal- Personal Injury", "assignedTo": "Jeffrey M. Bryan", "dateTerminated": "2026-02-26"}
```

[note: "cause: 28:1441 Petition for Removal" means the federal docket opened on removal from a Minnesota state court; the state-court filing date precedes 2025-06-09 and is not in this record. "dateTerminated 2026-02-26" is a docket status field; the disposition (dismissal, settlement, remand) is not in the fields returned and was not reached. Docket entries require authentication (HTTP 401) and the docket HTML page returned HTTP 403.]

## Pull notes — mechanical only

- The v4 search endpoint answered anonymously (HTTP 200, 62,695 and 7,506 bytes). One try each on the docket page (403) and the docket-entries endpoint (401); not retried, no account created.
- wolfriverelectric.com (HTTP 200, 347 KB) was pattern-searched for "Google", "lawsuit", "AI Overview": only a Google-logo image and Google Site Kit script matched; no statement about the suit on the homepage.
- No EU court or regulator docket was searched for a business-side complaint about an AI answer (no open EU docket search endpoint identified in this pull).
