# Dow Jones & Company, Inc. and NYP Holdings, Inc. v. Perplexity AI, Inc. — docket and complaint

```yaml
source:          CourtListener / RECAP, S.D.N.Y. PACER docket 1:24-cv-07984
url_or_doc_id:   https://www.courtlistener.com/docket/69280523/dow-jones-company-inc-v-perplexity-ai-inc/ ; complaint PDF https://storage.courtlistener.com/recap/gov.uscourts.nysd.630270/gov.uscourts.nysd.630270.1.0.pdf
published:       2024-10-21 (complaint filed)
pull_date:       2026-09-22
pull_method:     browser extension (courtlistener.com docket search and page, 403 to plain fetch); complaint PDF retrieved by direct fetch of storage.courtlistener.com (200, not gated) and converted with pdftotext
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed court complaint (trust-rubric.md "Filed — S-1, 10-K, court exhibit, funding filing")
source_label:    filed
lane:            B
sub_market:      organic recommendation
engine:          Perplexity AI (priority-2 engine); complaint also names OpenAI as a licensing counterexample (n/a model version — no LLM version named in this filing)
metric_kind:     traffic
supersedes:      none
captured:        section "Nature of the Action" (paragraphs 1-19), section "Parties" and "Jurisdiction and Venue" (paragraphs 16-27), section "Factual Background" including "Harm from Perplexity's Illegal Conduct" (paragraphs 28-110, numeric paragraphs only), Count headers (paragraphs 111-137, headers plus registration references only) — full 42-page complaint downloaded, paragraphs bearing a number on traffic, referral, revenue, ad spend, or licence fee transcribed verbatim below; paragraphs without a number are not transcribed
```

## Case caption

UNITED STATES DISTRICT COURT
SOUTHERN DISTRICT OF NEW YORK

DOW JONES & COMPANY, INC. and NYP HOLDINGS, INC., Plaintiffs, v. PERPLEXITY AI, INC., Defendant.

Civil Action No. 24-cv-7984 — COMPLAINT — JURY TRIAL DEMANDED

- **Court:** U.S. District Court, Southern District of New York
- **Docket number:** 1:24-cv-07984
- **Filed:** October 21, 2024
- **Assigned to:** Judge Katherine Polk Failla
- **Parties:** Plaintiffs Dow Jones & Company, Inc. ("Dow Jones") and NYP Holdings, Inc. ("NYP Holdings"), both News Corporation subsidiaries; Defendant Perplexity AI, Inc. ("Perplexity")
- **Cause:** 17:101 Copyright Infringement; Nature of Suit: 820 Copyright; Jury Demand: Plaintiff
- **Status shown on docket (as of pull):** Last Updated Sept. 16, 2026, 9:59 a.m.; Date of Last Known Filing Sept. 15, 2026. No termination date shown on the docket header — active.
- **Sealed items:** none observed on the docket's first entry page or in this pull. If any exist further in the docket's later pages, they were not reached by this pull; recorded as `unknown — checked docket page 1 of 2, 2026-09-22`, not as absent.

## Claims / counts as captioned

- COUNT ONE — Copyright Infringement (17 U.S.C. § 106) — Perplexity's Copying of Plaintiffs' Copyrighted Work to Create "Inputs" for Its RAG Index (¶¶111-120)
- COUNT TWO — Copyright Infringement (17 U.S.C. § 106) — Perplexity's Copying of Plaintiffs' Protected Work to Generate "Outputs" to User Queries (¶¶121-133)
- COUNT THREE — False Designation of Origin and Dilution of Plaintiffs' Trademarks (15 U.S.C. § 1125) (¶¶134-...)

## Verbatim — numbered paragraphs stating a number on traffic, referral, revenue, ad spend, or licence fee

> **¶25.** "Perplexity aggressively promotes and advertises its products and services in this State and District, including through its dynamic, heavily interactive website (https://www.perplexity.ai and associated subpages) and mobile applications. Perplexity's website targets customers in this State and District with promotional material tailored to a New York audience, including a web page inviting visitors to "Discover New York with Perplexity." Perplexity's marketing activities include promoting on its Instagram account a massive billboard in Times Square from September 2024 which read "Congratulations Perplexity on 250 million questions answered last month.""

> **¶14.** "Other AI companies have engaged with Plaintiffs and other publishers, resulting in legitimate market-based licensing solutions. Indeed, as Forbes has recently observed, "AI content licensing initiatives abound." For example, News Corp recently partnered with OpenAI to license its content for certain uses in OpenAI's applications. OpenAI users will have the benefit of accessing Plaintiffs' content, whether quoted or summarized by OpenAI. This cooperative relationship will allow OpenAI and Plaintiffs to experiment with new product experiences and revenue models."

> **¶69.** "Upon information and belief, Perplexity's citations make users less inclined to visit the original content source, because, as Perplexity has boasted, citations make content appear more "Reliable," allowing Perplexity's readers to feel more confident that they can "Skip the Links" when they believe they are reading content from credible sources."

> **¶70.** "This observation is corroborated by Plaintiffs' experience of detecting virtually no click-through traffic on their websites from "cited sources" links on Perplexity, despite Perplexity receiving approximately 250 million queries per month."

> **¶73.** "According to Perplexity, the Publishers' Program was developed "[t]o further support the vital work of media organizations and online creators," because the company "need[s] to ensure publishers can thrive as Perplexity grows." The program purports to share an unspecified portion of ad revenue from advertisements that Perplexity plans to host in "coming months.""

> **¶104.** "The substantial fundraising Perplexity has accomplished, totaling in excess of $150 million, and Perplexity's current market valuation, which purports to be in excess of $3 billion, is indicative of the potentially massive illegal transfer of revenue from news publishers to Perplexity, purposefully accomplished by Perplexity."

Footnote 29 (cited at ¶73 context, sourced page): "Charlotte Tobitt, *Perplexity to share ad revenue with signed-up publishers after flurry of criticism*, PRESS GAZETTE (July 30, 2024), https://pressgazette.co.uk/news/perplexity-publishers-revenue-sharing."

## Pull notes — mechanical only

- Docket located via CourtListener case-name search (`case_name=Dow+Jones+v.+Perplexity`, 1 result) and confirmed against the docket ID already surfaced by the Pass 1 red-team (`query-book-redteam.md` §5 B8: `courtlistener.com/docket/69280523/dow-jones-company-inc-v-perplexity-ai-inc/`).
- `www.courtlistener.com` returned 403 to plain fetch/curl, matching `channels.md` C62; reached via the Chrome browser extension (`tabs_context_mcp` then a dedicated new tab, tabId 1697683928). `storage.courtlistener.com`, which hosts the actual RECAP PDFs, returned HTTP 200 to a direct `curl` fetch — no extension needed for the PDF itself.
- Complaint PDF (`gov.uscourts.nysd.630270.1.0.pdf`, 42 pages, 6.3MB) downloaded and converted to text with `pdftotext -layout` for verbatim paragraph extraction; the source PDF is a text-layer PDF (not scanned), so extraction is direct, not OCR.
- Five appendices are attached to the complaint (WSJ copyright registration numbers, NYP copyright registration numbers, NYP June 2024 article, WSJ July 2024 article, NYP August 2024 article) — these are evidentiary exhibits (copyright registrations, reproduced articles) and were not found to carry additional traffic/revenue/referral numbers beyond what is quoted above; not separately transcribed.
- Docket entries beyond the initial complaint and its attachments (motions, orders, etc.) were not individually pulled in this session; the docket's "Last Updated" and "Date of Last Known Filing" fields were read from the docket header only.
