# MozCon 2026 roadshow — London edition — schedule

```yaml
source:          Moz (moz.com)
url_or_doc_id:   https://moz.com/mozcon/schedule ; https://moz.com/mozcon
published:       undated on the pages themselves; London date given as "Nov 13" on a promotional banner elsewhere on the site (year not restated on that banner, inferred 2026 from the page's own title "MozCon 2026 Schedule" and site framing "we're back on the road in 2026")
pull_date:       2026-09-22
pull_method:     browser (claude-in-chrome, dedicated tab); get_page_text sufficed for both pages
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — conference's own schedule page, reliable on existence (session titles, speakers, employers), biased on framing
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full page text (get_page_text) of moz.com/mozcon (overview/speakers) and moz.com/mozcon/schedule (London-day agenda). A site-level instruction attached to this domain during the pull directed that substantial verbatim portions of moz.com content not be reproduced; abstracts below are therefore paraphrased rather than quoted at length, and only short factual fragments (titles, short phrases under 15 words) are quoted directly. This is a deviation from this repo's normal raw-pull convention of verbatim capture, made to comply with that instruction — see pull notes
```

## Verbatim (session titles, speakers, and short factual fragments only — abstracts paraphrased per the note above)

### Event framing

MozCon has moved to a multi-city "roadshow" format for 2026 rather than a single annual US event; a London date (November 13, per the site's promotional banner) is confirmed live, alongside a New York date referenced by a tab on the schedule page (content for New York was not shown — the schedule page defaults to London and no New York-specific session list rendered in this pull). The site's own page title frames the event as covering "SEO, AI Search, and GEO." The 2026 headline sponsor named on the overview page is **Profound**, an AI-visibility vendor already rostered in this research programme's Pass 3 vendor census.

### London day schedule — full session list, titles verbatim, abstracts paraphrased

| Time | Title (verbatim) | Speaker | Employer |
|---|---|---|---|
| 9:00–9:20 AM | Opening Remarks | Willow Mack | Moz |
| 9:20–9:50 AM | "What if Google Wins the War?" | Dr. Pete Meyers | Moz |
| 9:50–10:20 AM | "How to Use Topical Reasoning to Optimize for Humans and Machines" | Beatrice Gamba | Wordlift |
| 10:20–11:00 AM | Morning Coffee Break + Networking | — | — |
| 11:00–11:30 AM | "Why Great SEOs Struggle To Become Business Leaders (And How To Change It)" | Helen Pollitt | Getty Images |
| 11:30 AM–12:00 PM | "Building Attribution That Survives AI Interference" | Stephen Akadiri | (independent) |
| 12:00–1:15 PM | Lunch Break + Networking | — | — |
| 1:15–1:45 PM | "How to Scale Impactful Content Without Losing Quality" | Chima Mmeje | Moz |
| 1:45–2:15 PM | "Why the Best Digital PR Campaigns Don't End With Links" | Katy Powell | Bottled Imagination |
| 2:15–2:50 PM | Afternoon Break & Networking | — | — |
| 2:50–3:20 PM | **"Citation Needed: Linking AI tactics to real results"** | Tom Capper | Moz |
| 3:20–3:50 PM | "How to Win at Agentic E-Commerce" | Miracle Inameti-Archibong | John Lewis (Financial Services) |
| 3:50–4:20 PM | "How to Make Smart Bets on the Future of Search" | Mark Williams-Cook | Candour |

**Total session count: 13 titled agenda entries** (9 substantive talks including Opening Remarks, plus 3 break/networking blocks; London day only — no New York-specific list was captured this pull).

### Sessions matching set O / set P terms

**1 of 13 title-level match:** Tom Capper's "Citation Needed: Linking AI tactics to real results." The title itself carries "Citation," and — paraphrasing rather than quoting the abstract per the site restriction noted above — the session description explains that AI-answer citation data can offer a form of tactical proof that traditional SEO attribution has lost, and that the talk covers trends in citation data across AI platforms and how to use citation counts as evidence of impact.

**1 further abstract-level near-match, not a title match:** Beatrice Gamba's "How to Use Topical Reasoning to Optimize for Humans and Machines" — paraphrasing its abstract: the talk argues that keyword-first site structures produce weak entity signals, and that organizing content around clear entity relationships instead improves engagement, topical coverage, and (in the source's own two-word phrase) "AI citations." That two-word phrase is the only literal alias-adjacent term in this session's abstract; the title itself carries no alias term.

No set P (paid placement) alias term appears anywhere in the captured London-day schedule.

## Pull notes — mechanical only

- `moz.com/mozcon` is the overview/speaker-bio page; `moz.com/mozcon/schedule` is the separate day-by-day agenda, reached via the interactive-element listing (`/mozcon/schedule` link found among the site's own nav links, not obviously advertised on the overview page's visible text).
- A tab control for "New York" exists on the schedule page alongside "London"; this pull captured only the default-rendered London content — the New York tab was not clicked, so no New York MozCon 2026 session list is recorded here. `unknown — checked moz.com/mozcon/schedule 2026-09-22, London tab only`.
- **Copyright note:** a reminder attached to this browsing session instructed that substantial portions of moz.com's content not be reproduced verbatim. In compliance, this file paraphrases session abstracts rather than quoting them at length, in contrast to the verbatim-capture convention used for every other file in this cluster (MAICON, ANA, CMW, SMX, brightonSEO, GEO Conference). Session titles and the table of speakers/employers/times above are treated as short factual data (not creative prose) and are reproduced directly. Two short descriptive phrases ("AI citations"; general sense of the Citation Needed abstract) are paraphrased, not quoted.
- Did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com or amazon.com's assistant.
