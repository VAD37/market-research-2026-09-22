# Orphan audit — 2026-09-24

Set 2026-09-24 on user request ("run subagents to pull-compile the gaps"). Orphan = raw file with no citation in `markets/`, `competitors/`, `customers/`, `findings/`, no citation from another cited raw file, and none in `method/` or `sources/`. Count 147 of 1,038 raw files at HEAD f720a40 (A 6, B 51, C 2, D 48, E 26, F 14). Measured by main-thread script, filename match only — a file cited by paraphrase without its name counts as orphan.

Litigation note: `b-court-*` (11 files) are reached only through `b-court-dockets-table-2026-09-22.md`; compiled docs carry 0 hits for Britannica or Daily News. GAP-LIT owns them though they are not on the orphan list.

Agents append one section each by shell append (`cat >>`), never edit this file. Verdicts: `compiled` (target file + section), `covered` (compiled path already carrying the facts), `not briefable` (reason), `superseded` (newer raw path).

## Orphan list by owner

### Lane A — 6 files, owner GAP-ACEF

- `a-practitioner-github-open-prompt-visibility-tool-2026-09-22.md`
- `a-practitioner-hackernews-chatgpt-recommend-discussion-2026-09-22.md`
- `a-practitioner-hackernews-sitefire-launch-discussion-2026-09-22.md`
- `a-practitioner-linkedin-shivam-srivastava-chatgpt-ads-gap-2026-09-22.md`
- `a-refibuy-ai1000-rankings-2026-09-22.md`
- `a-similarweb-openai-dsa-country-cut-walls-2026-09-23.md`

### Lane B — 51 files, owner GAP-B

- `b-adthena-data-pulse-repull2-2026-09-23.md`
- `b-amazon-10q-q2-2026-advertising-services-2026-09-23.md`
- `b-anthropic-help-report-block-remove-content-2026-09-23.md`
- `b-asa-cap-ai-monitoring-2026-09-23.md`
- `b-campaign-openai-ads-100m-2026-09-23.md`
- `b-cnbc-openai-ads-1bn-2026-09-23.md`
- `b-criteo-openai-pilot-march-2026-09-23.md`
- `b-criteo-openai-update-june-2026-09-23.md`
- `b-digiday-openai-ads-fomo-cpm-2026-09-23.md`
- `b-digiday-openai-carousels-2026-09-23.md`
- `b-duckduckgo-duckai-help-2026-09-23.md`
- `b-emarketer-openai-ads-100m-2026-09-23.md`
- `b-eu-cnam-dsa-2026-09-22.md`
- `b-eu-commission-ai-act-art50-guidance-2026-09-23.md`
- `b-euperspectives-chatgpt-ads-eu-2026-09-23.md`
- `b-google-gml2026-collection-2026-09-22.md`
- `b-google-report-content-ai-overviews-gemini-feedback-2026-09-23.md`
- `b-mediaincanada-gemini-ads-denial-2026-09-23.md`
- `b-mediaincanada-openai-pilot-agencies-2026-09-23.md`
- `b-meta-10q-q2-2026-advertising-revenue-2026-09-23.md`
- `b-meta-q2-2026-release-2026-09-23.md`
- `b-mi3-zeroclick-55m-2026-09-23.md`
- `b-microsoft-8k-q4-fy2026-search-advertising-2026-09-23.md`
- `b-microsoft-copilot-report-concern-check-2026-09-23.md`
- `b-novadata-rufus-ads-free-2026-09-23.md`
- `b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23-img-2026-09-23.md`
- `b-openai-help-account-setup-2026-09-23.md`
- `b-openai-help-ads-faq-2026-09-23.md`
- `b-openai-help-billing-payment-2026-09-23.md`
- `b-openai-help-budget-pacing-2026-09-23.md`
- `b-openai-help-daily-budgets-2026-09-23.md`
- `b-openai-help-launch-campaigns-2026-09-23.md`
- `b-openai-help-maximize-results-2026-09-23.md`
- `b-openai-help-product-feed-campaigns-2026-09-23.md`
- `b-openai-help-quickstart-2026-09-23.md`
- `b-openai-help-sponsored-agents-2026-09-23.md`
- `b-perplexity-help-report-inaccurate-answers-2026-09-23.md`
- `b-ppcland-criteo-1000-brands-2026-09-23.md`
- `b-ppcland-gemini-ads-denial-2026-09-23.md`
- `b-sel-copilot-showroom-ads-2026-09-23.md`
- `b-sensortower-chatgpt-ads-rising-density-repull2-2026-09-23.md`
- `b-seranking-chatgpt-ads-tracker-2026-09-23.md`
- `b-seroundtable-chatgpt-ads-updates-2026-09-23.md`
- `b-seroundtable-google-direct-offers-2026-09-23.md`
- `b-snap-my-ai-sponsored-links-2026-09-23.md`
- `b-techcrunch-koah-seed-2026-09-23.md`
- `b-techcrunch-meta-ai-chat-ad-targeting-2026-09-23.md`
- `b-trendingtopics-chatgpt-ads-eu-privacy-2026-09-23.md`
- `b-walmart-10k-fy2026-advertising-2026-09-23.md`
- `b-walmart-8k-q2-fy2027-advertising-2026-09-23.md`
- `b-wppmedia-netherlands-chatgpt-ads-2026-09-23.md`

### Lane C — 2 files, owner GAP-ACEF

- `c-adobe-analytics-q2-2026-traffic-report-repull2-2026-09-23.md`
- `c-cloudflare-pay-per-crawl-docs-2026-09-23-img-2026-09-23.md`

### Lane D — 48 files, owner GAP-D

- `d-injection-brave-comet-disclosure-2026-09-22.md`
- `d-injection-chen-ipi-proxy-2026-09-22.md`
- `d-injection-choi-agent-data-injection-2026-09-22.md`
- `d-injection-google-mitigating-pi-2026-09-22.md`
- `d-injection-greshake-foundational-ipi-2026-09-22.md`
- `d-injection-microsoft-copilot-bounty-2026-09-22.md`
- `d-injection-narisetty-oob-defenses-2026-09-22.md`
- `d-injection-nestaas-adversarial-seo-2026-09-22.md`
- `d-injection-pfrommer-ranking-manipulation-2026-09-22.md`
- `d-injection-poisonedrag-2026-09-22.md`
- `d-injection-yin-llm-rankers-2026-09-22.md`
- `d-paper-abxlab-agent-consumer-choice-2026-09-23.md`
- `d-paper-aces-ai-agent-buying-2026-09-23.md`
- `d-paper-ads-conflicts-of-interest-2026-09-23.md`
- `d-paper-ads-that-talk-back-2026-09-23.md`
- `d-paper-aeo-natural-experiment-referral-2026-09-23.md`
- `d-paper-agentfloor-open-weight-ladder-2026-09-23.md`
- `d-paper-ap2-red-team-prompt-inj-2026-09-23.md`
- `d-paper-attacker-moves-second-2026-09-23.md`
- `d-paper-brand-retrieval-ranking-eval-2026-09-23.md`
- `d-paper-camel-design-defense-2026-09-23.md`
- `d-paper-commercial-persuasion-experiment-2026-09-23.md`
- `d-paper-decepticon-dark-patterns-2026-09-23.md`
- `d-paper-defending-gemini-ipi-2026-09-23.md`
- `d-paper-detecting-native-ads-2026-09-23.md`
- `d-paper-genre-ad-insertion-vcg-2026-09-23.md`
- `d-paper-injection-paradox-brand-suppression-2026-09-23.md`
- `d-paper-lazy-grounding-search-agents-2026-09-23.md`
- `d-paper-llm-osda-dynamic-auction-2026-09-23.md`
- `d-paper-magentic-marketplace-2026-09-23.md`
- `d-paper-mageo-multi-agent-geo-2026-09-23.md`
- `d-paper-maxshapley-fair-attribution-2026-09-23.md`
- `d-paper-mgeo-multimodal-rank-2026-09-23.md`
- `d-paper-mosaic-truthful-llm-ad-auction-2026-09-23.md`
- `d-paper-mpma-mcp-preference-2026-09-23.md`
- `d-paper-neuron-auctions-2026-09-23.md`
- `d-paper-perplexity-trap-source-bias-2026-09-23.md`
- `d-paper-prompt-to-purchase-clickstream-2026-09-23.md`
- `d-paper-protocol-attacks-agentic-commerce-2026-09-23.md`
- `d-paper-segment-auction-rag-ads-2026-09-23.md`
- `d-paper-skillshift-agent-skills-2026-09-23.md`
- `d-paper-sponsored-questions-auction-2026-09-23.md`
- `d-paper-training-induced-source-bias-2026-09-23.md`
- `d-structured-arxiv-volpini-rag-2026-09-22.md`
- `d-structured-llmstxt-directory-count-2026-09-22.md`
- `d-structured-llmstxt-org-spec-2026-09-22.md`
- `d-structured-redocly-overhyped-2026-09-22.md`
- `d-structured-schemaorg-about-2026-09-22.md`

### Lane E — 26 files, owner GAP-ACEF

- `e-case-5w-ai-communications-report-repull2-2026-09-23.md`
- `e-case-athenahq-new-multi-2026-09-23.md`
- `e-case-boily-dental-geo-comparison-primary-2026-09-23-img-2026-09-23.md`
- `e-case-boily-dental-geo-comparison-primary-2026-09-23.md`
- `e-case-ddg-vendor-multi-2026-09-23.md`
- `e-case-fresha-google-agentic-2026-09-23.md`
- `e-case-jonathanmall-geo-experiment-primary-2026-09-23-img-2026-09-23.md`
- `e-case-jonathanmall-geo-experiment-primary-2026-09-23.md`
- `e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-primary-2026-09-23-img-2026-09-23.md`
- `e-case-practitioner-hackernews-bando-geo-experiment-2026-09-22.md`
- `e-case-practitioner-hackernews-firegeo-reddit-perplexity-leads-2026-09-22.md`
- `e-case-practitioner-hackernews-llmstxt-no-results-2026-09-22.md`
- `e-case-practitioner-linkedin-muneeb-ahmad-chatgpt-ads-b2b-dtc-2026-09-22.md`
- `e-case-profound-new-multi-2026-09-23.md`
- `e-case-searchengineland-two-geo-experiments-primary-2026-09-23.md`
- `e-case-titles-opened-multi-2026-09-23.md`
- `e-dentsu-global-ad-spend-forecast-2026-2026-09-23.md`
- `e-gartner-ad-platforms-prediction-2028-2026-09-23.md`
- `e-magna-dec-2025-pointer-mediaconfidential-2026-09-23.md`
- `e-magna-search-report-page-2026-09-23.md`
- `e-market-size-coherent-organic-2026-09-23.md`
- `e-market-size-juniper-agentic-2026-09-23.md`
- `e-market-size-marketintelo-organic-agentic-2026-09-23.md`
- `e-market-size-marketsandmarkets-organic-2026-09-23.md`
- `e-market-size-nextmsc-agentic-2026-09-23.md`
- `e-wayback-profound-customers-2026-09-23.md`

### Lane F — 14 files, owner GAP-ACEF (f-courtlistener: GAP-LIT)

- `f-birdeye-multilocation-ai-search-S2-S6-2026-09-23-img-2026-09-23.md`
- `f-courtlistener-ltl-led-v-google-ai-overview-defamation-2026-09-23.md`
- `f-hubspot-state-of-marketing-2026-check-2026-09-23.md`
- `f-jobboards-S1-eu-national-2026-09-23.md`
- `f-jobboards-S1-eu-paid-agentic-2026-09-23.md`
- `f-linkedin-S1-eu-paid-agentic-2026-09-23.md`
- `f-reddit-arcticshift-S13-brand-accuracy-2026-09-23.md`
- `f-reddit-arcticshift-S5-eu-paid-agentic-2026-09-23.md`
- `f-signal-hr-llmstxt-repull2-2026-09-23.md`
- `f-signal-sk-llmstxt-repull2-2026-09-23.md`
- `f-ted-ukcf-S10-eu-paid-agentic-2026-09-23.md`
- `f-vendor-S2-eu-paid-agentic-2026-09-23.md`
- `f-vendor-S2-yext-scout-localized-fr-it-2026-09-23.md`
- `f-vendor-tradepress-S13-brand-accuracy-2026-09-23.md`

## Agent verdicts

Row format per agent section: `| raw file | verdict | target or reason |`.

### GAP-D — 2026-09-24

| raw file | verdict | target or reason |
|---|---|---|
| `d-injection-brave-comet-disclosure-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-chen-ipi-proxy-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-choi-agent-data-injection-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-google-mitigating-pi-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-greshake-foundational-ipi-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-microsoft-copilot-bounty-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-narisetty-oob-defenses-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-nestaas-adversarial-seo-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-pfrommer-ranking-manipulation-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-poisonedrag-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-injection-yin-llm-rankers-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-abxlab-agent-consumer-choice-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-aces-ai-agent-buying-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-ads-conflicts-of-interest-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-ads-that-talk-back-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-aeo-natural-experiment-referral-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-agentfloor-open-weight-ladder-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-ap2-red-team-prompt-inj-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-attacker-moves-second-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-brand-retrieval-ranking-eval-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-camel-design-defense-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-commercial-persuasion-experiment-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-decepticon-dark-patterns-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-defending-gemini-ipi-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-detecting-native-ads-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-genre-ad-insertion-vcg-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-injection-paradox-brand-suppression-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-lazy-grounding-search-agents-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-llm-osda-dynamic-auction-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-magentic-marketplace-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-mageo-multi-agent-geo-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-maxshapley-fair-attribution-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-mgeo-multimodal-rank-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-mosaic-truthful-llm-ad-auction-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-mpma-mcp-preference-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-neuron-auctions-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-perplexity-trap-source-bias-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-prompt-to-purchase-clickstream-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-protocol-attacks-agentic-commerce-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-segment-auction-rag-ads-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-skillshift-agent-skills-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-sponsored-questions-auction-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-paper-training-induced-source-bias-2026-09-23.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-structured-arxiv-volpini-rag-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-structured-llmstxt-directory-count-2026-09-22.md` | superseded | `raw/e-wayback-llms-txt-directories-2026-09-23.md` (3,830, 2026-09-23), carried in `findings/market-potential.md` |
| `d-structured-llmstxt-org-spec-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-structured-redocly-overhyped-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |
| `d-structured-schemaorg-about-2026-09-22.md` | compiled | `findings/frontier-scan.md` §Manipulation evidence ledger (L89–157) |

GAP-D tally: 47 compiled, 1 superseded, 0 covered, 0 not briefable. No broken pulls.

### GAP-LIT — 2026-09-24

| raw file | verdict | target or reason |
|---|---|---|
| `b-court-britannica-v-perplexity-2026-09-22.md` | compiled | `markets/organic-recommendation.md` "Publisher litigation — added 2026-09-24"; `findings/whitespace.md` "Litigation risk register — added 2026-09-24" |
| `b-court-daily-news-v-microsoft-openai-2026-09-22.md` | compiled | `markets/organic-recommendation.md` "Publisher litigation — added 2026-09-24" |
| `b-court-nyt-v-microsoft-openai-2026-09-22.md` | compiled | both GAP-LIT sections above |
| `b-court-usnews-v-openai-2026-09-22.md` | compiled | `markets/organic-recommendation.md` "Publisher litigation — added 2026-09-24" |
| `b-court-mdl-openai-copyright-2026-09-22.md` | compiled | `markets/organic-recommendation.md` "Publisher litigation — added 2026-09-24" |
| `b-court-reddit-v-anthropic-2026-09-22.md` | compiled | `markets/organic-recommendation.md` "Publisher litigation — added 2026-09-24" |
| `b-court-dow-jones-v-perplexity-2026-09-22.md` | compiled | both GAP-LIT sections; figures already in `markets/paid-placement.md` L100 |
| `b-court-penske-v-google-2026-09-22.md` | compiled | both GAP-LIT sections; figures already in `markets/paid-placement.md` L99 |
| `b-court-chegg-v-google-2026-09-22.md` | covered | `markets/paid-placement.md` L98; status row added in GAP-LIT organic section |
| `b-court-dockets-table-2026-09-22.md` | covered | index file; cited by `findings/proof-scorecard.md` L259–261, `findings/trigger-timeline.md` L65 |
| `b-court-dockets-table-repull2-2026-09-23.md` | compiled | `markets/organic-recommendation.md` "Publisher litigation — added 2026-09-24" (Chegg row) |
| `f-courtlistener-ltl-led-v-google-ai-overview-defamation-2026-09-23.md` | compiled | both GAP-LIT sections; also `customers/high-cpa-regulated.md` L203 |
| `a-court-mdl-microsoft-ctr-data-2026-09-22.md` | covered | `markets/paid-placement.md` L97; `findings/whitespace.md` risk row 1; `findings/proof-scorecard.md` L252 |

New raw, 2026-09-24 (6): `b-court-{britannica-v-perplexity,dow-jones-v-perplexity,usnews-v-openai,daily-news-v-microsoft-openai,ltl-led-v-google,chegg-penske-v-google}-repull3-2026-09-24.md` — all compiled in the GAP-LIT organic section.

### GAP-B — 2026-09-24

| raw file | verdict | target or reason |
|---|---|---|
| `b-adthena-data-pulse-repull2-2026-09-23.md` | not briefable | negative locate check, no figure; noted in paid-placement GAP-B caveats |
| `b-amazon-10q-q2-2026-advertising-services-2026-09-23.md` | covered | `markets/paid-placement.md` §Baselines beyond Google, P16-c1; `findings/market-potential.md` (stem cite) |
| `b-anthropic-help-report-block-remove-content-2026-09-23.md` | covered | `method/demand-signals.md` L124 (stem cite); lane A accuracy channel, not paid |
| `b-asa-cap-ai-monitoring-2026-09-23.md` | compiled | `markets/paid-placement.md` §EU and UK rules, GAP-B (L341–349) |
| `b-campaign-openai-ads-100m-2026-09-23.md` | compiled | `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 (<7% low relevance); $100M, 600 advertisers already via Reuters raw |
| `b-cnbc-openai-ads-1bn-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339) (self-serve India, Europe, MENA); $1B via OpenAI raw |
| `b-criteo-openai-pilot-march-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 |
| `b-criteo-openai-update-june-2026-09-23.md` | compiled | `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 (CTR 2–3×, >80% new); 2,000 brands already Pass 12 (stem cite) |
| `b-digiday-openai-ads-fomo-cpm-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 Prices published (stem cite) |
| `b-digiday-openai-carousels-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); ai-ads-evidence E22 |
| `b-duckduckgo-duckai-help-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 per-engine; ai-ads-evidence E16 (stem cite) |
| `b-emarketer-openai-ads-100m-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 |
| `b-eu-cnam-dsa-2026-09-22.md` | compiled | `markets/paid-placement.md` §EU and UK rules, GAP-B (L341–349) |
| `b-eu-commission-ai-act-art50-guidance-2026-09-23.md` | covered | `findings/whitespace.md` S3 (stem cite) |
| `b-euperspectives-chatgpt-ads-eu-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339) (UK unknown answered, tier 5) |
| `b-google-gml2026-collection-2026-09-22.md` | covered | hub page; relevant articles compiled via b-google-gml2026-search-ads raws |
| `b-google-report-content-ai-overviews-gemini-feedback-2026-09-23.md` | covered | `method/demand-signals.md` L124 (stem cite); lane A |
| `b-mediaincanada-gemini-ads-denial-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339) (with PPC Land copy) |
| `b-mediaincanada-openai-pilot-agencies-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 agencies row via wppmedia, mediapost, dentsu raws |
| `b-meta-10q-q2-2026-advertising-revenue-2026-09-23.md` | covered | `markets/paid-placement.md` §Baselines P16-c1; market-potential (stem cite) |
| `b-meta-q2-2026-release-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 per-engine; ai-ads-evidence E16 (stem cite) |
| `b-mi3-zeroclick-55m-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 value chain; `competitors/INDEX.md` (stem cite) |
| `b-microsoft-8k-q4-fy2026-search-advertising-2026-09-23.md` | covered | `markets/paid-placement.md` §Baselines P16-c1; market-potential (stem cite) |
| `b-microsoft-copilot-report-concern-check-2026-09-23.md` | covered | `method/demand-signals.md` L124 (stem cite); lane A |
| `b-novadata-rufus-ads-free-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 caveats, tier-6 noise (stem cite) |
| `b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23-img-2026-09-23.md` | not briefable | ACP flow diagram, no figure; text compiled in agentic-commerce.md |
| `b-openai-help-account-setup-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-ads-faq-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320); ai-ads-evidence E19 |
| `b-openai-help-billing-payment-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-budget-pacing-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-daily-budgets-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-launch-campaigns-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-maximize-results-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-product-feed-campaigns-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320); ai-ads-evidence E19 |
| `b-openai-help-quickstart-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads buying mechanics, GAP-B (L302–320) |
| `b-openai-help-sponsored-agents-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 per-engine, limited alpha (stem cite) |
| `b-perplexity-help-report-inaccurate-answers-2026-09-23.md` | covered | `method/demand-signals.md` L124 (stem cite); lane A |
| `b-ppcland-criteo-1000-brands-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 |
| `b-ppcland-gemini-ads-denial-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); ai-ads-evidence E23 |
| `b-sel-copilot-showroom-ads-2026-09-23.md` | covered | ai-ads-evidence E13 via b-microsoft-ads-copilot-formats-blog (Showroom, 25%) |
| `b-sensortower-chatgpt-ads-rising-density-repull2-2026-09-23.md` | not briefable | primary not located; ai-ads-evidence Unknowns already carries it |
| `b-seranking-chatgpt-ads-tracker-2026-09-23.md` | compiled | `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 (tracker bundling); 25.94%, 1,159 already via study raw |
| `b-seroundtable-chatgpt-ads-updates-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); ai-ads-evidence E22 |
| `b-seroundtable-google-direct-offers-2026-09-23.md` | covered | `markets/paid-placement.md` L77, Pass 12; `findings/trigger-timeline.md` L42 (2026-01-11) |
| `b-snap-my-ai-sponsored-links-2026-09-23.md` | covered | ai-ads-evidence E16 (stem cite) |
| `b-techcrunch-koah-seed-2026-09-23.md` | covered | `competitors/INDEX.md` Koah row (stem cite) |
| `b-techcrunch-meta-ai-chat-ad-targeting-2026-09-23.md` | covered | `markets/paid-placement.md` §Pass 12 per-engine (stem cite) |
| `b-trendingtopics-chatgpt-ads-eu-privacy-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); `markets/paid-placement.md` §EU and UK rules, GAP-B (L341–349) |
| `b-walmart-10k-fy2026-advertising-2026-09-23.md` | covered | `markets/paid-placement.md` §Baselines P16-c1 (stem cite) |
| `b-walmart-8k-q2-fy2027-advertising-2026-09-23.md` | covered | `markets/paid-placement.md` §Baselines P16-c1; market-potential (stem cite) |
| `b-wppmedia-netherlands-chatgpt-ads-2026-09-23.md` | compiled | `markets/paid-placement.md` §ChatGPT Ads and Gemini timeline, GAP-B (L322–339); `markets/paid-placement.md` §Vendor and company performance claims, GAP-B (L351–362); `findings/ai-ads-evidence.md` E19–E23 |

GAP-B tally: 25 compiled, 23 covered, 3 not briefable, 0 superseded. "Stem cite" = compiled doc cites the raw by name without its date suffix, missed by the filename-match audit (17 of the 23 covered). Pulls: 0; no broken pulls found.
Correction, GAP-B 2026-09-24: stem cites are 19 of the 23 covered, not 17; four covered rows rest on other raws (gml2026 collection, mediaincanada agencies, SEL Copilot, SER Direct Offers).
Line-range correction, GAP-B 2026-09-24: paid-placement GAP-B sections sit at mechanics L303–322, timeline L324–341, EU/UK rules L343–351, performance claims + caveats L353–364; table rows above cite ranges 1–2 lines early.

### GAP-ACEF — 2026-09-24

| raw file | verdict | target or reason |
|---|---|---|
| `a-practitioner-github-open-prompt-visibility-tool-2026-09-22.md` | compiled | `markets/organic-recommendation.md` §Engine spread and orphan lane-A items |
| `a-practitioner-hackernews-chatgpt-recommend-discussion-2026-09-22.md` | not briefable | tier 6, no figure; graded "Not a case", `e-case-census-c5` row 2 |
| `a-practitioner-hackernews-sitefire-launch-discussion-2026-09-22.md` | not briefable | tier 6, no figure; `e-case-census-c5` row 7 |
| `a-practitioner-linkedin-shivam-srivastava-chatgpt-ads-gap-2026-09-22.md` | not briefable | tier 6, no metric; `e-case-census-c5` row 9 |
| `a-refibuy-ai1000-rankings-2026-09-22.md` | compiled | organic §Engine spread; `markets/agentic-commerce.md` §Merchant readiness |
| `a-similarweb-openai-dsa-country-cut-walls-2026-09-23.md` | compiled | unknowns recorded, organic §Engine spread |
| `c-adobe-analytics-q2-2026-traffic-report-repull2-2026-09-23.md` | compiled | unknown recorded, agentic §Merchant readiness |
| `c-cloudflare-pay-per-crawl-docs-2026-09-23-img-2026-09-23.md` | compiled | agentic §Merchant readiness (diagram, no figure) |
| `e-case-5w-ai-communications-report-repull2-2026-09-23.md` | compiled | unknown recorded, `findings/proof-scorecard.md` §Orphan case files |
| `e-case-athenahq-new-multi-2026-09-23.md` | covered | proof-scorecard V1–V4, cited by stem |
| `e-case-boily-dental-geo-comparison-primary-2026-09-23-img-2026-09-23.md` | compiled | proof-scorecard §Orphan case files (footnote); figures agree L128 |
| `e-case-boily-dental-geo-comparison-primary-2026-09-23.md` | compiled | same |
| `e-case-ddg-vendor-multi-2026-09-23.md` | covered | proof-scorecard A1–A4, cited by stem |
| `e-case-fresha-google-agentic-2026-09-23.md` | compiled | agentic §Merchant readiness |
| `e-case-jonathanmall-geo-experiment-primary-2026-09-23-img-2026-09-23.md` | compiled | proof-scorecard §Orphan case files (per-page values) |
| `e-case-jonathanmall-geo-experiment-primary-2026-09-23.md` | compiled | same ("1,353" queries) |
| `e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-primary-2026-09-23-img-2026-09-23.md` | compiled | proof-scorecard §Orphan case files (per-type CTR) |
| `e-case-practitioner-hackernews-bando-geo-experiment-2026-09-22.md` | not briefable | tier 6 Fools gold, unquantified; `e-case-census-c5` row 3 |
| `e-case-practitioner-hackernews-firegeo-reddit-perplexity-leads-2026-09-22.md` | not briefable | tier 6 Fools gold, tool author self-measured; census c5 row 1 |
| `e-case-practitioner-hackernews-llmstxt-no-results-2026-09-22.md` | not briefable | below bar, no n or dates; census c5 row 4 |
| `e-case-practitioner-linkedin-muneeb-ahmad-chatgpt-ads-b2b-dtc-2026-09-22.md` | covered | `findings/transition-evidence.md` L91 (`-muneeb-ahmad-*`) |
| `e-case-profound-new-multi-2026-09-23.md` | covered | proof-scorecard V5–V7, cited by stem |
| `e-case-searchengineland-two-geo-experiments-primary-2026-09-23.md` | compiled | proof-scorecard §Orphan case files, X8 |
| `e-case-titles-opened-multi-2026-09-23.md` | covered | proof-scorecard T15–T17, cited by stem |
| `e-dentsu-global-ad-spend-forecast-2026-2026-09-23.md` | compiled | `findings/market-potential.md` §US / EU cuts (regional); global at `markets/paid-placement.md` L238 |
| `e-gartner-ad-platforms-prediction-2028-2026-09-23.md` | covered | `markets/paid-placement.md` L239 |
| `e-magna-dec-2025-pointer-mediaconfidential-2026-09-23.md` | covered | `markets/paid-placement.md` L240 |
| `e-magna-search-report-page-2026-09-23.md` | covered | `markets/paid-placement.md` L237; market-potential L185 |
| `e-market-size-coherent-organic-2026-09-23.md` | covered | market-potential L51, L99; organic L132 |
| `e-market-size-juniper-agentic-2026-09-23.md` | compiled | market-potential §US / EU cuts (method detail); figure at L54 |
| `e-market-size-marketintelo-organic-agentic-2026-09-23.md` | compiled | market-potential §US / EU cuts (CAGRs) |
| `e-market-size-marketsandmarkets-organic-2026-09-23.md` | compiled | market-potential §US / EU cuts (regional split) |
| `e-market-size-nextmsc-agentic-2026-09-23.md` | compiled | market-potential §US / EU cuts (2026 figure) |
| `e-wayback-profound-customers-2026-09-23.md` | covered | market-potential L226, L238 |
| `f-birdeye-multilocation-ai-search-S2-S6-2026-09-23-img-2026-09-23.md` | compiled | `customers/local-multi-location.md` §Birdeye study cover |
| `f-hubspot-state-of-marketing-2026-check-2026-09-23.md` | covered | `customers/skincare-beauty.md` L140; b2b-saas L135; high-cpa L173 |
| `f-jobboards-S1-eu-national-2026-09-23.md` | compiled | `findings/demand-map.md` §EU national job boards; organic L173 |
| `f-jobboards-S1-eu-paid-agentic-2026-09-23.md` | compiled | demand-map §EU national job boards |
| `f-linkedin-S1-eu-paid-agentic-2026-09-23.md` | covered | demand-map §EU paid and agentic cells; customers/*.md raw lists |
| `f-reddit-arcticshift-S13-brand-accuracy-2026-09-23.md` | covered | `customers/b2b-saas.md` L168 |
| `f-reddit-arcticshift-S5-eu-paid-agentic-2026-09-23.md` | covered | demand-map §EU paid and agentic cells; customers raw lists |
| `f-signal-hr-llmstxt-repull2-2026-09-23.md` | not briefable | wall again (403, PerimeterX); no figure; status unchanged |
| `f-signal-sk-llmstxt-repull2-2026-09-23.md` | not briefable | wall again (Akamai 403, waiting room); no figure |
| `f-ted-ukcf-S10-eu-paid-agentic-2026-09-23.md` | covered | demand-map §EU paid and agentic cells; customers raw lists |
| `f-vendor-S2-eu-paid-agentic-2026-09-23.md` | covered | same |
| `f-vendor-S2-yext-scout-localized-fr-it-2026-09-23.md` | covered | organic L171; b2b-saas L183 |
| `f-vendor-tradepress-S13-brand-accuracy-2026-09-23.md` | covered | `customers/skincare-beauty.md` L175 |

Tally: compiled 23, covered 17, not briefable 7, superseded 0. Most "covered" files are cited by stem without the date suffix, which the filename-match audit counted as orphan.
Tally corrected by row count: compiled 21, covered 18, not briefable 8, superseded 0 (47). The line above is wrong.
