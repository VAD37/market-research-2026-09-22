# Job postings — LinkedIn Jobs, Indeed (blocked), Upwork (blocked), Freelancer.com — skincare and beauty × AI visibility/GEO/AEO/agentic commerce

```yaml
source:          LinkedIn Jobs (linkedin.com/jobs); Indeed (indeed.com, blocked); Upwork (upwork.com, blocked); Freelancer.com
url_or_doc_id:   linkedin.com/jobs/search/?keywords=...; linkedin.com/jobs/view/ai-product-owner-agentic-commerce-at-e-l-f-beauty-4460992848; indeed.com/jobs?q=...; upwork.com/nx/search/jobs/?q=...; freelancer.com/jobs/generative-engine-optimization/; freelancer.com/jobs/search/?keyword=AI+visibility+beauty
published:       job posting "posted 2 weeks ago" relative to pull date (E.L.F. BEAUTY posting); other pages undated live listings
pull_date:       2026-09-22
pull_method:     browser extension (MCP_DOCKER Playwright, dedicated new tab, tab index 2 — tabs 0 and 1 belonged to other concurrent agents and were not touched)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default per demand-signals.md S1 ("3, employer's own posting") for the LinkedIn postings opened at full text (the E.L.F. BEAUTY posting); listing-page snippets without the full posting opened are not independently tiered above the search-result level
source_label:    company-stated
lane:            F
sub_market:      organic recommendation; agentic commerce
engine:          n/a — the posting itself names ChatGPT, Perplexity, Google AI Overviews, Copilot, Claude as the AI assistants its work targets
metric_kind:     none
supersedes:      none
captured:        job-search-result card lists (title + employer, up to 25 per query) via DOM scrape; one full posting (E.L.F. BEAUTY "AI Product Owner, Agentic Commerce") captured in full including disclosed base-pay range
```

## Query — verbatim

LinkedIn Jobs (`linkedin.com/jobs/search/?keywords=<query>&location=`), each run 2026-09-22, US location filter left blank (defaults to United States per page title):

| Query | Result count shown | Notes |
|---|---|---|
| `generative engine optimization beauty` | "4,000+" | LinkedIn's saturation display, not an exact count |
| `"generative engine optimization" beauty` | "4,000+" | Identical result set and count to the unquoted query — quoting is not honored as an exact-phrase operator by LinkedIn's job search |
| `"AEO" OR "GEO" skincare OR beauty OR cosmetics` | "10,000+" | Token-OR matching confirmed — results dominated by generic beauty-industry roles (sales, supply chain, creative) unconnected to AI visibility |
| `GEO specialist skincare small business` | "6,000+" | No SMB-beauty GEO/AI-visibility posting found in the top 20 |

Indeed: `indeed.com/jobs?q=%22generative+engine+optimization%22+beauty&l=` — page title "Blocked - Indeed.com" under the browser extension (not just plain fetch's 403). No content reached.

Upwork: `upwork.com/nx/search/jobs/?q=generative%20engine%20optimization%20beauty` — Cloudflare "Just a moment..." interstitial persisted after a 4-second wait under the browser extension. No content reached.

Freelancer.com: `freelancer.com/jobs/generative-engine-optimization/` (the platform's own GEO skill-tag category page) and `freelancer.com/jobs/search/?keyword=AI%20visibility%20beauty` (open keyword search) — both HTTP 200, extension-free.

## Verbatim

**E.L.F. BEAUTY — "AI Product Owner, Agentic Commerce"** (full posting opened), `linkedin.com/jobs/view/ai-product-owner-agentic-commerce-at-e-l-f-beauty-4460992848`, posted "2 weeks ago" (relative to 2026-09-22 pull), "116 applicants":

> "In our Fiscal year 26, we had net sales of $1.6 Billion and our business performance has been nothing short of extraordinary with 7 consecutive years of net sales growth... We're hiring an AI Product Owner, Agentic Commerce to grow e.l.f.'s presence and performance across emerging agent-driven shopping channels — from AI assistants and answer engines to conversational and agentic checkout experiences... You'll work closely with our AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization) team to increase e.l.f.'s visibility, share-of-answer, and citations across generative search and AI assistants (ChatGPT, Perplexity, Google AI Overviews, Copilot, Claude)... Drive Agentic visibility with the AEO/GEO team — Partner with AEO/GEO to grow e.l.f.'s visibility, share-of-answer, and citations across generative search and AI assistants... Co-build measurement for agentic visibility (citation tracking, share-of-answer, sentiment by engine) and tie it to commerce outcomes."

Disclosed base pay range (page top-card field, distinct from the body text above): **"Base pay range $110,000.00/yr - $140,000.00/yr"**.

Requirements excerpt: "5-10 years of relevant experience... Hands-on experience in at least one (ideally more) of: AI products, digital/e-commerce commerce, or AEO/GEO/SEO... Preferred: Direct experience with Agentic Commerce, AEO, GEO, or AI-driven search/discovery (in-house or at a platform/agency)... Background in beauty, retail, consumer goods, or high-velocity DTC/e-commerce."

**Other beauty-employer postings surfaced** (title | employer, from search-result cards, not opened to full text): "Sr Manager, AI Platform Architecture | Ulta Beauty"; "Staff Machine Learning Engineer | The Estée Lauder Companies Inc."; "VP, Data & AI, Value Chain | The Estée Lauder Companies Inc."; "AVP, Head of AI Solutions | L'Oréal"; "AI Analyst (LA) | Pixi Inc." — none of these titles themselves name AI visibility, GEO, or AEO (general AI/ML/data roles); not counted as qualifying S1 hits, listed here for completeness only.

**Non-beauty GEO/AEO-titled postings surfaced in the same searches** (for contrast, not counted toward this vertical): "Senior Director, Generative & Answer Engine Optimization (GEO/AEO) | Eli Lilly and Company" (pharma); "Senior Director, Generative & Answer Engine Optimization (GEO/AEO) | BioSpace" (same posting relayed); "SEO/GEO Manager | Physician's Choice®" (supplements, high-CPA regulated vertical, not this one).

Freelancer.com, GEO category page (`freelancer.com/jobs/generative-engine-optimization/`), full listing: "1 jobs found... Web3 AEO/GEO Citation Boost, 1 day left, Verified... I'm working on visibility for Pryai ($PRY) on the TON blockchain... $89 Avg Bid, 27 bids." The one job in this category is a Web3/cryptocurrency project, not beauty.

Freelancer.com, open keyword search (`freelancer.com/jobs/search/?keyword=AI%20visibility%20beauty`): "352 jobs found" — top result "LoL Companion App with AI Coaching" (a League of Legends gaming tool), confirming broad token-OR matching, not a genuine beauty-AI-visibility freelance market.

## Pull notes — mechanical only

- This cluster held the Playwright browser slot in a dedicated new tab (tab index 2 of 3 open tabs); tabs 0 (`courtlistener.com` docket, another agent's page) and 1 (a LinkedIn Pulse article, another agent's page) were left untouched throughout.
- LinkedIn's displayed result counts ("4,000+", "6,000+", "10,000+") are confirmed saturation/cap displays, not literal counts — verified by identical counts returned for quoted-vs-unquoted variants of the same query.
- Indeed blocked the browser-extension request outright with a "Blocked - Indeed.com" interstitial, a stronger block than the plain-fetch 403 recorded in `channels.md` C34 — recorded as `unknown — checked indeed.com 2026-09-22, blocked (browser extension and plain fetch both)`.
- Upwork's Cloudflare challenge did not clear after a 4-second wait under the browser extension — recorded as `unknown — checked upwork.com 2026-09-22, Cloudflare challenge not cleared`. No further retry (e.g., longer wait, interactive challenge-solving) was attempted within this cluster's time budget.
- No SMB- or mid-market-tagged AI-visibility/GEO/AEO job posting for a skincare-or-beauty employer was found in any LinkedIn query run this pull; the one qualifying full-text hit (E.L.F. BEAUTY) is Enterprise-banded by the posting's own disclosed net-sales figure ($1.6B, per `demand-signals.md`'s revenue fallback band, over $1B = Enterprise).
- No login was used on LinkedIn (anonymous/logged-out search); per `channels.md` C33, deeper paging past the visible result cards needs a login and was not attempted.
