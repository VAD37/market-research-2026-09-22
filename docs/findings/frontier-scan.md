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
