# Ahrefs (Brand Radar)
| | |
|---|---|
| Profile date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — `raw/a-vendor-roster-2026-09-22.md` (every cited pull carries the same date) |
| Lane | A, E |
| Sub-market | organic recommendation — incumbent bundling |
| Roster position | 15 — `raw/a-vendor-roster-2026-09-22.md` row 15 |
| Roster sources | (a) 2 — Businesswire 2026-01-20, "Ahrefs Launches Custom AI Prompt Tracking for Brand Visibility" (Yahoo Finance carries the same release, counted once); G2 AEO category p2 (4.5/5, 714 reviews) |
| Feature name, launch | "Brand Radar", two tracks: "Custom Prompts" (per-customer) and "AI Visibility Index" (shared prompt database). Launch **2026-01-20 carried from the roster's Businesswire citation and not re-verified** — this pass's re-pull failed on a connection error (two attempts), and `ahrefs.com/blog/introducing-brand-radar` 404s — `raw/a-ahrefs-launch-2026-09-22.md` |
| Status | operating (private; HQ country not stated in any source pulled) — `raw/a-vendor-census-c3-2026-09-22.md` row 5 |

## Sells what, to whom
| Product | What it does | Buyer named by the vendor | Source | Raw |
|---|---|---|---|---|
| Brand Radar | Four defined metrics: "Mentions", "Citations", "AI Share of Voice", "Estimated Impressions"; plus AI Analytics (AI traffic, bot visits) and AI Sources (YouTube, TikTok, Reddit) | "teams"; "marketers"; existing Ahrefs paid-plan customers | vendor-reported | `raw/a-ahrefs-brand-radar-product-2026-09-22.md`, `raw/a-ahrefs-method-2026-09-22.md` |

## Model and pricing — JPY as the page rendered it (geolocated pull); USD figures from `/brand-radar` kept beside them, unreconciled
| Model | Tier or SKU | Disclosed price | Unit | Contract shape | Source | Raw |
|---|---|---|---|---|---|---|
| subscription | Lite — **base plan, and it already includes Brand Radar plus "5 tracked AI prompts"** | ¥19,900/mo | per month, 1 user | self-serve | vendor-reported | `raw/a-ahrefs-pricing-2026-09-22.md` |
| subscription | Standard → 10 prompts; Advanced → 20 prompts; Enterprise → "From 83" prompts | ¥38,400/mo; ¥68,900/mo; ¥230,900/mo (annual commitment) | per month | self-serve; Enterprise sales-led | vendor-reported | `raw/a-ahrefs-pricing-2026-09-22.md` |
| subscription, standalone | "Brand Radar AI" / "AI Visibility Index" — same SKU, two prices the same session | "from ¥30,600/mo" on `/pricing`; "$199/mo" on `/brand-radar` (83 prompts/day, +2,500 checks/mo, overage $0.020/check) | per month | self-serve | vendor-reported | `raw/a-ahrefs-pricing-2026-09-22.md`, `raw/a-ahrefs-brand-radar-product-2026-09-22.md` |
| usage | Custom prompt packages — Basic / Growth / Scale | ¥7,700/mo (+2,500 checks); ¥15,420/mo (+7,000); ¥38,500/mo (+25,000). On `/brand-radar`: "Starts at $50/mo, $699/MO FOR ALL MODELS" | per month, per check overage | self-serve | vendor-reported | `raw/a-ahrefs-pricing-2026-09-22.md` |
| — | Price delta | **There is no feature-free base plan.** Delta is a quota ladder: Lite ¥19,900 → Standard ¥38,400 (**+¥18,500**, +5 prompts) → Advanced ¥68,900 (**+¥30,500**, +10 prompts) → Enterprise ¥230,900 (**+¥162,000**) | per month | — | vendor-reported | `raw/a-ahrefs-pricing-2026-09-22.md`; `markets/organic-recommendation.md` §Structural checks |

## Scale
| Measure | Figure | Layer | As of | Source | Raw |
|---|---|---|---|---|---|
| Revenue or ARR | `unknown — checked ahrefs.com/pricing, /brand-radar, roster sources 2026-09-22` (private, not a filer) | — | 2026-09 | — | `raw/a-vendor-census-c3-2026-09-22.md` row 5 |
| Headcount | `unknown — checked ahrefs.com, roster sources 2026-09-22` | — | 2026-09 | — | `raw/a-vendor-roster-2026-09-22.md` row 15 |
| Customers | "Used by 3,000+ companies" — stated on `/brand-radar`, not confirmed Brand-Radar-specific | logos, product-wide | 2026-09 | vendor-reported | `raw/a-ahrefs-brand-radar-product-2026-09-22.md` |
| Funding | `unknown — checked ahrefs.com, businesswire.com (connection failure ×2), roster sources 2026-09-22` | — | 2026-09 | — | `raw/a-ahrefs-launch-2026-09-22.md` |

## Trajectory — a number and a direction
| Measure | From | To | Window | Direction | Source | Raw |
|---|---|---|---|---|---|---|
| Company revenue, headcount, customers or funding | `unknown — checked ahrefs.com, businesswire.com (connection failure ×2), roster sources 2026-09-22` — no dated pair of figures exists in any pulled source | — | — | unknown | — | `raw/a-ahrefs-launch-2026-09-22.md` |

## Per-engine coverage
Index size: "454M+ Total monthly prompts" on `/brand-radar` — AI Overviews 312.8M, Gemini 31.3M, Perplexity 31.2M, ChatGPT 31.2M, Copilot 30.8M, AI Mode 16.9M — against "475M+ organic prompts" on `/pricing`; both recorded, unreconciled.

| Engine | Covered | Surface | Metric offered | Method disclosed | Source | Raw |
|---|---|---|---|---|---|---|
| ChatGPT — P1 | yes — prompt-based index, 31.2M | consumer chat | mention, citation, share of voice, estimated impressions | yes — n, generation method ("real queries... expanded... via People Also Ask and semantic fanout"), cadence ("re-tested monthly on a 90-day reporting window"), history "back to 2025"; prompt wordings not published | vendor-reported | `raw/a-ahrefs-method-2026-09-22.md` |
| Claude — P1 | yes — Custom Prompts only, "Claude consumes 8 checks per update"; not in the prompt-based index breakdown | consumer chat | as above | as above | vendor-reported | `raw/a-ahrefs-brand-radar-product-2026-09-22.md`, `raw/a-ahrefs-method-2026-09-22.md` |
| Google AI Overviews, AI Mode, Gemini — P1 | yes, all three — AI Overviews and AI Mode also via a search-query-based index | search-integrated and consumer chat | as above | as above | vendor-reported | `raw/a-ahrefs-method-2026-09-22.md` |
| Microsoft Copilot — P2 | yes — 30.8M | consumer chat | as above | as above | vendor-reported | `raw/a-ahrefs-brand-radar-product-2026-09-22.md` |
| Amazon Rufus / Alexa for Shopping, Grok — P2 | `unknown — checked ahrefs.com/brand-radar, ahrefs.com/pricing 2026-09-22` | — | — | — | vendor-reported | `raw/a-ahrefs-brand-radar-product-2026-09-22.md` |
| Perplexity — P3 | yes — 31.2M | consumer chat | as above | as above | vendor-reported | `raw/a-ahrefs-method-2026-09-22.md` |

## Proof claims — graded against the evidence bar
No claim clears the bar — 1 claim screened, 0 cleared, as of 2026-09-22. The only Brand Radar customer reference is a workflow-efficiency testimonial with no number: "With Brand Radar, it's now just a few clicks to identify what I need, and export everything directly" — Laura Lancu, SEO Growth Specialist, Octopus Energy. Its "Read Case Study" link could not be reached (`ahrefs.com/case-studies` and `/case-studies/octopus-energy` both 404) — `raw/a-ahrefs-customers-2026-09-22.md`.

## Positioning
| Against | How it positions itself | Vendor's own words | Raw |
|---|---|---|---|
| Setup-heavy prompt-tracking tools | An instant shared index for established brands, custom prompts for the rest | "See any brand's AI visibility instantly across 454M prompts. No setup." / "Make AI recommend your brand" | `raw/a-ahrefs-brand-radar-product-2026-09-22.md` |

## Negatives
| Negative | Evidence | Source | Raw |
|---|---|---|---|
| The same standalone SKU carries two prices and two index sizes across two of its own pages, same session | "$199/mo" and "454M+" on `/brand-radar` vs "from ¥30,600/mo" and "475M+" on `/pricing` | vendor-reported | `raw/a-ahrefs-pricing-2026-09-22.md`, `raw/a-ahrefs-brand-radar-product-2026-09-22.md` |
| Zero gradable customer cases; the one case study linked from the product page is unreachable | 1 testimonial, no quantified metric; two 404s | vendor-reported | `raw/a-ahrefs-customers-2026-09-22.md` |
| The launch date rests on a citation this pass could not re-open | businesswire.com connection failure ×2; `/blog/introducing-brand-radar` 404; the product page is undated | company-stated, unverified this pass | `raw/a-ahrefs-launch-2026-09-22.md` |
| The AI Visibility Index has stated coverage limits for the brands most likely to need it | "may have limited coverage for brands with little or no search volume" | vendor-reported | `raw/a-ahrefs-method-2026-09-22.md` |

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Launch-post text; the $199 vs ¥30,600 and 454M vs 475M discrepancies; the Octopus Energy case study; per-tier platform count and update frequency; revenue, headcount, funding, HQ country | businesswire.com (×2), ahrefs.com/blog/introducing-brand-radar, /brand-radar, /pricing, /case-studies, /case-studies/octopus-energy | 2026-09-22 |

## Caveats
- Every figure is vendor-reported on Ahrefs's own pages; none is independently audited, and the disclosed 454M-prompt method is Ahrefs's own account of its own pipeline.
- Conflicting figures kept side by side, unreconciled: $199/mo vs ¥30,600/mo; 454M+ vs 475M+; JPY on `/pricing` vs USD on `/brand-radar` in the same session (exit IP geolocated to Japan).
- Layer mismatch: "3,000+ companies" is a product-wide figure that may not be Brand Radar users, and no revenue of any layer exists to size the feature.
- Category turnover is fast; this profile is stale one quarter after 2026-09-22.

## Primary re-pulls, REPULL-1, 2026-09-23

- Ahrefs Brand Radar custom-prompt launch date 2026-01-20 · `raw/a-ahrefs-launch-2026-09-22.md` (n/a — connection failure) · `raw/a-businesswire-ahrefs-brand-radar-custom-prompts-primary-2026-09-23.md` (3) · "Jan 21, 2026 12:16 AM Eastern Standard Time"; "today announced custom AI prompt tracking in Brand Radar"; "over $100 million in annual recurring revenue"; "bootstrapped, profitable"; "available now in Brand Radar for paid Ahrefs customers" · differs by one day (display 2026-01-21 00:16 EST; release ID 20260120714417) — both recorded; primary adds the $100M+ ARR company-stated figure
