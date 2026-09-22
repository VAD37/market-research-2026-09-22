# LinkedIn Jobs — S1 job postings naming AI visibility / GEO / AEO / AI search, high-CPA regulated vertical

```yaml
source:          LinkedIn Jobs, public (logged-out) search and individual posting pages
url_or_doc_id:   www.linkedin.com/jobs/search/?keywords=<query> (multiple, see Queries below); individual www.linkedin.com/jobs/view/<slug> pages for the five fully opened postings
published:       postings dated per LinkedIn job-id (undated on the public page beyond "posted X ago"; job ids and content as served 2026-09-22)
pull_date:       2026-09-22
pull_method:     fetch (direct curl, no browser extension, no login) — per task scope this agent holds no Chrome extension slot
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default for S1 — job board / employer's own posting content served through LinkedIn's public search and view pages
source_label:    company-stated
lane:            F
sub_market:      organic recommendation (every qualifying posting names SEO/GEO/AEO/AI-search functions; none names paid placement or agentic-commerce marketing roles — see Negative results below)
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        search-result listing pages (title/company/location fields only, via regex extraction of the served HTML) for each query below; full posting body text (via the `description__text` block) for the five postings opened in full
vertical:        high-CPA regulated — insurance and supplements sub-verticals qualify per the postings' own text; no qualifying posting found for the credit-card sub-vertical (see Negative results)
cell:            organic recommendation / enterprise — Cigna ("Enterprise Technical Search Lead/Analyst", explicit); organic recommendation / unassigned — GEICO, Amica Insurance, Embrace Pet Insurance, Insurify, Juice Plus+ Company, Simply Business (none of these postings states the employer's own headcount or revenue in the captured text; see per-posting notes for qualitative scale language)
query:           see Queries table below, verbatim
```

## Access note

LinkedIn's public jobs search (`linkedin.com/jobs/search/?keywords=`) returns HTTP 200 to an anonymous, unauthenticated `curl` request with no browser extension — consistent with `channels.md` C33's recorded access code ("200 anonymous, deeper paging needs login"). Indeed and Upwork both returned 403 to the same method (see `f-signal-hr-S1-indeed-upwork-2026-09-22.md`). No login, no cookies, no JavaScript rendering was used for any pull in this file.

**LinkedIn's public search does not reliably honour quoted exact-phrase matching.** A quoted query such as `"generative engine optimization"` returned generic large-employer ML/LLM-engineering postings (Airbnb, Capital One, JPMorganChase, Pinterest, Mastercard) that use "generative," "engine," and "optimization" as separate tokens in unrelated technical titles ("Principal Software Engineer - LLM Optimization," "Senior Machine Learning Engineer- Generative AI"). Adding an explicit marketing/discipline term (SEO, AEO, GEO, "AI Search") alongside a vertical token sharply improved precision. This defect is recorded, not worked around by a different tool, per task scope.

## Queries — search-listing pulls, title/company pairs extracted verbatim from the served HTML

| # | Query (verbatim `keywords=` value, URL-decoded) | LinkedIn's own displayed count | Qualifying hits (title, company) | Non-qualifying pattern in the same results |
|---|---|---|---|---|
| Q1 | `generative engine optimization insurance` | 8,000+ | none in first page | Generic AI/ML engineering roles at GEICO, Guidewire Software, FurtherAI, EverQuote, Mercury Insurance, PURE Insurance, WithCoverage, Vouch Insurance, Guardian, Crum & Forster — all engineering, not marketing/visibility |
| Q2 | `"generative engine optimization"` (quoted) | 10,000+ | none in first page | Same defect as above; Airbnb, Tern, Capital One, Bubble, JPMorganChase, The Home Depot, Qumis, Outdoorsy, Mastercard, Vouch Insurance — all engineering |
| Q3 | `"AI visibility"` (quoted) | 3,000+ | none | OpenAI, Character.ai, Canon USA, Cohere, Fiddler AI — AI-safety/research roles, no vertical match |
| Q4 | `answer engine optimization` | not captured | "SEO/GEO Manager" at Mercury; "Senior SEO/AEO Manager – Remote"; multiple marketing-function hits, none insurance/card/supplement-tagged in first page | Boca Recovery Center (addiction treatment, not this vertical), Plante Moran (accounting), Opendoor (real estate) |
| Q5 | `AEO marketing` | not captured | none vertical-qualifying | Safelite, LEGO Group, Enterprise Mobility, Valvoline, Kohler — general marketing roles, no vertical match |
| Q6 | `SEO/AEO insurance` | not captured | **"SEO & AI Search Content Writer – Commercial Insurance" — GEICO**; **"SEO Generative/AI Search Analyst" — Amica Insurance**; **"Organic Search / SEO Manager" — Embrace Pet Insurance**; **"Lead Analyst, Technical Search (SEO/AEO/GEO)" — The Cigna Group**; "SEO Content Marketer — Fintech / Insurtech (US Remote)" (employer not individually confirmed this pull) | U Trust Insurance Agency, Jet Insurance Company, Evlo AI, Feathery, ADP — present in the same result set, roles not opened |
| Q7 | `GEO insurance marketing` | not captured | "AEO Outreach Manager" — GEICO; "VP, Marketing (P&C Insurance)" — State Farm (title/company pairing not individually re-verified — see caveats); "Manager - Marketing, P&C Insurance" — AAA Mountain West Group | Generali Global Assistance, Guidewire Software (Senior Product Marketing Manager, ClaimCenter — a vendor to insurers, not an insurer itself) |
| Q8 | `SEO AI search credit card` | 4,000+ | **"Senior Manager, AI Search & Discovery (GEO/AEO)" — Insurify** (insurance-comparison platform, not a card issuer; surfaced because "AEO & SEO" query also returned "Head of AEO & SEO" at Stripe) | Stripe, Mercury, Step, Feathery, Acrisure, Credit One Bank — no qualifying card-issuer marketing hit; Credit One Bank's listed role in this result set was engineering-only (see S1 cards sub-vertical negative result) |
| Q9 | `AEO GEO credit card` | not captured | **none** | American Express — every returned title is Audit, Risk Management, Compliance, or Business Development; zero marketing/visibility roles |
| Q10 | `generative engine optimization credit card` | not captured | **none** | Capital One, Credit Acceptance, interface.ai, Stripe, Caribou Financial, JPMorganChase — all ML-engineering or credit-risk-modeling titles |
| Q11 | `AI search visibility credit card` | not captured | **none** | ClarityPay, Credit One Bank, Credit Acceptance, One Park Financial, Payactiv, Capital One — Data Science/AI/Credit-modeling titles only |
| Q12 | `AEO GEO supplement brand` | not captured | none | Antelope, Elanco, Arcaea, Grande Cosmetics, SeneGence — beauty/pet-pharma brand-management roles, not GEO/AEO-titled |
| Q13 | `SEO AI search vitamins` | not captured | "Head of Search and AI Visibility" / "Head of Search & AI Visibility" (company pairing not individually re-verified) | FIGS, Vagaro, KnowBe4, Pet Honesty ("Amazon SEO Manager" — Amazon-marketplace SEO, not GEO/AI-answer visibility) |
| Q14 | `generative engine optimization wellness` | not captured | **"Senior Manager, Growth Marketing & Search" — The Juice Plus+ Company** (confirmed by full posting, see below) | "Growth Manager" — Dr. Berg Nutritionals (opened in full; body text names no GEO/AEO/AI-search term — false positive, see below) |
| Q15 | `small business insurance agency GEO AI search` | not captured | **"Senior Manager, SEO & GEO" — Simply Business** (confirmed by full posting, see below) | AACI Group ("General Manager, AI-Native Insurance Agency" — a company built around AI, not a GEO/marketing-function posting), Agenzee, Applied Systems |
| Q16 | `independent insurance agent AI visibility` | not captured | none | Indicium AI, Insurify (different role than Q8's — Enterprise Account Executive, not marketing), Anthropic — no qualifying marketing/visibility posting |
| Q17 | `DTC supplement brand GEO AEO` | not captured | none | Farmasi, TRIP, Physician's Choice, iHerb, Tarte Cosmetics, Nutricost — Brand/Creative/Sales roles, no GEO/AEO term in title |
| Q18 | `ChatGPT ads insurance` | not captured | GEICO's Commercial Insurance posting recurs (already counted at Q6) | AIG, AAA Life Insurance Company, Afficiency, State Farm — GenAI/automation engineering, no paid-placement marketing role |
| Q19 | `AI advertising credit card` | not captured | **none** | Credit One Bank, Block, Capital One, Credit Acceptance, Intuit — AI/ML engineering (incl. "Senior AI Scientist - Credit Karma") |
| Q20 | `agentic commerce insurance` | not captured | **none** (marketing) | Assured, Travelers, GEICO, PURE Insurance — "Senior Copywriter, AI & Category Narrative" (Assured) is the closest hit; role scope not opened, not confirmed as agentic-commerce-specific |
| Q21 | `agentic checkout supplement` | not captured | **none** | Physician's Choice, Just Ingredients, "Agentic Commerce Startup" (unnamed), Create Wellness, quip. — Creative/Brand/Growth titles, none GEO/AEO/agentic-commerce-marketing-specific |

## Five postings opened in full (body text captured via the `description__text` block)

### 1. GEICO — "SEO & AI Search Content Writer – Commercial Insurance"

URL: `https://www.linkedin.com/jobs/view/seo-ai-search-content-writer-%E2%80%93-commercial-insurance-at-geico-4461925761`

> "GEICO is a member of the Berkshire Hathaway family of companies and one of the largest auto insurers in the United States." … "GEICO is seeking a skilled SEO & AI Search Content Writer to join our team with a focus on the Commercial Insurance sector." … "this role will focus on advancing GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization) initiatives, ensuring content is structured to meet modern search intent and deliver value across emerging search platforms." … "Reporting to the Director of Marketing Strategy, SEO, the SEO & AI Search Content Writer will operate in a collaborative environment…"

Vertical: insurance (commercial insurance line, explicit). Buyer size: no numeric headcount or revenue stated on the captured page; the posting's own qualitative language ("one of the largest auto insurers in the United States," Berkshire Hathaway subsidiary) is company-stated scale language, not a headcount/revenue figure per `demand-signals.md`'s boundary rule — recorded `unassigned` per the rule's instruction that an unmappable statement is not guessed into a band.

### 2. Insurify — "Senior Manager, AI Search & Discovery (GEO/AEO)"

URL: `https://www.linkedin.com/jobs/view/senior-manager-ai-search-discovery-geo-aeo-at-insurify-4421188612`

> "Insurify is one of America's fastest-growing MIT FinTech startups… Top 100 InsurTech company… $130M total funding… We're looking for a Senior Manager, AI Search & Discovery (GEO) to help build and scale Insurify's GEO/AEO program, improving how Insurify and sub-brands are discovered, described, cited, and recommended across AI-powered search, generative answer engines, and emerging organic discovery surfaces… Reporting to the Director of Product SEO, you'll manage the day-to-day operating system for AI search visibility, including prompt monitoring, reporting, source-gap analysis…"

Vertical: insurance (comparison/InsurTech platform, explicit "Top 100 InsurTech company"). Buyer size: `unassigned` — "$130M total funding" is disclosed but is not a headcount or revenue figure per the boundary rule; no employee count stated in the captured text.

### 3. The Cigna Group — "Lead Analyst, Technical Search (SEO/AEO/GEO)"

URL: `https://www.linkedin.com/jobs/view/lead-analyst-technical-search-seo-aeo-geo-at-the-cigna-group-4464204096`

> "Cigna is seeking an **Enterprise** Technical Search Lead/Analyst (SEO/AEO/GEO) to join the Paid Media Center of Expertise within the Marketing and Communication organization… As the enterprise subject matter expert for Technical SEO, Answer Engine Optimization (AEO), and Generative Engine Optimization (GEO), this role will drive AI readiness, technical governance, automation, and innovation… Lead enterprise Technical SEO, AEO/GEO strategy across The Cigna Group's priority brands and digital properties… develop scalable solutions that improve search performance across a large enterprise ecosystem."

Vertical: insurance (health/life insurer). Buyer size: **Enterprise — source's own wording**, the only posting in this file that states its own band directly ("Enterprise Technical Search Lead/Analyst," "the enterprise subject matter expert," "a large enterprise ecosystem"). Cell: organic recommendation / enterprise, high-CPA regulated (insurance).

### 4. The Juice Plus+ Company — "Senior Manager, Growth Marketing & Search"

URL: `https://www.linkedin.com/jobs/view/senior-manager-growth-marketing-search-at-the-juice-plus%2B-company-4468597175`

> "Juice Plus+ is seeking a commercially minded, data-driven Senior Manager, Growth Marketing & Search to lead two of our most important growth engines: Paid Media (USA) and Organic Search (Global)… this position will help shape how Juice Plus+ appears across Google Search, AI Overviews, ChatGPT, Gemini, Perplexity, and emerging answer engines, ensuring the brand remains visible and competitive in the future of search."

Vertical: supplements (Juice Plus+ is a global nutritional-supplement and "Partner" network-marketing brand). Buyer size: `unassigned` — "Organic Search (Global)" and "Paid Media (USA)" state geographic scope, not headcount/revenue; no numeric figure in the captured text.

### 5. Simply Business — "Senior Manager, SEO & GEO"

URL: `https://www.linkedin.com/jobs/view/senior-manager-seo-geo-at-simply-business-4434883629`

> "Simply Business is a digital insurance brokerage that specializes in one thing: protecting the businesses our customers are working hard to build… simplifying the insurance-buying process for all small businesses… Founded in the UK in 2005, Simply Business is an insurtech pioneer with nearly 20 years of experience supporting small businesses… Simply Business is seeking a visionary Senior Manager, SEO & GEO to lead our search strategy into the next era… Salary Range $114,700.00 - $189,200.00"

Vertical: insurance (a digital insurance brokerage/marketplace whose own customers are small businesses — **note**: this describes Simply Business's customer segment, not Simply Business's own employer size; per `demand-signals.md` the buyer-size band applies to the entity budgeting the AI-visibility role, i.e. Simply Business itself, not its SMB customers). Buyer size: `unassigned` — no headcount/revenue for Simply Business itself is stated in the captured text; the disclosed salary band ($114,700–$189,200) is compensation, not a price paid for a vendor/tool (not an S11 observation).

## False positive, recorded and discarded

**Dr. Berg Nutritionals — "Growth Manager"** (`https://www.linkedin.com/jobs/view/growth-manager-at-dr-berg-nutritionals-4464590267`, matched by query `generative engine optimization wellness`). Full body text opened: the role is a CRO/testing-strategy "Growth Manager" role ("own our testing strategy across the entire customer journey… map key conversion touchpoints, build and evolve the testing roadmap"). No occurrence of GEO, AEO, "generative engine," "answer engine," "AI search," or "AI visibility" anywhere in the captured description. Discarded — not counted as a qualifying S1 hit, per `trust-rubric.md`'s "percentage/claim with no base" discipline applied to keyword matches: a term match in the query is not a term match in the source.

## Negative result — credit-card sub-vertical

Across nine card/issuer-targeted queries (Q8, Q9, Q10, Q11, Q19, plus card-adjacent tokens inside Q1–Q3), the only companies surfaced were American Express, Capital One, Credit One Bank, Credit Acceptance, JPMorganChase, Mastercard, Block, Stripe, interface.ai, and Caribou Financial — and in every case the returned titles were Audit, Risk Management, Compliance, Credit/Fraud Modeling, or general ML/AI engineering, never a marketing function naming SEO, AEO, GEO, or AI-search visibility. **`none — checked "AEO GEO credit card", "generative engine optimization credit card", "AI search visibility credit card", "AI advertising credit card", "SEO AI search credit card" 2026-09-22`** for the credit-card sub-vertical specifically. Insurance and supplements both cleared with qualifying hits; cards did not.

## Caveats

- LinkedIn's public search returns a self-reported result count ("X,000+") that is a broad relevance count across all keyword tokens, not a phrase-exact count; it is recorded where captured but is not treated as a precise S1 unit ("postings per period, per employer size band" per `demand-signals.md`) — no query in this file supports a defensible per-period count.
- Buyer-size band could not be mapped for five of the six qualifying postings (Cigna is the exception). This is the general LinkedIn-public-page limitation: company headcount/size badges are not present on the anonymous, logged-out view used here (no login was used, per task scope and `channels.md` C33's own access note that "deeper paging needs login").
- Title/company pairings in the search-listing table (Q1–Q21) were extracted by parallel array position from the served HTML for titles and a separate `hidden-nested-link` array for companies; where a pairing is not individually re-verified against the specific posting URL, this is stated inline ("pairing not individually re-verified").
- Every posting captured is a live, open requisition as served 2026-09-22; none is dated on the public page beyond a relative "posted X ago" indicator not captured here.
