# Semrush — customer success stories (AI-visibility-specific, screened and graded on intake)

```yaml
source:          Semrush
url_or_doc_id:   https://www.semrush.com/company/stories/sure-oak-ai-visibility/; https://www.semrush.com/company/stories/activate-digital-ai-visibility/
published:       undated on both pages
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP, MCP_DOCKER) — both pages are JS-rendered SPAs; a plain `curl` fetch returned only nav/footer chrome with an empty body, so `document.body.innerText` was read after full render
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from table default (5, vendor case study with n) — both stories disclose some numeric figures but no absolute calendar dates, no independent measurer, and one (Sure Oak) explicitly states a benchmarking screenshot used anonymized comparator names; per trust-rubric.md "vendor measuring the thing it sells, no third-party replication," bias flagged
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          Sure Oak case: ChatGPT, Google AI Overviews (both named). Activate Digital case: ChatGPT, Google AI Mode, Perplexity, "SearchGPT" (all named, verbatim as the customer quote states them)
metric_kind:     traffic (referral growth, lead share); visibility (AI Overview appearance growth)
supersedes:      none
captured:        full text of both stories
feature:         AI Visibility (feature name as used in both stories: "AI Visibility Toolkit")
```

## Verbatim

### Sure Oak — full text (condensed; nav/footer chrome elided per this cluster's convention)

"Sure Oak Drives New Leads from AI Visibility — When the rise of ChatGPT reignited the 'SEO is dead' debate, Andrea Schultz saw the opportunity in the AI search race as a new frontier."

Headline stats: 41% — MoM increase in referrals from ChatGPT. 286% — lift in Google AI Overview appearances. 40% — of all new leads now come through AI visibility.

About Sure Oak: "Sure Oak is an SEO agency built on measurable organic growth. Led by SEO Director Andrea Schultz, the agency recently pivoted to tackle AI-driven search from LLMs such as ChatGPT and Perplexity, and Google's AI Overviews."

The Challenge: "Potential clients were finding answers directly in AI-generated responses — and agencies not visible there risked losing market share." Stated goals: measure & improve visibility in ChatGPT and AI Overviews; show clients where they stood against competitors; adapt SEO strategies.

The Solution: "Sure Oak turned to Semrush... They began by benchmarking clients against competitors with the list of questions from the Narrative Drivers report... **Note: Client and competitor names have been anonymized for this example.** Next came AI-driven content recommendations... To prove results, Andrea leaned on the AI Visibility Toolkit's visual dashboards that revealed client sentiment and Share of Voice in AI search... Finally, they brought it all together in Looker Studio... The team was able to get the Sure Oak brand listed at the top of the AI Overview for super-relevant searches, like 'winning saas seo' and 'seo partner program.'"

Strategy quote: "We're consistently getting featured in Google AI Overviews as well as listed as sources on LLMs for recent blog content and conversion-oriented prompts using these strategies." — Andrea Schultz, SEO Director, Sure Oak. Listed tactics: schema implementation, HTML tagging/heading architecture, avoiding JS-heavy structures, TOCs and key takeaways, topic-cluster content, E-E-A-T enhancement.

The Results: "+41% MoM growth in ChatGPT referrals (July vs. June); +286% growth in Google AI Overviews appearances (May–June vs. July–August); 40% of all new leads now come directly through LLM visibility." "Not only are these leads more numerous — they're also higher quality. According to Andrea, prospects who discover Sure Oak via ChatGPT or AI Overviews tend to be more informed and further along in their decision-making journey."

**evidence_grade: Bronze** (on intake). Present: brand named (Sure Oak, real agency, not anonymized — only its comparison-dashboard example used anonymized data); engines named (ChatGPT, Google AI Overviews); a month-over-month percentage comparison naming specific months (July vs. June; May–June vs. July–August); intervention described in detail. Missing against the full seven-item bar: no year is stated for any of the named months (page is undated); no numeric baseline (percentages only, no underlying referral counts or lead counts); no sample size; no unaffected control metric; no independent measurer (Semrush wrote and published its own customer's story). The "40% of leads now come through AI visibility" claim is a referral-attribution figure, not an incrementality test — flagged per `trust-rubric.md`'s "referral traffic reported as influence" discard-on-sight criterion; kept and graded (not discarded outright) consistent with this cluster's treatment of other vendors' case studies, but the caveat is recorded explicitly here since it bears directly on how much this claim should weigh.

### Activate Digital / Dryer Vent Wizard — full text (condensed)

"Activate Digital Grows AI Visibility and Doubles Organic Traffic — Activate Digital Media used Semrush to boost AI visibility leads by 10% and double organic traffic. Now, they drive 10% of all franchise leads from AI search."

Headline stats: #1 — rankings achieved on AI Mode and ChatGPT. +10% — growth in leads coming from AI visibility in 60 days. 100% — boost in organic traffic. 10% — of leads now come from AI visibility.

Background: Dryer Vent Wizard, part of Neighborly Corporation (30+ home service brands); over 120 franchise locations.

The Challenge (quoted): "The problem with DryerVentWizard.com [was] that the organic traffic is quite low. For over 120 locations, the traffic was sitting flat at like 25,000–26,000 new organic users per month." — Jonathan Banks, Director at Activate Digital.

What They Did: Semrush's AI Visibility tool surfaced customer questions asked in Google and AI platforms plus synthesized answers, letting the team "reverse engineer" competitor content. One opportunity (dryer error codes) was pursued: a competitor blog was "pulling in an estimated 12,000 monthly visits on the topic"; Activate Digital built a comprehensive resource and localized it across 100+ franchise sites.

The Results (within two months, per the page's own framing): "#1 rankings on ChatGPT and AI Mode for priority queries"; "10% increase in leads from AI visibility"; "Organic traffic doubled, jumping from 25K to over 50K monthly users"; "10% of all franchise leads now coming from AI search engines like ChatGPT, Perplexity, and SearchGPT." Quote: "Every one of these locations locally is now ranking for error codes. The traffic is now almost doubling because of the content that we're adding now. In addition, 10% of the leads across 100 locations are now coming from AI sources, including Perplexity in Search GPT." — Jonathan Banks, Director at Activate Digital.

Secondary effect noted: the same customer-question insights informed "35 commercials for Meta, LinkedIn, and TikTok" within two months — an advertising-strategy spillover, not itself an AI-visibility metric.

**evidence_grade: Bronze** (on intake). Present: brand named (Activate Digital / Dryer Vent Wizard); engines named (ChatGPT, AI Mode, Perplexity, and "SearchGPT" as the customer's own term — not a Semrush or industry-standard engine name, kept verbatim); numeric baseline and post figures for organic traffic (25K → 50K+ monthly users, a genuine before/after pair); a relative date window ("within two months," "in 60 days"). Missing against the full seven-item bar: no absolute calendar date (no year or specific start/end date stated); no sample size beyond the customer's own scale (120+ locations); no unaffected control cohort; no independent measurer. Traffic and lead-share claims only, no revenue figure — Bronze, not Silver, for lack of a control metric.

## Pull notes — mechanical only

- Both pages required the Playwright MCP browser (`mcp__MCP_DOCKER`) after a plain `curl` fetch returned only site chrome with no article body — these are client-side-rendered pages. claude-in-chrome extension reported "not connected" at task start; used the Playwright fallback per task instructions, from a dedicated tab that did not touch another agent's open tab (`courtlistener.com`, observed passively, not interacted with) in the same shared browser instance.
- A third named case, "Coalition Technologies boosts AI traffic and conversions," was linked from the AI Visibility feature page (`semrush.com/company/stories/coalitiontechnologies/`) but not opened this pull — counted as screened, not graded. `unknown — checked semrush.com/features/ai-visibility (teaser only) 2026-09-22` for its full figures.
- Neither story states a publication or "results as of" date; both are recorded `published: undated` per the raw-pull template's rule, even though both name specific months for their percentage comparisons.
