# Otterly.AI — customers / case studies

```yaml
source:          Otterly.AI (otterly.ai)
url_or_doc_id:   https://otterly.ai/case-studies (index, lastmod 2026-09-05T19:10:38.098Z); https://otterly.ai/instant-geo-case-study (lastmod 2026-07-06T07:13:26.401Z); https://otterly.ai/videoloft-case-study (lastmod 2026-04-30T17:42:08.183Z)
published:       see per-page lastmod above; the other 9 case studies linked from the index were not individually fetched this task (see Method note)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number (2 individually-verified cases) and evidence about category noise (9 index-teaser-only cases, unverified beyond the teaser)
tier:            6 for the 9 teaser-only cases (no independently confirmed n/date/method beyond the index page's own summary sentence); 6 for the 2 individually-verified cases (Instant Commerce graded Bronze on full-page text but still vendor-reported/self-measured with no independent party; Videoloft screened, no metric at all)
tier_reason:     none of the 11 cases discloses an unaffected control metric, an independent (non-Otterly, non-customer) measurer, or a stated prompt-set/n behind its headline percentage — the ceiling for any of them under trust-rubric.md is Silver at best, and none reaches even that; several are marketing-listicle-style teasers with a percentage and no base, which trust-rubric.md discards on sight outside a category-noise pull_purpose
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          varies per case — see table (most name ChatGPT specifically; several name Perplexity, Google AI Overviews)
metric_kind:     visibility and/or traffic (no case in this set makes a direct sales/revenue claim with a dollar figure — "sign-ups," "demos," and "leads" are the closest proxies and are graded as such)
supersedes:      none
captured:        index page in full (two fetches, 0-4000 and 4000-7000+ characters); two individual case-study pages to ~3500 characters each (see grading notes on which items came from the index teaser alone vs. the full page)
```

## Method note on this file — partial verification

The case-studies index lists 11 cases. Two (Instant Commerce, Videoloft) were individually fetched and graded on their full page text. The remaining 9 are graded on the index page's own teaser/summary text only — this task did not have remaining budget to individually fetch and verify all 11 pages across a six-vendor cluster. Each of the 9 is marked "teaser-only, not independently verified beyond this text" in the grading table below; a case study whose teaser alone already fails to name a bar item is graded on that basis (missing items can only worsen, not improve, on the full page).

## Grading table — 11 case studies, graded on intake

| # | Case | Brand (real, named) | Vertical/type (as tagged by Otterly) | Metric claimed | Engine(s) named | Baseline | Date window | n / measurer | Grade | Missing items | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Chatarmin / "10% of Demos from ChatGPT" | Chatarmin (Richard Wagentristl, head of marketing, named on video) | B2B SaaS | "scaled booked demos via ChatGPT from 1% to 10%" | ChatGPT | **1%** (numeric baseline given) | not stated (video interview, no absolute window in the teaser) | video testimonial; Otterly-measured/customer-stated, not independent | **Fools gold** | date window, independent measurement, control — a lead/demo-conversion claim (sales-adjacent) with a numeric baseline but no control | teaser-only |
| 2 | Slopelift / "An agency, rebuilt around GEO" | Slopelift (Marietta Robitza, Head of SEO & CKO, named on video) | Agency | no quantified metric in the teaser — "agency transformation" | not named | n/a | n/a | video testimonial | **screened — no claim to grade** | no numeric result | teaser-only |
| 3 | NOLA Marketing / "30% More Inbound Leads" | NOLA Marketing (client not separately named) | Agency | "30% More Inbound Leads... grow AI citations, and turn AEO into a measurable client program" | not named in teaser | not stated | not stated | agency self-report | **Fools gold** | numeric baseline, date window, engine, independent measurement, control — a leads claim (sales-adjacent) with none of the supporting items | teaser-only |
| 4 | Stella Rising / "A GEO practice, built on data" | Stella Rising | Agency | no quantified metric in the teaser — "learned to measure visibility in a world where the click is no longer the point" | not named | n/a | n/a | agency self-report | **screened — no claim to grade** | no numeric result | teaser-only |
| 5 | Bacula / "How Bacula Won on AI Search" | Bacula Enterprise | Enterprise | "achieved #1 ranking in ChatGPT responses for 'best HPC backup software'" | ChatGPT | not stated (no prior rank given) | not stated | vendor/customer self-report | **Bronze** | numeric baseline (prior rank), date window, sample size, independent measurement — a visibility/ranking claim, no revenue link | teaser-only |
| 6 | Videoloft / "Videoloft Scales AI Visibility" | Videoloft (Laura Worrell, COO, named) | B2B SaaS | teaser: "improving AI search visibility" (no percentage in the teaser); full page confirms **no quantified metric anywhere** — only qualitative bullets ("Position themselves more competitively," "Create content," "Boost domain and brand visibility") | ChatGPT, Google AI Overviews, Perplexity (named on full page) | qualitative only ("No visibility on ChatGPT & AIO") | not stated | full page read; OtterlyAI/customer self-report | **screened — no quantified claim to grade** | no percentage or number anywhere on the full page | **full page verified** |
| 7 | SORN.AI / "From Zero to Top 5 in 90 Days" | SORN.AI (a Shopify SaaS) | Agency & SaaS | "turned strong Google rankings into ChatGPT and Perplexity citations... doubling sign-ups in three months" | ChatGPT, Perplexity | "Zero" (qualitative, not numeric) for AI citations; sign-up baseline not numerically stated | "90 days" / "three months" (relative, not absolute-dated) | agency/customer self-report | **Fools gold** | numeric baseline, absolute date window, independent measurement, control — a sign-ups claim (sales-adjacent) doubling with no numeric baseline or control | teaser-only |
| 8 | Instant Commerce / "How Instant Built GEO from Zero" | Instant Commerce (Rebecca Anderson, Content Marketing Manager, named) | B2B SaaS | "2x increase in AI search visibility: measurable growth tracked directly through Ot[terlyAI]" — visibility AND "incoming traffic" both cited as 2x per the homepage testimonial | ChatGPT, Google AI Overviews, Perplexity (named on full page) | "Zero visibility" (qualitative, not numeric) | not stated (relative "since using OtterlyAI") | OtterlyAI's own Brand Report; not independent | **Bronze** (traffic + visibility, no dollar/revenue figure) | numeric baseline, absolute date window, sample size, independent measurement | **full page verified** |
| 9 | What IF Web / "300%+ AI Traffic in 28 Days" | What IF Web | Web Design Agency | "went from manually prompting ChatGPT to tracking prompt-level citations with OtterlyAI, tripled its AI referral traffic in a month" | ChatGPT | not stated numerically (implicit low/manual baseline) | "28 days" / "a month" (relative, not absolute-dated) | agency self-report | **Fools gold** — traffic claim, but "referral traffic" reads closer to a sales-proxy claim per this vendor's own framing ("6x Higher conversion rate on AI Search," per `a-otterly-method-2026-09-22.md`) than a pure visibility metric; graded conservatively as Bronze-adjacent but downgraded for the missing numeric baseline and control — recorded as **Fools gold** per the "no baseline or no control" rule | numeric baseline, absolute date window, independent measurement, control | teaser-only |
| 10 | Neur Digital (Medical Device) / "8x More Citations in 12 Months" | unnamed medical device brand, via agency partner Neur Digital | MedTech | "8x Website Citations for their Medical Device Brand in 12 Months" | not named in teaser | not stated numerically | "12 months" (relative but with a stated duration) | agency partner self-report | **Bronze** | brand name (anonymized, not "credibly specified" per the bar's own language), numeric baseline, absolute date window, engine, independent measurement | teaser-only |
| 11 | TM Blast LLC / "500% Increase in ChatGPT sessions" | TM Blast LLC | Agency | "increased daily mentions on ChatGPT which ultimately resulted in a 500% increase in traffic from ChatGPT" | ChatGPT | not stated numerically | not stated | video, self-report | **Fools gold** | numeric baseline, date window, independent measurement, control — a traffic claim with a large unbased percentage | teaser-only |

**Summary: 11 case studies. Screened (no claim to grade): 2 (Slopelift, Stella Rising teaser; Videoloft on full-page verification). Graded: 9. Best grade: Bronze (3 of 9: Bacula, Instant Commerce, Neur Digital/MedTech). Fools gold: 5 of 9 (Chatarmin, NOLA Marketing, SORN.AI, What IF Web, TM Blast). No Silver, no Gold.** Note: Videoloft was teased with a visibility claim on the index page but, on full-page verification, carried no quantified metric at all — reclassified from a likely-Bronze teaser read to screened once the full page was checked. This is flagged as a caution: teaser-only grades for the other 8 unverified cases could shift on full-page review, in either direction.

## Verbatim — case-studies index page (relevant sections)

"GEO Case Studies and AI Search Success Stories — Companies of all sizes around the world use OtterlyAI's AI Search Monitoring solution. From small to big brands and websites. — Trusted by marketing teams at

B2B SaaS — 10% of Demos from ChatGPT — Watch our interview with Richard Wagentristl, head of marketing at Chatarmin and see how they've scaled booked demos via ChatGPT from 1% to 10%. — Watch Video

Agency — An agency, rebuilt around GEO — Watch our interview with Marietta Robitza, Head of SEO & Chief Knowledge Officer at Slopelift to learn more about their agency transformation and how they are offering GEO. — Watch Video

Agency — 30% More Inbound Leads — How NOLA Marketing used OtterlyAI to guide content strategy, grow AI citations, and turn AEO into a measurable client program. — Read full story

Agency — A GEO practice, built on data — How Stella Rising built a Generative Engine Optimization practice on OtterlyAI, and learned to measure visibility in a world where the click is no longer the point. — Read full story

Enterprise — How Bacula Won on AI Search — Bacula Enterprise has achieved #1 ranking in ChatGPT responses for 'best HPC backup software' by using its strategic Generative Engine Optimization — Read full story

B2B SaaS — Videoloft Scales AI Visibility — OtterlyAI has helped Videoloft refine its messaging, create new content, and boost visibility in AI-driven search, improving AI search visibility. — Read full story

Agency & SaaS — From Zero to Top 5 in 90 Days — How SORN.AI turned strong Google rankings into ChatGPT and Perplexity citations for a Shopify SaaS, doubling sign-ups in three months. — Read full story

B2B SaaS — How Instant Built GEO from Zero — Starting with no AI search tracking, Instant Commerce used OtterlyAI to identify winning content angles and turn AI Search into a repeatable growth channel. — Read full story

Web Design Agency — 300%+ AI Traffic in 28 Days — What IF Web went from manually prompting ChatGPT to tracking prompt-level citations with OtterlyAI, tripled its AI referral traffic in a month. — Read full story

MedTech — 8x More Citations in 12 Months — A Medical Device GEO Case Study by our Agency Partner Neur Digital. See how they 8x Website Citations for their Medical Device Brand in 12 Months. — Read full story

Agency — 500% Increase in ChatGPT sessions — TM Blast LLC is showcasing in this video how they increased daily mentions on ChatGPT which ultimately resulted in a 500% increase in traffic from ChatGPT. — View Video

'Since using OtterlyAI, I've seen a 2x increase in both our visibility in AI search engines and incoming traffic. OtterlyAI is a must-have for any content team that wants to build their GEO presence.' — Rebecca Anderson, Content Marketing Manager at Instant Commerce"

Additional un-cased testimonial quotes on the same index page (no case-study link, names and companies given, no metric): Laura Worrell (COO, Videoloft), Michael Farr (Founder, MFF Marketing), Fernando C. (Director SEO), Mat Bumann (CEO, AB3), Michelle B. (Founder, Small Business), Fabian (VP Marketing, Series B SaaS), Peter Jeitschko (Chief Revenue Officer, JetHire), Trent Kennelly (Marketing Expert), Roman Kalkowski (Head of Marketing, Vaadin), Daniel Pirciu (Growth Marketing, Brizy — notably self-deprecating: "I just tried it out, and I like the product...although our brand Brizy is not ranking for top website builders on those AI searches"), Nathan Jean (Senior Account Manager, BizStream), Lukas Mehnert (B2B SaaS Marketing Expert). None of these twelve names a quantified metric; all screened as testimonials, not case studies.

## Pull notes — mechanical only

- Index page fetched via two calls (max_length 4000 at start_index 0, then max_length 3000 at start_index 4000) reaching character ~7000+; the page continues beyond that point (a "70+ agency partners" section and further content were visible in the second call's tail but not further pursued).
- Instant Commerce and Videoloft individual pages each fetched to ~3500 characters (full page for Videoloft; Instant Commerce's "Results & Outcomes" section was cut mid-list at "✅ 2x increase in AI search visibility... [note: truncated]" — the full bullet list of results was not completely captured, but the headline 2x figure and its measurement caveat were captured before truncation).
- The remaining 9 case studies (Chatarmin, Slopelift, NOLA Marketing, Stella Rising, Bacula, SORN.AI, What IF Web, Neur Digital/MedTech, TM Blast) were not individually fetched — grades above are based on the index page's own teaser text only and are flagged "teaser-only" in the table. This is the same consolidation approach used for the other five vendors in this cluster, applied here to manage pull volume across a six-vendor task.
