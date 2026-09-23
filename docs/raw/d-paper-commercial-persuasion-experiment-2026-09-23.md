# Commercial Persuasion in AI-Mediated Conversations

```yaml
source:          Francesco Salvi, Alejandro Cuevas, Manoel Horta Ribeiro
url_or_doc_id:   arXiv:2604.04263 ; https://arxiv.org/abs/2604.04263
published:       2026-04-05 (arXiv v1; latest listed 2026-04-05)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint; two preregistered randomized experiments (N=2,012) with OSF materials; academic table 'preprint with code/materials'
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          five frontier models incl. GPT-5.2/5.4, Gemini 3 Pro/3.1 Pro, Claude Opus 4.5, DeepSeek-v3.2, Qwen3
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    arXiv preprint
code_availability: OSF: https://osf.io/3zpkd/ and https://osf.io/ps6un/ (view-only links in paper)
capability_class: conversational persuasion raises sponsored-product selection; effect of 'Sponsored' label measured
```

## Verbatim — abstract

"As Large Language Models (LLMs) become a primary interface between users and the web, companies face growing economic incentives to embed commercial influence into AI-mediated conversations. We present two preregistered experiments (N = 2,012) in which participants selected a book to receive from a large eBook catalog using either a traditional search engine or a conversational LLM agent powered by one of five frontier models. Unbeknownst to participants, a fifth of all products were randomly designated as sponsored and promoted in different ways. We find that LLM-driven persuasion nearly triples the rate at which users select sponsored products compared to traditional search placement (61.2% vs. 22.4%), while the vast majority of participants fail to detect any promotional steering. Explicit "Sponsored" labels do not significantly reduce persuasion, and instructing the model to conceal its intent makes its influence nearly invisible (detection accuracy < 10%). Altogether, our results indicate that conversational AI can covertly redirect consumer choices at scale, and that existing transparency mechanisms may be insufficient to protect users."

## Verbatim — result sentences (from arXiv HTML full text)

- "We find that LLM-driven persuasion nearly triples the rate at which users select sponsored products compared to traditional search placement (61.2% vs. 22.4%), while the vast majority of participants fail to detect any promotional steering."
- "Explicit “Sponsored” labels do not significantly reduce persuasion, and instructing the model to conceal its intent makes its influence nearly invisible (detection accuracy < 10%)."
- "In the Chat–Persuasion condition, 61.2% of participants selected a sponsored product (SE = 2.4, 95% CI [56.4, 65.9]), nearly tripling the rate observed under Search–Placement (38.8 pp, p adj p_{mathrm{adj}} < < 0.001) and more than doubling the rate under Chat–Placement (34.4 pp, p adj p_{mathrm{adj}} < < 0.001)."
- "Adding an explicit “Sponsored” label and briefing study participants that some products would be promoted ( Chat–Persuasion, Explicit ) reduced Persuasion Rate only slightly, to 55.5% (SE = 2.5, 95% CI [50.6, 60.4])."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2604.04263`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
