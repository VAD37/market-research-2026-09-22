# PoPETs 2026 — A Year Under the DSA: Ad Transparency's Uneven Landscape

```yaml
source:          Proceedings on Privacy Enhancing Technologies (PoPETs), Vol. 2026, Issue 2
url_or_doc_id:   https://petsymposium.org/popets/2026/popets-2026-0059.php ; DOI https://doi.org/10.56553/popets-2026-0059
published:       2026 (Volume 2026, Issue 2, pages 517-532); no more specific date on the abstract page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            4
tier_reason:     adjusted from academic-table default 3 ("peer-reviewed, data or code published") to 4 ("preprint with code and prompt set" tier) because data/code publication is not confirmed anywhere on the abstract page itself — no dataset or code link is shown; PoPETs is a peer-reviewed venue but the trust-rubric's tier-3 row requires data or code actually published, which this pull could not verify
source_label:    analyst-derived
lane:            B, D
sub_market:      paid placement
engine:          n/a — covers Facebook, Instagram, YouTube, X (none are AI-assistant engines in this task's scope)
metric_kind:     none
supersedes:      none
captured:        full page, get_page_text
```

## Verbatim

Title: "A Year Under the DSA: Ad Transparency's Uneven Landscape"

Authors: "Abir Benzaamia (LIX, CNRS, Inria, École Polytechnique, IP Paris), Asmaa El Fraihi (LIX, CNRS, Inria, École Polytechnique, IP Paris), Ines Abdelaziz (LIX, CNRS, Inria, École Polytechnique, IP Paris), Oana Goga (LIX, CNRS, Inria, École Polytechnique, IP Paris)"

Volume: 2026. Issue: 2. Pages: 517-532. DOI: https://doi.org/10.56553/popets-2026-0059

Abstract: "The Digital Services Act (DSA) has put platform accountability on center stage, requiring online platforms to provide greater transparency into how advertisements are targeted and delivered to users. Central to these obligations are two mechanisms: user-facing ad explanations, which inform individuals why they were shown a given ad, and public ad repositories, which are intended to enable independent auditing of advertising practices. This study provides the first multi-platform evaluation of these two mechanisms across Facebook, Instagram, YouTube and X. Using 48,511 user-facing "Why am I seeing this ad?" (WAIST) notices, and a systematic analysis of each platform's public ad repository, we assess how well current implementations disclose the parameters and decision processes involved in targeting. To do so, we develop and apply an operational framework based on Articles 26 and 39 of the DSA—capturing the granularity, attribution of targeting and delivery choices, data source disclosures, and accuracy—and apply it across both user-facing notices and public ad repositories. Our findings show that transparency remains fragmented and inconsistent across platforms. User-facing explanations vary widely in precision and often omit key targeting information, while repositories provide incomplete, misattributed, and at times difficult-to-interpret targeting data. Moreover, discrepancies between explanations and repository entries undermine the reliability of both mechanisms. Overall, current transparency infrastructures fall short of the DSA's expectations and highlight the need for clearer and more enforceable standards for advertising transparency moving forward."

Keywords: "Digital Services Act (DSA), Online Advertising, Ad transparency, Ad explanations, Ad repositories"

"Copyright in PoPETs articles are held by their authors. This article is published under a Creative Commons Attribution 4.0 license."

## Pull notes — mechanical only

- Abstract page only — the PDF was not downloaded/read in this pull; the full paper's methodology section, sample dates, and per-platform findings tables were not captured. The "48,511 user-facing ... notices" figure and per-platform assessment are stated in the abstract only.
- **The four platforms studied — Facebook, Instagram, YouTube, X — are none of them AI-assistant engines in this task's scope.** The paper is evidence about DSA Article 39 ad-repository quality generally (methodology and findings pattern transferable), not about any priority-1 or priority-2 AI-assistant engine's ad repository specifically. No ChatGPT, Claude, Gemini, Perplexity, Copilot, or Amazon assistant content appears in the abstract.
- The paper's finding that repositories provide "incomplete, misattributed, and at times difficult-to-interpret targeting data" and that "current transparency infrastructures fall short of the DSA's expectations" corroborates, independently and via peer-reviewed measurement, the Commission's own finding against X's ad repository specifically (`b-eu-ec-x-fine-120m-2026-09-22.md`) — X is one of the paper's four studied platforms.
