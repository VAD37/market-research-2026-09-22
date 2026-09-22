# Sitefire — Jerry.ai case study, full dedicated page

```yaml
source:          Sitefire — case study "Using Sitefire, Jerry's AI referral traffic rose 78%"
url_or_doc_id:   https://sitefire.ai/case-studies/jerry
published:       undated — no publish date on page; case covers "March through July" 2026 (interventions "between April and June 2026"), year inferred from the page's own "GPT-5.4 release" reference and from `docs/raw/a-sitefire-*-2026-09-22.md` (Sitefire founded 2025, YC W26)
pull_date:       2026-09-22
pull_method:     fetch (plain curl, no browser extension used)
pull_purpose:    evidence about a number
tier:            5 — vendor-reported case study, n and date window stated, no independent third-party replication (table default per `../method/trust-rubric.md` tier 5: "vendor or agency study with n, dates, method")
tier_reason:     table default; not adjusted — method (control-page comparison, indexing approach) is disclosed in the page's own "Methodology" section, which is why this sits at 5 rather than 6
source_label:    vendor-reported
lane:            E, F
sub_market:      organic recommendation
engine:          "AI models" / "AI Search" generic on this page; the only specifically named engine is "GPT-5.4" (named as the cause of a March traffic disruption, not as the target of Jerry's optimization). ChatGPT, Gemini, Perplexity, Claude appear only in unrelated site-wide product-feature copy elsewhere on the same page (JSON feature blocks at "AI Monitoring" / "Track which prompts mention you across ChatGPT, Gemini, Perplexity, and Claude"), not inside the Jerry case narrative itself
metric_kind:     visibility, traffic
vertical:        high-CPA regulated — insurance, as the source names it ("Jerry wanted to know where AI models were sending insurance shoppers"; Jerry.ai's own tagline on the page: "The first AI-powered advisor to manage all your physical assets")
evidence_grade:  Bronze. Seven bar items ticked from this page:
                 1. Brand — YES: Jerry (Jerry.ai), named and described
                 2. Engine — NO (missing): no specific engine (ChatGPT/Gemini/Perplexity/Claude) is named inside the case narrative; only "AI models" generically, plus "GPT-5.4" as an external disruption event, not as the optimization target
                 3. Date window, absolute — YES: "shipped the changes in two waves between April and June 2026"; charts run "March through July" 2026; headline comparison is "the three months after the first improved pages went live" vs. "the three weeks before"
                 4. Baseline — YES: "the three weeks before" the first improved pages went live; and "each group's own level before the March [GPT-5.4] update" for the bot-traffic chart
                 5. Intervention — YES: "Sitefire mapped the topics worth competing for... Jerry's team shipped the changes in two waves," described as clearer structure, more direct answers, better-sourced data on already-live pages
                 6. Sample size / traffic volume — NO (missing): every figure is a percentage (+78%, +56%, +27%, +9%, 112% vs. 72% of pre-update level); no absolute visit count, click count, or n of pages/prompts disclosed on this page (a "comparable set of pages" is named as the control cohort but never sized)
                 7. Who measured, paid by outcome — PARTIAL: measured by Sitefire (vendor) using Jerry's own site analytics ("own server logs and analytics" per `../a-sitefire-customers-2026-09-22.md`'s framing of the same relationship); not an independent third party. Paid-by-outcome: not stated anywhere on this page
                 Per grading rule 1 (`../method/plan-review-1-2026-09-22.md` §3, `../method/plan.md` "Evidence bar — grading rule 1"): missing items 2 and 6 caps this at Bronze despite the page disclosing an explicit unaffected-control cohort (item satisfying Silver's "baseline plus an unaffected control metric" standard on its own) — the missing-item cap controls per rule 1's own text ("a case missing any of items 1-7 is Bronze at best")
direction:       positive (all four headline metrics — AI referral traffic, AI bot traffic, AI citation share, AI visibility — reported as increases; the page frames a March GPT-5.4-driven traffic drop as a confound the intervention outperformed, not as a negative result of the vendor's own program)
paid_by_outcome: unknown — not stated on this page
supersedes:      none
captured:        full page — single fetch, reached the footer ("Get started with Sitefire" / site nav), no truncation. The page is a Next.js client-rendered app; the plain-text extraction below is regex-stripped HTML/JSON-LD, not a browser-rendered DOM read — chart labels and axis values may be incompletely captured where they are rendered as SVG or canvas rather than text (see Pull notes)
```

## Verbatim

Page title: "Using Sitefire, Jerry's AI referral traffic rose 78% - Sitefire"

"Jerry.ai — The first AI-powered advisor to manage all your physical assets"

"Using Sitefire, Jerry's AI referral traffic rose 78%. Jerry wanted to know where AI models were sending insurance shoppers, and what it would take to get Jerry's own pages into those answers. Sitefire mapped the topics worth competing for, then showed page by page what was keeping Jerry out of them."

"Jerry's team shipped the changes in two waves between April and June 2026. The recommendations helped the team produce content with clearer structure, more direct answers, and better-sourced data on pages that were already live. Every measure rose as a result. And because Jerry left a comparable set of pages untouched, there's a clean read on how much of the lift was Sitefire's insights and how much was the market moving on its own. The gap between them is the Sitefire effect."

"+78% AI referral traffic — Clicks to jerry.ai from AI answers.
+56% AI bot traffic — Requests from AI models fetching Jerry's pages.
+27% AI citation share — Jerry's citations as a share of all AI citations.
+9% AI visibility — Share of AI answers mentioning Jerry.
Each figure compares the three months after the first improved pages went live with the three weeks before."

"Singling out the Sitefire effect. In early March, a GPT-5.4 release cut AI bot traffic across the web, and this also affected Jerry. To recover traffic, Jerry used Sitefire to improve a selected set of pages, while keeping the rest untouched. The results are shown below: Weekly AI bot traffic, March to June. Each group shown against its own level before the March update. [chart: improved pages / pages Jerry did not touch / GPT-5.4 release / improved pages went live] Following the changes in April, the improved pages recovered quickly from the GPT model update, drove up AI traffic and referrals, and ended up at an average of 112% of their pre-GPT model update level, compared to only 72% for untouched pages."

"Sitefire tip: AI models re-crawl on their own schedule, so the numbers don't move the day you publish. Expect a lag of a few days to a few weeks before the changes show up."

"Why measure AI bot traffic and referrals? AI visibility is the score you optimize against, but it's calculated from a synthetic prompt set that someone had to choose. That choice is a hypothesis about what your customers ask, and a hypothesis can be wrong. Traffic, on the other hand, is the ground truth. When referrals and bot activity move in line with visibility, the prompt set is tracking what real people are actually asking. When they don't, the problem is the prompts, not the pages."

"Jerry is spearheading the new era of agentic marketing. Using Sitefire, Jerry runs a continuous loop: find the prompts its customers ask AI, see where the gaps are, then fix those pages and publish. Diagnose. Sitefire researches which prompts are worth focusing on, then shows which brands the answers mention and which pages the models cite. Improve. For each topic, Sitefire agents research what's working, then return one prioritized brief per page with line-by-line improvements. Jerry's writers review the changes and publish. Measure. Sitefire tracks Jerry's position on those prompts, and how AI bot and referral traffic respond to the edited pages. Using Sitefire agents, Jerry can run this loop multiple times a day. Sitefire produces the briefs; Jerry writes and edits the content."

"'Sitefire showed us which pages actually mattered for GEO and what each one was missing. The goal was never to publish more - we already have a pretty strong content production engine. Instead, we wanted to make the pages we already had get trusted and cited by the LLMs.' — Ida Sultan, Chief of Staff, Jerry"

"Jerry's AI visibility and citation share have risen every month since March. Sitefire measures visibility and citation share against Jerry's prompt set. The charts run March through July, so they cover the weeks before the first improved pages went live as well as the months after. AI visibility: Share of AI answers mentioning jerry.ai, weighted by how much each prompt matters. [chart values, read from axis labels: 3% 4% 5% 6%, Mar-Jul]. Citation share: Jerry's share of every web page cited across those answers. [chart values: 2% 2.5% 3% 3.5%, Mar-Jul]."

"The bottom line. Using Sitefire, Jerry turned their articles into content AI models cite consistently."

"Methodology. The headline figures. Each compares the three months after the first improved pages went live with the three weeks before. Those three weeks fall after the March update, so the comparison chart indexes every week to the pre-update level instead. The comparison. The pages Jerry improved against comparable pages on the same site that Jerry did not touch, over the same weeks. The two groups did not fall equally in March, so each is indexed to its own level before the update and read against that level rather than against the other group. The chart runs March to June. AI bot traffic counts AI models fetching a page to build an answer to a live prompt. AI referral traffic is a floor, not a ceiling: many buyers research inside the model and then navigate directly, so they never appear as referral traffic at all. AI visibility and citation share are measured against a set of prompts fixed at onboarding and never changed, so later comparisons stay meaningful. Definitions at sitefire.ai/docs/kpis."

[note: the two line/bar charts ("Weekly AI bot traffic, March to June" and the AI-visibility / citation-share trend charts) render as SVG/canvas in the live page; only axis-label percentages were recovered by the regex text-extraction pull method used here — individual weekly data points are not captured, only the axis scale and the two summary comparison numbers (112% vs. 72%) stated in prose]

## Pull notes — mechanical only

- Fetched via plain `curl` (no browser extension, no Playwright — fetch-only per this task's constraints), URL `https://sitefire.ai/case-studies/jerry`, HTTP 200, no redirect.
- Page is a Next.js client-rendered app; HTML was regex-stripped to text (script tags, CSS custom-property blocks, and cookie-consent theming boilerplate make up roughly two-thirds of the raw file size before stripping — none of that content is reproduced above).
- Cross-checked against `docs/raw/a-sitefire-customers-2026-09-22.md` (the vendor's homepage teaser for the same case, pulled 2026-09-22 by a different task): the homepage names the same two headline figures (+78% AI referral traffic, +56% AI bot traffic) and grades the case Bronze from the teaser alone. This full-page pull adds: the explicit April-June 2026 intervention window, the "three weeks before" baseline, the named unaffected-control cohort ("a comparable set of pages... untouched"), the GPT-5.4 traffic-disruption context, and the two additional metrics (AI citation share +27%, AI visibility +9%) — none of which appear on the homepage teaser. The added detail does not change the grade (still Bronze) because the two items that cap it — a specifically named engine and any absolute sample size — are absent from both the teaser and the full page alike.
- This case was not among the 12 rows P4-c4 pulled (`docs/raw/e-case-census-c4-2026-09-22.md` — that cluster's Sitefire row covered only Pointhound, graded Silver on the full page). Jerry.ai was pulled fresh by this task (P4-c10) because it is the vertical-relevant Sitefire case (insurance) that P4-c4 did not cover.
- No independent verification of Jerry's underlying analytics was possible or attempted; the case is Sitefire's own retelling of the customer's data per the "Methodology" section, consistent with every other case in this vendor's roster (`docs/raw/a-sitefire-customers-2026-09-22.md`).
