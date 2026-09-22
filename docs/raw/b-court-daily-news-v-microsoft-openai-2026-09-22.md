# Daily News, LP; Chicago Tribune Company, LLC; Orlando Sentinel Communications Company, LLC; Sun-Sentinel Company, LLC; San Jose Mercury-News, LLC; DP Media Network, LLC; ORB Publishing, LLC; Northwest Publications, LLC v. Microsoft Corporation, OpenAI, Inc. et al. — docket and complaint

```yaml
source:          CourtListener / RECAP, S.D.N.Y. PACER docket 1:24-cv-03285
url_or_doc_id:   https://www.courtlistener.com/docket/68484432/daily-news-lp-v-microsoft-corporation/ ; complaint PDF https://storage.courtlistener.com/recap/gov.uscourts.nysd.620514/gov.uscourts.nysd.620514.1.0.pdf
published:       2024-04-30 (complaint filed)
pull_date:       2026-09-22
pull_method:     browser extension (courtlistener.com docket search and page, 403 to plain fetch); complaint PDF retrieved by direct fetch of storage.courtlistener.com (200, not gated) and converted with pdftotext
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed court complaint
source_label:    filed
lane:            B
sub_market:      organic recommendation
engine:          Microsoft (Bing Chat / Copilot) and OpenAI (ChatGPT), both co-defendants; GPT-2, GPT-3, GPT-3.5, GPT-4 named as model versions in the complaint's own text
metric_kind:     traffic
supersedes:      none
captured:        "Nature of the Action" opening paragraphs (1, 7), "OpenAI's Business" (paragraphs 58-61), "Training on the Publishers' Content" — C4/Common Crawl token counts (paragraph 86), "Misappropriation" section (paragraph 116) — 98-page complaint; only numbered paragraphs stating a number on traffic, referral, revenue, ad spend, or licence fee are transcribed below
```

## Case caption

UNITED STATES DISTRICT COURT
SOUTHERN DISTRICT OF NEW YORK

DAILY NEWS, LP; CHICAGO TRIBUNE COMPANY, LLC; ORLANDO SENTINEL COMMUNICATIONS COMPANY, LLC; SUN-SENTINEL COMPANY, LLC; SAN JOSE MERCURY-NEWS, LLC; DP MEDIA NETWORK, LLC; ORB PUBLISHING, LLC; and NORTHWEST PUBLICATIONS, LLC, Plaintiffs, v. MICROSOFT CORPORATION, OPENAI, INC., OPENAI LP, OPENAI GP, LLC, OPENAI, LLC, OPENAI OPCO, LLC, OPENAI GLOBAL, LLC, OAI CORPORATION, LLC, and OPENAI HOLDINGS, LLC, Defendants.

Civil Action No. 24-3285 — COMPLAINT — JURY TRIAL DEMANDED

- **Court:** U.S. District Court, Southern District of New York
- **Docket number:** 1:24-cv-03285
- **Filed:** April 30, 2024
- **Assigned to:** Judge Sidney H. Stein; referred to Magistrate Judge Ona T. Wang
- **Parties:** Eight Plaintiff newspaper-publishing entities — Daily News LP (New York Daily News), Chicago Tribune Company LLC, Orlando Sentinel Communications Company LLC, Sun-Sentinel Company LLC, San Jose Mercury-News LLC, DP Media Network LLC (Denver Post), ORB Publishing LLC (Orange County Register), Northwest Publications LLC (St. Paul Pioneer Press) — all Alden Global Capital-affiliated titles; Defendants Microsoft Corporation and the OpenAI corporate family
- **Cause:** 17:501 Copyright Infringement; Nature of Suit: 820 Copyright; Jury Demand: Both
- **Status shown on docket (as of pull):** most recent docket activity found in this pull dated October 15, 2025 and January 5, 2026 (discovery letter-motions), filed under the coordinated MDL docket number 1:25-md-03143 as well as this member-case number 1:24-cv-03285 — active, no termination shown.
- **MDL relation:** a member case of `In Re: OpenAI, Inc. Copyright Infringement Litigation`, 1:25-md-03143 (S.D.N.Y.) — discovery motions filed in this pull's search results carry both case captions. See companion raw file `b-court-mdl-openai-copyright-2026-09-22.md`.
- **Sealed items:** none observed in the docket entries reached (search-result excerpts and the document-1 complaint page). Full docket page range not enumerated in this pull; recorded `unknown — checked case-name search result and document-1 page, 2026-09-22` for any sealed entry elsewhere on the docket, not as absent.

## Claims / counts as captioned

- COUNT I — Copyright Infringement (17 U.S.C. § 501)
- COUNT II — Vicarious Copyright Infringement
- COUNT III — Contributory Copyright Infringement
- COUNT IV — Contributory Copyright Infringement
- COUNT V — Digital Millennium Copyright Act — Removal of Copyright Management Information
- COUNT VI — Common Law Unfair Competition By Misappropriation
- COUNT VII — Trademark Dilution (15 U.S.C. § 1125(c))
- COUNT VIII — Dilution and Injury to Business Reputation (N.Y. Gen. Bus. Law § 360-l)

## Verbatim — numbered paragraphs stating a number on traffic, referral, revenue, ad spend, or licence fee

> **¶58.** "OpenAI became a household name upon the release of ChatGPT in November 2022. ChatGPT is a text-generating chatbot that, given user-generated prompts, can mimic humanlike natural language responses. ChatGPT was an instant viral sensation, reaching one million users within a month of its release and gaining over 100 million users within three months."

> **¶60.** "These commercial offerings have been immensely valuable for OpenAI. Over 80% of Fortune 500 companies are using ChatGPT. According to recent reports, in December 2023 OpenAI achieved $2 billion in revenue and expects to double this figure to $4 billion in revenue in 2025."

> **¶86.** "Collectively, content from the Publishers' websites accounts for at least 124 million tokens in the C4 dataset, broken down as follows: 48M tokens from the Chicago Tribune; 22M tokens from the New York Daily News; 12M tokens from the Mercury News; 11M tokens from the Orlando Sentinel; 11M tokens from the Sun Sentinel; 9.8M tokens from the Denver Post; 6.5M tokens from the Orange County Register; and 3.2M tokens from the Pioneer Press."

> **¶116.** "In this way, synthetic search results divert important traffic away from copyright holders like the Publishers. A user who has already read the latest news, even—or especially—with attribution to the Publishers, has less reason to visit the original source."

> (Un-numbered background, opening "Nature of the Action") "...OpenAI purported at one time to be a non-profit organization, its recent $90 billion valuation... [Microsoft's] Bing Chat... has also added hundreds of billions of dollars to Microsoft's market value." / "The Publishers have spent billions of dollars sending real people to real places to gather the news." / "Microsoft has invested at least $13 billion in [OpenAI]." / "$495 million capital raise for OpenAI" (entity-formation paragraph, OpenAI Global LLC's corporate history).

## Pull notes — mechanical only

- Docket located via CourtListener case-name search (`case_name=Daily+News+v.+Microsoft`), 2 results; the S.D.N.Y. district docket (docket ID 68484432) was pulled — a second docket ID (69470429) appeared in the same search, likely a related transfer/MDL-tagged record, not independently opened in this pull.
- `www.courtlistener.com` 403 to plain fetch, reached via Chrome extension. `storage.courtlistener.com` PDF fetched directly by curl, HTTP 200.
- Complaint PDF (`gov.uscourts.nysd.620514.1.0.pdf`, 98 pages) converted to text with `pdftotext -layout`; text-layer PDF, not scanned.
- This complaint is textually parallel to `b-court-nyt-v-microsoft-openai-2026-09-22.md` (same law firm, near-identical structure and count list) but names different plaintiffs, different per-publisher token counts, and a different (December 2023) OpenAI revenue figure ($2B, doubling to $4B by 2025) than the New York Times complaint's ($80M/month, $1B pace) — the two are not reconciled here; both are filed statements from different complaints on different dates and are cited side by side across the two raw files, never averaged.
- Two later docket entries surfaced in the search result (Document #478, October 15 2025; Document #561 attachments, January 5 2026) show this case is active in discovery as of early 2026 and is being litigated jointly with the MDL; their own text (interrogatory correspondence) was read only as much as the search snippet shows and was not independently pulled as a full PDF, since it carries no new traffic/revenue/referral number distinct from the original complaint.
