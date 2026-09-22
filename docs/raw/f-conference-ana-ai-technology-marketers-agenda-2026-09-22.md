# 2026 ANA AI and Technology for Marketers Conference — agenda

```yaml
source:          ANA (Association of National Advertisers)
url_or_doc_id:   https://www.ana.net/content/show/id/ms-mfm-sep26-agenda (overview: https://www.ana.net/content/show/id/ms-mfm-sep26)
published:       undated on the page itself; conference dated September 23-25, 2026, Oxon Hill, MD (MGM National Harbor), presented by Meta
pull_date:       2026-09-22
pull_method:     browser (claude-in-chrome extension, dedicated new tab; tabs_context_mcp reported connected, two other agents' tabs already open on google.com and sec.gov, neither touched); get_page_text sufficed for the overview/speakers page, read_page's interactive-element listing was used to find the distinct Agenda-tab URL (`...-agenda`), then get_page_text on that URL
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — conference's own agenda page, reliable on existence (session titles, speakers, employers, abstracts), biased on framing (abstracts are marketing copy; "the conference agenda, including speakers, is subject to change" per the page's own cancellation-policy notes)
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page text (get_page_text) of the Overview/Speakers tab and of the distinct Agenda-tab page; both captured in full, no pagination encountered
```

## Verbatim

### Event note

> The 2026 ANA AI and Technology for Marketers Conference, presented by Meta this September 23-25 just outside of Washington, D.C. in Oxon Hill, Md.

This event postdates the pull date (conference runs 2026-09-23 through 2026-09-25; pulled 2026-09-22, one day before it opens). No recordings or slide decks can be public yet for any session below.

### Total session count

Method: every distinct titled agenda-line item across the three published days (Wed Sept 23, Thu Sept 24, Fri Sept 25), as printed on the Agenda tab, counted by hand from the captured verbatim text. Two counts given because the page mixes short "Remarks" entries with full sessions:

- **46 total listed agenda entries** with a title (including Welcome/Opening/Closing Remarks, the Showcase Opening/Closing Remarks, and the MarTech Mastery Awards Gala), excluding only the un-titled logistics blocks (Registration Open, three Networking Breaks, Breakfast x2, Lunch, Networking Reception, Marketing Roundtable Meet-ups is titled and counted).
- **37 of the 46** are substantive named talks/workshops/panels/showcases (excluding the 9 "Remarks"-only entries: 2 on Day 1 — Welcome, Closing; 5 on Day 2 — Opening, Welcome, Closing, Showcase Opening, Showcase Closing; 2 on Day 3 — Welcome, Closing).

Breakdown by day: Day 1 (Sept 23) 13 entries (11 substantive); Day 2 (Sept 24) 24 entries (19 substantive); Day 3 (Sept 25) 9 entries (7 substantive).

### Sessions matching set O / set P terms (`docs/sources/query-book.md` alias sets)

**1 of 46 matched** — title and abstract read in full for every one of the 46 entries; only one names a set O term ("GEO", "AI Visibility") verbatim.

> SHOWCASE #3: BEYOND GEO: TURNING AI VISIBILITY INTO BUSINESS OUTCOMES
>
> Don't just track visibility. Know what it's worth.
>
> Every brand is racing to track how often AI engines mention it -- but visibility measurement is table stakes, not a strategy. This session moves past citation counts and share-of-answer benchmarks to the question that actually matters: is your AI presence driving your business? Jon Werther, Head of US Business at Brandlight, breaks down why most GEO tools stop at measurement and directional recommendations -- and shares real client outcomes that show what it looks like when visibility actually pays off.
>
> Jon Werther
> Head of US Business
> Brandlight.ai
> MGM Grand Ballroom A (IN-PERSON ONLY)
> Thursday, September 24, 2026, 11:30am - 11:40am

[note: abstract promises "real client outcomes" but the session has not been delivered as of the pull date — no client name, no engine, no date window, no figure is stated in the abstract itself. Screened, no public artefact — see census]

### Other sessions naming AI-assistant-adjacent concepts without a literal set O/P alias term (checked, not counted as matches)

Two further sessions discuss zero-click/AI-answer influence but do not use a literal set O or set P alias phrase in their title or abstract, so are excluded from the match count above per the literal-alias rule:

> WINNING WITHOUT THE VISIT - WHY INFLUENCE MATTERS MORE THAN CLICKS IN THIS NEXT AI
> Smriti Sharma, SVP of Analytics and Managing Director, Comscore CustomIQ
> "consumers aren't just searching for what they want - they're asking questions, comparing products, validating results, and acting on in-depth conversations with AI, often without visiting a brand's website"

> TRUST & CREDIT IN THE AGE OF AI: AI CAN GENERATE THE ANSWER. HUMANS STILL CREATE THE TRUST
> Pete Blackshaw (Founder & CEO, BrandRank.AI), Mishka Pitter-Armand (CMO, NPR)
> introduces "Trust Contribution: the value that trusted, human-created content brings to an AI answer, even when that contribution is invisible"

### Vendor/agency speakers present on this agenda relevant to lane A/E rosters

Speakers whose employer is an AI-visibility vendor or GEO-focused agency already noted elsewhere in this research programme, named here for cross-reference only (no additional claim pulled): Pete Blackshaw (Founder & CEO, BrandRank.AI), John Costello (CEO, Costello Ventures; Advisor to Canva, BrandRank.ai and ZeroToOne.ai), Jon Werther (Head of US Business, Brandlight.ai), Danilo Tauro (CEO, CartographAI), Andrew Bailey (Co-Founder & COO, ZeroToOne.AI).

### Sponsor visibility (S8 bias note)

[note: the agenda page lists a "Presenting Sponsor" (Meta, named in the event description as presenting sponsor) and a "General Sponsors" section, but the sponsor logos/names under "General Sponsors" render as images not captured by get_page_text — sponsor names beyond Meta and Hightouch/adMarketplace (named as meal sponsors in the agenda body: "BREAKFAST (Sponsored by Hightouch)", "LUNCH (Sponsored by adMarketplace)") are `unknown — checked ana.net 2026-09-22`]

## Pull notes — mechanical only

- The Overview/Speakers tab and the Agenda tab are separate URLs on this platform (`...ms-mfm-sep26` vs `...ms-mfm-sep26-agenda`), reached by following the "Agenda" tab link's actual `href` (found via `read_page` interactive-element listing) rather than a same-page anchor scroll — clicking the visible "Agenda" tab link while on the Overview page did not change the captured `get_page_text` output.
- No pagination or "Load More" control encountered; the full three-day agenda text was returned by one `get_page_text` call on the Agenda-tab URL.
- Sponsor logo images under "General Sponsors" were not OCR'd or alt-text-extracted this pull.
- Did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com or amazon.com's assistant. Worked from a dedicated tab; did not touch the two tabs already open in the shared browser group at session start (google.com search, sec.gov EDGAR).
