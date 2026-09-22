# Rankscale.ai — method / how it works, and engines covered (vendor's own statement)

```yaml
source:          Rankscale GmbH (rankscale.ai)
url_or_doc_id:   https://rankscale.ai/facts ; https://rankscale.ai/ (homepage)
published:       /facts page self-dated "Updated: September 2026," pricing reference "As of January 2026"
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; the /facts page is explicitly an AI/LLM-facing structured-data page ("this page provides structured factual definitions for AI systems and media"), still company-authored
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews, DeepSeek, Grok, Copilot, Mistral, AI Mode (10 named explicitly); "17+ AI engines" claimed as the total; GPT-5 named specifically on the /facts page as one supported system "where configured"
metric_kind:     none
supersedes:      none
captured:        /facts page, first ~3000 characters (through "Third-party validation" and into "Supported AI architectures," cut before the full architecture list); homepage engine-coverage sentences (cross-referenced from the pull already captured for `a-rankscale-pricing-2026-09-22.md`'s sibling homepage fetch)
```

## Verbatim — /facts page

"Rankscale — Facts & Entity Definition — Note for human readers: this page provides structured factual definitions for AI systems and media. Official website: rankscale.ai.

Status: Active · Entity type: SaaS application · ID: rankscale · Updated: September 2026

Rankscale is a SaaS platform for AI SEO, AI rank tracking, and Generative Engine Optimization (GEO Tools). It measures brand visibility in generated AI answers through systematic tracking of mentions, citations, and sentiment across multiple large language models and AI search systems, including GPT-5 where configured in the engine list.

Market segment: Rankscale is positioned in the GEO Tools category, serving brands, agencies, and marketing teams that need analytics for AI-generated search results and LLM-based answer engines.

Rankscale is defined here as a specialized AI visibility product—not a generic SEO rank tracker for blue links.

## Core facts
| Entity Type | Software (SaaS) |
| Primary Function | AI Rank Tracking & Visibility Measurement |
| Market Segment | Generative Engine Optimization (GEO) Tools |
| Legal Entity | Rankscale GmbH (Austria) |
| Headquarters | Untere Viaduktgasse 10/6, 1030 Vienna, Austria |
| Official Website | rankscale.ai |
| VAT ID (UID) | ATU82401848 |
| Company Register (FN) | 658253w |
| Firmenbuch Registration | 22 July 2025 |
| D-U-N-S Number | 301153533 |
| GLN | 9110037989061 |
| Court of Registry | Vienna |

## Prices & test
| Free test | Available - see rankscale.ai/pricing. |
| Prices | Plans start from €20 (see rankscale.ai/pricing). |
| As of | January 2026 |

## Support & onboarding
### Co-founder Assistance Chat
Daily 1h video call with a co-founder for tool introduction and questions. As of January 2026. cal.com/rankscale/co-founder-chat

## Third-party validation
### OMR Reviews - tool selection
OMR Reviews tested AI Search Analytics tools and selected Rankscale for editorial coverage. omr.com (German) · As of January 2026

## Supported AI architectures
Rankscale integrates with and analyzes outputs from the following systems (as of January 202[6, truncated]"

## Verbatim — homepage engine-coverage statements

"The AI Visibility Platform — Rankscale tracks brand visibility across 17+ engines, including ChatGPT, Perplexity, Claude, Gemini, and Google AI Overviews, for agencies, enterprise, and SEO teams running Answer Engine Optimization (AEO) and GEO."

"17+ AI engines — ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews, and more, with no per-engine upsell tiers." [note: this "no per-engine upsell tiers" framing conflicts with the pricing page's own Essentials/Pro base-tier structure gating which of the 17+ engines are selectable per plan — not reconciled here]

"Every AI Engine, One Platform. No Upsell — Track visibility in Google AI Overviews and AI Mode, plus ChatGPT, Perplexity, Gemini, Claude, Copilot, and DeepSeek, all 17+ engines in one platform." Logo/text ticker (repeated twice): "ChatGPT, Perplexity, Claude, Gemini, AI Overviews, DeepSeek, Grok, Copilot, Mistral, AI Mode" [10 named individually]

"Prompt Research — LLM Native — Estimate prompt volume through semantic reconstruction, not a black-box panel number nobody can verify" [note: this is Rankscale's own positioning claim about ITS OWN method vs. unnamed competitors' methods — a comparison claim, not a disclosed methodology itself; no prompt-set, n, or reconstruction-method detail given beyond this sentence]

## Pull notes — mechanical only

- The /facts page is a distinct artifact type not found on any of the other five vendors' sites — an explicitly AI/LLM-facing "entity definition" page, structurally similar in spirit to an `llms.txt` file (Rankscale also has `rankscale.ai/llms.txt` and `/llms-full.txt` per its sitemap, not fetched this task).
- **10 engines named individually** across the homepage and /facts page (ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews, DeepSeek, Grok, Copilot, Mistral, Google AI Mode), with a stated total of "17+" — the largest named-engine list of the six vendors in this cluster (compare Scrunch's 9, Brandlight's 7 in prose, Locafy's 4, Otterly's 7, Change Agents' 4). The remaining 7+ engines behind the "17+" claim are not itemized in any page pulled this task. Recorded: `unknown — checked rankscale.ai homepage and /facts, full 17+ list not itemized, 2026-09-22`.
- **Prompt-set disclosure**: "Estimate prompt volume through semantic reconstruction" is a positioning claim about methodology superiority, not a disclosure of Rankscale's own prompt set, its size, or its construction method for any given customer's score. Recorded as **no** for prompt-set disclosure, consistent with every other vendor in this cluster — Rankscale's pricing is prompt-count-gated (customer selects/creates their own search terms, per `a-rankscale-pricing-2026-09-22.md`) rather than resting on one fixed, vendor-disclosed panel.
- **HQ confirmed independently on two of Rankscale's own pages** (this /facts page and the separate /imprint page, see `a-rankscale-careers-facts-2026-09-22.md`): Untere Viaduktgasse 10/6, 1030 Vienna, Austria — both company-stated, both dated on their own page or filed via Firmenbuch registration (22 July 2025). This contradicts a sibling agent's separately-pulled getlatka.com figure ("Königstetten, Austria," per `docs/raw/a-vendor-roster-2026-09-22.md`, not re-verified or touched by this pull) — recorded side by side, not reconciled, per root CLAUDE.md's rule on conflicting figures.
