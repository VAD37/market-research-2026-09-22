# EMARKETER — "AI Commerce 2026" (primary landing page: abstract, key stat $144 billion by 2029, headline chart)

```yaml
source:          EMARKETER — report by Carina Lamb; contributors listed on page (Suzy Davidkhanian, Eleni Digalaki, Nate Elliott, Penelope Lin, Cindy Liu, Wendy Malloy, Amy Rotondo, Matt Torpey, Emman Velasco, Ali Young)
url_or_doc_id:   https://www.emarketer.com/content/ai-commerce-2026
published:       2026-01-26 ("Jan 26, 2026")
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome, paywall-bypass extension active); chart image by curl with DNS-over-HTTPS
pull_purpose:    evidence about a number
tier:            4
tier_reason:     named-analyst forecast, no published method; body behind EMARKETER PRO+ (client seat, "Purchase this Report" also offered); only the abstract, key stat and a redacted headline chart are public
source_label:    analyst-derived
lane:            E
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI; Google; Perplexity (as named in the abstract)
metric_kind:     sales
supersedes:      e-market-size-stellagent-agentic-2026-09-22.md (eMarketer rows only)
captured:        public landing page in full (title, subtitle, byline, abstract, key question, key stat, headline chart image, wall text, authors); report body not reached
verbatim:        partial — [note: paywalled; figures and short quotes only]
```

## Verbatim

[note: paywalled; figures and short quotes only — the free landing text is reproduced in full below because it is the public abstract]

Title: "AI Commerce 2026"
Subtitle: "AI Is Reshaping Ecommerce Journeys, but Retailer Sites Still Own the Transaction"
"Report by Carina Lamb | Jan 26, 2026"

> The era of AI commerce is underway, with more consumers using AI tools to discover, research, and even purchase products. After leaning heavily into commerce, AI platforms such as ChatGPT, Google, and Perplexity will drive a growing share of ecommerce sales through 2029. But despite innovations like Instant Checkout and partnerships with prominent payment players, most transactions are still completed on retailer websites. And future growth could stall or accelerate, depending on consumer experiences and strategies by the major players.

> Key Question: What is the outlook for AI commerce in 2026 and beyond?

> Key Stat: AI platform-driven ecommerce sales will surpass $144 billion by 2029, which will be 8.8% of total retail ecommerce sales.

Headline chart (image), alt text as in the page HTML:

> "US Ecommerce Sales via AI Platforms Will Exceed $20 Billion in 2026 and Top $144 Billion by 2029, (billions in US AI platform-driven retail ecommerce sales, % change, and % of total retail ecommerce sales, 2025-2029 (redacted))"

[image: docs/raw/img/e-market-size-emarketer-ai-commerce-2026-primary-2026-09-23/01-us-ecommerce-sales-via-ai-platforms-2025-2029.png]

Wall text: "READ THIS WITH EMARKETER PRO+ … Schedule a Demo · Purchase this Report".

## Pull notes — mechanical only

- Located via html.duckduckgo.com in the browser (`site:emarketer.com "AI Commerce" 2026 forecast $144 billion 2029`), first result.
- Tab resolved emarketer.com; curl needed `--doh-url https://cloudflare-dns.com/dns-query`. One load through the extension; PRO+ wall unchanged. No login, no form, no purchase.
- Chart image saved by curl (HTTP 200, 57,922 bytes, image/png); per the alt text the per-year values are redacted in the public image. INDEX row added; values not transcribed (IMG-1).
- Comparison with substitute (Stellagent tier-6 table): substitute "eMarketer, US, 2029, $144B, EC sales via AI platforms only" and "over $20 billion in 2026 … $144 billion by 2029 (roughly 8.8% of US e-commerce)" — primary agrees: "$20 Billion in 2026", "$144 billion by 2029", "8.8% of total retail ecommerce sales" (US, per chart alt).
