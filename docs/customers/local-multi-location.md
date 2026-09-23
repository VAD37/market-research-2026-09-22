# Local and multi-location

| | |
|---|---|
| File date | 2026-09-23. Oldest pull depended on: 2026-09-22 — `raw/a-yext-customers-2026-09-22.md`, `raw/a-soci-product-pricing-2026-09-22.md`. Oldest source publication carried: 2024-10-15, Walgreens 10-K FY2024 (headcount only) |
| Cells | 9 — 3 sub-markets × 3 buyer sizes. Reads: spend 1, attention 3, none 5 |
| Cells with a spend signal | 1 of 9 — Organic / Enterprise |
| Signals in the catalogue checked | 12 of 12 in the organic cells (S9 relative index only); 11 of 12 in paid and agentic (S4, S12 n/a by construction; S9 unrun) |

## Segment definition
| | |
|---|---|
| What counts as this vertical | Brands and chains selling through many physical locations — QSR, hotels, dental and chiropractic chains, fitness, pharmacy, home services, salons, senior living — and the franchise system behind them; the buyer is the brand or franchisor, not one outlet |
| Excluded and why | Single-outlet businesses with no chain → out of scope here; hotel groups double as travel (reserve vertical) — counted here, flagged in caveats; beauty retail chains (Ulta, Sephora) → skincare-beauty.md |
| Size bands, as the sources define them | Sources define none. Vendor pages say "multi-location brands" (Birdeye, SOCi, Yext — `raw/a-birdeye-search-ai-product-2026-09-22.md`, `raw/a-soci-product-pricing-2026-09-22.md`, `raw/a-yext-scout-product-2026-09-22.md`) and "small business owners" (Yext Corvo, `raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md`); location counts are stated, headcount is not. Repo bands applied by headcount per `method/demand-signals.md` |
| Buyer-size proxies used, per company | Walgreens Boots Alliance "approximately 312,000 people", filed FY2024 → enterprise. The Joint Corp "approximately 202 persons on a full-time basis and approximately 128 persons on a part-time basis", 960+ clinics, filed → mid-market by headcount (revenue undisclosed here). Choice Hotels "1,562 U.S. and 192 international associates" → enterprise. Hyatt "approximately 242,000 colleagues" → enterprise. IHG 7,109 hotels, half-year revenue $2,659m → enterprise by revenue fallback. Domino's "nearly 7,000 local franchise locations", Brookdale "65 offices", FedEx "725+ locations", Black Bear Diner "150+ Locations", Arrow Senior Living "46 communities": location counts only → `unassigned`. All in `raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md`, `raw/f-yext-customer-stories-local-S2-2026-09-23.md`, `raw/f-birdeye-multilocation-ai-search-S2-S6-2026-09-23.md`, `raw/e-case-birdeye-arrow-senior-living-2026-09-23.md` |

## Cell reads
| Sub-market | Buyer size | Read | Deciding signal, figure, tier, raw path | Signals | Strongest tier | Spend evidence |
|---|---|---|---|---|---|---|
| Organic recommendation | SMB | attention | S5 — r/localseo threads matching `"AI visibility"` 73, `AEO` 47, `"generative engine optimization"` 4, Mar–Sep 2026; top thread "I Lost a Local SEO Client to ChatGPT", score 38, 41 comments; tier 5; `raw/f-reddit-localseo-smallbusiness-franchise-S5-2026-09-23.md`. S6 — Local Falcon self-serve "$24.99 to $199.99 when billed monthly", "Cancel anytime"; BrightLocal 14-day trial; tier 3; `raw/f-localfalcon-brightlocal-whitespark-local-ai-S6-S8-2026-09-23.md`. Both attention class | 2 | 3 | no |
| Organic recommendation | Mid-market | attention | S7 — The Joint Corp 8-K decks, 2026-05-07 "Ongoing SEO and AI visibility optimization", 2026-08-06 "SEO and AI visibility optimization driving organic traffic and lead quality"; no figure named → attention by rule; tier 2; `raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md` | 1 | 2 | no |
| Organic recommendation | Enterprise | **spend** | S1 — Walgreens "Senior Manager, Performance Search & AI Marketing", Deerfield, IL, "$125,000 - $218,750 a year", Indeed card matched on `"generative engine optimization"`; tier 3, spend class; `raw/f-indeed-S1-repull2-2026-09-23.md` #22; Choice Hotels "Senior Manager, Social Media Strategy & Marketing" same match, #21. S2 — Yext 8-K: Scout "increasing citations by 186% for one hearing care provider"; IHG, Domino's, FedEx named Yext customers; tier 2 / 5 | 4 | 2 | yes |
| Paid placement | SMB | none — checked | 11 of 12 signals run or n/a; no local buyer on any paid roster, agency page or filing | 0 | — | no |
| Paid placement | Mid-market | none — checked | as above | 0 | — | no |
| Paid placement | Enterprise | none — checked | as above; Google Direct Offers and ChatGPT Ads rosters name no chain (`raw/f-signal-hr-S2-paid-agentic-check-2026-09-23.md`) | 0 | — | no |
| Agentic commerce | SMB | none — checked | 11 of 12 signals run or n/a | 0 | — | no |
| Agentic commerce | Mid-market | none — checked | as above | 0 | — | no |
| Agentic commerce | Enterprise | attention | S7 — IHG 6-K 2026-08-11: "our ChatGPT plug-in recommends IHG hotels … onward to IHG's direct booking channels", "participating in Google's Agentic AI booking pilot … within Google's AI Mode"; no figure → attention; tier 2; `raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md` | 1 | 2 | no |

## Signals
Class per `demand-signals.md`: S1, S2, S10, S11 spend; S7 spend only with a budget figure, none names one here. Raw prefix `raw/`, suffix `-2026-09-23.md` unless stated.

| Cell | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | Read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organic / SMB | none — checked LinkedIn guest API 8 local queries, 80 cards, none naming GEO/AEO (3, `f-linkedin-guest-api-local-S1`) | Yext "Corvo AI … for small business owners", early version, no customer named (2, `f-edgar-fts-local-multilocation-S7`) — sell-side, moves no cell | none — checked INDEX.md funding table | blank — unattributed: G2 SOCi 4,684 / Birdeye 4,234 reviews, buyer size not exposed (5, `f-g2-capterra-S4-repull`) | r/localseo 73 / 47 / 4 threads (5, `f-reddit-localseo-smallbusiness-franchise-S5`) | Local Falcon $24.99–$199.99/mo; BrightLocal trial (3, `f-localfalcon-brightlocal-whitespark-local-ai-S6-S8`) | none — checked EDGAR FTS 6 queries | none — checked Whitespark summit, BrightLocal LSFG (agenda not rendered), Localogy | Google Trends relative index only, not run for local terms — `unknown — checked trends token gate 2026-09-22` | none — checked TED 12 queries, sam.gov, Contracts Finder (`f-ted-S10-repull2`, `f-procurement-S10-repull`) | none — checked r/localseo thread "hubspot aeo pricing … $50 a month" is a list price, not paid | 2 of 16 answering domains serve llms.txt — Wyndham, Anytime Fitness (1, `f-llms-txt-multilocation-domains-S12`) | attention — S5, S6 |
| Organic / Mid-market | none — checked as above | none — checked Yext, Birdeye, SOCi story pages opened | none — checked | blank — unattributed | blank — unattributed (subreddit, not a company) | blank — unattributed | The Joint Corp decks, no figure (2, `f-edgar-fts-local-multilocation-S7`) | none — checked | as above | none — checked | none — checked | blank — unattributed | attention — S7 |
| Organic / Enterprise | Walgreens $125,000–$218,750; Choice Hotels $123,663–$145,486 (3, `f-indeed-S1-repull2`) | Yext hearing-care 186% citations (2 filed, vendor claim); IHG, Domino's, FedEx, Brookdale story pages, no AI metric (5, `f-yext-customer-stories-local-S2`); Birdeye Arrow Senior Living 46 communities (5, `e-case-birdeye-arrow-senior-living`) | Yext ARR $440.8M, filed (2, `INDEX.md`) — vendor, not buyer | blank — unattributed | blank — unattributed | Birdeye study 16,240 scans, 1,500+ brands, "18.6% of locations never surfaced" (5, `f-birdeye-multilocation-ai-search-S2-S6`) — sell-side | Hyatt 10-K names ChatGPT, Claude, Gemini, Grok as "alternative distribution channels"; Yelp, 1-800-Flowers risk factors (2) | none — checked | as above | none — checked | none — checked | as SMB row | **spend** — S1 |
| Paid / SMB, Mid, Enterprise | none — checked Indeed cards, LinkedIn | none — checked Direct Offers, ChatGPT Ads, Perplexity rosters (`f-signal-hr-S2-paid-agentic-check`) | none — checked | n/a by construction | none — checked r/localseo, r/franchise `"AI search"` 0 | none — checked agency pages (`f-signal-sk-S6-paid-agencies`, `f-signal-bs-S5-S6-paid-agentic`) name no chain | none — checked EDGAR FTS | none — checked | unrun | none — checked TED | none — checked | n/a | none — checked |
| Agentic / SMB, Mid | none — checked | none — checked UCP, ACP, Instant Buy rosters | none — checked | n/a | none — checked r/franchise 0 | none — checked | none — checked | none — checked | unrun | none — checked | none — checked | n/a | none — checked |
| Agentic / Enterprise | none — checked | IHG in Google agentic booking pilot (2, `f-edgar-fts-local-multilocation-S7`) — self-filed, no metric | none — checked | n/a | none — checked | none — checked | IHG ChatGPT plug-in, AI Mode pilot (2) | none — checked | unrun | none — checked | none — checked | n/a | attention — S7 |

## Cells with no signal — channels checked
| Cell | Signals checked | Channels checked | Date | Result |
|---|---|---|---|---|
| Paid × 3; Agentic / SMB, Mid | 11 of 12 (S9 unrun; S4, S12 n/a) | Indeed cards (35), LinkedIn guest API (8 queries), EDGAR FTS (6 queries, 5 answered), Yext / Birdeye / SOCi / Local Falcon / BrightLocal / Whitespark pages, Arctic Shift r/localseo r/franchise (r/smallbusiness 422 on 5 of 7 windows, 0 on 2), TED, sam.gov, Contracts Finder, G2 via Wayback, franchise trade press (walled: `raw/f-franchise-trade-press-search-wall-2026-09-23.md`) | 2026-09-23 | none found |

## Willingness to pay
| Cell | Price actually paid | What it bought | Who disclosed it | Label | Raw |
|---|---|---|---|---|---|
| all nine | unknown — checked EDGAR FTS, TED, r/localseo, vendor story pages 2026-09-23 | — | — | — | `raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md`; `raw/f-reddit-localseo-smallbusiness-franchise-S5-2026-09-23.md` |

Asking prices on record, not prices paid: Local Falcon $24.99–$4,999/mo credit packages; HubSpot AEO "$50 a month" as quoted by a r/localseo poster; Yext, SOCi, Birdeye, Uberall undisclosed (`competitors/INDEX.md`). Walgreens and Choice Hotels salary bands are headcount cost.

## Engine × segment and buying process
Mentions over the 30 local raw files (24 on disk before this pass, 6 new): Gemini / AI Mode / AI Overviews 102 (15 files), ChatGPT 97 (17), Perplexity 52 (16), Claude 25 (9), Grok 8 (4), Copilot 6 (4), Rufus 0 — `raw/f-engine-mentions-raw-count-2026-09-23.md`, measured-by-us word count; the pre-pass row used a wider pattern, see its note. Cell-attributable: Agentic / Enterprise — IHG names ChatGPT and Google AI Mode (2); Organic / Enterprise — Hyatt names ChatGPT, Claude, Gemini, Grok as competition, not as a target (2); vendor pages name ChatGPT, Gemini, Perplexity (Birdeye), ChatGPT, AI Overviews, AI Mode, Gemini, Grok (Local Falcon) — sell-side. Local Falcon is the only vendor in any vertical whose pages name Grok as a tracked surface. Buying process: `unknown — checked every raw file cited here 2026-09-23`; vendor-side, Yext "annual and multi-year subscriptions", "non-cancelable contracts" (2), SOCi term per Order Form with a six-month tail (3), Local Falcon and BrightLocal monthly cancel-anytime (3) — `raw/a-vendor-terms-contract-length-2026-09-23.md`. Franchisor-vs-franchisee decision path: no source states it.

## Reserve-vertical trigger — read, not applied
`method/plan.md` L233 opens consumer electronics and travel "only if the anchor set produces no Gold or Silver cases". Gold: 0 on every reading (`findings/proof-scorecard.md`). Silver: `grade_raw` B2B SaaS 1 (E4), high-CPA 1 negative (E6), skincare 0 → **not met**; `grade_rule1` all three verticals 0 → **met**. Both stand. Neither vertical opened here. Travel evidence already in raw without a pass: visitBerlin TED notice with a "Konzeptpapier GEO" requirement, EUR 3,647,000 (2, `raw/f-ted-S10-repull2-2026-09-23.md`); Hyatt and IHG filings above; MakeMyTrip 20-F in the "AI search" FTS hit list, not opened; six hotels head the llmstxt.site directory (`raw/e-wayback-llms-txt-directories-2026-09-23.md`). Consumer electronics: nothing surfaced in any channel this pass.

## Hypotheses touched
| H | What this vertical contributes | Status after this file |
|---|---|---|
| H4 — attention-only in every SMB cell | Local Organic / SMB reads attention (S5, S6), Paid and Agentic / SMB none | consistent with the kill already recorded; adds no SMB spend cell |
| H7 — organic ahead of paid and agentic | Organic 1 spend, paid 0, agentic 0 | consistent; outside the 27-cell count |
| H9 — agentic spend enterprise-only | Agentic / Enterprise reads attention (IHG), not spend | neither confirms nor kills |

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Posting bodies for the Walgreens, Choice Hotels, Ziggi's Coffee, RestauNax, A Place for Mom, MAHEC cards — whether GEO/AEO is a duty or an Indeed match artefact | Indeed card data only (`f-indeed-S1-repull2`); queued to P16-c4b | 2026-09-23 |
| r/smallbusiness thread volume on AI-visibility terms | Arctic Shift: HTTP 422 "Timeout" on 5 of 7 windows; 0 threads on the two 3-month aggregates that answered | 2026-09-23 |
| Franchise trade-press coverage counts (S8-adjacent) | franchising.com (no result list), franchisetimes.com 429, qsrmagazine.com 403, restaurantbusinessonline.com and 1851franchise.com (script-rendered) | 2026-09-23 |
| SOCi, Birdeye, Uberall customer counts by location band; Yext Scout customer count | vendor pages, 8-K; not stated | 2026-09-23 |

## Caveats
- Every read rests on internet-only proxies; no signal observes a budget (`scope.md` R2). The one spend cell rests on S1 — "headcount budget, not category spend — weakest spend class" — and on an Indeed card whose posting body was not read; Indeed's phrase match is not verified per posting.
- Attention cells rest on filings that name the activity and no figure (The Joint Corp, IHG) and on a subreddit archive at tier 5 with coverage unverified; September counts are partial.
- The vertical overlaps travel (Hyatt, IHG, Choice, Wyndham) and healthcare (dental, chiropractic, senior living); a reader opening the travel reserve vertical will re-cut these rows. Buyer-size bands are a method choice; every source here states location counts, not headcount, so five named brands read `unassigned`.
- Vendor-side evidence is dense (Birdeye study, Yext 8-K, Local Falcon pages) and buyer-side thin; nothing from a vendor's target-customer page moved a cell. Publication bias runs one way: the five `none` reads are weaker evidence than the one `spend` read.
- S9 was not run for local terms (Google Trends token gate, 2026-09-22 record); S4 and S12 are `n/a by construction` in paid and agentic, following the three existing files.

## S1 posting bodies, P16-c4b, 2026-09-23

Indeed walled on the first posting page (Cloudflare "Additional Verification Required", 16:21); bodies read from employer career sites instead. Raw: `raw/f-indeed-S1-repull3-2026-09-23.md` (tier 3, company-stated). Format: employer · title · phrase in body · engines named · budget or tool named · salary · size band · raw section.

- Walgreens · "Senior Manager, Performance Search & AI Marketing" · yes — "Generative Engine Optimization (GEO), AI Search Optimization (AISO), conversational search experiences" · none by name; "traditional search engines, AI assistants, and emerging discovery platforms" · no figure; "managing significant media investments", agency partners · "$125000 - $218,750.00 / Salaried" · Enterprise — "approximately 220,000 team members" (body, 2026-09-10) beside the filed ~312,000 above · §posting #22
- Choice Hotels · "Senior Manager, Social Media Strategy & Marketing" · yes — "Collaborate with the Paid Media team on their social content within GEO (Generative Engine Optimization) strategies"; "LLM visibility and content discoverability" · none · none · "$123,663.00 - 145,486.00" plus MIP bonus · `unassigned` from the body ("7,500 hotels in 45+ countries", headcount absent); Enterprise stands on the filed headcount in this file · §posting #21
- A Place for Mom · "Staff Product Manager, Acquisition & Growth" · yes — "AI / Generative Engine Optimization (GEO) and emerging distribution"; "AI search citations", "MCP integrations", "agentic endpoints" · none by name · none; "existing AI discovery measurement framework and tooling", unnamed · "Base Salary: $165,000 – $195,000", "Bonus: 10% Corporate Bonus" · `unassigned` ("15,000+ senior living communities" in network; headcount absent) · §posting #4
- MAHEC · "Director, Marketing and Brand Strategy" · yes — "search engine optimization (SEO), generative engine optimization (GEO), analytics" · none · none; "administers, and monitors departmental budgets", no figure · none in body · `unassigned` · §posting #6
- Ziggi's Coffee · "Senior Manager, Performance Marketing" · unread — Indeed wall; ziggiscoffee.com careers carries store roles only · — · — · card "$120,000 - $150,000 a year" · `unassigned` · §Checked, not found
- RestauNax · "AI-Native Marketing Lead" · unread — Indeed wall; restaunax.com has no careers page · — · — · card "$10 - $25 an hour" · `unassigned` · §Checked, not found

Cell check. Organic / Enterprise **spend** rested on the Walgreens #22 and Choice Hotels #21 cards: **confirmed** — the phrase is in both bodies as a duty, not an Indeed match artefact. A Place for Mom (referral marketplace, remote) and MAHEC (one regional healthcare and education organisation) sit at this vertical's boundary; both bodies name GEO as a duty; neither is band-attributable; neither moves a cell. Six bodies name no assistant by brand.
