# StockTitan — Criteo (CRTO) stock news page — admission-rule second source

```yaml
source:          StockTitan (stocktitan.net) — third-party financial-news aggregator, independent of Criteo
url_or_doc_id:   https://www.stocktitan.net/news/CRTO/
published:       page aggregates releases through 2026-09-16; page itself undated as a standalone document
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool, plain HTTP, no browser needed)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted down from table default 3 — StockTitan's "Rhea-AI Summary" content is AI-generated summarization of the underlying press release/filing, not the filing itself; SEC.gov direct access returns HTTP 403 to this session's fetch tool (robots.txt-based refusal, matching every prior P2/P3 cluster's identical finding per docs/method/STATE.md), so this is used as the substitute per that precedent
source_label:    analyst-derived
lane:            B
sub_market:      paid placement
engine:          n/a — financial reporting on the company, not an assistant engine
metric_kind:     sales
supersedes:      none
captured:        page excerpt — company description plus the four most recent news items at pull time
```

## Verbatim

"Criteo (CRTO) Stock News & Updates | StockTitan"

"Welcome to our dedicated page for Criteo news (Ticker: CRTO), a resource for investors and traders seeking the latest updates and insights on Criteo stock."

"**Criteo S.A.** reports developments around its commerce intelligence and digital advertising platform, which connects brands, agencies, retailers, publishers, and media owners through AI-driven campaign decisioning. Company news commonly covers Retail Media and Performance Media results, activated media spend, **product updates such as Criteo GO, AI advertising integrations, and retail or commerce partnerships**."

"09/16/2026 06:02 AM — News — Criteo Expands Regional Reach Through New Reseller Partnership with Tyroo — Rhea-AI Summary: Criteo (CRTO) has entered a strategic reseller partnership with ad tech company Tyroo Technologies to expand its presence in Thailand, Malaysia and the Philippines. Under the agreement, Tyroo will promote Criteo's performance media solutions in these markets... builds on an existing relationship between the two companies in India since 2021."

"08/25/2026 07:00 AM — News — CRITEO TO PRESENT AT THE CITI 2026 GLOBAL TMT CONFERENCE ON SEPTEMBER 8, 2026 — Rhea-AI Summary: Criteo (NASDAQ: CRTO) announced that CEO Michael Komasinski will present at the Citi 2026 Global TMT Conference..."

"08/05/2026 07:00 AM — News — CRITEO APPOINTS CONNOR MCGOGNEY AS CHIEF FINANCIAL OFFICER — Rhea-AI Summary: Criteo (NASDAQ: CRTO) appointed Connor McGogney as Chief Financial Officer, effective August 10, 2026... He succeeds Sarah Glickman, CFO since 2020..."

"08/05/2026 07:00 AM — News — CRITEO REPORTS SECOND QUARTER 2026 RESULTS — Rhea-AI Summary: Criteo (NASDAQ: CRTO) reported **Q2 2026 revenue of $428 million, down 11% year-over-year**, with gross profit of $222 million and Contribution ex-TAC of $255 million, all declining double digits. GAAP net income was $[truncated by tool output limit]"

## Pull notes — mechanical only

- Fetched via plain HTTP fetch tool. Content truncated by the tool's max_length mid-sentence in the Q2 2026 results item; not re-fetched at a higher start_index since the load-bearing fact (Criteo S.A. is a Nasdaq-listed, publicly reporting company, ticker CRTO) was already captured.
- Direct sec.gov access not attempted for this vendor in this pull, consistent with the identical block already logged for Feedonomics/Commerce (CMRC) in this same cluster and by P3-c2/P3-c3 in `docs/method/STATE.md`.
- **Admission-rule role**: this is the second, independent-of-Criteo source required by this task's admission rule, alongside source 1 (`docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md`, OpenAI's own ads-partner page naming Criteo as a "technology partner"). StockTitan is a third-party financial-news aggregator with no disclosed commercial relationship to Criteo, satisfying limb (a)'s "two or more independent non-listicle sources" test.
- Q2 2026 revenue ($428M, company-wide, down 11% YoY) is Criteo-wide, not broken out by product line (Criteo GO vs. the broader Commerce Media Platform) on this page — recorded as company-level, not a Criteo-GO-specific figure. `unknown — checked stocktitan.net/news/CRTO 2026-09-22, no Criteo-GO-only revenue line item found`.
