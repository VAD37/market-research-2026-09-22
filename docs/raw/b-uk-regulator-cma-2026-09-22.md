# UK CMA — Google general search SMS designation and fair ranking conduct requirement

```yaml
source:          Competition and Markets Authority (CMA), via GOV.UK
url_or_doc_id:   https://www.gov.uk/cma-cases/googles-general-search-and-search-advertising-services (case index); https://assets.publishing.service.gov.uk/media/68e8b29b1c8b2a3b50690811/SMS_Decision_Notice.pdf (SMS Decision Notice); https://www.gov.uk/find-digital-markets-measures/google-search-fair-ranking-conduct-requirement (fair ranking conduct requirement page)
published:       SMS Decision Notice: 2025-10-10. Fair ranking conduct requirement: imposed 2026-06-17, page last updated 2026-08-04. Case index page: published 2025-01-14, last updated 2026-06-17.
pull_date:       2026-09-22
pull_method:     browser extension (case index and fair-ranking CR pages); WebFetch (SMS Decision Notice PDF, which loaded and rendered as readable text, unlike the two eur-lex-sourced PDFs also attempted in this session — see pull notes)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed/binding regulatory decision (SMS Decision Notice under the Digital Markets, Competition and Consumers Act 2024) and the CMA's own case-management page naming its imposed conduct requirement
source_label:    filed
lane:            B, D
sub_market:      paid placement
engine:          Google — AI Overviews, AI Mode (explicitly in scope); Gemini app (explicitly out of scope, see below)
metric_kind:     none
supersedes:      none
captured:        SMS Decision Notice paragraphs 1-12 (full) and its Annex (full) naming which Google products are in/out of scope, including AI Overviews, AI Mode and the Gemini AI assistant; case-index page's full "Conduct requirements" and "SMS investigation" sections with all dates; fair ranking conduct requirement page (full)
```

## Verbatim

### SMS Decision Notice — designation and scope (full document, 5 pages)

"NOTICE UNDER SECTION 14(2) OF THE DIGITAL MARKETS, COMPETITION AND CONSUMERS ACT 2024 (THE ACT)

The Competition and Markets Authority (CMA) hereby gives notice as required by section 14(2) of the Act that, having carried out an initial strategic market status (SMS) investigation as required by section 2(4) of the Act (the SMS Investigation), it has decided to designate the undertaking known as Google as having SMS in respect of general search services pursuant to section 2(1) of the Act (the SMS Designation).

...

Description of the digital activity with respect to which the SMS Designation has effect

2. The SMS Designation has effect with respect to Google's provision of:

A service that searches the world wide web, and can draw on other sources, to return information on any subject (general search);

and

A service that enables advertising to users of general search (search advertising)

together, general search services.

...

The period for which the SMS Designation has effect

5. In accordance with section 18(1) of the Act, the SMS Designation has effect for five years beginning with the day after the day on which this notice is given.

6. The SMS Designation will therefore begin on 11 October 2025 and have effect until 10 October 2030 (the Designation Period), subject to the provisions in the Act for extension of the Designation Period and revocation of the SMS Designation before the end of the Designation Period.

...

Competition and Markets Authority

10 October 2025

Annex

Google products within and outside the scope of the SMS Designation as of the date of the SMS Decision Notice

This Annex sets out which of the existing products offered by Google are within the scope of the SMS Designation at the point of issuing the SMS Decision Notice. The CMA may update this Annex during the Designation Period.[footnote 1]

1. As of the date of the SMS Decision Notice, the following Google products are within the scope of the SMS Designation:

a. Google Search:

i. however it is accessed; and

ii. all information it returns through its underlying infrastructure, including on its search engine results page (SERP). For example:

1. generative AI features such as AI Overviews and AI Mode;

2. other features presented on the SERP such as specialised search units, videos and maps, and the 'Top Stories' carousel;

3. the 'News' tab; and

4. Google Discover;

b. Programmable Search Engine (ProSE) and Web Search Syndication (WSS) when configured to provide general search;

c. AdSense for Search when used in conjunction with ProSE or WSS to provide advertising to users of general search; and

d. Google Ads and SA360 when they provide search advertising.

2. As of the date of the SMS Decision Notice, the following Google products are outside the scope of the SMS Designation:

a. Google's standalone specialised search services;

b. ProSE and WSS when not configured to provide general search;

c. Google News;

d. Gemini AI assistant; and

e. Google's advertising products when they do not provide search advertising. For example:

i. Google Ad Manager which provides display advertising;

ii. Google Ads and SA360 when they provide display advertising; and

iii. AdSense for Search when not used in conjunction with ProSE or WSS to provide advertising to users of general search.

[footnote 1: Although it would not necessarily do so in every case, the CMA would carry out a public consultation before deciding whether to update this Annex so as to include Google's Gemini AI assistant within the scope of the SMS Designation.]"

### Case index page (gov.uk/cma-cases/googles-general-search-and-search-advertising-services) — full "Conduct requirements" section

"Conduct requirements

Fair ranking and data portability conduct requirements imposed

17 June 2026: The CMA has imposed its fair ranking and data portability conduct requirements on Google.

Fair ranking conduct requirement (17.6.26)
Data portability conduct requirement (17.6.26)
Press release: Further CMA action to secure a fairer deal for businesses and improve Google search services in UK (17.6.26)

Publisher conduct requirement imposed

3 June 2026: The CMA has imposed its publisher conduct requirement on Google.

Publisher conduct requirement (3.6.26)
Press release: CMA secures fairer deal for publishers and improves Google search services in UK (3.6.26)"

### Fair ranking conduct requirement page (gov.uk/find-digital-markets-measures/google-search-fair-ranking-conduct-requirement) — full body text

"Google search fair ranking conduct requirement

The Competition and Markets Authority (CMA) has imposed a conduct requirement on Google, in relation to its general search services.

From: Competition and Markets Authority
Published: 17 June 2026
Last updated: 4 August 2026 — See all updates
Firm: Google
Activity: Search
Type: Conduct requirement
State: Open
Opened: 17 June 2026

Imposition of conduct requirement

17 June 2026: Following the CMA's decision to designate Google as having strategic market status in respect of general search services and public consultation on proposed conduct requirements, the CMA has imposed the fair ranking conduct requirement (the fair ranking CR) on Google.

Fair ranking CR summary (PDF, 175KB) (4.8.26)
Fair ranking CR final decision (PDF, 413KB) (17.6.26)
Fair ranking CR notice (PDF, 150KB) (17.6.26)
Fair ranking CR interpretative notes (PDF, 132KB) (17.6.26)
Fair ranking CR compliance reporting notice (PDF, 158KB) (17.6.26)

The fair ranking CR requires Google to:

rank organic search results based on objective and non-discriminatory criteria, including in search generative AI features

provide transparency over how it ranks organic search results, and provide sufficient notice and information about material changes that could affect publishers and reduce avoidable costs

enable publishers to effectively raise concerns about manual actions and material changes that may have a distortive or other adverse effect on UK markets"

## Pull notes — mechanical only

- The SMS Decision Notice PDF (138.5KB, from `assets.publishing.service.gov.uk`) rendered fully readable via `WebFetch`'s file-save-and-`Read` path (the file was saved locally and read with the `Read` tool, which parsed it cleanly as 5 pages) — unlike two EU-hosted PDFs attempted earlier in this same task (the AI Act and DSA authentic-OJ PDFs were not attempted as PDFs at all; a separate `SMS_decision_notice.pdf` guessed-URL attempt 404'd before the correct URL was found via the page's own link elements). The 2.6MB "Final decision report" PDF for the same case was also attempted via `WebFetch` and returned unreadable binary/compressed-stream output — not re-attempted via `Read` in this session due to time budget; flagged as a gap.
- The case-index page (`gov.uk/cma-cases/...`) and the fair-ranking CR page (`gov.uk/find-digital-markets-measures/...`) both loaded cleanly via the Chrome extension's `get_page_text`, no truncation issues (unlike the EU eur-lex pulls in this cluster, gov.uk pages did not require the `textContent`/windowed-extraction workaround).
- Not pulled in this session, for the record: the Fair ranking CR final decision, notice, interpretative notes and compliance reporting notice PDFs (413KB/150KB/132KB/158KB); the data portability and publisher conduct requirements (imposed the same dates, named on the case index page but not opened); the 2023 CMA "AI Foundation Models: Initial review" and its subsequent 2024/2025 update papers (found by search, not opened — the 2025-10-10 SMS Decision Notice and the 2026-06-17 fair ranking CR are more directly on-point for "AI search" as named in this task, and are dated closer to the 2026-09-22 pull date).
- This file does not establish whether the fair-ranking CR's "transparency over how it ranks organic search results" extends to *paid* placement disclosure inside AI Overviews/AI Mode specifically, as distinct from organic ranking — the CR text captured above speaks to organic ranking criteria and transparency, not to sponsored/paid-content labelling. Recorded as an unknown in the summary file.
- Gemini (Google's standalone AI assistant app) is explicitly **outside** SMS-designation scope as of the SMS Decision Notice's own date (2025-10-10), with the CMA's footnote stating it would consult publicly before adding Gemini to scope. No later CMA page found in this session states Gemini has since been added. Recorded as `unknown — checked gov.uk/cma-cases/googles-general-search-and-search-advertising-services 2026-09-22 (case index shows no update on this point beyond 17 June 2026)` in the summary file.
