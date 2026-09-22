# Nestaas, Debenedetti, Tramèr — Adversarial Search Engine Optimization for Large Language Models

```yaml
source:          arXiv (Fredrik Nestaas, Edoardo Debenedetti, Florian Tramèr)
url_or_doc_id:   https://arxiv.org/abs/2406.18382
published:       2024-06-26 (v1); last revised 2024-07-02 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     No venue/"Comments" field naming a peer-reviewed venue, and no code-or-prompt-set link, was returned by this pull's WebFetch of the arXiv abs page as fetched 2026-09-22 — treated as preprint without confirmed code per trust-rubric.md academic table default. Academic sources are exempt from the plan.md recency/staleness filter.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Bing and Perplexity (named as production LLM search engines tested); plugin APIs for GPT-4 and Claude (named as production plugin surfaces tested)
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus subject metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "Adversarial Search Engine Optimization for Large Language Models"

Authors, as printed: Fredrik Nestaas, Edoardo Debenedetti, Florian Tramèr

Submission history, as printed: [v1] Wed, 26 Jun 2024 14:24:51 UTC (3,764 KB); [v2] Tue, 2 Jul 2024 08:56:48 UTC (3,763 KB)

Subjects, as printed: Cryptography and Security (cs.CR); Machine Learning (cs.LG)

Abstract, verbatim:

"Large Language Models (LLMs) are increasingly used in applications where the model selects from competing third-party content, such as in LLM-powered search engines or chatbot plugins. In this paper, we introduce Preference Manipulation Attacks, a new class of attacks that manipulate an LLM's selections to favor the attacker. We demonstrate that carefully crafted website content or plugin documentations can trick an LLM to promote the attacker products and discredit competitors, thereby increasing user traffic and monetization. We show this leads to a prisoner's dilemma, where all parties are incentivized to launch attacks, but the collective effect degrades the LLM's outputs for everyone. We demonstrate our attacks on production LLM search engines (Bing and Perplexity) and plugin APIs (for GPT-4 and Claude). As LLMs are increasingly used to rank third-party content, we expect Preference Manipulation Attacks to emerge as a significant threat."

[note: no crafted-content or attack-string text is reproduced here — the abstract itself does not print the payload, and none was sought beyond what the abstract states.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2406.18382` on 2026-09-22; this re-pulls a source the predecessor repo's `injection-feasibility-pulls.md` (dated 2026-09-16) also carried, per the task instruction to re-pull rather than inherit.
- This abstract is the clearest single statement in this cluster's pulls of Pass 5 question (1) applied directly to brand steering: "carefully crafted website content or plugin documentations can trick an LLM to promote the attacker products and discredit competitors" — i.e. the named mechanism is content-based preference manipulation via what the abstract calls Preference Manipulation Attacks, tested against named production consumer/API surfaces (Bing, Perplexity, GPT-4 and Claude plugin APIs), not a lab harness the authors built from scratch.
- No numeric attack-success rate, sample size, or date window for the production tests is stated in the abstract; the census's measured-effect table records this as a gap, not a finding.
