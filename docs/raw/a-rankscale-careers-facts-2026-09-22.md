# Rankscale.ai — careers, company registration, and docs/changelog

```yaml
source:          Rankscale GmbH (rankscale.ai)
url_or_doc_id:   https://rankscale.ai/careers ; https://rankscale.ai/imprint ; https://rankscale.ai/changelog
published:       careers and imprint undated on-page (imprint gives a filed registration date, 22 July 2025); changelog entries individually dated, most recent captured 2026-09-04
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; the imprint's registration data (Firmenbuch, VAT, D-U-N-S) is filed-adjacent (Austrian statutory disclosure) but not independently cross-checked against the Austrian companies register itself this pull
source_label:    vendor-reported (careers, changelog); filed (imprint's statutory registration fields, as disclosed by the company on its own page, not independently verified against the Firmenbuch register directly)
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        careers page in full; imprint page in full; changelog page, first ~2500 characters (September 2026 entries only)
```

## Verbatim — Careers

"Rankscale Careers — 5 open roles/1 location/Hybrid team — Join us in building the future of AI Search visibility — We are hiring for 5 roles in Vienna (hybrid). We hire based on talent and drive, regardless of background.

Vienna (Hybrid) - Full-time — Full Stack Developer — Build the product experience that turns AI visibility data into actionable insights for our growing client base.

Vienna (Hybrid) - Full-time — Front-End Developer / Product Designer — Own how Rankscale looks, feels, and works by designing and building product experiences users love.

Vienna (Hybrid) - Full-time — Technical Sales Manager — Own our sales motion from first contact to signed contract, and grow into the leader who builds the sales team around you.

Vienna (Hybrid) - Part-time — Junior Sales Rep — Run real product demos with real prospects from week one after ramp, then grow into a full-time Account Executive if it is a mutual fit.

Vienna (Hybrid) - Part-time — Brand & Marketing Intern — Support the CMO directly on brand, content, and campaigns. Four-month internship with the intent to continue into a role where you own a clear marketing lane, not the full marketing function, if we are a mutual fit."

**5 open roles listed, all statically rendered** (unlike Scrunch's and Brandlight's client-side-rendered job boards). No total headcount figure stated.

## Verbatim — Imprint (Austrian statutory disclosure)

"Imprint — Information duty according to E-Commerce Gesetz, §14 Unternehmensgesetzbuch, §63 Gewerbeordnung and disclosure requirement according to §25 Mediengesetz.

## Rankscale GmbH
Purpose of company: Services in automatic data processing and information technology
VAT number: ATU82401848
Company register number: 658253w
Registered in Firmenbuch: 22 July 2025
D-U-N-S number: 301153533
GLN number: 9110037989061
Commercial register court: Vienna

## Contact Information
Headquarter: Untere Viaduktgasse 10/6, 1030 Vienna
Website: https://rankscale.ai
Email: info@rankscale.ai"

## Verbatim — Changelog (most recent entries)

"What's new in Rankscale — New features, improvements, and fixes across the platform. [Month/Type filters; RSS and JSON subscribe links, both 'latest' and 'full']

September 4, 2026 · New — Query Fanout widgets on Custom Dashboard — Add Fanout Coverage, Top Fanout Queries, Fanout Activity Over Time, Probed Domains, and Appendix Signals widgets to Custom Dashboard so Query Fanout insights can live on saved dashboard views.

September 4, 2026 · Improved — Uncapped search term lists in the Metrics API — GET /v1/metrics/search-terms now supports uncapped=true so API clients can return every operational search term for a brand instead of stopping at the default list limit.

September 3, 2026 · New — Query Fanout Insights — Query Fanout on Brand Details ranks the internal searches AI engines run for your prompts...

September 2, 2026 · New — See citation sources for a sentiment statement at a glance...

September 2, 2026 · New — Set or clear expiry on shared dashboard links — Enterprise and Agency Growth plans can set a custom expiry per shared dashboard link in Settings...

September 2, 2026 · New — Filter branded and non-branded prompts on the Search Terms table...

September 2, 2026 · Improved — Clearer dashboard cards with Latest, period average, and peer badges...

August 28, 2026 · New — Brand distribution widgets, a brand presence filter, and a comp[arison feature — truncated]"

## Pull notes — mechanical only

- Careers and imprint pages each fetched in one call and captured in full.
- Changelog fetched to ~2500 characters, capturing seven dated entries spanning 2026-08-28 to 2026-09-04; the page continues further back (not pursued this pull).
- **This is the only vendor of the six in this cluster with a real, publicly dated, itemized changelog** — Scrunch, Brandlight, Change Agents Corp, and Locafy have none; Otterly.AI has a docs site but no separately-verified changelog page.
- **HQ, founding/registration date, and legal entity resolved with high confidence**: Rankscale GmbH, Untere Viaduktgasse 10/6, 1030 Vienna, Austria, registered in the Austrian Firmenbuch (commercial register) 22 July 2025, VAT ATU82401848 — confirmed identically on two separate Rankscale-owned pages (this imprint page and the /facts page, `a-rankscale-method-engines-2026-09-22.md`). This directly contradicts a sibling agent's separately-pulled getlatka.com HQ figure ("Königstetten, Austria"), which was not touched or re-verified by this pull — recorded side by side per root CLAUDE.md.
- No funding round, investor, or revenue/ARR figure is disclosed on any Rankscale-owned page pulled this task. Recorded: `unknown — checked rankscale.ai careers, imprint, facts, and pricing pages, 2026-09-22 — no funding round, investor, or ARR figure found on the vendor's own domain`. (A sibling agent's separate getlatka.com pull, per `docs/raw/a-vendor-roster-2026-09-22.md`, reports "~$220K ARR, 2-person team" — not independently re-verified by this pull, and in apparent tension with the 5 concurrently-open roles found on Rankscale's own careers page today, which would suggest a team larger than 2 if all were filled.)
