# Zou, Geng, Wang, Jia — PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation

```yaml
source:          arXiv / USENIX Security Symposium 2025 (Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia)
url_or_doc_id:   https://arxiv.org/abs/2402.07867 ; USENIX listing https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag ; code https://github.com/sleeepeer/PoisonedRAG
published:       2024-02-12 (v1); last revised 2024-08-13 (v3); USENIX Security 2025 proceedings, August 2025, pp. 3827-3844 per the predecessor-repo pull
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Peer-reviewed (USENIX Security Symposium 2025, per the arXiv "Comments" field: "To appear in USENIX Security Symposium 2025") with published code — per trust-rubric.md academic table "Peer-reviewed, data or code published" = 3. Not independently replicated by an unrelated party within this cluster's pulls, so not tier 2. Academic sources are exempt from the plan.md recency/staleness filter.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — self-built RAG knowledge database (black-box and white-box settings), not a named production assistant
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus venue/comments metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models"

Authors, as printed: Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia

Submission history, as printed: [v1] Mon, 12 Feb 2024 18:28:36 UTC (481 KB); [v2] Sun, 11 Aug 2024 21:46:29 UTC (483 KB); [v3] Tue, 13 Aug 2024 01:55:06 UTC (483 KB)

Venue/Comments, as printed: "To appear in USENIX Security Symposium 2025. The code is available at [this https URL](https://github.com/sleeepeer/PoisonedRAG)"

Subjects, as printed: Cryptography and Security (cs.CR); Machine Learning (cs.LG)

Abstract, verbatim:

"Large language models (LLMs) have achieved remarkable success due to their exceptional generative capabilities. Despite their success, they also have inherent limitations such as a lack of up-to-date knowledge and hallucination. Retrieval-Augmented Generation (RAG) is a state-of-the-art technique to mitigate these limitations. The key idea of RAG is to ground the answer generation of an LLM on external knowledge retrieved from a knowledge database. Existing studies mainly focus on improving the accuracy or efficiency of RAG, leaving its security largely unexplored. We aim to bridge the gap in this work. We find that the knowledge database in a RAG system introduces a new and practical attack surface. Based on this attack surface, we propose PoisonedRAG, the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. We formulate knowledge corruption attacks as an optimization problem, whose solution is a set of malicious texts. Depending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, we propose two solutions to solve the optimization problem, respectively. Our results show PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts. We also evaluate several defenses and our results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses."

[note: no malicious-text payload is reproduced here — the abstract states the attack recipe abstractly (five injected texts per target question, optimization-based) without printing the injected text itself.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2402.07867` on 2026-09-22; this re-pulls a source the predecessor repo's `injection-feasibility-pulls.md` (dated 2026-09-16) also carried, per the task instruction to re-pull rather than inherit.
- The 90% attack success rate figure ("injecting five malicious texts for each target question into a knowledge database with millions of texts") is a lab-harness result: the authors construct and control the knowledge database themselves; the abstract names no production assistant or third-party indexed corpus as the target. This is recorded in the census's measured-effect table as a lab-only, not consumer-surface, measurement.
- No production or consumer-surface transfer test is claimed in this abstract, unlike the Pfrommer and Nestaas papers pulled alongside it in this cluster.
