# Ahrefs — method / how-it-works (Brand Radar FAQ)

```yaml
source:          Ahrefs (ahrefs.com)
url_or_doc_id:   https://ahrefs.com/brand-radar (FAQ section)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary; this is a methodology disclosure, not a proof-of-lift claim, so trust-rubric's vendor-study caveats for case studies do not apply the same way — recorded as platform primary
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        FAQ section, two fetch calls (start_index 6000 and 9000) covering four of an unknown total number of FAQ entries
```

## Verbatim

"## Questions? We have answers

**How is AI visibility measured in Ahrefs Brand Radar?**
Brand Radar measures AI visibility by running 454M+ search-backed prompts through AI platforms (AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini, Copilot) and storing every response. Your visibility is then calculated from how often your brand is mentioned or cited in those responses, with these key metrics:
- **Mentions** – how often your brand name appears in AI answer text
- **Citations** – how often AI links to your pages or domains as a source
- **AI Share of Voice** – the percentage of AI responses within your topic set that mention or cite your brand versus competitors
- **Estimated Impressions** – potential visibility weighted by the real search volume behind each prompt

**What's the difference between the AI Visibility Index and Custom Prompts?**
The AI Visibility Index maps how brands appear across millions of pre-collected AI responses, instantly, with no setup. It's ideal for benchmarking share of voice and discovering topics you didn't know AI was answering. It works best for established brands or topics with meaningful search demand, since the index is built on Ahrefs' keyword database and may have limited coverage for brands with little or no search volume.

Custom Prompts are specific buyer questions answered by the AI platforms that matter to your pipeline, defined and set up by you, populated with data from the moment you start tracking. Brand Radar runs them on demand as often as daily. They are great if your brand is not well-known, or you have uncommon queries to track.

**How does Ahrefs Brand Radar collect AI visibility data?**
Brand Radar builds two distinct kinds of indexes:
- **Prompt-based indexes** (ChatGPT, Perplexity, Gemini, Copilot, AI Overviews, AI Mode). Ahrefs takes real queries from its keyword database, expands them into natural questions via People Also Ask and semantic fanout, then runs the resulting 454M+ prompts through each AI platform and stores the responses.
- **Search-query-based indexes** (AI Overviews and AI Mode only). Instead of asking AI a question, these track the keywords that trigger an AI answer inside Google Search, and whether your brand appears in it. They exist only for AI Overviews and AI Mode, because those are the only AI surfaces that show up in Google's own results.

**Question sets are re-tested monthly on a 90-day reporting window.** Because both index types derive from real search demand, not synthetic guesses, the visibility metrics reflect what people really ask.

**What kind of queries can I track in Ahrefs Brand Radar?**
Brand Radar tracks AI visibility across two query types, filterable by platform:
- Prompts – long-tail natural-language questions available for ChatGPT, AI Overviews, AI Mode, Gemini, Perplexity, Copilot, and **Claude**.
- Search queries – short queries that triggered an AI answer in Google (via AI Overview or AI Mode). Brand Radar tracks whether your brand appears in it. This type only covers AI Overviews and AI Mode, because they're the only ones that show up inside Google Search.

**Can I backtrack my AI visibility data to my SEO strategy?**
Yes. Every prompt in the Index maps back to real search demand, on two levels:
- Search demand – the branded keywords behind your mentions, so you can see the actual query volume driving your AI visibility.
- Topics – clustered keywords that group related queries, so you can see which high-volume topics trigger AI answers, which pages and domains get cited, and where your content is (or isn't) feeding AI responses.

Brand Radar also tracks the social channels that influence AI answers (Reddit threads ranking in Google and YouTube).

**Do I need to set anything up or wait for data to collect?**
For the AI Visibility Index, you don't have to set anything up. You can immediately search any brand, product, or entire category, including **historical responses back to 2025**, and no domain cap.

If you choose Custom Prompts, you have to configure them yourself. The data starts to accumulate from that point. You can choose the ch[...]" [note: content truncated by the fetch tool at this point]

## Prompt-set / n / method disclosure assessment

**Disclosure verdict: yes — the most complete methodology disclosure found across any incumbent in this cluster.** Ahrefs discloses: total n (454M+ prompts, broken down per-platform on the product page: AI Overviews 312.8M, Gemini 31.3M, Perplexity 31.2M, ChatGPT 31.2M, Copilot 30.8M, AI Mode 16.9M); the prompt-generation method (real queries from Ahrefs' own keyword database, expanded via "People Also Ask and semantic fanout"); a re-test cadence ("re-tested monthly on a 90-day reporting window"); a historical-data start point ("back to 2025"); and four explicitly defined metrics (Mentions, Citations, AI Share of Voice, Estimated Impressions). The one gap: the **actual prompt wordings** themselves are not published (they are auto-generated from Ahrefs' proprietary keyword database, not a shared, citable benchmark list) — so this is disclosure of *method and scale*, not a publicly inspectable *prompt-set document*.

## Pull notes — mechanical only

- Two fetch calls (start_index 6000, then 9000); the second call was truncated mid-sentence ("You can choose the ch..."), so the FAQ is not confirmed complete — `unknown — checked ahrefs.com/brand-radar 2026-09-22` for any FAQ entries beyond the six captured here.
