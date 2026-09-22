# Pfrommer et al. — Ranking Manipulation for Conversational Search Engines

```yaml
source:          arXiv / EMNLP 2024 (Samuel Pfrommer, Yatong Bai, Tanmay Gautam, Somayeh Sojoudi)
url_or_doc_id:   https://arxiv.org/abs/2406.03589 ; companion code https://github.com/spfrommer/cse-ranking-manipulation
published:       2024-06-05 (v1); last revised 2024-09-25 (v3)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Peer-reviewed (2024 Conference on Empirical Methods in Natural Language Processing, Main track, per the arXiv "Comments" field) with a published companion code repository — per trust-rubric.md academic table "Peer-reviewed, data or code published" = 3. Not independently replicated by an unrelated party within this cluster's pulls, so not tier 2. Academic sources are exempt from the plan.md recency/staleness filter.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          perplexity.ai (named explicitly as the production transfer target); unnamed set of LLMs evaluated in the controlled dataset
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus venue/subject metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page; companion code repo description carried over from the predecessor-repo channel pull dated 2026-09-16 (`D:\researchs\market-research\docs\raw\injection-feasibility-pulls.md`), re-verified against this fresh 2026-09-22 abs-page fetch, not independently re-fetched from GitHub this pull
```

## Verbatim

Title, as printed: "Ranking Manipulation for Conversational Search Engines"

Authors, as printed: Samuel Pfrommer, Yatong Bai, Tanmay Gautam, Somayeh Sojoudi

Submission history, as printed: [v1] Wed, 5 Jun 2024 19:14:21 UTC (7,039 KB); [v2] Thu, 13 Jun 2024 01:12:56 UTC (7,039 KB); [v3] Wed, 25 Sep 2024 14:59:24 UTC (4,788 KB)

Venue/Comments, as printed: "2024 Conference on Empirical Methods in Natural Language Processing (Main)"

Subjects, as printed: Computation and Language (cs.CL)

Abstract, verbatim:

"Major search engine providers are rapidly incorporating Large Language Model (LLM)-generated content in response to user queries. These conversational search engines operate by loading retrieved website text into the LLM context for summarization and interpretation. Recent research demonstrates that LLMs are highly vulnerable to jailbreaking and prompt injection attacks, which disrupt the safety and quality goals of LLMs using adversarial strings. This work investigates the impact of prompt injections on the ranking order of sources referenced by conversational search engines. To this end, we introduce a focused dataset of real-world consumer product websites and formalize conversational search ranking as an adversarial problem. Experimentally, we analyze conversational search rankings in the absence of adversarial injections and show that different LLMs vary significantly in prioritizing product name, document content, and context position. We then present a tree-of-attacks-based jailbreaking technique which reliably promotes low-ranked products. Importantly, these attacks transfer effectively to state-of-the-art conversational search engines such as perplexity.ai. Given the strong financial incentive for website owners to boost their search ranking, we argue that our problem formulation is of critical importance for future robustness work."

Companion code repository self-description, carried over verbatim from the predecessor-repo pull dated 2026-09-16 (source: `https://github.com/spfrommer/cse-ranking-manipulation`): dataset "a real-world e-commerce website dataset" (RAGDOLL), with an open-sourced "dataset collection pipeline"; attack technique lineage "a tree-of-attacks-based jailbreaking technique which reliably promotes low-ranked products," built "based on the minimal implementation" of "Tree of Attacks (TAP): Jailbreaking Black-Box LLMs Automatically"; transfer test target named explicitly as "closed-source, online-enabled RAG implementations such as the Sonar Large Online model by perplexity.ai."

[note: no adversarial/injection strings are reproduced here — the abstract and the code repo's own description do not print the payload text, and none was sought beyond what these two pages state.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2406.03589` on 2026-09-22; this re-pulls a source the predecessor repo's `injection-feasibility-pulls.md` (dated 2026-09-16) also carried, per the task instruction to re-pull any primary relied on rather than inherit the predecessor's pull.
- The companion-code paragraph is carried over from the predecessor channel's 2026-09-16 pull rather than independently re-fetched from GitHub this pull; it is quoted as the predecessor file recorded it, dated as such, and its content (dataset name, attack lineage, named transfer target) is consistent with what the fresh 2026-09-22 abstract itself states.
- This is the paper most directly on point for Pass 5 question (3): it names a specific production consumer surface (perplexity.ai) as a transfer target for a ranking-manipulation attack built via prompt injection, though the abstract does not itself give a numeric attack-success rate, n, or date window for the perplexity.ai transfer test specifically — see the census's measured-effect table for what is and is not quantified here.
