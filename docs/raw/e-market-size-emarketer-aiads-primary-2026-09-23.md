# EMARKETER — "US AI Advertising Forecast 2026" (primary landing page: abstract, key stat, headline chart)

```yaml
source:          EMARKETER — report by Nate Elliott; contributors listed on page (Eleni Digalaki, Vivian Dong, Kyndall Krist, Emma Noyes, Shelleen Shum, Matt Torpey, Johann Valderrama, Max Willens, Julia Woolever, Yoram Wurmser)
url_or_doc_id:   https://www.emarketer.com/content/us-ai-advertising-forecast-2026
published:       2026-06-04 ("Jun 4, 2026")
pull_date:       2026-09-23
pull_method:     browser (claude-in-chrome, paywall-bypass extension active); chart image by curl with DNS-over-HTTPS (local DNS fails for emarketer.com)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     named-analyst forecast with a stated scope note (chart footnote) but no published method or model; report body and per-year values behind EMARKETER PRO+ (client seat) — only the abstract, key stat and a redacted headline chart are public
source_label:    analyst-derived
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI; Microsoft Copilot; Google AI Overviews; Google AI Mode; Bing Copilot Search (as named in the chart note)
metric_kind:     none
supersedes:      e-market-size-emarketer-aiads-paid-2026-09-22.md
captured:        public landing page in full (title, subtitle, byline, abstract, key question, key stat, headline chart image, PRO+ wall text, authors); report body not reached
verbatim:        partial — [note: paywalled; figures and short quotes only]
```

## Verbatim

[note: paywalled; figures and short quotes only — the free landing text is reproduced in full below because it is the public abstract]

Title: "US AI Advertising Forecast 2026"
Subtitle: "Most Spending Will Happen Next To—Not Within—AI, as OpenAI Falls Far Short of Its $100 Billion Target"
"Report by Nate Elliott | Jun 4, 2026"

> AI search is growing quickly, but most AI ad spending still depends on traditional search formats. Conversational search ads (e.g., ads inside search engine-based chatbots like Google AI Mode) are scaling faster than ads on standalone chatbots (e.g., ChatGPT or Gemini), which will continue to face pressure on inventory, pricing, and advertiser returns.

> Key Question: How will advertising in and around AI content grow as the category matures?

> Key Stat: More than 80% of AI advertising in 2026 will appear next to AI content—such as traditional search ads next to Google AI Overviews (AIOs)—rather than inside AI chatbots or conversations. Overall, AI ad spending will more than double in the next five years to $68.25 billion in 2030.

Headline chart (image, alt "AI Ad Spending Will More Than Double by 2030"):

[image: docs/raw/img/e-market-size-emarketer-aiads-primary-2026-09-23/01-ai-ad-spending-will-more-than-double-by-2030.png]

Chart text as rendered: title "AI Ad Spending Will More Than Double by 2030"; subtitle "US AI ad spending in billions, by ad type, 2026-2030 (redacted)"; stacked bars 2026–2030; labels "$32.03" (2026), "$--.--" (2027, 2028, 2029), "$68.25" (2030); arrow "2.1x" from 2026 to 2030; series legend "AI search-adjacent", "AI conversational search", "AI chatbots"; y-axis $10–$60. Chart note: > "includes advertising that appears within large language model (LLM) generative AI platforms (e.g., ChatGPT, Microsoft Copilot) and within or alongside AI-powered search summaries (e.g., Google AI Overviews) and AI-powered search conversations (e.g., Google's AI Mode, Bing Copilot Search); excludes traditional keyword-based search ads and standard paid listings on search engine result pages where no AI-generated content is present". "Source: EMARKETER Forecast, May 2026". Chart ID 366969.

Wall text: "READ THIS WITH EMARKETER PRO+ … These insights are limited to EMARKETER PRO+ subscribers."

## Pull notes — mechanical only

- emarketer.com resolved in the Chrome tab on 2026-09-23 (the 2026-09-23 R-BLOCKED probe recorded DNS ERR_NAME_NOT_RESOLVED); curl on this machine still fails DNS for the domain, and worked with `--doh-url https://cloudflare-dns.com/dns-query` (resolves to Cloudflare 104.18.16.94 / 104.18.17.94).
- Two loads through the extension (initial and one reload): identical output; the PRO+ wall did not move. The bypass extension did not change what rendered. No login, no account, no form, no demo request.
- Chart image saved by curl (HTTP 200, 149,952 bytes, image/png); the 2027–2029 values are redacted in the public image itself. INDEX row added.
- Comparison with substitute (PPC Land pointer): $32.03 billion 2026 and $68.25 billion 2030 agree; ">80% next to AI content" agrees with the pointer's "over 80% flows next to AI content". The pointer's "less than $1 billion" chatbot 2026 / "just over $5 billion" 2030 sub-figures and the $60 → ~$15 CPM line are inside the paywalled body and are not on the public page — not in primary (public part).
