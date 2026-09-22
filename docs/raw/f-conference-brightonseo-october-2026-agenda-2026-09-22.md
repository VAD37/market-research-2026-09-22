# brightonSEO — October 2026 (Brighton, UK) — talk schedule

```yaml
source:          brightonSEO (roughagenda.com / brightonSEO.com)
url_or_doc_id:   https://brightonseo.com/events/october-2026/schedule-oct-2026 (event overview: https://brightonseo.com/events/october-2026)
published:       undated on the page itself; event dated October 8-9, 2026, The Brighton Centre, UK
pull_date:       2026-09-22
pull_method:     browser (claude-in-chrome, dedicated tab). get_page_text returned an unrelated sponsored-party blurb rather than the schedule; javascript_tool (document.body.innerText, sliced) was used instead and returned the schedule in full for the day it rendered
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — conference's own schedule page, reliable on existence (session titles, speakers, tracks, times), biased on framing (session titles are speaker-written pitches)
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full rendered page text (document.body.innerText, 12,073 characters) via javascript_tool. This event postdates the pull date (Oct 8-9, 2026; pulled 2026-09-22), so no recordings or decks can be public yet for any session below
```

## Verbatim

### Event note

> October 2026 talk schedule
> Our October 2026 agenda for both brightonSEO and MeasureFest is now live and ready for you to start planning your visit.
> Browse the line-up below and create your own personalised agenda with the sessions you do not want to miss this 8 - 9 October.
> Here is the full agenda for our conference days on October 8-9 2026, including all the MeasureFest talks too.

From the event overview page (`brightonseo.com/events/october-2026`): "Join 4,500+ marketers from more than 70 countries... 190+ expert speakers... Hundreds of practical talks across SEO, AI search, content, digital PR and more... Full access to MeasureFest, our dedicated analytics and measurement event."

### Total session count

Method: `(document.body.innerText.match(/\b20 minutes\b/g)||[]).length` plus the same for `1 hour` (the two session-length labels the page prints per talk), run against the fully rendered page text.

> 20min=75 1hr=6 total=81

**81 talks captured — Day 1 (Thursday, October 8) only.** The rendered page ends at the "06:30 PM Thursday Night Party" evening-social entry and repeats the same party block in the footer; no Day 2 (Friday, October 9) content is present in the DOM captured this pull — see pull notes. 81 is a Day-1-only count, not the two-day total.

### Sessions matching set O / set P terms (`docs/sources/query-book.md` alias sets)

**9 of the 81 Day-1 talks matched** (title, track name, or both carry a literal set O alias term — GEO, AEO, or "LLM visibility"). No set P (paid placement) alias term matched anywhere in the captured text.

**Track: "GEO & AEO"** (Auditorium 1, 09:30 AM) — the track name itself is a direct alias match:

> Jean Sarunporn — Getting Your Brand Recommended by AI Agents: A Practical Guide to GEO
> Paris Childress — Information Gain: The Missing Metric in Every GEO Content Strategy?
> Samanyou Garg — Drowning in prompts? How to build an AEO program around the data that matters

**Standalone matches, other tracks/times:**

> Sam Page — Win at Local AEO - The Wild West of AI Search
> [time slot ~around 09:30-10:00 AM block, exact track heading not captured with certainty this pull]

> Jane Hunt — Prove It: A Digital PR Playbook for Winning AI Citations and Reporting GEO Impact
> Track: Digital PR / Communicating Data (MeasureFest), Syndicate 3&4

> Paul Ryazanov, Serge Bezborodov — Masterclass: AI Search Optimisation & LLM Visibility
> Mass Media, 1 hour masterclass, afternoon slot (immediately before the "06:30 PM Thursday Night Party" entry)

**Track: "AI and Brand Citations"** (Syndicate 1&2, 03:30 PM) — the track name itself carries the set O-adjacent word "Citations" (not itself a set O/P alias term, but the three talks below discuss brand citation in AI answers directly):

> Tuhin Banik — It's Not Enough to be Cited: How AI Systems Draw Conclusions About Brands
> Jonathan Kiekbusch — Getting Cited Is the Easy Part: How to Change What AI Actually Says About You
> Chris Donnelly — What a billion sources teach us about getting mentioned & cited in AI

[note: the three "AI and Brand Citations" titles use "cited"/"cite" rather than the literal alias-list forms "citation rate" or "AI discoverability" — included here because the track name itself is a direct topical match on AI citation of brands, flagged as a track-level rather than title-level match, per the same treatment given to CMW's and MAICON's near-miss entries elsewhere in this cluster]

### Near-miss sessions checked and excluded (AI-search-adjacent, no literal set O/P alias phrase in title or track)

> Gintarė Rimolaitytė — Who AI Cites Now: How Source Patterns Shifted Since December 2025 (track: AI & Automation)
> Tom Wells — All Mentions are not created equal in AI search. (track: Understanding AI Search, 3:30 PM)
> Dixon Jones — Entity Maps: Brief AI Before It Briefs Itself (track: Understanding AI Search)
> Josh Blyskal — Owning the second layer of AI search
> Dhanya Nair — Beyond AI Search: 5 Ways Charities Can Win in a Fragmented Search Landscape
> Edward (Teddie) Cowell — No Clicks? No Rankings? No Problem: How AI Panic is Giving SEO a Seat at the C-Suite Table
> Judith Lewis — Schema in the AI Era: From Rich Results to Machine Interpretation

### Sponsor visibility (S8 bias note)

> The evening social event is "kindly sponsored by AirOps" — one sponsor name captured. A fuller sponsor list exists at the site's "Sponsors" nav section but was not fetched this pull. `unknown — checked brightonseo.com 2026-09-22` beyond AirOps.

## Pull notes — mechanical only

- Guessed URL `brightonseo.com/october-2026` 404'd; correct path found via the homepage's interactive-element listing: `brightonseo.com/events/october-2026`, then its "Explore the agenda" link to `brightonseo.com/events/october-2026/schedule-oct-2026`.
- `get_page_text` on the schedule page returned an unrelated sponsored evening-party blurb (likely a readability-extraction mismatch on this page's layout) rather than the schedule table; `javascript_tool` (`document.body.innerText`) was used instead and returned the full rendered text in one read.
- The rendered page appears to cover Day 1 (Thursday, October 8) only — it ends at the Thursday-night party entry and the same block repeats in the footer, with no Day 2 (Friday, October 9) session content anywhere in the captured 12,073-character text. Whether Day 2 requires a separate day-tab click (not attempted this pull) or a separate URL was not determined. **Session and match counts above are Day-1-only, not a two-day total.**
- Two ambiguous track attributions noted inline above (Sam Page's talk's exact track heading, and one earlier "AEO" cluster's precise sub-boundary) were not fully disambiguated from the surrounding running text; titles and speaker names are exact, track labels around them are best-effort.
- Did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com or amazon.com's assistant.
