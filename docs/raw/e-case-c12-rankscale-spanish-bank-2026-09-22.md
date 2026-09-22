# Rankscale — Spanish bank AI-search visibility case study

```yaml
source:          Rankscale GmbH (rankscale.ai), Case Studies — partner agency Pixelclip, author Eduard Maeso
url_or_doc_id:   https://rankscale.ai/case-studies/spanish-bank-ai-search-215-top3-growth
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch (curl, direct)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor-authored case study (Rankscale GmbH, an AI-visibility measurement vendor headquartered in Vienna, Austria) about its own product's use by a partner agency on an anonymised client, with no engine named, no absolute date window, no baseline value, and only a vague sample-size bucket ("hundreds of specialized prompts") — trust-rubric.md "vendor measuring the thing it sells, no third-party replication" with hidden method (no prompt count, no per-engine breakdown) drops it from the table default 5 to 6
source_label:    vendor-reported
lane:            E, F
sub_market:      organic recommendation
engine:          not named — "major AI engines" / "generative answer engines" stated generically, no ChatGPT/Gemini/Claude/Perplexity/Copilot named individually for this case
metric_kind:     visibility (visibility increase %, top-3 placement growth %, share of voice rank)
supersedes:      none
captured:        full page
language:        English
country:         Spain (brand's market, as the source states it: "one of Spain's leading Tier-1 banking groups")
vertical:        high-CPA regulated (page's own category tags: "Banking & Fintech / Tier-1 Financial Institution")
evidence_grade:  Bronze (visibility-only claim, no revenue link; missing bar items below)
paid_by_outcome: unknown — not stated on page
```

## Verbatim

Title: "How a Leading Spanish Bank Achieved +215% Growth in Top-3 AI Search Placements"

Subtitle: "A generative engine optimization strategy that turned AI search into a dominant visibility channel for one of Spain's largest banking groups."

Category tags: "Case Study / Banking & Fintech / Tier-1 Financial Institution"

Partner agency: Pixelclip · Author: Eduard Maeso

Headline metrics (verbatim, as displayed): "+180% Visibility Increase" / "+215% Top-3 Ranking Growth" / "#1 Share of Voice vs. Competitors"

"The Client — The client is one of Spain's leading Tier-1 banking groups-a household name in financial services with deep digital authority across traditional search. Despite this strong foundation, a growing wave of fintech disruptors was outpacing them in an emerging channel: AI-driven search. As consumers increasingly turned to generative engines for financial guidance, the bank's visibility in these new ecosystems lagged behind smaller, more agile competitors."

"The Ask — Could a legacy banking institution reclaim its authority in the AI search landscape-and become the primary source for high-intent financial queries like 'best mortgage rates' and 'sustainable investment funds'? The client needed a comprehensive AI-visibility audit and a strategic roadmap to dominate brand mentions across generative answer engines, all while maintaining strict regulatory compliance."

"Steps Taken in Rankscale — 01 Audit & Benchmark: Using Rankscale's visibility tracking, the team mapped the bank's current presence across major AI engines. Hundreds of specialized prompts were deployed to benchmark performance against fintech competitors across high-priority financial categories. 02 Research & Configure: The team clustered prompts by buyer persona and financial product line, then leveraged Rankscale's AI-driven recommendations to systematically refine landing pages and technical infrastructure-aligning content architecture with generative search patterns. 03 Execute & Track: Real-time citation data from Rankscale fueled a high-impact digital PR strategy, concentrating authority-building efforts on the exact sources and narratives that AI engines were already prioritizing in the banking sector. Progress was monitored via Rankscale dashboards in iterative optimization sprints."

"Results — +180% visibility increase for priority financial topics. Within the AI search ecosystem, the bank's brand authority saw a substantial lift across all tracked categories. High-intent queries that previously surfaced competitor content now consistently referenced the client's products and expertise. +215% growth in top-3 generative search placements. By optimizing technical infrastructure and content architecture specifically for AI engines, the client secured the leading share of voice against both traditional banking competitors and emerging fintech disruptors-a position that compounds over time as citation authority builds. A new strategic channel for long-term competitive advantage. The engagement transformed AI search from an unmonitored blind spot into a structured growth channel with clear reporting and ongoing optimization. Pixelclip and the banking group have expanded their partnership to cover additional product lines and international markets."

## gloss (agent translation):

Page is already in English; no translation needed. Numbers-bearing passage restated for clarity: bank achieved **+180% visibility increase** for priority financial topics and **+215% growth in top-3 generative search placements**, reaching **#1 share of voice** versus competitors, measured via Rankscale's tracking dashboards over an audit-then-execute engagement of unstated duration, using "hundreds" of unspecified prompts.

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Partial** | "one of Spain's leading Tier-1 banking groups" — anonymised, no company name; specified only by country and tier |
| 2 | The engine or engines | **Absent** | "major AI engines" and "generative answer engines" — no ChatGPT/Gemini/Claude/Perplexity/Copilot named individually |
| 3 | The date window, absolute | **Absent** | No date, month, or year appears anywhere on the page for either the engagement or the measurement |
| 4 | The baseline before intervention | **Absent** | Only percentage deltas given ("+180%", "+215%"); no starting visibility %, ranking count, or share-of-voice value stated |
| 5 | The intervention itself | **Present** | Three-step process: audit & benchmark, research & configure, execute & track — described with specifics (prompt clustering by persona, content/technical refinement, digital PR) |
| 6 | The sample size, or the traffic volume | **Partial** | "Hundreds of specialized prompts" — an order-of-magnitude bucket, not a stated count |
| 7 | Who measured, and whether they were paid by the outcome | **Partial** | Measurer named: Rankscale (the vendor publishing the case study) and partner agency Pixelclip. No statement of fee structure or whether payment was contingent on the outcome |

**Full-page grade: Bronze.** Visibility-only claim (visibility %, top-3 ranking growth %, share-of-voice rank) with no revenue or sales figure — fits Bronze by definition regardless of the missing items. Missing against the full seven-item bar: item 2 (no engine named), item 3 (no date window at all), item 4 (no baseline value). Items 1, 6 and 7 partial.

## Pull notes — mechanical only

- Fetched via direct `curl` GET, HTTP 200, full case-study page captured in one pull including header/footer chrome; site is Next.js-rendered but this page's body content is present in the server-delivered HTML (confirmed by full-text extraction), unlike Rankscale's own case-studies index page, which required a follow-up fetch to resolve exact case-study slugs via `<a href>` links.
- Rankscale GmbH states "Made with precision in Vienna" in its footer — the vendor itself is Austria-headquartered (EU), distinct from the Spanish bank client described in the case.
- No client name, no engine name, and no date are disclosed anywhere on this page — a materially thinner disclosure than Rankscale's own MiniFinder case study (`e-case-c12-rankscale-minifinder-germany-2026-09-22.md`), pulled the same session from the same case-studies index.
