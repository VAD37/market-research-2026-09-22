# Similarweb Ltd. — SEC filings: 20-F risk factors and Q2 2025 shareholder letter (AI Brand Visibility launch dates)

```yaml
source:          Similarweb Ltd. (SEC filer, ticker SMWB, CIK 0001842731)
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1842731/000184273126000018/smwb-20251231.htm (Form 20-F, fiscal year ended 2025-12-31, filed 2026-03-02); https://www.sec.gov/Archives/edgar/data/1842731/000184273125000028/q22025smwbshareholderlet.htm (Form 6-K, Exhibit 99.2, filed 2025-08-12, period ending 2025-06-30)
published:       2026-03-02 (20-F); 2025-08-12 (6-K exhibit)
pull_date:       2026-09-22
pull_method:     fetch (curl, direct sec.gov URL from two SEC EDGAR full-text search API hits at efts.sec.gov/LATEST/search-index — first for %22answer+engine+optimization%22 filtered to CIK 0001842731, second for %22AI+Brand+Visibility%22 same CIK)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed. Form 20-F (annual report, foreign private issuer) and Form 6-K exhibit, both filed by the registrant itself
source_label:    filed
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT (named, "close to 700 million weekly users" cited as context)
metric_kind:     none directly for the feature (no feature-specific revenue or customer-count figure found); company-wide revenue/customer figures present in the same exhibit, noted in pull notes
supersedes:      none
captured:        the one 20-F risk-factor passage matching "answer-engine optimization" plus its expanded discussion elsewhere in the same filing; the shareholder letter's "Similarweb and the AI revolution" section in full
```

## Verbatim

### Form 20-F (FY2025, filed 2026-03-02) — risk factors

Risk-factor summary bullet (page ~9 of the filing's own pagination): "Our business could be negatively affected by changes in search engine algorithms and by changes in how information is discovered, ranked, summarized or surfaced by search engines, answer engines and other AI-driven discovery platforms, including shifts toward answer-engine optimization and generative responses."

Expanded discussion under the heading "The evolving role of artificial intelligence and its impact on Internet search engines and related products and services could result in reduced demand for our solutions" (page ~17): "The rapid development and deployment of artificial intelligence ('AI') technologies pose both opportunities and risks to internet search engines and products and services such as ours that rely on them. The pace of AI innovation has accelerated significantly, particularly with respect to generative AI, large language models and AI-powered assistants. Generative AI alternatives to search engines have the potential to disrupt traditional search engine models by changing the way information is accessed, organized, and presented to users. These changes may reduce the volume of traditional search queries, increase 'zero-click' experiences, or shift user engagement away from third-party websites and tools... In particular, the widespread adoption of AI-powered alternatives to traditional search, such as chatbots, virtual assistants, or advanced AI-driven search engines, may undermine the market share and profitability of traditional internet search engines and in turn products and services that rely on them. Search engines may increasingly surface AI-generated summaries, answers or recommendations directly to users, reducing traffic to external websites and limiting the availability, visibility or granularity of underlying data... We cannot predict with certainty how the continued evolution of AI technologies will shape the future of internet search and its related ecosystems. Our ability to respond effectively may require significant investment in research and development, data acquisition, partnerships, or new technologies, including AI-enabled capabilities, with uncertain returns... If we are unable to anticipate, respond to, or capitalize on these changes, or if AI-driven alternatives reduce demand for search-based intelligence solutions, this could lead to material adverse effects on our business operations, market position, and financial results."

[note: this 20-F risk-factor discussion frames AI-driven search as a **threat** to Similarweb's existing (pre-AI) web-traffic-estimation business, and does not itself name or describe the "AI Brand Visibility" product as a mitigation — that product-specific disclosure and its launch date are found instead in the separately-pulled 6-K shareholder letter below, not in this 20-F.]

### Form 6-K, Exhibit 99.2 — Q2 2025 Shareholder Letter — "Similarweb and the AI revolution" (full section)

"At our core, we are a data company. Our unique data asset, Similarweb Digital Data, provides the foundation for our solutions... As part of our mission to provide a 360° view of the digital world, we've significantly expanded our product offering in 2025 to empower customers with faster, deeper insights across the digital landscape. We launched Similarweb Ad Intelligence, giving businesses a clearer and more complete view of the digital marketing universe. We also introduced enhanced modules for mobile app intelligence and GenAI intelligence—each representing a key layer in how users interact with digital content today."

"**Similarweb and the AI revolution** — The AI revolution is accelerating, and we are already seeing clear traction across key use cases. As a leading supplier of digital data, the AI revolution presents significant opportunities for us. High quality, comprehensive, actionable and trusted data, like Similarweb's, is a critical and foundational component for every AI and LLM tech stack. We're focused on three high-impact opportunities where we believe that Similarweb is uniquely positioned to lead: 1. Generative AI & LLM Data Partnerships - we are supplying our unique and fresh Digital Data to companies that are building their own LLMs and Generative AI applications. 2. **GenAI Intelligence** - with ChatGPT reaching close to 700 million weekly users, generative AI is reshaping how people discover and engage online. To help brands lead in this shift, we launched our Gen AI Intelligence suite. **- In April [2025], we introduced AI Traffic to show how much website traffic comes from GenAI sources —along with the prompts and landing pages driving it. - In June [2025], we expanded the suite with AI Brand Visibility, giving companies daily insights into how often they are cited in AI-generated content across key topics.**"

## Pull notes — mechanical only

- Both filings fetched via direct `curl` to their `sec.gov/Archives/edgar/data/...` URLs, found via two `efts.sec.gov/LATEST/search-index` full-text queries (correct CIK 0001842731 found via `sec.gov/cgi-bin/browse-edgar` after an initial guessed CIK returned zero hits); both HTTP 200.
- **Launch date, filed and dated precisely: AI Traffic launched April 2025; AI Brand Visibility launched June 2025**, both as expansions of Similarweb's "Gen AI Intelligence suite," per the company's own Q2 2025 shareholder letter (filed as a 6-K exhibit 2025-08-12) — this is the most precise dated launch disclosure found for any of the five incumbents in this cluster, tied with (and independently corroborating in kind) Semrush's own year-only 10-K disclosure.
- The 20-F is a large filing (2.5 MB, 6,876 extracted lines); this file reproduces only the two passages matching the search terms plus surrounding context. No revenue or customer-count figure specific to AI Brand Visibility or the Gen AI Intelligence suite was found in either filing — the shareholder letter gives only company-wide Q2/Q3 2025 revenue guidance ($71.5M-$72.0M for Q3-25) and company-wide customer-growth figures (18% YoY total customer accounts, 13% YoY growth in $100,000+ customers), not a feature-level breakout. `unknown — checked smwb-20251231.htm (20-F), q22025smwbshareholderlet.htm (6-K exhibit) 2026-09-22` for a Gen AI Intelligence / AI Brand Visibility revenue or customer-count figure specifically.
- A separate full-text search for "AI Visibility" (without "Brand") was not re-run against this CIK, since "AI Brand Visibility" is the product's own name and the search above already isolates its one filed mention.
