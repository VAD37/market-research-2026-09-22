# High-CPA regulated — cards, insurance, supplements
| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — `raw/f-signal-census-hr-2026-09-22.md` and the 12 files it cites; underlying documents 2026-02-25 (NerdWallet 8-K) to 2026-09-17 |
| Cells | 3 sub-markets × 3 buyer sizes = 9. Cells with a spend signal: 1 — organic recommendation / enterprise |
| Catalogue signals checked | 10 of 12 (S2, S3 not swept per cell; S9 unreachable). Signals found with no buyer band stated: 9, across S1, S2, S7, S8 |

## Segment definition
| | |
|---|---|
| What counts, and what is excluded | Credit cards, insurance, supplements (`method/plan.md` §Verticals). Out: loans, mortgage, tax, legal — LendingTree, LegalZoom, H&R Block, whose sources name no vertical — `raw/e-case-census-c1-2026-09-22.md`, `raw/e-case-census-c10-2026-09-22.md` |
| SMB and mid-market, as the sources define them | No source in this vertical defines a band. Fixed bands apply: under 100 / 100–999 headcount, 50M and 1B USD revenue fallbacks — `method/demand-signals.md` |
| Enterprise, as the source defines it | "Enterprise Technical Search Lead/Analyst… the enterprise subject matter expert… a large enterprise ecosystem" — The Cigna Group, `raw/f-signal-hr-S1-linkedin-2026-09-22.md`. Word only, no headcount or revenue |

## Cell reads — nine cells, S1–S12
| Sub-market | Size | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | Read | Deciding signal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organic | SMB | blank — unattributed | blank — unattributed | unchecked | none — checked | none — checked | none — checked | blank — unattributed | blank — unattributed | unchecked | none (sam.gov) / unknown (UK CF, TED) | none — checked | n/a — vertical-level | blank | No source states SMB; S3, S9 unchecked, S10 part-unresolved |
| Organic | Mid-market | blank — unattributed | blank — unattributed | unchecked | none — checked | none — checked | none — checked | blank — unattributed | blank — unattributed | unchecked | none / unknown | none — checked | n/a | blank | No source states mid-market; S3, S9 unchecked |
| Organic | Enterprise | **1 posting, "Enterprise", The Cigna Group (tier 3)** | blank — unattributed | unchecked | none — checked | none — checked | none — checked | blank — unattributed | blank — unattributed | unchecked | none / unknown | none — checked | n/a | **spend** | S1, spend class, tier 3, cell stated by source — `raw/f-signal-hr-S1-linkedin-2026-09-22.md` |
| Paid | SMB | none — checked | unchecked | unchecked | none — checked | none — checked | none — checked | none — no paid-framed case | none — checked | unchecked | none / unknown | none — checked | n/a | blank | S1, S4–S8, S11 none; S2, S3, S9 unchecked, S10 part |
| Paid | Mid-market | none — checked | unchecked | unchecked | none — checked | none — checked | none — checked | none — no paid-framed case | none — checked | unchecked | none / unknown | none — checked | n/a | blank | As above |
| Paid | Enterprise | none — checked | unchecked | unchecked | none — checked | none — checked | none — checked | none — no paid-framed case | none — checked | unchecked | none / unknown | none — checked | n/a | blank | As above |
| Agentic commerce | SMB | none — checked | unchecked | unchecked | none — checked | none — checked | none — checked | none — no agentic case | blank — unattributed | unchecked | none / unknown | none — checked | n/a | blank | S8 found, band not stated; S2, S3, S9 unchecked |
| Agentic commerce | Mid-market | none — checked | unchecked | unchecked | none — checked | none — checked | none — checked | none — no agentic case | blank — unattributed | unchecked | none / unknown | none — checked | n/a | blank | As above |
| Agentic commerce | Enterprise | none — checked | unchecked | unchecked | none — checked | none — checked | none — checked | none — no agentic case | blank — unattributed (John Lewis FS) | unchecked | none / unknown | none — checked | n/a | blank | S8 John Lewis FS names no headcount or revenue |

## Signals — figure, tier, channels, pull path
| Signal | Observation, vertical-wide | Class | Tier | Channels checked 2026-09-22 | Raw |
|---|---|---|---|---|---|
| S1 job postings | 6 qualifying postings; employers GEICO, Amica, Embrace Pet, Cigna, Insurify, Juice Plus+, Simply Business; cards 0 of 9 queries | spend | 3 | LinkedIn Jobs, 21 queries; indeed.com 403; upwork.com 403; freelancer.com 200, empty | `raw/f-signal-hr-S1-linkedin-2026-09-22.md`, `raw/f-signal-hr-S1-indeed-upwork-freelancer-2026-09-22.md` |
| S2 vendor logos | Jerry.ai (Sitefire), Zurich Insurance UK (Conductor), The Hartford + Aetna (Brandlight), MidFirst Bank (Yext) | spend | 6 — no n, no date | Pass 3 vendor customer rosters, 23 files grepped | `raw/e-case-census-c10-2026-09-22.md`, `raw/e-case-c13-conductor-multi-2026-09-22.md`, `raw/a-vendor-census-c3-2026-09-22.md` |
| S3 funding and ARR | Not swept per vertical; roster records Primerica as "Financial services company; not a category seller" | ARR spend / round attention | unchecked | vendor roster only | `raw/a-vendor-roster-2026-09-22.md` |
| S4 review volume | none — no reviewer-industry breakdown for any GEO vendor; LoyJoy adjacent, discarded | spend if purchase-verified | n/a | g2.com 403, capterra.com 403, omr.com/en/reviews/category/ai 200 | `raw/f-signal-hr-S4-review-sites-2026-09-22.md` |
| S5 community threads | none — 0 on-topic threads; 1 vendor-side hit (GeoArk AI Show HN, 2026-03-09), not vertical-specific | attention | n/a | HN Algolia, 7 queries; reddit.com 403 | `raw/f-signal-hr-S5-community-2026-09-22.md` |
| S6 agency pages | none — 5 rostered agencies name no client here; 2 fresh results opened, both discarded | attention | n/a | `f-agency-census-c5`, lite.duckduckgo.com; html.duckduckgo.com 403 | `raw/f-signal-hr-S6-agency-pages-2026-09-22.md`, `raw/f-agency-census-c5-2026-09-22.md` |
| S7 filings and decks | Primerica 10-K exec bio; NerdWallet cards -24% YoY; LendingTree and EverQuote statement-only. No budget figure named | attention — S7 spend needs a named figure | 2 | EDGAR full-text, 18 filer hits, 2026-01-01 to 2026-09-22 | `raw/f-signal-hr-S7-primerica-10k-2026-09-22.md`, `raw/f-signal-hr-S7-p4c1-crossref-2026-09-22.md` |
| S8 conference agendas | 4 name-matches: NerdWallet, Mutual of Omaha, Franklin Templeton (GEO Conf NYC); John Lewis Financial Services (MozCon London) | attention | 3 | 9 events, 6 `f-conference-*` files grepped | `raw/f-signal-hr-S8-conferences-2026-09-22.md` |
| S9 search interest | unknown — JS-rendered surface, no browser tool held; Similarweb, Datos, SparkToro, StatCounter publish no vertical cut | attention | n/a | trends.google.com/trends/explore — not reached | `raw/f-signal-hr-S9-search-interest-2026-09-22.md` |
| S10 procurement | none on sam.gov (2 queries, 0 qualifying); unknown on UK Contracts Finder (keyword filter non-functional) and TED (405) | spend | 2 | sam.gov API, contractsfinder OCDS API, ted.europa.eu | `raw/f-signal-hr-S10-procurement-2026-09-22.md` |
| S11 price paid | none — no buyer in this vertical discloses a price paid; hits were list prices and vendor vertical-landing pages, excluded by rule | spend | n/a | lite.duckduckgo.com, 1 query; cross-ref S1, S6, S7 | `raw/f-signal-hr-S11-price-paid-2026-09-22.md` |
| S12 on-property artifacts | 3 of 9 resolved domains (33%) served a real `/llms.txt`: bankrate.com, everquote.com, ritual.com; 1 hit per sub-vertical | attention | 1 measured-by-us | 10 brand domains, direct GET | `raw/f-signal-hr-S12-llmstxt-sample-2026-09-22.md` |

## Unattributed signals — found, not assigned to a cell
| Item, as the source names it | Sub-vertical | Signal | Tier | Why unassigned | Raw |
|---|---|---|---|---|---|
| GEICO — "SEO & AI Search Content Writer – Commercial Insurance", "AEO Outreach Manager"; Amica — "SEO Generative/AI Search Analyst"; Embrace Pet Insurance — "Organic Search / SEO Manager" | insurance | S1 | 3 | no band stated; "one of the largest auto insurers" is not a headcount or revenue figure | `raw/f-signal-hr-S1-linkedin-2026-09-22.md` |
| Insurify — "Senior Manager, AI Search & Discovery (GEO/AEO)"; "$130M total funding" | insurance | S1 | 3 | funding is neither headcount nor revenue | same |
| The Juice Plus+ Company — "Senior Manager, Growth Marketing & Search" | supplements | S1 | 3 | scope is geographic ("Global", "USA"), not size | same |
| Simply Business — "Senior Manager, SEO & GEO"; salary $114,700–$189,200 | insurance | S1 | 3 | its customers are small businesses; its own band is unstated | same |
| Primerica 10-K — Chief Reputation Officer role includes "search and generative engine optimization" | insurance | S7 | 2 | headcount XBRL-tagged, not extractable this pull | `raw/f-signal-hr-S7-primerica-10k-2026-09-22.md` |
| NerdWallet 8-K — "Credit cards revenue of $26.5 million decreased 24% year-over-year"; insurance +13% | cards, insurance | S7 | 2 | no band stated; a revenue-impact figure, not a spend figure | `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md` |
| Conference names: NerdWallet, Mutual of Omaha, Franklin Templeton, John Lewis Financial Services | insurance, finance | S8 | 3 | neither agenda states a band for any name | `raw/f-signal-hr-S8-conferences-2026-09-22.md` |
| Vendor-named customers: Jerry.ai, Zurich Insurance UK, The Hartford, Aetna | insurance | S2 | 6 | no band, no n, no date; logos, not contracts | `raw/e-case-census-c10-2026-09-22.md`, `raw/e-case-c13-conductor-multi-2026-09-22.md` |

## Personas, jobs-to-be-done, switching costs, buying process
| | |
|---|---|
| Persona, title verbatim | "Lead Analyst, Technical Search (SEO/AEO/GEO)"; sits in "the Paid Media Center of Expertise within the Marketing and Communication organization" — The Cigna Group, `raw/f-signal-hr-S1-linkedin-2026-09-22.md` |
| Job-to-be-done, employer-stated | "drive AI readiness, technical governance, automation, and innovation"; "improve search performance across a large enterprise ecosystem" — Cigna, same file |
| Job-to-be-done, CEO-stated | "our focus remains on building durable consumer relationships and making NerdWallet a no-brainer destination for shopping financial products" — Tim Chen, Co-Founder and CEO, 2026-02-25, `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md` |
| Switching costs, buying process | unknown — no source states either. Every named brand is silent on its own property: Jerry.ai, Grüns, The Hartford, Aetna, all `silent — checked` — `raw/e-case-census-c7-2026-09-22.md` |

## Willingness to pay
| Cell | Price actually paid | Raw |
|---|---|---|
| All nine | `unknown — checked lite.duckduckgo.com, EDGAR, vendor pricing pages 2026-09-22` | `raw/f-signal-hr-S11-price-paid-2026-09-22.md` |

## Proof landscape, per sub-vertical
| Sub-vertical | Screened / cleared | What cleared | Raw |
|---|---|---|---|
| Cards | 16 / 1 | NerdWallet, Silver, **negative direction** — cards revenue -24% YoY "due to continued headwinds in organic search traffic" | `raw/e-case-census-c10-2026-09-22.md`, `raw/e-case-census-c1-2026-09-22.md` |
| Insurance | 12 / 2 | Sitefire / Jerry — **Bronze** per c10, **Silver** per c13's full-page re-grade. Both stand, side by side, not merged | `raw/e-case-census-c10-2026-09-22.md`, `raw/e-case-census-c13-2026-09-22.md` |
| Supplements | 6 / 0 | Zero. Grüns / AthenaHQ (Bronze) is not vertical-tagged by its own source, so it is not counted here | `raw/e-case-census-c10-2026-09-22.md` |
| Corroboration and nulls | 0 of 4 corroborate; 0 nulls | Jerry.ai, Grüns, The Hartford, Aetna silent on their own domains; no null-result item names this vertical | `raw/e-case-census-c7-2026-09-22.md`, `raw/e-case-census-c11-2026-09-22.md` |

## Hypotheses touched
| ID | What this file contributes |
|---|---|
| H4 | All three SMB cells here read `blank`, not `spend`. No SMB cell in this vertical carries a source-attributed signal of any class |
| H7 | Within this vertical: organic 1 spend cell, paid 0, agentic 0 — consistent with H7's direction, on one vertical of three |
| H9 | No agentic cell reads spend, enterprise included. The one agentic signal (S8, John Lewis Financial Services) states no band |
| H11 | No transition case at tier 3 or better here: Sitefire/Jerry is tier 5 vendor-reported, Conductor/Zurich UK tier 6, NerdWallet tier 2 but names no brand action |
| H14 | Lane D density runs against H14's direction: regulated 0 filed specimens (`raw/d-technique-census-c2-2026-09-22.md`); 1 affiliation-only adjacent item vs B2B SaaS 1 tested specimen (`raw/d-technique-census-c3-2026-09-22.md`) |

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Do Indeed or Upwork carry postings this vertical that LinkedIn missed? | indeed.com 403, indeed.com/rss 403, upwork.com 403, upwork RSS 403 | 2026-09-22 |
| Does any review site or practitioner thread name this vertical? | g2.com 403, capterra.com 403, omr.com 200 (general AI category only); reddit.com 403, HN Algolia 7 queries | 2026-09-22 |
| What is search interest for category terms inside this vertical? | trends.google.com — JS-rendered, not reachable without a browser tool | 2026-09-22 |
| Does any procurement register carry an award naming the category? | sam.gov 200 (no match), contractsfinder OCDS 200 (keyword filter non-functional), ted.europa.eu 405 | 2026-09-22 |

## Caveats
- Internet-only proxies, no interview (`scope.md` R2). No signal observes a budget; the one `spend` read evidences that money moved somewhere in that cell, not how much. Underlying documents run 2026-02-25 to 2026-09-17, none stale under `plan.md`'s one-quarter rule.
- That read rests on a single signal, S1, at tier 3, on one posting whose band is a word ("Enterprise") and not a figure. S1's own bias: postings lag spend and over-represent large firms; headcount budget is not category spend.
- Eight cells read `blank`, not `none`: the sources naming this vertical omit the buyer band, and S3, S9 and two thirds of S10 were never reached. `demand-signals.md`: a blank is never written as `none`.
- The credit-card sub-vertical returned zero marketing postings across nine LinkedIn queries, and four supplement filers zero EDGAR hits — an absence on the channels named, not proven silence. Publication bias runs one way: quiet spending leaves no public trace, so `blank` and `none` are weaker evidence than `spend`.
- No read rests on a vendor target-customer page: the S11 sweep's `primeaxiom.ai/geo/geo-for-insurance` and `viewership.ai/industries/insurance` hits are sell-side claims, excluded. A list price is not a price paid; Simply Business's $114,700–$189,200 is compensation, not a price paid.

### Pass 8 re-run, 2026-09-23

Task P8-r. Runs S2, S3, S9, S10 across all nine cells (previously unchecked or partial per `plan-review-2-2026-09-23.md` §5), and bands every S1/S2/S7/S8 name found without one 2026-09-22. Raw: `raw/f-signal-hr-band-attribution-2026-09-23.md` (headcount); `raw/f-signal-hr-S2-paid-agentic-check-2026-09-23.md` (S2 paid/agentic); `raw/a-funding-crunchbase-pitchbook-repull-2026-09-23.md` (S3, R-BLOCKED); `raw/f-google-trends-S9-repull-2026-09-23.md` (S9, R-BLOCKED); `raw/f-procurement-S10-repull-2026-09-23.md` (S10, R-BLOCKED).

**Bands resolved (S1, S2, S7, S8 names), headcount, tier 5 (aggregator/LinkedIn, hidden method):** GEICO 26,142 (Enterprise); Amica 3,132–3,524 (Enterprise); Embrace Pet Insurance 201–202 (**Mid-market**); Insurify 166–242 (**Mid-market**); The Juice Plus+ Company 3,875 (Enterprise); Simply Business 850–851 (**Mid-market**); Jerry.ai 392–394 (Mid-market); Zurich Insurance UK ~5,000 (Enterprise); The Hartford 18,100–27,220 (Enterprise, three sources, not averaged); Aetna ~40,000–41,000 (Enterprise); MidFirst Bank 1,640–3,300 (Enterprise, four sources, not averaged); Primerica 45,392 total / 2,800+ corporate (Enterprise either way); NerdWallet 735 (Mid-market); Mutual of Omaha 6,000–9,500 (Enterprise); Franklin Templeton 9,800–12,000 (Enterprise); John Lewis Financial Services — `unknown — checked LinkedIn, Wikipedia, Statista, Revelio Labs, ZoomInfo 2026-09-23` for the unit itself; parent John Lewis Partnership ~74,000 found but not applied to the cell (division ≠ company; `unassigned` stands, per boundary rule, moves no cell).

**S2 paid and agentic, all nine cells:** `none — checked` — Google Direct Offers pilot names Petco, e.l.f. Cosmetics, Samsonite, Rugs USA, Shopify merchants; ChatGPT/Google AI Mode agentic-checkout rosters name Wayfair, Chewy, Etsy; Perplexity Instant Buy names no roster. No insurance, card or supplement name in any roster — `raw/f-signal-hr-S2-paid-agentic-check-2026-09-23.md`.

**S3, all nine cells:** checked, `blank — unattributed` (vertical-level, moves no cell). Vendor funding found: AthenaHQ seed $2.1M (01-Apr-2025); Peec AI seed $8.08M (02-Jul-2025), Series A undated; Profound Series D $180M (15-Sep-2026) — all filed via PitchBook/Crunchbase free previews, tier 5. None ties to a high-CPA customer; these are organic-recommendation-tool vendors, not paid or agentic vendors.

**S9, all nine cells:** checked, `blank — unattributed` (vertical-level). Google Trends "AI visibility insurance", US, past 12 months: average index 7 (of 100, normalised against "generative engine optimization" 35 and "AI search optimization" 42 in the same comparison) — nonzero but not decomposable by sub-market or buyer size.

**S10, all nine cells:** mixed. SAM.gov exact-phrase, active records: "No matches found" — checked, zero. UK Contracts Finder: "We've found 667 notices" but the keyword URL parameter is not applied by the page — exhausted, untrusted, not a clean zero. TED: "Human Verification" wall — **blocked**, `blocked-channels.md` row stands, not exhausted.

**Cell reads, updated:**

| Cell | Change | New read | Deciding signal |
|---|---|---|---|
| Organic / Mid-market | blank → **spend** | **spend** | S1 — Embrace Pet Insurance (201 emp., "Organic Search / SEO Manager"), Insurify (166–242 emp., "AI Search & Discovery (GEO/AEO)"), Simply Business (850 emp., "SEO & GEO"); tier 3, all Mid-market by headcount |
| Organic / Enterprise | spend (reinforced) | spend | GEICO, Amica, Juice Plus+ now band Enterprise (S1); Zurich UK, Hartford, Aetna, MidFirst Bank band Enterprise (S2); Primerica, Mutual of Omaha, Franklin Templeton band Enterprise (S7/S8) |
| Organic / SMB | blank → **none — checked** (loose) / blank (strict) | none (loose) / blank (strict) | No S1/S2/S7/S8 name bands SMB; S3, S9 checked-unattributed; S10 blocked (TED) |
| Paid / SMB, Mid, Enterprise (×3) | blank → **none — checked** (loose) / blank (strict) | none (loose) / blank (strict) | S2 checked-none (Direct Offers roster); S3, S9 checked-unattributed; S10 blocked (TED) |
| Agentic / SMB, Mid, Enterprise (×3) | blank → **none — checked** (loose) / blank (strict) | none (loose) / blank (strict) | S2 checked-none (agentic-checkout rosters); S8 John Lewis Financial Services stays `unassigned` (division, no independent band); S3, S9 checked-unattributed; S10 blocked (TED) |

**Tally, both readings — 9 cells:** loose: spend 2, attention 0, none 7, blank 0 (9 of 9 closed). Strict (TED still blocked counts as unchecked): spend 2, attention 0, none 0, blank 7 (2 of 9 closed). Of the original 8 blanks: 1 closes to spend under the strict reading (Organic/Mid); all 8 close under the loose reading (7 to none, 1 to spend).

**Caveats, this append:** The Mid-market band for Embrace Pet Insurance, Insurify and Simply Business rests on third-party workforce aggregators (Revelio Labs, LeadIQ, Tracxn, GetLatka) whose headcount method is not published on the page — tier 5, hidden method, per `trust-rubric.md`. Sources disagree by tens of employees per company; ranges are recorded, not averaged. John Lewis Financial Services is deliberately left `unassigned` rather than banded to its parent's ~74,000 headcount: a division is not the company, and the boundary rule's proxy order (filing, careers page, network profile) named none for the division itself — accepting the parent would flip Agentic/Enterprise from `none` to `attention`, and is recorded here as a live possibility, not applied. The strict-reading blank on six cells rests entirely on one channel, TED's human-verification wall; UK Contracts Finder's non-functional keyword filter is the second-weakest link (667 unfiltered notices, not inspected for relevance).

File now 128 lines against the 100-line `customer-segment.md` budget; overrun is this append, kept whole rather than cut to fit.

### R-BLOCKED-2, 2026-09-23

Re-probe of the channels behind this file's strict-reading blanks. Raw: `raw/f-ted-S10-repull2-2026-09-23.md` (TED, tier 2); `raw/f-indeed-S1-repull2-2026-09-23.md` (Indeed, tier 3, logged-in US); `raw/b-reddit-advertiser-reports-repull2-2026-09-23.md` and `raw/f-reddit-S5-counts-repull2-2026-09-23.md` (Reddit archive, tier 5).

**S10, TED — reached.** Brief terms: "generative engine optimization" 14 notices, 5 procedures; a sixth, An Post, under "optimisation"; "AI visibility", "answer engine optimization", "AI search optimisation", "large language model visibility" 0 each. Paid/agentic terms: "ChatGPT Ads", "sponsored answers", "agentic checkout" 0; "agentic commerce" 1 (tourism website). One buyer in this vertical:

| Buyer | Band, source | Notice | Scope naming GEO | Value | Cell |
|---|---|---|---|---|---|
| KKH Kaufmännische Krankenkasse (statutory health insurer) | Enterprise — "rund 4.000 Menschen beschäftigt", kkh.de | 66176-2026 call; 522860-2026, 533563-2026 results | GEO one of ~18 marketing-agency themes | framework max 11,000,000.00 EUR; winner, award value not published | Organic / Enterprise |

NRW.BANK (development bank) and KfW Bankengruppe also named GEO or Perplexity; lending sits outside this vertical's definition — recorded, unassigned.

**S1, Indeed — partial, then walled.** 2 of 36 queries completed before "Too Many Requests" and "Additional Verification Required"; no vertical-term query ran. Names from this vertical among 35 cards: The Cigna Group (already Enterprise); Safe Life US LLC, GESA Credit Union, CAL Financial — posting bodies unread, band and sub-vertical `unassigned`, no cell moves.

**S11 / S5, Reddit.** A "premium DTC supplement brand" in Spain reports ChatGPT Ads spend "€37.61", "0 conversions" (RB2, `findings/ai-ads-evidence.md`). Supplements, paid placement, buyer size unstated → `unassigned`, moves no cell; recorded beside the Paid `none` reads, not merged. S5 counts are subreddit-level, no vertical attribution.

**Cell reads, both readings:**

| Cell | Before (strict / loose) | Now (strict / loose) | Deciding change |
|---|---|---|---|
| Organic / SMB | blank / none | **none — checked** / none | TED reached, no SMB buyer in vertical |
| Organic / Mid-market | spend / spend | spend / spend | unchanged |
| Organic / Enterprise | spend / spend | spend / spend, reinforced | S10 KKH, tier 2 filed |
| Paid / SMB, Mid, Enterprise | blank / none (×3) | **none — checked** / none (×3) | TED 0 on paid terms; RB2 unassigned beside |
| Agentic / SMB, Mid, Enterprise | blank / none (×3) | **none — checked** / none (×3) | TED 0 on agentic terms in vertical |

**Tally, 9 cells.** Strict: spend 2, attention 0, none 7, blank 0. Loose: unchanged, spend 2, none 7.

**Still blank or thin, with reason.** No cell blank. Indeed vertical queries: unrun, wall. UK Contracts Finder keyword filter: untrusted zero, unchanged. John Lewis Financial Services: `unassigned`, unchanged.

**Caveats.** KKH is a public-law statutory insurer; counting it as "insurance" follows the vertical definition's wording, not a separate check. The 11,000,000.00 EUR is the whole agency framework ceiling, not GEO spend. TED covers EU public buyers only; the strict `none` reads rest on TED plus the earlier channels, and publication bias still runs one way. Indeed names are card fields only.

## Budget line, P16-c1, 2026-09-23

Which existing line funds AI-visibility or AI-ads spend for an insurance, credit-card or supplement buyer. Raw prefix `raw/`, suffix `-2026-09-23.md` unless stated.

| Evidence | What it states | Line named | Tier | Raw |
|---|---|---|---|---|
| eHealth (Medicare and health-insurance marketplace), 10-K FY2025; 10-Q Q2 2026 | "our ability to reach consumers through established search‑engine optimization, paid search, and other digital marketing channels may be adversely impacted"; "Increased reliance on alternative marketing channels could further increase our marketing expenditures" | SEO and paid search named as the lines at risk; no reallocation, no dollar | 2 | `f-signal-hr-S7-ehealth-10k-2025`; `f-signal-hr-S7-ehealth-10q-q2-2026` |
| EDGAR FTS, "AI search", eight insurers and lead-gen filers, 2026 | 0 hits; broader phrase query returns eHealth only | none | 2 | `f-edgar-fts-budget-line-queries` |
| LegalZoom, 10-Q Q2 2026 — adjacent, legal is outside this segment's definition | "a reduction in organic traffic and a higher emphasis on paid search"; "expanding beyond traditional search through strategic partnerships ... including with AI platforms"; "we are investing accordingly" | organic → paid search; AI-platform partnerships funded, line unnamed | 2 | `f-signal-hr-S7-legalzoom-10q-q2-2026` |
| Gartner CMO Spend Survey 2026; HubSpot State of Marketing 2026 | `unknown — paid`; gated | — | —; 6 | `e-gartner-ad-platforms-prediction-2028`; `f-hubspot-state-of-marketing-2026-check` |

**Read.** `unknown — checked EDGAR FTS (10 CIKs plus phrase queries), eHealth 10-K and 10-Q, gartner.com, hubspot.com 2026-09-23; search engines walled` (`f-search-engines-wall-log`). No filer names the line that funds AI-surface work.
## Engine × segment and buying process, P16-c4, 2026-09-23
**Engines named, this vertical's raw.** Mentions and files-with-mention across the 22 high-CPA raw files (`f-signal-hr-*`, `f-signal-census-hr-*`, `e-case-census-c10-*`, `e-case-c10-*`, `e-case-aicited-*`, `e-case-fireandspark-*`), regex count, method in `raw/f-engine-mentions-raw-count-2026-09-23.md` (measured-by-us on raw already pulled). Partial by design.

| Engine | Mentions | Files | Cell-attributable naming, source, tier |
|---|---|---|---|
| ChatGPT | 49 | 10 | Juice Plus+ S1 posting: "how Juice Plus+ appears across Google Search, AI Overviews, ChatGPT, Gemini, Perplexity, and emerging answer engines" — Organic / Enterprise (band per `raw/f-signal-hr-band-attribution-2026-09-23.md`), 3, `raw/f-signal-hr-S1-linkedin-2026-09-22.md` |
| Gemini / AI Mode / AI Overviews | 35 | 7 | Juice Plus+ posting (AI Overviews, Gemini); NerdWallet 8-K "AI overviews and LLMs" — Organic / Enterprise, negative direction, 2, `raw/e-nerdwallet-8k-repull-2026-09-23.md` |
| Perplexity | 15 | 6 | Juice Plus+ posting |
| Claude | 7 | 3 | vendor and case files only |
| Grok | 2 | 2 | vendor and case files only |
| Copilot | 0 | 0 | — |
| Rufus / Alexa for Shopping | 0 | 0 | — |

Cell-level naming exists only at Organic / Enterprise (Juice Plus+, supplements; NerdWallet, cards). The Cigna, GEICO, Amica, Embrace, Insurify and Simply Business postings name GEO/AEO duties without an engine in the text captured (`raw/f-signal-hr-S1-*`; `raw/f-indeed-S1-repull2-2026-09-23.md` card only). Mid-market cell: `unknown — checked the three banded postings 2026-09-23`. Paid and agentic rosters name no insurance, card or supplement brand (`raw/f-signal-hr-S2-paid-agentic-check-2026-09-23.md`).

**Switching cost and buying process.** Buyer-side: `unknown — checked every raw file cited in this document, OMR (0 lines naming a buying step), G2 review text (403 to fetch), TED, sam.gov, Contracts Finder 2026-09-23`. The one public-buyer procurement near this vertical, KKH's EUR 11,000,000 marketing framework naming GEO (`raw/f-ted-S10-repull2-2026-09-23.md`, tier 2), states a framework ceiling and a tender path, not a vendor contract length. Vendor-side terms, tier 3, `raw/a-vendor-terms-contract-length-2026-09-23.md`: monthly cancel-anytime self-serve at Peec, Otterly, AthenaHQ, Local Falcon, BrightLocal; annual auto-renewal at Otterly and Semrush (Semrush non-cancellable, 7-day refund on 12-month-or-longer terms only); enterprise order forms of undisclosed length at Profound, Scrunch, AthenaHQ, SOCi; Yext "annual and multi-year subscriptions", "non-cancelable contracts" (10-K, tier 2). Regulated-buyer reviewer presence: Profound G2 industry "Financial Services (76)" of 1,129, AthenaHQ "Financial Services (3)" of 47, Brandlight "Financial Services (7)" of 216 (`raw/f-g2-capterra-S4-repull-2026-09-23.md`, tier 5). Board-level pull, not vertical-cut: Corporate Ink survey via Yext 8-K, 88% / 34%, tier 5 relay, no n (`raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md`).

**Caveats, this append.** Word counts over raw include headers and query strings; this vertical's raw set is the smallest of the three, so counts are not comparable across verticals in absolute terms. One posting carries every cell-level engine naming. Vendor terms are asking terms; no regulated buyer's contract is on record.
## S13 brand accuracy and EU cells, P16-c3, 2026-09-23
S13 per `method/demand-signals.md` addition 2026-09-23. Raw prefix `raw/`, suffix `-2026-09-23.md`.

| Sub-market | Size | S13 | Channels checked 2026-09-23 |
|---|---|---|---|
| Organic | SMB, Mid-market, Enterprise | none — checked | LinkedIn guest API (3 terms); Arctic Shift r/smallbusiness, r/SEO, r/marketing (r/bigseo 422); CourtListener; TED, UK CF; vendor sitemaps; SEJ; engine help ×5 |
| Paid | all three | none — checked | same; no insurance, card or supplement brand named |
| Agentic commerce | all three | none — checked | same |

Nearest S13 observation: LTL LED, LLC (Wolf River Electric) v. Google LLC, D. Minn. 0:25-cv-02394, "320 Assault Libel & Slander", filed 2025-06-09, terminated 2026-02-26 — solar installer, outside this vertical (`f-courtlistener-ltl-led-v-google-ai-overview-defamation`, tier 2, moves no cell).

EU cells — organic sub-market only; paid and agentic not checked with EU terms, blank:

| Country | Size | S1 | Read | Raw, tier |
|---|---|---|---|---|
| UK | unassigned | Compare the Market "Senior Manager - Search & LLM Discovery", Peterborough, 2026-09-08, 26 applicants: "LLM Discovery & Optimisation Lead", "generative AI discovery" — insurance comparison per employer, vertical not stated in posting; headcount `unknown — checked comparethemarket.com (403) 2026-09-23` | moves no cell | `f-linkedin-S1-eu-countries`, 3 |
| UK | SMB, Mid-market, Enterprise | no other regulated employer of 30 cards | none — checked | same |
| FR | all three | Hello Watt "Responsable SEO et GEO" is energy brokerage — outside vertical; 0 insurance, card, supplement employers | none — checked | same |
| ES | all three | 0 of 30 cards | none — checked | same |
| IT | all three | 0 of 30 cards | none — checked | same |
| NL | all three | 0 of 30 cards | none — checked | same |

S2, S5, S10 per country as in the B2B SaaS append of the same date: Yext /fr and /it Scout pages, no customer; 0 national-sub threads (1 off-topic r/italy post); TED 0 notices outside DEU and IRL; UK CF 0. Raw: `f-vendor-S2-yext-scout-localized-fr-it` (3), `f-reddit-arcticshift-S5-eu-national-subs` (5), `f-ted-ukcf-S10-eu-country-brand-accuracy` (2).

**Caveats, this append.** Compare the Market's vertical is read from the employer's business, which the posting does not state; the boundary rule keeps it out of a cell. "Regulated" here follows the segment definition above (credit cards, insurance, supplements). Single pass, fetch-only, 2026-09-23.
## S1 posting bodies, P16-c4b, 2026-09-23
Indeed walled on the first posting page (Cloudflare "Additional Verification Required", 16:21); bodies read from employer career sites instead. Raw: `raw/f-indeed-S1-repull3-2026-09-23.md` (tier 3, company-stated). Format: employer · title · phrase in body · engines named · budget or tool named · salary · size band · raw section.

- The Cigna Group · "Lead Analyst, Technical Search (SEO/AEO/GEO)" · yes — "Answer Engine Optimization (AEO), and Generative Engine Optimization (GEO)"; "Enterprise AI Search Technical Roadmap" · none by brand ("AI-powered answer engines", "large language models"; "Claude Code" named as a development tool) · vendors: "AEO tools (e.g. Profound, Scrunch, Bluefish, Evertune, etc.)"; "SEO tools (e.g. BrightEdge, SEMrush, Conductor, etc.)"; no budget figure · "79,100 - 131,800 USD / yearly" plus annual bonus · Enterprise by the source's word only, unchanged (no headcount in body) · §posting #20
- GESA Credit Union · "Brand Content Strategist" · unread — Indeed wall; Paycom listing has no match · — · — · card "$29.90 - $60.25 an hour" · `unassigned` · §Checked, not found
- Safe Life US LLC, CAL Financial, Inc., Ann & Robert H. Lurie Children's Hospital · unread — Indeed wall; employer sites not attempted · — · — · cards: none, "$40 - $60 an hour", "$70,720.00 - $115,627.20 a year" · `unassigned` · superseded file

Cell check. Organic / Enterprise **spend** rests on the LinkedIn pull of the same Cigna posting (`raw/f-signal-hr-S1-linkedin-2026-09-22.md`), not on the Indeed card; the employer-site body **confirms** the duty and adds the first buyer-side naming of AEO vendors in this vertical (Profound, Scrunch, Bluefish, Evertune — "e.g.", tools the candidate should know, not a purchase). Posted 2026-09-14 (Workday startDate), six US locations.
## EU paid and agentic cells, P16-c3b, 2026-09-23
Closes the paid and agentic EU cells P16-c3 left blank. Raw prefix `raw/`, suffix `-2026-09-23.md`. Channels as in the skincare append of the same date.

| Country | Sub-market | Size | S1 | S2 | S5 | S10 | Read |
|---|---|---|---|---|---|---|---|
| UK | Paid | all three | 0 regulated employers of 6 pages | BestMoney "3.88% across the UK and US" — see unassigned row | 0 threads, 4 queries | TED 0, UK CF 0; FCA "Agentic AI" award is buyer-side IT | none — checked |
| UK | Agentic | all three | 0 regulated employers | none | query 422 ×2 | UK CF "agentic commerce" 0 | none — checked (S5 failed) |
| FR | Paid | all three | Havea/Biocyte (supplements) intern: ChatGPT as creative tool, Meta/TikTok ads — nil | OpenAI posts name no advertiser | 0 threads | TED 0 | none — checked |
| FR | Agentic | **Mid-market** | Alan "Product Lead - Growth", 2026-09-22: "a GPT app where a prospect can shop for and buy health insurance, and agentic commerce more broadly"; "The team is 800+ people" | none | 0 threads | TED 0 | **spend** |
| FR | Agentic | SMB, Enterprise | no other insurer, card or supplement employer | none | 0 threads | TED 0 | none — checked |
| ES | Paid | all three | 0 of 8 pages; Tecnoempleo 0 | none | both queries 422 ×2 | TED 0 | none — checked (S5 failed) |
| ES | Agentic | all three | 0 regulated employers | none | 0 threads | TED 0 | none — checked |
| IT | Paid | all three | 0 of 8 pages | none | 0 threads | TED 0 | none — checked |
| IT | Agentic | all three | 0 of 8 pages | none | 0 threads | TED 0 | none — checked |
| NL | Paid | all three | 0 regulated employers of 9 pages | OpenAI nl-NL names no advertiser | 0 threads, 2 queries | TED 0 | none — checked |
| NL | Agentic | all three | 0 regulated employers | Adyen names no insurer | query 422 ×2 | TED 0 | none — checked (S5 failed) |

Alan cell: vertical stated in the posting (health insurance); size from alan.com/en/careers "800+ people" → mid-market per `method/demand-signals.md` bands; S1 spend class, tier 3 (`f-jobboards-S1-eu-paid-agentic`). The posting is a product role naming the surface, not a media or checkout buy.

Unassigned, UK × Paid: BestMoney "3.88% across the UK and US", Adthena index week 2026-07-13 to 07-20 — "financial comparison" per the source, not an issuer or insurer; size unknown; moves no cell (`b-ppcland-adthena-7378-advertisers`, 5). Outside vertical, EU paid, for the record: Volkswagen and Vodafone "testing ChatGPT Ads" via Adform, release 2026-09-10, country entity unstated (`f-vendor-S2-eu-paid-agentic`, 3); giffgaff 14.0%, Vodafone 11.3% top UK ChatGPT advertisers (`b-ppcland-adthena-7378-advertisers`, 5).

Raw: `f-linkedin-S1-eu-paid-agentic` (3), `f-jobboards-S1-eu-paid-agentic` (3), `f-vendor-S2-eu-paid-agentic` (3), `f-adthena-S2-eu-paid-agentic` (5), `f-reddit-arcticshift-S5-eu-paid-agentic` (5), `f-ted-ukcf-S10-eu-paid-agentic` (2).

**Caveats, this append.** The one spend read rests on a single posting (S1 alone — flagged per `demand-signals.md`) whose "agentic commerce" wording is aspirational product scope, not a checkout programme joined. "(S5 failed)" cells rest on S1, S2, S10 only.
## Image reads, IMG-1c, 2026-09-23
No insurer, lender, card issuer, legal or health advertiser in Adthena's UK leaderboard images (ChatGPT Ad Index, week of 2026-07-13 to 07-20; tier 5, vendor index, vendor-reported). Full UK-tagged list as printed — all-markets table: Booking.com 13.81%, Almedia USA, Inc. 12.76%, efaq.com 4.55%, Expert Market 4.38%, giffgaff 4.28% (UK only); UK card: giffgaff 14.0%, Vodafone 11.3%, Booking.com 9.0%. The images print no vertical for any advertiser. Side by side with the unassigned row above: BestMoney appears only in the US card (rank 3, 6.1%), not in the UK card or the visible all-markets rows; "3.88% across the UK and US" rests on the trade relay (`b-ppcland-adthena-7378-advertisers`, 5) alone. giffgaff 14.0% and Vodafone 11.3% (telecom, outside vertical) match the relay figures. UK × Paid cells unchanged: none — checked. Class per `method/demand-signals.md` S2 rules for any advertiser named by a vendor index: attention (vendor-reported, not a budget). Raw: `raw/f-adthena-S2-eu-paid-agentic-2026-09-23-img-2026-09-23.md`.
