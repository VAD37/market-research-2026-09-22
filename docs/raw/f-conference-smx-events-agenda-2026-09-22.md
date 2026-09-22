# SMX events (Search Engine Land / Third Door Media, and SMX Munich licensee) — agendas

Three related "SMX" branded conferences pulled in one session because they share a publisher family (Search Engine Land / Third Door Media for the US events; a separate licensee, Rising Media, for SMX Munich) and were discovered together via one search. Each event is a separate pull with its own header block below.

```yaml
source:          Search Engine Land / Third Door Media (SMX Advanced, SMX Next); Rising Media (SMX Munich, licensed SMX brand)
url_or_doc_id:   https://searchengineland.com/smx/advanced/agenda ; https://searchengineland.com/smx/next/agenda ; https://smxmuenchen.de/en/agenda/2026/
published:       undated on the pages themselves; event dates stated per event below
pull_date:       2026-09-22
pull_method:     browser (claude-in-chrome, dedicated tab); searchengineland.com returns 403 to plain WebFetch (per `docs/sources/query-book.md` note) so the browser extension was used throughout; get_page_text returned only nav/footer text on both searchengineland.com pages, so javascript_tool (`document.body.innerText`, sliced) was used for SMX Advanced; javascript_tool returned "Permission denied for JavaScript execution on this domain" on smxmuenchen.de, so read_page (accessibility tree) was used there instead — first ~40,000 of an ~88,000-character rendered tree captured, see pull notes for the resulting coverage gap
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — each event's own agenda page, reliable on existence (titles, speakers, employers), biased on framing (marketing copy per session)
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        SMX Advanced — full rendered agenda text (19,722 characters via javascript_tool, no pagination beyond initial load). SMX Next — full page text, agenda not yet published. SMX Munich — first ~40,000 characters of the rendered accessibility tree (day 1, morning through mid-afternoon); day 1 evening and all of day 2 (11 March) not captured this pull
```

## Verbatim

### Event 1 — SMX Advanced 2026, Boston (June 3-5, 2026 — past event as of pull date)

Page title: "SEO, PPC AI training | SMX® Advanced | June 3-5, 2026 | Boston"

**Total session count.** Method: full page text (19,722 characters) scanned; every distinct titled agenda-line item counted by hand across the rendered days (Wednesday June 3 through the point the text ends — the rendered text reaches into "Friday — June 5th, 2026" per the pull, so all three days are represented, though not confirmed complete to the day's close). **Not decomposed into an exact total this pull** — see pull notes; the count exercise below is restricted to the set O/P keyword matches, which is what this pull's done-condition requires.

**Sessions matching set O / set P terms** — regex-scanned across the full page text for the same alias-term list used on the other conferences in this cluster. **5 of the scanned agenda matched** (title or speaker-title field carries a literal alias term):

> The SEO + AEO convergence: Change the way you work
> Chris Sachs, VP of Value Enablement, seoClarity
> 2:55 PM - 3:10 PM ET

> Stop reacting. Start leading: Change management for search's next era
> Speaker: Jennifer Cornwell, **Sr. Director of AI SEO**, Tinuiti [match is in the speaker's job title, not the session title]
> Moderator: Danny Goodwin, Editorial Director, Search Engine Land & SMX
> Track: PPC, Location: Grand Ballroom B, 4:15 PM - 4:45 PM ET

> From SEO to GEO: Increasing AI search Share of Voice in 90 days
> Christian Hustle, Global Enablement Manager & Search Strategist, Uberall
> Track: Theater, Location: Grand Ballroom C, 9:35 AM - 9:50 AM ET
> [graded separately with its public YouTube recording — see `docs/raw/e-case-smx-advanced-christian-hustle-2026-09-22.md`]

> How to actually measure AIO/GEO success
> Simon Lesser, Chief Product Officer, Dragon Metrics
> 11:15 AM - 11:30 AM ET

> Entity optimization in 2026: Schema, site architecture, and signals that define your brand
> Speaker: Grant Simmons, **Director of SEO | Content & GEO Strategist**, Waikay, InLinks & Fiat Growth [match is in the speaker's job title, not the session title]
> Moderator: Danny Goodwin, Editorial Director, Search Engine Land & SMX
> Location: Grand Ballroom A, 12:30 PM - 1:00 PM ET

**Near-miss sessions checked and excluded** (topically about AI search/visibility but no literal set O/P alias phrase in the title, speaker field, or the empty description placeholder rendered on the page — every session's "Description" field rendered empty in the static DOM this pull, requiring a per-session "Explore" click not performed at scale):

> Your AI ROI story is broken: How to fix it before budgets get cut — Purna Virji, Founder, Agent-Led Growth
> From rankings to responses: Growing visibility in AI-driven search — Chris Sullivan, Head of Growth, Previsible
> From search to genAI: New research on consumer trust, brand strategy, and discovery — Kelsey Libert, Cofounder, Fractl
> Searchpocalypse AI: Zero-click searches are surging and AI traffic isn't filling the gap — Eli Goodman, CEO & Co-founder, Datos
> The local content crisis in the age of AI search — Shawn Huber, SEO Program Director & Sebastian Pawlowski, EVP, Lastmile Retail
> AI Ops for SEO: How operational maturity wins the next decade of search — Darrell Tyler, Senior Manager, Organic Growth, CallRail
> The AI account revolution: Why keywords are dead and how one enterprise rebuilt for publisher intelligence — Kyle Thomas, Chief Scientist, MotiveMetrics
> Organic, paid, and AI search: One strategy to rule them all — Brad Stephenson, SVP Marketing, Level Agency
> AI answer tracking wins and woes: What to measure and how to avoid false wins — James Wirth, Sr. Director Strategy & Growth, Citation Labs
> The AI Search Operating System for SEO leaders — Amanda Milligan, Content and Growth Manager, Semrush

### Event 2 — SMX Next 2026, Online (November 18, 2026 — future event as of pull date)

Page title: "SEO, GEO, PPC, AI Agenda | SMX® Next | Online Nov. 18, 2026"

> Keep scrolling to preview the SMX Next 2026 agenda!

No session-level content is rendered on the page as of the pull date — the page consists of nav, a "Keep scrolling to preview..." placeholder, sponsor/newsletter blocks, and footer only. `unknown — checked https://searchengineland.com/smx/next/agenda 2026-09-22` for session count and set O/P matches; only the page's own title tag ("SEO, GEO, PPC, AI Agenda") confirms GEO is a named track category for this future event.

### Event 3 — SMX Munich 2026 (10-11 March 2026, ICM International Congress Center Munich, Germany — past event as of pull date; EU event)

Page title: "Agenda - SMX Munich 2026"; header: "Review Agenda - SMX Munich 2026 10th & 11h March, 2026 ICM - International Congress Center Munich"

Tracks listed: Analytics & Data Literacy, Content, Partner Track, PPC, SEO, SEO and PPC Basics, SMX for E-Commerce, Specials, SMX Partner Track, Interactive Sessions, Interaktive Sessions.

**Sessions matching set O / set P terms**, read from the portion of the agenda captured (day 1, 10 March, morning through ~4:05 PM CET):

> The Citation Playbook – Data and Insights on the Most Cited Sources in AI Search
> Speaker: Malte Landwehr, CPO & CMO, **Peec AI**
> Moderator: Jana Lavrov, Director Data Analytics and SEO, DIE ZEIT
> Room: Saal 1, 11:40 AM
> Abstract (truncated by the accessibility tree at ~100 chars): "In this session, Malte will present large-scale data on the most frequently cited sources across Cha[tGPT...]"

> Navigating the SEO & GEO Landscape: How the Most Successful Brands Are Winning in AI Search (and How...) [title itself truncated by the accessibility tree]
> Speaker: Leon Sentker, **Peec AI**
> Moderator: Dr. Christoph Röck, Managing Director, 121WATT
> Room: Saal 2, 4:05 PM
> Abstract (truncated): "LLMs have fundamentally changed how consumers search and buy products. To win, brands need to stay v[isible...]"

**Vendor speakers present, cross-reference only (no literal alias term in the session title itself, so not counted as a match above):**

> AI-Monitoring im Reality Check: KPIs, Messbarkeit & Umsetzung
> Speakers: Thomas Peham, CEO, **OtterlyAI**; Mathias Ptacek, Founder and CEO, **Rankscale.ai**
> Moderator: Markus Hövener, Founder and SEO Advocate, Bloofusion
> Room: Saal 13a, 2:40 PM

**Discussion-round sub-topics naming AI/LLM concepts without a session-level alias match** (these are breakout-table topics inside a single "Discussion Rounds" interactive session, not their own titled sessions): "Content Strategy in the Age of LLMs", "AI Overviews & Generative Search: How can we measure traffic reliably?", "PMax & AI Max: How do we maintain control in a fully automated environment?" (German-language duplicate round makes the same three points).

**Total session count: not fully captured this pull.** The rendered accessibility tree for this single agenda page ran to approximately 88,000 characters; this pull captured the first ~40,000 (day 1, 10 March, from the 7:00 AM morning run through the 4:05 PM session block) before the read tool's per-call size limit was reached, and a second call to continue past that point returned the same initial content rather than the next segment (the tool has no text-offset parameter, only a `ref_id`/depth scoping the same rendered tree does not expose). Day 1 evening sessions and the entirety of day 2 (11 March 2026) are **not captured** — `unknown — checked https://smxmuenchen.de/en/agenda/2026/ 2026-09-22, partial render only`. A machine-readable full agenda exists as a PDF at `https://smxmuenchen.de/wp-content/uploads/sites/27/2026/03/smxde26_agenda_a4_030925.pdf` (linked from the page's "Print overview" control) but was not opened this pull.

Sessions counted in the captured portion (day 1 through ~4:05 PM, all tracks, including logistics entries): approximately 35 titled agenda items (hand count of headings captured; includes Morning Run, Registration, SMX Orientation, Opening, Opening Keynote, Coffee Break, then 6 parallel-track sessions at 10:30 AM, 6 at 11:40 AM, the Alex Schultz keynote conversation at 1:45 PM, Room Change, 6 parallel-track sessions at 2:40 PM, the Discussion Rounds block, Coffee Break, and 6 parallel-track sessions at 4:05 PM). This is a lower bound on the true one-day count and not a total for the two-day event.

## Pull notes — mechanical only

- SMX Advanced: `get_page_text` on `searchengineland.com/smx/advanced/agenda` returned only "Intelligence Reports..." boilerplate from the `<article>` element; `javascript_tool` (`document.body.innerText`) was used instead and returned the full 19,722-character rendered agenda in one read, no "Load More" or pagination control encountered. Per-session "Explore" links exist to expand each session's description but were not clicked at scale (156 CMW-style expansion would have required as many navigations as CMW's session count); only the two sessions graded as cases (Christian Hustle / Uberall — separate file) had their linked artefacts pursued.
- SMX Next: confirmed via direct page load that the agenda is not yet published (`Keep scrolling to preview the SMX Next 2026 agenda!` placeholder, no session content in the DOM).
- SMX Munich: `javascript_tool` returned `Permission denied for JavaScript execution on this domain` on both `smxmuenchen.de` page loads — the extension's site-level permission does not cover this domain in this session, and no retry mechanism to grant it was available to this task. `get_page_text` returned only the filter sidebar's track/day labels, not the session list. `read_page` (accessibility tree) was used instead and did return full session content, but the tool truncates at its `max_chars` ceiling with no offset/pagination parameter, so only the first segment of the tree was captured; a second identical call returned the same first segment rather than continuing.
- Did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com or amazon.com's assistant.
