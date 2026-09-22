# Oruesagasti / Interamplify (arXiv) — Algorithmic Trust and Compliance: Benchmarking Brand Notability for UK iGaming Entities in Generative Search Engines

```yaml
source:          Julen Oruesagasti; "Technical Report. Produced by Interamplify Research Division (UK)"
url_or_doc_id:   arxiv.org/abs/2603.12282
published:       2026-03-05
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-authored — Comments field states "Produced by Interamplify Research Division (UK)" — academic table row "vendor-authored," bias flagged; also no original empirical testing (see Pull notes)
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT (Bing integration), Google Gemini (Search Generative Experience), Perplexity AI — named as the systems examined, but the report does not run its own tests against them
metric_kind:     visibility
supersedes:      none
captured:        abstract, methodology assessment, results figures, code/data-release check (via arxiv.org/html/2603.12282 full-text extraction)
technique:       corpus seeding adjacent — compliance and regulatory-licensing signals (UK Gambling Commission standards), structured as machine-readable data, framed as an "authority multiplier" for earned-media citation in a regulated vertical
models_tested:   not independently tested by this report; it cites secondary figures attributed to "Aggarwal, Muralidhar, and Nagar (2024)" (see Pull notes on author-list discrepancy)
date_window:     not documented for any original iGaming-brand testing; the cited secondary study's own window is not restated here
measured_effect: yes, but secondary — Cite Sources +40% (p<0.01), Statistics Addition +37% (p<0.01), Quotation Addition +22% (p<0.05), Keyword Stuffing +3% (not significant); brand-owned content "fewer than 15-20% of total citations" — no original iGaming-brand measurement reported
vertical:        iGaming (UK gambling/online gaming) — not one of the three fixed verticals in docs/method/plan.md (skincare and beauty; B2B SaaS; high-CPA regulated — cards, insurance, supplements, loans, personal injury); recorded as the source names it, not mapped to "high-CPA regulated" by inference
```

## Verbatim

### Abstract

"The rapid adoption of generative AI-powered search engines—such as ChatGPT, Perplexity, and Google Gemini—is fundamentally reshaping information retrieval paradigms. This report presents an empirical analysis of how compliance signals—including UK Gambling Commission (UKGC) licensing standards—function as authority multipliers for LLMs when properly structured as machine-readable data. Recent large-scale experiments reveal that AI search exhibits a systematic and overwhelming bias towards earned media (third-party, authoritative sources) over brand-owned content."

### Methodology assessment

The document does not present original empirical testing of iGaming brands. It synthesizes prior research, primarily citing a study attributed to "Aggarwal, Muralidhar, and Nagar (2024)," which it states "evaluated nine distinct optimization strategies across approximately 10,000 queries." No date window or controlled testing of specific iGaming brands is documented in this report.

### Results figures (as cited by this report)

"Cite Sources strategy: +40% visibility improvement (p < 0.01)." "Statistics Addition: +37% improvement (p < 0.01)." "Quotation Addition: +22% improvement (p < 0.05)." "Keyword Stuffing: +3% (negligible, not significant)." Brand-owned content comprises "fewer than 15–20% of total citations."

### Limitations

None present — the report defines scope boundaries but contains no dedicated limitations section.

### Code/data/prompt release

None stated.

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2603.12282 for metadata, arxiv.org/html/2603.12282 for full text), both 200.
- Author-attribution discrepancy, recorded mechanically and not resolved by this pull: this report cites the foundational GEO study's headline figures (nine strategies, ~10,000 queries, ~40% visibility boost) under the author list "Aggarwal, Muralidhar, and Nagar (2024)." The actual foundational paper pulled separately in this cluster (`d-seeding-geo-foundational-2026-09-22.md`, arXiv:2311.09735) lists its authors as Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande — a different author list and no author named "Nagar." Both citing strings are recorded verbatim; no attempt made here to correct or reconcile them.
- Vertical fit: "iGaming" (UK online gambling) is the vertical this report itself names. It is not identical to any of the three fixed verticals in `docs/method/plan.md`; it is closest in kind to "high-CPA regulated" (heavily regulated, compliance-driven, high customer-acquisition cost) but is recorded here as its own named vertical, per `docs/sources/query-book.md`'s cell-attribution rule that a source is assigned only to a vertical it itself names.
