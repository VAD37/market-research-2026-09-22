# Semrush — AI Visibility Index methodology

```yaml
source:          Semrush
url_or_doc_id:   https://ai-visibility-index.semrush.com/; https://ai-visibility-index.semrush.com/methodology
published:       undated; data currency stated as "August 2026" on the index page
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     adjusted from table default (3, platform primary) up to reflect published n, date window and method — this is closer to a tier-4/5 vendor study than a plain product page, though it measures the market broadly (brand mentions/citations across many companies) rather than Semrush's own product, so the "vendor measuring the thing it sells" bias does not directly apply here the way it does to the customer case studies
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Google AI Mode, Google AI Overview, Gemini — the four platforms named as covered
metric_kind:     visibility
supersedes:      none
captured:        full text of both pages
feature:         AI Visibility Index — Semrush's free public study/benchmarking tool, built on the same underlying data infrastructure as the paid AI Visibility Toolkit product; answers this cluster's prompt-set/n/method disclosure question for Semrush
```

## Verbatim

### AI Visibility Index — overview page

"THE DEFINITIVE ANALYSIS OF AI VISIBILITY — See the patterns. Spot the gaps. And learn how to lead. Get new results every month." Data currency control shown as "August 2026 (1/8)" — read as month 1 of an 8-month-deep data window, or the 1st of 8 available monthly snapshots (page does not state which).

Headline stats: "4.4x — Users who search with LLMs are 4.4× more likely to convert than those using search engines." "2028 — AI-generated results are projected to overtake organic search traffic by 2028." "2.5b — Every day, ChatGPT receives 2.5 billion prompts from over 190 million users." [note: these three stats carry no source citation of their own on this page — recorded as Semrush's own stated figures, not independently sourced or graded as a case here]

"(03) Source Analysis — See which sources fuel the most AI answers... Sources are ranked by total citations across more than 126 million US AI search prompts." "(04) AI Platform Analysis — Deep dive into the similarity of the top sources and brand mentions for each AI platform by vertical... We analyzed how similar the top 100 mentioned brands are across all four major AI platforms: ChatGPT, Google AI Mode, Google AI Overview, and Gemini."

Metric definitions (verbatim, from in-page "Metrics explained" panels): "Mentions — A measure of visibility reflecting how often a brand name appears in an AI answer." "Citations — A measure of authority reflecting how often a brand's domain is cited as a source in an AI answer." "Mention-mention overlap — We take the top 100 mentioned brands from each pair of platforms and count how many appear in both lists. A higher number means the two platforms agree more on which brands are talked about." "Source-source overlap — We take the top 100 cited sources from each pair of platforms and count how many appear in both lists." "Source-mention overlap — We take the top 100 sources and the top 100 mentioned brands for each AI platform, and count how many appear in both lists."

### Methodology page — full text

"To understand how the major AI search platforms create responses and recommend brands, we analyzed Semrush's database of more than 126 million real US AI search prompts, covering ChatGPT, Google AI Mode, Google AI Overview, and Gemini. From this, we extracted the most mentioned brands and most cited domains across 22 industries."

"The prompt dataset — Our US prompt database has been curated, deduplicated, topic-organized prompts sourced from AI search clickstream data and Google's keyword dataset for AI Overviews." Three named characteristics: "(01) 126 million prompts and growing" (example: "Best running shoes"); "(02) Deduplicated with intent and semantics maintained" (example: "Best waterproof running shoes"); "(03) Enhanced with Datos clickstream and Google AI Overviews keyword data" (example: "Best waterproof running shoes to buy").

"How we collected the data — Our dataset captures what real users are searching for across the four major AI platforms. The data comes from two complementary signals: clickstream data showing actual user interactions with AI search tools, and Google's AI Overview keyword dataset. Coverage spans ChatGPT, Google AI Mode, Google AI Overview, and Gemini, in the US."

"What we measured — AI Visibility score: A Semrush metric that combines how often a brand shows up in responses with how consistently this is compared to other brands. Mentions: When and how often brands appeared in the AI answers. Citations: How often a domain is cited as a source in AI answers. Both raw citation counts and the share of all prompts a domain appears in. Audience and topic volume: How much search demand sits behind each topic where a brand or source appears, for a weighted view of visibility."

"How we ranked results — Each chart clearly states the metric used (mentions, citations, or similarity). For cross-platform comparisons, we present results separately for each of the four AI platforms rather than combining them into a single weighted score, because the four platforms behave differently enough that aggregation would hide insights. Where appropriate, we use rank correlation (Spearman) to measure how closely two platforms agree on brand and source rankings."

"How we manage variability — Because AI responses can change from day to day, we collected data over longer timeframes and averaged the results to ensure consistency."

## Pull notes — mechanical only

- Both pages fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML.
- **Prompt-set/n/method disclosure answer for Semrush: partial, and the strongest disclosure found on Semrush's own domain in this cluster.** N is disclosed (126 million US AI search prompts), data sources are named (Datos clickstream data plus Google's AI Overview keyword dataset), the four covered engines are named, the statistical method for cross-platform comparison is named (Spearman rank correlation), and the variability-handling approach is described qualitatively ("collected data over longer timeframes and averaged"). Not disclosed: the literal list of prompts (only illustrative examples like "Best running shoes" are shown); the exact averaging window length; and whether this same 126M-prompt corpus and method is identical to what powers the *paid* product's per-customer "50/100/200 prompts to track daily" tier limits (the pricing page's language — customer-selected/tracked prompts — describes a different mechanic than this Index's own broad corpus mining, and no page pulled this cluster states whether or how the two relate).
- This Index is a free public marketing/research artifact, distinct from (but data-infrastructure-adjacent to) the paid AI Visibility Toolkit product that the roster and 10-K name — flagged so the compiling pass does not conflate "Semrush discloses n/method for its public Index" with "Semrush discloses n/method for the customer-facing composite score inside the paid product," which remains `unknown — checked semrush.com/features/ai-visibility, semrush.com/pricing 2026-09-22` for the latter specifically.
