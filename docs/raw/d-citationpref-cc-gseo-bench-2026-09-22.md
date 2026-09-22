# Chen et al. — CC-GSEO-Bench: A Content-Centric Benchmark for Measuring Source Influence in Generative Search Engines

```yaml
source:          Qiyuan Chen, Jiahe Chen, Hongsen Huang, Qian Shao, Jintai Chen, Renjie Hua, Hongxia Xu, Ruijia Wu, Ren Chuan, Jian Wu
url_or_doc_id:   arxiv.org/abs/2509.05607
published:       2025-09-06 (v1); last revised 2025-12-26 (v2, "Technical Report")
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint labelled "Technical Report" by the authors themselves, no stated peer review, no code/data release statement isolated in this extraction — academic table "preprint without code"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          gpt-oss-120b named as "the backbone GSE model" for main results; other architectures noted as tested in an appendix not captured in this pull
metric_kind:     visibility
supersedes:      none
captured:        abstract, mechanism (five-dimension influence/quality framework including Readability & Structure and Trustworthiness & Safety), baseline method categories explicitly named after this cluster's target content features, a specific finding that heavy statistic-injection can backfire via a trust penalty
technique:       content written to satisfy known citation preferences — operationalizes exactly the features named in this task (statistics, authoritative/credibility framing, fluency, structure) as scored dimensions, and separately measures a trust/perceived-hallucination cost to aggressive statistic-stuffing
models_tested:   gpt-oss-120b (backbone GSE); judge model used to score Exposure, Faithful Credit and other dimensions not separately named in the passages captured
date_window:     v1 2025-09-06, v2 2025-12-26; no narrower data-collection window stated
measured_effect: yes — "the aggressive injection of numerical data may be perceived as hallucination-prone or artificially de[graded]... [causing a] significant degradation in Trustworthiness (7.613 vs. 8.352 for baseline)" despite gains on other influence metrics
vertical:        none named — query-article pairs drawn from ELI5 (1,710 pairs), Pinocchio (1,017), Natural Questions (922), MS MARCO (920), HotpotQA (197), DebateQA (185), AllSouls (49); none of these source datasets are vertical-scoped to skincare, B2B SaaS, or high-CPA regulated categories
```

## Verbatim

### Abstract

"Generative Search Engines (GSEs) synthesize conversational answers from multiple sources, weakening the long-standing link between search ranking and digital visibility. This shift raises a central question for content creators: How can we reliably quantify a source article's influence on a GSE's synthesized answer across diverse intents and follow-up questions? We introduce CC-GSEO-Bench, a content-centric benchmark that couples a large-scale dataset with a creator-centered evaluation framework. The dataset contains over 1,000 source articles and over 5,000 query-article pairs, organized in a one-to-many structure for article-level evaluation. We ground construction in realistic retrieval by combining seed queries from public QA datasets with limited synthesized augmentation and retaining only queries whose paired source reappears in a follow-up retrieval step. On top of this dataset, we operationalize influence along three core dimensions: Exposure, Faithful Credit, and Causal Impact, and two content-quality dimensions: Readability and Structure, and Trustworthiness and Safety. We aggregate query-level signals over each article's query cluster to summarize influence strength, coverage, and stability, and empirically characterize influence dynamics across representative content patterns."

### Mechanism — five-dimension framework, verbatim

"[Influence dimensions:] Exposure, Faithful Credit, and Causal Impact, and two content-quality dimensions, Readability and Structure and Trustworthiness and Safety. We aggregate query-level signals over each article's query cluster to summarize influence strength, cov[erage] and stability."

"Readability and Structure characterizes how easy the source document is to read and navigate, and how well its organization support[s extraction and synthesis]."

"Trustworthiness and Safety measures whether the source document appears reliable and avoids unsafe, harmful, or misleading content bas[ed on judge-model assessment]."

"[Worked example:] Source 1 demonstrates high Readability and Trustworthiness which translates into dominant Exposure and [downstream influence]... Source 2 exhibits low Trustworthiness and fails to positively influence the synthesized answer despite being retrieved."

### Method — baseline optimization strategies, verbatim

"Appendix A Baseline GSEO Methods. Our approach leverages distinct prompting strategies to achieve various GSEO goals, each targeting a specific aspect of content presentation to improve its 'rank' within a LLMs generated [response]." Named baseline categories: "A.1 Textual Fluency and Engagement," "A.2 Authority and Credibility Building," "A.3 SEO Techniques."

"[One rewrite method is characterized as] a form of 'vocabulary stuffing' for generative models, distinct from traditional keyword stuffing... SEO: This method directly addresses traditional SEO principles by incorporating new, relevant keyword[s]."

"Unless otherwise noted, we employ gpt-oss-120b as the backbone GSE model. Results for other architectures and cross-model consistency are provided in Appendix C."

### Results — the statistics-injection trust penalty, verbatim

"[A method optimizing for Exposure and Faithful Credit via aggressive statistic-injection achieves high Influence Coverage (ICov 0.091) and Faithful Credit, but] suffers from a significant degradation in Trustworthiness (7.613 vs. 8.352 for baseline), indicating that the aggressive injection of numerical data may be perceived as hallucination-prone or artificially de[graded, i.e., a trust cost attached to a visibility gain]."

"Faithful Credit (F) shows moderate correlation with [Causal Impact] C (r ≈ 0.254). Meanwhile, Readability (R) and Trustworthiness (T) are positively correlated (r ≈ 0.197), while C and T exhibit a weak negative correlation (r ≈ -0.081)."

### Dataset composition, verbatim

"Distribution of Query-Article Pairs by Original Source Dataset. Original Source Dataset | Number of Pairs — ELI5 1710, Pinocchio 1017, Natural Questions (NQ) 922, MS MARCO 920, HotpotQA 197, DebateQA 185, AllSouls 49."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2509.05607`, converted to plain text by stripping HTML/MathML tags.
- This paper is cited in the P5-c1 critical-survey pull (`d-seeding-critical-survey-2026-09-22.md`) as "Chen et al. [2025b]" (full bibliography entry recovered there: "CC-GSEO-Bench: A content-centric benchmark for measuring source influence in generative search engines, 2025b. URL https://arxiv.org/abs/2509.05607") and separately characterized in that survey's own summary table as "Chen et al. 2025 (CC-GSEO) PREPR. influence/quality — Retrieved web contexts, but LLM-generated article-centric queries and predominantly automated judges; no complementary human validation" — that limitation (automated-judge-only evaluation, no human validation) is confirmed as the survey's own reading, not independently re-derived by this pull from the primary source's limitations section, which was not isolated in this extraction.
- The "statistics injection can hurt trust" finding directly bears on the foundational GEO paper's "Statistics Addition" technique (already covered in `docs/raw/d-seeding-geo-foundational-2026-09-22.md`, P5-c1) — this paper is evidence of a boundary condition on that technique (aggressive/artificial-seeming statistic injection can read as fabricated) not present in the foundational paper's own reported results.
- Full baseline method list (Appendix A.1-A.3, naming all individual prompting strategies) was not exhaustively captured; the categories "Textual Fluency and Engagement," "Authority and Credibility Building," and "SEO Techniques" are the three named subsection headers, confirmed verbatim; the individual method names within each subsection were not fully isolated in this extraction — `unknown — checked arxiv.org/html/2509.05607 2026-09-22` for the complete list.
