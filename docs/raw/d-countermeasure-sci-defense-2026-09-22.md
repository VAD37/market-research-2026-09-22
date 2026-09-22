# Yu, Jin, Zeng & Wang — SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization (seed defense paper)

```yaml
source:          Xucheng Yu, Haibo Jin, Huimin Zeng, Haohan Wang
url_or_doc_id:   arxiv.org/abs/2605.21948 (abstract page); arxiv.org/html/2605.21948 (full-text HTML); arxiv.org/pdf/2605.21948 (PDF, task-assigned seed)
published:       "Submitted on 21 May 2026" — v1, Thu 21 May 2026 03:28:06 UTC (31 KB), per the abstract page's own version history
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint without code — academic table row "preprint without code"; authors state "Code and data will be released upon acceptance" (not yet released as of pull date). Submitted as a NeurIPS 2026 submission per the abstract page, not yet confirmed peer-reviewed/accepted
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — the paper evaluates a general-purpose defense pipeline against product/passage manipulation, not any named AI-assistant engine's production system
metric_kind:     none
supersedes:      none
captured:        title, authors, venue, abstract, method components, results figures, and limitations passage, as returned by the fetch tool across the abstract page and the HTML full text
technique:       defense literature — addresses corpus seeding / content-rewriting manipulation broadly, including a specific "Review attacks" evaluation category directly relevant to review and listicle manufacture
models_tested:   GPT-2 (used for the Perplexity-detection component); GPT-4o (used for the Semantic Integrity Scoring component and as the LLM judge scoring each manipulation dimension)
date_window:     n/a — no experiment date range stated beyond the submission date above
measured_effect: yes — see Verbatim
vertical:        n/a — tested on Amazon product descriptions (general retail) and MS MARCO web passages (general web), no single vertical named
```

## Verbatim

Title and venue, quoted as returned by the fetch tool:

"SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization" — NeurIPS 2026 submission.

Defense framework, quoted as returned by the fetch tool:

SCI-Defense comprises three components: "Perplexity detection (PPL), Semantic Integrity Scoring (SIS), and Inter-Candidate Detection (ICD)." The SIS component evaluates four manipulation dimensions: "Authority Attribution, Narrative Purposiveness, Comparative Claims, and Temporal Claims."

Measured results, quoted/reported as returned by the fetch tool:

Amazon Product Descriptions (600 samples across 6 categories) — Precision: 1.000, False Positive Rate: 0.000; Recall against String attacks: 1.000; Recall against Reasoning attacks: 0.952; **Recall against Review attacks: 0.830**.

MS MARCO Web Passages (600 samples) — String attacks blocked with perfect recall; "Review attacks yielded near-zero recall" on this dataset.

Comparison to prior defenses, quoted as returned by the fetch tool:

"Existing defenses — PPL-only filters, SafetyClf content classifiers, and paraphrasing — achieve zero recall against semantic manipulation attacks."

Limitations, quoted/reported as returned by the fetch tool (Section 6 "Discussion" and Section 7 "Conclusion"):

Section 7 "identifies semantic relevance manipulation as a structural blind spot... five novel attacks achieve Block@3=0.000 across two product categories, establishing this as the primary direction for future work." Attacks exploiting "semantic relevance inflation" (SEO Stuffing, Specification Amplification, Use-Case Saturation) produce scores below detection thresholds and "cannot be closed by threshold adjustment alone."

Code/data statement, quoted as returned by the fetch tool:

"Code and data will be released upon acceptance." No GitHub or other repository link found anywhere in the paper as captured.

## Pull notes — mechanical only

- Fetched via WebFetch across three URL forms: the abstract page (`arxiv.org/abs/2605.21948`, 200, gave title/authors/venue/submission-date/version-history), the PDF (`arxiv.org/pdf/2605.21948`, 200, returned mostly compressed/non-extractable binary content plus a high-level summary — saved locally, not further processed as this task's environment lacks a PDF-page-render tool (`pdftoppm`/poppler-utils not installed)), and the HTML full text (`arxiv.org/html/2605.21948`, 200, which is what yielded the model names, results detail, and limitations passage above).
- This is the paper this task was explicitly assigned to pull: "the seed paper arxiv.org/pdf/2605.21948." Its own citation trail (via the Semantic Scholar Graph API) is recorded separately at `docs/raw/d-countermeasure-semanticscholar-citation-trail-2026-09-22.md`, and two papers found through that trail are pulled as `d-countermeasure-geo-defender-2026-09-22.md` and `d-countermeasure-hae-geo-2026-09-22.md`.
- **The "Review attacks" recall figures (0.830 on Amazon, near-zero on MS MARCO) are the most directly relevant measured result in this task's defense-paper set to the P5-c2 "review and listicle manufacture" technique** — a dataset-dependent, large gap in detection performance, recorded here rather than interpreted.
- No independent replication of these figures was found in this pull; `unknown — checked Semantic Scholar's citation list for this paper (3 citing papers, none itself a replication of these specific numbers) 2026-09-22`.
