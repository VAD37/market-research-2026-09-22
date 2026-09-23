# Lane D paper census — Pass 14 frontier scan (2026-09-23)

```yaml
source:          arXiv API (export.arxiv.org/api/query) + WebSearch + Semantic Scholar citation graph, compiled 2026-09-23
url_or_doc_id:   n/a — census compiled from the pulls listed below
published:       n/a
pull_date:       2026-09-23
pull_method:     fetch (arXiv API listings/search; Semantic Scholar citations API; WebSearch for coverage gaps)
pull_purpose:    evidence about a number
tier:            n/a — each kept paper carries its own tier in its d-paper-*-2026-09-23.md file
source_label:    n/a — mixed
lane:            D
sub_market:      cross (organic recommendation, paid placement, agentic commerce)
metric_kind:     none
supersedes:      none — extends Lane D censuses c1–c7 (2026-09-22); no paper already filed in a d-* file was re-screened here
captured:        every paper screened this pass, with topic group, date, and kept/dropped reason
window:          2024-01 to 2026-09 (papers outside flagged in-row)
```

Lane D hard constraint: research into manipulation is described, never operationalised. No technique was run against any engine, brand, or third-party surface. Rows record method class, measured effect, model and date only.

## Screening summary

- Screened: **252** papers (arXiv API across cs.IR, cs.CL, cs.AI, cs.CY, cs.CR, cs.GT, econ.TH; plus Semantic Scholar citation trails and WebSearch coverage checks). Additional titles surfaced by WebSearch that duplicated arXiv hits are not double-counted.
- Kept: **38** (one `d-paper-*-2026-09-23.md` file each).
- By topic group (screened / kept): T1 steer recommendation/citation 63/13 · T2 ads in LLM answers 54/9 · T3 agentic commerce 78/8 · T4 measurement/attribution 13/2 · T5 frontier capability 30/2 · T6 countermeasures 14/4.
- Kept by tier: **tier 2 — 0 · tier 3 — 13 · tier 4 — 14 · tier 5 — 11**. (No replicated+peer-reviewed+code paper found, so no tier-2 academic row.)
- Topic-group tag: T1–T6 per the pass brief's six screen topics.

## Census table — every paper screened

| arXiv id | date | topic | title | kept / dropped (reason) |
|---|---|---|---|---|
| 1412.0879 | 2014-12-02 | T1 | Watsonsim: Overview of a Question Answering Engine | dropped — pre-window / historical QA, not in scope |
| 2209.11801 | 2022-09-14 | T1 | Solutions to preference manipulation in recommender systems require kn | dropped — attack/defense near-duplicate of kept countermeasure/steering papers |
| 2310.20501 | 2023-10-31 | T1 | Neural Retrievers are Biased Towards LLM-Generated Content | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2311.09735 | 2023-11-16 | T1 | GEO: Generative Engine Optimization | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2402.14836 | 2024-02-18 | T1 | Stealthy Attack on Large Language Model based Recommendation | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2403.15105 | 2024-03-22 | T1 | SAGraph: A Large-Scale Social Graph Dataset with Comprehensive Context | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2404.07981 | 2024-04-11 | T1 | Manipulating Large Language Models to Increase Product Visibility | **KEPT** t4 — `d-paper-strategic-text-sequence` |
| 2405.16546 | 2024-05-26 | T1 | Cocktail: A Comprehensive Information Retrieval Benchmark with LLM-Gen | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2406.13997 | 2024-06-20 | T1 | "Global is Good, Local is Bad?": Understanding Brand Bias in LLMs | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2502.01349 | 2025-02-03 | T1 | Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Reco | **KEPT** t3 — `d-paper-bias-beware-cognitive-bias` |
| 2503.08684 | 2025-03-11 | T1 | Perplexity Trap: PLM-Based Retrievers Overrate Low Perplexity Document | **KEPT** t3 — `d-paper-perplexity-trap-source-bias` |
| 2503.10728 | 2025-03-13 | T1 | DarkBench: Benchmarking Dark Patterns in Large Language Models | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2503.24228 | 2025-03-31 | T1 | PAARS: Persona Aligned Agentic Retail Shoppers | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2504.06435 | 2025-04-08 | T1 | Human Trust in AI Search: A Large-Scale Experiment | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2505.11154 | 2025-05-16 | T1 | MPMA: Preference Manipulation Attack Against Model Context Protocol | **KEPT** t3 — `d-paper-mpma-mcp-preference` |
| 2505.21849 | 2025-05-28 | T1 | Xinyu AI Search: Enhanced Relevance and Comprehensive Results with Ric | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2507.05301 | 2025-07-07 | T1 | News Source Citing Patterns in AI Search Systems | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2508.17715 | 2025-08-25 | T1 | How Do LLM-Generated Texts Impact Term-Based Retrieval Models? | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2509.08919 | 2025-09-10 | T1 | Generative Engine Optimization: How to Dominate AI Search | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2509.10762 | 2025-09-13 | T1 | AI Answer Engine Citation Behavior An Empirical Analysis of the GEO16  | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2511.05797 | 2025-11-08 | T1 | When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbo | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2511.20867 | 2025-11-25 | T1 | E-GEO: A Testbed for Generative Engine Optimization in E-Commerce | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2601.00869 | 2025-12-30 | T1 | Cultural Encoding in Large Language Models: The Existence Gap in AI-Me | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2601.01750 | 2026-01-05 | T1 | When Attention Becomes Exposure in Generative Search | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2601.12263 | 2026-01-18 | T1 | Multimodal Generative Engine Optimization: Rank Manipulation for Visio | **KEPT** t3 — `d-paper-mgeo-multimodal-rank` |
| 2601.13938 | 2026-01-20 | T1 | IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative E | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2602.02961 | 2026-02-03 | T1 | Generative Engine Optimization: A VLM and Agent Framework for Pinteres | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2602.10833 | 2026-02-11 | T1 | Training-Induced Bias Toward LLM-Generated Content in Dense Retrieval | **KEPT** t3 — `d-paper-training-induced-source-bias` |
| 2602.12187 | 2026-02-12 | T1 | SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented G | dropped — industrial recommender internals, not answer-steering by outside party |
| 2603.09296 | 2026-03-10 | T1 | Diagnosing and Repairing Citation Failures in Generative Engine Optimi | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2603.12282 | 2026-03-05 | T1 | Algorithmic Trust and Compliance: Benchmarking Brand Notability for UK | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2603.18300 | 2026-03-18 | T1 | Auditing Preferences for Brands and Cultures in LLMs | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2603.20062 | 2026-03-20 | T1 | The End of Rented Discovery: How AI Search Redistributes Power Between | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2603.20213 | 2026-03-02 | T1 | AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optim | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2603.29979 | 2026-03-31 | T1 | Structural Feature Engineering for Generative Engine Optimization: How | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2604.03656 | 2026-04-04 | T1 | Beyond Retrieval: Modeling Confidence Decay and Deterministic Agentic  | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2604.06163 | 2026-04-07 | T1 | Data, Not Model: Explaining Bias toward LLM Texts in Neural Retrievers | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2604.07585 | 2026-04-08 | T1 | Don't Measure Once: Measuring Visibility in AI Search (GEO) | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2604.19516 | 2026-04-21 | T1 | From Experience to Skill: Multi-Agent Generative Engine Optimization v | **KEPT** t3 — `d-paper-mageo-multi-agent-geo` |
| 2604.25707 | 2026-04-28 | T1 | From Citation Selection to Citation Absorption: A Measurement Framewor | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2605.12887 | 2026-05-13 | T1 | EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Searc | **KEPT** t5 — `d-paper-ecogeo-evidence-ecosystem` |
| 2605.21948 | 2026-05-21 | T1 | SCI-Defense: Defending Manipulation Attacks from Generative Engine Opt | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2605.25517 | 2026-05-25 | T1 | What Gets Cited: Competitive GEO in AI Answer Engines | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2605.29107 | 2026-05-27 | T1 | GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Opti | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2606.04362 | 2026-06-03 | T1,T4 | Disentangling Answer Engine Optimization from Platform Growth: A Log-B | **KEPT** t5 — `d-paper-aeo-natural-experiment-referral` |
| 2606.09204 | 2026-06-08 | T1 | The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM R | **KEPT** t4 — `d-paper-injection-paradox-brand-suppression` |
| 2606.12439 | 2026-05-18 | T1 | Position: Generative Engine Optimization Creates Underexamined Risks,  | dropped — survey/position (cited context, not a primary capability result) |
| 2606.20065 | 2026-06-18 | T1 | Generative Engine Optimization at Scale: Measuring Brand Visibility Ac | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2606.21121 | 2026-06-19 | T1 | Answer Engineering: Local Trajectory Editing for Protocol-Constrained  | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2606.23165 | 2026-06-22 | T1 | The Language Blind Spot: How Query Language and Brand Recognition Tier | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2606.25787 | 2026-06-24 | T1 | How Large Language Models Source Brand Reputation Across Languages and | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2606.28356 | 2026-06-08 | T1 | SafeGEO: Understanding Generative Engine Optimization Risks in Recomme | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2607.14035 | 2026-07-15 | T1 | Optimizing Visibility in Generative Engines: A Critical Survey of Gene | dropped — industrial recommender internals, not answer-steering by outside party |
| 2607.21951 | 2026-07-24 | T1 | SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulatio | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2608.04565 | 2026-08-05 | T1 | Breadcrumbing Search Agents | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2608.27631 | 2026-08-27 | T1 | Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Awa | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2608.29063 | 2026-08-29 | T1 | Agent2UCB: Agentic System for Generative Engine Optimization | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2608.30303 | 2026-08-31 | T1 | Lazy Grounding: Attacking Search Agents with Factual Evidence | **KEPT** t3 — `d-paper-lazy-grounding-search-agents` |
| 2609.02316 | 2026-09-02 | T1,T6 | Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting  | **KEPT** t3 — `d-paper-counter-geo-bench-defense` |
| 2609.02964 | 2026-09-02 | T1 | When Optimization Becomes Manipulation: Defending Generative Search ag | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2609.16304 | 2026-09-14 | T1 | Evaluating Brand Retrieval and Ranking in Large Language Model Recomme | **KEPT** t5 — `d-paper-brand-retrieval-ranking-eval` |
| 2609.23162 | 2026-09-19 | T1 | From Prompt to Recommendation: A Fitted Stage Model of Brand Visibilit | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| cs/0107006 | 2001-07-03 | T1 | Looking Under the Hood : Tools for Diagnosing your Question Answering  | dropped — pre-window / historical QA, not in scope |
| 2301.13794 | 2023-01-31 | T2 | Auctions with Tokens: Monetary Policy as a Mechanism Design Choice | dropped — payment-rail cryptography, not recommendation/ad steering |
| 2310.10826 | 2023-10-16 | T2 | Mechanism Design for Large Language Models | **KEPT** t4 — `d-paper-token-auction-mechanism` |
| 2311.07601 | 2023-11-11 | T2 | Online Advertisements with LLMs: Opportunities and Challenges | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2402.04889 | 2024-02-07 | T2 | Detecting Generated Native Ads in Conversational Search | **KEPT** t3 — `d-paper-detecting-native-ads` |
| 2402.14590 | 2024-02-07 | T2 | Scaling Up LLM Reviews for Google Ads Content Moderation | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2403.15214 | 2024-03-22 | T2 | InstaSynth: Opportunities and Challenges in Generating Synthetic Insta | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2404.08126 | 2024-04-11 | T2 | Auctions with LLM Summaries | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2404.17525 | 2024-04-26 | T2 | Large Language Model Agent as a Mechanical Designer | off-topic (unrelated domain, keyword collision) |
| 2405.05905 | 2024-05-09 | T2 | Truthful Aggregation of LLMs with an Application to Online Advertising | **KEPT** t5 — `d-paper-mosaic-truthful-llm-ad-auction` |
| 2405.16276 | 2024-05-25 | T2 | Mechanism Design for LLM Fine-tuning with Multiple Reward Models | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2406.09459 | 2024-06-12 | T2 | Ad Auctions for LLMs via Retrieval Augmented Generation | **KEPT** t4 — `d-paper-segment-auction-rag-ads` |
| 2409.15343 | 2024-09-10 | T2 | Advertiser Content Understanding via LLMs for Google Ads Safety | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2410.14753 | 2024-10-18 | T2 | Collaboratively adding new knowledge to an LLM | dropped — screened, lower relevance or duplicate capability class |
| 2412.00495 | 2024-11-30 | T2 | Rethinking Strategic Mechanism Design In The Age Of Large Language Mod | off-topic (telecom/UAV/IoT, keyword collision) |
| 2412.03577 | 2024-11-18 | T2,T3 | OKG: On-the-Fly Keyword Generation in Sponsored Search Advertising | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2412.11142 | 2024-12-15 | T2 | AD-LLM: Benchmarking Large Language Models for Anomaly Detection | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2501.07992 | 2025-01-14 | T2 | LLM-Ehnanced Holonic Architecture for Ad-Hoc Scalable SoS | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2502.12203 | 2025-02-16 | T2 | An Interpretable Automated Mechanism Design Framework with Large Langu | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2503.09533 | 2025-03-12 | T2 | Large Language Models for Multi-Facility Location Mechanism Design | off-topic (unrelated domain, keyword collision) |
| 2503.22726 | 2025-03-26 | T2 | InfoBid: A Simulation Framework for Studying Information Disclosure in | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2505.01559 | 2025-05-02 | T2 | On the effectiveness of Large Language Models in the mechanical design | off-topic (unrelated domain, keyword collision) |
| 2505.04209 | 2025-05-07 | T2 | To Judge or not to Judge: Using LLM Judgements for Advertiser Keyphras | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2506.03309 | 2025-06-03 | T2 | Position Auctions in AI-Generated Content | dropped — LLM-ad mechanism near-duplicate of kept auction papers |
| 2507.00509 | 2025-07-01 | T2 | TeamCMU at Touché: Adversarial Co-Evolution for Advertisement Integrat | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2507.03904 | 2025-07-05 | T2 | Agent Exchange: Shaping the Future of AI Agent Economics | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2508.16251 | 2025-08-22 | T2 | A QoE-Driven Personalized Incentive Mechanism Design for AIGC Services | off-topic (telecom/UAV/IoT, keyword collision) |
| 2509.14221 | 2025-09-17 | T2 | GEM-Bench: A Benchmark for Ad-Injected Response Generation within Gene | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2509.14256 | 2025-09-12 | T2 | JU-NLP at Touché: Covert Advertisement in Conversational AI-Generation | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2510.08111 | 2025-10-09 | T2 | Evaluating LLM-Generated Legal Explanations for Regulatory Compliance  | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2512.03373 | 2025-12-03 | T2 | LLM-Generated Ads: From Personalization Parity to Persuasion Superiori | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2512.03975 | 2025-12-03 | T2 | Sponsored Questions and How to Auction Them | **KEPT** t5 — `d-paper-sponsored-questions-auction` |
| 2512.10551 | 2025-12-11 | T2 | LLM-Auction: Generative Auction towards LLM-Native Advertising | dropped — LLM-ad mechanism near-duplicate of kept auction papers |
| 2601.19435 | 2026-01-27 | T2 | Ad Insertion in LLM-Generated Responses | **KEPT** t4 — `d-paper-genre-ad-insertion-vcg` |
| 2602.01563 | 2026-02-02 | T2 | AdNanny: One Reasoning LLM for All Offline Ads Recommendation Tasks | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2603.05134 | 2026-03-05 | T2 | LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2604.08525 | 2026-04-09 | T2 | Ads in AI Chatbots? An Analysis of How Large Language Models Navigate  | **KEPT** t3 — `d-paper-ads-conflicts-of-interest` |
| 2605.00087 | 2026-04-30 | T2 | DeGenTWeb: A First Look at LLM-dominant Websites | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2605.08326 | 2026-05-08 | T2 | LLM Advertisement based on Neuron Auctions | **KEPT** t5 — `d-paper-neuron-auctions` |
| 2605.08426 | 2026-05-08 | T2 | Mechanism Design Is Not Enough: Prosocial Agents for Cooperative AI | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2605.09918 | 2026-05-11 | T2 | NaiAD: Initiate Data-Driven Research for LLM Advertising | dropped — LLM-ad mechanism near-duplicate of kept auction papers |
| 2605.10059 | 2026-05-11 | T2 | Strategic Exploitation in LLM Agent Markets: A Simulation Framework fo | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2605.10964 | 2026-05-07 | T2 | Mechanism Design for Quality-Preserving LLM Advertising | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2605.16474 | 2026-05-15 | T2 | LERA: LLM-Enhanced RAG for Ad Auction in Generative Chatbots | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2605.21969 | 2026-05-21 | T2 | LLM Retrieval for Stable and Predictable Ad Recommendations | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2605.27856 | 2026-05-27 | T2 | Fine-Tuned LLM as a Complementary Predictor Improving Ads System | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2606.29113 | 2026-06-27 | T2 | LLM Semantic Signaling Game and Mechanism Design: Systematic Blindness | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2607.23121 | 2026-07-25 | T2 | SMART: LLM-Augmented Hybrid Retrieval for Dynamic Product Ads | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2607.24232 | 2026-07-27 | T2 | Strategy-Aware Parameter-Efficient Adaptation for LLM-based Auto-Biddi | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2607.25590 | 2026-07-28 | T2 | PILA: Plug-and-Play Insertion for LLM-native Advertising | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2608.00123 | 2026-07-31 | T2 | LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising i | **KEPT** t4 — `d-paper-llm-osda-dynamic-auction` |
| 2608.24662 | 2026-08-25 | T2 | The Invisible Editorial Layer: Formalizing Undisclosed Inference-Time  | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2608.28199 | 2026-08-28 | T2 | Fine-Tuning Autobidders with Group Relative Policy Optimization | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2609.00638 | 2026-09-01 | T2 | It Takes Two to Match: Co-Evolving Generative Retriever with Reinforce | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2609.11915 | 2026-09-10 | T2 | Generative Marketing Mix Modeling: A Causal Inference Framework Linkin | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2008.13115 | 2020-08-30 | T3 | Corruption and Audit in Strategic Argumentation | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2212.10228 | 2022-12-20 | T3 | Automated Configuration and Usage of Strategy Portfolios for Bargainin | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2402.10196 | 2024-02-15 | T3 | A Trembling House of Cards? Mapping Adversarial Attacks against Langua | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2405.14751 | 2024-05-23 | T3 | AGILE: A Novel Reinforcement Learning Framework of LLM Agents | dropped — attack/defense near-duplicate of kept countermeasure/steering papers |
| 2409.15436 | 2024-09-23 | T3 | Ads that Talk Back: Implications and Perceptions of Injecting Personal | **KEPT** t3 — `d-paper-ads-that-talk-back` |
| 2410.23252 | 2024-10-30 | T3 | Evaluating Cultural and Social Awareness of LLM Web Agents | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2412.13972 | 2024-12-18 | T3 | Decentralized Convergence to Equilibrium Prices in Trading Networks | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2502.12130 | 2025-02-17 | T3 | Scaling Autonomous Agents via Automatic Reward Modeling And Planning | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2503.01908 | 2025-02-28 | T3 | UDora: A Unified Red Teaming Framework against LLM Agents by Dynamical | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2503.20749 | 2025-03-26 | T3 | Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real  | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2504.09723 | 2025-04-13 | T3 | AgentA/B: Automated and Scalable Web A/BTesting with Interactive LLM A | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2505.12501 | 2025-05-18 | T3 | ALAS: A Stateful Multi-LLM Agent Framework for Disruption-Aware Planni | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2506.00073 | 2025-05-29 | T3 | The Automated but Risky Game: Modeling and Benchmarking Agent-to-Agent | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2506.15947 | 2025-06-19 | T3 | HybridRAG-based LLM Agents for Low-Carbon Optimization in Low-Altitude | off-topic (telecom/UAV/IoT, keyword collision) |
| 2506.17318 | 2025-06-18 | T3 | Context manipulation attacks : Web agents are susceptible to corrupted | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2507.14633 | 2025-07-19 | T3 | Agentic Satellite-Augmented Low-Altitude Economy and Terrestrial Netwo | off-topic (telecom/UAV/IoT, keyword collision) |
| 2508.02630 | 2025-08-04 | T3 | What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, &  | **KEPT** t4 — `d-paper-aces-ai-agent-buying` |
| 2508.16379 | 2025-08-22 | T3 | Agentic AI Empowered Multi-UAV Trajectory Optimization in Low-Altitude | off-topic (telecom/UAV/IoT, keyword collision) |
| 2509.21501 | 2025-09-25 | T3 | LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evalu | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2509.25609 | 2025-09-30 | T3 | A Framework for Studying AI Agent Behavior: Evidence from Consumer Cho | **KEPT** t3 — `d-paper-abxlab-agent-consumer-choice` |
| 2510.03285 | 2025-09-28 | T3 | WAREX: Web Agent Reliability Evaluation on Existing Benchmarks | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2510.04368 | 2025-10-05 | T3 | NegotiationGym: Self-Optimizing Agents in a Multi-Agent Social Simulat | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2510.06222 | 2025-08-30 | T3 | Inducing State Anxiety in LLM Agents Reproduces Human-Like Biases in C | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2510.07043 | 2025-10-08 | T3 | COMPASS: Benchmarking Constrained Optimization in LLM Agents | off-topic (non-commerce agent task) |
| 2510.18113 | 2025-10-20 | T3 | Investigating the Impact of Dark Patterns on LLM-Based Web Agents | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2510.19687 | 2025-10-22 | T3 | Are Large Language Models Sensitive to the Motives Behind Communicatio | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2510.25779 | 2025-10-27 | T3 | Magentic Marketplace: An Open-Source Environment for Studying Agentic  | **KEPT** t4 — `d-paper-magentic-marketplace` |
| 2511.03370 | 2025-11-05 | T3 | EQ-Negotiator: Dynamic Emotional Personas Empower Small Language Model | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2512.08737 | 2025-12-09 | T3 | Insured Agents: A Decentralized Trust Insurance Mechanism for Agentic  | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2512.16167 | 2025-12-18 | T3 | Ev-Trust: An Evolutionarily Stable Trust Mechanism for Decentralized L | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2512.21578 | 2025-12-25 | T3 | NEMO-4-PAYPAL: Leveraging NVIDIA's Nemo Framework for empowering PayPa | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2512.22894 | 2025-12-28 | T3 | DECEPTICON: How Dark Patterns Manipulate Web Agents | **KEPT** t4 — `d-paper-decepticon-dark-patterns` |
| 2601.03061 | 2026-01-06 | T3 | Vertical tacit collusion in AI-mediated markets | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2601.05257 | 2025-10-20 | T3 | KP-Agent: Keyword Pruning in Sponsored Search Advertising via LLM-Powe | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2601.06112 | 2026-01-03 | T3 | ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Li | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2601.17817 | 2026-01-25 | T3 | Multi-Agent Collaborative Intrusion Detection for Low-Altitude Economy | off-topic (telecom/UAV/IoT, keyword collision) |
| 2601.18225 | 2026-01-26 | T3 | ShopSimulator: Evaluating and Exploring RL-Driven LLM Agent for Shoppi | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2602.00213 | 2026-01-30 | T3 | TessPay: Verify-then-Pay Infrastructure for Trusted Agentic Commerce | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2602.06008 | 2026-02-05 | T3 | AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Tran | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2602.17452 | 2026-02-19 | T3 | Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledg | dropped — payment-rail cryptography, not recommendation/ad steering |
| 2602.23716 | 2026-02-27 | T3 | ProductResearch: Training E-Commerce Deep Research Agents via Multi-Ag | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2603.01179 | 2026-03-01 | T3 | A402: Binding Cryptocurrency Payments to Service Execution for Agentic | dropped — payment-rail cryptography, not recommendation/ad steering |
| 2603.11392 | 2026-03-12 | T3 | Agentic AI for Embodied-enhanced Beam Prediction in Low-Altitude Econo | off-topic (telecom/UAV/IoT, keyword collision) |
| 2603.14864 | 2026-03-16 | T3 | Shopping Companion: Benchmarking and Training LLM Agents for Long-Hori | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2603.20972 | 2026-03-21 | T3 | A Solicit-Then-Suggest Model of Agentic Purchasing | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2603.29247 | 2026-03-31 | T3 | MemRerank: Preference Memory for Personalized Product Reranking | dropped — industrial recommender internals, not answer-steering by outside party |
| 2604.04263 | 2026-04-05 | T3 | Commercial Persuasion in AI-Mediated Conversations | **KEPT** t4 — `d-paper-commercial-persuasion-experiment` |
| 2604.07003 | 2026-04-08 | T3 | EmoMAS: Emotion-Aware Multi-Agent System for High-Stakes Edge-Deployab | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2604.15367 | 2026-04-15 | T3,T5 | SoK: Security of Autonomous LLM Agents in Agentic Commerce | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2604.16966 | 2026-04-18 | T3 | Visual Inception: Compromising Long-term Planning in Agentic Recommend | dropped — attack/defense near-duplicate of kept countermeasure/steering papers |
| 2604.23993 | 2026-04-27 | T3 | EPM-RL: Reinforcement Learning for On-Premise Product Mapping in E-Com | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2604.26960 | 2026-04-07 | T3 | LLM Biases | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2605.14290 | 2026-05-14 | T3 | Web Agents Should Adopt the Plan-Then-Execute Paradigm | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2605.18673 | 2026-05-18 | T3 | Generative AI Advertising as a Problem of Trustworthy Commercial Inter | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2606.08790 | 2026-06-07 | T3 | RAILS: Verification-Native Clearing For Agentic Commerce | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2606.13385 | 2026-06-11 | T3 | Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking  | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2606.16613 | 2026-06-15 | T3 | CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Mul | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2606.27499 | 2026-06-25 | T3 | DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory wi | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2606.31693 | 2026-06-30 | T3 | ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Sh | dropped — industrial recommender internals, not answer-steering by outside party |
| 2607.00245 | 2026-06-30 | T3 | Agent-to-Agent Finance: Blockchain Payments and Trust Infrastructure f | off-topic (non-commerce agent task) |
| 2607.00255 | 2026-06-30 | T3 | SLM, LLM or Agentic AI? Toward Intelligent UAV-Enabled WPT Systems in  | off-topic (telecom/UAV/IoT, keyword collision) |
| 2607.06001 | 2026-07-07 | T3 | Information Limits and Attractor Dynamics in Economies of Frontier LLM | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2607.14396 | 2026-07-15 | T3 | CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Cont | dropped — attack/defense near-duplicate of kept countermeasure/steering papers |
| 2607.18347 | 2026-07-20 | T3 | A Decision-Centered Reference Architecture for Trustworthy Agentic Com | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2607.19436 | 2026-07-21 | T3 | Building Trust in Autonomous Commerce: A Verifiable Global Event Timel | dropped — payment-rail cryptography, not recommendation/ad steering |
| 2607.21824 | 2026-07-23 | T3 | Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform | **KEPT** t5 — `d-paper-protocol-attacks-agentic-commerce` |
| 2608.00102 | 2026-07-30 | T3 | Can LLM Agents Price Competitively? A Dynamic Multi-Attribute Auction  | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2608.02441 | 2026-08-03 | T3 | Agentic Commerce World: An Auditable and Verifiable Environment for Vi | off-topic (non-commerce agent task) |
| 2608.03606 | 2026-08-04 | T3 | Learning Clinical-Trial Strategy: Offline Policy Training for Decision | off-topic (non-commerce agent task) |
| 2608.05332 | 2026-08-05 | T3 | Hierarchical Server Architecture for Agentic Science | dropped — agent negotiation/pricing capability, not recommendation steering |
| 2608.06020 | 2026-08-06 | T3 | From Economic Agents to Agentic Economies: A Systems Blueprint for Eco | dropped — survey/position (cited context, not a primary capability result) |
| 2608.06033 | 2026-08-06 | T3 | ASGE-RR: Agentic Service Graph Embedding with Revisable Reservations f | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2608.08395 | 2026-08-09 | T3 | From Product Search to Preference Articulation: The Economics of Agent | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2608.09282 | 2026-08-10 | T3 | ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Baske | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2609.02564 | 2026-09-02 | T3 | A Finger on the Scale: Covert Policy Steering through Agentic Skills | **KEPT** t5 — `d-paper-skillshift-agent-skills` |
| 2609.11108 | 2026-09-10 | T3 | But How Would AI Agents Run a Town's Economy? | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2609.14744 | 2026-09-13 | T3,T5 | Runtime Authorization for Resources Acquired by AI Agents | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2609.25677 | 2026-09-22 | T3 | Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pret | dropped — attack/defense near-duplicate of kept countermeasure/steering papers |
| 2305.06311 | 2023-05-10 | T4 | Automatic Evaluation of Attribution by Large Language Models | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2311.03731 | 2023-11-07 | T4 | A Survey of Large Language Models Attribution | dropped — survey/position (cited context, not a primary capability result) |
| 2402.15089 | 2024-02-23 | T4 | AttributionBench: How Hard is Automatic Attribution Evaluation? | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2504.15629 | 2025-04-22 | T4 | CiteFix: Enhancing RAG Accuracy Through Post-Processing Citation Corre | dropped — conventional ad-tech (bidding/moderation), not in-answer LLM ad |
| 2509.04499 | 2025-09-02 | T4 | DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability  | off-topic (telecom/UAV/IoT, keyword collision) |
| 2512.05958 | 2025-12-05 | T4 | MaxShapley: Towards Incentive-compatible Generative Search with Fair C | **KEPT** t3 — `d-paper-maxshapley-fair-attribution` |
| 2604.02544 | 2026-04-02 | T4 | Developer Experience with AI Coding Agents: HTTP Behavioral Signatures | off-topic (non-commerce agent task) |
| 2606.10907 | 2026-06-09 | T4 | From Prompt to Purchase: How AI Brand Recommendations Move Consumers o | **KEPT** t5 — `d-paper-prompt-to-purchase-clickstream` |
| 2606.21595 | 2026-06-19 | T4 | Per-Entity Bias Mapping for AI Visibility: Why Brand Mentions Require  | dropped — GEO capability near-duplicate of kept steering papers (2604.19516, 2605.12887) |
| 2607.07652 | 2026-07-08 | T4 | Answering Without Referring: How AI Search Rewrites the Web's Economic | dropped — screened, lower relevance or duplicate capability class |
| 2607.15771 | 2026-07-17 | T4 | What Do Chinese-Language Generative Search Engines Cite and Surface? A | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2607.20328 | 2026-07-22 | T4 | Understanding Generative AI-mediated User Engagement with Academic Lib | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2608.23252 | 2026-08-24 | T4 | The Laws of Context Allocation: Causal Measurement and Closed-Loop Orc | dropped — attack/defense near-duplicate of kept countermeasure/steering papers |
| 2501.05647 | 2025-01-10 | T5 | Collaboration of Large Language Models and Small Recommendation Models | dropped — industrial recommender internals, not answer-steering by outside party |
| 2501.12573 | 2025-01-22 | T5 | Leveraging LLMs to Create a Haptic Devices' Recommendation System | off-topic (unrelated domain, keyword collision) |
| 2510.06135 | 2025-10-07 | T5 | Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verifi | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2511.14227 | 2025-11-18 | T5 | DevPiolt: Operation Recommendation for IoT Devices at Xiaomi Home | off-topic (telecom/UAV/IoT, keyword collision) |
| 2512.19432 | 2025-12-22 | T5 | MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Inter | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2601.09306 | 2026-01-14 | T5 | On-Device Large Language Models for Sequential Recommendation | dropped — industrial recommender internals, not answer-steering by outside party |
| 2601.18267 | 2026-01-26 | T5 | Orchestrating Specialized Agents for Trustworthy Enterprise RAG | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2601.22543 | 2026-01-30 | T5 | SCaLRec: Semantic Calibration for LLM-enabled Cloud-Device Sequential  | dropped — industrial recommender internals, not answer-steering by outside party |
| 2601.22569 | 2026-01-30 | T5 | Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via P | **KEPT** t5 — `d-paper-ap2-red-team-prompt-inj` |
| 2602.06345 | 2026-02-06 | T5 | Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigat | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2602.10021 | 2026-02-10 | T5 | Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Fr | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2602.22732 | 2026-02-26 | T5 | Generative Recommendation for Large-Scale Advertising | dropped — industrial recommender internals, not answer-steering by outside party |
| 2602.24068 | 2026-02-27 | T5 | A Novel Hierarchical Multi-Agent System for Payments Using LLMs | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2603.21573 | 2026-03-23 | T5 | Rethinking Visual Privacy: A Compositional Privacy Risk Framework for  | off-topic (unrelated domain, keyword collision) |
| 2603.23646 | 2026-03-24 | T5 | Swiss-Bench SBP-002: A Frontier Model Comparison on Swiss Legal and Re | off-topic (unrelated domain, keyword collision) |
| 2604.02135 | 2026-04-02 | T5 | GaelEval: Benchmarking LLM Performance for Scottish Gaelic | off-topic (unrelated domain, keyword collision) |
| 2604.02684 | 2026-04-03 | T5 | MBGR: Multi-Business Prediction for Generative Recommendation at Meitu | dropped — industrial recommender internals, not answer-steering by outside party |
| 2604.25884 | 2026-04-28 | T5 | QCalEval: Benchmarking Vision-Language Models for Quantum Calibration  | off-topic (unrelated domain, keyword collision) |
| 2605.00071 | 2026-04-30 | T5 | Compliance-Aware Agentic Payments on Stablecoin Rails | dropped — payment-rail cryptography, not recommendation/ad steering |
| 2605.00334 | 2026-05-01 | T5 | AgentFloor: How Far Up the tool use Ladder Can Small Open-Weight Model | **KEPT** t4 — `d-paper-agentfloor-open-weight-ladder` |
| 2605.04726 | 2026-05-06 | T5 | RecGPT-Mobile: On-Device Large Language Models for User Intent Underst | dropped — industrial recommender internals, not answer-steering by outside party |
| 2606.15367 | 2026-06-13 | T5 | S1-DeepResearch: Beyond Search, Toward Real-World Long-Horizon Researc | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2607.08317 | 2026-07-09 | T5 | Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2607.25339 | 2026-07-28 | T5 | SPARC: Sequence-aware Progressive Attribute Routing and Compression Fr | dropped — industrial recommender internals, not answer-steering by outside party |
| 2607.25398 | 2026-07-28 | T5 | HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Followin | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2607.27647 | 2026-07-30 | T5 | LoopMemGR: From Behavior Logs to Evolving Memory for Generative Recomm | dropped — industrial recommender internals, not answer-steering by outside party |
| 2608.07989 | 2026-08-08 | T5 | PushDualGen: Enabling LLMs to Generate Semantic IDs with Interpretable | dropped — industrial recommender internals, not answer-steering by outside party |
| 2608.23265 | 2026-08-24 | T5 | EvoWiki: Incremental State Overwriting and Traceable Question Answerin | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2609.00060 | 2026-08-30 | T5 | A Formal Analysis of Agent Payment Protocols | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2609.00986 | 2026-09-01 | T5 | TGR: Advancing Industrial Recommendation from Generative-Paradigm Rank | dropped — industrial recommender internals, not answer-steering by outside party |
| 2403.14720 | 2024-03-20 | T6 | Defending Against Indirect Prompt Injection Attacks With Spotlighting | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2409.17275 | 2024-09-12 | T6 | On the Vulnerability of Applying Retrieval-Augmented Generation within | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2410.05451 | 2024-10-07 | T6 | SecAlign: Defending Against Prompt Injection with Preference Optimizat | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2503.18813 | 2025-03-24 | T6 | Defeating Prompt Injections by Design | **KEPT** t4 — `d-paper-camel-design-defense` |
| 2504.21668 | 2025-04-30 | T6 | Traceback of Poisoning Attacks to Retrieval-Augmented Generation | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2505.14534 | 2025-05-20 | T6 | Lessons from Defending Gemini Against Indirect Prompt Injections | **KEPT** t5 — `d-paper-defending-gemini-ipi` |
| 2507.02735 | 2025-07-03 | T6 | Meta SecAlign: A Secure Foundation LLM Against Prompt Injection Attack | **KEPT** t4 — `d-paper-meta-secalign-open-defense` |
| 2510.09023 | 2025-10-10 | T6 | The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses A | **KEPT** t4 — `d-paper-attacker-moves-second` |
| 2510.25025 | 2025-10-28 | T6 | Secure Retrieval-Augmented Generation against Poisoning Attacks | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2603.16152 | 2026-03-17 | T6 | HIPO: Instruction Hierarchy via Constrained Reinforcement Learning | dropped — descriptive brand/citation bias measurement (near-duplicate of kept measurement papers) |
| 2604.09443 | 2026-04-10 | T6 | Many-Tier Instruction Hierarchy in LLM Agents | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2605.26754 | 2026-05-26 | T6 | Cordon-MAS: Defending RAG against Knowledge Poisoning via Information- | dropped — agentic-commerce trust/settlement infra, not steering or monetisation |
| 2607.23545 | 2026-07-26 | T6 | Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs | dropped — capability/benchmark without an outside-party steering or monetisation result |
| 2607.26228 | 2026-07-28 | T6 | Steering Instruction Hierarchies at Inference Time | dropped — capability/benchmark without an outside-party steering or monetisation result |
## Caveats

- Drop reasons name the nearest screen bucket; a "near-duplicate" drop means a kept paper covers the same capability class at equal-or-higher tier, not that the dropped paper is without merit.
- "off-topic (keyword collision)" rows are arXiv hits on a query term used in an unrelated field (telecom low-altitude economy, mechanical design, quantum), returned by broad `abs:` queries and screened out on abstract read.
- Dates are arXiv v1 submission dates; a paper's `updated` field can be later (recorded in each kept paper's file).
- Screened count is arXiv-API-reachable papers this pass; ACM DL, IEEE Xplore and OpenReview were reached only where a paper also had an arXiv mirror. Venue-only papers without an arXiv id are not counted and are an unknown, channel: ACM DL / IEEE Xplore / OpenReview direct, not exhausted this pass.
