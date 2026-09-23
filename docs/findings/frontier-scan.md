# Frontier scan — capabilities in the literature a party could abuse or monetise

| | |
|---|---|
| File date | 2026-09-23 |
| Oldest pull depended on | 2026-09-23 — every `raw/d-paper-*` cited. Oldest source publication carried: 2023-10-16, `raw/d-paper-token-auction-mechanism-2026-09-23.md` (WWW'24, pre-window, flagged) |
| Lane | D, plus the builder-constraint question (`findings/whitespace.md` line 52) |
| Hypotheses touched | H23, H24, H25 (scored below); H5, H13 restated beside existing marks |
| Claims at tier 3 or better | 6 of 9 |

## Question

> Which published capabilities in retrieval, recommendation, LLM advertising/auction, agentic commerce and answer-steering could a party abuse or monetise, and which run on public code and models without an engine partnership?

## Answer

Observations, not recommendations, and no verdict. The literature 2024–2026 documents four capability classes that (a) are demonstrated to move an LLM's recommendation, citation or purchase, (b) mostly run on public code and open or API-accessed models, and (c) are only partly covered by any priority-1 engine countermeasure: **content-side answer steering** (strategic text, persuasion-principle wording, structural/feature GEO, source-bias exploitation, RAG/evidence-ecosystem and multimodal-rank manipulation), **in-answer ad monetisation by auction** (token, segment, neuron, genre-VCG, optimal-stopping-timing, sponsored-clarifying-question), **agent-directed steering** (MCP tool-description preference, agent-skill policy steering, dark-pattern and description tweaks that move a buying agent's share), and **measurement/attribution** (stochastic brand-visibility metrics, clickstream/log incrementality, fair-attribution mechanisms). The monetisation mechanisms are the sharpest whitespace: every deployed P1 ad product keeps ads **separate and labelled** ("Ads are not integrated into responses" — OpenAI), whereas the papers auction placement **inside** the generated answer — a mechanism no P1 engine offers.

## Evidence — kept papers by capability class

| Capability class | Papers (tier) | Measured effect (verbatim, with n where stated) | Public code | P1 countermeasure named |
|---|---|---|---|---|
| Content answer-steering (organic) | strategic-text-sequence (4), bias-beware (3), mageo (3), mgeo (3), ecogeo (5), lazy-grounding (3), injection-paradox (4) | Bias-Beware: social-proof wording δRate "+334%" on Claude 3.5 Sonnet; MAGEO: engine-preference module worth "~19% on GPT 5.2"; EcoGEO/TRACE final recommendation rate "67.2%–73.9%", "+14.9 to +31.3 pp" over baselines; Injection-Paradox: Claude Opus 4.6 "54%→0% top-2… across all 50 trials" (suppression), GPT-4o-mini "17%→40%" (promotion) | 5 of 7 yes | generic only — Google spam policy names "manipulate generative AI responses" (2026-08-28); no engine names these specific techniques (`d-technique-census-c7`, E5) |
| In-answer ad monetisation by auction (paid) | token-auction (4), segment-auction-rag (4), neuron-auctions (5), genre-vcg (4), llm-osda (4), sponsored-questions (5), mosaic-truthful (5) | LLM-OSDA: "net revenue by 11%" over best fixed-timing baseline; genre-VCG clears "10^5 advertisers… ~1.25 seconds"; mechanisms auction placement inside generated text | 3 of 7 yes | none — no P1 ad product inserts auctioned ads into the answer (`markets/paid-placement.md`) |
| In-answer ad user studies (paid) | ads-conflicts (3), commercial-persuasion (4), ads-that-talk-back (3), detecting-native-ads (3) | Commercial-persuasion: sponsored selection "61.2% vs 22.4%", "Sponsored" label does not significantly reduce it, N=2,012; Ads-that-Talk-Back: "49.15% of participants did not realize… served an ad"; Ads-conflicts: Grok 4.1 Fast recommends pricier sponsored option "83%" | 4 of 4 yes | partial — labelling/independence stated by OpenAI, Microsoft, Google, Perplexity (`markets/paid-placement.md`) |
| Agent-directed steering (agentic) | mpma-mcp (3), skillshift (5), aces-ai-agent-buying (4), abxlab (3), magentic-marketplace (4), decepticon (4), ap2-red-team (5), protocol-attacks (5) | ACES: seller description tweak → market-share gain, significant in "33% of experiments"; SkillShift: attacker-favoured selection "81.33%" (shopping); Magentic: first-proposal "60–100%" selection; Decepticon: dark patterns steer agents ">70%" of tasks vs human 31% | 4 of 8 yes | partial — OpenAI MCP guide, Anthropic Agent-Skills security name malicious-server/skill and prompt injection; protocol-layer flaws unnamed |
| Measurement / attribution (cross) | maxshapley (3), brand-retrieval-eval (5), prompt-to-purchase (5), aeo-natural-experiment (5) | Prompt-to-Purchase: AI brand mention → same-name search "+4.3 pp [3.1,5.5]", panel; AEO natural experiment: intervention lift "1.82x (95% CI 1.31–2.54)" separated from platform tailwind; brand-retrieval: diagnostic cues raise BRP@5 "0%→81.3%" | 2 of 4 (2 vendor panels, aggregates only) | n/a — measurement, not a steering technique |
| Frontier capability / open-weight parity (cross) | agentfloor (4) | Open-weight gemma4:26b "equivalent to GPT-5 within a pre-registered margin" on routine tool-use; frontier gap remains only on long-horizon planning (E: GPT-5 10% vs 0%) | yes (released) | n/a |
| Countermeasures (defense) | counter-geo-bench (3), meta-secalign (4), camel (4), attacker-moves-second (4), defending-gemini (5) | Counter-GEO-Bench: off-the-shelf guardrails cut GEO-misinformation ASR "at most 5.7% relative"; a contrastive detector "47.6% relative"; Attacker-Moves-Second: adaptive attacks bypass "12 recent defenses… above 90%" that had reported near-zero | 4 of 5 yes | these ARE the engine/lab defenses (Google CaMeL & Gemini; Meta open) |

## Capability × property grid (descriptive)

| Capability class | Abusable | Monetisable | Runs on public code + models | Engine countermeasure named |
|---|---|---|---|---|
| Content answer-steering | yes (rank/citation/brand suppression shown) | indirectly (visibility-as-a-service) | yes — open weights (Llama/Qwen/Gemma) or public API | generic only (Google spam clause); specific techniques not named |
| In-answer ad auction | n/a (it is the monetisation) | yes (revenue mechanisms, IC pricing) | yes — theory + open-model demos | no — not offered by any P1 engine |
| In-answer ad user studies | yes (undetected persuasion) | yes | yes | partial (labelling/independence policies) |
| Agent-directed steering | yes (selection/share, protocol hijack) | yes (seller-side, sponsored-tool) | yes — public AP2/MCP stacks, open models | partial (malicious-server/skill guidance) |
| Measurement / attribution | no | yes (audit/attribution tooling) | yes (2 open) / vendor-panel (2) | n/a |
| Open-weight parity | n/a | n/a | yes (that is the finding) | n/a |
| Countermeasures | n/a | yes (defense tooling) | yes | these are the countermeasures |

## Builder-constraint reading (descriptive, no verdict)

Read against the papers only. Capabilities that need **no engine partnership**: content answer-steering (edits pages/corpora the builder controls; measured on open weights and public APIs — `strategic-text-sequence`, `bias-beware`, `mageo`, source-bias papers), measurement/attribution (runs on API sampling or opt-in clickstream — `brand-retrieval-eval`, `prompt-to-purchase`), agent-directed steering that acts on public protocol/skill/description surfaces (`mpma-mcp`, `skillshift`, `aces`, `ap2-red-team` on the public AP2 stack), and countermeasure/detection tooling (`counter-geo-bench`, `detecting-native-ads`, `meta-secalign`). Capabilities that **do** require the engine: in-answer ad monetisation by auction — every such mechanism assumes control of the generation/inference stack, which only the engine holds; papers demonstrate them on the authors' own open models, not on any P1 surface. `agentfloor` bears on the constraint directly: open-weight models reach GPT-5-level on routine tool-use, so a builder's non-frontier tasks need no frontier-model contract; long-horizon planning still favours frontier models.

## Claims

| # | Claim | Evidence | Tier | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | ≥1 peer-reviewed+code technique steers LLM recommendation and no P1 engine names a countermeasure to that specific technique | bias-beware (3), mageo (3), mgeo (3) vs `d-technique-census-c7` E5 + Google spam policy 2026-08-28 (generic) | 3 | n/a | yes (H23) |
| C2 | Papers describe in-answer ad-auction monetisation mechanisms that no P1 engine offers; P1 ads are separate/labelled | token/neuron/genre/segment/OSDA auctions (4–5) vs `markets/paid-placement.md` | 4 | n/a | yes (H24) |
| C3 | ≥1 kept capability runs on public code + open weights or a public API, no partner gate | strategic-text-sequence (4, github + Llama-2); meta-secalign (4, open model) | 4 | n/a | yes (H25) |
| C4 | Published before-and-after designs with prompt set and n now exist for content steering | strategic-text-sequence (4), bias-beware (3), injection-paradox (4) | 3 | n/a | yes (H5 restate) |
| C5 | A new P1 countermeasure names the manipulation class: Google spam policy covers "manipulate generative AI responses" (AI Overviews, AI Mode) | Google Search Central spam-policies page, last updated 2026-08-28 | 3 | n/a | yes (H13 restate) |

## Hypotheses

| ID | Mark | Basis (evidence at/above tier floor) |
|---|---|---|
| H23 | **confirmed** | bias-beware / mageo / mgeo (peer-reviewed, code, tier 3) steer recommendation; no P1 engine names these specific techniques (`d-technique-census-c7` E5, tier 3). Google's 2026-08-28 generic "manipulate generative AI responses" clause recorded side by side — names the class, not the technique; does not kill |
| H24 | **confirmed** | in-answer ad-auction mechanisms (token 2310.10826 t4; genre-VCG 2601.19435 t4; neuron 2605.08326 t5; OSDA 2608.00123 t4) describe placement inside the answer; every P1 ad doc (tier 3) states ads are separate/not integrated (`markets/paid-placement.md`) |
| H25 | **confirmed** | strategic-text-sequence (t4, github.com/aounon/llm-rank-optimizer, Llama-2 open weights) and meta-secalign (t4, open code+weights) run on public code and models, no engine partnership |
| H5 | restated — Pass-9 mark stands (`unresolved — checked` 2026-09-22 / review-1). Pass 14 supplies tier-3/4 published before-and-after with prompt set and n (bias-beware δRate pre/post; strategic-text-sequence before/after over 200 evals; injection-paradox 54%→0%, n=50/condition) — strengthens the confirm side, but all on benchmark/synthetic catalogs, not a production consumer surface (the review-1 distinction) | — |
| H13 | restated — Pass-9 mark **confirmed** stands. Pass 14 adds dated P1 statements: Google spam policy naming "manipulate generative AI responses" in AI Overviews/AI Mode (2026-08-28); OpenAI MCP-connectors guide naming malicious-server prompt injection; Anthropic Agent-Skills security naming malicious skills | — |

## Survivorship

The literature over-represents (i) organic GEO/citation steering (63 of 252 screened) and agentic-commerce security (78) — attack/benchmark papers are cheap to publish and cluster; (ii) results on retired or fast-moving model versions (GPT-4o, Claude 3.5, Gemini 2.0 appear beside GPT-5.x/Claude 4.x/Gemini 3.x — a 2024 result is evidence about 2024, rubric L33); (iii) auction/mechanism theory with synthetic or single open-model demos, not deployment. Defense papers that fail are rarely published, so the countermeasure set skews toward methods reporting success; `attacker-moves-second` (t4) is the counterweight, showing 12 published defenses fall to adaptive attack.

## Unknowns

| Question | Channel checked | Date | Why not answerable here |
|---|---|---|---|
| Venue-only papers with no arXiv mirror | arXiv API; ACM DL / IEEE Xplore / OpenReview reached only via arXiv mirrors | 2026-09-23 | direct proceedings crawl not run this pass; count is arXiv-reachable only |
| Whether any kept technique has been independently replicated (would raise to tier 2) | Semantic Scholar citations API (rate-limited, 429s) | 2026-09-23 | citation trails returned some replication-adjacent titles but no unrelated-party replication of a specific kept technique confirmed; no tier-2 row |
| Whether the OpenAI Atlas prompt-injection hardening post names any Pass-5 technique | openai.com/index/hardening-atlas (403 fetch; Cloudflare challenge in browser) | 2026-09-23 | primary page unreachable; secondary reporting only, not pulled as a number |
| Live effect of any technique on a current P1 consumer surface | none — Lane D rule forbids running techniques | 2026-09-23 | out of scope by construction; papers measure on their own harnesses |

## Caveats

- Preprints dominate: 25 of 38 kept papers are tier 4–5 (preprint, or vendor-authored on own product). Tiers rank provenance, not correctness (`trust-rubric.md`).
- No execution content: every `d-paper-*` file carries the abstract and result sentences verbatim; no prompt text, payload, or step list that would operationalise a technique is reproduced (Lane D rule). Attack artefacts are cited by arXiv id only.
- Model versions matter: measured effects sit on the model named in each file; a result on a retired model bounds nothing about a current one.
- Vendor-authored measurement (`prompt-to-purchase` — Scrunch AI; `aeo-natural-experiment` — Glasp; `defending-gemini` — Google DeepMind; `aces` — two MyCustomAI authors) is tier 5 / bias-flagged in each file, kept per rubric as evidence about the category, not as an independent number.
- H23/H24/H25 confirmed says nothing about whether any party can win a market; that verdict is the user's (`hypotheses.md` H25 caveat, `MegaPlan.md` line 17). This file produces evidence, not a go/no-go.
- H23's confirm and Google's generic anti-manipulation clause stand side by side, not reconciled: the clause names the manipulation class, not the specific peer-reviewed technique.
- Kill-on-absence rows (H23, H24) are only as strong as the P1 documents checked (`d-technique-census-c7` plus the Google spam, OpenAI MCP, Anthropic Agent-Skills pages read 2026-09-23); an absence with no channel list is not a kill.

## Manipulation evidence ledger — added 2026-09-24

Lane D orphan sweep (GAP-D): 48 raw files, one row each. Figures are paper-reported (analyst-derived) unless the tier cell says company-stated or vendor. Publication dates; every raw pulled 2026-09-22/23. Figures already quoted above are not restated; rows carry what is new.

| Family | Paper / source | Effect figure | Setup | Date | Tier | Raw |
|---|---|---|---|---|---|---|
| Retrieved-content injection | Greshake et al., indirect PI | none stated; attacks "demonstrate[d]" on Bing GPT-4 Chat | real + synthetic GPT-4 apps | 2023-02-23 | 5 | `raw/d-injection-greshake-foundational-ipi-2026-09-22.md` |
| Retrieved-content injection | Nestaas, Debenedetti, Tramèr — Preference Manipulation | none stated; promotes attacker, discredits competitors | Bing, Perplexity; GPT-4, Claude plugin APIs | 2024-06-26 | 5 | `raw/d-injection-nestaas-adversarial-seo-2026-09-22.md` |
| Retrieved-content injection | Pfrommer et al. (EMNLP 2024) | none stated; "reliably promotes low-ranked products" | product-site dataset; transfers to perplexity.ai | 2024-06-05 | 3 | `raw/d-injection-pfrommer-ranking-manipulation-2026-09-22.md` |
| Retrieved-content injection | Yin et al. (SIGIR 2026), LLM rankers | none in abstract; encoder-decoder rankers "strong inherent resilience" | pairwise/listwise/setwise rankers; ASR, nDCG@10 | 2026-02-18 | 3 | `raw/d-injection-yin-llm-rankers-2026-09-22.md` |
| Retrieved-content injection | PoisonedRAG (USENIX Sec 2025) | "90% attack success rate", 5 texts per question | own corpus, "millions of texts"; defenses insufficient | 2024-02-12 | 3 | `raw/d-injection-poisonedrag-2026-09-22.md` |
| Retrieved-content injection | Injection Paradox (second condition) | Opus 54%→8% (−46 pp); Sonnet 26%→8% | beside 54%→0% above; condition differs | 2026-06-08 | 4 | `raw/d-paper-injection-paradox-brand-suppression-2026-09-23.md` |
| Retrieved-content injection | Lazy Grounding (EMNLP 2026) | accuracy −5.9 pts mean, −17.3 max | 12 model-benchmark pairs; GPT-5 Mini, Tongyi | 2026-08-31 | 3 | `raw/d-paper-lazy-grounding-search-agents-2026-09-23.md` |
| Retrieved-content injection | Choi et al., agent data injection | none stated; bypasses IPI defenses | Claude in Chrome, Antigravity, Claude Code, Codex, Gemini CLI | 2026-07-06 | 5 | `raw/d-injection-choi-agent-data-injection-2026-09-22.md` |
| Retrieved-content injection | Chen et al., IPI-proxy (tooling) | none — 820-string red-team library | deployer's own whitelisted domains | 2026-05-12 | 4 | `raw/d-injection-chen-ipi-proxy-2026-09-22.md` |
| Retrieved-content injection | Brave disclosure, Perplexity Comet | none — exfiltration demo; fix incomplete 2025-08-20 | shipping consumer browser; Brave is rival | 2025-08-20 | 4 · company-stated | `raw/d-injection-brave-comet-disclosure-2026-09-22.md` |
| Content GEO / source bias | MAGEO (ACL 2026 Findings) | skill-bank removal "~13% drop" | GPT-5.2, Gemini-3 Pro, Qwen-3 | 2026-04-21 | 3 | `raw/d-paper-mageo-multi-agent-geo-2026-09-23.md` |
| Content GEO / source bias | MGEO (KnowFM @ ACL 2026) | none numeric; exceeds unimodal attacks | Qwen2.5-VL-7B ranker | 2026-01-18 | 3 | `raw/d-paper-mgeo-multimodal-rank-2026-09-23.md` |
| Content GEO / source bias | Perplexity Trap (ICLR 2025) | cause: low perplexity; debias costs <2 pp | BERT/Contriever retrievers; LLM corpora | 2025-03-11 | 3 | `raw/d-paper-perplexity-trap-source-bias-2026-09-23.md` |
| Content GEO / source bias | Training-induced bias (ECIR 2026) — contra | perplexity agreement near 50%; Contriever SciFact 42.2% | cause: fine-tuning data, not perplexity | 2026-02-11 | 3 | `raw/d-paper-training-induced-source-bias-2026-09-23.md` |
| Content GEO / source bias | Brand retrieval eval | L.L.Bean BRP@5 0%→88.5% with cues | six LLMs incl. GPT-5.5, Claude Opus 4.7 | 2026-09-14 | 5 | `raw/d-paper-brand-retrieval-ranking-eval-2026-09-23.md` |
| Structured data | Volpini et al. (WordLift) | entity pages +29.6% std RAG, +29.8% agentic | 349 queries, 4 domains; Gemini 2.5 Flash | 2026-03-11 | 5 · vendor | `raw/d-structured-arxiv-volpini-rag-2026-09-22.md` |
| Structured data | Volpini — JSON-LD alone | accuracy 3.62→3.89, "modest" (C1→C2) | same; e-commerce domain at ceiling | 2026-03-11 | 5 · vendor | same file |
| Structured data | llms.txt spec v2 (Answer.AI) | claim only: "thousands of sites"; Lighthouse audits for it | no n, no method | 2026-08-10 | 3 · company-stated | `raw/d-structured-llmstxt-org-spec-2026-09-22.md` |
| Structured data | Redocly CEO blog | claim only: no tested model "spontaneously" read llms.txt | no n, no models named; category noise | 2025-08-20 | 6 · company-stated | `raw/d-structured-redocly-overhyped-2026-09-22.md` |
| Structured data | Schema.org About | no effect; founders Google, Microsoft, Yahoo, Yandex | no AI-engine consumption statement | undated | 3 · company-stated | `raw/d-structured-schemaorg-about-2026-09-22.md` |
| Agent-directed steering | ABxLab (ICLR 2026) | attribute sensitivity 13–31% vs humans ~7% | 17 models, web shopping env | 2025-09-30 | 3 | `raw/d-paper-abxlab-agent-consumer-choice-2026-09-23.md` |
| Agent-directed steering | ACES | share +14.89 pp GPT-5.1; +0.32 Gemini 3 Pro | seller description tweak; 6 buying models | 2025-08-04 | 4 · MyCustomAI | `raw/d-paper-aces-ai-agent-buying-2026-09-23.md` |
| Agent-directed steering | ACES — tags | "Sponsored" 10%→7.9–8.9%; "Overall Pick" →19.9–42.6% | Claude Sonnet 4, GPT-4.1, Gemini 2.5 Flash | 2025-08-04 | 4 · MyCustomAI | same file |
| Agent-directed steering | Magentic Marketplace | Qwen3-4B third-listed 57.1–66.7%; 10–30x speed advantage | two-sided simulated market | 2025-10-27 | 4 · Microsoft | `raw/d-paper-magentic-marketplace-2026-09-23.md` |
| Agent-directed steering | MPMA (AAAI) | "Best Description" 100% ASR "almost all settings" | GPT-4o, Claude 3.7, Gemini 2.5 Flash, Grok-3 | 2025-05-16 | 3 | `raw/d-paper-mpma-mcp-preference-2026-09-23.md` |
| Agent-directed steering | SkillShift | shopping PSR 37.33%→81.33%; scanners fail to detect | GPT-5.5, Gemini 3-Flash, Claude Haiku 4.5 | 2026-09-02 | 5 | `raw/d-paper-skillshift-agent-skills-2026-09-23.md` |
| Agent-directed steering | Decepticon | >70% dark-pattern steering vs human 31% | 700 tasks; larger models more susceptible | 2025-12-28 | 4 | `raw/d-paper-decepticon-dark-patterns-2026-09-23.md` |
| Agent-directed steering | AP2 red team (IMNS 2026) | ranking manipulation 100%, 10 of 10 trials | AP2 agent on Gemini-2.5-Flash | 2026-01-30 | 5 | `raw/d-paper-ap2-red-team-prompt-inj-2026-09-23.md` |
| Agent-directed steering | Protocol attacks (AIP-Bench) | 33 vulns, 100% ASR; semantic: Claude 0%, GPT-4o-mini 99–100% | 3 platforms, single author | 2026-07-23 | 5 | `raw/d-paper-protocol-attacks-agentic-commerce-2026-09-23.md` |
| In-answer ads: behaviour | Ads conflicts (COLM 2026) | sponsored rec: Claude 4.5 Opus 28%; high-SES 64.1% vs low 48.6% | 23 LLMs | 2026-04-09 | 3 | `raw/d-paper-ads-conflicts-of-interest-2026-09-23.md` |
| In-answer ads: behaviour | Ads that Talk Back (IMWUT 2025) | ads cut performance ≤3%; 35.2% believed they detect ads | n=179; GPT-4o family | 2024-09-23 | 3 | `raw/d-paper-ads-that-talk-back-2026-09-23.md` |
| In-answer ads: behaviour | Commercial persuasion | label + briefing: 61.2%→55.5% [50.6, 60.4] | N=2,012 preregistered; 5 frontier models | 2026-04-05 | 4 | `raw/d-paper-commercial-persuasion-experiment-2026-09-23.md` |
| In-answer ads: behaviour | Detecting native ads (WWW 2024) | sentence transformers P/R >0.9; LLMs "struggle" | GPT-4, Mistral-7B | 2024-02-07 | 3 | `raw/d-paper-detecting-native-ads-2026-09-23.md` |
| Ad auction mechanism | Genre-VCG ad insertion | survey: 4.2% acceptable, 64.6% unacceptable | 36 raters; judge ρ≈0.66 | 2026-01-27 | 4 | `raw/d-paper-genre-ad-insertion-vcg-2026-09-23.md` |
| Ad auction mechanism | LLM-OSDA | iterative refinement +14–19% revenue | simulated corpus; Qwen3-4B | 2026-07-31 | 4 | `raw/d-paper-llm-osda-dynamic-auction-2026-09-23.md` |
| Ad auction mechanism | MOSAIC truthful aggregation | none numeric; "high advertiser value" | Llama-2-7b-chat | 2024-05-09 | 5 | `raw/d-paper-mosaic-truthful-llm-ad-auction-2026-09-23.md` |
| Ad auction mechanism | Neuron Auctions | none numeric; brand neurons ~orthogonal | Llama-3-8B, Qwen3-4B | 2026-05-08 | 5 | `raw/d-paper-neuron-auctions-2026-09-23.md` |
| Ad auction mechanism | Segment auction RAG (NeurIPS 2024) | none numeric; log-welfare maximising | gpt-4-turbo | 2024-06-12 | 4 | `raw/d-paper-segment-auction-rag-ads-2026-09-23.md` |
| Ad auction mechanism | Sponsored questions | theory: modular design Price of Anarchy unbounded | no model | 2025-12-03 | 5 | `raw/d-paper-sponsored-questions-auction-2026-09-23.md` |
| Measurement | Prompt-to-Purchase (Scrunch AI) | recall 7d +2.08 pp; retail 7d +0.52 pp | opt-in clickstream + chats; no transactions | 2026-06-09 | 5 · vendor | `raw/d-paper-prompt-to-purchase-clickstream-2026-09-23.md` |
| Measurement | AEO natural experiment (Glasp) | raw 5.7x vs untreated 3.5x; placebo p=0.16 | single domain, server logs | 2026-06-03 | 5 · vendor | `raw/d-paper-aeo-natural-experiment-referral-2026-09-23.md` |
| Measurement | MaxShapley | Jaccard >0.85 at <6% token cost | HotPotQA, MuSiQUE, MS MARCO | 2025-12-05 | 3 or 4 (file conflicts) | `raw/d-paper-maxshapley-fair-attribution-2026-09-23.md` |
| Measurement | AgentFloor | gemma4:26b ~15x cheaper per passed task than GPT-5 | 16,542 runs, 30 tasks | 2026-05-01 | 4 | `raw/d-paper-agentfloor-open-weight-ladder-2026-09-23.md` |
| Defense | CaMeL (Google) | 77% tasks solved securely vs 84% undefended | AgentDojo | 2025-03-24 | 4 · Google | `raw/d-paper-camel-design-defense-2026-09-23.md` |
| Defense | Narisetty et al., Progent reproduction | ASR 25.8%→4.2%; adaptive attack 2.6% | AgentDojo, Qwen2.5-7B, 3 runs | 2026-06-25 | 5 | `raw/d-injection-narisetty-oob-defenses-2026-09-22.md` |
| Defense | Attacker Moves Second | 12 defenses bypassed, ASR >90% "for most" | GPT-5, Gemini-2.5, Grok 4 | 2025-10-10 | 4 | `raw/d-paper-attacker-moves-second-2026-09-23.md` |
| Defense | Defending Gemini (DeepMind) | none numeric; continuous adaptive evaluation | Gemini 2.0, 2.5 | 2025-05-20 | 5 · Google | `raw/d-paper-defending-gemini-ipi-2026-09-23.md` |
| Engine statement | Google, "Mitigating prompt injection" | none; five defense layers, no rates | Gemini, Gemini in Workspace | 2025-06-13 | 3 · company-stated | `raw/d-injection-google-mitigating-pi-2026-09-22.md` |
| Engine statement | Microsoft Copilot Bounty | PI out of scope absent impact on others; $250–$30,000 | Copilot surfaces | 2026-04-07 | 3 · company-stated | `raw/d-injection-microsoft-copilot-bounty-2026-09-22.md` |

Superseded, not rowed: `raw/d-structured-llmstxt-directory-count-2026-09-22.md` (3,829 websites, 2026-09-22) — 3,830 on 2026-09-23 already in `findings/market-potential.md` from `raw/e-wayback-llms-txt-directories-2026-09-23.md`.

Count, 48 files: 29 carry a measured effect figure (26 papers, PoisonedRAG, Narisetty, Volpini); 15 state an effect in words only (7 injection sources, 6 papers, llms.txt spec, Redocly); 4 claim no effect (Google, Microsoft, Schema.org, directory count). Greshake, Nestaas, Pfrommer, Yin effect rates: `unknown — checked raw abstract pulls 2026-09-24`; full text never pulled.

### Caveats — ledger

- Lab, not production: only Nestaas (Bing, Perplexity), Pfrommer (perplexity.ai transfer), Choi (named agents) and Brave (Comet) touch shipping surfaces; none of those raws gives a rate.
- Model versions: rows span GPT-4 (2023) to GPT-5.5 / Claude Opus 4.7 (2026); an effect bounds only the model named.
- Vendor self-report: Volpini (WordLift; own blog a test domain), Prompt-to-Purchase (Scrunch AI), AEO experiment (Glasp), ACES (MyCustomAI), CaMeL and Defending Gemini (Google), Magentic (Microsoft), Brave (rival browser). Redocly is tier 6: noise, not a number; its negative result runs against its own shipped feature.
- Conflicts side by side: source-bias cause (Perplexity Trap: perplexity; ECIR 2026: fine-tuning data); Injection Paradox Opus 54%→0% vs 54%→8% (two conditions, one paper); Protocol-attacks Claude impact 0% vs Injection Paradox Claude suppression (different tasks); MaxShapley raw lists tier 3 and "kept conservative at 4".
- ASR is each author's metric on each author's harness; definitions differ (AP2: injected product ranked first, n=10).
- No payload, prompt text or step list is reproduced (Lane D rule).
