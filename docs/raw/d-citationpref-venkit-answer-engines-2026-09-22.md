# Venkit et al. — Search Engines in an AI Era: The False Promise of Factual and Verifiable Source-Cited Responses

```yaml
source:          Pranav Narayanan Venkit, Philippe Laban, Yilun Zhou, Yixin Mao, Chien-Sheng Wu
url_or_doc_id:   arxiv.org/abs/2410.22349; published version ACM FAccT 2025, doi:10.1145/3715275.3732089
published:       2024-10-15 (arXiv v1); ACM FAccT 2025 proceedings, pages 1325-1340
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed venue (ACM Conference on Fairness, Accountability, and Transparency 2025) with a released benchmark ("We release our Answer Engine Evaluation benchmark (AEE)") — academic table "peer-reviewed, data or code published"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          You.com (YouChat), Perplexity.ai, Bing Copilot/BingChat — all priority-2 or lower per plan.md's engine matrix, not priority-1
metric_kind:     visibility
supersedes:      none
captured:        abstract, method (participant study design, automated benchmark design, 8 metrics), key results (hallucination, citation accuracy), limitations of citation as a trust signal
technique:       bears on citation-preference content indirectly — documents that citation itself (the outcome the technique optimizes for) does not imply factual accuracy or verifiability, which bounds what "getting cited" is worth as a brand-visibility technique
models_tested:   Engine identities only (You.com, Perplexity.ai, BingChat as consumer products); underlying LLM versions not disclosed by the engines and not independently identified by the authors in the passages captured here
date_window:     study submitted 2024-10-15; not independently dated beyond arXiv submission and the FAccT 2025 proceedings date
measured_effect: yes — but measuring citation FAILURE modes (hallucination rate, citation inaccuracy), not a content-rewrite intervention's success; "Citation Accuracy = 4/7" worked example, and aggregate results described qualitatively as favoring specific engines over others
vertical:        none named — general/cross-topic web queries plus "expertise queries" and "debate queries" categories
```

## Verbatim

### Abstract

"Large Language Model (LLM)-based applications are graduating from research prototypes to products serving millions of users, influencing how people write and consume information. A prominent example is the appearance of Answer Engines: LLM-based generative search engines supplanting traditional search engines. Answer engines not only retrieve relevant sources to a user query but synthesize answer summaries that cite the sources. To understand these systems' limitations, we first conducted a study with 21 participants, evaluating interactions with answer vs. traditional search engines and identifying 16 answer engine limitations. From these insights, we propose 16 answer engine design recommendations, linked to 8 metrics. An automated evaluation implementing our metrics on three popular engines (You.com, Perplexity.ai, BingChat) quantifies common limitations (e.g., frequent hallucination, inaccurate citation) and unique features (e.g., variation in answer confidence), with results mirroring user study insights. We release our Answer Engine Evaluation benchmark (AEE) to facilitate transparent evaluation of LLM-based applications."

### Method, verbatim

"[We conducted] an audit-centric usability study... involving 24 participants [Pilot study with 3 participants and a final usability study with 21 participants] with expertise in technical domains (e.g., sociology, economic[s]...)."

"[Query categories included] Expertise queries [technical queries that participants self-report being experts on, allowing evaluation of] how Answer Engines perform on deeply technical question[s, and] debate queries [e.g., 'Why should we abolish Daylight [Saving Time]'; by initially asking participants if they support one side of the debate, we can evaluate how participants interact with the answers that support or refute their opinions]."

"[The automated benchmark evaluated] three popular Answer Engines (YouChat, Bing Copilot, and Perplexity AI) using the 8 metrics, on 303 sear[ch queries]."

"Citation Thoroughness: This ratio metric measures the fraction of accurate citations includ[ed]... [worked example:] four accurate citations ((1,1), (2,2), (4,2) and (5,5)), and three inaccurate citations ((3,1), (3,3), (6,4)), so Citation Accuracy = 4/7."

### Results, verbatim

"LLMs are known to hallucinate information and cannot detect factual inconsistencies (Venkit et al., 2024; Huang et al., 2023), even when authoritative sources are provided."

"The RAG framework is advertised to solve the hallucinatory behavior of LLMs by enforcing that an LLM generates an answer grounded in source documents, yet the results show that RAG-based answer engines sti[ll exhibit hallucination]... hallucinatory behavior is not only exhibited in statements that are unsupported by the sources but also in inaccurate citations that prohibit users from verifyi[ng claims]."

"[One engine shows] dependent regardless of the user query, and worse performance on hallucinatory-related metrics including the presence of unsupported statements, and lack of citation precision. BingChat's overall performance comes in between [the other two]... most metrics, including critical aspects related to handling hallucinations, unsupported statements, and citation accuracy. We release our benchmark for ongoing audits to ensure these systems' transparency, fairness, and [reliability]."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2410.22349`, converted to plain text by stripping HTML/MathML tags. Passage boundaries around the aggregate-results paragraph are imprecise (mid-sentence truncation from the extraction) and the specific engine named as weakest is not identifiable from the extracted text alone without re-reading the source table — recorded as `unknown — checked arxiv.org/html/2410.22349 2026-09-22, ranked-comparison table not resolved in plain-text extraction`, not asserted.
- Engines tested (You.com, Perplexity, BingChat) are priority-2 and unranked engines per `plan.md`'s engine matrix, not ChatGPT/Claude/Google — this paper is evidence about the citation-accuracy mechanism generally, not a priority-1-engine-specific finding.
- Directly relevant to Pass 5 question (1), mechanism: it documents that citation (the visible outcome that citation-preference-content techniques target) is not a proxy for factual accuracy or verifiability — "even when authoritative sources are provided," hallucination persists, which bears on whether "authoritative tone" as a rewrite technique produces a trustworthy citation or merely a citable one.
- Found via the P5-c1 critical-survey pull's (`d-seeding-critical-survey-2026-09-22.md`) citation trail, listed there as "Venkit et al. 2025 PEER use/verifiability — Qualitative study showing the practical limitations of citations; 3 pilot and 21 main-study participants" — confirmed verbatim against the primary source in this pull.
- No arXiv code/data link was isolated in this extraction beyond the stated benchmark name "AEE (Answer Engine Evaluation)"; `unknown — checked arxiv.org/html/2410.22349 2026-09-22` for a direct repository URL.
