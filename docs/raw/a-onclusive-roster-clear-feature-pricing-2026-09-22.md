# Onclusive — three-limb roster rule check (held name), GEO Analytics feature page, and pricing

```yaml
source:          Onclusive (onclusive.com, company-stated); UK Companies House (find-and-update.company-information.service.gov.uk, filed)
url_or_doc_id:   https://onclusive.com/products/geo-analytics/; https://find-and-update.company-information.service.gov.uk/search/companies?q=Onclusive
published:       undated (product page); Companies House record: incorporated 2014-04-08, live register
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed, for the UK Companies House record; product/pricing page is table default 3 (platform primary)
source_label:    filed (Companies House); vendor-reported (product/pricing page)
lane:            A
sub_market:      incumbent bundling
engine:          ChatGPT, Google Gemini, Grok, Claude, Perplexity — five named
metric_kind:     none directly (feature/pricing page); no revenue or customer-count figure found this pull
supersedes:      none
captured:        full text of the GEO Analytics product/pricing page; the Companies House search-result entry
feature:         "GEO Analytics" (product page title: "GEO Analytics & AI Search Intelligence"), also referenced as "AI Brand Visibility" in Onclusive's own primary navigation under the "Analytics" product family — same feature, two names used across the site
```

## Verbatim

### Roster-rule evidence — UK Companies House

"ONCLUSIVE UK LIMITED — 08984741 - Incorporated on 8 April 2014 — 1 Finsbury Market, 2nd Floor, London, England, EC2A 2BN."

**Roster-rule determination: Onclusive clears limb (a) (and arguably limb (b) directly, as a tier-2 filing).** Two independent, non-listicle, differently-published sources: (1) the G2 category listing already on record from `a-vendor-roster-2026-09-22.md` §3a ("Onclusive | g2.com/categories/answer-engine-optimization-aeo?page=2, read 2026-09-22 (4.3/5, 207 reviews)"); (2) this UK Companies House filing record — the same channel and tier the project's own roster rule already treats as qualifying (used to corroborate Searchable and geoSurge in `a-vendor-roster-2026-09-22.md` rows 2 and 4). **Onclusive moves from held to rostered.**

### GEO Analytics — product/pricing page (condensed; nav/footer chrome elided per this cluster's convention)

"GEO Analytics & AI Search Intelligence | Onclusive." "AI Search Intelligence — GEO Analytics — Monitor how your brand appears in AI-generated search results and connect it to your media strategy." "Your audiences are already gathering information about your brand from AI-generated search results. Onclusive GEO Analytics gives you visibility into what ChatGPT, Gemini, Grok, Claude, and Perplexity are telling them, so you can spot gaps and inaccuracies before your stakeholders do."

Four named capabilities: "Unified AI Monitoring — Track brand presence across 5 AI engines alongside your earned media, social, and analytics in one platform." "Actionable Intelligence — Priority Source Targets tell you exactly which publications and domains to pitch for maximum AI visibility impact." "Competitive Advantage — Understand how competitors are positioned in AI search results and identify opportunities to close the gap." "AI Visibility Metrics — Track share of voice, visibility, sentiment, and positioning across AI search platforms."

Four feature blocks with sub-bullets: "Multi-Engine AI Monitoring" (Monitor ChatGPT, Gemini, Grok, Claude, and Perplexity; track brand presence in any market and language; real-time visibility; sentiment analysis); "Earned Media to AI Connection" (Connect PR activity to AI engine responses; track which articles and sources AI tools cite; measure message pull-through; prove the earned media impact on AI visibility); "Priority Source Targets" (Impact-scored target publications; effort-ranked opportunities; strategic guidance; clear action plan); "Competitive Intelligence" (Share of voice across AI platforms; competitive positioning analysis; identify competitor advantages; track relative brand performance over time).

### Pricing table — "Choose Your Annual Plan" (full text, verbatim figures)

- **Starter** — "Perfect for individuals getting started." **From $105/month.** 1 country; ChatGPT; 80 prompts.
- **Essential** — "For growing teams needing more power." **From $280/month.** 1 country; ChatGPT, Perplexity, Gemini; 240 prompts.
- **Professional** ("Most popular") — "Scale across markets with full AI access." **From $1255/month.** 3 countries; ChatGPT, Perplexity, Gemini, Claude, Grok; 720 prompts.
- **Enterprise** — "Customize to your needs. Track every market and category that matters for your strategy." **Custom.** 5 countries; ChatGPT, Perplexity, Gemini, Claude, Grok; 2000 prompts.

### FAQ (method disclosure, full text of the load-bearing answers)

"What is GEO Analytics and how does it help brands? GEO Analytics (Generative Engine Optimization Analytics) tracks how brands appear in AI-powered search results from ChatGPT, Gemini, Grok, Claude, and Perplexity. It helps brands monitor their AI search presence, identify gaps in visibility, and connect earned media coverage to AI-generated recommendations about their products or services."

"Can GEO Analytics show which sources AI engines use for brand information? Yes, Onclusive GEO Analytics identifies the exact publications, domains, and content types that AI engines cite when discussing brands. The platform's Priority Source Targets feature scores these sources by impact and effort..."

"What metrics does GEO Analytics provide for measuring AI search performance? GEO Analytics provides sentiment analysis, share of voice comparisons, competitive positioning data, source attribution tracking, and cross-channel correlation metrics. The platform offers 4-level perception summaries from global to market-specific insights with executive-ready reporting."

"What is anomaly detection in GEO Analytics? Anomaly detection automatically identifies unusual changes in brand perception or competitive positioning across AI platforms. The system flags severity-ranked issues, such as sudden negative sentiment shifts or competitors gaining prominence..."

"Does GEO Analytics integrate with existing marketing and PR tools? Yes, Onclusive GEO Analytics integrates seamlessly with media monitoring, social listening, and analytics platforms. It works within the Onclusive Unified Platform alongside earned media tracking and social analytics..."

## Pull notes — mechanical only

- Both sources fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML, no JS-rendering gate.
- **Price disclosed cleanly, but no price delta is computable against a separate non-AI "base plan"**: unlike Semrush and SE Ranking (a base non-AI-or-partial-AI plan plus a priced AI upgrade/add-on) or BrightEdge/Muck Rack/Quattr/Similarweb (no public price at all), Onclusive's GEO Analytics is priced as its **own standalone four-tier product line** ($105 → $280 → $1255 → Custom/month), not sold as an add-on delta over a separate "Onclusive Unified Platform" base price — no base-platform dollar figure was found on this page to subtract from. Recorded as the disclosed standalone price, with this structural note, per this cluster's practice of stating each vendor's actual pricing shape rather than forcing a uniform "delta" framing where the vendor's own structure does not support one.
- **Prompt-set/n/method disclosure answer for Onclusive: partial.** Prompt counts are disclosed per tier (80/240/720/2000), and the metrics computed (share of voice, sentiment, positioning, source attribution) are named, but the actual prompt content/list is not published, and it is unclear from this page alone whether prompts are customer-defined (as with Quattr, SE Ranking, Uberall) or vendor-supplied per tier — `unknown — checked onclusive.com/products/geo-analytics 2026-09-22` for which.
- No customer case study or launch-date press release for GEO Analytics specifically was located this pull — time-budgeted against the census-summary and STATE.md work remaining for this cluster; `unknown — checked onclusive.com/products/geo-analytics, onclusive.com homepage nav (no dated press release found), news.onclusive.com (not opened this pull) 2026-09-22` for GEO Analytics' launch date and any customer case studies.
