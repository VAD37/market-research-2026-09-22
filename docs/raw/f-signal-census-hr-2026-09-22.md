# P8-c1-hr census — demand-signal sweep, high-CPA regulated vertical (cards, insurance, supplements)

```yaml
source:          this agent's own discovery log and nine-cell signal matrix for task P8-c1-hr
url_or_doc_id:   n/a — compiled from the twelve raw pulls listed below
published:       2026-09-22
pull_date:       2026-09-22
pull_method:     fetch (direct curl throughout — SEC EDGAR full-text API, LinkedIn Jobs public search/view pages, HN Algolia API, OMR, sam.gov API, UK Contracts Finder OCDS API, TED, lite.duckduckgo.com/lite, and direct /llms.txt checks); no Chrome extension, no Playwright, per task scope
pull_purpose:    evidence about a number
tier:            n/a — this file is a census/index; every figure traces to the raw/ files it cites, each tiered on its own header
tier_reason:     n/a
source_label:    n/a
lane:            F, E
sub_market:      organic recommendation, paid placement, agentic commerce
engine:          n/a
metric_kind:     visibility, traffic, sales, none — mixed, see per-signal raw files
vertical:        high-CPA regulated (credit cards, insurance, supplements)
supersedes:      none
captured:        n/a — index file
```

No cell-read verdicts (spend / attention / none) are assigned here — per the task's own instruction, that one-word read is Pass 8's compile step, not this raw sweep. This file marks, per cell and per signal, whether a source-attributed observation was **checked** (with the figure/finding and tier), **blank — unattributed** (the vertical/signal was checked and something was found, but no source stated the buyer-size band needed to place it in one of the nine cells), or **none — checked \<channels\> \<date\>** (checked, nothing found at all). S2 and S3 are out of this cluster's scope (see Caveats) and are marked accordingly.

## Raw files landed by this cluster

| File | Signal(s) | What it found |
|---|---|---|
| `f-signal-hr-S1-linkedin-2026-09-22.md` | S1 | 21 LinkedIn queries; 6 qualifying postings (GEICO, Amica, Embrace Pet Insurance, Cigna, Insurify — insurance; Juice Plus+, Simply Business — supplements/insurance); zero qualifying for the credit-card sub-vertical; Cigna is the only posting stating its own buyer-size band ("Enterprise") |
| `f-signal-hr-S1-indeed-upwork-freelancer-2026-09-22.md` | S1 | Indeed 403, Upwork 403 (both confirmed blocked, browser backlog); Freelancer.com 200 but near-empty (1 of 1 entries), no vertical signal |
| `f-signal-hr-S4-review-sites-2026-09-22.md` | S4 | G2 403, Capterra 403 (browser backlog); OMR 200 but no dedicated GEO-vertical reviewer-industry breakdown found; one adjacent, non-qualifying vendor (LoyJoy) noted |
| `f-signal-hr-S5-community-2026-09-22.md` | S5 | Reddit 403 (confirmed unreachable); HN Algolia — 0 exact-phrase hits, all near-miss hits off-topic or vendor-side |
| `f-signal-hr-S6-agency-pages-2026-09-22.md` | S6 | 5 rostered agencies (Pass 3) — none names a finance/insurance/supplements client; fresh DDG-lite sweep — 2 results opened in full, both discarded (one generic, one a GEO/geographic-ambiguity false positive dated 2023, pre-dating the category) |
| `f-signal-hr-S7-primerica-10k-2026-09-22.md` | S7 | New finding: Primerica, Inc. 10-K (tier 2, filed) — EVP/Chief Reputation Officer's role explicitly includes "generative engine optimization"; no supplement or card-issuer filer found via EDGAR |
| `f-signal-hr-S7-p4c1-crossref-2026-09-22.md` | S7 | Cross-reference to `e-case-census-c1`: NerdWallet (Silver, vertical-tagged, credit-cards revenue -24% "due to continued headwinds in organic search traffic"); LendingTree and EverQuote (statement-only, vertical tag withheld by that file's own strict rule) |
| `f-signal-hr-S8-conferences-2026-09-22.md` | S8 | Cross-reference: GEO Conference NYC 2026 sponsor/attendee logos (NerdWallet, Mutual of Omaha, Franklin Templeton); MozCon London 2026 agentic-commerce session speaker from John Lewis Financial Services |
| `f-signal-hr-S9-search-interest-2026-09-22.md` | S9 | Method gap recorded: Google Trends requires browser rendering; this agent is fetch-only |
| `f-signal-hr-S10-procurement-2026-09-22.md` | S10 | sam.gov 200, no qualifying match (expected — public-sector only); UK Contracts Finder 200 but keyword filter non-functional as invoked; TED 405, blocked |
| `f-signal-hr-S11-price-paid-2026-09-22.md` | S11 | No disclosed price actually paid found; only list prices and sell-side vertical-landing pages |
| `f-signal-hr-S12-llmstxt-sample-2026-09-22.md` | S12 | Measured-by-us, 10 domains (3 cards, 4 insurance, 2 supplements, 1 excluded for a 500 error): 3 of 9 resolved domains (33%) served a real `/llms.txt` — bankrate.com, everquote.com, ritual.com |

## The nine-cell matrix

S2 (vendor customer counts/logos) and S3 (vendor funding/ARR) are **out of this cluster's scope** — both are vendor-side signals already routed through Pass 3's vendor census (`docs/raw/a-vendor-census-c1..c4-2026-09-22.md`, `a-vendor-roster-2026-09-22.md`) rather than this demand-side sweep; the task assigning this cluster explicitly enumerates S1, S4, S5, S6, S7, S8, S9, S10, S11, S12 and not S2/S3. Every cell below reads `out of scope — see Pass 3 vendor census` for S2 and S3.

S9 and S12 are **vertical-wide, not cell-specific**, per their own catalog framing (S9 is a method-access gap that applies uniformly; S12 is "share of sampled domains carrying the artifact," measured once across the vertical, not per buyer-size band) — both are recorded identically across all nine cells with a pointer to their own raw file.

| Sub-market | Buyer size | S1 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Organic recommendation | SMB | blank — unattributed (6 qualifying postings found, none states SMB) | none — checked g2.com/capterra.com (403→ext), omr.com (200, no match) 2026-09-22 | none — checked HN Algolia, reddit.com (403) 2026-09-22 | none — checked 5 rostered agencies + DDG-lite sweep 2026-09-22 | blank — unattributed (Primerica, NerdWallet, LendingTree, EverQuote found, none states SMB) | blank — unattributed (conference logos found, none states SMB) | unknown — browser-only, not checked (see S9 file) | unknown/none — see S10 file (sam.gov none; UK CF/TED unresolved) | none — checked, no price-paid disclosure found | n/a — vertical-level, 3 of 9 domains hit (see S12 file) |
| Organic recommendation | Mid-market | blank — unattributed | none (as above) | none (as above) | none (as above) | blank — unattributed | blank — unattributed | unknown | unknown/none | none | n/a (as above) |
| Organic recommendation | Enterprise | **checked — "Enterprise Technical Search Lead/Analyst (SEO/AEO/GEO)," The Cigna Group, tier 3, company-stated** (`f-signal-hr-S1-linkedin-2026-09-22.md`) | none (as above) | none (as above) | none (as above) | blank — unattributed (Primerica is NYSE-listed but headcount/revenue not extractable this pull; NerdWallet/LendingTree/EverQuote state no band) | blank — unattributed | unknown | unknown/none | none | n/a (as above) |
| Paid placement | SMB | none — checked "ChatGPT ads insurance," "AI advertising credit card" 2026-09-22, no qualifying paid-marketing role found | none | none | none | blank — unattributed (P4-c1 cases are all organic-search-framed, not paid) | none — checked six `f-conference-*` files, no paid-placement session found in this vertical | unknown | unknown/none | none | n/a |
| Paid placement | Mid-market | none (as above) | none | none | none | blank — unattributed | none (as above) | unknown | unknown/none | none | n/a |
| Paid placement | Enterprise | none (as above) | none | none | none | blank — unattributed | none (as above) | unknown | unknown/none | none | n/a |
| Agentic commerce | SMB | none — checked "agentic commerce insurance," "agentic checkout supplement" 2026-09-22, no qualifying role found | none | none | none | blank — unattributed (no P4-c1 case names agentic commerce) | blank — unattributed (MozCon session found, no SMB statement) | unknown | unknown/none | none | n/a |
| Agentic commerce | Mid-market | none (as above) | none | none | none | blank — unattributed | blank — unattributed | unknown | unknown/none | none | n/a |
| Agentic commerce | Enterprise | none (as above) | none | none | none | blank — unattributed | **blank — unattributed** ("How to Win at Agentic E-Commerce," John Lewis Financial Services, `f-signal-hr-S8-conferences-2026-09-22.md` — a large UK retailer's financial-services division, but no headcount/revenue stated in the captured text, so recorded unassigned rather than guessed to Enterprise) | unknown | unknown/none | none | n/a |

**Cells with at least one `checked` mark: 1 of 9** (organic recommendation / enterprise, via S1).

## Spend-class vs. attention-class tally

Per `demand-signals.md`'s classes: S1, S3, S7 (split), S10, S11 are spend-class in the catalog; S2, S4 (conditionally), S5, S6, S8, S9, S12 are attention-class (S4 is spend-class only if purchase-verified, which none of this cluster's findings are).

| Class | Signal | Tier reached this cluster | Counts as spend per the cell-read rule (tier ≥5 required)? |
|---|---|---|---|
| Spend-class | S1 (Cigna posting) | 3 | **No** — below tier 5, downgrades to attention per `demand-signals.md`: "A spend-class signal below tier 5 counts as attention for the read" |
| Spend-class | S7 (Primerica filing) | 2 | **No** — filed but names no budget figure; S7's split-class rule requires a named spend figure to count as spend |
| Spend-class | S7 (NerdWallet) | 2 (per `e-case-census-c1`) | **No** — names a revenue-impact figure, not a spend figure; does not meet S7's spend-class carve-out |
| Spend-class | S10 | n/a | No qualifying finding |
| Spend-class | S11 | n/a | No qualifying finding |

**Spend-class findings that actually clear the tier-5 bar for a spend cell read, this cluster: 0.** Every finding in this cluster that touches a spend-class signal (S1, S7) falls below the tier-5 threshold or lacks a named budget figure, and therefore reads as attention-class evidence under `demand-signals.md`'s rule, not as a spend cell-read input. This is consistent with H4's framing (demand is attention-only in every SMB cell) but extends further here: **no cell in this vertical, at any buyer size, produced a qualifying spend-class observation this pull** — the strongest evidence found (Cigna's Enterprise-labelled posting, NerdWallet's Silver-graded revenue case) is real, attributable, and tier-appropriate, but neither clears the spend bar as `demand-signals.md` defines it.

Attention-class findings, all cells combined: 6 LinkedIn postings (S1, tier 3), 1 filed exec-bio (S7, tier 2), 1 Silver P4-c1 case plus 2 statement-only P4-c1 cases (S7, tier 2), 4 conference-logo names plus 1 conference session (S8, tier 3), 3 `/llms.txt` hits of 9 resolved domains (S12, tier 1, vertical-wide).

## Browser backlog

| Item | Channel | Blocked as |
|---|---|---|
| 1 | Indeed | 403 to fetch, no extension held |
| 2 | Upwork | 403 to fetch, no extension held |
| 3 | G2 | 403 to fetch, no extension held |
| 4 | Capterra | 403 to fetch, no extension held |
| 5 | TED (ted.europa.eu) | 405, human-verification challenge |
| 6 | Google Trends | requires JS rendering, no browser tool held (S9) |
| 7 | Search Engine Land (referenced by `f-agency-census-c5`, not re-attempted this pull) | Cloudflare challenge on every tool tried in that prior pull |

**Browser backlog count: 6 distinct channels this cluster** (item 7 is a pre-existing backlog item from a different cluster's file, not counted again here).

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| Does Indeed or Upwork carry additional GEO/AEO/AI-visibility postings at card issuers, insurers, or supplement brands not found via LinkedIn? | indeed.com, indeed.com/rss (both 403); upwork.com, upwork.com/ab/feed/jobs/rss (both 403) | 2026-09-22 |
| Does G2, Capterra, or OMR carry a reviewer-industry (financial services / insurance / health) breakdown for any GEO/AI-visibility vendor? | g2.com (403), capterra.com (403), omr.com (200, general AI category only, no dedicated GEO category found) | 2026-09-22 |
| Does UK Contracts Finder carry a GEO/AI-visibility procurement award once correctly keyword-filtered? | contractsfinder.service.gov.uk OCDS API (200, filter appears non-functional as invoked) | 2026-09-22 |
| Does TED carry any EU tender naming GEO/AI-visibility services? | ted.europa.eu (405, human-verification block) | 2026-09-22 |
| What is Google Trends' relative search-interest series for GEO/AEO/AI-visibility terms, filtered to insurance/cards/supplements? | trends.google.com (not reachable without browser rendering) | 2026-09-22 |
| Does Primerica's 10-K disclose an extractable headcount or revenue figure to place its S7 finding into a buyer-size band? | `sec.gov/Archives/edgar/data/1475922/000119312526082233/pri-20251231.htm` (XBRL-tagged figures not isolated by this pull's plain-text grep method) | 2026-09-22 |

## Counts

| | Count |
|---|---|
| Raw pull files landed, this cluster | 12 (11 signal files + this census) |
| Cells with at least one `checked` mark (of 9) | 1 (organic recommendation / enterprise) |
| Signals with at least one blocked channel (of 10 in scope) | 5 (S1 — Indeed/Upwork; S4 — G2/Capterra; S9 — no browser tool; S10 — TED, UK CF filter; S6 — DDG rate-limiting, partially worked around via lite.duckduckgo.com) |
| Spend-class findings clearing the tier-5 cell-read bar | 0 |
| Browser backlog items | 6 |
| Unknowns recorded | 6 |
| Qualifying S1 postings found (any buyer size) | 6 (insurance ×5, supplements ×1 counted once for Juice Plus+; Simply Business also insurance — 6 total across insurance/supplements combined) |
| S1 credit-card sub-vertical result | 0 qualifying (9 queries checked, all returned engineering/risk/compliance titles only) |
| New S7 filer found beyond P4-c1 | 1 (Primerica, Inc.) |
| S12 domains resolved cleanly (of 10 sampled) | 9 (1 excluded, 500 error); 3 of 9 (33%) served a real `/llms.txt` |

## Deviations from the task's channel list

- `html.duckduckgo.com/html/` 403'd on every attempt this pull (consistent with `f-agency-census-c5`'s prior note on rate-limiting); `lite.duckduckgo.com/lite/` was substituted and worked (200) for the S6 and S11 sweeps. This is a same-provider fallback, not a different search engine, and is noted inline in the affected raw files.
- Google's search-interest tool (S9) could not be attempted at all — the task names this signal "browser-only," and this agent holds no browser tool; recorded as a method gap, not a search failure.
- The Primerica 10-K's employee headcount could not be isolated from its XBRL-tagged markup by this pull's plain-text extraction method; this is recorded as `unknown` rather than guessed.

## Caveats

- Per `demand-signals.md`'s cell-attribution rule, a finding that names the vertical but not the buyer size "moves no cell" — this is why 8 of the 9 cells in the matrix above carry no `checked` entry for S1/S7/S8 despite this cluster finding six qualifying job postings, one new filing, and four conference name-matches. The evidence exists at the vertical level; it does not exist at the cell level, because the sources themselves did not state a buyer-size band. This is a structural property of the source material (job postings and filings rarely self-describe the poster's own size band in prose), not a gap in this pull's search effort.
- Oldest pull depended on: 2026-09-22 (every raw file in this cluster was pulled today; the two conference cross-references were themselves pulled 2026-09-22 by a different task, and `e-case-census-c1`'s underlying filings range from 2026-02-03 to 2026-08-06, none flagged stale under `plan.md`'s one-quarter rule as of this pull's date).
- No cell-read verdict (spend/attention/none) is assigned in this file — per the task's own scope, that is Pass 8's compile step (`docs/customers/high-cpa-regulated.md`), which reads this census and the raw files it cites.
