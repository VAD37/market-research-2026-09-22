# Disclosed price actually paid — skincare and beauty buyer, AI-visibility/GEO tooling or services

```yaml
source:          cross-check of channels already pulled by this cluster (EDGAR full-text search, GR0 case study, OMR Rankscale.ai review) plus one new targeted EDGAR sweep
url_or_doc_id:   efts.sec.gov/LATEST/search-index (entityName-scoped queries against named AI-visibility vendors); see also f-signal-sk-S6, f-signal-sk-S4, f-signal-sk-S7 in this same cluster for the underlying sources re-checked
published:       n/a — negative-result compilation
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default per demand-signals.md S11 ("2 filed") for the EDGAR sweep method; no qualifying figure was found at any tier, so no tier is assigned to a number
source_label:    filed
lane:            F
sub_market:      n/a — no qualifying observation in any sub-market
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        EDGAR full-text search API JSON results (hit counts and one opened hit's metadata); cross-reference notes against three other raw files in this cluster
```

## Query — verbatim

EDGAR full-text search, `entityName`-scoped to five named beauty filers (Estee Lauder, elf Beauty, Ulta Beauty, Coty Inc, L'Oreal), each queried for seven named AI-visibility vendor names (Profound, Scrunch, Otterly, Ahrefs, Semrush, Peec, Rankscale) — 35 queries, run 2026-09-22:

- Two non-zero hits: "Estee Lauder" × "Profound" (3 hits), "Ulta Beauty" × "Profound" (1 hit). All other 33 combinations returned 0.
- The one Ulta Beauty hit opened: an 8-K exhibit (`tm252061d1_ex99-1.htm`, accession 0001104659-25-001305), filed 2025-01-06 — a date that pre-dates this pull's date-rule window (`query-book.md`'s "published 2026" default and the one-quarter staleness cutoff of 2026-06-22) and pre-dates most of this category's public activity per `scope.md`'s "category is roughly two years old as of 2026-09" framing. Not opened further this pull; treated as very likely a coincidental match on the common English word "profound" (e.g., in a phrase like "profound impact"), not the AI-visibility vendor Profound — **not verified either way**, recorded as an open item rather than a finding.

Cross-referenced against sources already opened elsewhere in this cluster: the Coty Inc. 10-K passage (`f-signal-sk-S7-coty-10k-2026-09-22.md`) names no vendor and no price. The GR0 luxury-skincare-brand case study (`f-signal-sk-S6-gr0-agency-case-studies-2026-09-22.md`) names Profound as a measurement tool but discloses no fee paid by the client to either GR0 or Profound, and does not name the client. The OMR Rankscale.ai review from a Cosmetics-industry reviewer (`f-signal-sk-S4-omr-reviews-2026-09-22.md`) discloses Rankscale.ai's own list price ("Prices start at €20 per month") but not what the reviewer's employer (Marcvs Group) actually pays — a list price is explicitly excluded from S11 per `demand-signals.md` and `templates/customer-segment.md` ("a vendor list price is not a willingness-to-pay observation").

## Verbatim

EDGAR hit metadata, the one item opened (Ulta Beauty × "Profound"):

```json
{"ciks":["0001403568"],"period_ending":"2025-01-06","display_names":["Ulta Beauty, Inc.  (ULTA)  (CIK 0001403568)"],"root_forms":["8-K"],"file_date":"2025-01-06","biz_states":["IL"]}
```

No dollar figure, contract value, or service fee tied to any AI-visibility vendor and any skincare-or-beauty buyer was found by any query in this file or by cross-reference to this cluster's other raw pulls.

## Pull notes — mechanical only

- This is a negative-result compilation drawing on one new targeted sweep (35 EDGAR entityName × vendor-name queries) plus cross-references to three other files already produced in this cluster, rather than a single new page pull.
- The one ambiguous EDGAR hit (Ulta Beauty × "Profound", 2025-01-06 8-K exhibit) was not opened to resolve the ambiguity, given its pre-2026-06-22 date would in any case require a staleness re-check before use, and the seven-vendor / five-filer sweep's near-total-zero pattern already supports a `none` reading for this signal.
- No procurement, court-docket (C62), or DSA ad-repository (C60) channel was separately re-checked for a price-paid figure in this file — `f-signal-sk-S10-procurement-2026-09-22.md` (same cluster) already covers the procurement channels and found no genuine beauty-AI-visibility record of any kind, which would preclude a price figure existing there.
- Result for S11 across all nine skincare-and-beauty cells: `none — checked EDGAR full-text search (35 entityName × vendor-name queries), GR0 case study, OMR Rankscale.ai review, Coty Inc. 10-K, sam.gov/contractsfinder/ted.europa.eu (per f-signal-sk-S10) 2026-09-22`.
