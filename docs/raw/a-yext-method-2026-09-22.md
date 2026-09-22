# Yext — method / how-it-works (Yext Research citation-behavior study, underlying Scout's data)

```yaml
source:          Yext Research (yext.com)
url_or_doc_id:   https://www.yext.com/research/ai-citation-behavior-across-models-consistent-source-preferences-across-a-growing-ai-landscape
published:       "Research Brief · AI Citation Behavior · July 2026"; study window "January through March 2026" / "Q1 2026"
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-authored study (Yext Research) with n, date window, and method disclosed (per `trust-rubric.md`'s "vendor or agency study with n, dates, method" = tier 5, bias flagged) — not the Scout product's own "how it works" documentation, but the closest disclosed-methodology page found on Yext's site describing the AI-citation data Scout is built on. No independent replication found or attempted this session.
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        first ~5000 characters (truncated by the fetch tool)
```

## Verbatim

"Research Brief · AI Citation Behavior · July 2026 — With location on, AI cites the sources that know places — AI assistants answer with the person's location on by default, and across more than 155 million location-grounded citations the models leaned on the sources that know where things are. By Arjun Sangwan, Yext Research.

**An analysis of 155.5 million AI citations across 1,623 brands and four AI models, January through March 2026.**

location context · AI citations · zones of control · listings · brand websites

5.8× Citations to the top mapping directory for every one to the internet's encyclopedia
155.5M AI citations parsed across 1,623 brands in Q1 2026
80% Point to sources a brand can influence
+28% Citations per scan, quarter over quarter, in a fixed 770-brand cohort"

"The short version — Ask an AI about a brand with no sense of where the human is, and you are likely to see sources like Wikipedia. That is rarely the question a customer asks. Location is central to the context an answer is built on, and assistants keep it on by default, so a brand question is usually a place question. The 155.5 million citations in this study were earned on location-grounded questions, the kind customers actually ask. Four in five pointed to a website or a listing, the two things a brand can keep current, and the mix likely shifts again at every level of geography, from national to DMA to state to city to neighborhood to the single location.

What to do. Read your AI presence with location in the question, at every level you compete at, and keep your website pages, listings, and the small directories current, because the models read them and cite what they find."

"How to read the zones of control — Each citation was classified by the type of source it points to. Websites are pages on the brand's own domain. Listings are public directories that carry structured business facts. Reviews and social covers platforms where customers write about the brand. News and other covers press, forums, and everything else. The study counts the first two as influenceable, since a brand writes its own pages and, when listings are managed, controls those too."

"Finding 01 — The forgotten publishers top the third-party list — Set the brand-owned domains aside and rank where else the models point. The top spot belongs to MapQuest, with almost six million citations in one quarter, 5.8 for every one that Wikipedia earned. TripAdvisor sits second and climbing, and Yelp is third and new to the list, so the whole top ten is directories and review platforms with the internet's encyclopedia as the lone exception. ... MapQuest drew 6.0 million citations, TripAdvisor 3.8 million, and Yelp 2.1 million against Wikipedia's 1.0 million."

"Finding 02 — Four in five citations sit in the influenceable zones — Across all four models, 80 percent of the citations pointed at a website or a listing, the two zones a brand can keep current, while the other fifth came from reviews, social, press, and forums, the zones it can only nudge. **Per model, the influenceable share runs 85 percent for OpenAI, 81 for Gemini, 80 for Perplexity, and 69 for Anthropic. That is a 16-point spread between the highest model and the lowest.** ... Websites take 52.0 percent of Gemini's citations and 50.9 of Perplexity's, listings take 36.1 percent of OpenAI's, and reviews and social take 19.5 percent of Anthropic's against 2.6 for OpenAI." [note: content truncated by the fetch tool at this point]

**Prompt-set / n / method disclosure assessment:** this study discloses **n = 155.5 million citations, 1,623 brands, 4 named AI models (OpenAI, Gemini, Perplexity, Anthropic), a stated date window (January–March 2026 / Q1 2026), and a stated classification method** (citations bucketed into website / listing / reviews-social / news-other zones). **This is the most complete n/date/method disclosure found across any incumbent in this cluster (compare AirOps: partial; Conductor: none; HubSpot: engine + prompt-count + cadence but no wording; Yext's `/platform/scout` product page itself: no method disclosure).** However, this is a **category-level research study about AI citation behavior generally**, run on Yext's own aggregate citation database across its customer base — it is not a disclosure of the prompt set or sampling method behind the Scout product's own per-customer "visibility" or "AEO" score specifically. No page found this session states how many prompts, or what prompts, Scout itself runs per tracked brand or location.

## Pull notes — mechanical only

- Single fetch call, max_length 5000; truncated mid-paragraph ("...listings take 36.1 percent of OpenAI's, and reviews and social take 19.5 percent of Anthropic's against 2.6 for OpenAI."). Further findings (the sitemap listed three more related research pages — "Introducing Elo for Google Rank," "Profiles Performance," "AI Page Citations") were not fetched this session due to time/call budget across six incumbents.
- **`unknown — checked yext.com/platform/scout 2026-09-22` for Scout's own per-customer prompt-set/n/sampling-method disclosure** — distinct from and not resolved by this category-level research page.
