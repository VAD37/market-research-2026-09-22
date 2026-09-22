# Brand-side corroboration census — P4-c7 (Pass 4 second sweep)

```yaml
source:          brand-owned domains only (newsroom, IR, blog, careers, own product/customer pages); DuckDuckGo html endpoint used as a site-restricted search substitute over each brand's own domain (WebSearch budget exhausted per STATE.md)
url_or_doc_id:   multi-brand — see rows below; every URL checked is a brand-owned domain or a DuckDuckGo site: query scoped to one
pull_date:       2026-09-22
pull_method:     fetch (mcp__MCP_DOCKER__fetch; DuckDuckGo html.duckduckgo.com/html/ used as the search substitute per task instruction "DuckDuckGo's HTML endpoint sparingly"; no browser extension, no Playwright — fetch-only per task boundary)
pull_purpose:    evidence about a number (brand-side corroboration or contradiction of a vendor/program case-study claim)
tier:            n/a at this file's level — this is the census summary, not a pull; every row would be tier 3 (company-stated / brand's own page) had a corroboration or contradiction been found. None was.
tier_reason:     table default
source_label:    company-stated (for any hit); this file itself is a compiled index
lane:            E, F
sub_market:      organic recommendation (vendor cases), paid placement (Direct Offers, ChatGPT Ads partners), agentic commerce (Copilot Checkout)
engine:          n/a — brand-side check, not engine-side
metric_kind:     none
supersedes:      none
captured:        census summary — compiled from the source files named in the task brief; every brand traces to one of those files
```

No interpretation. Every row traces to the Pass 2/3 file that named the brand. `silent — checked <query/URL> 2026-09-22` used where the brand's own domain was searched and no corroboration or contradiction was found. Grading rule 1 (`plan-review-1-2026-09-22.md` §3) applies to any corroboration carrying a result claim; none was found this pull, so no case in this file is graded.

## Result — zero corroborations, zero contradictions

**Every one of the 59 brands checked this pull reads `silent`.** No brand's own newsroom, IR page, blog, or careers page named the AI-visibility vendor, ad program, or checkout program that a Pass 2/3 file attributed to it. No raw pull files were created under `e-case-c7-<brand>-2026-09-22.md` because the deliverable rule ("one raw file per brand page that **corroborates or contradicts**") was never triggered — every check landed on `silent`. This is recorded as the finding for this cluster, not adjusted or padded (`plan.md`: "Do not pad the table to avoid it").

Two near-misses, recorded for completeness, neither counted as corroboration:

- **Tinybird** (`tinybird.co/customer-stories/scrunch`, checked 2026-09-22): Tinybird's own site does name "Scrunch" — but as **Tinybird's own customer** for its data-infrastructure product ("Scrunch ships AI search analytics... with Tinybird"), the reverse commercial relationship from the one in question (Scrunch's customer census claims Tinybird as *Scrunch's* AI-visibility customer, "3x'd brand mentions"). The page makes no mention of Scrunch's AI-visibility product, brand mentions, or any metric matching the claim. Read: **silent** on the specific claim.
- **Ramp** (`ramp.com/vendors/profound`, `ramp.com/leading-indicators/...`, checked 2026-09-22): Ramp's own "Ramp Rate" spend-intelligence product profiles Profound as a fast-growing vendor category (adoption/spend data), but this is Ramp reporting on Profound as a SaaS vendor in its own analytics product — not Ramp confirming the specific claim attributed to it in Profound's case study ("Ramp — increased AI brand visibility 7x in accounts payable"). Read: **silent** on the specific claim.

## Counts

| Metric | Count |
|---|---|
| Brands named across all cited Pass 2/3 files (best-effort count, see §"Not checked — cap" for the itemised remainder) | ~166 |
| Checked this pull (priority-ordered per task cap) | 59 |
| Corroborates | 0 |
| Contradicts | 0 |
| Silent — checked | 59 |
| Not checked — cap | ~107 (itemised by source vendor below) |
| Raw pull files written (`e-case-c7-*`) | 0 — no corroboration or contradiction to pull |

**Per-vertical counts (skincare/beauty, B2B SaaS, high-CPA regulated):** not applicable — zero brand pages were opened and graded (all reads are `silent`), so no case entered the evidence-bar pipeline for any vertical. None of the 59 checked brands' Pass 2/3 source rows carry a vertical tag matching the three verticals in `plan.md`; most are horizontal SaaS, consumer, or retail names outside the anchor set. This is stated as the finding, not inferred as a vertical read.

**Unknowns recorded:** 4 — brand's own domain could not be conclusively identified within this pull's budget for **Aleph** (Profound customer; "AI-powered financial analysis platform," domain not resolved — multiple unrelated companies share the name "Aleph"), **Owings Auto** (RankPrompt case; only the vendor's own domain and the vendor founders' own LinkedIn posts were found, not a brand-owned domain), **Activate Digital** (Semrush case; `activate.digital` returned no DuckDuckGo index, domain unconfirmed), **Chime** (AirOps case; checked `chime.me`, a real-estate CRM brand — domain match to the AirOps case subject not independently confirmed).

**Browser backlog:** 0 — this cluster is fetch/DuckDuckGo-only per task boundary (no Chrome extension, no Playwright); no URL was left needing a browser.

## Checked — 59 brands, all `silent`

Priority order per task: (1) brands attached to a Bronze-or-better case, (2) Direct Offers / Copilot Checkout / ChatGPT Ads partners, (3) the rest.

### Priority 1 — Bronze-or-better cases

| Brand | Vertical as named | Vendor / program (Pass 2/3 raw path) | Reads | Brand-side check (URL/query) |
|---|---|---|---|---|
| Men's Wearhouse | none named (apparel retail) | Quattr, **Silver** — `docs/raw/a-vendor-census-c4-2026-09-22.md` row 3 | silent — checked | `menswearhouse.com` (DDG site: query, "Quattr"), 2026-09-22 |
| Plaid | none named (fintech) | Profound, Bronze — `docs/raw/a-profound-customers-2026-09-22.md` | silent — checked | `plaid.com` (DDG site: query, "Profound") — page found only an unrelated use of the word "profound" as an adjective, 2026-09-22 |
| MongoDB | none named (database/dev tools) | Profound, Bronze | silent — checked | `mongodb.com` (DDG site: query, "Profound AI") — no match, 2026-09-22 |
| Aleph | financial analysis platform (per vendor's own case page) | Profound, Bronze | silent — checked | domain not conclusively identified (see Unknowns); `tryprofound.com/customers/aleph` itself is the vendor's page, not brand-owned, 2026-09-22 |
| OpusClip | none named (video AI) | Profound, Bronze | silent — checked | `opus.pro` (DDG site: query, "Profound") — no match, 2026-09-22 |
| Hone | none named (HR/L&D) | Profound, Bronze | silent — checked | `honehq.com` (DDG site: query, "Profound") — no match, 2026-09-22 |
| Ramp | none named (fintech/spend mgmt) | Profound, Bronze | silent — checked (near-miss, see above) | `ramp.com` (DDG site: query, "Profound"), 2026-09-22 |
| Airbyte | none named (data infra) | Profound, Bronze | silent — checked | `airbyte.com` (DDG site: query, "Profound") — no match, 2026-09-22 |
| Lake.com | none named (travel) | Profound, Bronze | silent — checked | `lake.com` (DDG site: query, "Profound") — no match, 2026-09-22 |
| 1840 & Co. | none named (staffing/BPO) | Profound, Bronze | silent — checked | `1840andco.com` (DDG site: query, "Profound") — no match, 2026-09-22 |
| Akamai | none named (CDN/security) | Scrunch, Bronze — `docs/raw/a-scrunch-customers-2026-09-22.md` | silent — checked | `akamai.com` (DDG site: query, "Scrunch") — no match, 2026-09-22 |
| Strapi | none named (dev tools/CMS) | Scrunch, Bronze | silent — checked | `strapi.io` (DDG site: query, "Scrunch") — no match (only Strapi's own GEO guide blog post, unrelated), 2026-09-22 |
| Tinybird | none named (data infra) | Scrunch, Bronze | silent — checked (near-miss, see above) | `tinybird.co/customer-stories/scrunch` (full page fetched), 2026-09-22 |
| BairesDev | none named (nearshore dev staffing) | Scrunch, Bronze | silent — checked | `bairesdev.com` (DDG site: query, "Scrunch") — no match, 2026-09-22 |
| Stratabeat | none named (B2B SEO/GEO agency) | Scrunch, Bronze | silent — checked | `stratabeat.com` (DDG site: query, "Scrunch") — no match, 2026-09-22 |
| NinjaOne | none named (IT/RMM software) | BrightEdge, Bronze — `docs/raw/a-vendor-census-c4-2026-09-22.md` row 1 | silent — checked | `ninjaone.com` (DDG site: query, "BrightEdge") — no match, 2026-09-22 |
| Riskonnect | none named (GRC software) | BrightEdge, Bronze | silent — checked | `riskonnect.com` (DDG site: query, "BrightEdge") — no match, 2026-09-22 |
| Bloomfire | none named (knowledge mgmt) | BrightEdge, Bronze | silent — checked | `bloomfire.com` (DDG site: query, "BrightEdge") — no match (only login-portal subdomains indexed), 2026-09-22 |
| Sure Oak | SEO agency (self-described) | Semrush, Bronze — `docs/raw/a-vendor-census-c4-2026-09-22.md` row 4 | silent — checked | `sureoak.com` (DDG site: query, "Semrush") — page references Semrush's Authority Score generically, not the Bronze case, 2026-09-22 |
| Activate Digital | none named (agency) | Semrush, Bronze | silent — checked | `activate.digital` — domain not conclusively confirmed, no DDG index (see Unknowns), 2026-09-22 |
| Chime | real-estate CRM (domain-inferred) | AirOps, Bronze — `docs/raw/a-airops-customers-2026-09-22.md` | silent — checked | `chime.me` (DDG site: query, "AirOps") — no match; domain match unconfirmed (see Unknowns), 2026-09-22 |
| Title Nine | none named (apparel retail) | Conductor, Bronze — `docs/raw/a-conductor-customers-2026-09-22.md` | silent — checked | `titlenine.com` (DDG site: query, "Conductor") — no match, 2026-09-22 |
| verito.com | none named | AthenaHQ, Bronze ("#1 on ChatGPT") — `docs/raw/a-athenahq-customers-2026-09-22.md` | silent — checked | `verito.com` — DDG found only an unrelated "Verito" IT-services company (Wilmington, DE), identity match unconfirmed, 2026-09-22 |
| Grüns | supplements/DTC | AthenaHQ, Bronze ("6x Share of Voice") | silent — checked | `gruns.co` (DDG site: query, "AthenaHQ") — no match, 2026-09-22 |
| Humand | HR/internal-comms software | RankPrompt, Bronze — `docs/raw/a-rankprompt-customers-2026-09-22.md` | silent — checked | `humand.co` (DDG site: query, "RankPrompt") — no match; found only an unrelated "SEO Specialist: AI Search" job posting on Humand's own careers page (no vendor named), 2026-09-22 |
| Owings Auto | auto dealership | RankPrompt, Bronze — `docs/raw/a-rankprompt-customers-2026-09-22.md` | silent — checked | Brand-owned domain not located; only `rankprompt.com` (vendor's own site) and RankPrompt founders' personal LinkedIn posts found, 2026-09-22 |
| Pointhound | travel/points-booking app | Sitefire, Bronze — `docs/raw/a-sitefire-customers-2026-09-22.md` | silent — checked | `pointhound.com` (DDG site: query, "Sitefire") — no match, 2026-09-22 |
| Jerry.ai | auto insurance app (domain confirmed) | Sitefire, Bronze | silent — checked | `jerry.ai` (DDG site: query, "Sitefire") — no match, 2026-09-22 |
| Freshpet | pet food (agency case) | Intero Digital, Bronze — `docs/raw/f-agency-census-c5-2026-09-22.md` row 3 | silent — checked | `freshpet.com` (DDG site: query, "Intero Digital"; retried without vendor name for "GEO"/"AI search") — no match on either, 2026-09-22 |

### Priority 2 — Direct Offers / Copilot Checkout / ChatGPT Ads partners

| Brand | Vertical as named | Vendor / program (Pass 2 raw path) | Reads | Brand-side check |
|---|---|---|---|---|
| Chewy | pet retail | Google Direct Offers pilot — `docs/raw/b-google-platform-summary-2026-09-22.md` Table 1 | silent — checked | `chewy.com` (DDG site: query, "Direct Offers" OR "AI Mode" Google) — no results, 2026-09-22 |
| Gap | apparel retail | Google Direct Offers pilot | silent — checked | `news.gap.com` (DDG site: query) — no results; retried "AI shopping" — no results, 2026-09-22 |
| L'Oréal | beauty/cosmetics | Google Direct Offers pilot | silent — checked | `loreal.com` (DDG site: query, "Direct Offers" Google) — no results, 2026-09-22 |
| Petco | pet retail | Google Direct Offers pilot | silent — checked | `petco.com` (DDG site: query, "Direct Offers" Google) — no results, 2026-09-22 |
| e.l.f. Cosmetics | beauty/cosmetics | Google Direct Offers pilot | silent — checked | `elfbeauty.com` (DDG site: query, "Direct Offers" OR "Google AI") — no results, 2026-09-22 |
| Samsonite | luggage retail | Google Direct Offers pilot | silent — checked | `samsonite.com` (DDG site: query, "Google AI") — no relevant results, 2026-09-22 |
| Rugs USA | home goods retail | Google Direct Offers pilot | silent — checked | `rugsusa.com` (DDG site: query, "Google AI") — no relevant results, 2026-09-22 |
| Lowe's | home improvement retail | Google Business Agent pilot — `docs/raw/c-google-ucp-merchant-agentic-2026-09-22.md` | silent — checked | `corporate.lowes.com` (DDG site: query, "Google AI Overviews" OR "Business Agent") — no results, 2026-09-22 |
| Michael's | arts/crafts retail | Google Business Agent pilot | silent — checked | `michaels.com` / `newsroom.michaels.com` (DDG site: query, "Google AI") — no relevant results, 2026-09-22 |
| Poshmark | resale/marketplace | Google Business Agent pilot | silent — checked | `poshmark.com` / `investors.poshmark.com` (DDG site: query, "Google AI") — no relevant results, 2026-09-22 |
| Reebok | apparel/footwear | Google Business Agent pilot | silent — checked | `reebok.com` (DDG site: query, "Google AI Mode") — no relevant results (only unrelated Google Assistant smartwatch feature), 2026-09-22 |
| Urban Outfitters | apparel retail (URBN) | Microsoft Copilot Checkout launch partner — cited via `docs/raw/c-vendor-census-c6-2026-09-22.md` §2, sourcing `c-microsoft-copilot-checkout-brand-agents-2026-09-22.md` | silent — checked | `urbn.com` (DDG site: query, "Copilot Checkout" OR Microsoft) — no relevant results, 2026-09-22 |
| Anthropologie | apparel/home retail (URBN) | Microsoft Copilot Checkout launch partner | silent — checked | shares URBN corporate domain with Urban Outfitters — same check, no relevant results, 2026-09-22 |
| Ashley Furniture | furniture retail | Microsoft Copilot Checkout launch partner | silent — checked | `ashleyfurniture.com` (DDG site: query, "Copilot Checkout") — no results; page has its own "Ashley AI Chat" product, unrelated to Microsoft Copilot Checkout, 2026-09-22 |
| Etsy | marketplace | Microsoft Copilot Checkout launch partner | silent — checked | `investors.etsy.com` (DDG site: query, "Copilot Checkout" OR "Microsoft Copilot") — no results from Etsy's own domain (only third-party trade press), 2026-09-22 |

### Priority 3 — the rest (Peec AI, Brandlight, Searchable named logos, sampled to cap)

| Brand | Vertical as named | Vendor / program (Pass 2/3 raw path) | Reads | Brand-side check |
|---|---|---|---|---|
| Chanel | luxury fashion/beauty | Peec AI — `docs/raw/a-peec-customers-2026-09-22.md` | silent — checked | `chanel.com` (DDG site: query, "Peec AI") — no relevant results, 2026-09-22 |
| Axel Springer | media/publishing | Peec AI | silent — checked | `axelspringer.com` (DDG site: query, "Peec AI") — no relevant results, 2026-09-22 |
| ElevenLabs | AI voice tech | Peec AI | silent — checked | `elevenlabs.io` (DDG site: query, "Peec AI") — no relevant results, 2026-09-22 |
| TUI | travel/tourism | Peec AI | silent — checked | `tuigroup.com` (DDG site: query, "Peec AI") — no relevant results (found only unrelated "AI at TUI" content), 2026-09-22 |
| Kimberly-Clark | consumer packaged goods | Brandlight AI — `docs/raw/a-brandlight-customers-2026-09-22.md` | silent — checked | `kimberly-clark.com` (DDG site: query, "Brandlight") — no relevant results, 2026-09-22 |
| LG | consumer electronics | Brandlight AI | silent — checked | `news.lg.com` (DDG site: query, "Brandlight") — no results, 2026-09-22 |
| The Hartford | insurance | Brandlight AI | silent — checked | `thehartford.com` / `newsroom.thehartford.com` (DDG site: query, "Brandlight") — no relevant results, 2026-09-22 |
| Estée Lauder | beauty/cosmetics | Brandlight AI | silent — checked | `elcompanies.com` (DDG site: query, "Brandlight") — no relevant results, 2026-09-22 |
| Samsung | consumer electronics | Brandlight AI | silent — checked | `news.samsung.com` (DDG site: query, "Brandlight") — no relevant results, 2026-09-22 |
| Aetna | health insurance | Brandlight AI | silent — checked | `aetna.com` (DDG site: query, "Brandlight") — no relevant results, 2026-09-22 |
| American Express | financial services | Searchable — `docs/raw/a-searchable-customers-2026-09-22.md` | silent — checked | `about.americanexpress.com` (DDG site: query, "Searchable") — no results, 2026-09-22 |
| Siemens | industrial/engineering | Searchable | silent — checked | `siemens.com` (DDG site: query, "Searchable" AI visibility) — no relevant results, 2026-09-22 |
| Pfizer | pharma | Searchable | silent — checked | `pfizer.com` (DDG site: query, "Searchable" AI visibility) — no relevant results (found only an unrelated job posting referencing generative-AI/SEO skills), 2026-09-22 |
| H&M | apparel retail | Searchable | silent — checked | `hmgroup.com` (DDG site: query, "Searchable") — no relevant results, 2026-09-22 |
| Wayfair | home goods retail | Searchable | silent — checked | `about.wayfair.com` (DDG site: query, "Searchable") — no results, 2026-09-22 |

## Not checked — cap (~107 brands)

Per task cap: every named brand beyond the 59 above is recorded here by vendor source, not individually checked. Grouped by the Pass 2/3 file that named them; vendor/case grade noted where known.

| Source vendor / program (Pass 2/3 raw path) | Brands not checked — cap |
|---|---|
| Searchable, Fools gold-or-screened logos — `a-searchable-customers-2026-09-22.md` | Coach, KPMG, DigitalOcean, BCG, Revlon, Heights, Lottie, Bolt, 1-800-Flowers, Fi, Glenmuir, Amadeus, 1mind, 303, Blackbird |
| Peec AI, testimonial-only — `a-peec-customers-2026-09-22.md` | n8n, Graphite, Glide, Amsive |
| Promptwatch, testimonials + case subjects — `a-promptwatch-customers-2026-09-22.md` | NXT Pharma, Six Group, Center Parcs, Elaboratum, MX2, Scrolling, Bambuu, Schoonenberg, NoNonsense, Octolize, Landytech, Marvia, Everflow, Deepblue Digital, Advise, Wortell, Revisto Marketing, OpenUp, Monks, Crisp |
| Profound, remaining Bronze/Fools gold — `a-profound-customers-2026-09-22.md` | WHOOP, Alchemy, Jordan Digital Marketing, Omnilux, CRS credit API, One Identity, Statsig |
| AthenaHQ, remaining — `a-athenahq-customers-2026-09-22.md` | Popl.co |
| RankPrompt, logo-only — `a-rankprompt-customers-2026-09-22.md` | Mastercard, P&G, 7-Eleven |
| Sitefire, testimonials — `a-sitefire-customers-2026-09-22.md` | BMW, Xtrackers, DWS, Wemolo, Chamber |
| Scrunch, remaining case subjects — `a-scrunch-customers-2026-09-22.md` | Proper Propaganda, Runpod, Clapping Dog Media, AlchemyLeads |
| Locafy, testimonials (unnamed in census, not individually checkable) — `a-locafy-customers-2026-09-22.md` | 8 unnamed real-customer testimonials (names not captured in the census summary) |
| Otterly.AI, remaining case subjects — `a-otterly-customers-2026-09-22.md` | Instant Commerce, Videoloft, plus 9 further teaser-graded/unnamed items |
| AirOps, remaining — `a-airops-customers-2026-09-22.md` | Docebo, Webflow |
| Conductor, AgentStack technology partners (not end-customers) — `a-conductor-launch-2026-09-22.md` | Optimizely, Razorfish, Havas, IBM |
| HubSpot, testimonials/beta users — `a-hubspot-launch-2026-09-22.md`, `a-hubspot-aeo-product-2026-09-22.md` | Sandler, Scrums, Anedot, Fresha (Docebo already listed under AirOps) |
| Yext, testimonials + launch-release case — `a-yext-customers-2026-09-22.md`, `a-yext-launch-2026-09-22.md` | MidFirst Bank, Sorbet, Beltone |
| BrightEdge, remaining identified-not-opened — `a-brightedge-customers-2026-09-22.md` | Arm, Overdrive Interactive |
| Muck Rack, teaser case — `a-muckrack-customers-2026-09-22.md` | Three Rings |
| Quattr, remaining case subjects — `a-quattr-customers-2026-09-22.md` | CloudEagle, Housing.com, Kiteworks |
| Semrush, remaining — `a-semrush-customers-2026-09-22.md` | Coalition Technologies |
| SOCi, roster-clearance evidence — `a-soci-roster-clear-2026-09-22.md` | Batteries Plus |
| Feedonomics, named logos — `c-vendor-census-c6-2026-09-22.md` row 1 | Dell, Logitech, Euro Car Parts, New Balance, Pacsun, Coldwater Creek, Cole Haan |
| Criteo, named case brands — `c-vendor-census-c6-2026-09-22.md` row 2 | Unice, Denon Store, Netshoes |
| Pacvue, named case brands — `c-vendor-census-c6-2026-09-22.md` row 4 | Itsumo, Perdue, Duracell (L'Oréal and Revlon already checked above under other vendors) |
| Kargo, named case brands — `c-vendor-census-c6-2026-09-22.md` row 7 | HP Toast, WeTransfer, CTV Glass, Hershey's, Anytime Fitness, American Eagle |
| Intero Digital, remaining — `f-agency-census-c5-2026-09-22.md` row 3 | Window Well Supply, Sticker Mountain |
| Fire&Spark, testimonial — `f-agency-census-c5-2026-09-22.md` row 5 | Hinge Health |
| Seer Interactive, blocked case reference — `f-agency-census-c5-2026-09-22.md` row 4 | Home Depot (case page itself was Cloudflare-blocked at source, per that file's own pull notes) |

## Caveats

- **Zero corroborations, zero contradictions across 59 brand-side checks.** This is recorded as the finding, matching the `plan.md` survivorship framing: published vendor case studies are not, in this sample, echoed anywhere on the named brand's own newsroom, IR, blog, or careers domain. This is evidence of *absence on the brand side*, not proof the underlying vendor claims are false — a brand's silence on a minor vendor relationship is expected regardless of whether the claim is true.
- Every check in this file used `html.duckduckgo.com/html/?q=site:<domain> <vendor>` as a search substitute (WebSearch budget exhausted per `docs/method/STATE.md`), per this task's explicit allowance to use "DuckDuckGo's HTML endpoint sparingly." DuckDuckGo's site-restricted index is not exhaustive — a true positive could exist on a brand's own domain that this index does not surface. Two brands' checks were followed by a full direct fetch of the specific brand-owned page found (Tinybird, Ramp) to confirm the near-miss was not a corroboration; all others rest on the DDG index result alone.
- Four brand-owned domains could not be conclusively identified within this pull's budget (Aleph, Owings Auto, Activate Digital, Chime) — recorded as `silent — checked` against the best-guess domain, not as a stronger negative claim. A resuming agent with WebSearch budget should re-resolve these four domains first.
- Grading rule 1 (`plan-review-1-2026-09-22.md` §3) was never triggered — no brand-side page was opened that named a result, so no case in this file is `screened — no claim` or graded; every entry is `silent — checked`, which is a distinct status from both.
- No brand named across the ~166-brand universe was excluded from checking because it seemed unimportant — the priority order (Bronze-or-better cases, then Direct Offers/Copilot Checkout/ChatGPT Ads partners, then the rest) is the one specified in the task brief, applied mechanically against the brands as the Pass 2/3 files name them.
- Nothing in this file comes from memory. Every brand name traces to the cited Pass 2/3 raw file; every check result traces to a fetch made 2026-09-22.
- This cluster did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com, or amazon.com's assistant. No Chrome extension, no Playwright browser — fetch and DuckDuckGo html only, per task boundary (both browser slots held by other agents).
- Oldest pull depended on: 2026-09-22 — every source Pass 2/3 file and every brand-side check in this file was made or re-cited today.
