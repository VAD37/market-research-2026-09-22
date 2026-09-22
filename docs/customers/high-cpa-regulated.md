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
