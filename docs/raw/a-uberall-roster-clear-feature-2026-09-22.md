# Uberall — three-limb roster rule check (held name), and GEO Studio feature page

```yaml
source:          Uberall (uberall.com, company-stated); North Data GmbH (northdata.com, filed — German commercial register aggregator)
url_or_doc_id:   https://uberall.com/en-us/products/geo-studio; https://uberall.com/en-us/company/news-press/uberall-launches-first-generative-engine-optimization; https://www.northdata.com/Uberall+GmbH,+Berlin
published:       undated (product page); 2025-12-16 (GEO Studio launch press release, per news-index date); North Data register data spans multiple dated filing events (capital changes, managing-director changes), most recent entries undated on the captured page
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default for the North Data source — filed (German Handelsregister / commercial register, aggregated); product page and press release are table default 3 (platform primary / company-stated)
source_label:    filed (North Data); vendor-reported (product page); company-stated (press release)
lane:            A
sub_market:      incumbent bundling
engine:          ChatGPT (OpenAI), Perplexity, Google AI Overviews, Google AI Mode, Gemini, Claude (Anthropic), Copilot (Microsoft), Grok (xAI), DeepSeek — nine named
metric_kind:     visibility
supersedes:      none
captured:        full text of the GEO Studio product page (feature, how-it-works, FAQ, testimonials) and the North Data register entry (company identity and capital-history fields)
feature:         "GEO Studio" — Uberall's AI-visibility product, launched in collaboration with AthenaHQ (an already-rostered organic-recommendation vendor from this project's own roster, `a-vendor-roster-2026-09-22.md` row 8)
```

## Verbatim

### Roster-rule evidence — North Data (German commercial register aggregator)

"uberall GmbH, Berlin, Germany, District Court of Charlottenburg (Berlin) HRB 141620 B: Network, Financial information." Register-change history includes capital figures from €47,490 up through €120,652 and multiple managing-director changes over time, named verbatim: "Managing Director: Brad Anthony Foy · No longer Managing Director: Florian Hübner"; "Managing Director: Fabrice Lévy"; "No longer Managing Director: David Federhen." [note: this page lists a long capital/register-change history table; only representative entries are reproduced here, not the full table]

**Roster-rule determination: Uberall clears limb (a) (arguably also limb (b) if a German Handelsregister entry is treated as equivalent to the UK Companies House filings this roster already tiers at 2).** Two independent, non-listicle, differently-published sources: (1) the G2 category listing already on record from `a-vendor-roster-2026-09-22.md` §3a ("Uberall | g2.com/categories/answer-engine-optimization-aeo?page=2, read 2026-09-22 (4.4/5, 237 reviews)"); (2) this North Data German commercial-register aggregation, an independent registry source distinct from both G2 and uberall.com, carrying a specific court-registered entity number (HRB 141620 B). **Uberall moves from held to rostered.** Multiple other channels were checked and found blocked or unhelpful this session: `getlatka.com/companies/uberall.com` (404), `crunchbase.com/organization/uberall` (403), `tracxn.com` (404 on guessed URL), `owler.com/company/uberall` (403), `businesswire.com` search (403), `prnewswire.com` search (0 hits for "Uberall AI Search"), AthenaHQ's own `athenahq.ai/blog` and `athenahq.ai/integrations` pages (no mention of Uberall found on the pages reached), AMPECO's `ampeco.com/blog/category/news/` (no mention of Uberall found on the one page of the category reached) — recorded for completeness though not needed once North Data cleared the rule.

### GEO Studio — product page (condensed; nav/footer chrome elided per this cluster's convention)

"GEO Studio — Your Brand Is Getting Erased by AI. Fix It. GEO Studio shows you exactly how ChatGPT, Gemini, Perplexity, and Google AI Overviews talk about your brand and locations — and gives you the tools to change it." Stats shown: "$750B+ in consumer spend expected to flow through AI-driven search by 2027"; "50% of Google searches are now powered by AI"; "44% AI Citation Lift by using Structured data"; "57% Google AI Overviews appearance in the SERP"; "45% of consumers now use AI tools for local recommendations, up from 6% just one year ago." [note: these are generic category-level stats, not tied to one customer/date/baseline — not graded as case evidence]

"How It Works — From invisible to unmissable in four steps: 1. Connect your locations... 2. Audit your AI presence — Our system runs thousands of AI queries across all major models to establish your baseline visibility, citation rates, and competitive position. 3. Get your action plan... 4. Watch your score rise — Apply recommendations in one click, then track your AI Visibility Score improve in real time."

Named customer testimonials (real brands, qualitative, no quantified metric): Manuela Fuchs, Edeka ("GEO Studio was the ideal entry point into AI optimization for us..."); Audika France ("Before using GEO Studio, we had no way to know which brand attributes AI models associated with Audika..."); Amparo Gil, Pizza Hut ("Having a partner like Uberall is an extension of our team..."). **Not graded — no quantified before/after metric in any of the three; screened only.**

### FAQ (method and pricing disclosure)

"How does GEO Studio work as an AI visibility tool? GEO Studio scans your brand across nine AI models — including ChatGPT, Gemini, Perplexity, Claude, Copilot, and DeepSeek — using thousands of prompts. It measures share of voice, citation rate, and the brand traits AI assigns to you..."

"What AI models does GEO Studio track? GEO Studio currently tracks brand visibility across nine AI models: **ChatGPT (OpenAI), Perplexity, Google AI Overviews, Google AI Mode, Gemini, Claude (Anthropic), Copilot (Microsoft), Grok (xAI), and DeepSeek.** New models are added as they gain market share."

"Where do the prompts in GEO Studio come from? GEO Studio uses seed prompts you define plus semantically similar variants the platform discovers automatically. You control what to track... Prompt data includes estimated monthly search volume and can be organized by topic, persona, and geography."

"Can GEO Studio track AI visibility at the individual location level? Yes, GEO Studio breaks down AI visibility by location..."

"How does GEO Studio pricing work? GEO Studio uses a usage-based credit model. You purchase a monthly credit package based on how much analysis you want to run. Credits are consumed as you generate insights... Unused credits can roll over or be banked, and you can add more credits at any time." **No dollar figure given for the credit package price on this page.**

## Pull notes — mechanical only

- All pages fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML.
- **Prompt-set/n/method disclosure answer for Uberall: partial.** N is disclosed qualitatively ("thousands of prompts," "runs thousands of AI queries") but not as an exact figure; the method is disclosed (customer-seeded prompts expanded algorithmically by the platform) but there is no fixed, vendor-wide composite-score prompt set to disclose in full — same customer-configured pattern as Quattr and SE Ranking in this cluster.
- Uberall's US mailing address is given elsewhere on the site (San Francisco, per a page captured incidentally during the roster-rule search, see `a-uberall-pricing-2026-09-22.md`'s pull notes) while its registered legal entity found via North Data is German (Berlin) — both recorded, not reconciled; likely a US commercial/sales entity alongside the original German GmbH.
