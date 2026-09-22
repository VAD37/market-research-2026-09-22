# Quattr — case study — Kiteworks ("79% More Answer Engine Citations")

```yaml
source:          Quattr, Inc. (quattr.com/case-studies index card; dedicated case page link did not resolve to a distinct URL this pull — see pull notes)
url_or_doc_id:   https://www.quattr.com/case-studies (card text, fetched today); proof-index summary also at docs/raw/a-quattr-method-2026-09-22.md
published:       undated
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome), own dedicated tab
pull_purpose:    evidence about a number
tier:            6
tier_reason:     table default — vendor-reported, Quattr is the measuring party, no independent replication; graded from the case-studies index card text (a fuller-than-teaser summary, not the customer-index-only teaser Pass 3 used, but short of the dedicated case page which did not resolve this pull)
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          Google AI Overviews (named explicitly)
metric_kind:     visibility (AI Overview citations); traffic (indexed pages)
supersedes:      none
captured:        case-studies index card text (headline + three stat callouts), full page fetched today; the dedicated "Read Case Study" sub-page link did not navigate on click this pull — recorded as a pull limitation, not as evidence the page does not exist
pass3_cluster:   a-vendor-census-c4 Part A row 3 (Quattr) — "Kiteworks — screened via the AI Visibility Proof Index only (not independently opened)... evidence_grade: Bronze (on intake, from the proof-index summary alone)"
pass3_grade:     Bronze (from the proof-index teaser, not the case's own page)
vertical:        none named on this card
paid_by_outcome: unknown — not disclosed
prompt_set_disclosed: no — not disclosed on this card
```

## Evidence bar — seven items ticked (from today's case-studies index card, fuller than the P3-c4 proof-index teaser)

1. **Brand** — Kiteworks. Quote: "Kiteworks replaced over 53,000 static links with a dynamic, AI-powered link graph, reversing a site-wide indexation decline and winning the new era of AI-driven search." — SATISFIED
2. **Engine(s)** — Google AI Overviews, named explicitly: "79% more citations in AI Overviews." — SATISFIED
3. **Absolute date window** — "within six weeks" for one sub-metric; no calendar dates. — NOT SATISFIED
4. **Baseline** — not stated numerically; qualitative "site-wide indexation decline" before. — NOT SATISFIED
5. **Intervention** — dynamic AI-powered link graph replacing 53,000+ static links. — SATISFIED
6. **Sample/traffic volume** — "over 53,000 static links" replaced (a scale figure for the intervention, not a traffic/citation-count n). — PARTIAL
7. **Who measured, paid-by-outcome** — Quattr (vendor); not independent; paid-by-outcome not disclosed. — NOT SATISFIED

## Verbatim

"79% More Answer Engine Citations — Kiteworks replaced over 53,000 static links with a dynamic, AI-powered link graph, reversing a site-wide indexation decline and winning the new era of AI-driven search. Read Case Study — 79% more citations in AI Overviews. 30% increase in indexed pages. 22% jump in keywords ranking in positions 1-3 within six weeks."

Separately, from Kiteworks' second Quattr case on the same index ("4x Increase in Non-Brand Traffic"): "Kiteworks scaled its content strategy using Quattr's AI-driven workflows and Autonomous Linking API, quadrupling non-brand traffic and significantly increasing qualified leads from demo and contact form fills... 300% increase in non-brand traffic in 19 months. 2.5x monthly increase in producing SEO-optimized content. 2x increase in demo and contact us form fills." [note: this second Kiteworks case names no AI engine and is classical organic/lead traffic — not graded as Lane E evidence, screened only, per the same rule applied to AirOps's classical-SEO cases in this cluster.]

## evidence_grade: **Bronze** (same as Pass 3, now confirmed from a fuller index-card text naming Google AI Overviews explicitly rather than the proof-index's engine-unspecified teaser)

Visibility-only (AI Overview citations), no revenue link, no control cohort, no independent measurer. Missing items 3, 4, 7.

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` `get_page_text` on `quattr.com/case-studies`, full page. Two "Read Case Study" click attempts on the Kiteworks card (`ref_173`) did not trigger navigation (URL and page title unchanged after click) — the dedicated sub-page was not reached this pull. Grading above rests on the fuller index-card text, which is a step short of "the case's own full page" per grading rule 1's letter but is materially more complete than the proof-index teaser Pass 3 graded from (it newly discloses the specific engine, Google AI Overviews, and the 53,000-link intervention scale). Flagged as a pull limitation; a resuming pull should retry the dedicated case-study URL directly once discovered.
- Housing.com's second Quattr case ("12.8% year-over-year growth in relative search market share," https://www.quattr.com/case-studies/housing-market-share-intelligence) was also checked this pull: no AI engine named anywhere on the index card or in the URL's own teaser — classical search-market-share story, not graded as Lane E evidence, consistent with Pass 3's own read (`a-quattr-customers-2026-09-22.md`: "this case reads as a general search-market-share story, not specifically AI-visibility evidence").
