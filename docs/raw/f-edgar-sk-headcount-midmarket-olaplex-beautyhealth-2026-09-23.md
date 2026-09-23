# SEC EDGAR 10-K — headcount, OLAPLEX Inc. and The Beauty Health Company (Hydrafacial), FY2025

```yaml
source:          U.S. Securities and Exchange Commission, EDGAR — OLAPLEX Holdings, Inc. (NASDAQ: OLPX, CIK 0001868726) and The Beauty Health Company (NASDAQ: SKIN, CIK 0001818093)
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1868726/000186872626000009/olpx-20251231.htm ; https://www.sec.gov/Archives/edgar/data/1818093/000162828026017376/skin-20251231.htm
published:       2026-03-05 (Olaplex 10-K, FY ended 2025-12-31); 2026-03-12 (Beauty Health 10-K, FY ended 2025-12-31)
pull_date:       2026-09-23
pull_method:     fetch (curl, data.sec.gov/submissions JSON to find accession, then sec.gov/Archives direct document; no efts.sec.gov full-text search used)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed (10-K "Human Capital Resources" section)
source_label:    filed
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        "Employees" subsection of "Human Capital Resources" / "Human Capital" item in each 10-K, full-text extracted
```

## Verbatim

> "Employees As of December 31, 2025, Olaplex employed 278 employees and leveraged contractors..." — OLAPLEX Inc. 10-K (FY2025, filed 2026-03-05), Item 1 Human Capital Resources.

> "As of December 31, 2025, we employed 613 employees..." — The Beauty Health Company 10-K (FY2025, filed 2026-03-12), Human Capital Resources. Geographic breakout on the same page: "United States of America 414 67% Asia-Pacific (APAC) 30 5% Europe, Middle East, and Africa (EMEA) [remainder]"; "As of December 31, 2025, 187 of these employees were based in our Long Beach, California headquarters." "None of our employees are represented by a labor organization..."

## Buyer-size mapping

Per `docs/method/demand-signals.md` "Buyer-size boundaries": headcount is primary, proxy order filing > company's own site > professional-network profile. Both figures are filed 10-K headcounts, the strongest available proxy.

| Company | Filed headcount, date | Band (100–999 headcount) |
|---|---|---|
| OLAPLEX Inc. (NASDAQ: OLPX) | 278, as of 2025-12-31 | **Mid-market** |
| The Beauty Health Company / Hydrafacial (NASDAQ: SKIN) | 613, as of 2025-12-31 | **Mid-market** |

Both companies sell skincare/haircare (Olaplex: haircare) and skin-health devices (Beauty Health: Hydrafacial, SkinStylus) direct to consumer and through professional/retail channels — both fall inside this vertical's definition in `docs/customers/skincare-beauty.md` ("Skincare, colour cosmetics, fragrance, haircare — brands and beauty retailers").

## Pull notes — mechanical only

- `efts.sec.gov` full-text search was not used (named in the task brief as liable to 403); instead `data.sec.gov/submissions/CIK##########.json` was fetched to list each company's 10-K filing history and accession numbers, then the primary document was fetched directly from `www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<primary-doc>.htm`. Both requests succeeded on the first attempt, HTTP 200, no wall.
- Both 10-K bodies were also scanned for "generative engine", "answer engine", "AEO", "GEO ", "AI search", "AI visibility", "large language model", "ChatGPT", "generative AI". Olaplex's only match is one generic risk-factor sentence: "The introduction of new technologies such as generative AI and automated decision-making tools may create new categories of operational, compliance, and cybersecurity risks..." — no marketing, visibility or recommendation framing. Beauty Health's only match: "We are implementing the use of AI solutions, including machine learning and generative AI tools that collect, aggregate, and analyze data to assist in the development of our products and in the use of internal tools..." — internal-tooling framing, not marketing. Neither 10-K names GEO, AEO, AI search visibility or brand recommendation by AI assistants anywhere in the document (S7: checked, nothing found for either company).
- No login, no paywall, no CAPTCHA.
