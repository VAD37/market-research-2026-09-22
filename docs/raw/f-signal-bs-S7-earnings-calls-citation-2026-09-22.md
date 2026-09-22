# S7 earnings-call mentions by SaaS filers — citation of existing raw, no new pull

```yaml
source:          this repo's own docs/raw/ — P4-c1 earnings-call census, plus HubSpot and Yext SEC-filing access-attempt files
url_or_doc_id:   docs/raw/e-case-census-c1-2026-09-22.md ; docs/raw/a-hubspot-filing-2026-09-22.md ; docs/raw/a-yext-filing-2026-09-22.md ; docs/raw/a-vendor-roster-2026-09-22.md rows 10 and 14
published:       2026-09-22 (all three cited files pulled same day, this pass)
pull_date:       2026-09-22
pull_method:     manual (citation of prior same-day raw pulls, no new fetch performed by this file)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     inherits the tier of the strongest cited evidence (filed, per trust-rubric.md) where a filing is genuinely reached; downgraded per-item below where only an access attempt or a company-stated substitute was obtained
source_label:    filed (where reached); company-stated (HubSpot/Yext substitute pages); n/a (P4-c1 SaaS-vertical cells — zero cleared)
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        n/a — this file quotes and cross-references the cited raw files rather than re-capturing their bodies
```

## Verbatim

**From `e-case-census-c1-2026-09-22.md` (P4-c1, earnings calls and investor decks, success-story hunt):** ten filings/transcripts screened this cluster (IAC ×2, Yelp, Chegg, NerdWallet, TechTarget, Criteo, EverQuote, LendingTree, Reddit) from 64 total screened. **Cleared per vertical: high-CPA regulated 1 (NerdWallet, Silver); skincare and beauty 0; B2B SaaS 0; none named 3.** None of the ten filers is itself best described as a B2B SaaS company in the sense this repo's vertical uses (they are media/lead-gen, consumer finance, and consumer-review businesses); the AI-relevant passage in each names no B2B SaaS vertical. This is the direct, load-bearing finding for S7 in this vertical: **the earnings-call channel, as already swept by P4-c1, produced zero B2B SaaS cases at any grade.**

**From `a-hubspot-filing-2026-09-22.md` and `a-yext-filing-2026-09-22.md`:** both files are access **attempts**, not successful filing pulls — every `sec.gov` / `efts.sec.gov` / `data.sec.gov` path returned a 403 robots.txt block or an "Undeclared Automated Tool" page to both the plain-fetch tool and a Playwright browser, in the session that produced them. Yext's file did obtain a substitute: the company's own Investor Relations site republication of its Q2 FY27 earnings release (`investors.yext.com`, 2026-09-01), stating verbatim: **"Completed acquisition of GoShine, expanding the Yext platform to brand-level visibility optimization for AI search."** HubSpot's file obtained no filing-text substitute, only a third-party filing-index page (BamSEC) confirming filing dates without body text.

**Per `a-vendor-roster-2026-09-22.md`** (cited by both filing-access files, not re-opened by this file): row 10 records that HubSpot's 10-K (filed 2026-02-11) and DEF 14A (filed 2026-04-27) were found via EDGAR full-text search to name "answer engine optimization"; row 14 records Yext's 8-K / Q2 FY27 earnings release naming the same passage quoted above.

## Pull notes — mechanical only

- **Important distinction, recorded explicitly:** HubSpot and Yext are both SaaS companies that themselves **sell** AI-visibility/AEO-adjacent products (HubSpot's AEO features, Yext's GoShine acquisition) — they are S7 hits only in the sense that a SaaS filer's own filing names the category, not in the sense of a SaaS company disclosing a **budget line for buying** an AI-visibility tool from someone else. Per the task's own framing ("earnings-call mentions by SaaS filers"), both are recorded here as the closest available S7 evidence, but flagged: **neither passage names a spend figure, so per `demand-signals.md`'s S7 split-class rule ("only a named budget figure in S7 counts as spend... the rest is attention"), this does not clear the spend bar even before considering that it describes product strategy rather than purchasing.**
- Buyer-size mapping if this were treated as a demand cell: HubSpot and Yext are both large public companies (headcount well over 1,000 per public record, not independently re-verified this pull) — Enterprise band — but since neither passage is a genuine buyer-side spend disclosure, **no cell is moved by this evidence.** Recorded as `checked — see e-case-census-c1 (0 B2B SaaS cleared) and a-hubspot-filing/a-yext-filing (product-strategy mentions, not buyer spend) — 2026-09-22`, cell-attribution: none.
- No new fetch was performed by this file — it exists to give S7 its own dedicated `docs/raw/f-signal-bs-*` filename per the task's deliverable-naming requirement, while avoiding a duplicate re-pull of channels this repo's Pass 4 cluster already exhausted for B2B SaaS earnings-call evidence today.
- ZoomInfo: no dedicated ZoomInfo SEC-filing raw file was found in `docs/raw/` under this task's read-only citation set (only HubSpot and Yext filing-access files exist as of this pull) — recorded as `unknown — checked docs/raw/ for a ZoomInfo filing file — none found — 2026-09-22`, consistent with the task brief's phrasing ("ZoomInfo / HubSpot / Yext filings are in raw already") being only partially accurate for ZoomInfo specifically.
