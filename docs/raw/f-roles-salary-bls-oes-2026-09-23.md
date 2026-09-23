# US BLS OEWS — Market Research Analysts & Marketing Specialists, Marketing Managers, Web Developers — May 2024 and May 2025

```yaml
source:          U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics (OEWS) program
url_or_doc_id:   https://www.bls.gov/oes/special-requests/oesm24nat.zip (May 2024 national data file); https://www.bls.gov/oes/special-requests/oesm25nat.zip (May 2025 national data file); index page https://www.bls.gov/oes/tables.htm
published:       2025-04-02 (May 2024 reference-period release, per BLS OEWS release calendar); 2026-05-15 (May 2025 reference-period release, per USDL-26-0725 press release found during search)
pull_date:       2026-09-23
pull_method:     fetch (curl download of BLS national data-file .zip, then read with openpyxl; individual narrative HTML occupation pages under /oes/2024/may/oes<code>.htm and /oes/current/oes<code>.htm now redirect to /oes/tables.htm and no longer serve per-occupation tables)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     official U.S. federal statistical survey (OEWS), full-population establishment survey with published methodology (methods_24.pdf); not an SEC-type "filing" but assigned source_label "filed" per task instruction as the closest fit — treated as tier 2 (filed) by analogy, not tier 3, since it is a compulsory government collection, not a platform's own marketing page
source_label:    filed
lane:            F
sub_market:      n/a
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        table only — rows for OCC_CODE 13-1161, 11-2021, 15-1254 (plus 11-2000 and 13-1199 captured incidentally), extracted from the "national" data file for each reference year
```

## Verbatim

All figures below are exactly as printed in the BLS OEWS national data files (`national_M2024_dl.xlsx`, `national_M2025_dl.xlsx`), AREA = 99 ("U.S."), NAICS = 000000 ("Cross-industry"), OWN_CODE = 1235. Units: `H_*` = hourly wage in USD, `A_*` = annual wage in USD. `#` is BLS's own suppression symbol, meaning the wage is at or above the tenth-decile top-coding threshold BLS uses for that release (BLS caps published hourly figures at $115.00/hr and does not publish an exact annual 90th-percentile figure above the wage-cap threshold for that cell).

### May 2024 (source file `oesm24nat.zip` → `national_M2024_dl.xlsx`)

**OCC_CODE 13-1161 — Market Research Analysts and Marketing Specialists** (O_GROUP: detailed)
- TOT_EMP = 861,140; EMP_PRSE = 0.7
- H_MEAN = 41.58; A_MEAN = 86,480; MEAN_PRSE = 0.4
- H_PCT10 = 20.23; H_PCT25 = 27.03; H_MEDIAN = 37.00; H_PCT75 = 50.42; H_PCT90 = 69.52
- A_PCT10 = 42,070; A_PCT25 = 56,220; A_MEDIAN = 76,950; A_PCT75 = 104,870; A_PCT90 = 144,610

**OCC_CODE 11-2021 — Marketing Managers** (O_GROUP: detailed)
- TOT_EMP = 384,980; EMP_PRSE = 0.8
- H_MEAN = 82.46; A_MEAN = 171,520; MEAN_PRSE = 0.6
- H_PCT10 = 39.38; H_PCT25 = 53.47; H_MEDIAN = 77.42; H_PCT75 = 101.48; H_PCT90 = # (suppressed, above wage cap)
- A_PCT10 = 81,900; A_PCT25 = 111,210; A_MEDIAN = 161,030; A_PCT75 = 211,080; A_PCT90 = # (suppressed, above wage cap)

**OCC_CODE 15-1254 — Web Developers** (O_GROUP: detailed)
- TOT_EMP = 78,860; EMP_PRSE = 2.6
- H_MEAN = 47.50; A_MEAN = 98,790; MEAN_PRSE = 1.1
- H_PCT10 = 23.35; H_PCT25 = 30.36; H_MEDIAN = 43.72; H_PCT75 = 59.76; H_PCT90 = 78.30
- A_PCT10 = 48,560; A_PCT25 = 63,140; A_MEDIAN = 90,930; A_PCT75 = 124,300; A_PCT90 = 162,870

Incidentally captured, same file, OCC_CODE 11-2000 — Advertising, Marketing, Promotions, Public Relations, and Sales Managers (O_GROUP: minor): TOT_EMP = 1,122,770; A_MEDIAN = 144,530; A_PCT10 = 73,320; A_PCT25 = 100,740; A_PCT75 = 204,920; A_PCT90 = # (suppressed).
Incidentally captured, OCC_CODE 13-1199 — Business Operations Specialists, All Other: TOT_EMP = 1,128,200; A_MEDIAN = 81,270; A_PCT10 = 46,230; A_PCT25 = 60,820; A_PCT75 = 110,030; A_PCT90 = 147,830.

### May 2025 (source file `oesm25nat.zip` → `national_M2025_dl.xlsx`)

**OCC_CODE 11-2021 — Marketing Managers**
- TOT_EMP = 395,240; EMP_PRSE = 0.8
- H_MEAN = 85.47; A_MEAN = 177,770; MEAN_PRSE = 0.3
- H_PCT10 = 43.39; H_PCT25 = 59.15; H_MEDIAN = 80.19; H_PCT75 = 104.04; H_PCT90 = 141.16
- A_PCT10 = 90,260; A_PCT25 = 123,020; A_MEDIAN = 166,790; A_PCT75 = 216,410; A_PCT90 = 293,610

**OCC_CODE 13-1161 — Market Research Analysts and Marketing Specialists**
- TOT_EMP = 899,580; EMP_PRSE = 0.8
- H_MEAN = 43.03; A_MEAN = 89,490; MEAN_PRSE = 0.5
- H_PCT10 = 20.86; H_PCT25 = 28.05; H_MEDIAN = 37.87; H_PCT75 = 52.07; H_PCT90 = 74.75
- A_PCT10 = 43,390; A_PCT25 = 58,350; A_MEDIAN = 78,760; A_PCT75 = 108,310; A_PCT90 = 155,480

**OCC_CODE 15-1254 — Web Developers**
- TOT_EMP = 70,190; EMP_PRSE = 6.7
- H_MEAN = 47.49; A_MEAN = 98,770; MEAN_PRSE = 1.5
- H_PCT10 = 23.12; H_PCT25 = 30.88; H_MEDIAN = 44.54; H_PCT75 = 60.69; H_PCT90 = 78.03
- A_PCT10 = 48,100; A_PCT25 = 64,230; A_MEDIAN = 92,650; A_PCT75 = 126,230; A_PCT90 = 162,290

No BLS SOC code exists for GEO, AEO, "generative engine optimization" or "answer engine optimization" — these titles do not appear anywhere in the SOC 2018 taxonomy underlying OEWS. The closest matches are 13-1161 (Market Research Analysts and Marketing Specialists, which folds in most "SEO specialist" postings) and 11-2021 (Marketing Managers). [note: BLS narrative text describing which job titles map into 13-1161 was not separately captured in this pull — only the wage table rows.]

## Pull notes — mechanical only

- The individual narrative occupation pages that formerly existed at `/oes/<year>/may/oes<occ-code>.htm` and `/oes/current/oes<occ-code>.htm` (e.g. `oes131161.htm`, `oes112021.htm`, `oes151254.htm`) now 301-redirect to `/oes/tables.htm` (and in one case to `/oes/home.htm`) — confirmed via `curl -sL` on 2026-09-23. WebFetch on the old-style URLs likewise returned only the OEWS homepage/table-index content, not occupation data.
- `/oes/tables.htm` lists the downloadable national/state/metro/industry `.zip` data files by year (oesm25nat.zip, oesm24nat.zip, oesm23nat.zip … back to oesm21nat.zip); the 2023 vintage is the last year with an HTML `oes_nat.htm` narrative page still linked.
- Downloaded `oesm24nat.zip` (282,052 bytes) and `oesm25nat.zip` (279,525 bytes) directly via curl, 200 status both. Each unzips to a single file: `national_M2024_dl.xlsx` / `national_M2025_dl.xlsx`, 1,404 and comparable data rows, 32 columns.
- Read via Python (openpyxl, installed this session with `pip install --break-system-packages openpyxl`) filtering `OCC_CODE` in the target set; no manual transcription of numbers, values copied directly from cell output.
- `MEAN_PRSE` / `EMP_PRSE` are BLS's own relative standard error columns, carried through verbatim as reliability indicators.
- No UK ONS ASHE pull attempted in this file — not reached this session; would need a separate pull.
