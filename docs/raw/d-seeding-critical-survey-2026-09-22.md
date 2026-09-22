# Martinez (arXiv) — Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023–2026)

```yaml
source:          Olivier Martinez
url_or_doc_id:   arxiv.org/abs/2607.14035; full text also fetched at arxiv.org/html/2607.14035v1
published:       2026-07-15
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; no code/data release, and no statement of a prompt set (this is a literature survey, not an original experiment) — academic table row "preprint without code"; the paper does state "ancillary literature matrix and search protocol included" as a method appendix, which raises trust per trust-rubric.md "Trust rises when... method appendix is published," but does not meet the "code and prompt set" bar for tier 4
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a (survey of 45 studies spanning multiple engines; no original engine testing by this paper)
metric_kind:     none
supersedes:      none
captured:        abstract (via arxiv.org/html/2607.14035v1 extraction), measured-effect assessment, engine-countermeasure check
technique:       meta-evidence on the technique category as a whole — directly addresses Pass 5 question (3), "whether any measured evidence shows it moving an answer," at the level of the whole literature rather than one paper
models_tested:   n/a — survey; underlying 45 studies each carry their own models, not itemized in this pull
date_window:     "November 2023–July 2026 publication window, including one earlier preprint published at EMNLP after the window opened"
measured_effect: no (this is the survey's own headline finding) — "already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior"
vertical:        not vertical-specific (survey of the literature as a whole)
```

## Verbatim

### Abstract

"Generative Engine Optimization (GEO) seeks to increase content's presence, likelihood of citation, or influence in answers produced by generative engines. Since the foundational GEO paper, the field has expanded rapidly, but terminology, metrics, and evidence standards remain heterogeneous. This critical survey reviews 45 studies selected under a November 2023–July 2026 publication window, including one earlier preprint published at EMNLP after the window opened, plus relevant RAG and evaluation work. We argue that GEO is not a single ranking task but a stochastic, partially observable pipeline spanning search activation, crawling and indexing, retrieval, reranking and context allocation, citation, prominence, factual absorption, fidelity, and user behavior. The foundational paper's widely cited gains are valid within its experimental setting but conditional on a source already being present in a fixed context; they establish neither organic discoverability nor durable traffic effects. Reviewed work indicates that topical relevance and context position are the most reproducible levers, generic heuristics transfer poorly, competition can erode individual gains, and citation-oriented rewrites can impair retrieval. Commercial audits further reveal low source overlap, substantial run-to-run variability, and persistent fidelity gaps."

### Measured-effect assessment (extracted passage)

"Surfaces Do Not Share the Same Sources" — "53% of domains cited by Google AIO do not appear in the organic top 10." Across commercial engines audited, "only 26% were cited by both systems."

Headline finding on causal evidence: "already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior."

### Engine countermeasures

Not addressed by this paper's abstract or the extracted passages — the survey documents the state of GEO research, not engine policy responses. Recorded as `unknown — checked arxiv.org/abs/2607.14035 and arxiv.org/html/2607.14035v1 2026-09-22`, not asserted as an absence in the underlying literature generally.

### Comments field

"18 pages, 8 tables, 1 figure; critical survey of 45 studies; ancillary literature matrix and search protocol included"

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2607.14035 for metadata and Comments field, arxiv.org/html/2607.14035v1 for abstract and body passages), both 200.
- Foundational-paper cross-reference: this survey's characterization of the foundational GEO paper's gains as "conditional on a source already being present in a fixed context" is recorded here as this survey's own stated critique. The foundational paper itself is pulled separately at `d-seeding-geo-foundational-2026-09-22.md` (arXiv:2311.09735); the two are not reconciled here, only cited side by side.
- Section 9.1, on distinguishing "white-hat" from adversarial GEO approaches by "semantic preservation" and "evidentiary authenticity," was checked for third-party seeding tactics during an earlier search pass on this same source and found not to address them; not re-quoted here as it falls outside the four passages captured above.
