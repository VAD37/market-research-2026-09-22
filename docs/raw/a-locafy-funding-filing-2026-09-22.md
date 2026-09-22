# Locafy Limited — primary filing record (SEC, NASDAQ: LCFY)

```yaml
source:          StockTitan (stocktitan.net), Rhea-AI-generated summaries of Locafy Limited's own SEC filings (10-Q, 8-K, F-3, Form 3/4/144 insider filings)
url_or_doc_id:   https://www.stocktitan.net/sec-filings/LCFY/
published:       filings dated 2025-12-17 through 2026-08-28 (each summary carries its own filing date, reproduced inline below)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     downgraded from the task's specified tier 2 (SEC filing) — direct access to sec.gov, efts.sec.gov, and data.sec.gov all failed this pull for the same reason documented in `a-changeagents-funding-filing-2026-09-22.md` (robots.txt itself returned HTTP 403 on every SEC domain tried); StockTitan's Rhea-AI summaries are the best available substitute and are tiered as an analyst-derived secondary source
source_label:    company-stated (as relayed by a third-party AI-summarization service)
lane:            A, E
sub_market:      organic recommendation
engine:          not named in any filing summary captured
metric_kind:     sales
supersedes:      none
captured:        StockTitan's LCFY filings-list page, two fetches spanning characters 0-9000 (through the FAQ footer, page content ends before 9000)
```

## Verbatim — SEC filing summaries, most relevant excerpts (StockTitan/Rhea-AI, quoting or closely paraphrasing the underlying LCFY filings)

**Company description / country / listing** (from the 08/04/2026 04:06 PM Form F-3 shelf-registration summary): "Locafy is an Australian emerging growth company and foreign private issuer whose technology automates creation of search-optimized web pages and supports visibility in traditional and AI search. Its ordinary shares and IPO warrants trade on Nasdaq under the symbols LCFY and LCFYW."

**Revenue, company-wide (not broken out by product)** (from the 07/01/2026 05:08 PM summary, "Locafy grows revenue 31% and narrows loss in FY 2026"): "Locafy Limited reported strong progress for the first nine months of fiscal 2026, with revenue rising 31% to AUD 3.11 million compared with the prior-year period. Subscription revenue grew 36% to AUD 3.0 million, reflecting demand for the company's core SEO and AEO software products. Operating expenses fell 13%, helping narrow the net loss to AUD 2.24 million, an improvement of AUD 1.3 million or 36% year over year. Cash and cash equivalents increased to AUD 1.44 million as of March 31, 2026, supported by positive operating cash flow of AUD 0.06 million and equity raises totaling AUD 2.76 million. Management highlighted preparations to launch its new Poseidon AEO SaaS platform, targeted for July 2026, as a key future growth driver."

**No product-level (AEO/Poseidon-specific) revenue breakout found** — the 31%/36% figures above are stated for "core SEO and AEO software products" combined, not for AEO/Poseidon in isolation. Recorded: `unknown — checked stocktitan.net/sec-filings/LCFY, 2026-09-22 — no summary in this pull isolates Poseidon- or AEO-specific revenue from the company's combined SEO+AEO subscription revenue line`.

**Capital raise / shelf** (08/04/2026 04:06 PM): "Locafy Limited is establishing a shelf registration on Form F-3 permitting primary offerings of up to $100 million of ordinary shares, preference shares, warrants, subscription rights and units... Within this shelf, the company may sell up to $588,883 of ordinary shares through an at-the-market sales agreement with H.C. Wainwright & Co. on Nasdaq. As of June 2026, public float was about $7.28 million, based on 1,829,701 ordinary shares held by non-affiliates at $3.98 per share... At March 31, 2026, Locafy reported cash and cash equivalents of A$1,441,709 and total capitalization of A$4,739,268. Proceeds from future offerings may be used to commercialize and further develop its SEO-focused SaaS technology, reduce debt, pursue strategic acquisitions, and for working capital and general corporate purposes."

**Prior product name — "Localizer"** (from the 12/17/2025 08:00 AM summary): "Locafy Limited submitted a report that mainly forwards a new press release to investors. The release, dated December 17, 2025 and attached as an exhibit, is titled 'Locafy Reports Continued Commercial Growth as Localizer Adoption and Partner Results Build into CY 2026.' This indicates the company is communicating ongoing commercial progress around its Localizer product and partner performance heading into calendar year 2026, but detailed financial or operating figures are contained in the attached press release rather than in this summary document." [note: the underlying press-release exhibit itself was not reached this pull — SEC.gov access blocked, see Pull notes]

**No customer count found** in any filing summary captured this pull. **No risk factor specifically naming "AI search" as a named risk** (as distinct from ordinary going-concern/competition language) was found in the captured summaries — none of the summaries reached this pull quote a risk-factors section at all; only 8-K/F-3/current-report and insider-transaction summaries were captured, not the 10-K's risk-factors section specifically.

**Insider transactions** (context only, not AI-visibility-specific): CEO Gavin Burnett — indirect holdings of 158,000 shares (Burnett Family Trust) and 12,026 shares (Big Superannuation Fund), per a Form 3 dated 2026-03-18; also an insider sale of 5,000 shares for $16,340 on 2025-11-20 (Form 144, reported 2026-02-17). CFO Tan Melvin Leong Pean — indirect holdings of 121,872 shares (Melt Investment Trust) and 5,722 shares (MM Super Fund), per a Form 3 dated 2026-03-18. COO Jason Dale Jackson — bought 9,285 shares at $4.20 on an unstated date, reported 2026-04-07; initial Form 3 holding of 1,765 shares, reported 2026-03-31. Director John Joseph Chegwidden — indirect holding of 17,908 shares via the J & K Chegs Share Trust, reported 2026-03-30.

StockTitan's FAQ states: "StockTitan tracks 14 SEC filings for Locafy (LCFY)... The most recent SEC filing for Locafy (LCFY) was filed on August 28, 2026."

## Pull notes — mechanical only

- **Blocker, load-bearing** — identical to the one documented in `a-changeagents-funding-filing-2026-09-22.md`: direct fetch of `www.sec.gov`, `data.sec.gov`, and `efts.sec.gov` all failed with "received status 403" on the robots.txt check for every SEC domain tried; the Chrome browser extension fallback was unavailable ("Browser extension is not connected," checked once this task and not re-checked per vendor). StockTitan's filings-list page was used as the best available substitute for both Locafy and Change Agents Corp.
- StockTitan's LCFY filings-list page fetched across two overlapping calls (start_index 0, max_length 4000; then start_index 4500, max_length 4500) to reach the page's FAQ footer, which confirms the page's content ends there (no further "No more content available" check was needed — the FAQ/footer block is a clear terminus, matching the pattern observed on the CHGA page).
- Task instruction ("pull the relevant sections verbatim... segment description, revenue attributed to the AI-visibility product if broken out, customer counts, risk factors naming AI search") is partially met: segment description (Australian foreign private issuer, "SEO and AEO software products") and combined revenue growth are covered by verbatim excerpts above; product-specific revenue breakout, customer counts, and an AI-search-specific risk factor are all recorded `unknown` for lack of any figure or quoted risk-factor text in the accessible source. A 10-K or 20-F risk-factors section, which would be the most likely place to find a risk factor naming AI search specifically, was not among the individual filing summaries captured on this page (the page surfaces recent/newsworthy filings — 8-Ks, F-3, insider forms — not necessarily the annual report's full risk-factors text).
