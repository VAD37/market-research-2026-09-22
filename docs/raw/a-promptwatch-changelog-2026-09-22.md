# Promptwatch — changelog

```yaml
source:          Promptwatch (promptwatch.com)
url_or_doc_id:   https://www.promptwatch.com/changelog
published:       entries dated individually (latest captured: September 8, 2026)
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
captured:        section "changelog entries, September 2026 (Sept 8 back to Sept 1)" (page continues further back; truncated at the tool's per-call character limit, not re-fetched further this session)
```

## Verbatim

<p>Changelog | Promptwatch</p>Book a Demo

# Promptwatch Changelog

Stay up to date with the latest features, improvements, and announcements from Promptwatch. We're constantly working to make your AI search visibility tracking and optimization better.

## September 2026

**New Feature — September 8, 2026 — GEO 360: Topic Insights**

The 360 Dashboard has a new Topic insights tab. Every page on your site is grouped into topics, and each topic shows how many pages it covers and the average AI crawls, citations, and clicks those pages get. A bubble chart lays out the whole landscape, so you can see at a glance which topics AI engines pick up and which ones sit idle.

* Sort the landscape by most activity, most crawled, or most cited, and switch between averages and absolute numbers.
* Zoom from all topics into topic groups and subtopics, and click a bubble to open the pages, crawls, citations, and LLM citations behind it.
* Best, worst, and most popular topics are called out below the chart: which topics earn the most AI activity per page, which underdeliver for their footprint, and which cover the most pages.
* The first hundred topics load right away and the rest page in as you scroll.

**New Feature — September 8, 2026 — Competitor Sentiment Heatmaps**

Two new tabs on the Sentiment page show how AI talks about you next to your competitors. By topic lays out sentiment per brand for every topic you track. By competitor gives one row per brand with the sentiment split across positive, neutral, and negative, so you can see where a competitor wins the tone and you don't.

* Your own brand always sits in the first row, and picking specific competitors overrides the default cap.
* Both tabs share the brand picker and export button with the rest of Sentiment.

**New Feature — September 8, 2026 — LinkedIn Citation Tracking**

Socials now covers LinkedIn alongside Reddit and YouTube. See which LinkedIn posts and authors AI answers cite for your prompts, how often, and how that changes over time. Filter by prompt, topic, or tag, and export the table like any other citation view.

**New Feature — September 8, 2026 — API: Share of Voice, Models Filter & Docs Search in Agent Chat**

The REST v2 API and MCP server now return the same share of voice you see on the dashboard, on the responses summary and brand visibility endpoints. Response analytics and query fan-outs accept a models filter, and citation rank comes back as a 1-based answer position. Agent Chat can also search the Promptwatch docs, so questions about how a feature works get answered from the documentation instead of a guess. API docs.

**Bug Fix — September 8, 2026 — Bug Fixes & Stability Improvements**

A round of fixes across the platform to keep things running smoothly:

* Verified crawler data now uses historical IP ranges from each provider, so crawler visits from ranges a provider has since retired are counted again instead of being dropped.
* The team member list is only visible to organization owners. Members and viewers no longer see who else is in the organization.
* The onboarding checklist covers Bing Webmaster, Slack, and Agent Chat, and only owners see the invite teammates step.
* Links to actions, comments, and content gap reports open the right sheet on a hard page load.
* Applying prompt selections to all monitors stays in sync with what you picked.
* The feature explainer shows before announcements the first time you open a page.

**New Feature — September 7, 2026 — View Prompts by Topic**

The prompts page has a new By topic view. Each topic rolls up its prompts with average visibility, average sentiment, prompt count, and analyzed responses, and expands to show the prompts underneath. Filters work the same way as the default table, so a topic row always matches what you'd see when filtering the list.

**New Feature — September 7, 2026 — Custom Actions & Agent Replies in Comments**

The action board is no longer limited to what Promptwatch detects. Create your own actions with a title, description, severity, and status, edit them later, and dismiss accepted items so they leave the board but stay under dismissed actions. @-mention the agent in an action comment and it replies in the thread.

**New Feature — September 4, 2026 — GEO 360: Search Insights With Google & Bing**

The 360 Dashboard gets a Search insights tab that puts Google Search Console and Bing Webmaster performance next to your AI data. See clicks, impressions, and top queries per page, split branded from non-branded queries, and open a page to compare its search traffic with AI crawls and citations.

* Weekly windows snap to full weeks, and a banner tells you which date range the search numbers cover.
* Page detail sheets keep the row's totals in the header and cache their live lookups, so opening a page doesn't refire Google and Bing calls.

**Improvement — September 2, 2026 — Content Agent: Meta Titles & Page Tracker Filter**

Articles now have a separate meta title. The editor labels the old title as H1 and adds a meta title field that falls back to the H1 when empty. Webflow and Framer field mappings can point at it, and it comes back in the REST v2 and MCP content responses. Page Tracker can filter to pages that came out of the Content Agent, and the competitor picker in the content brief shows how many unique citations each competitor has for the selected prompt.

**Announcement — September 1, 2026 — Earn Agent Credits With a G2 Review**

Organizations on Essential or Professional can submit a G2 review from the sidebar. Once approved, you get 2,000 extra agent credits every month for Agent Chat and the Content Agent.

**New Feature — September 1, 2026 — New Free AI Visibility Report**

Enter a website and watch a live scan of how AI talks about the brand. The report reads robots.txt, extracts what AI thinks you do, then asks real engines the questions buyers ask. In a couple of minutes you get scores for visibility, mentions, position, citations, and whether AI crawlers can actually read the site.

[note: content truncated by the tool's max_length limit at this point; page continues further back before September 1, 2026. Not re-fetched with a higher offset this session — the captured range establishes a very active September 2026 release cadence (9 entries in 8 days) and is what is cited.]

## Pull notes — mechanical only

- Fetched via plain fetch tool (raw=false, markdown-simplified HTML), max_length 6000, truncated after the "New Free AI Visibility Report" entry. Browser extension unavailable this session.
- Engines named in this excerpt: ChatGPT (implicitly, via general "AI" references), Google Search Console and Bing Webmaster named as distinct integrations, not AI engines. No explicit per-engine breakdown in this excerpt beyond "AI crawls, citations, and clicks".
- Confirms an active, near-daily shipping cadence in September 2026 (9 dated entries across September 1, 2, 4, 7 and 8) — vendor-reported, not independently verified.

## Caveats

- Changelog entries are vendor-authored release notes — company-stated, tier 3 on existence of features and their ship dates.
