# SE Ranking — three-limb roster rule check (held name), and AI Search Toolkit feature page

```yaml
source:          SE Ranking (seranking.com, company-stated); Latka Inc. (getlatka.com, analyst-derived, independent)
url_or_doc_id:   https://seranking.com/ai-visibility-tracker.html; https://getlatka.com/companies/seranking.com
published:       undated (SE Ranking page); "Last updated Dec 20, 2024" (Latka profile)
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     table default for the SE Ranking feature page (3, adjusted to 5-context since discussed alongside the revenue source); getlatka.com is analyst-derived, tier 5 per demand-signals.md S3 row ("Funding filings, company statements... Filed beats stated")
source_label:    vendor-reported (feature page); analyst-derived (getlatka.com revenue/funding profile)
lane:            A
sub_market:      incumbent bundling
engine:          Google AI Overviews, Google AI Mode, ChatGPT, Gemini, Perplexity — all five named
metric_kind:     none (feature page); sales (getlatka.com revenue figure)
supersedes:      none
captured:        full text of the AI Visibility Tracker landing page's feature/FAQ sections; full text of the getlatka.com company profile
feature:         "AI Search Toolkit" (product family name) / "AI Visibility Tracker" (landing-page name) — components: AI Competitor Research, AI Results Tracker, AI Source & Coverage Analysis; also a separately-branded sibling product "SE Visible" ("Analyze AI visibility strategically") referenced in global nav but not independently pulled this session
```

## Verbatim

### Roster-rule evidence — getlatka.com company profile

"SE Ranking Revenue 2024: $35M ARR." "City Of Wilmington, Delaware, United States. seranking.com. Local SEO Software. 2024 Revenue $35M. Funding $0. Team 215. Founded 2012." "SE Ranking generated $35M in revenue in 2024. Source: leadiq.com." "SE Ranking is a multifunctional and powerful SEO software that is designed for SEO specialists, web masters and website owners... Last updated Dec 20, 2024." "In 2024, SE Ranking's revenue reached $35M. The company previously reported $21M in 2024."

**Roster-rule determination: SE Ranking clears limb (a).** Two independent, non-listicle, differently-published sources: (1) the G2 category listing already on record from `a-vendor-roster-2026-09-22.md` §3a ("SE Ranking | g2.com/categories/answer-engine-optimization-aeo, read 2026-09-22 (4.7/5, 1,606 reviews)"); (2) this getlatka.com revenue/funding profile, a different publisher (an independent SaaS-revenue database, not G2, not SE Ranking's own site), carrying its own last-updated date (2024-12-20) and citing a third source of its own (leadiq.com). **SE Ranking moves from held to rostered.**

### AI Search Toolkit / AI Visibility Tracker — feature page

"AI Visibility Tracker that fits your delivery map — Track brands across Google AIOs, AI Mode, ChatGPT, and Gemini, and bring that data to the visibility story your stakeholders are asking for." Free live checker on the page itself: enter a domain plus up to 5 competitors, select from AI Overviews / AI Mode / ChatGPT / Gemini / Perplexity, "5 free attempts left for today" (rate-limited, no account required for the free check).

Three named components: "AI Competitor Research" ("Expand your competitor performance analysis to AI search... Add up to five competitors and track presence over time"); "AI Results Tracker" ("Monitor brand mentions and links triggered by your prompts... Review AI responses to discover how your brand is framed... See how your visibility changes over time with historical data"); "AI Source & Coverage Analysis" ("Map domains and URLs that appear in AI answers... Track AI visibility and sources across 7 supported markets. Analyze and filter performance across five languages").

Per-engine breakdown, each with its own paragraph: AI Overviews, ChatGPT, AI Mode, Perplexity, Gemini — e.g. "ChatGPT — See how ChatGPT responds to your target queries and if your brand makes the cut. Analyze linked pages, content, prompts, check the dynamics, and track competitive visibility in generative search with the AI visibility tool."

Integration/export: "Pull AI mention, link, and competitor visibility data directly into your own tools via API or query it live inside Claude or other AI assistants via MCP."

### FAQ (method disclosure)

"How does the AI Search Toolkit work? The AI Search Toolkit monitors AI-generated answers tied to the prompts you track. It also checks for linked and unlinked references to brands, products, businesses, or personal names. You'll see if your website or brand is mentioned, whether it's linked or not, and where it appears among the sources. You can also monitor how often your competitor domains or any sites of interest are cited, so you can spot trends in visibility over time."

"What are the key features of the tool? SE Ranking's AI Search Toolkit covers the full AI visibility workflow: Brand mention and link tracking across AI Overviews, AI Mode, ChatGPT, Gemini, and Perplexity. Competitor AI visibility monitoring with side-by-side analysis and deeper research in LLMs. Source data to see which domains and URLs are featured in AI-generated answers. Cached AI answer copies to see how LLMs frame brands. Historical data to monitor how AI visibility evolves over time and catch shifts."

"What's the difference between the AI Search Toolkit and traditional SEO tools? Traditional SEO tools check to see if your website links appear for targeted keywords in the search engine results page. The AI search grader focuses on generative engine optimization (GEO). It monitors answers generated by ChatGPT, Google's AIOs, and others. Here are the metrics it tracks: Mentions in AI answer texts with and without site links. It captures brand mentions and other references. Links to websites that AI use the most to generate answers and that appear most often in the cited sources section. Citation dynamics, traffic driven by AIOs, and average ranking within generated responses."

"How to run an AI visibility audit? ...Start with the free AI visibility checker on this page. Enter your domain and up to five competitors to get an instant snapshot across AI systems. You get 5 free checks per day. For a complete audit, add prompts you'd like to track to SE Ranking's AI Search Toolkit..."

Metrics named in the live checker's results table: "Brand mentions, #", "Brand mentions, %", "Linked mentions, #", "Linked mentions, %" — per engine (AI Overviews, AI Mode, ChatGPT, Gemini, Perplexity).

## Pull notes — mechanical only

- Both pages fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML, no JS-rendering gate for the FAQ/feature text captured here (the live interactive checker's results table itself requires JS execution and was not run).
- **Prompt-set/n/method disclosure answer for SE Ranking: partial.** The metric definitions and scoring mechanics (mention/link counts and percentages, per-engine, per-prompt) are clearly disclosed; what is customer-configured rather than vendor-fixed is the prompt list itself (the customer adds their own tracked prompts, per the FAQ's "add prompts you'd like to track") — there is no single fixed composite-score prompt set to disclose in the way `hypotheses.md` H15 anticipates, similar to Quattr's pattern (customer-configured tracking, not a fixed vendor panel).
- SE Ranking's own case-studies page (linked from nav as "Case studies") and the sibling product "SE Visible" were not independently pulled this session — time-budgeted against the remaining two held-name checks (Uberall, Onclusive) in this cluster; `unknown — checked seranking.com nav only 2026-09-22` for SE Ranking's own AI-visibility-specific customer case studies.
