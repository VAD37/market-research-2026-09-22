# Conference cross-reference — S8, high-CPA regulated names at GEO Conference NYC 2026 and MozCon London 2026

```yaml
source:          docs/raw/f-conference-geo-conference-nyc-2026-agenda-2026-09-22.md ; docs/raw/f-conference-mozcon-london-2026-agenda-2026-09-22.md (this repo, cross-referenced, not re-pulled)
url_or_doc_id:   https://geo-conference.com/events/nyc-2026 ; https://geo-conference.com/#events ; https://moz.com/mozcon/schedule ; https://moz.com/mozcon
published:       geo-conference.com pages undated (NYC edition dated 2026-12-04 as an event date, not a publish date); moz.com pages undated, London date "Nov 13" inferred 2026
pull_date:       2026-09-22 (both cited files; this file's own pull date is a same-day cross-reference)
pull_method:     cross-reference (read of this repo's own already-landed raw/ files, both pulled by browser extension per their own headers — see `pull_method` in each cited file)
pull_purpose:    evidence about a number
tier:            3 — inherited from both cited files (table default: conference's own site, reliable on existence, biased on framing)
tier_reason:     see cited files' own tier_reason
source_label:    company-stated
lane:            A, B, C, F
sub_market:      organic recommendation (GEO Conference NYC logos); agentic commerce (MozCon London session)
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        cross-reference — the two exact lines quoted below, taken verbatim from the cited raw files
vertical:        high-CPA regulated — insurance (Mutual of Omaha), finance/investment (Franklin Templeton), comparison publisher (NerdWallet); financial services (John Lewis Financial Services division)
cell:            unattributed — neither source states its own buyer-size band for the named companies
query:           n/a — cross-reference; original pulls found via browser extension per the cited files' own headers
```

## GEO Conference NYC 2026 — sponsor/attendee logo wall

Per `docs/raw/f-conference-geo-conference-nyc-2026-agenda-2026-09-22.md`:

> "Company logos listed (attendee/sponsor wall): Google, Adobe, Marriott, AT&T, Bayer, Incyte, Expedia, Red Bull, L'Oréal, Comcast, Accenture, Intuit, Cloudflare, Etsy, Yelp, Electronic Arts, **NerdWallet**, Condé Nast, **Franklin Templeton**, Philip Morris Int'l, Sixt, Semrush, Federal Reserve Bank of NY, Pew Research, Carnegie Mellon, The Wharton School, Euromonitor, Choice Hotels, Webflow, Yext, Conductor, **Mutual of Omaha**, Houston Methodist"

Three names from this logo wall map to the high-CPA-regulated vertical as defined for this repo (`plan.md`: "cards, insurance, supplements"): **NerdWallet** (a comparison publisher explicitly named as this vertical's own subject in `plan.md`'s vertical description — also independently confirmed as a genuine AI-search-affected brand by `e-case-census-c1`'s Silver-graded case), **Mutual of Omaha** (a life/health/Medicare-supplement insurer), and **Franklin Templeton** (an asset-management/investment firm — finance-adjacent, not strictly cards/insurance/supplements, recorded as a borderline inclusion). The Federal Reserve Bank of NY is a regulator, not a buyer in this vertical, and is excluded.

A logo on a sponsor/attendee wall is company-attendance evidence (the company sent someone, or is a sponsor), not a spend-on-GEO-tools or a named-role evidence — weaker than the S1 job-posting or S7 filing evidence in this cluster. It is recorded as an attention-class signal (S8's catalog class), not spend-class, per `demand-signals.md`.

## MozCon London 2026 — agentic-commerce session

Per `docs/raw/f-conference-mozcon-london-2026-agenda-2026-09-22.md`:

> | 3:20–3:50 PM | "How to Win at Agentic E-Commerce" | Miracle Inameti-Archibong | **John Lewis (Financial Services)** |

John Lewis Partnership's financial-services division (credit cards, insurance, and related consumer-finance products under the John Lewis/Waitrose brand in the UK) is credited as the speaker's employer for a named session specifically on **agentic commerce** — the only S8 hit in this cluster that maps to the agentic-commerce sub-market rather than organic recommendation. This is attention-class (a conference speaking slot), not a disclosed spend figure.

## Result

**`checked — 2 conferences, 3 borderline-to-clear vertical name-matches (NerdWallet, Mutual of Omaha, Franklin Templeton at GEO Conference NYC; John Lewis Financial Services at MozCon London) 2026-09-22`.** Both cited files are tier 3, company-stated, attention-class per S8's catalog entry. No buyer-size band is stated by either source for any of the four companies — cell attribution stays `unassigned` per `demand-signals.md`'s cell-attribution rule.

## Caveats

- This file adds no new pull; it routes the task's instruction ("S8 conference sessions naming the vertical — cite P4-c3 raw: `docs/raw/f-conference-*`") through the two `f-conference-*` files that actually name a high-CPA-regulated company, out of the six `f-conference-*` files landed by Pass 4/8's conference cluster (`ana-ai-technology-marketers`, `brightonseo-october-2026`, `content-marketing-world`, `geo-conference-nyc-2026`, `mozcon-london-2026`, `smx-events` — the other four were checked via `grep` for `insur|financ|credit card|supplement|bank|health.?care|pharma` and returned no match).
- A sponsor/attendee logo is the weakest form of S8 evidence in the catalog ("a paid slot is not demand" — `demand-signals.md` S8 bias line); it is recorded here as attendance/sponsorship, not as a purchase of a GEO/AI-visibility tool.
- NerdWallet's appearance both at this conference (S8) and in the P4-c1 Silver case (S7, see `f-signal-hr-S7-p4c1-crossref-2026-09-22.md`) is the same company evidenced twice through two different signal classes — recorded side by side, not merged into one stronger claim, per root `CLAUDE.md`'s "never averaged" rule applied here to cross-signal corroboration.
