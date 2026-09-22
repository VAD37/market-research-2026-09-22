# Content Marketing World 2026 — schedule agenda

```yaml
source:          Content Marketing World 2026 (produced by Informa / Content Marketing Institute)
url_or_doc_id:   https://schedule.contentmarketingworld.com/ (session detail URLs cited per session below)
published:       undated on the page itself; event dates stated as October 5-7, 2026, Denver, CO (conference Oct 5-6, workshops Oct 7)
pull_date:       2026-09-22
pull_method:     browser (claude-in-chrome extension, dedicated new tab; tabs_context_mcp reported connected with two other agents' tabs already open — google.com and sec.gov — neither touched); get_page_text and read_page returned only the "2026 Agenda" heading on this single-page app, so javascript_tool (document.body.innerText, sliced) was used to extract rendered content; session totals and keyword matches captured via javascript_tool scans of the fully-loaded DOM after repeatedly invoking the page's own "Load More Sessions" control
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — conference's own schedule-builder page, reliable on existence (session titles, speakers, employers, tracks, dates), biased on framing (abstracts are marketing copy for the session)
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full rendered session-list DOM text (document.body.innerText) after the "ALL" day tab's paginated list was scrolled/clicked to completion (156 of 156 session links, list plateaued after 5 "Load More Sessions" clicks — see pull notes); individual session detail pages fetched in full for the three sessions matching set O/P terms
```

## Verbatim

### Event header (from schedule.contentmarketingworld.com root)

> October 5-7, 2026 Denver, CO
> Conference: Oct 5-6
> Workshops: Oct 7

### Total session count

Method: `document.querySelectorAll('a[href*="/session/"]').length` on the "ALL" day tab (default view, no track/session-type/pass-type filters applied — filter-checkbox clicks on this page did not visibly change the rendered list in this pull, so the unfiltered "ALL" view is what is reported), after repeatedly clicking the page's "Load More Sessions" button until the count stopped increasing.

> start=50 | after-click-0=75 | after-click-1=100 | after-click-2=125 | after-click-3=150 | after-click-4=156 | after-click-5=156 | plateau-at-5

**156 session-detail links** on the agenda as rendered 2026-09-22. This count includes every item with its own `/session/` page — keynotes, workshops, sponsored sessions, "Ask Me Anything" interactive slots, and logistics-type entries (Registration Open, Breakfast, Networking Break, Running Club, Yoga, Badge Pickup) that the platform lists as sessions with their own detail pages. Not decomposed into a substantive-only subcount this pull; the platform's own "Session Type" filter values observed in the DOM are: Keynote, Session, Workshop, Networking, Summit (All Access Required), Interactive Experience, Registration, Sponsored Session.

### Tracks listed (from the filter sidebar/dialog, `docs/method/demand-signals.md` S8 "channel kind" context)

> AI Systems & Content Tech, Ask Me Anything, Audience Building, B2B Marketing Impact, Brand & Demand Marketing, CMWorld, Career Building, Content Creation & Storytelling, Content Operations & Workflow, Content Strategy, Discoverability & Optimization, Earned Media, PR, & Brand Visibility, Expert Insights, General Session, Insight to Impact, LIONS, Marketing Analytics, Data, & ROI, Marketing Core Concepts, Partner Case Studies, Purposeful Marketing, Social Media & Creator Marketing, Summit | Marketing Effectiveness, Summit | Science & Magic, The Content Lab, Thought Leadership, Visual & Audio Experiences, Workshops

### Sessions matching set O / set P terms (`docs/sources/query-book.md` alias sets)

Method: `document.body.innerText` of the fully-loaded 156-session list was regex-scanned for every set O and set P alias term (see `query-book.md`). Matches on literal terms "AI visibility" and "AI search optimization"; the string "LLM-driven" also isolated one further session title. "sponsored" matches were all the platform's own "Session Type: Sponsored Session" label, not a set P alias, and are not counted as matches. No matches for GEO, AEO, LLMO, AI SEO, AI search visibility, brand visibility in AI, LLM visibility, citation rate, share of voice in AI answers, AI SOV, AIO, GSO, AISEO, AI Overviews optimisation, citation economy, AI discoverability, generative engine optimization/optimisation, answer engine optimization, sponsored answers/results/prompts, AI ads, conversational ads, ads in AI Overviews/AI Mode, AI ad inventory, Copilot ads, rate card, ChatGPT Ads, Perplexity, Alexa for Shopping.

**3 of 156 sessions matched** (title-level match; abstracts pulled in full below):

---

**Session 1 of 3**

> The Future of LLM-Driven Discovery: Becoming Discoverable in an AI-First World
> Tom Mansell (VP of Organic Performance, Croud)
> Location: Room 109
> Date: Monday, October 5
> Time: 10:00 am - 10:30 am
> Pass Type: All Access, Digital, CMWorld 2-Day, CMWorld 3-Day
> Session Type: Session
> Track: Discoverability & Optimization, CMWorld
> URL: https://schedule.contentmarketingworld.com/session/the-future-of-llm-driven-discovery-becoming-discoverable-in-an-ai-first-world/918766
>
> The search landscape is undergoing a major transformation. AI, social search, online communities, and digital marketplaces are breaking up the traditional search journey, and audiences are now navigating multiple platforms guided by intent, emotion, and identity.
>
> In this session, Tom Mansell, VP of Organic Performance at Croud, will introduce Croud's SearchAnywhere approach and offer practical insights on how to develop and execute a holistic search strategy, highlighting examples of client success stories. Attendees will learn how to expand brand visibility across the digital ecosystem, optimize for LLM-driven discovery, and combine human expertise with AI-powered tools. Using Croud's proprietary BrandCI and SEOCI tools, Tom will demonstrate how to measure discoverability, align brand signals with audience intent, drive measurable growth, and deliver a true return on intelligence in an increasingly fragmented search world.
>
> Rethink search beyond Google: Learn how to map the full search ecosystem to ensure your brand is visible wherever audiences are exploring.
> Build a data-driven, audience-centered strategy: Discover how to combine audience insights, behavioral signals, and human expertise with AI tools to optimize content and improve discoverability across platforms.
> Activate and measure across channels: Gain practical frameworks for executing cross-platform search strategies and measuring impact so your brand can drive visibility, engagement, and measurable growth in an AI-first world.

[note: abstract references "client success stories" and proprietary measurement tools (BrandCI, SEOCI) but names no brand, no engine-specific figure, no date window, and no sample size — screened separately below, no numeric claim to grade]

---

**Session 2 of 3**

> Gaining AI Visibility and Losing Human Credibility
> Wil Reynolds (Chief Executive Officer / VP Innovation, Seer Interactive)
> Location: Room 105
> Date: Tuesday, October 6
> Time: 10:15 am - 10:45 am
> Pass Type: All Access, Digital, CMWorld 2-Day, CMWorld 3-Day
> Session Type: Session
> Track: Content Strategy, CMWorld
> URL: https://schedule.contentmarketingworld.com/session/gaining-ai-visibility-and-losing-human-credibility/920776
>
> Your tightrope to winning in AI and with people is the tightest it has ever been. Gone are the days of low quality text at the bottom of your page, gone is the gaming of domain authority. Optimizing in the world of AI has picked up on some of the bad habits of SEO. We're already starting to see every major AI company coming up with ways to penalize the scaled recommendations.
>
> I'm producing 60–70% less content. My pipeline is growing. I want to help you think about KPIs for AI through a new lens.
>
> One Seer page went from 52 to 1,000 ChatGPT citations, we'll show you how that happened and the strategy behind the tests we deploy and how they've turned out.
>
> Everyone's racing for AI visibility. I want to pressure you to race for visibility that drives credibility.
>
> I'll show you what long term AI success looks like and I'll give you the numbers to back it up.
>
> I'll show how I'm using AI behind the scenes. Not to write more. To think harder about what's worth writing.
>
> Citations are not traffic. Traffic is not revenue. Know which one you're actually chasing — and how to explain the gap to your C-suite.
>
> Your prompt tracking is probably already out of date — and you're optimizing for a customer who no longer exists.
>
> The highest-leverage use of AI isn't content production. It's everything around it. I'll show you how I use AI to explore possibilities, and pull research from a dozen tools.

[note: speaker Wil Reynolds also appears as a MAICON 2026 speaker per `docs/raw/f-maicon-speakers-2026-09-22.md`, same employer Seer Interactive]

---

**Session 3 of 3**

> Scaling AI Search Optimization With Proactive AI-powered Agents
> Dale Bertrand (President, Fire&Spark)
> Location: Room 205
> Date: Wednesday, October 7
> Time: 10:45 am - 12:15 pm
> Pass Type: All Access, CMWorld 3-Day
> Session Type: Workshop
> Track: Workshops, CMWorld
> URL: https://schedule.contentmarketingworld.com/session/scaling-ai-search-optimization-with-proactive-ai-powered-agents/919219
>
> We approached AI search optimization the same way we approached SEO, with time-consuming research and content planning. Then we learned that AI search optimization at scale requires AI. This case study details how we built proactive, AI-powered workflows for AI search. Learn how we use AI to identify trending micro-topics, automate content refreshes, and monitor campaign performance.
>
> Build proactive AI agents for AI search to reduce time from signal to action
> Reduce manual analysis with autonomous content AI agents
> Create a trigger system for proactive content updates
> Deploy AI workflows to scale AI search execution
> Test content with AI before publishing

[note: speaker Dale Bertrand also appears as a MAICON 2026 speaker per `docs/raw/f-maicon-speakers-2026-09-22.md`, same employer Fire&Spark. Abstract calls itself "This case study" but names no client brand, no figure, no date window, no sample size]

---

### Near-miss checked and excluded (title uses "brand visibility" and "AI" but not as a contiguous set O alias phrase)

> Reinventing Brand Visibility: Communications in the Age of AI
> Erin Miller (Yahoo)
> Track: Earned Media, PR, & Brand Visibility, CMWorld
> Tuesday, October 6, 10:15am - 10:45am, Room 104

[note: excluded from the matched-session count above because the title does not contain "AI visibility" or "brand visibility in AI" as a contiguous phrase per `query-book.md` set O — "Brand Visibility" and "AI" appear separated by "Communications in the Age of"; abstract not pulled]

### Sponsor visibility (S8 bias note)

[note: this pull did not capture the event's sponsor/exhibitor list — `contentmarketingworld.com/sponsors/` exists as a separate page and was not fetched this pull. `unknown — checked schedule.contentmarketingworld.com 2026-09-22`, sponsor names not captured]

## Pull notes — mechanical only

- Access path: `https://www.contentmarketingworld.com/agenda/` returns 404; the real agenda lives at `https://schedule.contentmarketingworld.com/`, reached via the "View the Schedule" link in the main site's nav.
- `get_page_text` and `read_page` (accessibility-tree tools) both returned only the bare "2026 Agenda" heading on this page — the rendered session list sits outside the `<main>` element in the DOM as read by those tools, or is otherwise not captured by them. `javascript_tool` (`document.body.innerText`) was used instead for all substantive extraction on this domain; this is a deviation from the pull method used on other conference pages in this cluster (browser accessibility snapshot / get_page_text sufficed there).
- Track-checkbox filter clicks (`AI Systems & Content Tech`, `Discoverability & Optimization`, `Earned Media, PR, & Brand Visibility`) on both the inline sidebar form and the "Filters" dialog did not visibly change the rendered session list in two attempts; the unfiltered "ALL" list was used instead and scanned in full by keyword regex.
- The "Load More Sessions" pagination required simulated clicks (`Array.from(document.querySelectorAll('button')).find(...)`) with ~1.4s waits between clicks; count plateaued at 156 after 5 clicks (started at 50 on page load).
- Session count of 156 was not decomposed by Session Type in this pull (e.g., how many of the 156 are Registration/Networking/Breakfast logistics entries vs. substantive talks); flagged as a gap, not resolved.
- One independent-corroboration check was run for the Wil Reynolds "52 to 1,000 ChatGPT citations" claim: DuckDuckGo HTML search for `"seerinteractive" "ChatGPT citations" 52 1000` returned no matching results 2026-09-22 — the claim is not corroborated by any indexed page outside this session abstract as of the pull date.
- Did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com or amazon.com's assistant. Worked from a dedicated tab throughout; did not touch the two tabs already open in the shared browser group at session start (google.com search, sec.gov EDGAR) or the tabs opened by other concurrently-running agents observed appearing/changing in the shared tab group during this pull (tryprofound.com, quattr.com, athenahq.ai, rankprompt.com, sitefire.ai, courtlistener.com, trustpilot.com, openai.com, g2.com, capterra.com — none read or written to).
