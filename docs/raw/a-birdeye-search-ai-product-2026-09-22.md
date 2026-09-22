# Birdeye — Search AI product page (product + method)

```yaml
source:          Birdeye (birdeye.com)
url_or_doc_id:   https://birdeye.com/search-ai
published:       undated on-page; site-wide banner references a newer launch ("Birdeye Launches AI Coworkers for Multi-Location Brands")
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; the three headline percentage stats on this page are discard-on-sight per `trust-rubric.md` ("percentage with no base") — flagged explicitly below, not silently kept as evidence of a number; the two testimonials are graded separately in `a-birdeye-customers-2026-09-22.md`
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        full page text, single fetch call, no truncation marker
```

## Verbatim

Site banner: "Birdeye Launches AI Coworkers for Multi-Location Brands — Find out more"

"# Jay diagnoses and fixes AI visibility, by location — Watch Demo — Tracks visibility across ChatGPT, Gemini, Claude, and more. Diagnoses what's costing you visibility. Fixes it by orchestrating multiple agents."

"## Tracking AI visibility is table stakes. Jay improves it across locations.

**30%** AI visibility increase
**53%** Increase in lead volume
**74%** Recommendations accepted"

**[DISCARD-ON-SIGHT FLAG]** — These three headline percentages carry no stated base, no brand, no date window, and no sample size — they match `trust-rubric.md`'s explicit discard-on-sight example ("Percentage with no base") verbatim in form. **Not usable as evidence of a number; recorded here only because they appear on the platform-primary product page itself, per `pull_purpose: evidence about a number` — the number in question is discarded, not the fact that the vendor displays it.**

Two testimonials (Shannon Novak, Arrow Senior Living; Pasjion Savage, Drucker and Falk) — reproduced and graded in `a-birdeye-customers-2026-09-22.md`.

"## Tracking AI visibility at a brand level is not enough
- **1,762 multi-location brands analyzed, across 16,240 location-level scans**
- 1 in 5 locations is invisible in AI search — absent, not just ranked low
- Up to a 50-point visibility gap between a brand's best and worst location
Read the report" [note: the "Read the report" link target was not resolved this pull — attempted `birdeye.com/ai-visibility-report`, HTTP 404; report not independently located]

"## From insight to action
### See your full AI search picture — Your visibility score and Share of Voice, by location, across ChatGPT, Gemini, Claude, and more.
### Know what's costing you visibility — Citations, accuracy, and website signals — the exact causes behind every score.
### Fix what matters most — Listings, blogs, FAQs, and reviews — generated and applied, ranked by impact."

"## One Marketing Coworker—you coach him, he orchestrates the rest
### See your full AI search picture — Track your **Visibility Score** and **Share of Voice** — at both brand and location level, across ChatGPT, Gemini, Perplexity, and more.
### Make sure no location is left behind on AI search — See which AI answers you appear in, which competitors get recommended instead, and why — for prompts like 'best [service] near me,' location by location.
### Know what's costing you visibility — See which sources AI engines cite in your category, whether you appear in them, and how your website holds up against AI optimization criteria.
### Fix what matters most — The AI Search Optimization Agent ranks every fix by impact, then deploys the right agent — content, listings, or reviews — to close it."

"## One visibility drop. Jay orchestrates every agent that can fix it. — For example — Riverside's visibility score drops behind a competitor for 'emergency dental care near me.' [note: 'Riverside' appears to be an illustrative/hypothetical example, not a named real customer — no case-study framing, no metric attached beyond the narrative]
- Finds what's causing it — The AI Search Optimization Agent traces the drop to a wrong listing field and a missing content theme.
- Fixes the listing — Summons the Listings Optimization Agent to correct the inaccurate field.
- Fills the content gap — Summons the Blog Page Agent to publish on the theme where visibility is weakest."

"### Jay does more than AI Search — AI Search is one job. He orchestrates agents across every marketing job you need done. Reviews, Listings, Social [each with one-line descriptions]"

"## Learn why Birdeye is ranked #1 on G2 in Enterprise. Get the Free Report"

"## Frequently Asked Questions" [note: rendered with no visible question/answer text — likely an interactive accordion that did not render in the fetch tool's simplified markdown]

**Named metrics:** "Visibility Score" and "Share of Voice" are the two named metrics tracked "at both brand and location level"; "Citations, accuracy, and website signals" are named as diagnostic sub-factors, not separately scored metrics on this page.

**Prompt-set / n / method disclosure:** the page names example query shapes ("prompts like 'best [service] near me'") and states tracking is "by platform, location, citation" but discloses **no n (prompt count), no run frequency, and no fixed prompt-set version** for the per-customer Visibility Score/Share of Voice tracking. The separate "1,762 multi-location brands analyzed, across 16,240 location-level scans" figure is disclosed **n for a category-wide research report**, not for the per-customer product methodology — same pattern seen for Yext's research page in this cluster. **Disclosure verdict: no** (for the product's own per-customer method) — `unknown — checked birdeye.com/search-ai 2026-09-22`.

## Pull notes — mechanical only

- Single fetch call, max_length 6000, full page captured without a truncation marker.
- The FAQ section's question/answer content did not render — `unknown — checked birdeye.com/search-ai 2026-09-22` for its content.
- The "Read the report" link (1,762 brands / 16,240 scans study) could not be resolved to a working URL this pull.
