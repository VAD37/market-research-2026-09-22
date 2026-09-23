# TED Search API v3 and UK Contracts Finder — S10 procurement: paid-placement and agentic-commerce terms, buyer country of every hit

```yaml
source:          TED — Tenders Electronic Daily, Search API v3 (api.ted.europa.eu, anonymous); UK Contracts Finder REST API v2 (contractsfinder.service.gov.uk, anonymous)
url_or_doc_id:   POST https://api.ted.europa.eu/v3/notices/search {"query":"FT~\"<term>\"","scope":"ALL","limit":50,"fields":["publication-number","buyer-name","buyer-country","notice-title","publication-date"]} — 20 terms ; POST https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json {"searchCriteria":{"keyword":"\"<term>\""},"size":20} — 12 terms
published:       TED notices 2016-09-22 to 2026-08-03 (publication-date per notice); Contracts Finder notices 2025-02-03 to 2026-07-07
pull_date:       2026-09-23
pull_method:     fetch (Python urllib POST, JSON; 3 s between TED calls, 2 s between Contracts Finder calls)
pull_purpose:    evidence about a number (S10 per country, paid placement and agentic commerce)
tier:            2
tier_reason:     filed procurement records, table default for S10 (demand-signals.md "2 filed"); counts and fields as the registers return them; no notice XML opened (WAF-walled on curl per docs/raw/f-ted-S10-repull2-2026-09-23.md)
source_label:    filed
lane:            F
sub_market:      paid placement; agentic commerce
engine:          n/a
metric_kind:     none
supersedes:      none (extends docs/raw/f-ted-ukcf-S10-eu-country-brand-accuracy-2026-09-23.md, which holds the organic-term and "Perplexity" counts)
captured:        totalNoticeCount per term; every hit for the category terms (publication-number | buyer-country | publication-date | buyer-name | notice-title English label); country tally of the first 50 hits for the broad terms
```

## TED — counts, 20 terms, all HTTP 200

| Term sent as `FT~"<term>"` | totalNoticeCount | Buyer countries (first 50 hits) |
|---|---|---|
| ChatGPT Ads | 0 | — |
| AI advertising | 0 | — |
| sponsored answers | 0 | — |
| KI-Werbung | 0 | — |
| publicité IA | 4 | ROU 4 (Romanian notices: electrical installation repair 2021, photocopier paper 2022, railway works ×2 2025 — the term matched unrelated text) |
| pubblicità IA | 0 | — |
| publicidad IA | 0 | — |
| Copilot | 351 | FRA 25, ROU 8, DEU 4, ESP 3, PRT 3, POL 3, HUN 2, NLD 2 of the first 50 — aircraft, hospital-software and generic IT notices; first hits dated 2016–2017 |
| agentic commerce | 1 | DEU 1 |
| Instant Checkout | 0 | — |
| agentic checkout | 0 | — |
| commerce agentique | 2 | FRA 2 |
| comercio agéntico | 0 | — |
| commercio agentico | 0 | — |
| agentic | 154,055 | mixed (token matches "agent", "agency"; first 50 hits dated 2016-09) |
| ChatGPT | 60 | DEU 15, ROU 7, EST 6, GRC 5, BEL 4, SVN 4, NOR 3, AUT 3, NLD 2, ESP 2, POL 2, FIN 1, ISL 1 of the first 50 |
| Perplexity Ads | 0 | — |
| conversational advertising | 0 | — |
| AI Overviews | 1 | DEU 1 |
| agentic AI | 66 | BEL 17, ITA 7, ROU 6, DEU 5, NLD 5, LVA 3, ESP 2, LUX 2, DNK 2, GRC 1 of the first 50 |

## Verbatim — every hit on the category terms

`FT~"agentic commerce"`, 1 notice:
```
431874-2026 | ['DEU'] | 2026-06-25 | Rheinland-Pfalz Tourismus GmbH | Germany – World wide web (www) site operation host services – Relaunch, Betrieb und Hosting der Websites
```

`FT~"commerce agentique"`, 2 notices:
```
334749-2017 | ['FRA'] | 2017-08-25 | Collectivité territoriale de Corse | France-Ajaccio: Training services
304103-2019 | ['FRA'] | 2019-07-01 | Région Bourgogne-Franche-Comté | France-Besançon: Training services
```
[note: both French hits predate the category (2017, 2019) and are training-services notices; the phrase match is on unrelated text.]

`FT~"AI Overviews"`, 1 notice:
```
366557-2026 | ['DEU'] | 2026-05-28 | NRW.BANK AöR | Germany – Business services: law, marketing, consulting, recruitment, printing and security – RV Corporate Publishing Lo…
```

`FT~"ChatGPT"` — the NLD and ESP hits among the first 50:
```
772843-2023 | ['NLD'] | 2023-12-20 | Provincie Utrecht | Netherlands – Project-management services other than for construction work – Projectondersteuning digitalisering overhed…
545942-2024 | ['NLD'] | 2024-09-11 | Provincie Utrecht | same title family
311877-2025 | ['ESP'] | 2025-05-15 | Gerencia umivale Activa, Mutua Colaboradora con la Seguridad Social número 3 | Spain – IT services: consulting, software development, Internet and support – Servicio para el uso de las licencias Chat…
503020-2025 | ['ESP'] | 2025-07-31 | same buyer | same title family
```
FRA, ITA, GBR: 0 among the first 50 `ChatGPT` hits.

`FT~"agentic AI"` — the ITA, NLD and ESP hits among the first 50 are Europol, EMA, EFSA and EUIPO notices dated 2017–2022 (legal, medical and interim-staff services); the phrase match is on "agency"/"agent" text, not on the category.

## UK Contracts Finder — call log and counts, 12 terms, all HTTP 200

| keyword sent (quoted) | hitCount | Hits |
|---|---|---|
| "ChatGPT ads" | 0 | — |
| "AI advertising" | 0 | — |
| "sponsored answers" | 0 | — |
| "agentic commerce" | 0 | — |
| "Instant Checkout" | 0 | — |
| "agentic checkout" | 0 | — |
| "AI ads" | 0 | — |
| "Copilot ads" | 0 | — |
| "Perplexity" | 0 | — |
| "AI Overviews" | 0 | — |
| "ChatGPT" | 2 | OFCOM — "Future Consumers", published 2026-04-09, valueLow 87000, Awarded; NATIONAL NUCLEAR LABORATORY LIMITED — "Early Careers Online Assessments", 2025-02-03, valueLow 90000, Closed |
| "agentic" | 8 | Financial Conduct Authority — "Development support for Agentic AI", 2026-07-07, 600000–650000, Awarded; Home Office — "Co Pilot Agentic Stack Design and Development.", 2026-07-02, 3000000, Awarded; Home Office — "Co Pilot and Agentic Stack Business Change, Adoption & Assurance", 2026-07-02, 3000000, Awarded; Pension Protection Fund — "Agentic AI Development Services", 2026-06-22, 72000, Awarded; OFFICE FOR STANDARDS IN EDUCATION, CHILDRENS SERVICES AND SKILLS — "Agentic AI Support", 2026-01-19, 78000, Awarded; Central London Community Healthcare NHS Trust — "People Services Enterprise Platform", 2026-02-25, 0, Closed; DSIT — "AI Search Tools and the Future of the World Wide Web", 2026-01-29, 0–20000, Awarded; Home Office — "Discovery - Use Cases for AI Solution", 2025-12-19, 236268, Awarded |

[note: values are the register's valueLow / valueHigh fields in GBP as returned; the eight "agentic" hits are public-sector AI development and research contracts, none naming advertising, checkout or a consumer assistant as a sales surface.]

## Pull notes — mechanical only

- TED: 20 POST calls, all answered anonymously with HTTP 200; non-ASCII terms were sent as UTF-8 JSON (an earlier curl attempt with shell-escaped accents returned HTTP 400 on "publicité IA" and "comercio agéntico" and was discarded). buyer-country is the API's ISO-3 list per notice; the country tallies count each listed buyer of the first 50 hits (limit 50), not all hits.
- Contracts Finder: 12 POST calls, HTTP 200; noticeList item fields id, organisationName, title, publishedDate, valueLow, valueHigh, noticeStatus reproduced; facet blocks not reproduced.
