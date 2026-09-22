# P4-c1 cross-reference — S7, high-CPA regulated cases already landed by the earnings-call cluster

```yaml
source:          docs/raw/e-case-census-c1-2026-09-22.md and the three raw pulls it cites for NerdWallet, LendingTree, EverQuote (this repo, cross-referenced, not re-pulled)
url_or_doc_id:   docs/raw/e-case-census-c1-2026-09-22.md ; docs/raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md ; docs/raw/e-case-lendingtree-10k-2026-03-09-2026-09-22.md ; docs/raw/e-case-everquote-investor-deck-2026-08-03-2026-09-22.md
published:       2026-09-22 (all four files, this repo)
pull_date:       2026-09-22
pull_method:     cross-reference (read of this repo's own already-landed raw/ files; not a fresh external pull)
pull_purpose:    evidence about a number
tier:            n/a — this file inherits, and does not alter, the tiers already assigned in the cited raw files (Silver-graded NerdWallet at tier per that file's own header; LendingTree and EverQuote graded "statement only")
tier_reason:     see cited files
source_label:    filed (NerdWallet, LendingTree are SEC filings/exhibits; EverQuote is an 8-K exhibit investor deck)
lane:            E, F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     traffic, sales (NerdWallet); none (LendingTree, EverQuote — qualitative risk-factor/opportunity language, no figure)
supersedes:      none
captured:        summary cross-reference only — the task instructs "cite the P4-c1 raw files," not re-pull them; this file states what each contributes to the S7 row of the high-CPA-regulated cell matrix and points at the exact raw path for the verbatim
vertical:        high-CPA regulated — credit cards, insurance, loans (NerdWallet, LendingTree); insurance (EverQuote)
cell:            organic recommendation / unassigned — none of the three names its own buyer-size band in the passages `e-case-census-c1` captured
query:           n/a — cross-reference, not a fresh query
```

## What each contributes

**NerdWallet, Inc. (NRDS)** — 8-K Ex-99.1, Q4 FY25 earnings release, 2026-02-25. Per `e-case-census-c1-2026-09-22.md`'s candidate table: "Credit cards revenue of $26.5 million decreased 24% year-over-year, primarily due to continued headwinds in organic search traffic"; "Insurance revenue ... increased 13%" (offsetting direction). Graded **Silver** — the only high-CPA-regulated case that cleared the evidence bar at Bronze-or-better in that cluster's screen, and the only high-CPA-regulated case at Silver across P4-c1's entire 64-candidate screen. Vertical is stated directly by the source ("credit cards", "insurance" as named segment lines) — this is the strongest single S7 data point for this vertical to date across the repo. Raw: `docs/raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md`.

**LendingTree, Inc. (TREE)** — 10-K FY2025, filed 2026-03-09. Risk-factor language: "organic searches and artificial intelligence ('AI') overviews, that depend upon the searchable content on our sites." Graded **statement only** (no figure, no baseline). Per `e-case-census-c1`'s own caveat, the vertical tag is withheld here (`none named`) under the Pass 4 tagging rule — the passage itself does not name "loans" or "credit" as the affected vertical, even though LendingTree is a loan/credit marketplace by business description; the strict per-source-statement tagging rule in `plan.md`'s per-vertical tagging addition forbids inferring the tag from outside knowledge of the filer's business. Recorded here as high-CPA-regulated-**adjacent**, not vertical-tagged, consistent with the source file. Raw: `docs/raw/e-case-lendingtree-10k-2026-03-09-2026-09-22.md`.

**EverQuote, Inc. (EVER)** — 8-K Ex-99.2, Q2 2026 investor deck, 2026-08-03. "Consumer adoption of AI adds new sources of high-intent traffic" (ChatGPT listed as a channel, no figure attached). Graded **statement only**. Same vertical-tagging caveat as LendingTree: EverQuote is an insurance marketplace by business description, but the passage itself names no vertical, so it is recorded `none named` per the strict tagging rule, not assigned to "insurance" by inference. Raw: `docs/raw/e-case-everquote-investor-deck-2026-08-03-2026-09-22.md`.

## S7 result, high-CPA regulated, combining this cross-reference with the fresh Primerica finding

Three filed/company-stated data points cross-referenced from P4-c1 (NerdWallet Silver, LendingTree statement-only, EverQuote statement-only), plus one new tier-2 filed finding this cluster (Primerica — see `f-signal-hr-S7-primerica-10k-2026-09-22.md`). NerdWallet is the strongest: it is both vertical-tagged by its own source language and carries an actual revenue figure with a stated direction and cause ("credit cards revenue ... decreased 24% ... due to continued headwinds in organic search traffic"). This is the single highest-tier, most-specific S7 finding for this vertical across the repo as of 2026-09-22.

## Caveats

- This file adds no new fact beyond what `e-case-census-c1` already states; it exists to satisfy the task's instruction to route S7 through a citation of that cluster rather than a duplicate re-pull, and to state explicitly what it contributes to the nine-cell matrix in `f-signal-census-hr-2026-09-22.md`.
- `e-case-census-c1`'s own caveats note that of ten cleared/graded cases in that cluster, only NerdWallet carries both a named vertical and a figure — the other two high-CPA-regulated-adjacent filers (LendingTree, EverQuote) are withheld from vertical tagging on a strict reading of the tagging rule, which this file preserves rather than loosens.
