# Peec AI — changelog

```yaml
source:          Peec AI (peec.ai)
url_or_doc_id:   https://peec.ai/changelog
published:       entries dated individually (latest captured: Aug 3, 2026)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — vendor's own changelog, existence/feature facts
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        section "changelog entries, Aug 3 2026 back to Jul 6 2026" (page continues further back; truncated at the tool's per-call character limit, not re-fetched further this session)
```

## Verbatim

<p>Peec AI Changelog</p>

# Changelog

The latest improvements and behind-the-scenes updates from the Peec AI team.

Subscribe — Get a bi-weekly roundup of Peec AI product updates, and improvements

Aug 3, 2026
## Brand Perception is now live for everyone, plus a new Ads page

Visibility tells you whether AI mentions your brand. It does not tell you what the model actually says about you. When an engine is asked about your category it does not just list brands, it describes them, and those descriptions are what buyers act on.

Brand Perception is out of early access and available to everyone. It keeps two questions apart on purpose. What AI associates you with gives each attribute an association score. Where you hold ground against competitors gives every brand a market prominence score. Both run 0 to 100 and they are not comparable, which is exactly what makes the gap between them useful: you can be described as fast constantly and still lose "fast" to every competitor in your market. The summary names your top attribute, your strongest against competitors, and the biggest gap of the two. Find it under Brand in the sidebar.

### A new Ads page
ChatGPT shows sponsored ads inside some answers, so paid placement can sit in the same response as your organic mention. The Ads page shows every ad we captured on your tracked prompts: who is advertising, what they are promoting, which pages they send people to, and how often they appear. You also get advertisers in market, who is bidding on your branded and comparison prompts, and your ad coverage. A Partner column separates platform-bought placements from ads a brand booked directly. ChatGPT only for now. The docs walk through the page.

### Brand Perception in the API and the MCP
Brand Perception data is now queryable through the Customer API and the MCP server. An agent can pull your attribute scores, your competitive ranks, and the sources behind each attribute, then turn them into a content brief or a monthly report without you exporting anything. Ask Claude what your category associates you with and where you are losing ground, and it reads the same numbers the page shows. Setup docs.

### Sources in AI Shopping
The Shopping overview and each product page now show the domains and URLs behind the answer, the same source view you get everywhere else in Peec. When your product turns up in a carousel, this is how you find out which retailer or review page is doing the work, which is usually where the off-site brief starts.

### The command palette is now generally available
Command or Ctrl plus K opens the palette from any page at any time. It came out of early access this window and picked up real depth on the way: you can drill from a prompt into the domains and URLs it cites without leaving the palette, and every list now pages all the way through instead of stopping at the first twenty results.

### Early Access is now self-serve
Activate Early Access in your company settings to turn these on yourself. Prompt Builder is a guided setup that generates a prompt set for your brand and shows you the branded, non-branded, intent and persona split before you accept anything. New navigation regroups the left nav around how you actually work, so Results, Prompts, Sources and Brand each have a home. Crawlability history tracks how your robots.txt changed over time and lets you replay an earlier snapshot to see which AI crawlers you were allowing or blocking then.

Improvements
* Total citations and Citation share are now optional columns on the Domains and URLs tables, from the column picker
* Position is back on the URL and domain tables
* You can switch the industry your Brand Perception attributes are benchmarked against, when the category we inferred is not the right one
* Merchant data is now available through the Customer API and the MCP server
* Product variants are now available through the Customer API and the MCP server
* The category filter works on non-shopping pages too, with a toggle to set it across all of them at once
* The project switcher has a dedicated Projects tab, and switching projects keeps you on the same page instead of sending you back to the overview
* Long prompts now wrap in the prompt column instead of truncating
* Large numbers are shortened across the Agent Analytics pages
* API model selection is available on Scale and above
* Unsupported Looker Studio filters now warn instead of failing silently
* AI Mode is now tracked in France, so French prompts return AI Mode results

Fixes
* Fixed the Sources URL brand filter returning rows with no visible brand mentions
* Fixed prompt filtering on the Ads page for projects where every captured ad is ChatGPT-only
* Fixed Ads grouping breaking in some cases
* Fixed Prompt Builder generating topics in the brand's language instead of the market language you selected
* Fixed an empty "Retrievals by model" panel in URL analytics
* Fixed missing sentiment and position values
* Fixed the country filter showing stale countries that no prompts still use
* Fixed inconsistent day definitions across the Crawl Insights widgets
* Fixed "show errors only" in the CSV upload preview
* Fixed instant pitch projects that could get stuck
* Fixed Prompt Builder early access overwriting brand profile edits

Jul 6, 2026
## A new Query Fanouts page, plus AI Shopping in the MCP

When an AI engine answers one of your prompts, it quietly runs its own web searches first, then writes the answer from what it finds. Until now those searches were invisible, so you were optimizing for the answer without knowing what the model actually looked for to build it.

Query Fanouts is a new page that shows you exactly those searches. See the number of distinct fanout queries, filter them by type (Search, Shopping, Synthetic), and group them by topic or prompt. It surfaces which brands the engines name most often inside their searches and the word sequences that come up again and again, so you know what the models

[note: content truncated by the tool's max_length limit at this point; page continues further back before Jul 6, 2026. Not re-fetched with a higher offset this session — the captured range (Aug 3 back to Jul 6, 2026) is sufficient to establish an active release cadence and is what is cited.]

## Pull notes — mechanical only

- Fetched via plain fetch tool (raw=false, markdown-simplified HTML), two overlapping calls spliced (max_length 6000 from index 0). Browser extension unavailable this session.
- Confirms "Add extra models anytime" ChatGPT-ads tracking as a named ChatGPT-specific feature ("ChatGPT shows sponsored ads inside some answers... ChatGPT only for now"), corroborating lane B evidence already landed elsewhere in this research programme (OpenAI's own ad-product pages, P2-c3).
- Engines named in this excerpt: ChatGPT, AI Mode (France-specific tracking added), plus a general "Claude" mention in the MCP-integration paragraph ("Ask Claude what your category associates you with").
- "Mistral" and "Meta Spark" named as Enterprise-tier add-on models on the pricing page but not mentioned in this changelog excerpt.

## Caveats

- Changelog entries are vendor-authored release notes — company-stated, tier 3 on existence of features and their ship dates.
