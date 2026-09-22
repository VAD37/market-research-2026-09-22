# Flow Agency — B2B AEO agency service page naming SaaS clients

```yaml
source:          Flow Agency (flow-agency.com)
url_or_doc_id:   https://www.flow-agency.com/ ; https://www.flow-agency.com/services/b2b-aeo-agency/
published:       undated — no date on page (agency marketing site)
pull_date:       2026-09-22
pull_method:     fetch (curl with a browser User-Agent; no browser extension needed; seed found via a DuckDuckGo HTML search for `"generative engine optimization" OR "AEO" agency "B2B SaaS" pricing`)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default for S6 existence ("3 existence / 6 framing") — the agency's own dedicated service page names SaaS as a target client type; no list price is disclosed on the page, so the "6 on framing" branch (an unpriced marketing claim) applies to the qualitative claims within it
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        homepage title/meta description; full h1 and body-paragraph text of the dedicated `/services/b2b-aeo-agency/` page (CSS/animation markup stripped)
```

## Verbatim

Homepage (`flow-agency.com`) `<title>`: "Flow Agency. Our Expertise. Your B2B Success." Meta description: "B2B marketing agency for SaaS startups and professional services. Custom strategies, senior..." [truncated in the fetched meta tag]. Body text: "Growth marketing agency for B2B SaaS startups. Custom strategies, senior..." and "...meaningful traffic and conversions for B2B startups. As a boutique agency, we offer..." and "...boutique agency specialized in bespoke B2B marketing for SaaS startups and professional..." Award citation found in the page's structured data: `"award":["Best Use of Search B2B (SEO) - European Search Awards 2023..."`. Homepage nav includes a menu item: "AEO and LLM optimization" linking to `https://www.flow-agency.com/services/b2b-aeo-agency/`.

Dedicated service page (`/services/b2b-aeo-agency/`) `<title>`: "B2B AEO Agency for SaaS and Service Providers - Flow Agency." H1: "The B2B AEO agency to help you [gain] visibility and citations in Large Language Models (LLM) with Answer Engine Optimization (AEO)." Body paragraphs (script/CSS stripped, verbatim text):

> "You can no longer rely on traditional SEO alone to win organic traffic. AI-powered platforms like ChatGPT, Perplexity, and Google AI Overviews have changed how your customers research purchasing decisions. If you want them to find you, your marketing approach needs to change too."

> "We create a bespoke AEO strategy tailored to your go-to-market approach, business goals, and messaging."

> "We have helped 100+ B2B startups and service providers increase their SEO and AEO-driven revenue by scaling their visibility in organic and AI-driven search results."

> "While only a small percentage of your target audience is actively looking for your solutions, these are the people with the highest buying intent. Prospects who've clicked on links leading to Flow Agency clients' websites in AI-generated answers convert at 0.7% on average and 2.3% at the top end."

> "Your prospects are using LLM platforms like ChatGPT, Copilot, and Claude throughout their buying journey. From initial research to decision-making, generative AI helps them answer questions, find solutions, and make a final decision."

No `$`, `€`, "pricing," "starting at," "per month," or "retainer" string was found anywhere on either fetched page — no list price or rate card is disclosed on-page.

Founder/company-scale corroboration (via DuckDuckGo HTML search-result snippets, not independently opened): "After establishing her boutique B2B marketing firm, Flow Agency, in 2018, Viola has grown the business into a 15-person team and has worked with over 130 clients worldwide" (source snippet attributed to a Flow Agency bio page); a third-party directory (GEOToolHub, via the same snippet search) independently describes Flow Agency as "a boutique growth marketing agency founded in 2018 by Viola Eva... helping B2B SaaS startups and professional services scale traffic and conversions."

## Pull notes — mechanical only

- `flow.agency` (the bare `.agency` TLD) redirects to a client-rendered `/lander` page with no static content (a 114-byte JS-redirect stub); the working domain is `flow-agency.com` (`www.` prefix), reached directly without redirect trouble.
- No list price is disclosed on either fetched page — recorded per S6's own bias line ("A list price is an asking price, never a purchase") as an existence-only signal (tier 3), not a priced one; had a price been present it would still only be an asking price, never a willingness-to-pay observation (`templates/customer-segment.md`).
- Buyer size: the page addresses "B2B startups" and "SaaS startups" as its client type in its own words, which is a description of the agency's **target customer**, not a specific named client with a stated headcount — per `demand-signals.md`'s cell-attribution rule ("nothing is inferred from a vendor's target-customer page — that is a sell-side claim"), this is **not** mapped to a specific buyer-size cell. It is recorded at the vertical/sub-market level (B2B SaaS, organic recommendation) with buyer size `unassigned`, and flagged that "startups" in the agency's own language skews toward the SMB end without being a stated headcount.
- The 0.7%/2.3% conversion-rate figures are an unattributed, unbacked claim (no client name, no baseline, no n) — noted here for completeness but explicitly **not** treated as S11 (disclosed price paid) or as case-study evidence; it does not carry the seven-item evidence bar and was not run through Pass 4's grading, which is out of this cluster's scope.
- The listicle/roundup search results that surfaced Flow Agency (`"Top 8 Answer Engine Optimization (AEO) Agencies in 2026"`, `"The 10 Best Generative Engine Optimization (AEO) Agencies of 2026"`, and similar "Best AEO Agencies for B2B SaaS" titles) are tier-7 listicles per `trust-rubric.md` and were used only as a discovery pointer to Flow Agency's own domain, never pulled or cited as a source themselves.
