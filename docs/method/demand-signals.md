# Demand signals and the segment matrix

Set 2026-09-22, Pass 0, per `plan.md` "Demand signals — internet-only" and "Pass 0 additions". Fixes the catalogue Pass 8 fills per cell, the rule that turns signals into a one-word cell read, and the empty matrix. Terms are `glossary.md`'s; tiers are `trust-rubric.md`'s. No market facts here — this is the instrument, not a reading.

Internet-only per `scope.md` R2. No signal observes a budget directly; every row is a proxy.

## Catalogue

Codes S1–S9 are `plan.md`'s list, in its order, with its "proxies" and "bias" text carried through. S10–S12 are additions — see below the table. **Class** is binary: a spend signal evidences money that changed hands; an attention signal does not, at any volume.

| Code | Signal | Proxies | Channel kind | Unit | Bias | Expected tier | Class |
|---|---|---|---|---|---|---|---|
| S1 | Job postings naming AI visibility, GEO, AEO | Budgeted intent | Job boards, employer career pages | Postings per period, per employer size band | Lags spend; large firms over-represented. Headcount budget, not category spend — weakest spend class | 3 (employer's own posting) | spend |
| S2 | Vendor customer counts, logos, case-study rosters | Paying demand | Vendor site, case-study pages | Named customers; logo count | Vendor-reported; logos are not contracts; may include pilots and free tiers | 5 with n and date, 6 without | spend |
| S3 | Vendor funding rounds and stated ARR | Investor belief, not buyer demand | Funding filings, company statements | Currency raised; stated ARR | Filed beats stated. Funding is investor belief; only the ARR component evidences buyers | 2 filed, 5 stated | ARR spend; round attention |
| S4 | Review-site volume and dates | Active buyers | Software review sites | Reviews per month; first-review date | Vendors farm reviews; check velocity not count. Unverified reviews are attention only | 5 verified-buyer, 6 unverified | spend if purchase-verified |
| S5 | Community thread volume | Practitioner attention | Practitioner forums, subreddits | Threads and unique posters per period | Vocal minority; one poster can carry a thread count | 4 if the platform publishes counts | attention |
| S6 | Agency service pages and rate cards | Sell-side belief in demand | Agency sites | Pages offering the service; list price | Marketing. A list price is an asking price, never a purchase | 3 on existence, 6 on framing | attention |
| S7 | Earnings-call and investor-deck mentions by brands | Board-level attention | Transcripts, investor decks | Mentions per call; named spend line if any | Rare, high value when present. Attention unless a budget figure is named | 2 filed | attention; spend if a figure is named |
| S8 | Conference agenda counts | Category attention | Event agendas, session lists | Sessions per event; share of agenda | Sponsor-driven; a paid slot is not demand | 3 | attention |
| S9 | Search interest for category terms | Awareness, not spend | Search-interest tools | Indexed interest; absolute volume if disclosed | Term confusion across GEO meanings; index is relative, not a count | 4 if method published | attention |
| S10 | Procurement and tender records naming the category | Committed buyer budget | Public procurement registers, contract-award notices | Award value; award date; buyer | Public-sector and large-buyer only; private demand invisible here | 2 filed | spend |
| S11 | Disclosed price actually paid, buyer-stated | Willingness to pay | Buyer write-ups, filings, contract exhibits | Currency per period, with scope bought | Buyers who publish a price are unrepresentative; discounts unstated | 2 filed, 4 buyer-stated | spend |
| S12 | On-property adoption artifacts, measured across a brand sample | Unpaid effort committed | Brand domains, sampled by us | Share of sampled domains carrying the artifact | Effort, not money. Artifact presence may be a template default, not a decision | 1 measured-by-us | attention |

**Additions declared.** S10, S11 and S12 are not in `plan.md`'s list. S10 and S11 are added because `plan.md`'s nine carry no signal that observes a price actually paid, while `templates/customer-segment.md` requires one for the willingness-to-pay section. S12 is added because on-property artifacts are internet-observable at tier 1 and separate committed effort from stated interest. All three are internet-only and need no outreach.

**Channel kind, not channel.** Pass 1 names the concrete channels in `sources/channels.md`. The kinds above are what Pass 1 must find instances of.

## Cell-read rule

A cell reads exactly one word. Pass 8 applies this rule and nothing else.

| Read | Condition |
|---|---|
| **spend** | At least one spend-class signal observed **for that exact cell** at tier 5 or better |
| **attention** | No qualifying spend signal, and at least one signal of any class observed at any tier |
| **none — checked \<channels\> \<date\>** | Every catalogue signal checked, nothing found. The channels and date are named |
| *(blank)* | Not yet checked. A blank is never written as `none` |

- Attention never stands in for spend, at any volume. Ten attention signals do not make a spend read (`plan.md`).
- A spend-class signal **below** tier 5 counts as attention for the read, and is still recorded at its own tier and class.
- Cell attribution must come from the source: the source says which sub-market, which vertical and which buyer size. Nothing is inferred from a vendor's target-customer page — sell-side claim, `competitors/` (`plan.md` Pass 8).
- A signal that names a buyer size the source does not define is recorded with the source's own wording quoted and mapped per the boundary rule below; unmappable, it is recorded against the vertical and sub-market with buyer size `unassigned` and moves no cell.
- S3 and S7 are split-class: only the ARR component of S3, and only a named budget figure in S7, count as spend. The rest is attention.
- Conflicting observations inside one cell sit side by side, attributed, never averaged (root `CLAUDE.md`). A conflict does not downgrade a read: if the spend condition holds on one signal, the read is spend and the contrary observation is recorded beside it.
- Spend-class and attention-class signals are never summed into one score.

## Buyer-size boundaries — a method choice

Conventional bands, fixed here so Pass 8 applies one rule to every cell. **This is a method choice made 2026-09-22, not a fact about how this market segments itself.** Headcount is primary because it is the more often disclosed; revenue is the fallback.

| Band | Headcount, as disclosed | Revenue fallback, as disclosed |
|---|---|---|
| SMB | under 100 | under 50M USD annual |
| Mid-market | 100 to 999 | 50M to 1B USD annual |
| Enterprise | 1000 or more | over 1B USD annual |

- Observable proxy, in order: a filing; the company's own site or careers page; a professional-network company profile. Whichever is used is named in the cell's signal row.
- Revenue is used only when headcount is undisclosed. The two are never combined, and a company straddling the bands on the two measures is recorded at its headcount band with the revenue noted.
- Where a source publishes its own bands, `templates/customer-segment.md` requires the source's definition quoted. Map it to the bands above and show the mapping; if it cannot be mapped without a guess, record `unassigned`.
- Currency as disclosed; non-USD figures are kept verbatim with the currency, never converted.

## The empty matrix

3 verticals × 3 sub-markets × 3 buyer sizes = 27 cells. Every cell blank at Pass 0. One column per catalogue signal. Pass 8 fills it into `customers/<vertical>.md`, nine rows per file, per `templates/customer-segment.md`.

| Vertical | Sub-market | Buyer size | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | Read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Skincare and beauty | Organic recommendation | SMB | | | | | | | | | | | | | |
| Skincare and beauty | Organic recommendation | Mid-market | | | | | | | | | | | | | |
| Skincare and beauty | Organic recommendation | Enterprise | | | | | | | | | | | | | |
| Skincare and beauty | Paid placement | SMB | | | | | | | | | | | | | |
| Skincare and beauty | Paid placement | Mid-market | | | | | | | | | | | | | |
| Skincare and beauty | Paid placement | Enterprise | | | | | | | | | | | | | |
| Skincare and beauty | Agentic commerce | SMB | | | | | | | | | | | | | |
| Skincare and beauty | Agentic commerce | Mid-market | | | | | | | | | | | | | |
| Skincare and beauty | Agentic commerce | Enterprise | | | | | | | | | | | | | |
| B2B SaaS | Organic recommendation | SMB | | | | | | | | | | | | | |
| B2B SaaS | Organic recommendation | Mid-market | | | | | | | | | | | | | |
| B2B SaaS | Organic recommendation | Enterprise | | | | | | | | | | | | | |
| B2B SaaS | Paid placement | SMB | | | | | | | | | | | | | |
| B2B SaaS | Paid placement | Mid-market | | | | | | | | | | | | | |
| B2B SaaS | Paid placement | Enterprise | | | | | | | | | | | | | |
| B2B SaaS | Agentic commerce | SMB | | | | | | | | | | | | | |
| B2B SaaS | Agentic commerce | Mid-market | | | | | | | | | | | | | |
| B2B SaaS | Agentic commerce | Enterprise | | | | | | | | | | | | | |
| High-CPA regulated | Organic recommendation | SMB | | | | | | | | | | | | | |
| High-CPA regulated | Organic recommendation | Mid-market | | | | | | | | | | | | | |
| High-CPA regulated | Organic recommendation | Enterprise | | | | | | | | | | | | | |
| High-CPA regulated | Paid placement | SMB | | | | | | | | | | | | | |
| High-CPA regulated | Paid placement | Mid-market | | | | | | | | | | | | | |
| High-CPA regulated | Paid placement | Enterprise | | | | | | | | | | | | | |
| High-CPA regulated | Agentic commerce | SMB | | | | | | | | | | | | | |
| High-CPA regulated | Agentic commerce | Mid-market | | | | | | | | | | | | | |
| High-CPA regulated | Agentic commerce | Enterprise | | | | | | | | | | | | | |

Signal cell contents at Pass 8: the observation in 12 words with the figure verbatim, plus its `raw/` path and tier in the `customers/` signal table. A checked signal that yielded nothing is written `nil`; an unchecked signal stays blank.

## Caveats

- Every signal is a proxy. None observes a budget. A cell reading `spend` evidences that money moved somewhere in that cell, not how much.
- Publication bias runs one way: quiet spending leaves no public trace, so `none` reads are weaker evidence than `spend` reads. `templates/customer-segment.md` repeats this per file.
- S1, S2 and S4 — the three spend signals most likely to be available — are the three most exposed to vendor and employer self-presentation. A cell resting on one of them alone is flagged in its file.
- S10 and S11 reach tier 2 but are rare. Expect most cells to have neither.
- Tier expectations in the catalogue are expectations, not assignments. Every pull is tiered on its own evidence per `trust-rubric.md`, and a hidden method drops it one tier.
- The buyer-size bands are a method choice; a market that segments itself differently will be mis-cut by them, and the mis-cut will be invisible in the matrix.
- The catalogue is fixed at Pass 0. A signal found later is appended with its date and marked as added after registration, so cells read before the addition are known to be incomplete.
