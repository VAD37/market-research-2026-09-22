# B2B SaaS

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every cited `docs/raw/` file. Oldest *publication* depended on: 2025-06-03 (HN thread title, `raw/f-signal-bs-S5-hn-algolia-2026-09-22.md`) |
| Cells | 3 sub-markets × 3 buyer sizes = 9 |
| Cells with a spend signal | 3 of 9 — all organic recommendation |
| Signals in the catalogue checked | 12 of 12 in the three organic cells; 9 of 12 in the six paid and agentic cells |

## Segment definition

| | |
|---|---|
| What counts as this vertical, and what is excluded | A company the source itself names B2B SaaS / SaaS / B2B software, as the buyer. AI-visibility vendors and agencies themselves are excluded — supply side, handled in `competitors/` |
| Bands, as the sources define them | No source in this vertical publishes a band. `demand-signals.md` method choice applied throughout: SMB under 100 headcount, mid-market 100–999, enterprise 1000 or more. One vendor tag used verbatim: Profound tags MongoDB "SaaS · Enterprise" — `raw/e-case-census-c13-2026-09-22.md` — and defines no band |

## Cell reads

| Sub-market | Size | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | Read | Deciding signal (tier, raw) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organic | SMB | Actindo, 52–70 emp (3) | u | n | n | u | u | n | n | n | n | n | u | **spend** | S1 Actindo posting, tier 3, `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` |
| Organic | Mid-market | AutoLeap, 199–225 emp (3) | u | n | n | u | u | n | n | n | n | n | u | **spend** | S1 AutoLeap posting, tier 3, same raw file |
| Organic | Enterprise | Pennylane 1,100+; Mercury 1,001–5,000 (3) | MongoDB "SaaS · Enterprise" (6) | n | n | u | u | n | n | n | n | n | `/llms.txt` on 9 of 10 domains, 90% (1) | **spend** | S1 Pennylane posting, tier 3, same raw file |
| Paid | SMB | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | no signal observed; 9 of 12 signals checked |
| Paid | Mid-market | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Paid | Enterprise | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Agentic commerce | SMB | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Agentic commerce | Mid-market | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Agentic commerce | Enterprise | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |

The three organic reads rest on a tier-3 spend-class signal, **above** the tier-5 floor ("tier 5 or better" = tiers 1–5). The source census read that floor the other way and marked the same four hits attention — `raw/f-signal-census-bs-2026-09-22.md` §"Spend-class vs attention-class tally". Both readings stand, attributed.

## Signals

Marks: `n` = none — checked, nothing found, 2026-09-22. `u` = blank — unattributed: checked, data exists, the source states no buyer size, moves no cell. `b` = blank — unchecked: no paid- or agentic-term query was run; never written as `none`. `n/a` = S12's on-property artifact does not apply to paid or agentic commerce by construction. Spend-class and attention-class signals are never summed.

Channels behind each `n`, by signal, all checked 2026-09-22 — **S1** LinkedIn guest API, 18 queries; indeed.com and upwork.com 403; freelancer.com JS shell (`raw/f-signal-bs-S1-linkedin-jobs-guest-api-`, `-S1-indeed-`, `-S1-upwork-freelancer-`). **S2, S3** `raw/a-vendor-census-c1..c4-`, via `raw/f-signal-bs-S2-S3-vendor-census-citation-`. **S4** g2.com and capterra.com 403; omr.com reached — 56 reviews, 4.81 avg, reviewer industry undisclosed (tier 6) (`-S4-g2-capterra-`, `-S4-omr-`). **S7** `raw/e-case-census-c1-` (B2B SaaS screened 0, cleared 0) plus HubSpot and Yext filings (`-S7-earnings-calls-citation-`). **S8** six conference agendas plus `raw/e-case-census-c3-` (0 of 6 graded talks B2B SaaS) (`-S8-conference-sessions-citation-`). **S9** trends.google.com, data API token-gated (`-S9-google-trends-`). **S10** sam.gov 0 relevant, contractsfinder.service.gov.uk filter non-functional, ted.europa.eu grid not static (`-S10-procurement-`). **S11** DuckDuckGo HTML 0 results plus the B2B SaaS case files (`-S11-price-paid-`). Every `f-signal-bs-*` path carries the `2026-09-22` suffix.

Signals marked `u`, recorded at vertical level, moving no cell — **S2** vendor and agency case-study rosters naming a B2B SaaS client without a size: Quattr/CloudEagle "B2B SaaS (Spend Management)" (5), Foundation/Bitly "Link Management & QR Code Software (B2B SaaS)" (5), Seer's "SaaS" HR client (5), RankPrompt/Humand "B2B SaaS · HR technology" (6), deeploi and Heyflow via Radyant (5), Rankscale "AI SMS Platform" (6) — `raw/e-case-census-c4-`, `-c13-`, `-c9-`, `-c2-2026-09-22.md`. **S5** one HN thread, "From Traditional SEO to AI-Driven Answer Engine Optimization in B2B SaaS", 2 points, 1 comment (4) — `raw/f-signal-bs-S5-hn-algolia-2026-09-22.md`; reddit.com 403. **S6** Flow Agency "SaaS startups", Foundation Inc "AI Visibility Agency for B2B Tech & SaaS" (3 on existence) — `raw/f-signal-bs-S6-flow-agency-2026-09-22.md`, `raw/f-agency-census-c5-2026-09-22.md`: target-customer claims, excluded from every read.

## Cells with no signal — channels checked

| Cell | Signals checked | Channels checked | Date | Result |
|---|---|---|---|---|
| Paid and agentic commerce, all three sizes (6 cells) | 9 of 12 each (S5, S6 unchecked; S12 n/a) | LinkedIn guest API, Indeed, Upwork, vendor censuses c1–c4, G2, Capterra, OMR, EDGAR via c1, six conference agendas, Google Trends, SAM.gov, Contracts Finder, TED, DuckDuckGo | 2026-09-22 | none found |

## Willingness to pay

| Cell | Price actually paid | What it bought | Who disclosed it | Label | Raw |
|---|---|---|---|---|---|
| All nine | `unknown — checked DuckDuckGo HTML and the B2B SaaS Pass-4 case files 2026-09-22` | — | nobody | — | `raw/f-signal-bs-S11-price-paid-2026-09-22.md` |

Pass 3 asking prices — Semrush's +$60/mo AI-toolkit delta (`raw/a-vendor-census-c4-2026-09-22.md`), Pace Generative's $1,499–$2,499 list (`raw/f-agency-census-c5-2026-09-22.md`) — are list prices, never purchases, and are not willingness-to-pay observations.

## Buyer personas, jobs-to-be-done, switching costs, buying process

| Source | Role, quoted | Job, quoted | Cell |
|---|---|---|---|
| Actindo posting | "Digital Marketing Manager - B2B SaaS & AI (m/w/d)" | "Du unterstützt SEO- und GEO-Maßnahmen, um die Sichtbarkeit von Actindo in Suchmaschinen und KI-basierten Systemen zu steigern" | Organic / SMB |
| AutoLeap posting | "SEO Lead" | "Experience with AI SEO, Google Analytics, Google Tag Manager" | Organic / Mid-market |
| Pennylane, Mercury postings | "SEO & AI Content Specialist"; "Organic Search Marketer (SEO/AEO)" | "Build an understanding of the questions and prompts prospects use in AI-powered discovery tools"; "define how Mercury shows up across search engines, answer engines, and AI-native discovery" | Organic / Enterprise |
| Profound / MongoDB case | "Fiona Erickson, Team Lead, Organic Acquisition" | "If an Answer Engine gives the wrong information about how to configure MongoDB, the developer doesn't have a bad experience with the AI, they have a bad experience with us" | Organic / Enterprise (vendor tag) |
| Foundation / Bitly case | "Tara Robertson, Chief Marketing Officer, Bitly" | "the answers came from sources Bitly didn't write and couldn't control" | Organic, size unassigned |

Postings: `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` (3). Cases: `raw/e-case-profound-mongodb-2026-09-22.md` (6), `raw/e-case-foundation-inc-bitly-2026-09-22.md` (5). Switching costs and buying process: `unknown — checked every raw file this file cites, 2026-09-22` — no source states a contract length, renewal, incumbent displaced, decision maker, blocker, or cycle length for any B2B SaaS buyer in any sub-market. Bitly's "12 Months" is a delivery window the agency states, not a buying-process disclosure.

## Proof landscape — this vertical

| Cluster | Screened / cleared | Best grade | Detail |
|---|---|---|---|
| P4-c9 vertical sweep | ~100 / 4 | Bronze | G2, HubSpot, Heyflow ×2; 3 Fools gold; 0 Silver, 0 Gold; 6 of 9 pulled confirmed B2B SaaS by the source — `raw/e-case-census-c9-2026-09-22.md`. The one negative-direction case is HubSpot: "verlor HubSpot zwischen 30 und 40 Prozent des Traffics auf betroffenen Keywords", 2026-03-16 (5) — `raw/e-case-c9-hubspot-omr-podcast-2026-09-22.md` |
| P4-c2 agency posts | 12 agencies / 3 | **Silver** | Seer's "SaaS HR" client: test pages +219% then +300% AI traffic, site-wide AI sessions "remained stagnant" as control (5) — `raw/e-case-seer-interactive-content-recency-2026-09-22.md` |
| P4-c4 and P4-c13 vendor cases | 12 graded, ~150 titles re-graded / 4 | Bronze | Quattr/CloudEagle (5), RankPrompt/Humand (6), Rankscale/SoWork, Profound/MongoDB (6); Rankscale "AI SMS Platform" Fools gold, "$280,000 in qualified pipeline" — `raw/e-case-census-c4-`, `-c13-2026-09-22.md` |
| P4-c7 brand side, P4-c11 nulls | 59 brands, ~180 negatives / 0 | — | 0 corroborate, 0 contradict, 59 silent (MongoDB, Plaid, Ramp, Airbyte, Strapi, NinjaOne among them); 0 B2B SaaS null cleared — `raw/e-case-census-c7-`, `-c11-2026-09-22.md`. Zero Gold anywhere in this vertical; the one Silver's client is anonymised to "SaaS HR" |

## Hypotheses touched

| # | Claim | This vertical's input |
|---|---|---|
| H4 | Demand is attention-only in every SMB cell | **Falsifier condition met here**: Organic / SMB reads spend on Actindo's own posting, tier 3. Paid / SMB and Agentic / SMB read `none — checked`. Scoring across all 9 SMB cells is Pass 9's |
| H7 | Organic carries spend in more cells than paid or agentic | Input only: organic 3, paid 0, agentic 0 in this vertical. Needs all 27 cells |
| H9 | Agentic spend sits in enterprise cells, absent from SMB | Input only: no agentic cell here reads spend, enterprise included |

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| Does G2's or Capterra's AI-visibility category show a B2B SaaS reviewer segment, at what velocity? Does OMR expose reviewer industry or size anywhere a static fetch missed? | g2.com, capterra.com (403), omr.com/en/reviews/product/otterly-ai | 2026-09-22 |
| Do Indeed or Upwork carry GEO/AEO postings by B2B SaaS employers that LinkedIn's non-phrase-strict guest API missed? | indeed.com, upwork.com (403), freelancer.com (JS shell) | 2026-09-22 |
| Do r/SEO, r/PPC or r/bigseo carry B2B SaaS threads on any sub-market? Does search interest for GEO/AEO/AI-visibility terms concentrate in software contexts? | reddit.com search.json (403), trends.google.com (data API token-gated) | 2026-09-22 |
| Does any procurement register carry a B2B-SaaS-adjacent AI-visibility award once queried through a working search path? | sam.gov, contractsfinder.service.gov.uk, ted.europa.eu | 2026-09-22 |
| Does a paid-placement or agentic-commerce community thread or agency page exist for B2B SaaS? Sub-market-specific S5 and S6 queries were never run | hn.algolia.com, DuckDuckGo HTML — organic-alias terms only | 2026-09-22 |

## Caveats

- Every read rests on internet-only proxies. No interviews, no outreach (`scope.md` R2). No signal observes a budget. Willingness to pay is `unknown` in all nine cells, and nothing here is inferred from a list price.
- **All three spend reads rest on a single signal, S1, at tier 3.** `demand-signals.md` calls S1 "headcount budget, not category spend — weakest spend class", lagging spend and over-representing large firms. Three of the four postings' headcounts come from third-party data-vendor snippets (PitchBook, Revelio Labs, ZoomInfo, LeadIQ, RocketReach) read via search snippet, not opened; only Pennylane's "More than 1,100 Pennylaners" is primary. AutoLeap's sources conflict — 199 and 225 against a "51-200" range straddling the SMB / mid-market boundary — recorded, not averaged. LinkedIn's guest API does not enforce exact-phrase matching either — `"generative engine optimization"` returned zero relevant hits across two attempts — so S1 counts here likely undercount real hiring.
- **The six `none — checked` reads are partial.** S5 and S6 were run with organic-alias terms only, so those cells rest on 9 of 12 signals; several of the nine are access-level blocks (G2, Capterra, Reddit, Trends, Indeed, Upwork) that would have blocked any sub-market equally. 9 browser-backlog items stay open — `raw/f-signal-census-bs-2026-09-22.md` §Browser backlog.
- Publication bias runs one way: quiet spending leaves no public trace, so `none` reads are weaker evidence than `spend` reads. S12's 90% is measured-by-us at tier 1, but the sample's Enterprise band comes from public-record reputation and was not re-verified in the pull; it decides nothing, its cell already reading spend on S1.
