# Case census — P4-c4 — vendor case studies, full-page re-grade of Pass 3 Bronze/Silver cases

```yaml
source:          12 vendor case-study pages, one per row below — see raw paths per row
url_or_doc_id:   multi-vendor — see rows below
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome), own dedicated tab (tabId 1697684063), created and closed for this task — no other agent's tab touched
pull_purpose:    evidence about a number
tier:            5-6 per row — see individual raw files; every row is vendor-reported, no independent third-party replication
source_label:    vendor-reported (all 12)
lane:            E
sub_market:      organic recommendation
engine:          varies per row — see table
metric_kind:     mixed — visibility, traffic, sales — see table
supersedes:      none
captured:        this is the census summary required by the task, not a raw pull itself — compiled from the 12 raw files it cites
```

Task: pull the full dedicated case-study page (not the customers-overview page) for every case Pass 3 graded Bronze or Silver on intake, plus any Fools-gold case naming a revenue figure, and re-grade against all seven evidence-bar items on the full page. Source vendors: the P3-c1-c4 roster (`docs/raw/a-vendor-census-c1-2026-09-22.md` through `a-vendor-census-c4-2026-09-22.md`). 12 cases pulled, spanning 7 vendors: Quattr (2), Profound (2), AthenaHQ (2), RankPrompt (2, same URL), Sitefire (1), Rankscale (2), Conductor (1). No interpretation below; every cell traces to the raw file cited in it.

## Census table

| # | Vendor | Client | Engines (as named on the page) | Metric | Figure, verbatim | Date window | Baseline | Control/holdout (yes/no/quote) | Sample/traffic volume | Who measured | Paid by outcome | Vertical, as named | Pass 3 grade → full-page grade | Prompt set disclosed | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Quattr | Men's Wearhouse | Google (organic + AI Mode), ChatGPT | visibility, traffic | "75% more AI Mode visibility, 50% more top-3 ChatGPT citations... 46% more clicks on treated product pages" | none absolute — "days 0-30/31-60," "trailing 26 weeks," "observed launch window" | yes — e.g. "Treated ... 11,531 → 14,424" | **yes** — "Untreated control product pages not served in any Quattr API: 10,940 → 11,356, +3.8%" | 1,136 treated product-page lineages; 12 live GIGA pages | Quattr (vendor), on customer's first-party GSC data | unknown | Apparel and Fashion | Silver → **Silver (same)** | no | `docs/raw/e-case-quattr-menswearhouse-2026-09-22.md` |
| 2 | Quattr | CloudEagle | not individually named (ChatGPT/Perplexity/Google AIO named once, collectively) | traffic, visibility | "113% organic click growth... AI Citation Share increased by 3×" | none absolute — "12 complete weeks following intervention" | yes — "2.47K to 5.25K" clicks | no | 33 pages optimized; 328 net-new Page 1 queries | Quattr (vendor) | unknown | B2B SaaS (Spend Management) | Bronze → **Bronze (same)** | no | `docs/raw/e-case-quattr-cloudeagle-2026-09-22.md` |
| 3 | Profound | MongoDB | none named — generic "Answer Engines" | visibility | "50% increase in AI Search visibility while maintaining 90%+ accuracy rates" | none — no relative or absolute window stated | no | no | none disclosed | Profound (vendor), via an "internal Q&A training dataset" | unknown | none named on this page (Profound's index tags it "SaaS · Enterprise") | Bronze → **Bronze (same)** | no | `docs/raw/e-case-profound-mongodb-2026-09-22.md` |
| 4 | Profound | Plaid | ChatGPT, Perplexity, Claude (named once, collectively) | traffic (+300%); sales/conversion (+210%) | "LLM referral traffic to plaid.com is up over 300%, with conversions from that traffic up 210%" | none absolute — "since onboarding Profound" | no | no | none disclosed | Profound/Plaid self-report | unknown | none named on this page (Profound's index tags it "Finance · Mid-market") | Bronze → **Bronze (traffic, same); Fools gold (conversion claim, newly surfaced — not evaluated by Pass 3)** | no | `docs/raw/e-case-profound-plaid-2026-09-22.md` |
| 5 | AthenaHQ | Grüns | ChatGPT, Perplexity, Google AI Overviews | visibility | "Share of Voice 2.0% → 12.6% (~6x); Citation Rate 0.3% → 7.0% (~23x); Brand Mention Rate 4.0% → 25.0%" | partial — "Jul 17 → Sep 20" (year inferred from "Q3 2025" in the same case, not stated in the same sentence) | yes, full table | no | 15 targeted articles; 10,500+ est. LLM impressions | AthenaHQ (vendor) + partner agency Boring Ecom | unknown | none named on this page (Grüns is a wellness/DTC-supplement-snack brand) | Bronze → **Bronze (same, but 5-6 of 7 items now satisfied vs. 2 on the teaser)** | no | `docs/raw/e-case-athenahq-gruns-2026-09-22.md` |
| 6 | AthenaHQ | Verito (verito.com) | ChatGPT | visibility | "36% share of voice on ChatGPT... beating rivals 25x their size" | none absolute — "over the past six to eight weeks" | no | no | none disclosed | AthenaHQ (vendor); customer's own first-person account | unknown | none named on this page (IT/cloud hosting for tax and accounting) | Bronze → **Bronze (same)** | no | `docs/raw/e-case-athenahq-verito-2026-09-22.md` |
| 7 | RankPrompt | Humand | "6 AI engines" (count only, not itemized on this page) | visibility | "US AI visibility: 0% → 18.0%; Argentina AI visibility: 24% → 48.0%; Argentina citation share: 4.0% → 11.3%" | none absolute — "Twenty-two weekly reports" | yes | no (implied only) | 2 markets | RankPrompt (vendor) | unknown | B2B SaaS · HR technology | Bronze → **Bronze (same)** | no | `docs/raw/e-case-rankprompt-humand-2026-09-22.md` |
| 8 | RankPrompt | Owings Auto | "6 AI engines" (count only) | visibility, ranking | "Fort Worth AI visibility: 13.3% → 54.2%; Rank #12 of 247 → #2; Answers naming Owings: 16 of 120 → 65 of 120" | none absolute — "141 days" | yes | no (implied by "two lots," not disclosed as its own series) | 120 answers evaluated | RankPrompt (vendor) | unknown | Automotive · Fort Worth, TX | Bronze → **Bronze (same)** | no | `docs/raw/e-case-rankprompt-owings-auto-2026-09-22.md` |
| 9 | Sitefire | Pointhound | ChatGPT, Perplexity, Claude (named as crawler user-agents) | traffic (+300% site visits, +294% AI bot traffic), visibility (Visibility Score, Citation Share) | "+300% more site visits from AI Search... Visibility Score 0 → 1.0%... Citation Share 0 → 1.0%" | **yes, absolute** — "Weekly charts run February 23 to June 29, 2026. The first content went live March 14" | yes | **yes** — "THE CONTROL: new content vs. rest of site" AI bot traffic, split by page group | relative multiples only (0x-4x), no absolute n | Pointhound's own GA4/CDN logs; Sitefire's own tracked question set | unknown | none named on this page (award-flight-search / travel loyalty-points booking) | Bronze → **SILVER — UP** | partial (fixed prompt set at onboarding, n not disclosed) | `docs/raw/e-case-sitefire-pointhound-2026-09-22.md` |
| 10 | Rankscale | Austrian Optical Retail Chain (anonymised) | ChatGPT, Perplexity, Copilot, Google AI Mode | visibility | "AI Visibility grew from a 14.7% baseline to 75.3% in 5 months" (412% growth); "Recognition Rate 85%"; "Top-3 Rate 38%" | none absolute — "in 5 months" | yes | no | 185 mentions, 372 citations | Rankscale (vendor) + partner agency ithelps Digital | unknown | Optical retail / Multi-location retail | Bronze → **Bronze (same)** | partial (example prompts given, no total n) | `docs/raw/e-case-rankscale-optical-retail-2026-09-22.md` |
| 11 | Rankscale | AI SMS Platform (anonymised) | ChatGPT (named); "AI search engines" otherwise generic | sales | "$280,000 in qualified pipeline generated during the initial six months" | none absolute — "six months" / "3-month AI visibility sprint" | no | no | "dozens" of prompts | Rankscale (vendor) + partner agency Spyndle | unknown ("Ongoing retainer secured" implies non-performance fee, not stated explicitly) | AI SMS Software / B2B SaaS | Fools gold → **Fools gold (same)** | partial | `docs/raw/e-case-rankscale-ai-sms-platform-2026-09-22.md` |
| 12 | Conductor | Title Nine | none named — generic "AI search," "AI answer engines" | traffic/visibility bundle (+1,000% AI sessions, +100% AI traffic, +100% AI citations, +33% brand mentions); sales bundle (+18%/+11% category revenue) | "Title Nine Doubled AI Citations and Drove +1,000% AI Session Growth with Conductor" | partial — "In 2024" stated for a separate non-branded-SEO figure, not repeated in the AI-session paragraph | no (percentages only) | no | none disclosed | Conductor (vendor) + named customer employees (self-report) | unknown | Retail | Bronze/Fools gold → **Bronze (traffic bundle, same) / Fools gold (revenue bundle, same)** | no | `docs/raw/e-case-conductor-title-nine-2026-09-22.md` |

## Counts

**Cases pulled: 12** (all 8-12 range satisfied), across 7 vendors: Quattr (2), Profound (2), AthenaHQ (2), RankPrompt (2, one shared URL for both), Sitefire (1), Rankscale (2), Conductor (1).

**Grade changes:**
- **Up: 1** — Sitefire / Pointhound, Bronze (Pass 3, homepage teaser) → **Silver** (this pull, full page). The full dedicated case-study page discloses an absolute date window (Feb 23 - Jun 29, 2026) and an explicit unaffected-control comparison ("new content" vs. "rest of site" AI bot traffic) that Sitefire's homepage teaser did not carry at all — Pass 3 explicitly recorded that this case's own page was not opened that session.
- **Down: 0.**
- **Same: 11** — all other case grades confirmed identical to Pass 3's teaser-level grade (10 unchanged main-claim grades, plus Conductor's Title Nine split Bronze/Fools-gold bundle, itself unchanged from Pass 3's own full-page grading of the same URL).
- **New sub-claim surfaced, not counted in up/down/same: 1** — Profound/Plaid's "+210% conversion" figure does not appear in Profound's customers-index teaser that Pass 3 graded from (only the 300% traffic figure is titled there); this pull's full page discloses it for the first time and grades it Fools gold.

**Cleared (best grade) per vertical, as named on each case's own page:**

| Vertical, as named | Best grade cleared | Case(s) |
|---|---|---|
| Apparel and Fashion | Silver | Quattr / Men's Wearhouse |
| B2B SaaS (Spend Management) | Bronze | Quattr / CloudEagle |
| none named (5 cases: SaaS/Finance/wellness/IT-hosting/travel, per each vendor's own broader index tags, not on the dedicated pages themselves) | Silver | Sitefire / Pointhound (the vertical-less case that cleared Silver); others in this group (Profound/MongoDB, Profound/Plaid, AthenaHQ/Grüns, AthenaHQ/Verito) all Bronze |
| B2B SaaS · HR technology | Bronze | RankPrompt / Humand |
| Automotive · Fort Worth, TX | Bronze | RankPrompt / Owings Auto |
| Optical retail / Multi-location retail | Bronze | Rankscale / Austrian Optical Retail Chain |
| AI SMS Software / B2B SaaS | Fools gold (no Bronze/Silver/Gold clears) | Rankscale / AI SMS Platform |
| Retail | Bronze (plus a Fools-gold revenue sub-claim on the same case) | Conductor / Title Nine |

**Fools gold, revenue figure named: 3** — Profound/Plaid ("+210% conversions"), Rankscale/AI SMS Platform ("$280,000 in qualified pipeline"), Conductor/Title Nine ("+18%/+11% category revenue growth"). Per this task's instruction, one of these (Rankscale/AI SMS Platform) was pulled specifically because it is a Fools-gold case naming a revenue figure; the other two (Plaid, Title Nine) surfaced as sub-claims inside cases pulled for their Bronze/Silver headline claim.

**Zero Gold cases found.** No case among the 12 uses a holdout, geo-split, or switchback design; the two cases with an explicit control (Quattr/Men's Wearhouse, Sitefire/Pointhound) are both observational treated-vs-untreated comparisons on the same site, not randomized or geo-split experiments.

**Paid-by-outcome: 0 yes / 0 no / 12 unknown.** No case among the 12 states anywhere on its page whether the vendor, a partner agency, or the customer was paid contingent on the outcome. Two cases (Rankscale's Austrian Optical Retail and AI SMS Platform) name a paying partner agency (ithelps Digital, Spyndle respectively) whose own fee structure with the end client is never disclosed.

**Prompt set disclosed: 0 yes / 4 partial / 8 no.** Partial: AthenaHQ/Grüns, Sitefire/Pointhound, Rankscale/Austrian Optical Retail, Rankscale/AI SMS Platform — each names a fixed, versioned tracked-prompt set or gives example prompt wordings, but none discloses a total n. No vendor among the 7 profiled discloses a full published prompt list with n behind any of these 12 case-level figures, consistent with the P3-c1 through P3-c4 census finding that no vendor in the roster discloses a composite score's prompt set.

## Survivorship note

These 12 cases are vendor-selected winners, drawn from customer-facing marketing pages that vendors chose to publish. They are not a random or representative sample of any vendor's customer base, and the underlying screen-vs-clear counts from Pass 3 (`docs/raw/a-vendor-census-c1-2026-09-22.md` through `a-vendor-census-c4-2026-09-22.md`: roughly 150 case studies screened across the P3-c1-c4 vendor roster, the large majority graded Bronze or worse, most vendors clearing zero Silver or Gold) remain the operative screened/cleared counts for this survivorship read — this task did not re-screen the wider candidate pool, only re-pulled and re-graded the subset Pass 3 had already flagged Bronze, Silver, or (for one case) Fools-gold-with-a-revenue-figure. Even within this favourably-pre-screened subset, only one of 12 cases (Sitefire/Pointhound) clears Silver on the full page, and none clears Gold.

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| Whether any of the 12 cases' underlying figures were independently audited or replicated by a party other than the vendor and its customer | Each case's own dedicated page (12 pages, listed above) | 2026-09-22 |
| Whether Profound's conflicting Plaid figures (this page's "300% traffic / 210% conversions" vs. Profound's own customers-index page's "50% increase in AI Search visibility" for the same customer) are the same underlying study or two different measurement exercises | `docs/raw/e-case-profound-plaid-2026-09-22.md`, `docs/raw/a-profound-customers-2026-09-22.md` | 2026-09-22 |
| Whether the calendar year behind Conductor/Title Nine's AI-session figures ("+1,000%... from the beginning of the year to the end") is the same 2024 stated elsewhere on the same page for a different (non-branded organic) metric | `docs/raw/e-case-conductor-title-nine-2026-09-22.md` | 2026-09-22 |
| Fee structure (flat, retainer, or performance-based) behind any of the four agency-partnered cases (AthenaHQ/Boring Ecom for Grüns; Rankscale/ithelps Digital for Austrian Optical Retail; Rankscale/Spyndle for AI SMS Platform) | Each case's own dedicated page, plus `docs/raw/a-rankscale-careers-facts-2026-09-22.md` (Rankscale's general Agency Program terms, not case-specific) | 2026-09-22 |
| Total n of tracked prompts behind any of the four "partial" prompt-set-disclosure cases (Grüns, Pointhound, Austrian Optical Retail, AI SMS Platform) | Each case's own dedicated page | 2026-09-22 |

## Caveats

- Every case in this file is vendor-reported and bias-flagged per `trust-rubric.md`'s "vendor measuring the thing it sells" — no case among the 12 carries independent third-party replication, even where a case (Quattr/Men's Wearhouse, Sitefire/Pointhound) discloses an explicit unaffected control cohort sufficient to clear Silver on the correlational standard `glossary.md` sets for that grade.
- The two Silver-clearing cases (Quattr/Men's Wearhouse, already Silver at Pass 3; Sitefire/Pointhound, newly Silver this pull) share a structural feature: both compare a treated cohort (product pages served via an API, or newly-published content) against an untreated cohort on the *same site* (other product pages; the rest of the site's existing content) — an observational within-site control, not a randomized or geo-split experiment. Per `plan.md`'s grade definitions this clears Silver ("baseline plus an unaffected control metric") but not Gold ("holdout, geo-split, or switchback").
- Grade "sameness" across 11 of 12 cases should not be read as confirming the underlying numbers are more reliable than Pass 3's teaser-level read suggested — in most cases (AthenaHQ/Grüns being the clearest exception) the full page discloses the same or only marginally more of the seven-item bar than the teaser it was condensed from, because the teaser text itself was already drawn verbatim from the case-study page's own headline stats.
- This file's "vertical, as named" column follows the task's cell-attribution rule (`docs/method/demand-signals.md`): a vertical is recorded only when the case's own dedicated page states it; a vendor's separate customers-index page tagging a case with an industry label (e.g., Profound's "Finance · Mid-market" for Plaid) is not carried into this column when the dedicated page itself is silent on it, and is instead noted in the table cell as context.
- The oldest pull depended on in this file is 2026-09-22 (all 12 case pages pulled today; the census files they are graded against — `a-vendor-census-c1` through `c4` — are also dated 2026-09-22).
