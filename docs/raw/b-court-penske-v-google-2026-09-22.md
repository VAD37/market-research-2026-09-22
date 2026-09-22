# Penske Media Corporation, et al. v. Google LLC and Alphabet Inc. — docket, complaint and amended complaint

```yaml
source:          CourtListener / RECAP, D.D.C. PACER docket 1:25-cv-03192
url_or_doc_id:   https://www.courtlistener.com/docket/71332589/penske-media-corporation-v-google-llc/ ; original complaint PDF https://storage.courtlistener.com/recap/gov.uscourts.dcd.284823/gov.uscourts.dcd.284823.1.0.pdf ; amended complaint (operative pleading) PDF https://storage.courtlistener.com/recap/gov.uscourts.dcd.284823/gov.uscourts.dcd.284823.17.0.pdf
published:       2025-09-12 (original complaint filed); 2025-12-04 (amended complaint filed, operative pleading as of 2025-12-05 minute order)
pull_date:       2026-09-22
pull_method:     direct curl fetch of www.courtlistener.com (200 with a browser user-agent string; no Chrome-extension session available this session — extension reported "not connected" and a Playwright-driven browser_navigate to the same docket URL returned an AWS CloudFront/WAF challenge page — plain curl with a standard desktop Chrome user-agent succeeded on the first several requests of this session before subsequent requests to www.courtlistener.com began returning HTTP 202 challenge pages, worked around by spacing requests); both complaint PDFs retrieved by direct fetch of storage.courtlistener.com (200, not gated) and converted with pdftotext -layout
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed court complaint (both the original and the amended/operative complaint)
source_label:    filed
lane:            B
sub_market:      organic recommendation
engine:          Google (AI Overviews, AI Mode, Search Generative Experience, Bard, Gemini) — priority-1 engine; complaint also references OpenAI (ChatGPT) and Microsoft licensing deals as comparators, and Perplexity by name (footnote citing a NYT article on Perplexity)
metric_kind:     traffic
supersedes:      none
captured:        Both pleadings captured. Original complaint (Doc #1, 101 pages): "Nature of the Action" ¶¶1-15, PMC property traffic figures ¶¶37-54, Google revenue/market-share ¶¶81-84, CTR/zero-click stats ¶¶104-110, AI Overviews rollout and PMC-specific traffic/revenue decline ¶¶156-206, licensing/unjust-enrichment ¶¶217-219, 239-243, Prayer for Relief. Amended complaint (Doc #17, filed 2025-12-04, 108 pages, now the operative pleading per the court's 2025-12-05 minute order): same sections renumbered plus a new COUNT V (Sherman Act §2 tying, AI Overviews tied to general search) at ¶¶293-306 — only numbered paragraphs stating a number on traffic, referral, revenue, ad spend, or licence fee are transcribed below, drawn from the amended complaint's own numbering with the original complaint's equivalent paragraphs cited alongside where they differ
```

## Case caption (amended complaint, operative pleading)

UNITED STATES DISTRICT COURT
FOR THE DISTRICT OF COLUMBIA

PENSKE MEDIA CORPORATION, BILLBOARD MEDIA, LLC, DEADLINE HOLLYWOOD, LLC, FAIRCHILD PUBLISHING, LLC, GOLD DERBY MEDIA, LLC, THE HOLLYWOOD REPORTER, LLC, INDIEWIRE MEDIA, LLC, ROLLING STONE LLC, SHEMEDIA, LLC, and VARIETY MEDIA, LLC, Plaintiffs, v. GOOGLE LLC and ALPHABET INC., Defendants.

Civil Action No. 1:25-cv-03192-APM — AMENDED COMPLAINT — JURY TRIAL DEMANDED

- **Court:** U.S. District Court, District of Columbia (D.D.C.)
- **Docket number:** 1:25-cv-03192
- **Filed:** September 12, 2025 (original complaint); amended complaint filed December 4, 2025
- **Assigned to:** Judge Amit Priyavadan Mehta (the same judge who presided over *United States v. Google*, the DOJ general-search-monopoly case cited throughout this complaint)
- **Parties — original complaint (Doc #1):** 15 Plaintiffs — Penske Media Corporation ("PMC"), Artforum Media LLC, Art Media LLC, Billboard Media LLC, Deadline Hollywood LLC, Fairchild Publishing LLC, Gold Derby Media LLC, The Hollywood Reporter LLC, Indiewire Media LLC, Rolling Stone LLC, SheMedia LLC, Sourcing Journal Media LLC, Sportico Media LLC, Variety Media LLC, Vibe Media Publishing LLC; Defendants Google LLC and Alphabet Inc.
- **Parties — amended complaint (Doc #17, operative):** 10 Plaintiffs — the same list minus Artforum Media LLC, Art Media LLC, Sourcing Journal Media LLC, Sportico Media LLC, and Vibe Media Publishing LLC (5 dropped between the original and amended filing; no docket entry found in this pull explaining the drop). Defendants unchanged.
- **Cause:** 15:1 Antitrust Litigation; Nature of Suit: 410 Anti-Trust; Jury Demand: Plaintiff; Jurisdiction: Federal Question
- **Status shown on docket (as of pull):** Last Updated Sept. 2, 2026, 3:28 p.m.; Date of Last Known Filing Sept. 2, 2026. Procedural history: original Motion to Dismiss (Doc #16, filed 2025-11-06) denied as moot after PMC filed the Amended Complaint (Doc #17, 2025-12-04) — minute order of 2025-12-05 states "The 17 Amended Complaint shall now be the operative pleading in this matter." Google then moved to dismiss the amended complaint (Doc #25, filed 2026-01-12); PMC opposed (Doc #26, filed 2026-02-12). A joint motion to consolidate oral argument with the related case *Chegg, Inc. v. Google LLC*, No. 1:25-cv-00543 (also before Judge Mehta, and separately pulled in this cluster — `b-court-chegg-v-google-2026-09-22.md`) was granted 2026-07-29: "The parties shall appear for a consolidated hearing on the pending motions to dismiss in this case and in Chegg, Inc. v. Google LLC, No. 25-cv-543, on August 25, 2026, at 2:00 p.m. in Courtroom 10." No termination date shown — active, motions to dismiss pending as of pull date.
- **Sealed items:** none observed among the docket entries reached in this pull (complaint, amended complaint, all motion/order entries through the 2026-07-29 consolidation order). Not every docket-entry page was individually opened; recorded `unknown — checked docket entry list (unpaginated single view) and document-1/document-17 pages, 2026-09-22` for any sealed entry not captured in the extracted entry list.

## Claims / counts as captioned (amended complaint)

- COUNT I — Reciprocal Dealing in Violation of Section 1 of the Sherman Act
- COUNT II — Reciprocal Dealing in Violation of Section 2 of the Sherman Act
- COUNT III — Unlawful Monopoly Leveraging in Violation of Section 2 of the Sherman Act
- COUNT IV — Unlawful Monopolization in Violation of Section 2 of the Sherman Act
- COUNT V — Unlawful Tying of AI Overviews to General Search Services in Violation of Section 2 of the Sherman Act (**new in the amended complaint; not present in the original**)
- COUNT VI — Unlawful Attempted Monopolization in Violation of Section 2 of the Sherman Act
- COUNT VII — Common Law Unjust Enrichment

(Original complaint carried six counts in this same order, without the tying count, as Counts I–VI.)

## Verbatim — numbered paragraphs stating a number on traffic, referral, revenue, ad spend, or licence fee

> **¶1** (Nature of the Action): "This action challenges Google's abuse of its adjudicated monopoly in General Search Services to coerce online publishers like PMC to supply content that Google republishes without permission in AI-generated answers that unfairly compete for the attention of users on the Internet in violation of the antitrust laws of the United States."

> **¶2**: "PMC depends on referrals from Google's monopoly search engine for a large portion of the revenue that it devotes to producing original online content through over 25 print and digital properties that include such iconic brands as Billboard, Deadline, Rolling Stone, Variety, and VIBE... PMC's award-winning content attracts a passionate monthly audience of more than 120 million visitors in the United States alone and nearly double that globally."

> **¶3** (original ¶3; amended complaint's equivalent paragraph carries the same figures): "Much of PMC's digital content--including a remarkable 6.7 million URLs that have been indexed by Google--is free to consumers. A significant portion of PMC's revenue relies on traffic to its websites which allows PMC to earn revenue from digital advertising, affiliate links and subscriptions to its publications."

> **PMC property traffic figures** (amended complaint, renumbered from the original's ¶¶40-54; figures unchanged between the two filings): "Rolling Stone generates an average of 87 million page views per month." "Billboard generates 55 million monthly pageviews on average across its offerings." "Variety.com receives 24 million monthly average visitors and an average of over 78 million monthly pageviews." "The website Hollywoodreporter.com receives more than 14.5 million average unique monthly views." "With over 49 million monthly page views, Deadline is the authoritative source for breaking entertainment industry news." "wwd.com, receives 8.9 million unique monthly visitors."

> **¶73** (Google's search monopoly; original complaint's ¶81 states the identical figure): "Google's search engine business generates annual revenue of nearly $200 billion and, by any metric, it possesses monopoly power in the search engine market." Citing Alphabet's 2024 Form 10-K.

> **¶ (revenue-share figure, same section)**: "[I]n 2021, Google paid out a total of $26.3 billion in revenue share under these contracts [with Apple, Mozilla, Android OEMs and wireless carriers] ... almost four times more than all other search-related costs combined," quoting the D.C. District Court's finding in *United States v. Google*.

> **¶ (market-share figure, quoting the same court)**: "Plaintiffs easily have demonstrated that Google possesses a dominant market share. Measured by query volume, Google enjoys an 89.2% share of the market for general search services, which increases to 94.9% on mobile devices. This overwhelms Bing's share of 5.5% on all queries and 1.3% on mobile, as well as Yahoo's and DDG's shares, which are under 3% regardless of device type."

> **¶ (CTR decline, citing a 2019 SparkToro post)**: "[B]y 2019, data indicated that less than 50% of Google searches resulted in a click-through to the original source, making Google more of a walled garden than a traffic director."

> **¶ (zero-click, citing Rand Fishkin / Datos clickstream data)**: "A study by Rand Fishkin, based on clickstream data from Datos, found that nearly 60% of visits to Google SERPs result in no clicks."

> **¶174 / original ¶174** (Semrush study, informational-query share): "content marketing platform Semrush found that nearly 90% of the queries that trigger an AI Overview are informational. The D.C. District Court similarly found in the Government Search Case that 80% of Google's queries are noncommercial in nature."

> **¶194** (Google "coverage" of PMC topics): "From late 2024 through early 2025, the percentage of searches that both returned links to PMC websites in Google's organic search results and generated AI Overviews dramatically increased to approximately 20%, and that number is likely to increase further as Google expands its GAI search offerings."

> **¶195** (PMC's own affiliate-revenue decline — company-stated inside a filed complaint): "Compared to PMC's peak, organic affiliate revenues across the portfolio have declined by more than a third by the end of 2024. This was a result of decreased referrals from Google Search."

> **¶196** (zero-click rate by publisher, citing Similarweb): "Internet security company Cloudflare, which is used by roughly 20% of all websites on the Internet, has reported that in its 'dataset of news-related customers (spanning the Americas, Europe, and Asia), Google's referrals have been clearly declining since February 2025.' Another study from April 2025 shows that Google's AI Overviews reduce click-through rates for publishers by as much as 34.5% for the top organic search result. Bain and Company concluded in February 2025 that 60% of searches terminate without the user clicking through to another website. According to the digital intelligence platform Similarweb, among searches with AI Overviews, the average zero-click rate is 83%." [This 83% Similarweb figure and the Cloudflare "20% of all websites" figure are new in the amended complaint; not present in the original complaint's equivalent ¶199.]

> **¶200-201** (executive statements — company-stated, quoted inside a filed complaint; new in the amended complaint, not present in the original): a Gannett/USA Today executive: Google's "insinuation ... that AI Overview is not getting in the way of the ten blue links and the traffic going back to creators and publishers is just 100% false. ... All of the information is out there about how reduced the flow of people is back to sites. I mean, they are reading the overview and stopping there. ... We see it." Vox Media CEO Jim Bankoff: "Google said recently ... 'we are sending a more qualified audience than ever to publishers.' And that's just simply not true. ... [W]e have Google Analytics that shows us that the traffic is less engaged, spending less time on the site, and of course there's a lot less of it."

> **¶202** (original ¶202, unchanged figure): "many publisher websites are experiencing click-through traffic losses in the 10-25% range year-over-year since the introduction of AI Overviews," citing Digiday, Aug. 15, 2025 ("Google AI Overviews linked to 25% drop in publisher traffic").

> **¶203** (new Pew Research figure in the amended complaint, not in the original): "users who encountered an AI Overview clicked on a traditional search result link in just 8% of all visits. By comparison, Pew's data showed that users who receive a traditional search result page without an AI Overview click through nearly twice as often."

> **¶204** (new in the amended complaint): "The Pew Research Center study also showed that AI Overviews appear in 60% of search queries that began with question words such as 'who,' 'what,' 'when' or 'why,' and 36% of searches that include both a noun and a verb."

> **¶302** (new COUNT V tying claim, amended complaint only): "Google's anticompetitive conduct affects a substantial volume of commerce, because PMC and other online publishers depend heavily on traffic from Google's general search. As a result of Google's conduct, nearly 60% of Google searches are now zero-click. Among searches that result in AI Overviews, over 80% are now zero-click."

> **¶ (licensing comparators, unjust enrichment section, ¶250 amended / ¶239 original, same figures in both)**: "OpenAI has entered into commercial agreements with at least several content owners, including an agreement with Axel Springer ballparked at 'tens of millions' of dollars, as well as an agreement with the Associated Press... OpenAI CEO Sam Altman stated publicly that OpenAI wanted to pay the New York Times 'a lot of money to display their content.'"

> **¶ (stock-price reaction to AI announcements, ¶251 amended / ¶240 original, same figures in both)**: "Google announced the launch of Bard on February 6, 2023. The very next day, the share price of its parent, Alphabet Inc., increased by approximately 4.6%. ... after Google announced a revamped AI-powered search engine on May 10, 2023, Alphabet's share price surged even further, rising 8.6% in the two days following that announcement. Google's stock price closed 5% higher after its Gemini announcement." Citing also, in a footnote, "Google Co-Founders Gain $18 Billion as AI Boost Lifts Stock" (Bloomberg, May 12, 2023).

> **¶ (PMC's own content cost, ¶254 amended / ¶243 original, same figures in both)**: "PMC content represents the work of hundreds of PMC employees and other contributors, the employment of and contracting with whom costs PMC tens of millions of dollars per year. ... By outright taking that extraordinary volume of content, Google has avoided the enormous costs PMC expended to create or acquire that content, ranging into the hundreds of millions of dollars, and created billions more in enterprise value for Google at PMC's expense."

> **¶ (AI content-licensing market size estimate, original complaint ¶217, retained in substance in the amended complaint's equivalent unjust-enrichment section)**: "analysts have estimated that the value of the overarching AI content market could grow close to $30 billion by 2034," citing Reuters, "Inside Big Tech's underground race to buy AI training data."

> **Prayer for Relief** (identical in both filings, no specific dollar figure demanded): "Awarding PMC compensatory damages, restitution, disgorgement, and any other relief that may be permitted by law or equity... Awarding PMC costs, expenses, and attorneys' fees as permitted by law." The new Count V (tying) prayer within the count itself, ¶304, adds: "PMC is entitled to receive treble damages for its injuries" — no dollar amount specified.

## Pull notes — mechanical only

- This is the docket the previous agent's session-ending note flagged ("same case number 1:25-cv-03192 — download the complaint") without identifying the case name. Identified in this session via a CourtListener case-search (`?q="1:25-cv-03192"&type=r`, plain curl with a desktop-Chrome user-agent string, HTTP 200) as *Penske Media Corporation, et al. v. Google LLC and Alphabet Inc.*, docket ID 71332589 — distinct from all seven previously-pulled dockets in this cluster and from the same-court, same-judge, consolidated-hearing companion case *Chegg, Inc. v. Google LLC*, No. 1:25-cv-00543, already pulled.
- Access path deviated from the task's stated default: `courtlistener.com` returned HTTP 200 to a plain `curl` request bearing a standard desktop Chrome user-agent string for the first several requests this session (docket page, both complaint PDFs via `storage.courtlistener.com`), contrary to the channel's `403→ext` expectation recorded in `channels.md` C62 and `query-book-redteam.md`. Later in the same session, further `www.courtlistener.com` search and docket-detail requests (attempting to identify additional dockets for this cluster, e.g. `Reddit, Inc. v. Anthropic PBC`) began returning HTTP 202 AWS-WAF challenge pages instead of content, and stayed blocked through eight retries spaced 25 seconds apart over roughly 3 minutes. The Chrome extension (`mcp__claude-in-chrome`) reported "Browser extension is not connected" throughout this session — the task's named fallback path was unavailable. A Playwright-driven browser (`mcp__MCP_DOCKER__browser_navigate`) was also tried against the same blocked URL and returned "ERROR: The request could not be satisfied" (the same CloudFront/WAF block, not a distinct workaround). `storage.courtlistener.com` PDF downloads were not observed to be rate-limited or WAF-gated at any point in this session.
- Both the original complaint (Doc #1, 101 pages) and the amended complaint (Doc #17, 108 pages, the operative pleading as of the 2025-12-05 minute order) were downloaded and converted to text with `pdftotext -layout`; both are text-layer PDFs, not scanned. The amended complaint was pulled specifically because it is the operative pleading and because a side-by-side check found it carries additional, more recent figures not present in the original (the Similarweb 83% AI-Overview zero-click rate, the Pew Research 8%/60%/36% figures, the Gannett/USA Today and Vox Media executive quotations, and the entire new Count V tying claim with its own ¶302 zero-click figures) as well as one structural change (five of the original 15 plaintiffs — Artforum Media, Art Media, Sourcing Journal Media, Sportico Media, Vibe Media Publishing — are absent from the amended complaint's caption and signature block; no docket entry explaining the drop was reached in this pull).
- Every dollar/percentage/traffic figure quoted above was cross-checked as present in both PDFs where the underlying paragraph carried the same content in both filings (renumbered but otherwise textually identical, confirmed by direct comparison of the surrounding sentences); figures marked "new in the amended complaint" were checked against the original complaint's text and are absent there.
- No exhibits were separately downloaded; docket entries list none attached to either the original or amended complaint (unlike several of this cluster's other dockets, which do attach side-by-side output exhibits).
- The docket's "Last Updated" field (Sept. 2, 2026) and the consolidated-hearing order (2026-07-29, hearing set 2026-08-25) postdate this pull's date and were read directly off the docket-entry list; no entry for the August 25, 2026 hearing's outcome was found in the entry list extracted, so its result (if any) is `unknown — checked docket entry list, 2026-09-22`.
