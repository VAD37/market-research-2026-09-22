# Koala AI — AI-SEO content-generation vendor claiming AI-answer citation

```yaml
source:          Koala AI (own marketing site)
url_or_doc_id:   https://koala.sh/
published:       undated — no copyright or publication date on the page (schema markup lists a Gainesville, FL address only)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor blog / marketing page — aggregate output totals ("4M+ articles generated," "20,000+ paid creators") carry no date window, no independent verification, and no n behind the implied AI-citation claim. Trust-rubric.md table default for "vendor blog, no n"
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          Google AI Overviews, ChatGPT, Perplexity — named directly in the vendor's own marketing claim (quoted below), with no evidence of citation rate, method, or n behind the claim
metric_kind:     none — "Get cited by Google AI Overviews, ChatGPT, and Perplexity" is a marketing promise, not a measured citation-rate figure
supersedes:      none
captured:        homepage marketing copy — product description, AI-citation claim, pricing, aggregate output totals
technique:       comparison-page farming and adjacent formats — vendor markets an "SEO agent" that analyzes Search Console data for "content gaps" and drafts articles at volume via "KoalaWriter"; page does not explicitly name "X vs Y," "best X for Y," or "alternatives to" pages as a distinct generated format, but directly and explicitly claims the general output is built to be "cited" by three named AI engines
models_tested:   n/a — not a research artifact
date_window:     n/a
measured_effect: no — the AI-citation claim ("Get cited by Google AI Overviews, ChatGPT, and Perplexity") is a promotional statement with no n, no date window, and no independent verification behind it. Discarded per trust-rubric.md's "vendor measuring what it sells, no third-party replication" rule as anything beyond a vendor's own marketing claim that the AI-citation sales pitch exists in this market
vertical:        none named
```

## Verbatim

### Product description (quoted as returned by WebFetch)

Koala AI is "an AI SEO platform combining an SEO agent, content writer, and publishing tools." The agent "analyzes Google Search Console data to identify content gaps," while "KoalaWriter drafts articles in your brand voice, with one-click publishing to WordPress, Shopify, Webflow, Ghost, or custom endpoints."

### AI-citation claim (quoted as returned by WebFetch)

"Get cited by Google AI Overviews, ChatGPT, and Perplexity" — offered as "AI search optimization." Elsewhere: finding "where you're invisible on Google and in AI answers, then fix it."

### Aggregate output claims (quoted as returned by WebFetch)

"20,000+ paid creators"; "4M+ articles generated"; "25M+ internal links placed"; "10M+ images created."

### Pricing (quoted as returned by WebFetch)

"From $49/mo" (Professional tier); full agent access requires the Boost tier "at $99/mo."

## Pull notes — mechanical only

- Fetched via `WebFetch` against `koala.sh/`, 200.
- No copyright or last-updated date is present on the page; recorded as `undated` per the raw-pull template's instruction rather than guessed.
- The page's AI-citation claim names three engines explicitly but is not accompanied by any citation-rate figure, prompt set, or date window — this pull records the claim's existence and wording only, not as evidence the claim is true. `unknown — checked the homepage only, 2026-09-22` on whether a separate case-study or methodology page on the same site substantiates the claim with a number.
- No explicit claim of comparison/"vs"/"best X"/alternatives page generation as a distinct SKU was found on the homepage; `unknown — checked the homepage only, 2026-09-22` on whether a deeper page markets this format specifically.
