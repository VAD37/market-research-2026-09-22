# Agentic commerce
| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every raw file cited. Oldest source publication carried: 2024-11-18, `raw/c-perplexity-shop-merchant-2026-09-22.md` |
| Lane | C |
| Engines covered | P1 ChatGPT, Claude, Google; P2 Copilot, Amazon, Grok; P3 Perplexity (reweight 1, `../method/plan.md`) |
| Geography | US primary. Canada and Australia named on one Google page. EU present by regulation only |

## Definition and boundary
| | |
|---|---|
| Definition | Checkout executed by the agent, per `../method/glossary.md` |
| Aliases in sources | agentic commerce, agentic checkout, transaction rails, Instant Checkout, Copilot Checkout, Buy with Pro |
| In | Agent-executed checkout; protocols ACP, AP2, UCP, x402, Visa TAP, Mastercard Agent Pay; per-engine merchant feed and checkout programs; sell-side feed and platform tooling |
| Out | Consumer AI shopping apps, per `../method/scope.md`. Ads inside AI answers → `paid-placement.md`. Unpaid appearance → `organic-recommendation.md` |
| Metric denominated in | Sales — orders, GMV, take rate. Traffic rows below stay labelled traffic and are never summed into a size |

## Sizing — bottom-up
| Input | Figure | As of | Label | Raw |
|---|---|---|---|---|
| Sell-side vendors rostered, lane C | 3 of 7 — Feedonomics, Shopware, Wix | 2026-09 | vendor-reported | `raw/c-vendor-census-c6-2026-09-22.md` |
| Disclosed price and customer count, per vendor | Shopware only on price: Community free; Rise €600/mo; Evolve €2,400/mo; Intelligence+ €19–29/mo. Counts: Shopware "More than 55,000 businesses"; Wix "300M+ Sites"; Feedonomics named logos, no aggregate | 2026-09 | vendor-reported | same |
| Engines with a live checkout program | 4 stated live: ChatGPT, Google, Copilot, Perplexity. Claude, Amazon, Grok: none found | 2026-09 | company-stated | per-engine table below |
| Fee or commission disclosed, per program | 1 of 4 — Copilot Checkout "does not take a commission or affiliate fee". Other 3 `unknown — checked` | 2026-09 | company-stated | `raw/b-microsoft-agentic-commerce-2026-09-22.md` |
| Merchants named in any program, count | No engine states a count. Named only: Urban Outfitters, Anthropologie, Ashley Furniture, Etsy sellers | 2026-01 | company-stated | `raw/c-microsoft-copilot-checkout-brand-agents-2026-09-22.md` |

**Build.** No multiplication is possible: the one disclosed price (Shopware) and the one disclosed count (55,000 businesses) describe that vendor's whole platform, not its agentic feature, and no engine discloses a take rate or a merchant count to multiply against.

| Result | Figure | Method | Coverage | Confidence limit |
|---|---|---|---|---|
| Bottom-up size | `unknown — cannot be built from disclosed inputs, checked c-vendor-census-c6, protocols table, engine pages 2026-09-22` | bottom-up, disclosed inputs | price 1 of 3 vendors; fee 1 of 4 engines; counts platform-wide, not agentic-attributable | Sees no transaction volume: every checkout settles on the merchant's own rails |

### Measured present state — one publisher's own platform base each, never summed into a size. All three rows: `raw/c-retail-analytics-table-2026-09-22.md`; no publisher breaks any figure out per engine — `unknown — checked Adobe, Salesforce, Shopify 2026-09-22`
| Publisher, population | Figures, verbatim | Base period | Measured / modelled | Tier |
|---|---|---|---|---|
| Adobe Analytics customers, ">1 trillion visits to U.S. retail sites" | "AI Conversion Now 42% Higher" / "Is Now 54% Higher"; "AI Visits Worth 37% More Than Non-AI Visits" / "53% More" | Mar 2026 / May 2026 | measured | 4 |
| Salesforce Commerce Cloud/Agentforce, "1.5 billion global shoppers" | "driving 20% of all retail sales and fueling $262 billion in revenue"; "Over 19% of orders were influenced by AI and agents" | Nov 1–Dec 31, 2025; Oct 1–Nov 15, 2025 | modelled — attributed, not incremental | 5 |
| Shopify storefronts, no merchant or session count disclosed | "convert at nearly 50% higher rates than organic search"; "converted about 80% better"; "14% higher average order values" | Q1 2026; Q2 2026; Q1 2026 | measured | 5 |

**Proxy.** No e-commerce GMV or retail-e-commerce-share proxy exists in the proxies table — `unknown — checked e-market-size-table-2026-09-22.md Table 2 2026-09-22` (both rows organic-side, one gated). Nearest adjacent figures, kept separate and not adopted: EMARKETER "8.8% of total retail ecommerce sales", 2026, relayed tier 6, `raw/e-market-size-stellagent-agentic-2026-09-22.md`; Shopify "over $100 billion of GMV in the first quarter alone", Q1 2026, not AI-attributed, tier 3, `raw/c-shopify-analytics-q1-2026-gmv-2026-09-22.md`.

## Forecasts — side by side, never as the size
| Author | Forecast figure | Target year | Base and scope | Label, verbatim | Tier | Raw |
|---|---|---|---|---|---|---|
| EMARKETER (relayed via Stellagent) | "over $20 billion in 2026, reaching $144 billion by 2029" | 2029 | 2026 base; US, "via AI platforms only" | "forecast"/"projects" | 6 relayed | `raw/e-market-size-stellagent-agentic-2026-09-22.md` |
| Morgan Stanley Research | "$190 billion to $385 billion in U.S. e-commerce spending by 2030... 10% to 20%" | 2030 | no base-year dollar anchor; US | "estimates" | 5 | `raw/e-market-size-morganstanley-agentic-2026-09-22.md` |
| Bain & Company | "$300 to $500 billion by 2030... roughly 15% to 25% of overall e-commerce" | 2030 | no base; US; excludes AI-assisted search or discovery | "estimates" | 6 | `raw/e-market-size-bain-agentic-2026-09-22.md` |
| McKinsey (via Digital Commerce 360 pointer) | "as much as $1 trillion in orchestrated U.S. retail revenue... $3 trillion to $5 trillion globally" | 2030 | no base; two scopes in one sentence | "estimates" per pointer | 5 | `raw/e-market-size-mckinsey-agentic-2026-09-22.md` |
| Edgar Dunn (relayed via Stellagent) | "$1.7T (narrow) / $2.9T (broad)" | 2030 | no base; global retail transaction flows | "forecast" per relay | 6 relayed, uncorroborated | `raw/e-market-size-stellagent-agentic-2026-09-22.md` |
| Gartner, Inc. | "By 2028, 90% of B2B buying will be AI agent intermediated, pushing over $15 trillion of B2B spend" | 2028 | no base; global B2B | "prediction" | 6 | `raw/e-market-size-gartner-agentic-2026-09-22.md` |
| Grand View Research | "valued at USD 5.7 billion in 2025 and is projected to grow... to USD 65.5 billion by 2033, at a CAGR of 35.7%" | 2033 | 2025 base; global | "valued at" / "projected" | 6 | `raw/e-market-size-grandviewresearch-agentic-2026-09-22.md` |

**Divergence, as the sources show it.** Across the 2029–2030-horizon rows the spread runs USD 144B (EMARKETER, US, 2029) to USD 5T (McKinsey, global, 2030) — roughly 35×. Over the whole set, `e-market-size-table-2026-09-22.md` states the range as "roughly $5.7B, 2025, Grand View Research's narrowest reading, to $15T, 2028, Gartner's global-B2B reading," and that "every agentic-commerce figure... uses a different, non-comparable scope definition." Seven of seven carry a forecast-family label from their own author; none is a closed-window measurement (H16 input). Nothing averaged.

## Growth
| Measure | Figures, verbatim | Base period | Label | Raw |
|---|---|---|---|---|
| AI-driven traffic to US retail sites, Adobe | "Up 393% YoY in Quarter One"; "Up 138% YoY in May 2026"; holiday "increased by 693.4% compared to the year prior"; December stated as "673%" in the Jan 2026 blog **and** "1,151% in December" in the Q2 2026 PDF — one publisher, conflict kept side by side, not averaged | Q1 2026; May 2026; Nov–Dec 2025; Dec 2025 — each vs the year prior | measured, tier 4 | `raw/c-retail-analytics-table-2026-09-22.md` |
| Traffic referred from AI chats, Salesforce | "grew between 150% and 428% year over year in every quarter measured"; "increased 3.8x globally YOY... and 1.8x in the U.S." | Q1 2024–Q1 2026, quarterly; 7 weeks to Nov 20, 2025 | measured, tier 5 | same |
| AI-referred orders and sessions, Shopify | orders "grew nearly 13x year-over-year", sessions "more than 8x"; next quarter sessions "grew 197%", orders "also grew 3x", against organic search sessions that "grew 12% on a much larger base" | Q1 2026; Q2 2026 — each vs the year prior | measured, tier 5 | same |

## Value chain — and where margin sits
| Stage | Who does it | What is charged | Margin evidence | Label | Raw |
|---|---|---|---|---|---|
| Engine surface | ChatGPT, Google AI Mode/Gemini, Copilot, Perplexity | Copilot 0%; the other three undisclosed | One fee statement across four live programs | company-stated | `raw/b-microsoft-agentic-commerce-2026-09-22.md` |
| Protocol | ACP, UCP, AP2, x402, Visa TAP, Mastercard Agent Pay | No protocol states a fee clause | 6 of 6 fee clauses `unknown — checked` 2026-09-22 | company-stated | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| Payment rail | Stripe, PayPal/Braintree, Visa, Mastercard, Google Pay (FPANs), Coinbase CDP facilitator | Standard processing; no agentic-specific rate stated | `unknown — checked docs.stripe.com, developer.paypal.com 2026-09-22` | company-stated | `raw/c-stripe-protocol-agentic-commerce-2026-09-22.md`; `raw/c-paypal-protocol-agentic-commerce-2026-09-22.md` |
| Commerce platform | Shopify (UCP, plus ACP-side Agentic Storefronts), Wix, Shopware | Merchant's existing platform subscription | Shopware only public rate card: €600–€2,400/mo | vendor-reported | `raw/c-vendor-census-c6-2026-09-22.md`; `raw/c-shopify-protocol-agentic-commerce-2026-09-22.md` |
| Feed / checkout tooling | Feedonomics, PayPal Store Sync, Microsoft Merchant Center, Google Merchant Center | Feedonomics custom-quoted, "we never take a percentage of revenue" | No dollar figure disclosed | vendor-reported | `raw/c-vendor-census-c6-2026-09-22.md` |
| Merchant | Retailer, stays "merchant of record" / "seller of record" | Keeps the transaction, customer data, relationship | Stated by Google and Microsoft in their own words | company-stated | `raw/c-google-merchant-ucp-checkout-2026-09-22.md`; `raw/c-microsoft-copilot-checkout-brand-agents-2026-09-22.md` |

### Who controls each protocol. Rows 1–4: `raw/c-agentic-commerce-protocols-table-2026-09-22.md`; row 5 `raw/c-visa-protocol-trusted-agent-2026-09-22.md`; row 6 `raw/c-mastercard-protocol-agent-pay-2026-09-22.md`. MCP is Anthropic-originated transport, not a commerce protocol, and carries no commerce spec to gate — `raw/c-anthropic-mcp-connector-2026-09-22.md`
| Protocol | Owner | Licence | Governance body | Gate |
|---|---|---|---|---|
| ACP | "maintained by OpenAI and Stripe"; Meta holds a TSC seat | Apache-2.0 | TSC, up to 7 seats; SEP-only veto held by OpenAI and Stripe | None to read; CLA to contribute |
| AP2 | Google-founded; "donated to FIDO" 2026-04-28 | Apache-2.0 | FIDO Alliance since 2026-04-28; repo keeps samples and SDK only | None to read; needs a commerce protocol alongside |
| UCP | Google-founded, no single owner | Apache-2.0 | Five councils — Shopping, Food, Lodging, Payments, Governance | Spec open; merchant checkout "select merchants", early access |
| x402 | x402 Foundation (formerly Coinbase) | Apache-2.0 | "Merging contributions is at the discretion of the x402 Foundation team" | None on the spec; a facilitator needs its own account |
| Visa Trusted Agent Protocol | Visa, sole | Proprietary click-through "Product Terms" | None named | Agent-side Implementation Guide "for onboarded agents" only |
| Mastercard Agent Pay | Mastercard, sole | Not found | Mastercard "enables and governs" the program | "All integrators must be registered with Mastercard"; no public schema |

## Per-engine cells — priority-1 and priority-2 engines × agentic commerce
| Engine | Checkout program live, as stated | Protocol used | Fee | Countries | Merchant gate | Raw |
|---|---|---|---|---|---|---|
| ChatGPT — OpenAI (P1) | "ChatGPT may also show an Instant Checkout option that lets you complete checkout in ChatGPT" | ACP | `unknown — checked developers.openai.com, help.openai.com, docs.stripe.com 2026-09-22` | `unknown — checked help.openai.com/en/articles/11128490 2026-09-22` | "Onboarding product feeds in ChatGPT is currently available to approved partners" | `raw/c-openai-shopping-chatgpt-search-2026-09-22.md`; `raw/c-openai-commerce-get-started-2026-09-22.md` |
| Claude — Anthropic (P1) | None found. Generic MCP connector only; "Project Deal" was a 69-employee internal pilot | MCP transport; no commerce spec | n/a — no program | n/a | `unknown — checked anthropic.com, docs.claude.com, platform.claude.com 2026-09-22` | `raw/c-anthropic-mcp-connector-2026-09-22.md`; `raw/c-anthropic-project-deal-2026-09-22.md` |
| Google — AI Mode, Gemini (P1) | "the checkout happens directly on Google's surfaces while keeping you the merchant of record" | UCP (compatible with AP2, A2A, MCP) | `unknown — checked developers.google.com/merchant/ucp, support.google.com/merchants 2026-09-22` | **Conflicting:** "United States, Canada, and Australia" vs "eligible U.S. retailers" — both kept | "available for select merchants at this time"; "early access program"; `native_commerce(checkout_eligibility)` required | `raw/c-google-merchant-ucp-checkout-2026-09-22.md`; `raw/c-google-ucp-merchant-agentic-2026-09-22.md` |
| Microsoft Copilot (P2) | "beginning to roll out in the U.S. on Copilot.com, with partner activation across PayPal, Shopify, and Stripe" | ACP adopted; "MMC will support Universal Commerce Protocol (UCP)" | **0%** — "No. Today, Microsoft does not take a commission or affiliate fee" | "Only English-language merchants who sell to US buyers are eligible at this time (supporting USD)" | "Pilot only to select customers"; Shopify merchants auto-enrolled after an opt-out window | `raw/c-microsoft-copilot-checkout-brand-agents-2026-09-22.md`; `raw/b-microsoft-agentic-commerce-2026-09-22.md`; `raw/c-microsoft-protocol-ucp-adoption-2026-09-22.md` |
| Amazon — Alexa for Shopping / Rufus (P2) | Consumer-side only: "the Buy for Me agentic AI feature handles the entire purchase on your behalf" | `unknown — checked a-amazon-alexa-for-shopping-* 2026-09-22` — no protocol named | `unknown — checked advertising.amazon.com pulls 2026-09-22` | "available to U.S. customers" | No merchant checkout program found — `unknown — checked a-amazon-alexa-for-shopping-customer-help-2026-09-22.md` | `raw/a-amazon-alexa-for-shopping-rename-2026-09-22.md` |
| Grok — xAI (P2) | None found | n/a | n/a | n/a | `unknown — checked c-agentic-commerce-protocols-table, c-vendor-census-c6 2026-09-22` | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| Perplexity (P3 per reweight 1) | "Buy with Pro, which lets you check out seamlessly right on our website or app for select products from select merchants" — 2024-11-18, stale | `unknown — checked perplexity.ai/hub 2026-09-22` | Merchant Program "free for merchants"; checkout take rate `unknown — checked perplexity.ai/hub/legal (404) 2026-09-22` | "For Perplexity Pro users in the U.S." | "large retailers" invited via signup form; Merchant Program terms page now 404s | `raw/c-perplexity-shop-merchant-2026-09-22.md` |

## Structural checks
| Check | Answer | As of | Label | Raw |
|---|---|---|---|---|
| Substitute — what the merchant does instead; is "do nothing" the real competitor | Existing own-site checkout: "users check out on the merchants' online store"; "With the existing checkout button, the transaction occurs on your site". Marketplaces: Amazon Store, Etsy. "Do nothing" is partly foreclosed — Shopify merchants are auto-enrolled into Copilot Checkout after an opt-out window | 2026-01 to 2026-09 | company-stated | `raw/c-openai-shopify-merchants-2026-09-22.md`; `raw/c-google-merchant-ucp-checkout-2026-09-22.md`; `raw/c-microsoft-copilot-checkout-brand-agents-2026-09-22.md` |
| Platform risk — engine-owned checkout vs open protocol | Both live engine checkouts run on the engine's own surface while the merchant stays merchant of record. Protocol control is moving off the engines: AP2 donated to FIDO 2026-04-28; UCP governed by five councils seating Google, Shopify, Etsy, Meta, Amazon, Target, Microsoft, Stripe; x402 moved to the x402 Foundation. Offsetting that: Visa TAP and Mastercard Agent Pay are single-owner, and Mastercard publishes no schema at all | 2026-09 | company-stated | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| Incumbent bundling — which incumbent added this, at what price delta, acquired by whom | Shopify implements UCP (Universal Cart API on an early-access waitlist; direct checkout completion needs a "higher trust tier") plus ACP-side Agentic Storefronts; Stripe co-maintains ACP and offers sellers "UCP or ACP"; PayPal publishes an ACP-to-Braintree guide plus gated Store Sync. Price delta: only Shopware publishes one (€600–€2,400/mo). Acquisition touching this sub-market in raw: Feedonomics sits inside Commerce (Nasdaq: CMRC, formerly BigCommerce); no agentic-commerce acquisition found — `unknown — checked c-vendor-census-c6, a-vendor-census-c1–c4 2026-09-22` | 2026-09 | company-stated, vendor-reported | `raw/c-shopify-protocol-agentic-commerce-2026-09-22.md`; `raw/c-stripe-protocol-agentic-commerce-2026-09-22.md`; `raw/c-vendor-census-c6-2026-09-22.md` |
| Regulatory — rules in force at the pull date, and designation status per engine | ChatGPT designated VLOSE 2026-08-31, 159.1M EU monthly recipients, no Art. 39 ad repository yet (four-month window to ~Jan 2027); Google Search VLOSE and Bing VLOSE 25.04.2023; Amazon Store VLOP 25.04.2023; Claude and Perplexity not designated, each self-stating it sits below the 45M threshold; Grok not separately designated. EU AI Act Art. 50 in force 2026-08-02; DSA Art. 26 ad-identification duty in force. No payment-specific rule for agent checkout appears in any pull — `unknown — checked b-regulators-ad-disclosure-table, b-eu-dsa-ad-repositories-table 2026-09-22`. No commerce-relevant docket found; every Amazon-side docket query was WAF-blocked — `unknown — checked courtlistener.com 2026-09-22` | 2026-08 to 2026-09 | filed | `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md`; `raw/b-regulators-ad-disclosure-table-2026-09-22.md`; `raw/b-court-dockets-table-2026-09-22.md` |

## Demand signals — the nine agentic cells across the three vertical censuses
| Cells | Read | Signal | Raw |
|---|---|---|---|
| Skincare × enterprise | attention | e.l.f. Beauty "AI Product Owner, Agentic Commerce", base pay $110,000–$140,000/yr, 116 applicants; tier 3, below the tier-5 spend floor — `raw/f-signal-census-sk-2026-09-22.md` | `raw/f-signal-census-sk-2026-09-22.md` |
| The other eight cells | none | Skincare SMB and mid-market: nothing on twelve signals. B2B SaaS ×3: LinkedIn queries 7/13/17 returned sell-side payments engineering only, zero buyer-side hits — `raw/f-signal-census-bs-2026-09-22.md`. High-CPA ×3: one conference session, "How to Win at Agentic E-Commerce", John Lewis Financial Services, recorded blank — unattributed, no size stated | `raw/f-signal-census-hr-2026-09-22.md` |

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Instant Checkout fee or take rate, and the fee clause for AP2, UCP, x402, Visa TAP, Mastercard Agent Pay | developers.openai.com, docs.stripe.com, github.com/agentic-commerce-protocol, and each protocol owner's own domain per the protocols table's nine recorded unknowns | 2026-09-22 |
| Merchant count enrolled in any engine checkout program; whether Anthropic runs a merchant or checkout program at all, and whether Rufus / Alexa for Shopping offers one | developers.openai.com, support.google.com/merchants, about.ads.microsoft.com, perplexity.ai/hub; anthropic.com, docs.claude.com, platform.claude.com; a-amazon-alexa-for-shopping-* and advertising.amazon.com pulls | 2026-09-22 |
| Perplexity Merchant Program terms, and Buy with Pro's current status | perplexity.ai/hub/legal/merchant-program-terms-of-service (404), perplexity.ai/hub | 2026-09-22 |
| Shopify's UCP trust-tier criteria; UCP's own GOVERNANCE.md; Google's conflicting UCP country list | shopify.dev/docs/agents/auth (404), Universal-Commerce-Protocol repo trees (file not found), support.google.com/merchants vs blog.google | 2026-09-22 |

## Caveats
- No bottom-up size exists. Every input the method needs — engine take rate, merchant count, agentic-attributable vendor revenue — is undisclosed except Copilot's stated 0% and Shopware's rate card. All seven published sizes are forecasts in their authors' own words, and no two share a scope: US vs global, B2C vs B2B, "completed on-platform" vs "total business opportunity". The 35× spread compares figures that are not comparable, which is the finding, not a range to narrow.
- The measured rows describe one publisher's own customer base each, never the open web; none is broken out per engine; Salesforce's "influenced" figures are modelled and attributed, never incremental. Adobe's two December 2025 traffic figures and Google's three country statements each conflict inside one publisher and are kept side by side.
- Copilot Checkout's fee reads 0% in `b-microsoft-agentic-commerce-2026-09-22.md` and `unknown` in the protocols table, whose pull could not render the same FAQ answer. Both recorded; the answered pull is cited above. Everything else about programs and protocols here is company-stated, tier 3, on the vendor's own domain. Nothing is independently audited or replicated. Protocol churn is fast — AP2 changed governance 2026-04-28, x402 changed owner, UCP's repo was pushed the day it was pulled.
- The Perplexity row rests on a 2024-11-18 post and Google's UCP announcement on 2026-01-11, both outside the one-quarter staleness window in `../method/plan.md`; neither was re-checked against a current page beyond finding Perplexity's terms page now 404s. The category is roughly two years old as of 2026-09; every figure here is a point reading, and the staleness rule applies to each pull cited.

### Pass 13 addition, 2026-09-23

Per `../method/plan.md` Pass 13. Compiled read: `../findings/market-potential.md`. Nothing above is edited.

| Read | Figure | As of | Label, tier | Raw |
|---|---|---|---|---|
| Assistant reach, Amazon | Rufus "250 million customers using it this year" → "300 million+ customers" in 2025; Alexa for Shopping "active users close to doubling" YoY | 2025-10-30 → 2026-02-05 → 2026-07-30 | company-stated, 3 | `raw/c-amazon-rufus-user-sales-statements-2026-09-23.md` |
| Assistant-influenced sales, adjacent | Rufus "nearly $12 billion in incremental annualized sales last year"; method unstated | 2025 | company-stated, 3 | same |
| Floor — agent-executed checkout GMV | `unknown — checked openai.com (403), shopify.com 2026-08-05 release, PayPal/Stripe, aboutamazon.com 2026-09-23` | 2026-09 | — | `raw/e-engine-user-count-checks-2026-09-23.md`; `raw/c-shopify-q2-2026-results-2026-09-23.md` |
| New forecasts, never sizes | Juniper "$1.5 trillion in 2030", global; NextMSC $1.90B (2025) → $54.22B (2035); Market Intelo $2.8B (2025) → $16.8B (2034); Mordor agentic-AI-in-retail software $60.43B (2026) → $218.37B (2031), adjacent | pub. 2026-04 to 2026-09 | analyst-derived, 6 | `raw/e-market-size-juniper-agentic-`, `-nextmsc-agentic-`, `-marketintelo-organic-agentic-`, `-mordor-agentic-2026-09-23.md` |
| Forecast spread, 2030 | Morgan Stanley US $190B to McKinsey global $5T, 26.3× over 7 forecasts; US-only 5.26×; global 3.33× | 2030 | analyst-derived, 5–6 | same, plus rows 12–14, 18 of `raw/e-market-size-table-2026-09-22.md` |

**Caveats — Pass 13 addition.** This append takes the file past its 120-line budget; overrun recorded here. Rufus figures count in-year customers and "incremental" sales on Amazon's own definition — not agent-executed checkout and not comparable to the forecasts. A BCG page credited with "$3 trillion to $5 trillion" by a search summary carries no such figure (`raw/e-bcg-commerce-everywhere-2026-09-23.md`).

## Primary re-pulls, REPULL-1, 2026-09-23

- Edgar Dunn agentic commerce $1.7T (narrow) / $2.9T (broad) 2030 · `raw/e-market-size-stellagent-agentic-2026-09-22.md` (6) · `raw/e-market-size-edgardunn-agentic-swot-primary-2026-09-23.md` (5) · "$2.9billion — Total value of retail sales conducted via AI agents by 2030" (as printed; "$2,916,789 mn", 29% of global e-commerce 2030; e-commerce $7.3 trillion 2026 → $10.1 trillion 2030); January 2026 · differs — $2.9T agrees, "$1.7T (narrow)" not in primary (grep for 1.7 / narrow / broad returns no sizing line)
- EMARKETER AI-platform ecommerce "over $20 billion in 2026, reaching $144 billion by 2029", 8.8% · `raw/e-market-size-stellagent-agentic-2026-09-22.md` (6) · `raw/e-market-size-emarketer-ai-commerce-2026-primary-2026-09-23.md` (4) · "AI platform-driven ecommerce sales will surpass $144 billion by 2029, which will be 8.8% of total retail ecommerce sales"; chart title "US Ecommerce Sales via AI Platforms Will Exceed $20 Billion in 2026 and Top $144 Billion by 2029" (EMARKETER, 2026-01-26; per-year values redacted) · agrees
- Copilot Checkout PSP rule · `raw/b-microsoft-agentic-commerce-2026-09-22.md` (3) · `raw/b-microsoft-agentic-commerce-faq-primary-2026-09-23.md` (3) · "By default, the PSP that completes onboarding first becomes the checkout partner. Merchants may request a change if needed."; "Today, Copilot Checkout supports a single PSP checkout partner per merchant."; "No. Today, Microsoft does not take a commission or affiliate fee." · agrees (completes the truncated answer; 0% fee confirmed on the same load)
- Grand View Research agentic commerce market size (noise-level forecast) · `raw/e-market-size-grandviewresearch-agentic-2026-09-22.md` (6 — search snippet) · `raw/e-market-size-grandviewresearch-agentic-primary-2026-09-23.md` (6) · "valued at USD 5.7 billion in 2025 and is projected to grow from USD 7.7 billion in 2026 to USD 65.5 billion by 2033, at a CAGR of 35.7%"; North America "38.2%" 2025; C2A "53.1%"; "Published: June 2026"; method line "IR Documents, Primary Interviews, Paid Databases" · agrees; report body behind purchase form
- OpenAI commerce GMV absence (floor — agent-executed checkout GMV) · `raw/e-engine-user-count-checks-2026-09-23.md` (n/a — openai.com 403) · `raw/b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23.md` (3) · "More than 700 million people turn to ChatGPT each week"; "U.S. ChatGPT Plus, Pro, and Free users can now buy directly from U.S. Etsy sellers right in chat, with over a million Shopify merchants … coming soon"; "Merchants pay a small fee on completed purchases, but the service is free for users, doesn't affect their prices, and doesn't influence ChatGPT's product results"; "Product results are organic and unsponsored" (2025-09-29) · not in primary (no GMV figure; floor stays `unknown`); the fee clause reads "a small fee", rate undisclosed — a second live-program fee statement beside Copilot Checkout's 0%
- McKinsey agentic commerce $1T US / $3–5T global by 2030 · `raw/e-market-size-mckinsey-agentic-2026-09-22.md` (5 — Digital Commerce 360 pointer) · `raw/e-market-size-mckinsey-agentic-commerce-opportunity-primary-2026-09-23.md` (5) · "by 2030, the US B2C retail market alone could represent an opportunity to orchestrate revenue in the range of $900 billion to $1 trillion. Globally, this opportunity is projected to range from $3 trillion to $5 trillion"; "(These figures only reflect goods and do not yet include services; nor do they account for the significant B2B marketplace.)"; "moderate assumptions about merchant readiness" (2025-10-17) · agrees; primary adds the $900bn lower bound and the goods-only scope; no model or n published on the page (27-page PDF not fetched)

## Image reads, IMG-1a, 2026-09-23

| Figure / text as shown | Chart or image | Date | Tier | Img raw |
|---|---|---|---|---|
| Pie labels: 2026 "0.6%", "$44,321 mn", "$7.3 trillion e-commerce"; 2030 "29%", "$2,916,789 mn", "$10.1 trillion e-commerce"; arrows "185% CAGR¹", "8% CAGR" | "Agentic Commerce as a Proportion of Total e-commerce, Global, 2026 & 2030" (EDC p.14) | 2026-01 | 5 | `raw/e-market-size-edgardunn-agentic-swot-primary-2026-09-23-img-2026-09-23.md` |
| Region pies 2030: North America 27%, EU 26%, APAC 31%, LAC 30%, MEA 30% — pairing confirmed on the rendered page | EDC p.15 | 2026-01 | 5 | same |
| p.11 prints "$2.9 billion"; p.14 prints "$2,916,789 mn" — same figure, two printings, side by side | EDC p.11, p.14 | 2026-01 | 5 | same |
| Generation bands used in the model: Gen Alpha 1-15, Gen Z 13-28, Millennial 29-44, Gen X 45-60, Baby Boomer 61-80 ("as of 2026"; "Sources: Bain, Parents") | EDC p.13 table | 2026-01 | 5 | same |
| Bar labels: "$20.57" (2026), "$144.45" (2029), "8.8%" (2029 share); 2025, 2027, 2028 and all % change redacted | "US Ecommerce Sales via AI Platforms Will Exceed $20 Billion in 2026…" (EMARKETER 358389) | chart "Dec 2025" | 4 | `raw/e-market-size-emarketer-ai-commerce-2026-primary-2026-09-23-img-2026-09-23.md` |
| Scope note: includes Target's app in ChatGPT, Atlas, Google AI Mode; excludes retailer-native assistants, BuyScout, AI search summaries | same | same | 4 | same |

Caveat: EDC pages read from a local render of the saved PDF; nothing on pp. 11–15 prints "$1.7 trillion".
