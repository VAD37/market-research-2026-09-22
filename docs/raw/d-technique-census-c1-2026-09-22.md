# Technique census — P5-c1, corpus seeding in high-citation sources

Pass 5, cluster P5-c1. Compiled 2026-09-22. Lane D, sub-market organic recommendation. Moves H5, H14. Cites 12 raw pulls landed 2026-09-22 (`docs/raw/d-seeding-*-2026-09-22.md`) plus two pre-existing raw pulls from Pass 2 (`docs/raw/b-openai-usage-policies-2026-09-22.md`, `docs/raw/b-anthropic-usage-policy-2026-09-22.md`), read but not re-pulled. No interpretation beyond the tables, per task instruction.

## (1) Mechanism — how it works, per source

| Source | Raw path | Mechanism as the source describes it |
|---|---|---|
| Aggarwal et al., foundational GEO paper (KDD 2024) | `d-seeding-geo-foundational-2026-09-22.md` | Nine content-optimization methods applied to a page's own text; "Cite Sources" and "Quotation Addition" add citations/quotations from credible external sources into the optimized page itself — not placement on a third-party site |
| GEO-Bench (Nimase et al.) | `d-seeding-geo-bench-2026-09-22.md` | Benchmarks black-box content-rewriting attacks, incl. an "Authoritative" rewriting strategy that rewrites a document to read as authoritative to raise its retrieval rank |
| SafeGEO (Wen et al.) | `d-seeding-safegeo-2026-09-22.md` | 22 content-rewriting "GEO attack variants" applied to product listings inside a recommendation-agent testbed, raising a flawed product's inclusion rate |
| Answer Bubbles (Huang et al., EMNLP 2026) | `d-seeding-answer-bubbles-2026-09-22.md` | Documents *why* seeding a source like Wikipedia would work: five AI-mediated search systems structurally over-cite Wikipedia and long-form content and under-cite social/forum content in this sample — mechanism is citation-source bias, not a seeding action itself |
| What Gets Cited (Vishwakarma et al., Sprinklr) | `d-seeding-what-gets-cited-2026-09-22.md` | Isolates which content factors make one of two competing sources win the first citation: topical relevance and list position dominate; explicit price and recent timestamp help; formatting alone does not |
| Dominate AI Search (Chen et al.) | `d-seeding-dominate-ai-search-2026-09-22.md` | Names the mechanism directly: AI Search systems draw disproportionately from "earned media (third-party, authoritative sources)" over brand-owned content; prescribes "dominate earned media to build AI-perceived authority" |
| UK iGaming notability report (Oruesagasti / Interamplify) | `d-seeding-igaming-notability-2026-09-22.md` | Compliance/regulatory-licensing signals (UK Gambling Commission standards), structured as machine-readable data, act as an "authority multiplier" for earned-media citation in a regulated vertical |
| Critical survey (Martinez) | `d-seeding-critical-survey-2026-09-22.md` | Reframes GEO as a multi-stage pipeline (activation, crawling, retrieval, reranking, citation, prominence, absorption, fidelity, behavior); states gains are conditional on a source already sitting inside a fixed retrieved context |
| McKelvey playbook (practitioner) | `d-seeding-justinmckelvey-playbook-2026-09-22.md` | Explicit tactic list: "be genuinely useful on Reddit," "earn press, even small press," "publish original data," "publish your prices" |
| SolCrys citation study (practitioner/vendor) | `d-seeding-solcrys-citations-2026-09-22.md` | Explicit "source-layer presence" tactic: allocate ~30% of GEO effort to "Community" — "pitch it to trade press, answer relevant community threads, and update Wikipedia where notability allows" |
| Incumbent Advantage (Chu & Hou, seed paper) | `d-seeding-incumbent-advantage-2026-09-22.md` | Adjacent, not the same mechanism: controlled test of brand-description content (identical specs vs. authority-style marketing language) inside an LLM recommendation prompt, not third-party placement |
| Google spam policies | `d-seeding-google-spam-policies-2026-09-22.md` | Describes the inverse direction — a host accepting low-value third-party content for that host's own ranking credit ("site reputation abuse") — not a brand placing content on an external high-citation site |

## (2) Who is documented doing it — per source, actor type

| Source | Raw path | Actor type | What the source documents |
|---|---|---|---|
| McKelvey playbook | `d-seeding-justinmckelvey-playbook-2026-09-22.md` | Independent practitioner (fractional CTO, runs a productized-services site) | Self-tracks own-domain citation outcomes; describes and recommends the technique for others |
| SolCrys | `d-seeding-solcrys-citations-2026-09-22.md` | GEO/AI-visibility vendor or content platform (commercial category inferred from site framing, no explicit disclosure found) | Recommends the "Community" seeding allocation as a stated practitioner methodology |
| What Gets Cited | `d-seeding-what-gets-cited-2026-09-22.md` | Vendor researchers (all three authors Sprinklr-affiliated) | Academic-style study of citation-winning factors; piloted internally at Sprinklr; not itself a seeding case study |
| SafeGEO, GEO-Bench, foundational GEO paper | see above | Academic researchers | Build and test attack/optimization methods in controlled benchmarks they construct; document the technique class as a research object, not as an observed real-world campaign |
| UK iGaming report | `d-seeding-igaming-notability-2026-09-22.md` | GEO/marketing research vendor ("Interamplify Research Division (UK)") | Advises iGaming brands to structure compliance signals as authority multipliers; no named brand case documented |
| Dominate AI Search | `d-seeding-dominate-ai-search-2026-09-22.md` | Academic researchers (no stated commercial affiliation found) | Documents the earned-media citation bias and prescribes it as a strategic agenda for practitioners; no named brand's seeding campaign documented |

No source in this cluster documents a **named brand** running a corpus-seeding campaign with before-and-after results. Every "who does it" row above is either a researcher studying the technique in a controlled benchmark, or a practitioner/vendor recommending the technique in the abstract. This absence is itself recorded, not filled by inference.

## (3) Measured-effect table — before-and-after with prompt set, n, models, date window (H5 test)

| Source | Raw path | Models tested | Date window | Prompt set published | n | Effect size, verbatim | Replicated by | Tier |
|---|---|---|---|---|---|---|---|---|
| Foundational GEO paper (Aggarwal et al., KDD 2024) | `d-seeding-geo-foundational-2026-09-22.md` | GPT-3.5-turbo (2022); G-Eval/GPT-3.5 as judge; real-world test on Perplexity.ai | Paper spans 2023-11-16 to 2024-06-28; no narrower run window stated | Yes — 10,000 queries, 25 domains, code/data at generative-engines.com/GEO/ and github.com/GEO-optim/GEO | 10,000 queries | "GEO can boost visibility by up to 40%"; Quotation Addition +41%, Statistics Addition +33%, Cite Sources +28%, Fluency +29% (Position-Adjusted Word Count); Perplexity.ai real-world +37% Subjective Impression, +22% Position-Adjusted Word Count | Not independently replicated in this cluster's pulls; critiqued (not replicated) by the critical survey below | 3 |
| GEO-Bench (Nimase et al.) | `d-seeding-geo-bench-2026-09-22.md` | Llama-3.1-8B-Instruct (target); Vicuna-7B (perplexity reference) | Not stated | Yes — code and 5 benchmark datasets at github.com/glad-lab/geobench | Datasets range 30–16,360 items | "Authoritative rewriting ties LLM Guidance for the highest NRG (0.83)... on C-SEO Bench" | Not stated | 4 |
| SafeGEO (Wen et al.) | `d-seeding-safegeo-2026-09-22.md` | Gemma 4 31B IT, Qwen3.6-27B, Devstral Small 2 24B Instruct, DeepSeek-V4-Flash | Not stated | Yes — code (Apache 2.0) and dataset (CC-BY 4.0) on GitHub/HuggingFace | 600 recommendation cases × 22 attack variants | "elevate flawed products' inclusion rates by up to 83.2 percentage points"; best defense "up to 39.2 pp" reduction, does not restore baseline | Not stated | 4 |
| Answer Bubbles (Huang et al., EMNLP 2026) | `d-seeding-answer-bubbles-2026-09-22.md` | GPT-4o-mini (two configs), Grok-4-1 (via Perplexity), Google AI Overviews/Search (version undisclosed) | Not stated in extracted passages | Query source published: Google Natural Questions corpus; code at github.com/scuba-illinois/answer-bubbles-audit | 11,000 queries | Wikipedia overrepresented +2.6pp (SearchGPT) / +5.4pp (Google AIO); Reddit underrepresented, diff=-0.221, p<.001, n=149 | Peer-reviewed (EMNLP 2026) — not independent replication of this specific finding | 3 |
| What Gets Cited (Vishwakarma et al.) | `d-seeding-what-gets-cited-2026-09-22.md` | Gemini-2.5-Flash, GPT-5-Nano, GPT-5-Mini, GPT-5.2, Claude-3.5-Sonnet, Kimi-K2-Thinking | Not stated (paper dated 25 May 2026) | Abstract claims release; no protocol/checklist URL found on inspection (2026-09-22) | 252,000 trials, 18 factors | "topical relevance and list position are the biggest drivers of being cited first... price information and a recent timestamp also helps consistently" | Not stated | 5 (vendor-authored, flagged) |
| Dominate AI Search (Chen et al.) | `d-seeding-dominate-ai-search-2026-09-22.md` | Not individually named per engine; aggregate "AI Search" (ChatGPT, Perplexity, Gemini) vs. Google | Reddit data collected August 2025; no other window stated | No code/data/query-set release found | 1,000 consumer ranking prompts (10×100) + 100 base queries × 6 languages × 8 paraphrase templates | Automotive/Canada: AI Search 69.1% Earned vs. Google 40.6% Earned; Consumer Electronics/USA: AI Search 92.1% Earned vs. Google 54% Earned | Not stated | 5 |
| UK iGaming report (secondary figures) | `d-seeding-igaming-notability-2026-09-22.md` | Not independently tested; cites secondary figures attributed to "Aggarwal, Muralidhar, and Nagar (2024)" (author-list discrepancy vs. the actual foundational paper, noted in the raw file) | Not documented | No | ~10,000 queries (as cited, not re-verified) | Cite Sources +40% (p<0.01), Statistics Addition +37% (p<0.01), Quotation Addition +22% (p<0.05), Keyword Stuffing +3% (n.s.) | This is itself an uncredited restatement of the foundational paper's figures, not a replication | 5 (vendor-authored, flagged) |
| Incumbent Advantage (seed paper) | `d-seeding-incumbent-advantage-2026-09-22.md` | GPT-4o-mini, Claude Sonnet, Gemini 3 Flash | Not stated | No — no code/data release found | 670–14,395 valid trials per experiment (see raw file) | Conditional Monopoly IAI=10.0 (100%); Authority-language Bias Surplus Value +0.17 rating points; payoff collapse +0.802 → +0.007 | Not stated (skincare-only; robustness check on 2 search goods replicates the monopoly/step-function pattern only) | 5 |
| McKelvey playbook | `d-seeding-justinmckelvey-playbook-2026-09-22.md` | Not disclosed (DataForSEO dataset, engine identity ChatGPT/Perplexity, no model version) | Single snapshot, DataForSEO pull dated 2026-07-31 (not a before/after window) | Query list not published | 90+ queries, 405–24,130 mentions across two spaces | Citation counts by domain (see raw file); own expert blog: 14 Perplexity citations, 0 ChatGPT citations | No | 5 |
| SolCrys citation study | `d-seeding-solcrys-citations-2026-09-22.md` | Not disclosed (ChatGPT, Perplexity, Google AI Overviews, Gemini named; no model versions) | 30-day window, pre-August-2026 (predates a stated "ChatGPT Reddit citation change"), page updated 2026-09-18 | 22-prompt set named ("AEO category") but prompts themselves not published | 1,936 responses, 2,219 domains, 17,551 citations | Top domains: Wikipedia 978, TechRadar 908, Reddit 785 (of 17,551 total); category shares given (see raw file) | No | 5 |

**H5 read from this table, factually stated, not scored here (scoring is Pass 9's):** every row above is a cross-sectional citation-share measurement or a controlled content-optimization benchmark. None is a true before-and-after test of the specific act of placing content into a third-party high-citation source (Wikipedia edit, Reddit post, press-release wire) with a baseline measured before that placement and again after. The closest is SolCrys's practitioner account, which is cross-sectional and names the tactic but does not report a before/after delta tied to a specific seeding action.

## (4) Engine statements — per engine, page and date, or unknown

| Engine | Statement | Page | Date | Raw path |
|---|---|---|---|---|
| Google | Names "scaled content abuse," "link spam," and "site reputation abuse" (third-party content hosted for the host's ranking credit) as prohibited. No section names "corpus seeding," Wikipedia/Reddit placement, or AI Overviews/AI Mode specifically | developers.google.com/search/docs/essentials/spam-policies | Last updated 2026-08-28 | `d-seeding-google-spam-policies-2026-09-22.md` |
| OpenAI | Usage Policies prohibit "deceit, fraud, scams, spam, or impersonation" under "Empower people," generically. No passage names search-ranking manipulation, AI-citation gaming, or corpus/third-party seeding | openai.com/policies/usage-policies/ | Effective 2025-10-29 | `docs/raw/b-openai-usage-policies-2026-09-22.md` (pre-existing Pass 2 pull, read not re-pulled) |
| Anthropic | Usage Policy (AUP) prohibits coordinating "malicious activity across multiple accounts," "spammy behavior" via automation, and "promot[ing] or facilitat[ing] the generation or distribution of spam." No passage names search-ranking manipulation, AI-citation gaming, or corpus/third-party seeding | anthropic.com/legal/aup | Effective 2025-09-15 | `docs/raw/b-anthropic-usage-policy-2026-09-22.md` (pre-existing Pass 2 pull, read not re-pulled) |
| Perplexity | `unknown — checked developers.google.com, openai.com, anthropic.com only in this cluster; Perplexity's own publisher/ad policy pages were not checked by this cluster 2026-09-22` — see `docs/sources/shortlist.md` P5-c7 (queued, not yet run) for the dedicated engine-countermeasure pass across priority-2 engines | — | — | — |
| Microsoft Copilot | `unknown — checked <none in this cluster> 2026-09-22`, routed to P5-c7 | — | — | — |
| Amazon (Rufus / Alexa for Shopping) | `unknown — checked <none in this cluster> 2026-09-22`, routed to P5-c7 | — | — | — |

**H13 read from this table, factually stated:** of the three engines checked by this cluster, none names "corpus seeding," Wikipedia/Reddit placement, or third-party high-citation-source manipulation as a distinct policy category. Google's "site reputation abuse" is the closest existing language, and it addresses the inverse direction (a host accepting third-party content for its own ranking credit), not a brand seeding an external site. This is a documented absence at the three engines checked, not a claim about the other three (Perplexity, Copilot, Amazon), which this cluster did not check.

## Per-vertical density — for H14

| Vertical | Items naming it | Raw paths |
|---|---|---|
| Skincare and beauty | 1 | `d-seeding-incumbent-advantage-2026-09-22.md` (seed paper; named vertical) |
| B2B SaaS | 0 direct; 1 adjacent, not identical | `d-seeding-justinmckelvey-playbook-2026-09-22.md` names "AI Consultant" and "Bookkeeping" services — B2B-services-adjacent but not literally named "B2B SaaS" by the source |
| High-CPA regulated (cards, insurance, supplements, loans, personal injury) | 0 direct; 1 adjacent, not identical | `d-seeding-igaming-notability-2026-09-22.md` names "iGaming" (UK gambling) — regulated and high-CPA in kind, but not one of the five named categories and not assigned to the cell by inference |
| None named | 9 | `d-seeding-geo-bench-2026-09-22.md`, `d-seeding-safegeo-2026-09-22.md`, `d-seeding-answer-bubbles-2026-09-22.md`, `d-seeding-what-gets-cited-2026-09-22.md`, `d-seeding-dominate-ai-search-2026-09-22.md` (names automotive and consumer electronics instead), `d-seeding-critical-survey-2026-09-22.md`, `d-seeding-geo-foundational-2026-09-22.md` (names 25 general domains, not a fixed vertical), `d-seeding-solcrys-citations-2026-09-22.md`, `d-seeding-google-spam-policies-2026-09-22.md` |

**H14 read from this table, factually stated, not scored here:** at equal-ish screen effort (one cluster, same search passes run across all sources without vertical-targeted queries), the anchor vertical (skincare) has exactly 1 item and the high-CPA regulated analogue (iGaming) has exactly 1 adjacent item; neither exceeds the other in this cluster's own count. This cluster alone cannot confirm or kill H14; it contributes one data point per vertical to whatever Pass 9 rolls up across P5-c1–c7.

## Screened-out — candidates examined, not pulled

**Academic (arXiv), 48 distinct items screened across 5 search passes, none pulled:**

Off-cluster — dense-retrieval / RAG corpus-poisoning security papers (a real technique, but adversarial-embedding attacks on a retrieval index the researchers control, not placement into a public high-citation platform; closer fit for P5-c3/P5-c6): 2410.06628, 2609.01325, 2504.17884, 2512.24268, 2606.11265, 2406.05087, 2503.21315, 2603.22934, 2501.04802 (9 items).

Off-cluster — GEO papers about a brand's own owned-content optimization, detection, or platform mechanism design (not third-party seeding): 2603.29979 (GEO-SFE), 2602.18455 (AI Overviews/Wikipedia traffic), 2606.20065 (GEO at Scale), 2609.02316 (Counter-GEO-Bench, a defense benchmark — candidate for P5-c7), 2608.29063 (Agent2UCB), 2608.27631 (Beyond the Vacuum), 2604.19113 (FeatGEO), 2604.19516 (MAGEO), 2609.07559 (Scoring Without the Engine), 2609.06811 (Measuring GEO Visibility), 2609.02964 (When Optimization Becomes Manipulation — defense, candidate for P5-c7), 2608.30466 (CHASE), 2608.16824 (GEO-Flag — detection/prevalence, not a seeding technique itself), 2608.11390 (Mechanism Design for Generative Engines), 2604.25707 (Citation Selection to Absorption), 2603.09296 (AgentGEO), 2507.03169 (Beyond SEO transformer), 2607.23893 (Who Gets Named — individual-naming study, cited as the seed paper's only Semantic Scholar citation) (18 items).

False-positive keyword matches (unrelated "engine" or "GEO" senses — combustion engines, jet engines, neural-network hardware engines, astrophysics central engines, honeypot engines, geospatial-ML "GEO-Bench" family): 2511.18178, 2510.16223, 2104.09630, 1511.05802, 2606.22283, 1207.0743, 2201.05326, 2410.18424, 1907.12473, 2507.00964, 2511.15658, 2604.10347, 2603.12762, 2503.20563, 2506.06281, 2503.10845, 2506.20174, 2605.03175, 2603.23408, 2411.19325, 2412.02732 (21 items).

**Practitioner write-ups found via search, not pulled (held — a later pass could pull these if the cluster reopens):** "How to Get Cited by ChatGPT Through Reddit: The 2026 Playbook" (medium.com/@candice_ervin); "Reddit GEO Playbook: How to Get Cited by ChatGPT and Perplexity in 2026" (medium.com/@tentenco — attempted, blocked: "Permission denied for reading page content on this domain" via claude-in-chrome browser, 2026-09-22); "How to Get Your Brand Cited by ChatGPT (2026 Playbook)" (llmpulse.ai); "How to Get Cited by ChatGPT (2026 Guide)" (redditgrow.ai); "How to Get Cited by ChatGPT Using Reddit in 2026" (medium.com/@mike_khorev); "How to Get Cited by ChatGPT: A Practical Guide for 2026" (geoclarity.io); "How to Get Your Site Cited by ChatGPT in 2026" (tryhikoo.com); "How to Get Cited by ChatGPT - A 2026 Guide" (gogochimp.com) — 8 items.

## Counts

| Count | Value |
|---|---|
| Raw pulls landed this cluster | 12 (`d-seeding-*-2026-09-22.md`) |
| Pre-existing raw pulls read, not re-pulled | 2 (`b-openai-usage-policies-2026-09-22.md`, `b-anthropic-usage-policy-2026-09-22.md`) |
| Academic items screened, not pulled | 48 |
| Practitioner items found, not pulled (held) | 8 |
| Total candidates examined | 70 |
| Items with a measured effect (any kind) | 10 of 12 (all except the Google spam-policy page and — partially — the critical survey, whose own measured finding is an *absence* of stable effect) |
| Items with both a published prompt set/query corpus and a stated n | 4 — foundational GEO paper, GEO-Bench, SafeGEO, Answer Bubbles (query source published; own prompt list not separately itemized in the extracted passages) |
| Items with a true before-and-after design (baseline measured, then re-measured after an intervention) | 0 in this cluster's 12 pulls — all are cross-sectional citation-share measurements or controlled-benchmark comparisons across conditions, not a pre/post test of one real seeding action |
| Highest tier reached | 3 (Answer Bubbles — peer-reviewed EMNLP 2026 + code; foundational GEO paper — peer-reviewed KDD 2024 + code/data) |
| Vendor-authored items (flagged) | 3 — What Gets Cited (Sprinklr), UK iGaming report (Interamplify), and both practitioner blog posts by commercial framing (see source_label in each raw file) |
| Engines with a stated countermeasure naming this technique | 0 of 3 checked (Google, OpenAI, Anthropic); 3 engines not checked by this cluster (Perplexity, Copilot, Amazon) |

## Unknowns

- `unknown — checked developers.google.com/search/docs/essentials/spam-policies 2026-09-22` on whether Google's general web-search spam policy governs AI Overviews/AI Mode citation selection specifically; the page does not scope itself either way.
- `unknown — checked <this cluster's search passes only> 2026-09-22` for Perplexity, Microsoft Copilot, and Amazon engine statements — routed to `docs/sources/shortlist.md` P5-c7 (queued, not yet run per `docs/method/STATE.md`).
- `unknown` whether any named brand has run and published a corpus-seeding campaign with a measured before-and-after result — no such case surfaced in 70 candidates examined; recorded as an absence with the screened count above, not asserted as a general absence in the category.
- `unknown` exact experiment-run date windows (as opposed to publication dates) for 8 of the 10 measured-effect rows in table (3) — most papers state a publication date but not a narrower data-collection window; recorded per-row in table (3) rather than guessed.
- `unknown` whether SolCrys and the two Medium/blog practitioner sites held in the screened-out list disclose a commercial affiliation beyond what their site framing suggests — not verified by this pull.

## Caveats

- This cluster's four-question tables answer Pass 5's questions for the "corpus seeding in high-citation sources" technique only; they do not score H5, H13, or H14 — scoring against `docs/method/hypotheses.md` decision conditions is Pass 9's task, against this file and the twelve raw pulls it cites.
- Every academic pull in this cluster is a preprint or a single peer-reviewed paper (tier 3–5); none is independently replicated by an unrelated party within this cluster's own pulls, per the academic tier table in `docs/method/trust-rubric.md`.
- Both practitioner sources (McKelvey, SolCrys) are cross-sectional citation-share snapshots from third-party citation-tracking tools (DataForSEO in McKelvey's case; tool not named in SolCrys's case) whose own underlying method is not independently verified here.
- No test was run against any third-party production answer surface, brand, or engine by this task, per the Lane D hard constraint in `docs/method/plan.md`.
