# Yin, Wang, Koopman, Zuccon — The Vulnerability of LLM Rankers to Prompt Injection Attacks

```yaml
source:          arXiv / SIGIR 2026 (Yu Yin, Shuai Wang, Bevan Koopman, Guido Zuccon)
url_or_doc_id:   https://arxiv.org/abs/2602.16752 ; DOI 10.1145/3805712.3808553 ; code https://github.com/ielab/LLM-Ranker-Attack
published:       2026-02-18
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Indexed under SIGIR 2026 proceedings per the paper's own DOI (10.1145/3805712.3808553), with public code — per trust-rubric.md academic table "Peer-reviewed, data or code published" = 3. Not independently replicated by an unrelated party within this cluster's pulls, so not tier 2. Academic sources are exempt from the plan.md recency/staleness filter.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — evaluated across unnamed LLM families used as rankers (pairwise, listwise, setwise paradigms); no named production consumer assistant
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus comments/DOI metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "The Vulnerability of LLM Rankers to Prompt Injection Attacks"

Authors, as printed: Yu Yin, Shuai Wang, Bevan Koopman, Guido Zuccon

Submission date, as printed: [v1] Wed, 18 Feb 2026 06:19:08 UTC (1,489 KB)

Subjects, as printed: Cryptography and Security (cs.CR)

Comments, as printed: "18 pages, 7 figures"

DOI, as printed: https://doi.org/10.48550/arXiv.2602.16752 (SIGIR 2026 proceedings DOI, per predecessor-repo pull dated 2026-09-16: 10.1145/3805712.3808553)

Abstract, verbatim:

"Large Language Models (LLMs) have emerged as powerful re-rankers. Recent research has however showed that simple prompt injections embedded within a candidate document (i.e., jailbreak prompt attacks) can significantly alter an LLM's ranking decisions. While this poses serious security risks to LLM-based ranking pipelines, the extent to which this vulnerability persists across diverse LLM families, architectures, and settings remains largely under-explored. In this paper, we present a comprehensive empirical study of jailbreak prompt attacks against LLM rankers. We focus our evaluation on two complementary tasks: (1) Preference Vulnerability Assessment, measuring intrinsic susceptibility via attack success rate (ASR); and (2) Ranking Vulnerability Assessment, quantifying the operational impact on the ranking's quality (nDCG@10). We systematically examine three prevalent ranking paradigms (pairwise, listwise, setwise) under two injection variants: decision objective hijacking and decision criteria hijacking. Beyond reproducing prior findings, we expand the analysis to cover vulnerability scaling across model families, position sensitivity, backbone architectures, and cross-domain robustness. Our results characterize the boundary conditions of these vulnerabilities, revealing critical insights such as that encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks. We publicly release our code and additional experimental results at [this https URL](https://github.com/ielab/LLM-Ranker-Attack)."

[note: no injection-variant prompt text is reproduced here — the abstract names the two injection variants (decision objective hijacking, decision criteria hijacking) as categories without printing the strings.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2602.16752` on 2026-09-22; this re-pulls a source the predecessor repo's `injection-feasibility-pulls.md` (dated 2026-09-16) also carried (including the SIGIR 2026 DOI and the title's-own-embedded-injection-joke note), per the task instruction to re-pull rather than inherit.
- Names two named injection variants as a taxonomy (decision objective hijacking, decision criteria hijacking) and two evaluation metrics (ASR, nDCG@10), but the abstract itself gives no aggregate percentage figure, n, or date window for the empirical study — those sit in the paper body, not fetched this pull.
- All testing is against LLM rankers in a research pipeline, not a named production consumer assistant — lab setting.
