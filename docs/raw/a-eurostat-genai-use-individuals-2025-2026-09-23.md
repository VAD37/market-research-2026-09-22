# Eurostat — "Individuals - use of generative AI tools" (isoc_ai_iaiu), 2025, EU27 / DE / ES / FR / IT / NL

```yaml
source:          Eurostat, ICT usage in households and by individuals survey, dataset isoc_ai_iaiu
url_or_doc_id:   https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_ai_iaiu?format=JSON&lang=EN&time=2025&geo=UK&geo=FR&geo=ES&geo=IT&geo=NL&geo=DE&geo=EU27_2020 ; catalogue TOC row: "Individuals - use of generative AI tools" "isoc_ai_iaiu" dataset, last update "05.06.2026", data 2025
published:       dataset "updated" field in the JSON: 2026-06-05T11:00:00+0200; reference year 2025
pull_date:       2026-09-23
pull_method:     fetch (curl on the Eurostat dissemination API, JSON-stat 2.0); values decoded from the flat index by this pull
pull_purpose:    evidence about a number
tier:            3
tier_reason:     official statistics from the EU statistical office with a published survey methodology; not a filing (tier 2) and not a platform's own docs — held at 3, one below filed
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          n/a — the survey asks about "generative AI tools" without naming engines
metric_kind:     visibility
supersedes:      none
captured:        table only — the IND_TOTAL (all individuals) x PC_IND (percentage of individuals) slice for the four indicators; the full JSON carries ~6,000 cells across age, sex, education and other breakdowns, not reproduced
```

## Verbatim — dimension labels (from the JSON `dimension.category.label` objects)

- indic_is: `I_IUAI` "Use of generative AI tools: in the last 3 months"; `I_IUAIPR` "Use of generative AI tools: for private purposes"; `I_IUAIWP` "Use of generative AI tools: for professional (work) purposes"; `I_IUAIFE` "Use of generative AI tools: for formal education"
- unit: `PC_IND` "Percentage of individuals"; `PC_IND_IU3` "Percentage of individuals who used internet in the last 3 months"; `PC_IND_IUAI` "Percentage of individuals who have used any generative AI tools in the last 3 months"
- ind_type used here: `IND_TOTAL` "All individuals"
- geo returned: `EU27_2020` "European Union - 27 countries (from 2020)", `DE` Germany, `ES` Spain, `FR` France, `IT` Italy, `NL` Netherlands. **`UK` was requested and is absent from the response** — the United Kingdom is not in the 2025 EU survey.
- time: 2025

## Verbatim — values, All individuals, Percentage of individuals, 2025

| geo | I_IUAI (last 3 months) | I_IUAIPR (private purposes) | I_IUAIWP (work purposes) | I_IUAIFE (formal education) |
|---|---|---|---|---|
| EU27_2020 | 32.66 | 25.49 | 15.36 | 9.32 |
| DE | 32.25 | 27.2 | 15.79 | 6.04 |
| ES | 37.88 | 30.24 | 17.94 | 16.26 |
| FR | 37.46 | 27.69 | 18.44 | 10.96 |
| IT | 19.86 | 12.81 | 8.0 | 6.37 |
| NL | 44.7 | 28.07 | 26.56 | 13.1 |

## Pull notes — mechanical only

- API returned HTTP 200, 94,551 bytes, JSON-stat. Values above are read from `value[<flat index>]` with the dimension order `freq, ind_type, indic_is, unit, geo, time` and sizes from `size`; the decoding was checked on two cells against the label order.
- The catalogue TOC (`/catalogue/toc/txt?lang=en`) lists a sibling dataset `isoc_ai_iaiuxr` "Individuals - reasons for not using generative AI tools" (2025) — not pulled.
- No engine names, no monthly series, no country cut for the UK in this dataset. Eurostat's survey population is individuals aged 16–74 per the ICT survey methodology; the age boundary was not re-read from the metadata in this pull.
