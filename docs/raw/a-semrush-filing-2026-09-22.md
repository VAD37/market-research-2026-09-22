# Semrush Holdings, Inc. — SEC filings: AI Visibility Toolkit revenue disclosure, and resolution of the "Semrush — By Adobe" G2 attribution

```yaml
source:          Semrush Holdings, Inc. (SEC filer, ticker SEMR, CIK 0001831840)
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1831840/000162828026013259/semr-20251231.htm (Form 10-K, fiscal year ended 2025-12-31, filed 2026-03-02); https://www.sec.gov/Archives/edgar/data/1831840/000162828026003416/semr-20260126.htm (Form 8-K, filed 2026-01-26, Item 8.01)
published:       2026-03-02 (10-K); 2026-01-26 (8-K)
pull_date:       2026-09-22
pull_method:     fetch (curl, direct sec.gov URL from an SEC EDGAR full-text search API hit at efts.sec.gov/LATEST/search-index?q=%22Adobe%22%20%22Semrush%22 and a second query for %22AI+Visibility%22 filtered to CIK 0001831840)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed. SEC Form 10-K and Form 8-K, both filed by the registrant itself
source_label:    filed
lane:            A
sub_market:      organic recommendation
engine:          large language models generically ("ChatGPT, Gemini, and Perplexity" named once, as example AI platforms in the Starter-plan description)
metric_kind:     sales (ARR figures)
supersedes:      none
captured:        section "Recent Developments" and the company-history bullet list plus adjacent business-description paragraphs (10-K); Item 8.01 in full (8-K) — both filings are large (10-K: 6,105 extracted lines); only the load-bearing passages are reproduced verbatim below, with page/section pointers
```

## Verbatim

### Resolution of the "Semrush — By Adobe" G2 attribution

**Confirmed: Semrush Holdings, Inc. is a wholly owned subsidiary of Adobe Inc. as of 2026-04-28.** Three independent-in-kind sources, none of them G2, corroborate this, found in this pull:

**(1) Form 8-K, filed 2026-01-26, Item 8.01 — verbatim:** "On December 29, 2025, Semrush Holdings, Inc., a Delaware corporation (the 'Company' or 'Semrush'), filed its definitive proxy statement on Schedule 14A... with respect to the special meeting of Semrush's stockholders... to be held in connection with the transactions contemplated by that certain Agreement and Plan of Merger (the 'Merger Agreement'), dated as of November 18, 2025, by and among the Company, **Adobe Inc., a Delaware corporation ('Adobe')**, and Fenway Merger Sub, Inc., a Delaware corporation and a direct, wholly owned subsidiary of Adobe ('Merger Sub'), pursuant to which Merger Sub will merge with and into the Company (the 'Merger'), **with the Company surviving as a wholly owned subsidiary of Adobe.**" Merger consideration: "each share of Class A common stock and each share of Class B common stock... will be converted into the right to receive **$12.00 in cash**, without interest." Termination fee: "$63,000,000 in cash." Special Meeting held 2026-02-03 (stockholder approval obtained same date, per the 10-K).

**(2) Form 10-K, filed 2026-03-02 (fiscal year 2025), "Recent Developments" section — verbatim:** "On November 18, 2025, we entered into the Merger Agreement, pursuant to which, and upon the terms and subject to the conditions therein, Merger Sub will merge with and into the Company, with the Company surviving the Merger as a wholly owned subsidiary of Adobe." Closing conditions listed include "the Company Stockholder Approval, which was obtained on February 3, 2026" and "the expiration of the waiting period applicable to the Merger under the Hart-Scott-Rodino Antitrust Improvements Act of 1976... (which has occurred)." Outside date for closing: "August 18, 2026, subject to an extension to November 18, 2026, in order to obtain required regulatory approvals."

**(3) Semrush's own newsroom, republishing an Adobe press release dated 2026-04-28 (company-stated, captured in full in `a-semrush-launch-2026-09-22.md`):** "Adobe (Nasdaq:ADBE)... today announced the completion of its acquisition of Semrush Holdings, Inc." The merger closed on this date, before the 10-K's own filing date of 2026-03-02 — note the closing (2026-04-28) postdates the 10-K's own filing (2026-03-02) and the Special Meeting approval (2026-02-03), consistent with the 10-K describing the transaction as pending ("Recent Developments") rather than completed at the time it was filed.

**G2's "Semrush — By Adobe" attribution (seen on both the AEO and AI-Search-Visibility category pages, per `docs/raw/a-vendor-roster-2026-09-22.md`) is therefore correct and independently confirmed**, not merely a G2 labeling artifact. Resolved via `efts.sec.gov` full-text search plus semrush.com/news — not via G2 itself and not via WebSearch (session WebSearch budget was exhausted before this cluster began; SEC EDGAR full-text search and direct sec.gov/semrush.com fetches were used instead, per the task's stated preference for direct fetch of company domains and sec.gov).

### AI Visibility Toolkit — filed revenue and product disclosure (10-K, page ~57 per the filing's own pagination)

Company-history bullet list, verbatim, final two entries: "2024: Surpassed $400 million in ARR and launched the general availability of the Enterprise SEO solution." "**2025: Surpassed $460 million in ARR and launched an expanded suite of generative AI products including the AI Visibility Toolkit and Enterprise AIO. Enterprise platform ARR grew to $37 million. AI products surpassed $38 million in ARR. Entered into a Merger Agreement with Adobe.**"

Elsewhere in the 10-K's business description: "The release of new products, tools, add-ons, and features, including our Enterprise AIO, Enterprise Site Intelligence, and AI toolkit, has enabled us to drive higher monetization over time as we have increased our ARR per paying customer to **$4,369 as of December 31, 2025** from **$3,522 as of December 31, 2024**."

"Our Starter subscription is designed for users beginning their SEO and AI visibility journeys, providing essential search tools and integrated tracking for brand performance across search engines and AI platforms, **such as ChatGPT, Gemini, and Perplexity**."

"While we launched the general availability of our Enterprise SEO solution in June 2024, we significantly expanded the portfolio in 2025 with the introduction of specialized products including Enterprise AIO and Enterprise Site Intelligence... Customers can supplement these tiers with **Enterprise AIO for granular brand analysis across large language models** and Enterprise Site Intelligence for technical site health."

"We have recently expanded our offerings to include Site Intelligence, a site health and monitoring solution... an official app in ChatGPT, and Enterprise AIO, a Semrush Enterprise solution that provides businesses with the tools to track, control, and optimize brand presence across AI-powered search platforms, and AI [text continues beyond the extracted passage]."

## Pull notes — mechanical only

- Both filings fetched via direct `curl` to their `sec.gov/Archives/edgar/data/...` URLs (found via two `efts.sec.gov/LATEST/search-index` full-text queries, not via the SEC EDGAR HTML search UI, which is `403→ext` per `channels.md` C13); both returned HTTP 200.
- The 10-K is a very large XBRL-tagged HTML document (2.2 MB, 6,105 lines after text extraction); this file reproduces only the passages naming "AI Visibility," "Adobe," or the Merger, located by keyword search within the extracted text, plus their immediate surrounding sentences for context. The full document is not reproduced.
- The 10-K's own "Recent Developments" section describes the Merger as pending (not yet closed) as of its 2026-03-02 filing date — the merger's actual close (2026-04-28) is documented only in the separately-pulled newsroom/press-release source (`a-semrush-launch-2026-09-22.md`), not in this 10-K itself, since the 10-K predates the closing.
- **No exact month/day launch date for the "AI Visibility Toolkit" specifically is given anywhere in the 10-K** — only the year "2025" in the company-history bullet. `unknown — checked semr-20251231.htm (this filing, full-text keyword search on "AI Visibility") 2026-09-22`.
- An earlier 8-K exhibit (EX-99.1, filed 2025-11-05, Q3 2025 earnings release) also matched the "AI Visibility" full-text search but was not separately opened this pull, since the 10-K supersedes it with the full-year figures; noted for completeness — `docs/raw` path not created for that exhibit this cluster.
