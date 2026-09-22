# Sitefire

| | |
|---|---|
| Profile date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every raw file cited below; oldest data window carried 2026-02-23 (start of the Pointhound case window), `raw/e-case-sitefire-pointhound-2026-09-22.md` |
| Lane / sub-market | A, proof claims E / organic recommendation |
| Roster | position 13, `raw/a-vendor-roster-2026-09-22.md` — 3 sources: Y Combinator company page (W26), Product Hunt, founderland.ai; plus Hacker News Launch HN thread 2026-03-20 (36 points, 27 comments) |
| Status | operating — "Active" on the YC company page; pricing, docs and case pages live, checked sitefire.ai 2026-09-22 |

## Sells what, to whom
| Product | What it does | Buyer named by the vendor | Source | Raw |
|---|---|---|---|---|
| Sitefire — AI Search Analytics, Source Analytics, Spark assistant, Agents that write and publish to the CMS, Agent Analytics | finds which content earns citations, writes brand-aware articles, pushes drafts to the CMS | "marketing/growth teams at Series A+ companies that need a GEO tool to actually take action"; "small brands"; "growing brands" | vendor-reported | `raw/a-sitefire-method-2026-09-22.md`, `raw/a-sitefire-pricing-2026-09-22.md`, `raw/a-sitefire-funding-2026-09-22.md` |

## Model and pricing
| Model | Tier or SKU | Disclosed price | Unit | Contract shape | Source | Raw |
|---|---|---|---|---|---|---|
| subscription | Lite | $249/month, billed monthly | 150 prompts, 8 action briefs, 3 articles/month, 3 of 5 engines | self-serve, 7-day trial | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |
| subscription | Pro ("Most Popular") | $499/month, billed monthly | 300 prompts, 30 sentiment-tracked, 18 briefs, 8 articles, 3 of 5 engines | self-serve, 7-day trial | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |
| subscription | Enterprise | not disclosed — checked sitefire.ai/pricing 2026-09-22 ("Custom", "Talk to us") | unlimited prompts, all 5 engines + Custom | sales-led, "done for you" | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |

## Scale
| Measure | Figure | Layer | As of | Source | Raw |
|---|---|---|---|---|---|
| Revenue or ARR | unknown — checked sitefire.ai (all pages), ycombinator.com/companies/sitefire 2026-09-22 | n/a | n/a | — | `raw/a-vendor-census-c1-2026-09-22.md` |
| Headcount | "Team Size: 2" (YC field, matching the two named founders); one open role, "Founding Product Engineer", Munich, €85–120k, 0.60–2.00% equity | total | 2026-09 pull | vendor-reported, tier 3 | `raw/a-sitefire-funding-2026-09-22.md` |
| Customers | no aggregate count found anywhere on sitefire.ai; named: BMW, Xtrackers, DWS (YC launch post), Jerry.ai, Wemolo, Chamber (testimonials), Pointhound (case study) | logos only | 2026-09 pull, undated | vendor-reported, tier 3/6 | `raw/a-sitefire-customers-2026-09-22.md`, `raw/a-sitefire-funding-2026-09-22.md` |
| Funding | not disclosed — checked ycombinator.com/companies/sitefire, sitefire.ai 2026-09-22; YC Winter 2026 backing confirmed, no dollar amount and no post-YC round found | n/a | batch W26 | vendor-reported, tier 3 | `raw/a-sitefire-funding-2026-09-22.md` |

## Trajectory — a number and a direction
| Measure | From | To | Window | Direction | Source | Raw |
|---|---|---|---|---|---|---|
| any revenue, headcount, customer or funding series | unknown — founded 2025, YC W26; no two-point series on any channel checked | — | — | — | — | `raw/a-sitefire-funding-2026-09-22.md` |
| Pointhound's AI-bot traffic share of new content (the vendor's own strongest series) | 0% | "45% of all AI bot traffic is the new content" | 2026-02-23 to 2026-06-29; first content live 2026-03-14 | up | vendor-reported, customer's GA4 and CDN logs | `raw/e-case-sitefire-pointhound-2026-09-22.md` |

## Per-engine coverage
| Engine | Covered | Surface | Metric offered | Method disclosed | Source | Raw |
|---|---|---|---|---|---|---|
| ChatGPT — OpenAI (P1) | yes, all tiers (one of "3 out of 5" on Lite and Pro) | consumer chat implied; crawler user-agents tracked server-side via Agent Analytics | mention, "Visibility Score", "Citation Share", sentiment, AI referral and AI bot traffic | partial — onboarding generates prompts from Google search volumes; no prompt set or n published | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md`, `raw/a-sitefire-method-2026-09-22.md` |
| Claude — Anthropic (P1) | named on the homepage and docs; absent from the pricing table's five — conflict, not reconciled | as above | as above | partial | vendor-reported | `raw/a-sitefire-method-2026-09-22.md`, `raw/a-sitefire-pricing-2026-09-22.md` |
| Google — AI Overviews, AI Mode, Gemini (P1) | yes, all three named on the pricing table | as above | as above | partial | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |
| Microsoft Copilot (P2) | no — not named on any page pulled | n/a | n/a | n/a | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |
| Amazon Rufus / Alexa for Shopping (P2) | no — not named | n/a | n/a | n/a | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |
| Grok (P2) | no — not named | n/a | n/a | n/a | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |
| Perplexity (P3) | yes, all tiers | as above | as above | partial | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |

## Proof claims — graded against the evidence bar
| Claim, as published | Metric | Grade | Bar items missing | Raw |
|---|---|---|---|---|
| Pointhound — "+300% more site visits from AI Search... Visibility Score 0 → 1.0%... Citation Share 0 → 1.0%"; "Weekly charts run February 23 to June 29, 2026. The first content went live March 14"; control stated as "new content vs. rest of site" | traffic, visibility | **Silver** — raised from Bronze at P4-c4 on the full page; the cluster's only Silver | 6 absolute n (relative multiples only); 7 paid-by-outcome | `raw/e-case-sitefire-pointhound-2026-09-22.md`, `raw/e-case-census-c4-2026-09-22.md` |
| Jerry — "+78% AI referral traffic... 112% vs. 72% treated-vs-untouched" | traffic, visibility | **Silver** at P4-c13 (raised from the Bronze homepage teaser); **Bronze** at P4-c10 on the same page, missing 2 and 6, item 7 partial — both grades stand, not reconciled | P4-c13: 6, 7. P4-c10: 2 engine, 6 n | `raw/e-case-c13-sitefire-jerry-2026-09-22.md`, `raw/e-case-c10-sitefire-jerry-2026-09-22.md` |
| BMW, Xtrackers, DWS, Wemolo, Chamber — named customers and testimonials | none quantified | screened — no claim; no metric attached to any | 2, 3, 4, 6, 7 | `raw/a-sitefire-customers-2026-09-22.md`, `raw/a-sitefire-funding-2026-09-22.md` |

Paid-by-outcome unknown on both cases; prompt set: partial for Pointhound (a fixed tracked question set at onboarding, n undisclosed), unknown for Jerry. Brand-side (P4-c7): Pointhound `silent — checked` at pointhound.com; Jerry.ai `silent — checked` at jerry.ai; BMW, Xtrackers, DWS, Wemolo, Chamber not checked (cap) — `raw/e-case-census-c7-2026-09-22.md`.

## Positioning
| Against | How it positions itself | Vendor's own words | Raw |
|---|---|---|---|
| "other GEO tools" | sells action taken, not measurement reported | "Unlike other GEO tools, sitefire actually tells you how to improve your AI visibility. It recommends actions, and takes them for you" | `raw/a-sitefire-funding-2026-09-22.md` |
| Score-based rivals | grounds its proof in server logs rather than a modelled score | "Every number below comes from the customer's own server logs and analytics - not synthetic scores" | `raw/a-sitefire-customers-2026-09-22.md` |

## Negatives
| Negative | Evidence | Source | Raw |
|---|---|---|---|
| Two people; no funding amount, revenue or customer count | YC "Team Size: 2"; careers page 404s despite a footer link; YC backing carries no figure; no post-YC round and no aggregate customer number found | vendor-reported; absence found by checking | `raw/a-sitefire-funding-2026-09-22.md`, `raw/a-sitefire-pricing-2026-09-22.md` |
| The Jerry case carries two conflicting grades | Silver at P4-c13, Bronze at P4-c10, same page, same session; both stand per `raw/e-case-census-c13-2026-09-22.md` | vendor-reported | `raw/e-case-c10-sitefire-jerry-2026-09-22.md`, `raw/e-case-c13-sitefire-jerry-2026-09-22.md` |
| Both Silvers are within-site observational comparisons | treated content vs the rest of the same site — not a holdout, geo-split or switchback, so neither reaches Gold | vendor-reported | `raw/e-case-census-c4-2026-09-22.md` |
| Claude named in docs but absent from the pricing table's engine list | homepage and docs name it; the "3 out of 5" table does not | vendor-reported | `raw/a-sitefire-pricing-2026-09-22.md` |

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Funding amount; any revenue figure; aggregate customer count; total prompt n behind the Pointhound case | ycombinator.com/companies/sitefire, sitefire.ai all pages, sitefire.ai/careers (404), the case's own page | 2026-09-22 |

## Caveats
- Every figure here is vendor-reported, including both Silver cases; they rest on the customers' own GA4, CDN and server logs as retold by Sitefire, with no named independent auditor and no third-party replication.
- Conflicting grades stand side by side, unreconciled: Jerry is Silver at P4-c13 and Bronze at P4-c10. The Claude engine-coverage conflict is likewise unreconciled.
- Layer mismatch: BMW, Xtrackers and DWS come from the founders' own YC launch post with no metric and no contract detail; they are logos, not disclosed customers.
- Category turnover is fast; this profile is stale one quarter after 2026-09-22.
