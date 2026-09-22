# News Plaintiffs' Public Redacted Summary Judgment Brief — In Re: OpenAI, Inc. Copyright Infringement Litigation (MDL 1:25-md-03143) — Microsoft click-through-rate data

```yaml
source:          News Plaintiffs (The New York Times Company, Daily News LP, The Center for Investigative Reporting, The Intercept Media, Ziff Davis LLC), filed via CourtListener/RECAP
url_or_doc_id:   https://www.courtlistener.com/docket/69879510/1977/1/in-re-openai-inc-copyright-infringement-litigation/ ; direct PDF: https://storage.courtlistener.com/recap/gov.uscourts.nysd.640396/gov.uscourts.nysd.640396.1977.1.pdf ; ECF No. 1977, Attachment 1, Case No. 1:25-md-03143-SHS-OTW (S.D.N.Y.)
published:       2026-09-17
pull_date:       2026-09-22
pull_method:     browser extension (CourtListener docket navigation) to locate the document; fetch (mcp fetch tool) to confirm PDF identity; Bash curl download of the PDF plus local pdftotext extraction to read the 92-page brief and quote verbatim passages
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed court exhibit (summary judgment brief with cited factual record), per trust-rubric.md tier 2 "filed — S-1, 10-K, court exhibit, funding filing"
source_label:    filed
lane:            A
sub_market:      organic recommendation
engine:          Microsoft Copilot (Bing Chat); OpenAI ChatGPT referenced comparatively
metric_kind:     traffic
supersedes:      none
captured:        excerpts — key click-through-rate and substitution passages extracted via pdftotext from the 92-page PDF; full document not reproduced. Pointer trade item: PPC Land, "Microsoft measured Copilot cutting publisher clicks by up to 94%," https://ppc.land/microsoft-measured-copilot-cutting-publisher-clicks-by-up-to-94/, published 2026-09-21, read 2026-09-22 — the article that led to this pull; its own figures are corroborated verbatim below, so no separate pointer file is filed for it per task instructions (primary reached).
```

## Verbatim

Document caption confirmed on CourtListener: "Exhibit Public Redacted Memorandum of Law — Document #1977, Attachment #1", filed 2026-09-17 10:30 a.m. EDT, in *In Re: OpenAI, Inc. Copyright Infringement Litigation*, 1:25-md-03143 (S.D.N.Y., Judge Sidney H. Stein). Docket description: "LETTER addressed to Judge Sidney H. Stein from Davida Brook dated September 17, 2026 re: Public, Redacted Version of News' Plaintiffs' Memorandum of Law. Document filed by Daily News LP, The Center for Investigative Reporting, Inc., The Intercept Media, Inc., The New York Times Company, Ziff Davis, LLC." PDF internal title (XMP metadata): "News Plaintiffs' Summary Judgment Brief_Public Version for September 17_Redacted for filing 1015am_Redacted.pdf", created 2026-09-17T10:03:54-04:00 by author "rthomas".

Page 10 of 92 (brief's own pagination, p.1 of argument):

> "Defendants' own data show this 'doom loop' in motion, with Microsoft recording 83-93% drops in click-through rates for The Times and DNP's domains, and 51% to 94% for ZD's domains, for Microsoft's Copilot 'answer engine' compared to traditional Bing search. SF1536."

Same page, preceding paragraph:

> "Microsoft's CEO Satya Nadella agreed under oath that conversing with chatbots 'has substituted ... giving you the information right there on the website on the AI platform versus needing to go to the underlying source.' SF1432. A Microsoft document recognizes that nobody wins that contest: 'Our AI content strategy has started a "doom loop" that will hurt the performance of our models and the entire web at the same time: It is highly unusual that an end-product threatens the economic foundations of its essential suppliers, but that is the situation we have created for our LLM business with respect to its "content supply chain."' SF1672."

Page ~61 of 92 (argument section on substitution):

> "But unlike traditional search engines, Defendants' products: (1) reduce the incentive for users to click on links to publishers' websites, (2) generate outputs using up to [REDACTED] characters of grounded content, and (3) provide portions of paywalled content to users. SF1536 (Microsoft data showing the overall click-through rate difference between Copilot and traditional Bing Search was 87-93% for The Times, 83-91% for DNP, and 51-94% for ZD); SF1524 (Copilot's home page welcoming users by stating: 'Instead of clicking through links, we can talk through whatever ...')"

Page 76 of 92:

> "Microsoft's survey expert reported that 37.2% of Copilot survey respondents would use 'traditional web search inquiries' like Google in the 'absence of a generative AI tool.' SF1515."

Same page, following paragraph:

> "The replacement of search with GenAI harms publishers by producing drastically lower click-through rates ('CTRs'). SF1530-1537. As explained above, Plaintiffs are not required to prove harm empirically: common sense suffices. But Microsoft's representative CTR data shows that the overall click-through rate reduction between Bing Chat and Bing Web Search was 87% to 93% for The Times's websites, 83% to 91% for DNP's websites, and 51% to 94% for ZD websites. SF1536."

Page ~36 of 92 (third-party ChatGPT-visit-behavior citation, not Microsoft's own data):

> "OpenAI's Nick Turley made the same point about ChatGPT's 'browse' function: once the chatbot gives an answer, there is 'no good reason to click' on a link to the underlying source, such as a news website. SF1525. See also SF1539 (third party study reporting that 87.78% of ChatGPT users visit no external websites during their search, compared to only 26.91% of Google users)."

NYT subscriber substitution figure:

> "Among Times subscribers who were surveyed who used or paid for ChatGPT for news, 36% responded that their use of ChatGPT 'means I no longer need news from the New York Times at all.' SF1581."

Cloudflare crawl-to-referral ratio:

> "Cloudflare's CEO cited data showing the ratio of webpages scraped to visitors sent: in 2015, Google scraped two pages for every visitor (2:1); by June 2025, that ratio was 18:1 for Google and 1,500:1 for OpenAI. SF1540."

[note: the brief cites its factual record via "SF" (Statement of Facts) paragraph numbers, e.g. SF1536, SF1432, SF1672, SF1515, SF1539, SF1581, SF1540 — the underlying SF exhibits themselves were not separately opened in this pull; only the brief's own quoted characterization of them is captured here, per what the brief states.]

[note: the brief internally states the Times/DNP click-through figure two different ways in two places — "83-93% drops ... for The Times and DNP's domains" (p.10, combined range across both plaintiffs) versus "87% to 93% for The Times's websites, 83% to 91% for DNP's websites" (p.76, separated per plaintiff) and "87-93% for The Times, 83-91% for DNP" (p.61 body text). Both versions are captured verbatim above, side by side, not reconciled — this is the brief's own internal presentation, not a transcription error introduced by this pull.]

## Pull notes — mechanical only

- Access path: `courtlistener.com` returns 403 to plain fetch (confirmed again this session) and to `robots.txt` check. The Chrome extension (`claude-in-chrome`) was connected this session and reached the docket cleanly — contrary to STATE.md's P2-c11 note that the extension reported "not connected" for that earlier agent. Extension access worked via a dedicated new tab (tabId 1697684069), created with `tabs_create_mcp` and not reused from any other agent's tab in the shared browser session.
- Located the case's RECAP docket at `courtlistener.com/docket/69879510/in-re-openai-inc-copyright-infringement-litigation/` (found via DuckDuckGo HTML search, since the case-name site search on courtlistener.com itself was navigated directly). The docket runs to 11 pages in the site's own paginated view; document #1977 was found on page 11 (`?page=11`) via the `find` tool's semantic element search, matching the PPC Land article's "docket 1977-1" reference exactly (Davida Brook letter dated 2026-09-17).
- The attachment (1977-1, "Exhibit Public Redacted Memorandum of Law") does not render its text through the page's own `<article>` DOM even after clicking the "Text" tab (page metadata only, PDF viewer is a separate embed) — so the direct PDF download link was extracted instead (`storage.courtlistener.com/recap/...1977.1.pdf`, found via the `find` tool locating the "From CourtListener" download href), downloaded via Bash `curl` to a local scratch path outside `docs/raw/` (`/tmp/p4c6/nyt-brief-1977-1.pdf`, 12.4 MB), and converted to text locally with `pdftotext -layout` (found on this machine at `/mingw64/bin/pdftotext`) for verbatim quote extraction. The PDF file itself was not copied into `docs/raw/` — only this raw-pull file, which quotes it verbatim per template.
- The brief is 92 pages; only the click-through-rate and substitution-metric passages relevant to this cluster's target (a primary behind a trade-press item reporting an AI-surface traffic/scale figure) were extracted. The brief also states scale figures (OpenAI/Microsoft revenue, valuation, training-corpus token counts) already captured in this repo's `docs/raw/b-court-mdl-openai-copyright-2026-09-22.md` and sibling docket files from Pass 2 cluster P2-c11 (those pulls captured only "docket header and page 1" of the coordination docket, not this specific September 17 exhibit, per that file's own caveats) — not re-captured here to avoid duplication.
- This document corroborates, verbatim and near-exactly, every figure PPC Land's article ("Microsoft measured Copilot cutting publisher clicks by up to 94%," 2026-09-21) attributed to it: the 87-93%/83-91%/51-94% click-through ranges, the 87.78%/26.91% no-external-click comparison, the 37.2% Copilot survey figure, the 36% NYT-subscriber substitution figure, and the 18:1/1,500:1 Cloudflare crawl-to-referral ratio. No discrepancy found between the trade item's reporting and the primary document.
- 51-94% figure is for Ziff Davis (ZD) properties specifically, not a market-wide figure — carried with that population label, per root `CLAUDE.md`'s no-guessed-base rule.
