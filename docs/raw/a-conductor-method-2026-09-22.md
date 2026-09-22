# Conductor — method / how-it-works (AI Search Performance)

```yaml
source:          Conductor (conductor.com)
url_or_doc_id:   https://www.conductor.com/platform/intelligence/ (AI Search Performance feature description + FAQ)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        full page text (two fetch calls, 0-6000 and 6000-onward, second call truncated)
```

## Verbatim

"AI visibility tracking — See your brand's visibility across any AI search surface — Track your mentions, citations, and sentiment in AI answer engines like ChatGPT and Perplexity, right alongside your performance in traditional search."

"Track your brand's visibility in AI search — AI Search Performance — Measure how your content appears in answer engines like ChatGPT and Perplexity, analyze intent and sentiment, and identify critical opportunities to win."

"## Frequently asked questions

Point tools only show you a piece of the puzzle—typically just basic visibility tracking. Conductor Intelligence is a complete, unified platform. We connect your AI visibility to the rest of your performance data (website analytics, technical data, traditional SEO) so you can measure the actual business impact and ROI of your efforts, not just vanity metrics.

Tracking AI mentions and citations tells you if you're part of the conversation, but it doesn't tell you if you're driving business. By unifying AI visibility with your website analytics (like GA4 and Adobe), you can see if that visibility is actually leading to traffic, engagement, and conversions. Conductor is the only platform that provides this connected view, allowing you to prove the ROI of your AEO strategy.

Yes, Conductor is designed for enterprise scale. Our plat[form...]" [note: truncated by the fetch tool at this point; remaining FAQ answers not captured]

**Named metrics:** "mentions, citations, and sentiment" — kept as three separate named metrics, not summed into a single composite/branded score name (no "Visibility Score" or equivalent index name found on this page). "AI Search Credits" (seen on `a-conductor-pricing-2026-09-22.md`) is the billing unit for this feature but is not described as a score.

**Engines named on this page:** "ChatGPT and Perplexity" (twice, identically, in both the hero copy and the feature-highlight copy). No other engine is named on this specific page — contrast with the homepage ("ChatGPT, Gemini, Copilot, Claude, and traditional search") and the "Free AI Visibility Report" CTA ("ChatGPT, Perplexity, Google AI Overviews, and more") — see `a-conductor-product-2026-09-22.md`. The engine list Conductor states is **inconsistent across its own pages**, recorded as found.

**Prompt-set / n / method disclosure:** No prompt set, prompt count, run count (n), sampling frequency, or model-version methodology is disclosed anywhere on this page. The FAQ addresses *what* is measured (mentions, citations, sentiment, tied to traffic/conversions) and *why* it matters, but not *how* — no description of how many queries are run, how often, or against which engine surface (consumer chat vs. API). **Disclosure verdict: no, undisclosed** — `unknown — checked conductor.com/platform/intelligence 2026-09-22` for prompt set, n and sampling method. (Pricing page's "AI Search Credits / Year" figure, e.g. "2,500 AI Search Credits / Year" for Growth, is a billing quota, not a stated prompt-set size or run count — see `a-conductor-pricing-2026-09-22.md`; whether one "credit" equals one prompt-run is not stated anywhere pulled.)

## Pull notes — mechanical only

- Second fetch call (start_index 6000) hit the tool's per-call limit again mid-FAQ-answer; the third and later FAQ answers referenced by the page's own anchor list were not captured.
- No separate "how it works" / methodology / docs subdomain (e.g. `help.conductor.com`) was checked this pull — `unknown — checked conductor.com/platform/intelligence only 2026-09-22`.
