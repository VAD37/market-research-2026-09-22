# PPC Land, pointer to EMARKETER — "US AI Advertising Forecast 2026" ($32.03bn 2026 -> $68.25bn by 2030)

```yaml
source:          PPC Land (pointer), primary EMARKETER, report authored by Nate Elliott
url_or_doc_id:   https://ppc.land/emarketer-says-us-ai-ad-spend-hits-68bn-by-2030-and-chatgpt-misses-most-of-it/ ; primary at https://www.emarketer.com/content/us-ai-advertising-forecast-2026 (subscription-gated — direct fetch this pull returned only the site nav/TOC shell, no figures; see pull notes)
published:       2026-06-04 (PPC Land article; EMARKETER report itself dated the same day per PPC Land)
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool; ppc.land fetched cleanly; emarketer.com primary attempted, paywalled beyond nav)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     trade-press pointer to a named-analyst report (EMARKETER, "US AI Advertising Forecast 2026," authored by Nate Elliott, EMARKETER's Principal Analyst for AI in Marketing and Commerce) with the underlying report's methodology partially relayed (three named ad-type categories, an analyst quote, a stated contrast with OpenAI's own investor figures) but not independently confirmed against the primary, which is subscription-gated; per trust-rubric.md "5 pointer" for trade press linking primary data where the primary itself is not fully reachable
source_label:    analyst-derived
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI; Google (AI Mode, AI Overviews); Microsoft Copilot; Gemini (named as the category "standalone LLM platforms")
metric_kind:     none
supersedes:      none
captured:        full PPC Land article up to the fetch tool's per-call truncation point (article continues into Google Q1 2026 earnings context, not captured further — not load-bearing for the headline figures)
```

## Verbatim

Headline: "EMARKETER says US AI ad spend hits $68bn by 2030 - and ChatGPT misses most of it." Sub-headline: "US AI ad spending will more than double to $68.25bn by 2030, but over 80% flows next to AI content, not inside chatbots, per EMARKETER's 2026 forecast report."

The size and forecast figure (the sentence carrying the number, and its author's own label):

> "A new forecast published on June 4, 2026 by EMARKETER projects that US advertising spending in and around artificial intelligence platforms will more than double from $32.03 billion this year to $68.25 billion by 2030."

Segment breakdown by ad type, as the report itself defines them:

> "The forecast covers three distinct ad types. AI search-adjacent advertising - the largest category - includes traditional keyword-based search ads that appear next to AI-generated summaries such as Google AI Overviews. AI conversational search advertising covers ads inside search engine-based chatbot experiences, such as Google AI Mode. AI chatbot advertising, the smallest and most contentious segment, refers to ads inside standalone large language model platforms such as ChatGPT, Microsoft Copilot, and Gemini."

The chatbot-specific sub-figure, contrasted explicitly against OpenAI's own investor projection (see the companion raw file `e-market-size-emarketer-openai-paid-2026-09-22.md` for that separate figure):

> "According to EMARKETER, ChatGPT and its direct competitors - the standalone chatbot category - will generate less than $1 billion in US chatbot advertising revenue in 2026. By 2030, that figure rises to just over $5 billion. Even if OpenAI captured every dollar of that segment, it would fall dramatically short of the $100 billion global target the company has described to investors."

Analyst attribution and a direct quote:

> "The report, titled 'US AI Advertising Forecast 2026,' was authored by Nate Elliott, EMARKETER's Principal Analyst for AI in Marketing and Commerce... Elliott posted the core argument on LinkedIn on June 9: 'OpenAI thinks ChatGPT will collect about $50 billion in US ad revenues in 2030,' he wrote. 'We think their entire addressable market will be 1/10th that.'"

CPM detail (a price figure within the forecast, not the market-size headline):

> "The report notes that ChatGPT launched its advertising pilot at a $60 CPM. EMARKETER projects that price will fall to barely one-quarter of that level - approximately $15 - by 2030."

## Pull notes — mechanical only

- `ppc.land` fetched cleanly, no 403, no paywall.
- The primary, `emarketer.com/content/us-ai-advertising-forecast-2026`, was fetched directly this pull: the page returned its full site navigation shell and a report landing page with author byline and table of contents ("Report by Nate Elliott | Jun 4, 2026"), but no body figures — full report text is subscription-gated ("Does my company subscribe? ... Become a Client"). No number beyond what PPC Land relays was independently confirmed against the primary.
- Article truncated by the fetch tool's per-call character limit partway through a section on Google's Q1 2026 earnings and Alphabet's AI infrastructure financing — not load-bearing for the headline AI-ad-spend figures already captured, not re-fetched further.
