# Narisetty, Kore, Kattamanchi, Kumarapu — Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents

```yaml
source:          arXiv (Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi, Jayaram Kumarapu)
url_or_doc_id:   https://arxiv.org/pdf/2606.26479 (abs page fetched: https://arxiv.org/abs/2606.26479)
published:       2026-06-25
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     No venue field and no code/data-release statement beyond the "Comments" field ("12 pages, 5 figures, 4 tables") as fetched 2026-09-22 — treated as preprint without confirmed code per trust-rubric.md academic table default. Academic sources are exempt from the plan.md recency/staleness filter. Task-designated seed for cluster P5-c6.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — AgentDojo benchmark, open-weight Qwen2.5-7B self-hosted by the authors; no named production consumer assistant
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus subject/comments metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents"

Authors, as printed: Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi, Jayaram Kumarapu

Submission date, as printed: 25 Jun 2026

Subjects, as printed: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

Comments, as printed: "12 pages, 5 figures, 4 tables"

Abstract, verbatim:

"Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions. Systems such as CaMeL, FIDES, Progent, RTBAS, and FORGE realize this with capabilities, information-flow labels, and reference monitors, and several report near-elimination of attacks on the AgentDojo benchmark. We make two contributions. First, we organize these out-of-band defenses as instances of classical integrity protection (Biba), reference monitoring, and least privilege, yielding a structured comparison of what they do and do not cover. Second, we warn that every one of them is validated only on static benchmarks (a fixed set of injection attempts), the same methodology that made in-band defenses look strong until adaptive, defense-aware attacks broke twelve of them at over 90% success; we specify the threat model and protocol an adaptive evaluation requires. We then run that protocol as an independent reproduction and extension of Progent's own adaptive-attack analysis, on AgentDojo, with an open-weight agent (Qwen2.5-7B) self-hosted on a single H200, a setting its authors did not test. Averaged over three runs, the defense held: Progent cut mean attack success roughly sixfold (25.8% to 4.2%), and a hand-crafted adaptive attack did not raise it (2.6%). This is one small-scale data point on a weak model with a single black-box attack template; a stronger optimized (white-box GCG) attack remains open. The result is consistent with, but does not establish, the hypothesis that deterministic out-of-band enforcement is a harder target for an adaptive attacker than in-band detection."

[note: no attack-template text is reproduced here — the abstract describes the attack class (hand-crafted adaptive, black-box) and reports success-rate numbers without printing the prompt strings.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2606.26479` on 2026-09-22 (task-given seed URL was the `/pdf/` path; the `/abs/` page carries the same abstract/metadata).
- This is a countermeasure/defense paper, not an attack-demonstration paper against a brand-recommendation surface — it is academic evidence for Pass 5 question (4)'s "what does the field do about it" thread (research-side defenses), distinct from the engine-side policy statements pulled separately in this cluster.
- Reports a prior-work claim, not independently verified by this pull beyond the abstract's own wording: "adaptive, defense-aware attacks broke twelve of [in-band defenses] at over 90% success" — no citation list was fetched in this pull to identify which twelve systems.
- All testing in the abstract is against a self-hosted open-weight model (Qwen2.5-7B) on the AgentDojo benchmark — lab harness, not a production consumer assistant or indexed-content surface.
