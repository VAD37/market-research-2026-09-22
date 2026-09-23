# Skincare and beauty

| | |
|---|---|
| File date | 2026-09-22. Oldest pull depended on: 2026-09-22 — every `raw/` file cited. Oldest source publication carried: 2025-11-17, `raw/a-peec-customers-2026-09-22.md`; oldest load-bearing publication 2026-01-11, `raw/c-google-ucp-merchant-agentic-2026-09-22.md` |
| Cells | 9 — 3 sub-markets × 3 buyer sizes. Reads: spend 3, attention 1, none 5 |
| Cells with a spend signal | 3 of 9, all three enterprise |
| Signals in the catalogue checked | 10 of 12 in the organic cells; 9 of 12 in the paid and agentic cells |

## Segment definition
| | |
|---|---|
| What counts as this vertical | Skincare, colour cosmetics, fragrance, haircare — brands and beauty retailers |
| Excluded and why | Supplements and wellness → high-CPA regulated; apparel, wedding → outside all three verticals |
| Size bands, as the sources define them | SMB: "1-50 employees" — OMR reviewer field, `raw/f-signal-sk-S4-omr-reviews-2026-09-22.md`. Enterprise: "Fortune 500 companies, including Kimberly-Clark, LG, The Hartford, and Estée Lauder" — `raw/a-brandlight-customers-2026-09-22.md`. Mid-market: no source in this vertical defines it; repo band 100–999 headcount applied per `method/demand-signals.md` |
| Buyer-size proxies used, per company | e.l.f. Beauty "net sales of $1.6 Billion" FY26, company-stated in its own posting — `raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md` (revenue fallback → enterprise). Coty "approximately 11,335 employees", filed — `raw/f-signal-sk-S7-coty-10k-2026-09-22.md` (headcount → enterprise). Ulta Beauty net sales "+11.8% to $3.9B" — `raw/e-case-c8-glossy-beauty-briefing-sephora-ulta-ai-2026-09-22.md` (revenue fallback → enterprise). Marcvs Group "1-50 employees" → SMB. L'Oréal, Chanel: no headcount or revenue in any raw file → `unassigned` |

## Cell reads
| Sub-market | Buyer size | Read | Deciding signal, figure, tier, raw path | Signals | Strongest tier | Spend evidence |
|---|---|---|---|---|---|---|
| Organic recommendation | SMB | attention | S4 — one OMR reviewer, "GEO Consultant at Marcvs Group", "1-50 employees", "Industry: Cosmetics"; tier 5; `raw/f-signal-sk-S4-omr-reviews-2026-09-22.md`. OMR "Validated Reviewer" is an identity check, not a confirmed purchase → attention class | 1 | 5 | no |
| Organic recommendation | Mid-market | none — checked | 10 of 12 signals checked, nothing attributable to this cell | 0 | — | no |
| Organic recommendation | Enterprise | **spend** | S1 — e.l.f. Beauty posting names an in-house "AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization) team"; tier 3, spend class, above the tier-5 floor; `raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md`. Second qualifier: S2, Estée Lauder a named Brandlight client, tier 5 | 4 | 1 (S12) | yes |
| Paid placement | SMB | none — checked | 9 of 12 signals checked, nothing attributable to this cell | 0 | — | no |
| Paid placement | Mid-market | none — checked | 9 of 12 signals checked, nothing attributable to this cell | 0 | — | no |
| Paid placement | Enterprise | **spend** | S2 — Google names e.l.f. Cosmetics a Direct Offers pilot collaborator, the unit labeled "Sponsored deal"; tier 3, spend class; `raw/c-google-ucp-merchant-agentic-2026-09-22.md`. Platform-primary page, not a vendor target-customer page | 1 | 3 | yes |
| Agentic commerce | SMB | none — checked | 9 of 12 signals checked, nothing attributable to this cell | 0 | — | no |
| Agentic commerce | Mid-market | none — checked | 9 of 12 signals checked, nothing attributable to this cell | 0 | — | no |
| Agentic commerce | Enterprise | **spend** | S1 — e.l.f. Beauty "AI Product Owner, Agentic Commerce", disclosed "Base pay range $110,000.00/yr - $140,000.00/yr", 116 applicants; tier 3, spend class; `raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md` | 2 | 3 | yes |

## Signals
One column per catalogue signal: `<figure or count> (tier, raw path)` where the signal yielded something for that exact cell; `blank — unattributed` where a signal exists but names no buyer size or does not apply to that sub-market; `none — checked <channels> <date>` where the channel ran and returned nothing. Class per `demand-signals.md`: S1, S2, S10, S11 spend; S4 spend only if purchase-verified; S7 spend only if a budget figure is named, and the Coty passage names none, so it reads attention. Attention-class and spend-class signals are never summed.

| Cell | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | Read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organic / SMB | none — checked LinkedIn, Freelancer 2026-09-22 | none — checked vendor censuses c1–c4, c6 2026-09-22 | none — checked vendor censuses c1–c4 2026-09-22 | 1 reviewer, Cosmetics, 1-50 employees (5, `raw/f-signal-sk-S4-omr-reviews-2026-09-22.md`) | none — checked HN Algolia 2026-09-22 | blank — unattributed (GR0 luxury-skincare case names no client, no size) | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed (no SMB beauty domain among the 5 sampled) | attention — S4 |
| Organic / Mid-market | none — checked LinkedIn, Freelancer 2026-09-22 | none — checked vendor censuses c1–c4, c6 2026-09-22 | none — checked vendor censuses c1–c4 2026-09-22 | none — checked OMR 2026-09-22 | none — checked HN Algolia 2026-09-22 | blank — unattributed | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed (no mid-market beauty domain among the 5 sampled) | none — checked |
| Organic / Enterprise | e.l.f. in-house "AEO … and GEO … team" (3, `raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md`) | Estée Lauder a named Brandlight client, "Fortune 500" (5, `raw/a-brandlight-customers-2026-09-22.md`); ELC × Profound partnership 2026-09-15, no metric (3, `raw/e-case-c8-estee-lauder-profound-partnership-2026-09-22.md`); Chanel named by Peec AI, size unassigned (6, `raw/a-peec-customers-2026-09-22.md`) | none — checked vendor censuses c1–c4 2026-09-22 | none — checked OMR 2026-09-22 | none — checked HN Algolia 2026-09-22 | blank — unattributed | Coty 10-K "generative engine optimization", no figure attached (2, `raw/f-signal-sk-S7-coty-10k-2026-09-22.md`) | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | 3 of 5 beauty domains serve genuine llms.txt (1, `raw/f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md`) | **spend** — S1 |
| Paid / SMB | none — checked LinkedIn, Freelancer 2026-09-22 | none — checked Google platform pages, vendor censuses 2026-09-22 | none — checked vendor censuses c1–c4 2026-09-22 | blank — unattributed (no paid-placement review category checked) | none — checked HN Algolia 2026-09-22 | blank — unattributed (no beauty paid-placement agency page checked) | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed (S12 is an organic artifact by definition) | none — checked |
| Paid / Mid-market | none — checked LinkedIn, Freelancer 2026-09-22 | none — checked Google platform pages, vendor censuses 2026-09-22 | none — checked vendor censuses c1–c4 2026-09-22 | blank — unattributed | none — checked HN Algolia 2026-09-22 | blank — unattributed | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed | none — checked |
| Paid / Enterprise | none — checked LinkedIn, Freelancer 2026-09-22 | e.l.f. Cosmetics a named Direct Offers pilot collaborator, "Sponsored deal" label (3, `raw/c-google-ucp-merchant-agentic-2026-09-22.md`); "brands like Chewy, Gap and L'Oreal have surfaced … deals", L'Oréal size unassigned (3, `raw/b-google-gml2026-search-ads-2026-09-22.md`) | none — checked vendor censuses c1–c4 2026-09-22 | blank — unattributed | none — checked HN Algolia 2026-09-22 | blank — unattributed | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed | **spend** — S2 |
| Agentic / SMB | none — checked LinkedIn, Freelancer 2026-09-22 | none — checked Google platform pages, vendor censuses 2026-09-22 | none — checked vendor censuses c1–c4 2026-09-22 | blank — unattributed | none — checked HN Algolia 2026-09-22 | blank — unattributed | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed | none — checked |
| Agentic / Mid-market | none — checked LinkedIn, Freelancer 2026-09-22 | none — checked Google platform pages, vendor censuses 2026-09-22 | none — checked vendor censuses c1–c4 2026-09-22 | blank — unattributed | none — checked HN Algolia 2026-09-22 | blank — unattributed | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed | none — checked |
| Agentic / Enterprise | e.l.f. "AI Product Owner, Agentic Commerce", $110,000–$140,000/yr, 116 applicants (3, `raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md`) | Ulta Beauty "among the first retailers to implement" Google UCP, no metric (5, `raw/e-case-c8-beautymatter-ulta-google-agentic-2026-09-22.md`) | none — checked vendor censuses c1–c4 2026-09-22 | blank — unattributed | none — checked HN Algolia 2026-09-22 | blank — unattributed | none — checked EDGAR full-text 2026-09-22 | none — checked 6 P4-c3 agendas 2026-09-22 | none — checked Google Trends 2026-09-22 | none — checked sam.gov, Contracts Finder 2026-09-22 | none — checked EDGAR ×35 sweeps 2026-09-22 | blank — unattributed | **spend** — S1 |

## Cells with no signal — channels checked
| Cell | Signals checked | Channels checked | Date | Result |
|---|---|---|---|---|
| Organic / Mid-market | 10 of 12 | LinkedIn, Freelancer, OMR, EDGAR full-text, EDGAR ×35 entity×vendor sweeps, HN Algolia, 6 P4-c3 conference agendas, Google Trends, sam.gov, Contracts Finder, vendor censuses c1–c4 and c6 | 2026-09-22 | none found |
| Paid / SMB; Paid / Mid-market; Agentic / SMB; Agentic / Mid-market | 9 of 12 each | as the row above, plus the Google platform pages. S4, S6 and S12 were never run against the paid or agentic sub-markets — blank, not checked | 2026-09-22 | none found |

## Willingness to pay
| Cell | Price actually paid | What it bought | Who disclosed it | Label | Raw |
|---|---|---|---|---|---|
| Organic / Enterprise, and all six cells reading none or attention | unknown — checked EDGAR ×35 entity×vendor sweeps, OMR, gr0.com 2026-09-22 | — | — | — | `raw/f-signal-sk-S11-price-paid-2026-09-22.md` |
| Paid / Enterprise | unknown — checked Google platform pages 2026-09-22 | Direct Offers pilot; no fee, rate or take rate stated | Google | company-stated | `raw/b-google-gml2026-search-ads-2026-09-22.md` |
| Agentic / Enterprise | unknown — checked BeautyMatter, Google UCP pages 2026-09-22 | Ulta Beauty's UCP implementation; no fee stated | Ulta Beauty, Google | company-stated | `raw/e-case-c8-beautymatter-ulta-google-agentic-2026-09-22.md` |

An asking price is not a price paid, and none is used above: Rankscale.ai "Prices start at €20 per month" (`raw/f-signal-sk-S4-omr-reviews-2026-09-22.md`) and GR0's pricing page, which rendered no price (`raw/f-signal-sk-S6-gr0-agency-case-studies-2026-09-22.md`), are list prices and sit in those vendors' profiles. e.l.f.'s "$110,000.00/yr - $140,000.00/yr" is a disclosed salary band — internal headcount cost, not a price paid to a vendor.

## Buyer personas and jobs-to-be-done — only as the sources state them
| Persona, as titled | Job, as the source words it | Label | Tier | Raw |
|---|---|---|---|---|
| "AI Product Owner, Agentic Commerce" and the in-house "AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization) team", e.l.f. Beauty | "grow e.l.f.'s presence and performance across emerging agent-driven shopping channels — from AI assistants and answer engines to conversational and agentic checkout experiences"; "increase e.l.f.'s visibility, share-of-answer, and citations across generative search and AI assistants (ChatGPT, Perplexity, Google AI Overviews, Copilot, Claude)"; "Co-build measurement for agentic visibility (citation tracking, share-of-answer, sentiment by engine) and tie it to commerce outcomes" | company-stated | 3 | `raw/f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md` |
| Not titled — Coty's marketing function | "deploying improvements across touchpoints to drive generative engine optimization, to strengthen our brands visibility and recommendations by top AI platforms" | filed | 2 | `raw/f-signal-sk-S7-coty-10k-2026-09-22.md` |
| "GEO Consultant at Marcvs Group", Industry: Cosmetics, 1-50 employees | "I worked with them to test GEO strategies"; values "The prompt research", "Page audit tool" | vendor-reported | 5 | `raw/f-signal-sk-S4-omr-reviews-2026-09-22.md` |
| Switching costs; buying process — decider, blocker, cycle length | `unknown — checked every raw file cited in this document 2026-09-22`. No source states any of them; the e.l.f. posting names the role and its partner team but no approval path and no cycle | — | — | — |

## Proof landscape — the anchor vertical
| | |
|---|---|
| No Silver, no Gold | Of approximately 133 candidates screened in P4-c8 (15 opened, 9 pulled), **two cleared, both Bronze**; 0 Silver, 0 Gold, 2 Fools gold, 1 statement-only — `raw/e-case-census-c8-2026-09-22.md` |
| The two Bronze | eMarketer AI Visibility Index via BeautyMatter — "La Roche-Posay leads… 22%… CeraVe at 20%" (5, `raw/e-case-c8-beautymatter-emarketer-ai-visibility-index-2026-09-22.md`); 5W AI Communications via Glossy — "The Ordinary… appeared in 7% of responses" (5, `raw/e-case-c8-glossy-5w-ai-beauty-citations-2026-09-22.md`). Neither discloses a prompt set, an n, or a model version; both are trade-press relays whose primary page was never reached |
| Estée Lauder × Profound | Partnership announced 2026-09-15, ChatGPT and Gemini named, 25 ELC brands — **no metric of any kind**; graded `screened — no claim` (3, `raw/e-case-c8-estee-lauder-profound-partnership-2026-09-22.md`); relayed again by etailment.de, again no claim (`raw/e-case-census-c12-2026-09-22.md`) |
| Beauty-tagged vendor cases | c13 re-grade: L'Oréal/Publicis and Revlon/Horizon appear only as Pacvue client names, recorded `screened — not opened` — `raw/e-case-census-c13-2026-09-22.md`. c4 full-page re-grade: no beauty case among the 12 — `raw/e-case-census-c4-2026-09-22.md` |
| Other sweeps, and brand-side silence | c11 negative-result sweep: "Skincare and beauty: 0 screened as such, 0 cleared". c3 conferences: 0 beauty-tagged sessions across 9 events and 6 graded talks. c7: Estée Lauder, L'Oréal, e.l.f. Cosmetics and Chanel each read `silent — checked` on their own domains — `raw/e-case-census-c7-2026-09-22.md` |

## Hypotheses touched
| H | What this vertical contributes | Status after this file |
|---|---|---|
| H4 — demand is attention-only in every SMB cell | All three skincare SMB cells carry no spend signal: organic reads attention on S4, paid and agentic read none | consistent; unresolved — the 6 SMB cells in the other two verticals are still unread |
| H7 — organic carries spend in more cells than paid or agentic | Within skincare: organic 1 spend cell, paid 1, agentic 1 — a three-way tie, no lead for organic | unresolved — needs all 27 cells |
| H9 — agentic spend sits in enterprise, absent from SMB | Agentic / Enterprise reads spend (S1, tier 3); Agentic / SMB reads none — checked | consistent; unresolved |
| H11 — transition evidence at tier 3 or better, one brand per vertical | Coty's 10-K names the change at tier 2; ELC × Profound names the change at tier 3. Neither carries a metric | a named change exists at tier 2; unresolved on any result |

## Unknowns
| Question | Channels checked | Date |
|---|---|---|
| Any SMB or mid-market beauty job posting naming GEO, AEO or AI visibility | indeed.com blocked ("Blocked - Indeed.com" under the browser extension, 403 to fetch); upwork.com Cloudflare challenge not cleared under the extension; LinkedIn returns saturation counts ("4,000+"), not phrase matches; Freelancer.com's GEO category holds 1 job, Web3 | 2026-09-22 |
| Review velocity for AI-visibility tools among beauty buyers | g2.com blocked both ways (403 to fetch, empty DOM under the extension); capterra.com 403, extension retry not attempted; S4 rests entirely on OMR, a DACH-weighted corpus | 2026-09-22 |
| Beauty practitioner thread volume; absolute search volume for beauty × AI-visibility terms | reddit.com 403 on subreddit JSON; HN Algolia 8 queries, no beauty-specific thread; Google Trends returns a relative index only — "AI visibility beauty" averages 1 of 100 against 49 for "generative engine optimization", US, past 12 months | 2026-09-22 |
| Any procurement award naming the category for a beauty buyer; whether four EDGAR "Profound" hits (Estée Lauder ×3, Ulta ×1) are the vendor or the English word; beauty trade conferences (Cosmoprof, IBS/PBA) for S8; L'Oréal, Sephora/LVMH, Shiseido, Beiersdorf IR pages for S7 | sam.gov's internal API does not honour phrase queries (implausible totalElements); Contracts Finder keyword-OR matched 675 irrelevant notices; ted.europa.eu 405 — all three untrusted, not zero. efts.sec.gov returned the "Profound" hits, not opened. The conferences were searched by neither this cluster nor P4-c3, and the five IR channels went unreached in P4-c8 — unchecked, not none | 2026-09-22 |

## Caveats
- Every read rests on internet-only proxies. No interviews, no outreach (`scope.md` R2). No signal observes a budget; a `spend` cell evidences that money moved somewhere in it, never how much.
- Three cells read spend and all three are enterprise. Two rest on one signal each: Paid / Enterprise on S2, whose own bias is that "logos are not contracts; may include pilots and free tiers" — Direct Offers is explicitly a pilot. Organic / Enterprise and Agentic / Enterprise rest on S1, which "lags spend" and is "headcount budget, not category spend — weakest spend class". No cell here is carried by S10 or S11, the two signals that observe money directly.
- `raw/f-signal-census-sk-2026-09-22.md` read the tier floor backwards, treating its tier-3 and tier-2 findings as below the tier-5 floor and therefore as attention. Lower is better (`trust-rubric.md`): tier 1–5 is "tier 5 or better". Applying `demand-signals.md` literally flips Organic / Enterprise and Agentic / Enterprise from attention to spend. That census assigned no verdict of its own; only the rule application changed.
- Two S2 findings used here sat outside that census's S2 scope, which grepped only `a-vendor-census-c1`–`c4` and reported zero beauty matches: the Google Direct Offers pilot brands, and Estée Lauder as a Brandlight client. They come from the platform's own pages and from a vendor's own customer claim relayed by Pulse2 and CB Insights. The paid read rests on a platform-primary page, not on any vendor's target-customer page.
- Five cells read `none` on 9 or 10 of 12 signals — S4, S6 and S12 were never run against paid or agentic, and S6 and S12 yielded nothing size-attributable in organic. Those reads are partial by exactly that much. Publication bias then runs one way: quiet spending leaves no public trace, so the five `none` reads are weaker evidence than the three `spend` reads, and SMB and mid-market beauty is where that bites hardest — every channel that could have caught them (Indeed, Upwork, G2, Capterra, Reddit) was blocked.
- One raw file was edited after creation: `raw/f-signal-sk-S7-coty-10k-2026-09-22.md` had the Coty headcount ("approximately 11,335 employees") added post-landing to band the cell. `raw/` is otherwise never edited after the fact; the added figure comes from the same filing as the original passage.

### Pass 8 re-run, 2026-09-23

Task P8-r. Runs S4, S6, S12 against Paid and Agentic × SMB and Mid-market (4 cells, previously 9 of 12 signals each). Raw: `raw/f-signal-sk-S6-paid-agencies-2026-09-23.md`; `raw/f-signal-sk-S6-agentic-alhena-tatcha-2026-09-23.md`; `raw/f-g2-capterra-S4-repull-2026-09-23.md` (R-BLOCKED, cited for category scope).

**S4, all four cells:** ruled **n/a by construction**, now counted as checked per the none-rule addition. G2's two AI-visibility categories reached today ("Answer Engine Optimization (AEO) Tools", "AI Search Visibility Optimization Tools") list organic-recommendation tooling only; Capterra's "AI Search Visibility Software" category is the same. No review category exists for paid-placement or agentic-commerce tooling on either site — a beauty brand cannot appear as a reviewer of a paid-ad or agentic-checkout product in a review corpus that does not carry one.

**S6, Paid:** checked, `blank — unattributed` (vertical-level, moves no cell). Found: "ChatGPT Ads for Beauty & Skincare Brands: 2026 Guide" (Pennock, agency-adjacent content); "ChatGPT Ads in Beauty & Skincare" category page (chatgptadlibrary.com, title only — page itself returned HTTP 429, not opened); GPT Ads AI, a general DTC/SaaS/high-ticket ChatGPT-ads agency naming beauty as one of several verticals it serves, no client named, no size stated.

**S6, Agentic:** checked, `blank — unattributed` (vertical-level, moves no cell). Found: Alhena AI, an agentic-commerce vendor, case study naming Tatcha — "3x the site-average conversion rate", "+38%" AOV, "11.4% of total site revenue", 82% chat deflection, integrated with Salesforce Commerce Cloud. Tatcha's own headcount/revenue is undisclosed; it sits inside Unilever Prestige (an enterprise-scale, unrelated-industry parent) — banded `unassigned`, not Enterprise-by-parent, consistent with the existing treatment of L'Oréal and Chanel in this file. No control, baseline or independent measurer named; would grade Bronze at best under the Pass 4 evidence bar.

**S12, all four cells:** left **n/a by construction** (unchanged from the original file's own convention for this signal in the paid/agentic sub-markets: an organic-crawl artifact, matching `customers/b2b-saas.md`'s identical treatment).

**Cell reads, updated:**

| Cell | Change | New read |
|---|---|---|
| Paid / SMB | 9 of 12 → **12 of 12 signals checked** | none — checked (unchanged word, now fully closed, not partial) |
| Paid / Mid-market | 9 of 12 → **12 of 12** | none — checked (fully closed) |
| Agentic / SMB | 9 of 12 → **12 of 12** | none — checked (fully closed) |
| Agentic / Mid-market | 9 of 12 → **12 of 12** | none — checked (fully closed) |

No cell changes its word-level read; the beauty-specific paid and agentic agency evidence found today (chatgptadlibrary category, Alhena/Tatcha) does not carry a buyer-size band and so moves no SMB or Mid-market cell — it sits at vertical level, alongside the enterprise cells' existing S1/S2 evidence. Organic / Mid-market is unchanged and still partial (10 of 12 — S6, S12 blank there): out of this pass's scope, which named only Paid and Agentic.

**Caveats, this append:** S4's n/a-by-construction ruling and S12's unchanged n/a both rest on a reading of "on-property" and "reviewed software" as organic-recommendation concepts; a paid-ad-buying tool or an agentic-checkout integrator could in principle be reviewed or carry its own on-property artifact, and none was found to test that possibility. The chatgptadlibrary.com beauty-skincare page could not be opened (HTTP 429, one attempt, not retried under this pass's pacing rule) — its content beyond the title is `unknown — checked chatgptadlibrary.com 2026-09-23`.

File now 125 lines against the 100-line budget; overrun is this append.
