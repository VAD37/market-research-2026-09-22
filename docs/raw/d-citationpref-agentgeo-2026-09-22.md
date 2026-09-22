# Tian et al. — Diagnosing and Repairing Citation Failures in Generative Engine Optimization (AgentGEO / MIMIQ)

```yaml
source:          Zhihua Tian, Yuhan Chen, Yao Tang, Jian Liu, Ruoxi Jia
url_or_doc_id:   arxiv.org/abs/2603.09296
published:       2026-03-10
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; no venue/review status found in this pull, no explicit code-release statement found in the passages captured; new benchmark (MIMIQ) is introduced and described in detail but a public release URL was not isolated in this extraction — academic table "preprint without code" pending further confirmation
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Generative engine simulated with GPT (gpt-4.1-mini) and Claude (claude-haiku-4-5-20251001) as backbones
metric_kind:     visibility
supersedes:      none
captured:        abstract, mechanism (taxonomy of citation failure modes, diagnose-then-repair agentic loop), models and dataset size, headline effect size, a caveat that generic optimization can harm long-tail content
technique:       content written to satisfy known citation preferences — reframes the technique from "apply generic rewrite recipes" to "diagnose why THIS document fails to be cited, then apply a targeted repair," explicitly critiquing uniform/generic rewriting as this cluster's other papers (C-SEO Bench, FeatGEO) also find weak or negative
models_tested:   gpt-4.1-mini, claude-haiku-4-5-20251001 ("state-of-the-art LLMs")
date_window:     not stated beyond arXiv submission date 2026-03-10
measured_effect: yes — "AgentGEO achieves over 40% relative improvement in citation rates while modifying only 5% of content, compared to 25% for baselines"
vertical:        none named — 204 webpages sampled from the ClueWeb22 general web index, not vertical-scoped
```

## Verbatim

### Abstract

"Generative Engine Optimization (GEO) aims to improve content visibility in AI-generated responses. However, existing methods measure contribution-how much a document influences a response-rather than citation, the mechanism that actually drives traffic back to creators. Also, these methods apply generic rewriting rules uniformly, failing to diagnose why individual document are not cited. This paper introduces a diagnostic approach to GEO that asks why a document fails to be cited and intervenes accordingly. We develop a unified framework comprising: (1) the first taxonomy of citation failure modes spanning different stages of a citation pipeline; (2) AgentGEO, an agentic system that diagnoses failures using this taxonomy, selects targeted repairs from a corresponding tool library, and iterates until citation is achieved; and (3) a document-centric benchmark evaluating whether optimizations generalize across held-out queries. AgentGEO achieves over 40% relative improvement in citation rates while modifying only 5% of content, compared to 25% for baselines. Our analysis reveals that generic optimization can harm long-tail content and some documents face challenges that optimization alone cannot fully address-findings with implications for equitable visibility in AI-mediated information access."

### Mechanism — taxonomy of citation failure modes, verbatim

"We introduce the first systematic taxonomy of citation failure modes spanning the generative engine pipeline: parsing-stage failures (malformed HTML, excessive noise), fetching/context failure[s]... [and generation-stage failures, e.g.] entity gaps, intent mismatch, competitor disadvantage. This taxonomy guides our tool library design and provides a foundation for future citation-focused optimization."

"Each failure mode requires a different intervention, yet generic rules cannot diagnose which stage failed, nor can they address upstream failures that occur before tex[t-level rewriting could help]."

"[The framing shifts the research question to] 'why did this webpage fail to be cited for the relevant queries?' We instantiate this perspective in AgentGEO, an agentic framework for iterative diagnosis and repair. Given a webpage that fails to be cited, Agent[GEO diagnoses the failure mode and selects a targeted repair]."

### Method — models and benchmark, verbatim

"[The system is] built with state-of-the-art LLMs, including GPT (gpt-4.1-mini), and Claude (claude-haiku-4-5-20251001)."

"We introduce MIMIQ (Multi-Intent Multi-Query), a document-centric benchmark associating each webpages with multiple queries spanning diverse intents, personas, and phrasings... Methods optimize using a training query set and are evaluated on held-out queries unseen during optimization. This protoco[l tests whether an optimization generalizes rather than overfits to one query formulation]."

"The standard MIMIQ dataset comprises 204 webpages sampled from the ClueWeb22 index. For each webpage, we curate a st[ructured set of training and held-out test queries]."

"[Two stress-test variants:] MIMIQ-OOD (Out-of-Distribution): To evaluate generalization, we enforce a distributional shift between training and testing. We cluster generated queries based on user personas; specific personas are reser[ved for testing only]... MIMIQ-HTML (Structural Robustness): In practice, citation failures often originate in the upstream fetching and parsing phases. MIMIQ-HTML subset identified as having complex or irregular DOM structures."

### Results and limitations, verbatim

"AgentGEO achieves over 40% relative improvement in citation rates while modifying only 5% of content, compared to 25% for baselines."

"[On documents receiving] no citation under baseline conditions... the question is not 'how much am I cited?' but 'why am I not cited at all?' Understanding and repairing these failures is an underexplored problem."

"Not all citation failures are recoverable... For certain webpages, even diagnostic optimization fails to improve citation. These webpages face disadvantages—dominant competitors—that no content-side modification can o[vercome]."

"For the remaining uncited webpages, some optimization steps inadvertently removed domain-specific information, making them less likely to be cited. Surprisingly, AutoGEO shows worse perf[ormance in this regime than simpler baselines, per the surrounding discussion]... generic optimization can harm long-tail content."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2603.09296`, converted to plain text by stripping HTML/MathML tags; the framework's stylized name renders as "𝙰𝚐𝚎𝚗𝚝𝙶𝙴𝙾" (mathematical sans-serif Unicode) in the source HTML — normalized to "AgentGEO" throughout this pull for readability; the Unicode styling itself carries no semantic content.
- The P5-c1 census (`d-seeding-geo-foundational-2026-09-22.md` cluster's own screened-out list) recorded this same arXiv ID under the label "2603.09296 (AgentGEO)" as an off-cluster item — that prior agent's characterization by title ("AgentGEO") is confirmed correct by this full pull; the earlier list entry appears to have transposed a different one-line description ("owned-content optimization... not third-party seeding") that does match this paper's actual scope. No conflict found; this is a first full pull of the paper, not a correction of a wrong ID.
- No venue name (conference/journal) was found in the passages captured in this pull; `unknown — checked arxiv.org/html/2603.09296 2026-09-22` for peer-review status, held pending further confirmation before any upgrade from tier 5.
- No explicit code or dataset release URL was isolated in this extraction; `unknown — checked arxiv.org/html/2603.09296 2026-09-22` for a repository link, despite the detailed MIMIQ benchmark construction description (204 webpages, ClueWeb22-sourced) suggesting a release is likely.
