# Peec AI — Pricing page, rendered (list prices, tier limits, add-on prices)

```yaml
source:          Peec AI (peec.ai)
url_or_doc_id:   https://peec.ai/pricing
published:       undated — no date on page; page banner references a live event "September 22" (2026)
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome, paywall-bypass extension active) — JS-rendered figures; static HTML carries no price
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — pricing page; table default
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, AI Mode, AI Overviews, Microsoft Copilot, Gemini, Naver AI (Starter–Advanced model choice); Enterprise adds Claude Sonnet 4, GPT 5 Search, Grok, Deepseek, Qwen, Mistral, Meta Spark, Perplexity (API)
metric_kind:     none
supersedes:      a-peec-pricing-2026-09-22.md (static HTML without price figures)
captured:        full rendered page: plan cards, comparison matrix, add-ons, testimonials, FAQ
verbatim:        full for prices and limits; feature-matrix labels listed; testimonials summarised
```

## Verbatim

"Pricing for Brands — Track and improve your brand visibility across AI platforms with analytics your team will actually enjoy using." "Trusted by 3000+ brands and agencies"

Plan cards (Monthly toggle):

| Plan | Price | Includes |
|---|---|---|
| Starter | $95 /mo | 50 prompts · Choose 3 models · Unlimited users · Daily tracking frequency · 1 project |
| Pro | $245 /mo | 150 prompts · Choose 3 models · Unlimited users · Daily tracking frequency · 2 projects |
| Advanced | $495 /mo | 350 prompts · Choose 3 models · Unlimited users · Daily tracking frequency · 5 projects · Multi country · Looker Studio integration |
| Enterprise | Custom (Annual) | Everything in advanced, plus: Fully customizable prompt tracking · Choose from all models · Daily or weekly tracking frequency · Unlimited projects · Custom prompt setup · API access · Single Sign-on (SSO) · Up to 13 LLM models tracked |

"Running a GEO agency? Track prompts across multiple brands. See agency pricing"

Comparison matrix, "Tracking Coverage" rows (Starter / Pro / Advanced / Enterprise):
- Available models: ChatGPT, AI Mode, AI Overviews, Microsoft Copilot, Gemini, Naver AI (all tiers); Enterprise adds Claude Sonnet 4 (API), GPT 5 Search (API), Grok (API), Deepseek (API), Qwen (API), Mistral (API), Meta Spark (API), Perplexity
- Prompts: 50 / 150 / 350 / 350 [as rendered; card says "Fully customizable"]
- Active models: 3 / 3 / 3 / unlimited
- Frequency: daily / daily / daily / daily / weekly
- Monthly AI answers ("Calculated by multiplying tracked prompts by active models and tracking frequency."): 4500 / 13500 / 31500 / unlimited
- Countries: 1 / 3 / 3 / unlimited; Projects: 1 / 2 / 5 / unlimited; Languages, Competitors, Team users: unlimited on all
- Discover — Prompt volume ("Relative demand for the topic behind each tracked prompt, scored 1–5."), competitor / topic / prompt suggestions, prompts from keywords, personas, bulk import, sub-brand tracking, brand and intent classification
- Measure — Visibility overview, Brand insights, Ads library ("Prompts where AI answers carry a sponsored placement, and which advertisers appear."), Local GEO, AI Shopping (product catalog upload, SKU-level tracking, top merchants, shopping query fanouts, shopping source visibility), Source analytics (domain/URL detail, subdomain tracking, fanout overview, retrievals, citation share, source classification), Brand Perception (attribute scoring, custom attributes, objections, prompts fact-checked, facts per brand)
- Act — Gap analysis, Recommended actions, Agent actions
- Report — Visibility impact, lift analysis, lift predictor, custom tables & views; Agent analytics: crawlability audit ("across 40+ bots"), AI referrals, crawl insights — bot-visit allowance 4M / 10M / 25M / Custom; automated reporting: - / Monthly / Weekly / Weekly; shareable dashboards 5 / 10 / 25 / unlimited; Data Studio connector 5 / 20 / 50 / unlimited; Data access: API, MCP, custom exports (CSV)
- Support channels: Chat / Chat + email / Chat + email / Dedicated; Onboarding: Self-serve / Self-serve / Self-serve / Custom
- Integrations — CDN & log providers: Vercel, Cloudflare, AWS, CloudFront, Google Cloud CDN, Wordpress, Akamai, Generic webhook, CSV/CLF Upload; Google Analytics

Add-ons — "Additional Models — Track more AI models without switching plans. ChatGPT, AI Mode, AI Overviews, Microsoft Co-pilot, Perplexity, Gemini." "Price reflects one additional model based on the prompts included in this plan.":

| Plan | Add-on price (Annual) |
|---|---|
| Starter | $30 /mo — "Save $60" |
| Pro | $70 /mo — "Save $180" |
| Advanced | $140 /mo — "Save $300" |

FAQ (verbatim, figures): > "What are AI answers? AI answers are the individual AI search results we track across platforms. It represents one chat result per model. Example: If you are running 25 prompts across 3 models for 30 days, we would analyze 25x3x30 = 2250 AI answers." · > "What determines the pricing? Pricing is based on the number of tracked prompts and models analyzed. Higher tiers get discounts on price per prompt and a dedicated support function." · > "How does pricing work for multiple countries/languages? You can track queries across any supported country or language with no additional cost." · > "Is there a yearly discount? We offer a 15% discount for customers who choose annual billing." · Agency bundles: "centralized billing and flexible prompt allocation".

Testimonials (names and figures): Crystal Carter (Head of SEO Comms); Jon Gitlin (SEO Strategist): "drive a 5x year-over-year increase in traffic and demo requests from LLMs"; Ethan Smith (CEO); Sepy Bazzazi (Head of Marketing, Glide): "ranking for targeted ChatGPT and Perplexity prompts within 24 hours"; Thomas Smeaton (SEO Manager); Artur Kosch (General Manager).

Footer: "rated 4.9/5 on G2".

## Pull notes — mechanical only

- Rendered in the extension tab; the price figures ($95 / $245 / $495; add-ons $30 / $70 / $140) are absent from the static HTML fetched by curl (1,218,187 bytes, no "$" price string). The page's default toggle read "Monthly" for the three cards and "Annual" for the add-on cards, as captured; the 15% annual discount is stated in the FAQ.
- Ads library row is present in the "Measure" block — a paid-placement feature on an organic-visibility tool, recorded for Lane B.
- No login, no form.
