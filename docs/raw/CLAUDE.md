# docs/raw/CLAUDE.md

Set 2026-09-24. How to find and read raw pulls. Rules on what raw is: `../CLAUDE.md` §raw. Raw files are never edited; this file is the only non-pull file here.

## Start here

Open `../method/snapshot-index.md` before any raw file. It sizes every lane and lane-key in words and estimated tokens, gives agents-at-budget, flags headers, and names the latest dated section of each compiled file. Per-file rows (path, lane, key, date, tokens, tier, label, cited-by, reach, audit verdict): `../method/snapshot-index.csv`. Filter the CSV, then read only the files you selected.

Stale check: index header names the last commit touching raw or compiled; if a later one exists or the tree is dirty there, re-run `python docs/method/gen-snapshot-index.py` (main thread only — it is a generated file).

Budget: raw is ~1.27M words, ~2.5M tokens estimated. No agent reads all of it. Split by lane or lane-key until each agent's selection sits under its budget.

## File names

`<lane>-<key>-<topic>[-<qualifier>]-<pull date>.md`, date = pull date `YYYY-MM-DD`.

| lane | subject |
|---|---|
| a | organic recommendation (GEO / AEO / LLMO) |
| b | paid placement, ads in assistants, filings, courts, regulation |
| c | agentic commerce |
| d | manipulation research (technique, never execution) |
| e | measurement and proof: cases, market sizes, panels |
| f | transition evidence: jobs, roles, signals, vendors |

Key = second segment: a vendor, platform or source family (`a-profound-*`, `b-openai-*`, `b-court-*`, `d-paper-*`). Compound keys: `e-case-<vendor or census cN>`, `e-market-size-*`, `f-signal-{sk,bs,hr}-S<n>-*` (segment × signal), `f-roles-*`, `f-jobboards-*`.

Qualifiers:
- `-primary-` — the original publisher's page, pulled to replace a secondary.
- `-repull<N>-` — later pull of the same source; the older file stays. Prefer the newest; cite both where figures differ.
- `-img-<date>` — transcription of images saved for the stem it names.
- `-table-`, `-census-` — pull-time aggregations across sources; tier/label may read `n/a` or `mixed`.

## Header

A fenced `yaml` block at the top: `source`, `url_or_doc_id`, `published`, `pull_date`, `pull_method`, `tier`, `tier_reason`, `source_label` (vendor-reported, analyst-derived, filed, company-stated, measured-by-us), often `lane`, `sub_market`, `pull_purpose`. Nine files have no header; the index lists them. Tier scale: `../method/trust-rubric.md`.

## Special paths

- `img/<raw-stem>/` — saved charts, image tables, PDFs; `img/INDEX.csv` maps each to its source raw and to the `-img-` file that analyses it.
- `../method/orphan-audit-2026-09-24.md` — verdict per raw file that no compiled doc cited as of 2026-09-24.

## Reading raw for a compiled claim

Cite as `raw/<file>.md`. Take numbers verbatim with their source label and date. A raw that contradicts a compiled figure is recorded side by side, never averaged.
