# Search Party Podcast Episode 5 — Josh Peacock on SEO career levels and hiring trends

```yaml
source:          Search Party Podcast (YouTube channel: Search Party Podcast)
url_or_doc_id:   https://www.youtube.com/watch?v=L_TuQmnmYnA
published:       2026-04-16
pull_date:       2026-09-23
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            5
tier_reason:     guest (Josh Peacock) is founder/CEO of Search for Hire and the SEO Salary Guide — a vendor of the salary data he is presenting; figures are the vendor's own dataset, self-promoted on his own product. Bias flagged.
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        section "description and chapters" — verbatim transcript not captured, see pull notes
```

## Verbatim

**Episode:** "SEO Salaries and Hiring Trends (2026) w/Josh Peacock | Search Party Episode 5"
**Show / channel:** Search Party Podcast
**Published:** 2026-04-16 (YouTube `uploadDate` meta tag)
**URL:** https://www.youtube.com/watch?v=L_TuQmnmYnA
**Views at pull:** 80 views, "5 months ago" (2026-09-23)
**Duration:** 39:55
**Speaker:** Josh Peacock, Founder & CEO, Search for Hire; creator of the SEO Salary Guide

### Full video description (verbatim)

> "Josh Peacock, Founder & CEO of Search for Hire and creator of the SEO Salary Guide, breaks down the latest data on SEO salaries, hiring trends, and in-demand skills.
>
> This conversation goes beyond surface-level career advice—diving into how the SEO industry is evolving, what companies actually look for when hiring, and how marketers can position themselves for long-term growth in an AI-driven landscape.
>
> Want to see exclusive Search Party footage and get access to more guest insights? Then join us at the Afterparty, a monthly newsletter full of actionable tips and previews on future episodes: https://forms.gle/tK3jbi5Zr2zoGU8MA
>
> Get the SEO Career Framework PDF: https://drive.google.com/file/d/16Z5T... [link truncated by YouTube UI]"

### Chapters (verbatim, as published — this is the episode's own career-ladder framework for SEO/AI-search roles)

> "00:00 — Introduction to Search Party
> 01:08 — Fun Facts About Josh
> 03:15 — Turning a Podcast Into a Book With AI
> 05:01 — The SEO Career Framework Explained
> 09:05 — Traditional SEO vs. AI-Native SEO
> 10:13 — 1) Entry-Level SEO Analyst
> 13:52 — 2) SEO Specialist Role
> 20:15 — 3) SEO Strategist: Skills and Responsibilities
> 24:31 — 4) SEO Manager: Leading Teams and Strategy
> 30:36 — 5) Director-Level SEO: Driving Business Impact
> 33:48 — 6) VP-Level SEO: Executive Leadership
> 37:50 — How to Use the SEO Career Framework
> 39:03 — Connect With Josh
> 39:43 — Closing"

[note: this chapter list is the episode's own stated structure for a six-level SEO/AI-search career ladder (Analyst → Specialist → Strategist → Manager → Director → VP), directly relevant to "new roles" framing, but the spoken content behind each chapter (tasks, KPIs, pay at each level) was not capturable — see pull notes. The same guest's own site (searchforhire.com/blog/seo-jobs-salaries-hiring-trends-in-2026/, pulled 2026-09-23 by web fetch, not part of this file's verbatim block since it is a blog pull, not audio/video) states: median SEO salary $92,500 (middle 50% $72,500–$125,000); AI-title roles median $113,625 vs. $89,438 without (27% gap); Director+ roles with AI command a $35,250 premium; 54.9% of job descriptions mention AI vs. only 11% of job titles; January 2026 was peak hiring month with 395 unique roles posted. These figures are attributed to Josh Peacock / Search for Hire, not verified independently — flag carries to any compiled use.]

## Pull notes — mechanical only

- Access path: Playwright browser (MCP_DOCKER), not signed in.
- `ytInitialPlayerResponse.captions` confirmed an English auto-generated (ASR) caption track exists for this video. Repeated attempts to open the transcript engagement panel (via the sidebar "Show transcript" button, the description-embedded "Show transcript" button, and a close/reopen cycle, each with 2–4s waits) left `ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"]` present but with 0 transcript segments loaded (innerText only "In this video / Chapters / Transcript") — the same technique that worked on the Periscopify pull (f-roles-av-periscopify-geo-shortlist-2026-09-23.md) failed here; browser console showed additional errors on each retry, consistent with an intermittent YouTube-side block on the transcript-fetch XHR (separate from the api/timedtext PO-token block already documented). Direct `yt-dlp` extraction also failed (see the Periscopify file's pull notes for the general yt-dlp/PO-token wall, which applies identically here).
- Wall: verbatim spoken transcript not captured for this episode. Captured instead: full video description and full chapter list (both verbatim, direct from the YouTube page DOM), which is itself substantive (a named 6-level SEO/AI-search career framework).
