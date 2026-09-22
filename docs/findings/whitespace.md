# Whitespace — where the evidence shows nothing at all

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every `raw/` file cited. Oldest source publication carried: 2024-11-12, `raw/b-perplexity-ads-launch-2026-09-22.md`, via `markets/paid-placement.md` |
| Lane | A, B, C and D, read across |
| Hypotheses touched | H2, H8, H12, H13, H15, H16, HE1 (scored in `unknowns.md`) |
| Claims at tier 3 or better | 6 of 8 |

## Question

> Where in this market does the evidence gathered so far record nothing — no vendor, no engine, no case, no number?

## Answer

Observations, not recommendations. The gaps sit in three places: **price** (no engine publishes a rate card for any AI-surface ad unit, no buyer discloses a price paid, no protocol states a fee), **method** (no vendor discloses the prompt set behind a composite score, no engine names three of six documented manipulation techniques), and **corroboration** (no named brand confirms a vendor claim on its own property, and no sub-market has a measured size).

## Evidence

| # | Gap — stated as an observation | Figure, verbatim where one exists | Compiled file | Raw behind it | Tier |
|---|---|---|---|---|---|
| E1 | No rate card exists for any AI-surface ad unit | "0 of 8 publish a rate card"; the only price any engine states is OpenAI's recommended max bid, "$3–$5 USD per click" | `markets/paid-placement.md` | `raw/b-openai-platform-summary-`, `b-google-platform-summary-`, `b-microsoft-amazon-platform-summary-2026-09-22.md` | 3 |
| E2 | No sub-market has a measured size | 18 published figures: 15 author-labelled forecasts, 3 measured — and "zero of these three carries a market-size figure with a forward target year" | `markets/organic-recommendation.md`, `paid-placement.md`, `agentic-commerce.md` | `raw/e-market-size-table-2026-09-22.md` | 3 |
| E3 | Bottom-up sizing is not computable for two of three sub-markets; the third yields a floor over 12% coverage | organic **$5.3M–$35.2M annualised** from 4 of 34 rostered vendors; paid and agentic `unknown — cannot be built from disclosed inputs` | same three | `raw/a-vendor-census-c1-`…`-c4-`, `c-vendor-census-c6-2026-09-22.md` | 5 |
| E4 | No vendor discloses the prompt set behind a composite score | "0 of 34 rostered vendors disclose a fixed published prompt set with n"; Ahrefs the fullest partial ("454M+ prompts"); no profile among the 41 in `competitors/` records one either | `markets/organic-recommendation.md`; `competitors/*.md` | `raw/a-vendor-census-c1-`…`-c4-2026-09-22.md` | 3 |
| E5 | No priority-1 engine names corpus seeding, comparison-page farming, or citation-preference content as a policy category | 6 of 36 engine × technique cells read `named`; the 6 sit in prompt injection (4 engines), fake reviews (Anthropic) and a Google disclaimer | — | `raw/d-technique-census-c7-2026-09-22.md` | 3 |
| E6 | llms.txt is read by no engine measured | "**No tool requested llms.txt**" — 15 tools × 3 trials, zero fetch events; Google states "You don't need to create new machine readable files, AI text files, or markup" | `markets/organic-recommendation.md` | `raw/d-structured-arxiv-borysenko-http-fingerprints-`, `a-google-ai-features-guidance-2026-09-22.md` | 4 |
| E7 | No technique in Lane D has a published single-action before-and-after on a production surface | "0 in this cluster's 12 pulls" have a true before-and-after design; 70 candidates screened | — | `raw/d-technique-census-c1-`…`-c7-2026-09-22.md` | 4 |
| E8 | The supplements sub-vertical produced no cleared case; the anchor vertical produced no Silver | supplements **6 screened / 0 cleared**; skincare ~133 screened, 2 Bronze, 0 Silver | `customers/high-cpa-regulated.md`, `customers/skincare-beauty.md` | `raw/e-case-census-c10-`, `-c8-2026-09-22.md` | 5 |
| E9 | Brand-side corroboration is absent across every brand checked | ~166 brands named; 59 checked on their own domains; **0 corroborate, 0 contradict, 59 silent**; ~107 not checked (cap) | `markets/organic-recommendation.md` | `raw/e-case-census-c7-2026-09-22.md` | 3 |
| E10 | No fee is disclosed anywhere in the agentic chain but one | 6 of 6 protocol fee clauses `unknown — checked`; 1 of 4 live checkout programs states a fee — Copilot Checkout, "does not take a commission or affiliate fee" | `markets/agentic-commerce.md` | `raw/c-agentic-commerce-protocols-table-`, `b-microsoft-agentic-commerce-2026-09-22.md` | 3 |
| E11 | No ad repository anywhere distinguishes an ad inside a conversational AI answer | ChatGPT designated VLOSE 2026-08-31, 159.1M EU recipients, no Art. 39 repository yet; Google, Bing, Amazon Store and X repositories name no AI surface | `markets/paid-placement.md` | `raw/b-eu-dsa-ad-repositories-table-`, `b-regulators-ad-disclosure-table-2026-09-22.md` | 2 |
| E12 | No retail-analytics publisher breaks any AI figure out per engine | `unknown — checked Adobe, Salesforce, Shopify 2026-09-22` | `markets/agentic-commerce.md` | `raw/c-retail-analytics-table-2026-09-22.md` | 4 |

E1 conflicts with nothing; E2 sits beside three named present-state figures (OpenAI's $1B annualized run rate, tier 3; Adthena 4.47%, tier 5; Similarweb 26%, tier 5) which are not sizes — **recorded side by side, not reconciled into one**.

### Priority-1 engine × sub-market cells — the done-condition row

Nine cells, each a number or an explicit `unknown — checked <path>`.

| Engine | Organic recommendation | Paid placement | Agentic commerce |
|---|---|---|---|
| **ChatGPT — OpenAI** | 3 crawler tokens (OAI-SearchBot, GPTBot, ChatGPT-User); 1 referral tag, `utm_source=chatgpt.com`; **0** native visibility tools — `unknown — checked raw/a-openai-publishers-developers-faq-2026-09-22.md` | product live from 2026-02-09; **$1B annualized run rate** (tier 3); ad presence 26% (Similarweb) vs 4.47% of US queries (Adthena) vs 0.00% of 169,560 UK scrapes — three figures, not reconciled; **0** rate cards | Instant Checkout live on ACP; fee `unknown — checked raw/c-openai-commerce-get-started-2026-09-22.md`; merchant count `unknown — checked` same |
| **Claude — Anthropic** | 3 crawler tokens (Claude-SearchBot, ClaudeBot, Claude-User); **0** inclusion-guidance pages, **0** referral tags, **0** native tools — `unknown — checked raw/b-anthropic-perplexity-platform-summary-2026-09-22.md` | **0** — "Claude will remain ad-free… nor will Claude's responses… include third-party product placements", 2026-02-04 (tier 3) | **0** programs found; MCP transport only; "Project Deal" a 69-employee internal pilot — `unknown — checked raw/c-anthropic-mcp-connector-2026-09-22.md` |
| **Google — AI Overviews, AI Mode, Gemini** | 1 reporting surface (Search Console "Web" type, no AI-specific segment); 1 crawler token named (Google-Extended, "Does not impact a site's inclusion"); Gemini app: **0** on all four cells — `unknown — checked raw/b-google-platform-summary-2026-09-22.md` | AI Overviews live, 12 named countries within-AIO and "200+ markets" above/below; AI Mode "testing", 5 named formats, pricing model `unknown — checked raw/b-google-gml2026-search-ads-2026-09-22.md`; Gemini app format `unknown — checked` same; **0 ad units observed in 90 measured runs**, tier 1 | UCP live for "select merchants"; fee `unknown — checked raw/c-google-merchant-ucp-checkout-2026-09-22.md`; country scope conflicts — "United States, Canada, and Australia" vs "eligible U.S. retailers", both kept |

**Done-condition row — "Priority-1 engine × sub-market cells" (bar: every cell a number or an explicit `unknown — checked`): satisfied, 9 of 9.**

### The builder-constraint question, returned unanswered

`scope.md` demotes "whether a cost-advantaged team can win it" to a question for `findings/` once the market is mapped, and `scope.md` revision 2 makes it a hypothetical only. It is returned here as the question it is, with no answer attempted: **which of the gaps above, if any, is reachable by a team whose cost advantage is engineering rather than distribution?** No evidence in `docs/` addresses it. `scope.md` also records, and does not endorse, the user's 2026-09-22 framing that "everyone needs it"; that framing is not tested by anything in this file.

## Claims

| # | Claim | Evidence | Tier of weakest row | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | No engine publishes a rate card for any AI-surface ad unit; 0 of 8 | E1 | 3 | n/a | yes |
| C2 | No sub-market has a measured size; 15 of 18 published figures are author-labelled forecasts and the 3 measured ones are present-state metrics, not sizes | E2 | 3 | n/a | yes |
| C3 | No priority-1 engine names corpus seeding, comparison-page farming, or citation-preference content as a policy category | E5 | 3 | n/a | yes |
| C4 | No vendor discloses a prompt set with n behind a composite visibility score | E4 | 3 | n/a | yes |
| C5 | No engine measured fetches llms.txt, and one engine states in its own docs that no such file is needed | E6 | 4 | n/a | yes |
| C6 | Two evidence deserts inside the tracked verticals: supplements 0 cleared at 6 screened, skincare 0 Silver at ~133 screened | E8 | 5 | Bronze at best | yes |
| C7 | No named brand corroborates a vendor claim on its own property; 59 of 59 checked are silent | E9 | 3 | n/a | yes |
| C8 | Every priority-1 engine × sub-market cell carries a number or an explicit `unknown — checked`; 9 of 9 | per-engine table | 3 | n/a | yes |

## Survivorship

Published cases are winners; the screened and cleared counts behind E8 and the case corpus are stated once, in `proof-scorecard.md`. This file rests on absences in vendor, engine and protocol documentation rather than on published cases, except E8.

## Unknowns

| Question | Channels checked | Date | Why not answerable from the channels used |
|---|---|---|---|
| Any engine rate card, and a precise advertiser count for any engine | openai.com, openai.com/de-DE, support.google.com/google-ads, about.ads.microsoft.com, advertising.amazon.com | 2026-09-22 | "tens of thousands of advertisers" is the only count any engine states |
| Take rate at any reseller, sell-side or protocol stage | advertising.amazon.com, criteo.com, stackadapt.com, pacvue.com (404), kargo.com, each protocol owner's own domain | 2026-09-22 | no fee clause appears in any protocol spec |
| Any Gartner, Forrester, IDC, EMARKETER or Statista size for organic recommendation | DuckDuckGo html endpoint, multiple queries; emarketer.com (subscription-gated) | 2026-09-22 | the named houses publish nothing reachable; the gated reports were not opened |
| Gemini app ad format; pricing model for Google AI Mode's five named formats; on-surface label wording for Copilot and Amazon | support.google.com/google-ads, blog.google/products/ads-commerce, about.ads.microsoft.com, advertising.amazon.com | 2026-09-22 | the pages exist and name formats without naming prices or label text |
| Whether Microsoft and Amazon name any of the six Pass-5 techniques | bing.com/webmasters (JS-rendered), learn.microsoft.com (404), amazon.com review-guidelines (503 / JS shell) | 2026-09-22 | policy surfaces unreachable without a browser; browser backlog |
| Whether the ~107 unchecked brands corroborate anything | brand newsrooms, IR and case pages — 59 of ~166 checked | 2026-09-22 | cluster cap, not exhaustion |

## Caveats

- C1, C2, C3, C4, C7 and C8 are load-bearing at tier 3 and rest on platform-primary and vendor-primary pages — reliable on existence, biased on framing (`method/trust-rubric.md`). C5 is tier 4 and C6 tier 5.
- Every gap above is an absence on the channels named, not proof that nothing exists. Five channels were blocked rather than exhausted this session: sec.gov, reddit.com, G2 / Capterra, Indeed / Upwork, Google Trends.
- The measured-by-us row in the engine table (0 ad units across 90 runs on Google AI Mode and AI Overviews) is one date, one localised network path, logged-out, and text-extraction-scoped: an icon-only or CSS-only "Sponsored" label would not be caught. It bounds nothing about the market.
- No metric crossing is relied on in this file; E3's dollar figure is a coverage-limited floor, never cited as a size.
- Conflicts left unreconciled: the three ChatGPT ad-presence percentages; Google's two UCP country statements; E2's three measured present-state figures beside 15 forecasts.
- The oldest pull cited is 2026-09-22; two pages behind the paid-placement cells are dated 2025-12-08 and 2025-08-06 and are flagged stale in their own raw files (`method/plan.md` staleness rule).
- This file carries evidence, not a verdict. It names gaps; it does not propose filling any of them.
