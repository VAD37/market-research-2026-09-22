# arXiv (Olivier Martinez) — critical survey, no reviewed GEO technique shows a stable causal effect

```yaml
source:          arXiv preprint, author Olivier Martinez
url_or_doc_id:   https://arxiv.org/abs/2607.14035
published:       2026-07-15 (v1 submission, "Wed, 15 Jul 2026 17:03:08 UTC")
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     Trust-rubric.md academic table: "Preprint without code" = tier 5. The paper's comments field states it includes "ancillary literature matrix and search protocol" — a method appendix — which raises trust per trust-rubric.md's general bullet ("Trust rises when... method appendix is published") without itself changing the tier row, since no code or dataset link is stated in the metadata captured this pull.
source_label:    analyst-derived
lane:            E
sub_market:      organic recommendation
engine:          n/a at the survey's own top level — the paper synthesizes 45 underlying studies (November 2023–July 2026 publication window) that between them span many engines and model versions; no single engine is this paper's own subject
metric_kind:     visibility
vertical:        none named
evidence_grade:  not graded (per grading rule 1: a case missing items 1, 4 and 5 of the seven-item bar is Bronze at best; here items 1 (single brand/profile), 4 (one stated baseline) and 5 (one stated intervention) do not apply at all, because this is a meta-analysis of 45 separate studies rather than a single case — the same shape mismatch this cluster's precedent files (`docs/raw/e-case-census-c2-2026-09-22.md` candidate #4, Foundation Inc's aggregate citation-fingerprint research) record as "not graded — aggregate research, not a single-brand case" rather than forcing a Gold/Silver/Bronze/Fools-gold label onto a shape the bar was not built for. Recorded here for its central finding, which is directly on point for H5 ("Corpus seeding measurably moves an answer" — kill condition: "No Pass 5 technique with published before-and-after") and for the survivorship framing of this cluster.
direction:       negative / null
vendor_named:    none — independent academic survey; no GEO/AI-visibility vendor's product is the subject
supersedes:      none
captured:        abstract, authors/comments/subjects metadata, submission history from the arXiv abstract page only. [note: the 18-page paper's body (per its own comments field: "18 pages, 8 tables, 1 figure") was not fetched or captured this pull — only the abstract page was read]
```

## Verbatim

### Title, author (arXiv abstract page)

> Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)
>
> Authors: Olivier Martinez

### Comments field

> 18 pages, 8 tables, 1 figure; critical survey of 45 studies; ancillary literature matrix and search protocol included

Subjects: Information Retrieval (cs.IR); Digital Libraries (cs.DL). Submission history: v1, Wed, 15 Jul 2026 17:03:08 UTC (42 KB).

### Abstract (verbatim)

> Generative Engine Optimization (GEO) seeks to increase content's presence, likelihood of citation, or influence in answers produced by generative engines. Since the foundational GEO paper, the field has expanded rapidly, but terminology, metrics, and evidence standards remain heterogeneous. This critical survey reviews 45 studies selected under a November 2023-July 2026 publication window, including one earlier preprint published at EMNLP after the window opened, plus relevant RAG and evaluation work. We argue that GEO is not a single ranking task but a stochastic, partially observable pipeline spanning search activation, crawling and indexing, retrieval, reranking and context allocation, citation, prominence, factual absorption, fidelity, and user behavior. The foundational paper's widely cited gains are valid within its experimental setting but conditional on a source already being present in a fixed context; they establish neither organic discoverability nor durable traffic effects. Reviewed work indicates that topical relevance and context position are the most reproducible levers, generic heuristics transfer poorly, competition can erode individual gains, and citation-oriented rewrites can impair retrieval. Commercial audits further reveal low source overlap, substantial run-to-run variability, and persistent fidelity gaps. We contribute a multistage formal model, a visibility vector separating discoverability, citation, absorption, and economic outcomes, an evidence hierarchy, and a reproducible protocol based on repeated measurements, paraphrases, controls, human validation, and multi-actor interference. Within this corpus, the evidence is narrow: already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior.

## Pull notes — mechanical only

- Pulled from `https://export.arxiv.org/abs/2607.14035` (301 redirect from the plain-HTTP `export.arxiv.org` host to HTTPS, followed). Only the abstract-page metadata was fetched this pull; the paper's own HTML full-text render (`arxiv.org/html/2607.14035v1` or similar) was not fetched — time budget for this cluster was directed at the higher-priority TW3 Partners/Citead paper's body sections instead.
- The abstract's final sentence — "no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior" — is the load-bearing line for this file and is quoted exactly as printed on the arXiv abstract page.
- No browser extension needed; plain fetch sufficient.
