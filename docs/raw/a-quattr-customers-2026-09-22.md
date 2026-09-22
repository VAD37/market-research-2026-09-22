# Quattr — customer case studies (screened and graded on intake)

```yaml
source:          Quattr, Inc.
url_or_doc_id:   https://www.quattr.com/case-studies/cloudeagle-boosts-clicks-and-ai-citations-with-quattr; https://www.quattr.com/case-studies/menswearhouse-increases-clicks-and-ai-visibility-using-quattr; Housing.com and Kiteworks case studies screened via `a-quattr-ai-visibility-2026-09-22.md` and `a-quattr-method-2026-09-22.md` teasers/proof-index only, full pages not opened this pull
published:       undated on both fully-opened case-study pages
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted from table default (6, vendor-reported with no n) up to 5 — both fully-opened case studies disclose n (page counts, click counts, query counts), a measurement window (though relative, not absolute-calendar), and in the Men's Wearhouse case an explicit unaffected control cohort; bias flagged per trust-rubric.md since Quattr is the vendor measuring its own customers' results with no independent third-party replication
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          CloudEagle case: unnamed AI engines collectively ("AI answers... not simulated prompts or API outputs" per the proof index scope note). Men's Wearhouse case: Google (organic + AI Mode, named separately) and ChatGPT, both with explicit before/after tables
metric_kind:     visibility (AI Citation Share, AI Mode footprint, ChatGPT citation coverage); traffic (organic clicks, Page 1/Top-3 query counts)
supersedes:      none
captured:        full text of the CloudEagle and Men's Wearhouse case-study pages; Housing.com and Kiteworks captured only as teasers/proof-index rows elsewhere in this cluster, counted as screened, not independently pulled
feature:         AI Visibility (AI Citation Share, AI Mode footprint, ChatGPT citation coverage) plus Quattr's GIGA agent and Autonomous Linking API (adjacent product capabilities within the same case studies)
```

## Verbatim

### CloudEagle case study — full text (condensed; boilerplate nav/footer elided per this cluster's convention)

Headline stats: 3× increase in AI Citation Share; 113% organic click growth; 328 net-new Page 1 queries that previously drove zero clicks; 77% of post-intervention traffic from high-intent, consideration-stage searches.

Customer: CloudEagle. Industry: B2B SaaS (Spend Management). Region: United States. "CloudEagle is an AI-powered SaaS Security, Management, and Identity Governance platform... By correlating data across IT, Security, HR, and Finance, CloudEagle provides complete visibility into application usage, user access, and software spend."

The Challenge: "Buyers were no longer researching exclusively through traditional Google SERPs. AI-mediated discovery via Google AI Overviews, ChatGPT, Perplexity, and other LLMs was increasingly shaping how prospects evaluated software." Three stated goals: optimize existing high-authority pages rather than net-new content; remove the SEO-expertise bottleneck; build semantic internal connections at scale "so search engines and LLMs could interpret CloudEagle's content as an authoritative knowledge base."

The Solution: CloudEagle deployed Quattr's GIGA AI SEO Agent and its "autonomous internal linking API," which "programmatically connected 33 priority pages into a semantic, demand-weighted link graph based on real user intent," using "actual Google Search Console queries" as anchor text sources.

The Result: "Across the 12 complete weeks following intervention, organic clicks across the pilot cohort increased from 2.47K to 5.25K, representing a +113% sustained lift." "Their AI Citation Share increased by 3× post optimizations... These insights were captured from real consumer-facing AI responses, not simulated prompts or API outputs, aligning measurement with how actual buyers experience AI search." Key outcomes: "Unlocked 328 net-new Page 1 queries that previously drove zero clicks"; "77% of post-intervention clicks coming from high-intent, consideration-stage searches"; "pricing, comparison, and buyer-stage content consistently outperformed baseline traffic levels" (no numeric baseline given for this last claim).

Quote: "Previously, everything was flowing from me. I had to give all the keywords, what to do, what topics to use. Now, it's democratized. The writers have become experts with the help of the system." — Joel Platini, Content Manager, CloudEagle.

**evidence_grade: Bronze** (on intake). Present: brand named; intervention described in detail (33-page internal-linking deployment via GIGA); numeric baseline and post figures for the headline traffic claim (2.47K → 5.25K clicks); relative date window (12 complete weeks following intervention); explicit statement that the AI-citation figure was captured from live production answers, not simulated. Missing against the full seven-item bar: no single named engine for the AI Citation Share figure (explicitly stated as unattributed to one engine); no absolute calendar date window (only "12 weeks," "post-intervention"); no unaffected control cohort; no third-party measurer — Quattr measured its own customer's result. Visibility (AI Citation Share) and traffic (clicks) only, no revenue link — Bronze, not Silver, for lack of a control metric.

### Men's Wearhouse case study — full text (condensed)

Headline stats: 10x stronger day-30 clicks on validated GIGA new content; 46% more clicks on treated product pages overall; 75% more AI Mode visibility; 50% more top-3 ChatGPT citation coverage.

Customer: Men's Wearhouse. Industry: Apparel and Fashion. Region: United States ("more than 600 stores nationwide"). Deployed Quattr's GIGA Agent and Autonomous Linking API together, built on "first-party Google Search Console Bulk Export data."

Results detail, with explicit before/after numbers:
- "Clicks rose from 771 in days 0-30 to 976 in days 31-60, while page-1 queries increased from 1,739 to 3,504 and top-3 queries grew from 1,234 to 2,603" for the validated new-content cohort.
- "12 live GIGA pages... about 2% of the entire blog URL universe" drove "16.01% of recent blog clicks," "25.46% of recent click growth," "25.73% of recent impression growth."
- Product-page result, reported in two explicitly separated layers: total treated-lineage rollout outcome (1,136 treated product page lineages) = **+46.4%** clicks over the post-rollout window; isolated linking-API effect after controlling for starting traffic and variant-opening footprint = **~7% to 8%** click advantage for the most-linked pages over the least-linked group, called out by Quattr as "statistically significant."
- **Explicit treated-vs-untreated control table** (verbatim): "Product-Page Before and After View — Cohort / Prior Window / Recent Window / Click Change. Treated product pages served from Quattr API on the blog: 11,531 → 14,424, +25.1%. Untreated control product pages not served in any Quattr API: 10,940 → 11,356, +3.8%."
- AI-surface before/after tables (verbatim): Google — Distinct queries 3,800 → 5,332 (+40.3%); Page 1 queries 25 → 31 (+24.0%); Top 3 queries 24 → 31 (+29.2%). AI Mode — Prompts/queries 59 → 103 (+74.6%); Page 1 prompts 45 → 76 (+68.9%); Top 3 prompts 42 → 58 (+38.1%). ChatGPT — Prompts 56 → 68 (+21.4%); Page 1 prompts 50 → 62 (+24.0%); Top 3 prompts 38 → 57 (+50.0%).
- "The treated product page cohort also showed statistically significant Google visibility lift versus untreated controls, with +51% more distinct queries, +61% more Page 1 queries, and +83% more Top 3 queries."

Quote: "Quattr gave us a more systematic way to move from search insight to execution. Because the workflow was built on our own Search Console data, we had more confidence in what to launch, what to optimize, and how to evaluate the outcome." — David Graveline, Sr Product Manager, Growth, Men's Wearhouse.

**evidence_grade: Silver** (on intake) — the strongest-disclosed case found across this entire P3-c4 cluster. Present: brand named (Men's Wearhouse); engines named explicitly with separate before/after tables (Google organic, Google AI Mode, ChatGPT); numeric baseline and post-intervention figures throughout, for both AI-surface metrics and the click/query counts; intervention described in detail (GIGA + Autonomous Linking API deployment); an **explicit unaffected control cohort** ("untreated control product pages not served in any Quattr API," +3.8% vs. treated +25.1% — this is the item that clears the Silver bar: "pre and post, baseline plus an unaffected control metric"); "statistically significant" language applied to the treated-vs-control gap. Missing against the full seven-item bar: no absolute calendar date window (only relative windows — "days 0-30/31-60," "trailing 26 weeks," "the observed launch window," "post-rollout window"); no third-party measurer — Quattr measured its own customer's result using the customer's first-party Search Console data, with no independent replication. Per `glossary.md`: "Silver — Pre and post, baseline plus an unaffected control metric | Cite as evidence, label correlational." **This case does not clear the plan.md seven-item bar as a qualifying "success story" (missing item 3, absolute date window) but is graded Silver on the strength of what it discloses — the first non-Bronze, non-Fools-gold grade found in this cluster's own pulls, and (per the P3-c1 census) the first Silver found across Pass 3's vendor-census clusters to date.**

### Kiteworks — screened via the AI Visibility Proof Index only (not independently opened)

Two rows appear for Kiteworks in `a-quattr-method-2026-09-22.md`'s proof-index table: "AI Overview presence, 79% expansion, window not stated" and "Content citation rate against baseline, 20% higher, within one week" — both on Google AI Overviews. **evidence_grade: Bronze** (on intake, from the proof-index summary alone) — brand and engine named, one of the two figures carries a date window (one week) and references a baseline, but no numeric baseline value, no sample size, and no independent measurer; the other figure's own vendor-stated window is "not stated." Counted as screened; the full Kiteworks case-study page itself was not opened this pull (not linked from any page reached in this cluster) — `unknown — checked quattr.com/ai-visibility, quattr.com/ai-visibility/method/ai-visibility-proof, quattr.com/case-studies 2026-09-22` for the direct Kiteworks case-study URL.

### Housing.com — screened via homepage teaser only (not independently opened)

Teaser text (from `a-quattr-ai-visibility-2026-09-22.md`): "12.8% year-over-year growth in relative search market share... grew while industry-wide clicks declined... algorithm shifts detected within days, against 18+ months of daily baseline tracking." No AI-engine-specific metric named in the teaser (this case reads as a general search-market-share story, not specifically AI-visibility evidence). **Not graded** — counted as screened only; full case-study page not opened, and the teaser alone does not establish this is even an AI-visibility case rather than a classical-SEO one.

## Pull notes — mechanical only

- Both fully-opened case-study pages fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML.
- A general case-studies index page (parallel to BrightEdge's `/resources/case-studies`) was not separately located on quattr.com this pull; the four case studies referenced across this cluster (CloudEagle, Men's Wearhouse, Housing.com, Kiteworks) were discovered via the AI Visibility page's tabs and the AI Visibility Proof Index table, not a dedicated index page — `unknown — checked quattr.com/customers (redirects to a "Customers" nav section, not independently crawled for a full list), quattr.com/case-studies (path not confirmed to exist as an index) 2026-09-22` for whether further AI-visibility case studies exist beyond these four.
- Two further case studies are named only in the proof index's companion search-outcome table with no AI-surface figure attached ("Global Consumer Technology Brand Increased Non-Brand Traffic by 37% in 6 Weeks" and "3.5M Additional Click Opportunity with Intelligent Linking," both seen in the Men's Wearhouse page's own "Case Studies" sidebar list) — the proof index itself states "Nine of the twelve studies report search outcomes only... so they are not listed" in the AI-surface table; these are counted in the screened total but not graded, since they carry no AI-surface metric to grade.
