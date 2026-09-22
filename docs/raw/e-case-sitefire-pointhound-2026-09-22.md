# Sitefire — Pointhound case study

```yaml
source:          Sitefire — case study "How Pointhound used Sitefire to grow site visits from AI Search by 300%"
url_or_doc_id:   https://sitefire.ai/case-studies/pointhound (visited via https://www.sitefire.ai/case-studies/pointhound, redirected to the bare domain)
published:       undated — no publish date on page; the "METHODOLOGY" section states an absolute measurement window (see below)
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome, own dedicated tab)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     discloses an absolute date window, explicit per-metric measurers (Pointhound's own GA4 and CDN server logs; Sitefire's own tracked question set), and an explicit unaffected-control comparison ("new content" vs. "rest of site" AI bot traffic) — the most complete method disclosure of any case pulled in this task; capped at 5, not higher, because the measurers are the vendor (Sitefire) and its own customer (Pointhound), with no independent third-party replication, per trust-rubric.md "vendor measuring the thing it sells"
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT named explicitly in body text; methodology section additionally names "ChatGPT-User, Perplexity-User, Claude-User" as the specific AI-crawler user-agents counted for the AI-bot-traffic metric — the most explicitly engine-attributed case pulled in this task
metric_kind:     traffic (site visits from AI Search, AI bot traffic — both percentage-change and charted) and visibility (Visibility Score, Citation Share — both vendor-defined sub-metrics with explicit before/after percentages)
supersedes:      none
captured:        full page — single call, reached the "METHODOLOGY" section at the page's end, no truncation
vertical:        none named as an industry-vertical label; Pointhound is described as "Award flight search - book flights with points" (a travel/loyalty-points booking service)
evidence_grade:  Silver (full-page, on this pull) — upgraded from the Pass 3 teaser-level grade. All seven bar items evaluated below.
pass3_grade:     Bronze (from `docs/raw/a-vendor-census-c1-2026-09-22.md`, graded off the homepage teaser — `docs/raw/a-sitefire-customers-2026-09-22.md`, which explicitly did not open this dedicated page: "the two 'See how X did it' links were not individually followed this session")
paid_by_outcome: unknown — quote below; the relationship described throughout ("Using Sitefire, Pointhound...") is a vendor-customer platform relationship, with no fee structure disclosed
prompt_set_disclosed: partial — "Sitefire's tracked question set: award-travel prompts fixed at onboarding, evaluated on the same models throughout" is disclosed as a method (a fixed, versioned set, not ad hoc), but no n of prompts and no prompt wordings are published
```

## Verbatim

Eyebrow: "POINTHOUND.COM — Award flight search - book flights with points"

Title: "How Pointhound used Sitefire to grow site visits from AI Search by 300%"

"More people ask an AI model how to book flights with points than ever before. Using Sitefire, Pointhound identified which of those questions it could win and created AI-optimized content for them. Within three months that content went from zero to nearly half of all AI bot traffic to the site, and Pointhound began appearing in AI answers where it had been absent. Every headline number comes from Pointhound's own server logs and analytics."

**Headline stat tiles (verbatim):**
- "+300% more site visits from AI Search — People clicking from an AI answer onto pointhound.com, since the new content went live. Measured in Pointhound's GA4."
- "+294% more AI models reading Pointhound's pages — Real-time fetches by AI models reading a page to answer a live question, since the new content went live. From Pointhound's CDN server logs."
- "~45% of all AI bot traffic is the new content — Up from zero. The content Pointhound created with Sitefire is now the most-fetched on the whole site."
- "0 → 1.0% Citation Share, from a standing start — Pointhound now appears in AI answers to the tracked award-travel questions. Measured in Sitefire."

**THE WORK — "Using Sitefire, Pointhound found where it could win and created the content":** "Award travel is confusing, and more of the people trying to figure it out now start with ChatGPT instead of Google. Pointhound is best positioned to be the answer those AI models give. Using Sitefire, Pointhound ran multiple GEO optimization loops. At each turn, Sitefire agents identified where award-travel questions were being answered across ChatGPT and other AI models, and in which topics Pointhound had the strongest claim to win. Pointhound then turned those insights into SEO and GEO optimized articles. Across the spring, Pointhound shipped three waves of content this way."

**The loop:** "1. Identify — Sitefire's agents map which award-travel questions AI models answer, and which of them Pointhound is best placed to win. 2. Create — Using Sitefire, Pointhound turns those insights into SEO and GEO optimized articles, built on its own brand voice. 3. Publish — Pointhound ships the wave, measures what the models read, and the loop starts again."

Quote: "With Sitefire, we ship articles we're actually proud to publish. No other tool got us there." — Jay Reno, Pointhound.

**THE RESULTS — "Every signal up since the content went live":** "Four signals, week by week, from late February to the end of June. The dashed vertical lines mark the three waves of content Pointhound published; the first went live on March 14. The first two charts come from Pointhound's own systems: CDN server logs and GA4 analytics. The other two come from Sitefire. Visibility Score is the share of AI answers on a tracked set of award-travel questions that mention pointhound.com. Citation Share is pointhound.com's citations as a share of all citations in those answers."

Chart 1 — "Site visits from AI Search +300%, per week, against the pre-launch week": "People who clicked out of an AI answer onto pointhound.com. Four times their earlier level by the end of June." (indexed 0x-4x, weekly points Feb 23, Mar 16, Apr 6, Apr 27, May 18, Jun 8, Jun 29)

Chart 2 — "AI bot traffic +294%, per week, against the pre-launch week": "The real-time fetches AI models make when they read a page to answer a live question, from Pointhound's CDN server logs." (same indexed 0x-4x scale, same weekly points)

Chart 3 — "Visibility Score 0 → 1.0%, share of tracked answers": "The share of AI answers on tracked award-travel questions that mention pointhound.com, from a standing start." (0.0%-1.2% scale, same weekly points)

Chart 4 — "Citation Share 0 → 1.0%, pointhound.com's share of cited sources": "pointhound.com's citations as a share of all citations in those answers, climbing as each wave of content came online." (0.0%-1.2% scale, same weekly points)

**THE CONTROL — "The new content against the rest of the site":** "The content Pointhound created with Sitefire now accounts for nearly half of its AI bot traffic, up from zero. The single most-fetched page on the whole site is now one of those articles." Chart, "AI bot traffic by page group, per week, against the pre-launch week", two series labelled "new content" and "rest of site": "The same metric as above, split by page group. The orange band is the content Pointhound published with Sitefire; it starts at zero and grows to roughly half the total." "Content that did not exist in March is now nearly half of what AI models read on the site. The rest of the site did not have to shrink for that to happen - the new content grew the total."

**IN SHORT:** "Using Sitefire, Pointhound identified the award-travel questions it could win in AI answers and created AI-optimized content for them. That content now accounts for nearly half of the site's AI bot traffic, site visits from AI Search grew 300%, and Pointhound now appears in AI answers where it had been absent - all measured in Pointhound's own logs and analytics. If your buyers are asking AI models about your category, the answers are already being written from someone's content. Sitefire shows you which questions you can win, and turns them into the content that wins them."

**WHAT COMES NEXT:** "Using Sitefire, Pointhound continues to identify new questions its customers ask and turn them into content, further growing its traffic from AI Search." Quote: "We're not slowing down. This is where our customers are searching now." — Jay Reno, Pointhound.

**METHODOLOGY (verbatim, in full):** "Windows. Weekly charts run February 23 to June 29, 2026. The first content went live March 14, with further waves in April and June. Headline changes compare the last full week before that first content went live with the most recent week, for every metric. AI bot traffic comes from Pointhound's own CDN server logs and counts the agents that read pages to answer live questions (ChatGPT-User, Perplexity-User, Claude-User). Indexing and training crawlers are excluded. Shown as change against the pre-launch week. Site visits from AI Search (AI referral traffic) come from Pointhound's GA4 and are a floor: most AI-influenced readers research inside the model and then navigate directly, and clicks from Google's AI Mode arrive with a plain google.com referrer. Sitefire metrics. Visibility Score and Citation Share come from Sitefire's tracked question set: award-travel prompts fixed at onboarding, evaluated on the same models throughout (definitions at sitefire.ai/docs/kpis)."

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension (connected this session), `get_page_text` on a dedicated new tab (tabId 1697684063) opened for this task. Full page captured in one call, reached the "METHODOLOGY" section at the page's end, no truncation.
- This page is substantially more detailed than Sitefire's homepage teaser that Pass 3 graded from (`docs/raw/a-sitefire-customers-2026-09-22.md`), which explicitly recorded that the "See how Pointhound did it" link was not followed that session. This full page discloses an absolute date window, a named control comparison, and per-metric measurer attribution — none of which appear on the homepage teaser.
- Chart values for site visits and AI bot traffic are given only as indexed multiples of the pre-launch week (0x-4x scale), not as absolute visitor or fetch counts — no raw traffic number is disclosed anywhere on the page for either metric.
- No n (count of tracked prompts) is disclosed for "Sitefire's tracked question set" — only that it is "fixed at onboarding" and "evaluated on the same models throughout," i.e., a versioned, non-ad-hoc set, but without a stated size.
- No statement anywhere on the page of who was paid by the outcome, or of any performance-based fee structure — every measurement is attributed either to Pointhound's own first-party tools (GA4, CDN logs) or to Sitefire's own tracked-question-set product, with no named independent third-party auditor for either.

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Present** | "POINTHOUND.COM — Award flight search - book flights with points" |
| 2 | The engine or engines | **Present** | "more of the people trying to figure it out now start with ChatGPT instead of Google"; methodology: "counts the agents that read pages to answer live questions (ChatGPT-User, Perplexity-User, Claude-User)" |
| 3 | The date window, absolute | **Present** | "Weekly charts run February 23 to June 29, 2026. The first content went live March 14, with further waves in April and June." |
| 4 | The baseline before intervention | **Present** | "Visibility Score 0 → 1.0%"; "Citation Share 0 → 1.0%"; "Headline changes compare the last full week before that first content went live with the most recent week" |
| 5 | The intervention itself | **Present** | Three-step "loop": "Identify" (Sitefire agents map winnable questions), "Create" (SEO/GEO-optimized articles), "Publish" (ship and re-measure); "three waves of content" |
| 6 | The sample size, or the traffic volume | **Absent** | Traffic shown only as indexed multiples ("0x-4x") of the pre-launch week, never as an absolute visitor or fetch count; no n given for the tracked question set behind Visibility Score/Citation Share |
| 7 | Who measured, and whether they were paid by the outcome | **Partial** | Measurer named per metric: "Measured in Pointhound's GA4"; "From Pointhound's CDN server logs"; "Measured in Sitefire." No statement anywhere of whether Sitefire or any party was paid by the outcome |

**Full-page grade: Silver.** Present: named brand, three named engines (the most explicit engine attribution of any case pulled in this task, via named crawler user-agents), an absolute calendar date window (the first found across every case in this cluster with a specific start and end date, not merely a relative duration), explicit numeric baselines across four separate metrics, a described three-step intervention, and — the item that clears Silver — an **explicit unaffected control comparison**: "THE CONTROL — The new content against the rest of the site," splitting AI bot traffic by page group ("new content" vs. "rest of site") and showing the new-content share grow from zero to roughly half while stating "the rest of the site did not have to shrink for that to happen." Missing against the full seven-item bar: item 6 (traffic shown only as relative multiples, never an absolute count or n) and full disclosure on item 7 (measurers are named per metric, but both are first-party — the customer's own analytics, and the vendor's own tracked-question-set product — with no independent third party, and no statement on paid-by-outcome). Not Gold: the control is an observational before/after comparison between page groups on the same site, not a holdout, geo-split, or switchback design.

**Grade change vs. Pass 3: UP (Bronze → Silver).** Pass 3 graded this case Bronze from Sitefire's homepage teaser alone (`docs/raw/a-sitefire-customers-2026-09-22.md`: "+300% site visits from AI Search"), explicitly recording that the case's own dedicated page ("See how Pointhound did it") was not opened that session. This full-page pull finds the dedicated case-study page discloses an absolute date window and an explicit unaffected-control comparison that the homepage teaser did not carry at all — the two items that separate Bronze from Silver per `glossary.md`. This is the first grade change (upward) found in this task's re-grading of the eight cases pulled so far from Bronze- or Silver-tagged vendors.
