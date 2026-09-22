# Primerica, Inc. — 10-K FY2025 — S7 filed mention of "generative engine optimization"

```yaml
source:          Primerica, Inc. (NYSE: PRI), SEC EDGAR
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1475922/000119312526082233/pri-20251231.htm ; CIK 0001475922 ; accession 0001193125-26-082233
published:       2026-02-27 (10-K filing date; period ending 2025-12-31)
pull_date:       2026-09-22
pull_method:     fetch (direct curl of the SEC Archives HTML path, no browser extension)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default for a filed SEC document
source_label:    filed
lane:            E, F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        one passage (executive-bio paragraph) located by full-text grep across the 9,336,323-byte filing; found via a targeted `efts.sec.gov` full-text search, then the source passage located and quoted directly from the filing itself
vertical:        high-CPA regulated — insurance (Primerica Life Insurance Company; Primerica is a NYSE-listed financial-services/life-insurance and investment-products company)
cell:            organic recommendation / unassigned — no headcount or revenue figure for Primerica was located in the text extractable by this pull's method (see Pull notes); NYSE listing and the filing's own "Kathryn E. Kieser has served as Executive Vice President and Chief Reputation Officer... since January 2019" tenure are qualitative scale indicators only, not a numeric headcount/revenue per `demand-signals.md`'s boundary rule
query:           `efts.sec.gov/LATEST/search-index?q=%22generative+engine+optimization%22&forms=8-K,10-Q,10-K&dateRange=custom&startdt=2026-01-01&enddt=2026-09-22` (18 filer hits, Primerica the only insurer/high-CPA-regulated match; see table in Pull notes)
```

## Verbatim

> "Kathryn E. Kieser has served as Executive Vice President and Chief Reputation Officer of Primerica, Inc. and President and Chair of the Primerica Foundation since January 2019, **leading public relations, social media, search and generative engine optimization, enterprise research and philanthropy**. Previously, she served as Executive Vice President of Investor Relations from April 2010 to December 2018. Ms. Kieser joined Primerica in October 1995 and has held many positions over her career including Vice President of Sales and Product Marketing, Senior Vice President of Auto and Homeowners Insurance, and Chief Marketing Officer for Primerica Life Insurance Company (PLIC)."

— Primerica, Inc. 10-K, fiscal year 2025, filed 2026-02-27, executive-officer biography section.

## Pull notes

- Found via an EDGAR full-text search for the exact phrase `"generative engine optimization"` across forms 8-K/10-Q/10-K, dated 2026-01-01 to 2026-09-22. That search returned 18 distinct filer hits; the great majority are vendors already covered elsewhere in this repo (Change Agents Corporation, Direct Digital Holdings, TechTarget, Onfolio Holdings, Adobe, Semrush Holdings, Upland Software, Zeta Global, Intuit, Fastly, Coty) or off-target micro-caps (Glidelogic Corp, Intelligent Protection Management Corp, Ooma). **Primerica, Inc. (SIC 6311, life insurance) is the only high-CPA-regulated-vertical filer among the 18**, and the only one confirmed by this pull to be a buyer (an insurer whose own executive owns a GEO-adjacent function) rather than a vendor or an off-target hit.
- This filer was **not** among the filings already cited by `docs/raw/e-case-census-c1-2026-09-22.md` (P4-c1's earnings-call/investor-deck census, which covers NerdWallet, LendingTree, EverQuote, Yelp, IAC/People Inc., Chegg, TechTarget, Criteo, Reddit) — it is a genuinely new finding for this cluster.
- The passage is an **executive-officer biography**, not a job posting and not an earnings-call remark. It is filed under S7 ("earnings-call and investor-deck mentions... named spend line if any") per the task's own routing instruction, on the reasoning that it is the filed-document equivalent of "budgeted intent" evidence: it names an existing, filled, C-suite-level role ("Executive Vice President and Chief Reputation Officer") whose responsibilities explicitly include "generative engine optimization" — filed at tier 2, a stronger provenance than an open job posting (tier 3) would be, since it evidences an ongoing function rather than an intent to hire.
- **Employee headcount was not located.** This pull attempted `grep`-based extraction of "full-time employees," "approximately [n] employees," and the filing's "Human Capital Management" section; the section was located but the specific headcount figure is rendered via XBRL inline-tagging that this pull's text-extraction method (plain-text grep across the raw HTML) could not reliably isolate from surrounding markup. Per `demand-signals.md`'s boundary rule ("if it cannot be mapped without a guess, record `unassigned`"), buyer size is recorded `unassigned` rather than guessed from Primerica's public profile.
- No `supplement`-vertical filer and no credit-card-issuer filer was found by parallel EDGAR full-text searches this pull: `"ChatGPT" "dietary supplement"` (0 hits); `"AI search" "credit card"` and `"AI Overviews" "credit card"` (12–17 hits, all off-target — TripAdvisor, Onfolio, LendingTree [already known], Yelp, 1-800-Flowers, Freshworks, Expedia, Walmart, Reddit, Eventbrite, DiamondRock Hospitality, TruBridge, Atlassian, Host Hotels, Trump Media & Technology Group — none is a credit-card issuer or supplement brand naming an AI-search/AI-Overviews effect on itself).

## Caveats

- This is one passage from one filing, not a repeated or independently-corroborated finding. It is filed at tier 2 (filed) per the trust rubric's provenance ranking, which ranks provenance, not the strength of what the passage proves — a title mentioning a function is weaker evidence of "spend" than a disclosed budget line, and this passage names no dollar figure.
- The EDGAR full-text search index only covers US SEC registrants (per `channels.md` C13's stated bias); private insurers, private card issuers, and private supplement brands are structurally invisible to this channel.
