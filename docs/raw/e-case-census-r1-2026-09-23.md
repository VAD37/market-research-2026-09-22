# Case census — P4-r (Pass 4 re-run, Lane E success stories), round 1

```yaml
source:          multi-source census — EDGAR full-text search; brand-owned domains; vendor case pages (Pass 3 unopened titles and sitemap-new pages); agency and practitioner pages found by DuckDuckGo html search; conference result pages; Arctic Shift archive of reddit.com
url_or_doc_id:   per row below; every opened page has a raw file named in its row
published:       per row
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, browser or research User-Agent); curl-equivalent EFTS calls with User-Agent "research contact vadprimary@gmail.com"; Playwright (MCP_DOCKER browser, pw holder) for link lists and blocked pages; Wayback Machine snapshots where live pages blocked; WebSearch (72 calls, then session cap); DuckDuckGo html endpoint after the cap; Arctic Shift API for Reddit
pull_purpose:    evidence about a number (census of every candidate screened, with grades)
tier:            n/a at file level — per row
tier_reason:     census index; each graded row carries the tier of its raw file
source_label:    per row — vendor-reported, company-stated, filed
lane:            E
sub_market:      organic recommendation (mainly); paid placement and agentic commerce rows marked
engine:          per row
metric_kind:     per row
supersedes:      none — extends raw/e-case-census-c1 … c13-2026-09-22.md; the ~980 candidates screened there are not re-screened
captured:        full census
verbatim:        n/a — census index; verbatim text sits in the raw file named per row
```

No interpretation. Grades per `method/plan.md` §Evidence bar, grading rule 1 and its 2026-09-23 reading: every graded row carries `grade_raw` (grade table read on the page) and `grade_rule1` (any of items 1–7 absent on the case's own page caps it at Bronze; Fools gold stays Fools gold). Status words: `screened — no claim` (page opened, no before/after metric), `screened — not opened`, `not reachable`, `discard on sight` (trust-rubric list), `action named, outcome unknown` (a change is named, no metric moved). Items: 1 brand or credible anonymised profile, 2 engine, 3 absolute date window, 4 baseline, 5 intervention, 6 sample size or traffic volume, 7 who measured and whether paid by outcome. Design field per the 2026-09-23 evidence-quality append: `experimental` = holdout, geo-split, switchback, or pre/post with a control; otherwise `observational`.

Verticals: `skin` skincare and beauty; `b2b` B2B SaaS; `hcpa` high-CPA regulated (cards, insurance, supplements); `none` outside the three (recorded, not graded for the done row). `borderline` marks a brand whose product sits at a vertical's edge (neobank, beauty-booking platform).

## Counts per channel

| Channel | Screened | Opened | Graded Bronze or better | Silver raw | Silver rule1 | Gold | Raw files |
|---|---|---|---|---|---|---|---|
| 1 EDGAR full-text | 1,098 documents (30 queries, 2025-01-01 to 2026-09-23) + 34 tickers × 5 terms per-CIK | 16 filings read in context | 1 (Yext self-claim) | 0 | 0 | 0 | e-case-edgar-fulltext-results-2026-09-23.md |
| 2 Brand pages | 109 brands (96 rows) | 11 brand pages found naming a vendor or an own AI metric | 2 (B1, B3) + 1 Fools gold (B2) | 0 | 0 | 0 | e-case-chime-careers-airops, e-case-brandside-found-multi, e-case-fresha-ai-bookings, e-case-fresha-google-agentic |
| 3 Pass 3 unopened and unreachable titles | 19 line items (c13: AirOps 9, Otterly 5, Blackbird, Pigeon Forge, c6 sell-side group, Home Depot, Green Energy) | 17 line items + 16 sell-side client pages | 6 (+1 Fools gold) | 0 | 0 | 0 | e-case-airops-*, e-case-otterly-{chatarmin,sornai-pagepilot,whatifweb,nola-spoc} |
| 4 Vendor pages new since 2026-09-01 | 36 vendor sitemaps; 44 URLs with lastmod ≥ 2026-09-01 matching case/customer paths | 13 | 7 (+2 Fools gold) | 0 | 0 | 0 | e-case-athenahq-new-multi, e-case-profound-new-multi, e-case-fireandspark-supplement-citations, e-case-birdeye-arrow-senior-living |
| 5 Agency and practitioner cases | 7 DuckDuckGo queries, ~60 result entries | 14 | 5 (+1 Fools gold) | 0 | 0 | 0 | e-case-ddg-vendor-multi, e-case-hubspot-aeo-data-cohort, e-case-fortune-hubspot-blog-traffic-loss |
| 6 Conference talks | 5 DuckDuckGo queries (brightonSEO, MozCon, SMX Advanced, Shoptalk, INBOUND), ~50 entries | 2 (via INBOUND query) | counted in channel 5 | 0 | 0 | 0 | — |
| 7 Platform, vendor and practitioner experiments with a control | 4 DuckDuckGo queries (~20 entries read) + Otterly experiment hub | 8 | 6 | 4 | 1 | 0 | e-case-otterly-{reddit-experiment,html-vs-markdown-experiment,llms-txt-experiment,geo-guide-experiment-claims}, e-case-jonathanmall-geo-experiment, e-case-boily-dental-geo-comparison |
| Reddit (Arctic Shift, comments) | 221 comments, 9 subreddits × 5 queries (31 of 45 calls returned) | 25 read in full | 0 (R2 Fools gold; R1 discard) | 0 | 0 | 0 | e-case-reddit-arcticshift-comments |

Totals, cases graded this pull (channels 1–5, 7; Reddit adds R2 Fools gold and R1 discard): Gold 0; Silver raw 4, Silver rule1 1; Bronze raw 23; Fools gold 5; action named, outcome unknown 13. Metric moved with experimental design: 4 (rows X1, X2, X5, X6), all outside the three verticals. Metric moved, observational: 28. Negative or null direction: 4 graded (X2, X3, X5 mentions sub-result, A9) + 1 not graded (X7).

## Case register

| # | Ch | Candidate | Vertical | URL | grade_raw | grade_rule1 | Items absent | Metric moved — metric, from → to, window | Design | Direction | Brand side | Raw |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | 3 | AirOps / Kong | b2b | airops.com/blog/kong-quill-story | screened — no claim | — | — | no — "results so far are just the beginning" | — | — | not checked | e-case-airops-unopened-multi |
| T2 | 3 | AirOps / Conviva | b2b | airops.com/blog/conviva-quill-story | screened — no claim | — | — | no — "results are ahead of it" | — | — | not checked | e-case-airops-unopened-multi |
| T3 | 3 | AirOps / two independent practitioners | none | airops.com/blog/solo-quill-story | screened — no claim | — | — | no | — | — | n/a | e-case-airops-unopened-multi |
| T4 | 3 | AirOps / Animalz | none | airops.com/blog/animalz-quill-story | screened — no claim (review-cycle claim, no AI metric) | — | — | no | — | — | n/a | e-case-airops-unopened-multi |
| T5 | 3 | AirOps / Bitly | b2b | airops.com/blog/bitly-quill-story | screened — no claim | — | — | no | — | — | not checked | e-case-airops-unopened-multi |
| T6 | 3 | AirOps / Merge | b2b | airops.com/blog/merge-customer-story | screened — no claim (level only) | — | — | no — "#1-2 LLM visibility… 300 tracked prompts", no before value | — | — | not checked | e-case-airops-merge |
| T7 | 3 | AirOps / Venn | hcpa (business credit cards) borderline | airops.com/blog/venn-customer-story | Bronze | Bronze | 3, 4, 6, 7 | citations +600%; LLM traffic +50% MoM; organic +150%, "four months", no dates | observational | up | not checked — search cap | e-case-airops-venn |
| T8 | 3 | AirOps / Harvard Business Publishing | none | airops.com/blog/harvard-business-publishing-and-airops | screened — no claim (efficiency only) | — | — | no | — | — | n/a | e-case-airops-unopened-multi |
| T9 | 3 | AirOps / Rhetoric | b2b | airops.com/blog/rhetoric-saves-engineering-headcount-and-ships-faster-with-airops | screened — no claim (2023, efficiency) | — | — | no | — | — | not checked | e-case-airops-unopened-multi |
| T10 | 3 | Otterly / Chatarmin | b2b | otterly.ai/blog/chatarmin-geo-ai-search-playbook/ | Fools gold | Fools gold | 3, 6, 7; no control | ChatGPT share of booked demos <1% → 5–10%, "a few months" (page 2026-06-30) | observational | up | not checked — search cap | e-case-otterly-chatarmin |
| T11 | 3 | Otterly / NOLA Marketing — Single Point of Contact | none | otterly.ai/blog/nola-marketing-ai-citation-rank-case-study/ | Bronze; leads sub-claim Fools gold | Bronze | 3, 7 | mentions +433%, citations +444%, three months to June; 64 prompts | observational | up | not checked — search cap | e-case-otterly-nola-spoc |
| T12 | 3 | Otterly / SORN.AI — PagePilot | b2b | otterly.ai/blog/geo-case-study-sornai/ | Bronze | Bronze | 6, 7 | AI chat referral sessions +31.1% MoM, June 2026, base ≈0.7% of organic sessions | observational | up | not checked — search cap | e-case-otterly-sornai-pagepilot |
| T13 | 3 | Otterly / What IF Web (own site) | none | otterly.ai/blog/geo-case-study-whatifweb/ | Bronze | Bronze | 3, 4, 6 | AI traffic +300%, 28 days vs prior 28 | observational | up | n/a — agency's own site | e-case-otterly-whatifweb |
| T14 | 3 | Otterly / TM Blast | none | LinkedIn video (teaser on otterly.ai/case-studies) | not reachable — video behind LinkedIn, no login | — | — | — | — | — | not checked | — |
| T15 | 3 | Searchable / Blackbird | none | searchable.com/customers/blackbird | Bronze; pipeline sub-claim Fools gold | Bronze | 3, 4, 6, 7 | "+30% average improvement in AI search visibility", 90-day sprints; "$1.1M in 2026 pipeline" | observational | up | silent — domain not resolved | e-case-titles-opened-multi |
| T16 | 3 | Orange142 / Pigeon Forge | none | orange142.com/blog/orange-142-helps-pigeon-forge-increase-ai-visibility-by-136 | Bronze | Bronze | 3, 4, 6, 7 | AI mentions +136%, "within months" | observational | up | found — co-named in DRCT release 2026-02-10 (programme) | e-case-titles-opened-multi |
| T17 | 3 | c6 sell-side group — Feedonomics 12, Kargo 4 opened | none | feedonomics.com/success-stories/{12 slugs}; kargo.com/case-studies/{4 slugs} | Euro Car Parts: action named, outcome unknown; Fruugo: action named; 14: screened — no claim | — | — | no — "Enriched 25,000 listings… to boost AI search visibility" (Euro Car Parts) | — | — | silent (brand table) | e-case-titles-opened-multi (Euro Car Parts lines) |
| T18 | 3 | Seer Interactive / Home Depot (was unreachable) | none | searchengineland.com/guide/enterprise-ecommerce-llm-visibility-case-study via web.archive.org 2026-07-22 | screened — no claim: Semrush-authored snapshot, Feb 2026 AIO data, SoV 28.9%, no intervention | — | — | no | — | — | silent | e-case-titles-opened-multi |
| T19 | 3 | Orange142 / "A Green Energy Client" (was unreachable) | none | orange142.com/case-studies/green-energy-seo (404, no Wayback capture) | not reachable; orange142.com/energy snapshots are classical SEO (124% page views), no AI engine | — | — | — | — | — | n/a | — |
| B1 | 2 | Chime — AirOps case, brand-side page | hcpa borderline (neobank; secured credit card) | airops.com/blog/chime-case-study; careers.chime.com (Wayback 2026-02-23) | Bronze | Bronze | 2, 4, 6, 7 (window "July", year implied 2025) | AI citations 3x "in less than 4 weeks" (brand: "tripled our AI citations"); refresh velocity 16 → 27 posts/month | observational | up | **found — corroborates** (careers.chime.com 2025-11-24) | e-case-airops-chime-case-study; e-case-airops-chime-quill; e-case-chime-careers-airops |
| B2 | 2 | Fresha — own post (found in HubSpot brand check) | skin borderline (beauty and wellness booking) | fresha.com/blog/fresha-ai-booking-growth | Fools gold | Fools gold | 3, 5, 7 | APAC share of online booking referrals from Gemini/LLMs ~1 in 7 → 25% ("two years ago" → 2026-02-24); AI-referred bookings +50% MoM | observational | up | company-stated (own domain) | e-case-fresha-ai-bookings |
| B3 | 2 | Proper Propaganda — own case study, Scrunch named | none (agency) | properpropaganda.net/case-study-how-proper-propaganda-built-its-own-generative-engine-optimization-geo-presence/ | Bronze | Bronze | 4, 6 | overall share of answer 10%, Perplexity 15%, July → November 2025; "2 signed clients" (vendor page: "5x'd lead gen") | observational | up | found — own page; vendor and brand figures differ, side by side | e-case-brandside-found-multi |
| B4 | 2 | Kiteworks — own release, Quattr named | b2b | kiteworks.com press release 2023-06-07 | screened — no AI metric ("doubled inbound organic search traffic") | — | — | no AI-engine metric | — | — | found — programme | e-case-brandside-found-multi |
| V1 | 4 | AthenaHQ / Nuvadermis (Lyra Collective) | skin | athenahq.ai/case-studies/3x-share-of-voice-nuvadermis-geo-case-study/ | Bronze | Bronze | 3, 4, 6, 7 | share of voice 3x in 3 months; on-page citation rate single digits → 20%+ (category avg 4%), "early 2025" | observational (category average is a cross-sectional comparator) | up | unreachable — search cap | e-case-athenahq-new-multi |
| V2 | 4 | AthenaHQ / AutoRFP.ai | b2b | athenahq.ai/case-studies/10x-chatgpt-traffic-autorfp-success-story/ | Fools gold (demos); traffic Bronze | Fools gold | 3, 4, 6, 7 | chatgpt.com referred traffic 10x since end 2024; one third of demo prospects cite ChatGPT | observational | up | not checked — search cap | e-case-athenahq-new-multi |
| V3 | 4 | AthenaHQ / Lago | b2b | athenahq.ai/case-studies/lago-ai-overview-impressions-citations-case-study/ | Bronze | Bronze | 6, 7 | AI Overview impressions 3% → 33% (prompt cohorts, GSC), March → September 2025; citation rate 3.5% → 17%; ~50% of demos "directional" | observational | up | not checked — search cap | e-case-athenahq-new-multi |
| V4 | 4 | AthenaHQ / Buried (agency, own site) | none | athenahq.ai/case-studies/300-percent-more-leads-buried-geo-case-study/ | Fools gold | Fools gold | 3, 4, 6, 7 | leads +300% in four months; citation rate 11.2% vs competitor avg 3% | observational | up | n/a | e-case-athenahq-new-multi |
| V5 | 4 | Profound / Kiteworks | b2b | tryprofound.com/customers/kiteworks | Bronze | Bronze | 3, 4, 6, 7 | ~50% aggregate AI visibility in five months; #1 cited domain within one month | observational | up | found — Quattr programme only, Profound not named | e-case-profound-new-multi |
| V6 | 4 | Profound / WHOOP | none | tryprofound.com/customers/whoop | Bronze | Bronze | 3, 4, 6, 7 | visibility +6.6% in 6 months; 56% of answers on top prompts | observational | up | silent | e-case-profound-new-multi |
| V7 | 4 | Profound / Apartment List | none | tryprofound.com/customers/apartment-list | Bronze | Bronze | 3, 4, 6, 7 | AI citations 2x; initial results in 2 weeks | observational | up | not checked | e-case-profound-new-multi |
| V8 | 4 | Fire&Spark / anonymised natural weight-loss supplement brand | hcpa (supplements) | fireandspark.com/case-study/clinical-data-ai-search-citations/ | Bronze | Bronze | 3, 4, 7 | 275 citation instances, position 1 on 14 of 20 prompts, 157 runs, first 30 days after launch; Gemini 256 of 275 | observational (new content, no pre-launch value) | up | n/a — anonymised | e-case-fireandspark-supplement-citations |
| V9 | 4 | Birdeye / Arrow Senior Living | none | birdeye.com/resources/case-studies/arrow-senior-living/ | Bronze; leads Fools gold | Bronze | 3, 7 | visibility score 16.24% → 18.88%; new leads 1.4K → 2.1K (+52.8%), one month, 46 communities | observational | up | not checked | e-case-birdeye-arrow-senior-living |
| V10 | 4 | Locafy / Mitchell Dental Group; Clean Pro Services | none | locafy.com/case-studies/{mitchell-dental-group, clean-pro-services} | screened — no claim (testimonial: "now appearing in AI Overviews") | — | — | no | — | — | not checked | — |
| V11 | 4 | AirOps / "results-from-aeo" | — | airops.com/blog/results-from-aeo | screened — no claim (guide, no case) | — | — | no | — | — | — | — |
| V12 | 4 | BrightEdge global-services-provider; SOCi three roundups; Yext Accor; Onclusive DE/FR case indexes | none | per sitemap | screened — not opened (titles classical SEO, listings, social) | — | — | — | — | — | — | — |
| A1 | 5 | OptimizeGEO / anonymised global beauty (haircare) brand | skin | optimizegeo.ai/docs/case-studies/beauty-ai-visibility | Bronze | Bronze | 1, 3, 7 | brand mentions 86 → 282+ at peak (3.3x) over 120 prompts, "within weeks" of four weeks of fixes | observational | up | n/a — anonymised | e-case-ddg-vendor-multi (tier 6) |
| A2 | 5 | BrandCited / "Lumara Skincare" | skin | brandcited.ai/case-studies/ecommerce-brand-invisible-to-number-one-chatgpt | Bronze | Bronze | 3, 6, 7; brand existence unverifiable | vendor visibility score 8 → 38 (30 days) → 68 (90 days); top ChatGPT recommendation in 4 categories | observational | up | unreachable — no brand domain located | e-case-ddg-vendor-multi (tier 6) |
| A3 | 5 | Over The Top SEO / "ProjectFlow" | b2b | overthetopseo.com/geo-case-study-ai-search-citations/ | Bronze; signups Fools gold | Bronze | 1 (pseudonym), 3, 7 | citation rate 12% → 87% over four months, 50 queries/week, GPT-4o, Perplexity, Claude, AIO | observational | up | n/a — pseudonym | e-case-ddg-vendor-multi (tier 6) |
| A4 | 5 | Go Fish Digital / unnamed client | unknown | gofishdigital.com/blog/generative-engine-optimization-geo-case-study-driving-leads/ | Bronze (traffic +43%); Fools gold (conversions +83.33%) | Bronze / Fools gold | 1, 3, 4, 6 | AI referral traffic +43%, conversions +83.33%, three months | observational | up | n/a | e-case-ddg-vendor-multi (tier 6) |
| A5 | 5 | CiteWorks Studio / business insurance brand | hcpa (insurance) | citeworksstudio.com/case-studies/client-implementation/business-insurance-ai-search-case-study | discard on sight — value is an estimate ("directional estimate" of $204,641.36 monthly branding value) | — | — | — | — | — | n/a | not pulled |
| A6 | 5 | Geology / insurance client | hcpa (insurance) | getgeology.com/blog/case-study-insurance-ai-visibility | discard on sight — no n, no window ("impressions triple in two weeks") | — | — | — | — | — | n/a | not pulled |
| A7 | 5 | FAIV / nutritional supplements brand | hcpa (supplements) | foraivisibility.com/en/cases/suplementos-nutricionales-chatgpt | screened — no claim | — | — | no | — | — | n/a | — |
| A8 | 5 | HubSpot company news / AEO customer cohort | b2b | hubspot.com/company-news/aeo-data-buyers-using-ai-search-more-likely-to-purchase | Fools gold | Fools gold | 1, 3, 6, 7 | AEO-optimizing customers vs "comparable customers": +20% AI-visit traffic, +170% MQLs, +82% deals; "HubSpot proprietary data" | observational — cross-sectional, self-selected (correlation reported as incrementality) | up | company-stated (vendor = brand) | e-case-hubspot-aeo-data-cohort |
| A9 | 5 | Fortune op-ed, HubSpot CMO — own blog traffic | b2b | fortune.com/2026/09/22/hubspot-ai-impact-marketing-blog-posts-traffic/ | Bronze (negative) | Bronze | 3, 4, 6 | blog −5 million visits in a thirty-day period; AI search usage +37%, traditional search −11% | observational | **negative** | company-stated | e-case-fortune-hubspot-blog-traffic-loss |
| A10 | 5 | grro.io / DTC skincare brand | skin | grro.io/blog/case-study-ecommerce-ai-visibility | not reachable — HTTP 402 Payment Required | — | — | snippet: "0 AI search mentions to 2,800 monthly AI referrals in 6 months… $38K" (not graded) | — | — | — | — (handed to REPULL-1) |
| A11 | 5 | aicited.org / "national insurance carrier 310%" | hcpa (insurance) | aicited.org/case-analyses/how-a-national-insurance-carrier-achieved-a-310-increase-in-ai-citations-through-p… | not reachable — fetch error | — | — | — | — | — | — | — |
| A12 | 5 | Growtika / bootstrapped startup | none | growtika.com/blog/geo-case-study | not reachable — page body not rendered to fetch (1,168 characters) | — | — | — | — | — | — | — |
| A13 | 5 | WPP, Publicis, Omnicom, Dentsu, Havas, IPG | none | DuckDuckGo results: wpp.com/case-studies, wppmedia.com/case-studies, publicissapient.com/customers/stories, omc.com "Omnicom Health Winning in AI Search" guide | screened — no AI-visibility client case with a number in results | — | — | — | — | — | — | — |
| X1 | 7 | OtterlyAI / Reddit engagement experiment | none (tactic test, vendor-created communities) | otterly.ai/blog/reddit-geo-ai-search-citations/ | **Silver** | **Silver** | none | AI citations 48 (dormant arm) vs 426 (active arm), April 11 → June 10, 2026; 60 threads per arm; six engines | **experimental** — concurrent two-arm comparison, one community per arm; arms unmatched (subscribers 7 vs 1,485; median post 670 vs 19.5 words); vendor calls it "observational study" | up | n/a — vendor's own | e-case-otterly-reddit-experiment |
| X2 | 7 | OtterlyAI / HTML vs Markdown | none | otterly.ai/blog/geo-experiment-html-vs-markdown/ | Silver | Bronze | 3 (14 days, dates not printed) | AI citations of .md pages 0; AI bot visits .md 0% vs HTML 2.8–4.6% | **experimental** — paired pages, same site, same window | **null** (tactic) | n/a | e-case-otterly-html-vs-markdown-experiment |
| X3 | 7 | OtterlyAI / llms.txt, 90 days | none | otterly.ai/blog/the-llms-txt-experiment/ | Bronze | Bronze | 3, 4 | /llms.txt 84 of 62,100+ AI bot visits (0.1%) vs ~265 per average page | observational | **null** | n/a | e-case-otterly-llms-txt-experiment |
| X4 | 7 | OtterlyAI / FAQ on homepage (GEO guide) | none | otterly.ai/blog/geo-gsvo/ | Bronze | Bronze | 3, 6 | citations 529 → 2,379 (~350%) "in the comparison window" | observational | up | n/a | e-case-otterly-geo-guide-experiment-claims |
| X5 | 7 | Jonathan Mall / anonymised "Brand A" | none (expert services, German-language answers) | jonathanmall.com/en/geo-experiment-ai-citation-test/ | Silver | Bronze | 1 (niche deliberately vague), 3 (July 2 → July 9, year not printed) | 1,353 matched ChatGPT queries: citations 171 gained vs 32 lost (5.3:1) against a measured noise floor (Jaccard 0.35); treated page 23 → 72 citing queries; untreated explainers down; mentions +32 / −27 | **experimental** — pre/post, within-site untreated pages, noise floor measured first | up (citations); **null** (mentions) | n/a — anonymised | e-case-jonathanmall-geo-experiment |
| X6 | 7 | Boily / two Korean dental clinics | none (healthcare) | boily.co.kr/guide/geo-repair-case-2026-06 | Silver | Bronze | 3 (two weeks, slug 2026-06, no dates) | mention rate, 100 fixed queries × ChatGPT, Claude, Gemini, Perplexity: treated 11% → 27%; untreated 11% → 10% | **experimental** — pre/post with one untreated comparison clinic (N=2); vendor: "not a controlled A/B" | up | n/a — clinics anonymised | e-case-boily-dental-geo-comparison |
| X7 | 7 | AI+Automation / Princeton GEO replication, 3,205 pages | none | aiplusautomation.com/blog/princeton-geo-replication-failure | not graded — not a brand case; cross-sectional replication | — | — | statistics density replicates; citation and quotation density wrong direction (Google AI Mode p = 0.008) | observational | **null** (2 of 3 claims) | — | not pulled — P14-papers cross-reference |
| X8 | 7 | Search Engine Land / "Two GEO experiments challenge conventional AI visibility advice" | none | searchengineland.com/geo-experiments-challenge-conventional-ai-visibility-advice-488342 | not reachable — HTTP 403 | — | — | snippet: citations by platform ChatGPT 148, Claude 96, Gemini 87, Perplexity 64 (not graded) | — | — | — | — |
| E1 | 1 | Yext 8-K EX-99.3, 2026-09-01 — own brand | b2b | sec.gov …/ex993q2fy27productupdatepr.htm | Bronze | Bronze | 3, 4, 6 | "grow its AI visibility by 147%… in only two weeks" (vendor on itself) | observational | up | filed | e-case-edgar-fulltext-results |
| E2 | 1 | TechTarget 10-K, 2026-03-11 | b2b (tech media) | sec.gov …/ttgt-20251231.htm | screened — no claim (cross-sectional ratio) | — | — | "2x to 3x higher membership conversion rate from answer engine and LLM citations compared to traditional organic search" — no before/after | observational | — | filed | e-case-edgar-fulltext-results |
| E3 | 1 | TechTarget 8-K, 2025-08-12 | b2b | sec.gov …/ttgt-ex99_1.htm | action named, outcome unknown | — | — | "over 50,000 AI overviews monthly… substantial increase in traffic" — no number | — | up (no number) | filed | e-case-edgar-fulltext-results |
| E4 | 1 | Coty 10-K, 2026-08-20 | skin | sec.gov …/coty-20260630.htm | action named, outcome unknown | — | — | "deploying improvements across touchpoints to drive generative engine optimization" | — | — | filed | e-case-edgar-fulltext-results |
| E5 | 1 | LendingTree 8-K, 2026-07-29 | hcpa | sec.gov …/tree-63026xer.htm | action named, outcome unknown | — | — | "launched several new consumer-facing AI capabilities such as our ChatGPT app" | — | — | filed | e-case-edgar-fulltext-results |
| E6 | 1 | Chime DRS/A, 2025-01-29 | hcpa borderline | sec.gov …/filename1.htm | action named, outcome unknown (content generation with ChatGPT; not a visibility metric) | — | — | no | — | — | filed | e-case-edgar-fulltext-results |
| E7 | 1 | Freshworks 10-K, 2026-02-26 | b2b | sec.gov …/frsh-20251231.htm | action named, outcome unknown | — | — | "Traffic from large language model (LLM)-based platforms… small portion… growing in recent quarters" — no number | — | up (no number) | filed | e-case-edgar-fulltext-results |
| E8 | 1 | HubSpot DEF 14A, 2026-04-27 | b2b | sec.gov …/hubs-20260427.htm | action named, outcome unknown | — | — | "AI referrals are now tracked as a lead source" | — | — | filed | e-case-edgar-fulltext-results |
| E9 | 1 | JOINT Corp 8-K, 2026-08-06 | none | sec.gov …/a8-05x26q22026resultsdec.htm | action named, outcome unknown | — | — | "SEO and AI visibility optimization driving organic traffic and lead quality" — no number | — | up (no number) | filed | e-case-edgar-fulltext-results |
| E10 | 1 | Klarna 6-K, 2026-08-18; Etsy 8-K, 2026-04-29; Rent the Runway 10-Q, 2026-09-11; ZipRecruiter 8-K, 2026-05-07 | none | per raw | action named, outcome unknown ×4 | — | — | "grew sharply"; "strong growth"; "some positive results"; ChatGPT app — no AI number | — | up (no number) | filed | e-case-edgar-fulltext-results |
| E11 | 1 | High Roller (Lines.com) 8-K, 2026-01-21 and 2026-04-20; Yelp 8-K, 2026-08-06 | none | per raw | screened — no claim (cross-sectional citation counts) | — | — | "nearly 800 AI citations… more than three times key competitors"; Yelp "3.4x as many AI citations", Q4 2025, commissioned | observational | — | filed | e-case-edgar-fulltext-results |
| E12 | 1 | Publisher and marketplace headwind filings (People Inc/IAC, Chegg, TNL Mediagene, Gambling.com, trivago, Expedia, Perion, Fiverr, Zedge, ZoomInfo, 1-800-Flowers, Root risk factors) | none | per raw | not graded — no brand visibility action; sector headwind statements | — | — | e.g. People Inc 10-Q 2026-08-03 "22% decline in Core Sessions, due primarily to… Google AI Overviews" | observational | negative (sector) | filed | e-case-edgar-fulltext-results |

Per vertical, this pull (grade_rule1):

| Vertical | Candidates screened this pull | Bronze or better | Fools gold | Silver | Gold | Action named, outcome unknown | Negative / null |
|---|---|---|---|---|---|---|---|
| Skincare and beauty | 22 — cases V1, A1, A2, A10, B2, E4; brand pages P&G, Revlon, Omnilux, Stella Rising, Sorbet, Fresha; EDGAR per-CIK ELF, EL, ULTA, COTY; DuckDuckGo skincare query 10 entries (counted once) | 3 (V1, A1, A2) | 1 (B2) | 0 | 0 | 1 (E4) | 0 |
| B2B SaaS | 41 — cases T1, T2, T5, T6, T9, T10, T12, V2, V3, V5, A3, A8, A9, E1–E3, E7, E8; 23 brand pages | 6 (T12, V3, V5, A3, A9, E1) | 3 (T10, V2, A8) | 0 | 0 | 3 (E3, E7, E8) | 1 (A9) |
| High-CPA regulated | 21 — cases T7, B1, V8, A5, A6, A7, A11, E5, E6; brand pages CRS, Chime, MidFirst, Jerry; EDGAR per-CIK NRDS, TREE, EVER, LMND, ROOT, MAX, SLQT, QNST, PGR, ALL | 3 (T7 borderline, B1 borderline, V8) | 0 | 0 | 0 | 2 (E5, E6) | 0 |

### Reddit rows (Arctic Shift archive, comments endpoint)

| # | Ch | Candidate | Vertical | URL | grade_raw | grade_rule1 | Items absent | Metric moved — metric, from → to, window | Design | Direction | Brand side | Raw |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Reddit | r/SEO comment, 2026-09-03, unnamed site | none | reddit.com/r/SEO/comments/1w5uv4c/…/p7iakjf/ | discard on sight — one account, no brand, no method | — | 1, 3, 6, 7 | Google generative-AI impressions 5K → 15K daily from August 1, "no traffic increase at all"; ~300 Copilot visits | observational | **null** (traffic) | n/a | e-case-reddit-arcticshift-comments |
| R2 | Reddit | r/PPC comment, 2026-09-17, ZapDigits ChatGPT Ads test (paid placement) | b2b | reddit.com/r/PPC/comments/1v961ix/…/pacw1r4/ | Fools gold | Fools gold | 3, 4, 7; no control | spend ~$4,800, ~310k impressions, ~8,900 clicks, 620 signups, 87 paid conversions, CAC ~$55 | observational | — (no baseline) | n/a | e-case-reddit-arcticshift-comments |

Reddit screen: 45 calls planned (9 subreddits × 5 queries), 31 returned data, 14 failed (HTTP 422 ×9, 429 ×5); 221 comments returned; 25 passed a filter for a number plus a test/result word plus an AI-engine term; 2 carry a site-level metric (R1, R2); 0 name a brand with a before/after and a control.

## Pass 3 unopened and unreachable titles — resolution

| c13 line | Title | Resolution 2026-09-23 | Row |
|---|---|---|---|
| 157 | AirOps ×9 — Kong, Conviva, Two Independent Practitioners, Animalz, Bitly, Merge, Venn, Harvard Business Publishing, Rhetoric | all 9 opened | T1–T9 |
| 126 | Otterly ×5 — Chatarmin, NOLA Marketing, SORN.AI, What IF Web, TM Blast | 4 opened; TM Blast not reachable (LinkedIn video) | T10–T14 |
| 30 | Searchable / Blackbird | opened (searchable.com/customers/blackbird) | T15 |
| 243 | Orange142 / Pigeon Forge | opened (orange142.com/blog/…-136) | T16 |
| 250 | c6 sell-side group (~35 clients) | 16 client pages opened (Feedonomics 12 via sitemap, Kargo 4); Criteo and Pacvue client pages not reachable by fetch (sitemaps empty, index JS-rendered); remaining named Feedonomics clients have no page in feedonomics.com/sitemap | T17 |
| 245 | Seer Interactive / Home Depot (unreachable) | opened via Wayback 2026-07-22; guide authored for Semrush, not a Seer case | T18 |
| 243 | Orange142 / Green Energy (unreachable) | still not reachable: 404, no Wayback capture | T19 |

## Brand pages — found / silent / unreachable

Search substitute: WebSearch site: queries (72 calls in this pull) until the session cap of 200 WebSearch calls was reached; see §Blocked. Every row names the domain searched. `found` means the brand's own domain names the vendor, the programme or an own AI metric; `corroborates` is used only where the brand's page states the vendor's result.

| Brand | Vendor / programme | Vertical | Domain checked | Query | Reads | Note |
|---|---|---|---|---|---|---|
| Coach | Searchable | none (fashion) | coach.com; tapestry.com | WebSearch site: "Searchable" AI search | silent | no brand-domain page names Searchable |
| KPMG | Searchable | none (professional services) | kpmg.com | WebSearch site: "Searchable" AI visibility | silent | only generic "searchable data" articles |
| DigitalOcean | Searchable | B2B SaaS (cloud) | digitalocean.com | WebSearch site: "Searchable" AI search visibility | silent | only product docs, listicles |
| Revlon | Searchable; Pacvue | skincare/beauty | revlon.com | WebSearch site: "Searchable" OR "AI search" OR ChatGPT | silent | no revlon.com page returned |
| BCG | Searchable | none (consulting) | bcg.com | WebSearch site: "Searchable.com" OR "Searchable AI" | silent | BCG X "Future of Discoverability" article, no vendor named |
| 1-800-Flowers | Searchable | none (gifting retail) | 1800flowers.com; 1800flowersinc.com | WebSearch site: "Searchable" OR "AI search" ChatGPT | silent | no match |
| Heights | Searchable | none (supplements DTC) | heights.com (brand domain; yourheights.com redirects) | WebSearch "Heights" "Searchable" AI search | silent | only review sites returned |
| Lottie | Searchable | none (health-tech care homes) | lottie.org | WebSearch "Lottie" "Searchable" case | silent | search returns Searchable co-founder Chris Donnelly engineered Lottie growth (founder link, not brand-side) |
| Bolt | Searchable | none | bolt.com / bolt.eu (identity unresolved) | WebSearch "Bolt" "Searchable" case | silent | identity not resolved |
| Fi | Searchable | none (pet tech) | tryfi.com | WebSearch site: "Searchable" OR "AI search" OR ChatGPT | silent | no tryfi.com page returned |
| Glenmuir | Searchable | none (apparel) | glenmuir.com | WebSearch site: "Searchable" AI visibility | silent | no page returned |
| Amadeus | Searchable | none (travel tech) | amadeus.com | WebSearch site: "Searchable" AI visibility | silent | only "searchable cruise lines" product copy |
| 1mind | Searchable | B2B SaaS (AI sales agents) | 1mind.com | WebSearch site: "Searchable" | silent | 1mind.com pages returned, none name Searchable |
| 303 | Searchable | none (agency) | identity unresolved | n/a | silent — domain not resolved | Searchable case subject; no brand domain located |
| Blackbird | Searchable | none (AI search agency) | blackbird (agency) domain not resolved | WebSearch | silent — domain not resolved | case page opened (see census titles) |
| n8n | Peec AI | B2B SaaS | n8n.io | WebSearch site: "Peec AI" OR "Peec" | silent | only integration pages |
| Graphite | Peec AI | B2B SaaS | graphite.dev | WebSearch site: "Peec AI" OR "Peec" | silent | no page returned |
| Glide | Peec AI | B2B SaaS | glideapps.com | WebSearch site: "Peec AI" OR "Peec" | silent | no page returned |
| Amsive | Peec AI | none (agency) | amsive.com | WebSearch site: "Peec AI" | found — tool mention only | amsive.com/insights/seo/google-i-o-2025-announcements-takeaways-impacts-on-seo/ names Peec AI among LLM tracking tools; no programme or result |
| NXT Pharma | Promptwatch | none (pharma) | nxtpharma.com | WebSearch site: "Promptwatch" | silent | no page returned |
| Six Group | Promptwatch | none (financial infrastructure) | six-group.com | WebSearch site: "Promptwatch" | silent | no match |
| Center Parcs | Promptwatch | none (travel) | centerparcs.com | WebSearch site: "Promptwatch" | silent | no match |
| Schoonenberg | Promptwatch | none (hearing care) | schoonenberg.nl | WebSearch site: "Promptwatch" | silent | no match |
| Octolize | Promptwatch | B2B SaaS (Woo plugins) | octolize.com | WebSearch "Promptwatch" Octolize | silent | testimonial only on promptwatch.com |
| Landytech | Promptwatch | B2B SaaS (fintech) | landytech.com | WebSearch "Promptwatch" Landytech | silent | testimonial only on promptwatch.com |
| Marvia | Promptwatch | B2B SaaS | marvia.com | WebSearch "Promptwatch" Marvia | silent | testimonial only on promptwatch.com |
| Everflow | Promptwatch | B2B SaaS | everflow.io | WebSearch "Promptwatch" Everflow | silent | testimonial only on promptwatch.com |
| Wortell | Promptwatch | none (IT services) | wortell.nl | WebSearch "Promptwatch" Wortell | silent | no match |
| Monks | Promptwatch | none (agency) | monks.com | WebSearch "Promptwatch" Monks | silent | no match |
| Crisp | Promptwatch | B2B SaaS | crisp.chat | WebSearch "Promptwatch" Crisp | silent | no match |
| OpenUp | Promptwatch | none (mental health) | openup.com | WebSearch "Promptwatch" OpenUp | silent | no match |
| WHOOP | Profound | none (wearables) | whoop.com | WebSearch site: "Profound" AI search visibility | silent | press center pages, no vendor |
| Statsig | Profound | B2B SaaS | statsig.com | WebSearch site: "Profound" | silent | no match |
| One Identity | Profound | B2B SaaS (security) | oneidentity.com | WebSearch site: "Profound" | silent | no page returned |
| Alchemy | Profound | B2B SaaS (web3 infra) | alchemy.com | WebSearch site: "Profound" | silent | no page returned |
| Omnilux | Profound | skincare/beauty (LED devices) | omnilux.com | WebSearch site: "Profound" | silent | no page returned |
| Jordan Digital Marketing | Profound | none (agency, B2B/fintech clients) | jordandigitalmarketing.com | WebSearch site: "Profound" AI visibility | found — programme named, no result | jordandigitalmarketing.com/services/ai-llm-search names Profound as its reporting platform |
| Popl.co | AthenaHQ | B2B SaaS | popl.co | WebSearch site: "AthenaHQ" OR "Athena" | silent | only athenahq.ai case page returned |
| CRS Credit API | Profound | high-CPA regulated (credit data API) — borderline | crscreditapi.com | WebSearch site: "Profound" OR "AI search" OR ChatGPT | silent | only an unrelated fraud-API article on own domain |
| Mastercard | RankPrompt (logo) | none (payments) | mastercard.com | WebSearch "RankPrompt" Mastercard OR P&G OR 7-Eleven | silent | logo only on rankprompt.com |
| P&G | RankPrompt (logo) | skincare/beauty (CPG incl. beauty) | pg.com | same combined query | silent | no brand-domain hit |
| 7-Eleven | RankPrompt (logo) | none (convenience retail) | 7-eleven.com | same combined query | silent | no brand-domain hit |
| BMW | Sitefire | none (auto) | bmw.com; bmwgroup.com | WebSearch site: "Sitefire" | silent | no match |
| Xtrackers / DWS | Sitefire | none (asset management) | dws.com; etf.dws.com | WebSearch site: "Sitefire" | silent | no match |
| Wemolo | Sitefire | none (parking tech) | wemolo.com | WebSearch site: "Sitefire" OR "AI search" | silent | own parking-product pages only |
| Chamber | Sitefire | B2B SaaS (YC W26) | chamber.so | WebSearch site: "Sitefire" OR "AI search" | silent | no page returned |
| Runpod | Scrunch | B2B SaaS (GPU cloud) | runpod.io | WebSearch site: Scrunch OR ChatGPT "acquisition channel" | silent | product docs only |
| Proper Propaganda | Scrunch | none (tech PR agency) | properpropaganda.net | WebSearch site: "Scrunch" | found — programme and result | own case study names Scrunch; share of answer 10%, Perplexity 15%, 2 signed clients (vendor page: 5x lead gen). Raw: e-case-brandside-found-multi-2026-09-23.md |
| Clapping Dog Media | Scrunch | none (agency) | clappingdogmedia.com | WebSearch site: "Scrunch" | found — tool mention only | clappingdogmedia.com/seo-consult/ names Scrunch AI in its audit; no result |
| AlchemyLeads | Scrunch | none (agency) | alchemyleads.com | WebSearch site: "Scrunch" | silent | no page returned |
| Instant Commerce | Otterly | B2B SaaS (commerce) | instantcommerce.io | WebSearch site: "Otterly" OR "AI search" OR ChatGPT | silent | no page returned |
| Videoloft | Otterly | none (video security) | videoloft.com | same query | silent | no page returned |
| Bacula | Otterly | B2B SaaS (backup software) | baculasystems.com | WebSearch site: "Otterly" OR "ChatGPT" ranking | silent | no page returned |
| Slopelift | Otterly | none (agency) | slopelift.com | WebSearch site: "Otterly" | silent | no page returned |
| Stella Rising | Otterly | skincare/beauty (beauty agency) | stellarising.com | WebSearch site: AI search OR GEO OR Otterly | silent on vendor | GEO service and LLM-survey pages on own domain; Otterly not named |
| Neur Digital | Otterly | none (medspa and med-device agency) | neurdigital.com | WebSearch site: "Otterly" | found — partner mention | neurdigital.com/ai-search-monitoring-services/ names Otterly as its monitoring tool; no result |
| Docebo | AirOps | B2B SaaS (LMS) | docebo.com | WebSearch site: "AirOps" | silent | only airops.com pages returned |
| Webflow | AirOps | B2B SaaS (web platform) | webflow.com | WebSearch site: "AirOps" AI search citations | found — integration listing only | webflow.com/integrations/airops; no customer result |
| Chime | AirOps | high-CPA regulated (consumer banking, secured credit card) — borderline | careers.chime.com (c7 checked chime.me, a different company) | WebSearch site:chime.com "AirOps" OR "AI search" citations | found — corroborates result | careers.chime.com article 2025-11-24: AirOps named; "tripled our AI citations and increased content velocity by 70 percent". Raw: e-case-chime-careers-airops-2026-09-23.md |
| Optimizely | Conductor (AgentStack partner) | B2B SaaS (DXP) | optimizely.com | WebSearch site: "Conductor" AgentStack OR "AI search" | found — partnership programme | optimizely.com press release 2026-06-10; no result metric. Raw: e-case-brandside-found-multi-2026-09-23.md |
| Razorfish | Conductor (partner) | none (agency) | razorfish.com | WebSearch site: "Conductor" AI search | silent | AI-search articles; Conductor not named |
| Havas | Conductor (partner) | none (agency) | havas.com | same query | silent | no page returned |
| IBM | Conductor (partner) | none (IT) | ibm.com | WebSearch site: "Conductor" "AgentStack" | silent | IBM quote appears only in third-party copies of Conductor's release |
| Sandler | HubSpot | none (sales training) | sandler.com | WebSearch site: "HubSpot AEO" OR "answer engine optimization" | silent | HubSpot CRM pages only |
| Scrums | HubSpot | B2B SaaS (dev staffing) | scrums.com | WebSearch site: AI search ChatGPT visibility | silent | own AI-product pages; HubSpot AEO not named |
| Anedot | HubSpot | B2B SaaS (donations) | anedot.com | WebSearch site: "HubSpot AEO" | silent | no page returned |
| Fresha | HubSpot | skincare/beauty (beauty and wellness booking) — borderline | fresha.com | WebSearch site: "HubSpot AEO" OR "answer engine optimization" | silent on vendor; own AI-bookings metric found | fresha.com/blog/fresha-ai-booking-growth 2026-02-24. Raw: e-case-fresha-ai-bookings-2026-09-23.md |
| MidFirst Bank | Yext | high-CPA regulated (banking) — borderline | midfirst.com | WebSearch site: "Yext" Scout AI search | silent | banking product pages only |
| Beltone | Yext | none (hearing care) | beltone.com | same query | silent | no page returned |
| Sorbet | Yext | skincare/beauty (beauty salons) | sorbetbeauty.com (domain inferred) | WebSearch site: AI search ChatGPT visibility | silent | no page returned |
| Arm | BrightEdge | B2B (semiconductor IP) | arm.com | WebSearch site: "BrightEdge" OR "AI agent traffic" | silent | only brightedge.com case page returned |
| Overdrive Interactive | BrightEdge | none (agency) | ovrdrv.com | WebSearch site:overdriveinteractive.com "BrightEdge" | silent | ovrdrv.com/ai-info returned; BrightEdge not named |
| Three Rings | Muck Rack | none (PR agency) | threeringsinc.com | WebSearch site: "Muck Rack" OR "Generative Pulse" | silent — blog index returned, not opened | threeringsinc.com/in-the-ring-blog |
| CloudEagle | Quattr | B2B SaaS | cloudeagle.ai | WebSearch site: "Quattr" | silent | no page names Quattr |
| Housing.com | Quattr | none (real estate portal) | housing.com | WebSearch site: "Quattr" OR "AI search" | silent | only quattr.com pages returned |
| Kiteworks | Quattr; Profound | B2B SaaS (secure content) | kiteworks.com | WebSearch site: "Quattr" | found — programme named; result is classical organic | press release 2023-06-07: Quattr "doubled inbound organic search traffic"; no AI-engine result. Raw: e-case-brandside-found-multi-2026-09-23.md |
| Coalition Technologies | Semrush | none (agency) | coalitiontechnologies.com | WebSearch site: "Semrush" AI referral traffic case | silent on case | own blog uses Semrush data; +429% case not restated |
| Batteries Plus | SOCi | none (retail) | batteriesplus.com | WebSearch site: "SOCi" OR "AI search" | silent | no page returned |
| Dell; Logitech; New Balance; Pacsun; Cole Haan | Feedonomics | none (retail, electronics) | dell.com; logitech.com; newbalance.com; pacsun.com; colehaan.com | WebSearch "Feedonomics" with five site: operators | silent | no page names Feedonomics |
| Euro Car Parts; Coldwater Creek | Feedonomics | none (retail) | eurocarparts.com; coldwatercreek.com | WebSearch "Feedonomics" site: | silent | no page names Feedonomics |
| Unice; Denon Store; Netshoes | Criteo | none (retail) | unice.com; denon.com; netshoes.com.br | WebSearch "Criteo" site: ChatGPT | silent | Netshoes product pages only |
| Itsumo; Perdue; Duracell | Pacvue | none (CPG) | itsumo.com; perduefarms.com; duracell.com | WebSearch "Pacvue" site: | silent | no page names Pacvue |
| Hershey's; Anytime Fitness; American Eagle; WeTransfer | Kargo | none | thehersheycompany.com; anytimefitness.com; ae.com; wetransfer.com | WebSearch "Kargo" site: | silent | only a street address 'Jalan Kargo' |
| HP Toast; CTV Glass | Kargo | none | identity not resolved | n/a | silent — domain not resolved | names as printed on the Kargo index |
| Window Well Supply | Intero Digital | none (home goods) | windowwellsupply.com | WebSearch "Intero Digital" site: | found — agency byline only | blog posts carry an "Intero Web Division" byline; no result |
| Sticker Mountain | Intero Digital | none | stickermountain.com | same query | silent | no page returned |
| Hinge Health | Fire&Spark | none (digital health) | hingehealth.com | WebSearch site: "Fire&Spark" OR "AI search" | silent | only fireandspark.com pages returned |
| Home Depot | Seer Interactive | none (home improvement) | homedepot.com; corporate.homedepot.com | WebSearch site: "Seer Interactive" OR "LLM visibility" | silent | product pages only |
| Aleph | Profound | B2B SaaS (FP&A); domain resolved getaleph.com | getaleph.com | WebSearch site: "Profound" OR "AI search" OR AEO | silent | no getaleph.com page returned |
| Owings Auto | RankPrompt | none (auto dealer); domain resolved owings-auto.com | owings-auto.com | WebSearch "Owings Auto" RankPrompt | silent on vendor | owings-auto.com/llm-info/ AI-assistant info page; RankPrompt not named |
| Activate Digital | Semrush | none (agency) | domain not resolved | WebSearch "Activate Digital" Semrush | silent — domain not resolved | vendor story only: semrush.com/company/stories/activate-digital-ai-visibility/ |
| Men's Wearhouse (E1 re-check) | Quattr | none (apparel) | menswearhouse.com; tailoredbrands.com | WebSearch site: "Quattr" OR "AI Mode" OR ChatGPT | silent | blog AI-summary buttons; Quattr not named |
| Pointhound (E2 re-check) | Sitefire | none (travel) | pointhound.com | WebSearch site: "Sitefire" OR ChatGPT OR "AI search" | silent | card-benefit page only |
| Jerry.ai (E3 re-check) | Sitefire | high-CPA regulated (auto insurance) | jerry.ai | WebSearch site: "Sitefire" OR "AI search" OR ChatGPT referral | silent | 2021 newsroom item only |
| Nuvadermis / Lyra Collective | AthenaHQ | skincare/beauty (scar care) | not checked | n/a | unreachable — WebSearch session cap reached | new case this pull |
| Pigeon Forge Dept. of Tourism | Orange142 | none (travel DMO) | ir.directdigitalholdings.com 2026-02-10 release (co-named) | fetch | found — co-announced programme, no result | brand's own domain not checked |

Reads: 109 brands in 96 rows — found 11 (1 corroborates a result: Chime; 1 programme plus a different result: Proper Propaganda; 9 programme, integration, partnership, tool or byline only); silent 97 (incl. 6 whose domain was not resolved — 303, Blackbird, Bolt, Activate Digital, HP Toast, CTV Glass — and 3 silent on the vendor with an own AI page: Fresha, Stella Rising, Owings Auto); contradicts 0; unreachable 1 (Nuvadermis — search cap). Four c7 unknowns re-resolved: Aleph → getaleph.com (silent); Owings Auto → owings-auto.com (silent on vendor); Chime → chime.com, not chime.me (found — corroborates); Activate Digital (still unresolved).

Not checked this pull: Chatarmin, NOLA Marketing, SORN.AI / PagePilot, What IF Web, TM Blast, Venn, AutoRFP.ai, Lago, Apartment List, Arrow Senior Living, Bitly, Kong, Conviva, Merge, Rhetoric — WebSearch session cap reached before these were queued; Locafy's 8 unnamed testimonials — not checkable (no names).

Silver-or-better cases, brand-side: E1 Men's Wearhouse, E2 Pointhound, E3 Jerry.ai re-checked with WebSearch — all silent. E4 Seer client, E5 self-authored, E6 filing, E7 paper — n/a as before. New Silver raw X1, X2 (vendor's own experiments), X5, X6 (anonymised) — n/a.

## Vendor sitemaps scanned for case pages modified since 2026-09-01

36 domains: scrunch.com (no sitemap urls), tryprofound.com (11), athenahq.ai (7), conductor.com (0), rankprompt.com (0), sitefire.ai (0), brightedge.com (1), quattr.com (0), semrush.com (0), rankscale.ai (0, no lastmod), peec.ai (0), promptwatch.com (1, a bot page), searchable.com (0), airops.com (8), otterly.ai (0), yext.com (803, lastmod churn across locales — only /customers/ paths read: accor-live-limitless), www.peec.ai (0), geosurge.ai (0), brandlight.ai (0, no lastmod), birdeye.com (13), locafy.com (2), muckrack.com (0), onclusive.com (2), seranking.com (0), soci.ai (4), uberall.com (9, index pages), pacegenerative.com (0), orange142.com (0, no lastmod), interodigital.com (0), seerinteractive.com (0), fireandspark.com (1), stackadapt.com (11, blog and webinar pages), pacvue.com (0), kargo.com (10), feedonomics.com (0 new), changeagents.ai (0). Sitemap lastmod is a modification date, not a publication date; pages were opened to check whether the case is new to this programme (rows V1–V12).

## DuckDuckGo html queries (after the WebSearch cap)

1 "GEO case study control group ChatGPT citations"; 2 "WPP generative engine optimization case study results"; 3 "Publicis AI search visibility case study client"; 4 "Omnicom AI search optimization brand results"; 5 "skincare brand AI search visibility case study ChatGPT increase"; 6 "insurance AI search visibility case study ChatGPT citations increase"; 7 "supplement brand ChatGPT visibility case study"; 8 "credit card AI search GEO case study" (no results parsed); 9 "brightonSEO 2026 GEO test results slides"; 10 "MozCon 2026 AI search experiment results"; 11 "SMX Advanced 2026 AI Overviews test results brand"; 12 "Shoptalk 2026 ChatGPT traffic brand results"; 13 "INBOUND 2026 AEO results HubSpot traffic AI"; 14 "GEO did not work no increase AI citations experiment"; 15 "AI Overviews traffic loss case study skincare brand" and 16 "GEO experiment failed citations did not change" (both returned after the output limit; not read). Queries 2–4 and 9–13 returned case indexes, recaps and decks; none opened carried a brand before/after other than rows A8, A9.

## Blocked and deferred

| Channel | URL | What was needed | Block type | Status |
|---|---|---|---|---|
| WebSearch | tool | brand-page and agency searches | session cap — "used its web search budget (200 of 200 WebSearch calls)"; this agent made 72 | open — DuckDuckGo html used as substitute |
| Reddit posts | arctic-shift.photon-reddit.com/api/posts/search | practitioner posts | rate limit / timeout ("Timeout. Maybe slow down a bit"); HTTP 422 | open — comments endpoint used |
| reddit.com live | reddit.com | — | extension-only channel; deferred per brief | deferred to ext |
| G2, Capterra | g2.com, capterra.com | negative reviews | extension-only channels | deferred to ext |
| careers.chime.com | live page | brand-side text | Cloudflare block (fetch 403, Playwright block page) | Wayback copy used |
| searchengineland.com | two URLs | Home Depot guide; "Two GEO experiments" article | Cloudflare (Playwright challenge, fetch 403) | Wayback copy used for the first; second not reached |
| muckrack.com/customers | — | Three Rings case | HTTP 403 | not reached |
| Criteo, Pacvue client case pages | criteo.com, pacvue.com | c6 client cases | no sitemap URLs, JS-rendered index | not reached |

## Paywalled or truncated — handed to REPULL-1

| URL | Block | Raw file carrying the secondary |
|---|---|---|
| https://grro.io/blog/case-study-ecommerce-ai-visibility | HTTP 402 Payment Required | none — DuckDuckGo snippet only, quoted in row A10 of this census |
| https://www.aicited.org/case-analyses/how-a-national-insurance-carrier-achieved-a-310-increase-in-ai-citations-through-p… | fetch error, URL truncated in search result | none — row A11 |
| https://searchengineland.com/geo-experiments-challenge-conventional-ai-visibility-advice-488342 | HTTP 403 | none — snippet in row X8 |
| https://www.linkedin.com (TM Blast video, Otterly teaser) | login wall | raw/a-otterly-customers-2026-09-22.md (teaser text) |

## Pull notes — mechanical only

- Every URL in the register was fetched 2026-09-23. Raw-file names in the Raw column omit the `-2026-09-23.md` suffix where abbreviated.
- WebSearch session cap hit after 72 calls by this agent; 4 further calls refused. DuckDuckGo html endpoint used thereafter at 6-second spacing.
- Image rule (coordinator, 2026-09-23): pages opened after the instruction were the 12 Feedonomics and 2 Kargo client pages; their images are logos, navigation icons and lifestyle photos — decorative, none saved; `docs/raw/img/INDEX.csv` unchanged.
- The ~980 candidates of Passes 3 and 4 were not re-screened; overlap was checked by grep of `docs/raw/` for every new case name before opening.
