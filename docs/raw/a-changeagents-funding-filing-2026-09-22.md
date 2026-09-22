# Change Agents Corporation / Avalon Quantum AI, LLC — primary filing record (SEC, NASDAQ: CHGA)

```yaml
source:          StockTitan (stocktitan.net), Rhea-AI-generated summaries of Change Agents Corporation's own SEC filings (10-Q, 8-K, S-1/A, DEF 14A/proxy)
url_or_doc_id:   https://www.stocktitan.net/sec-filings/CHGA/
published:       filings dated 2026-08-26 through 2026-09-21 (each summary carries its own filing date, reproduced inline below)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     downgraded from the task's specified tier 2 (SEC filing) — direct access to sec.gov, efts.sec.gov, and data.sec.gov all failed this pull (robots.txt itself returned HTTP 403 on every SEC domain tried, which the fetch tool treats as a full disallow), so the primary filing text was not reached; StockTitan's Rhea-AI summaries — AI-generated abstracts of the underlying filings, not the filings themselves — are the best available substitute and are tiered as an analyst-derived secondary source, flagged for re-verification against the primary filing by whichever pass next has SEC.gov access
source_label:    company-stated (as relayed by a third-party AI-summarization service)
lane:            A, E
sub_market:      organic recommendation
engine:          not named in any filing summary captured
metric_kind:     sales (financial/going-concern figures only; no AI-visibility-product revenue breakout found)
supersedes:      none
captured:        StockTitan's CHGA filings-list page, four fetches spanning characters 0-16000 (full page); changeagentscorp.com homepage AWS/Avalon Quantum AI item cross-referenced
```

## Verbatim — SEC filing summaries, most relevant excerpts (StockTitan/Rhea-AI, quoting or closely paraphrasing the underlying CHGA filings)

**Business description / segments** (from the 09/18/2026 05:23 PM S-1 resale-prospectus summary): "The business now centers on Agentic AI software (the Catch-Up video platform and Beacon GEO search product) and the Keto Air ketosis breathalyzer." And (from the 09/16/2026 05:11 PM Form S-1/A Amendment No. 3 summary): "CHGA has pivoted from biotech into AI-driven software (the Catch-Up agentic video platform and Beacon GEO search tool) and Keto Air consumer health products." And (from the 09/15/2026 05:26 PM summary): "CHGA has pivoted from biotech into two main businesses: an AI software segment (the Catch-Up agentic video platform and Beacon AI search-visibility product) and a consumer health segment distri[buting the Keto Air ketosis breathalyzer in North America]."

**Subsidiary naming the AI segment** (from the 08/31/2026 08:50 AM 8-K summary): "Change Agents Corporation (Nasdaq: CHGA) reported that its subsidiary Avalon Quantum AI, LLC has completed Phase 2 development of the Catch-Up agentic AI video studio platform in collaboration with Amazon Web Services and Caylent, Inc. AWS agreed to provide $125,000 of project funding, which was contingent on completing the project within seven months and has now been provided. The enhanced Catch-Up platform is designed to autonomously create personalized short-form video content for social media influencers, podcasters, and digital content creators across multiple platforms with minimal technical expertise. Beta testing of the upgraded platform is expected to begin in September 2026 as Change Agents works to advance Catch-Up toward broader commercialization within its SaaS portfolio."

**Risk factors — going concern, cash, debt** (from the 09/16/2026 and 09/18/2026 summaries, consistent across both): "CHGA... reports substantial losses, going-concern risk, only $172,000 of cash as of September 11, 2026, and roughly $2.7 million of debt." And, more fully (from the character-8000-12000 excerpt of the same page): "Risk disclosures emphasize a going-concern uncertainty, with only about $172,000 of cash as of September 11, 2026 versus an estimated $5 million cash need for 12 months, historical net losses over $17.5 million in 2025 and a large accumulated deficit, plus about $2.7 million of debt including a secured business loan and multiple high-cost notes. The stock trades on Nasdaq Capital Market under the symbol CHGA, but continued listing depends on meeting Nasdaq standards."

**Reverse split / share structure** (08/31/2026 04:05 PM 8-K summary): "Change Agents Corporation (CHGA) is implementing a 1-for-20 reverse stock split of its common stock pursuant to stockholder authorization granted on June 9, 2026... Issued and outstanding shares were reduced from approximately 21,071,803 to approximately 1,053,591... Trading on a split-adjusted basis on The Nasdaq Capital Market under the symbol CHGA begins August 31, 2026." A later summary (09/18/2026) states common shares outstanding "rising from 1,120,216 to as many as 6,400,513 shares" if a $10M Hudson Global Ventures equity line is fully drawn.

**No AI-visibility-product revenue breakout found.** No summary captured in this pull states a dollar figure of revenue attributable specifically to Beacon (or to Catch-Up). Consistent with Beacon being described as "coming soon" on the company's own site (`a-changeagents-pricing-2026-09-22.md`), and with the AWS-funded Catch-Up platform's beta only "expected to begin in September 2026," both AI products read as pre-revenue or early-revenue as of this pull. Recorded: `unknown — checked stocktitan.net/sec-filings/CHGA (17 filings tracked, most recent 2026-09-21) — no summary in this pull states a Beacon- or Catch-Up-specific revenue figure, 2026-09-22`.

**No customer count found** for Beacon or Catch-Up in any filing summary captured this pull.

## Pull notes — mechanical only

- **Blocker, load-bearing**: direct fetch of `www.sec.gov`, `data.sec.gov`, and `efts.sec.gov` all failed identically — each attempt returned "When fetching robots.txt (https://<host>/robots.txt), received status 403 so assuming that autonomous fetching is not allowed." This blocked all primary-filing access via this agent's fetch tool for the entire SEC.gov domain family, not just one path. The Chrome browser extension (the task's own stated fallback for 403s) was also checked and reported "Browser extension is not connected" — the same failure logged by a concurrent sibling agent (P2-c11) for the same session. Neither fallback was available. `bamsec.com` was tried with a guessed CIK (1922858) and returned an unrelated company (ECD Automotive Design Inc.) — the correct CHGA CIK was not independently determined this pull. `sec.report` failed with a connection error on two attempted paths.
- StockTitan's filings-list page fetched across four overlapping calls (start_index 0, 4000, 8000, 12000; a fifth call at 18000 returned "No more content available," confirming the page's content ends before that offset). No paywall or login wall encountered on StockTitan.
- StockTitan states it tracks "17 SEC filings for Change Agents Corporation," most recent filed 2026-09-21, oldest date range not fully captured in this pull (page shows an EFFECT filing 09/21/2026 back through an 08/26/2026 proxy-related 8-K; earlier filings exist per the FAQ's 17-filing count but were not individually captured).
- Task instruction ("pull the relevant sections verbatim... segment description, revenue attributed to the AI-visibility product if broken out, customer counts, risk factors naming AI search") is only partially met: segment description and going-concern risk factors are covered by the verbatim StockTitan excerpts above; no risk factor specifically naming "AI search" as a competitive or technology risk (as opposed to the company's own going-concern/liquidity risks) was found in the captured summaries; revenue-breakout and customer-count items are both recorded `unknown` above for lack of any figure in the accessible source.
