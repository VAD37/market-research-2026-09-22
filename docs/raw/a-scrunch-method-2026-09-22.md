# Scrunch AI — method / how it works

```yaml
source:          Scrunch AI (scrunch.com FAQs)
url_or_doc_id:   https://scrunch.com/faqs/what-methods-does-scrunch-use-to-collect-data-from-ai-platforms/ ; https://scrunch.com/faqs/how-does-scrunch-help-improve-brand-visibility-across-ai-platforms/
published:       undated — no date on page (FAQ format, no per-answer date stamp)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary FAQ/product page; no independent replication of the described method
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Gemini, Claude, and others (as named in the verbatim below)
metric_kind:     none
supersedes:      none
captured:        section "What methods does Scrunch use to collect data from AI platforms?" plus section "How does Scrunch help improve brand visibility across AI platforms?", each truncated at ~3000 characters per the tool's fetch cap
```

## Verbatim

### What methods does Scrunch use to collect data from AI platforms?

"Also asked as: Where does Scrunch get its data? / Is Scrunch data accurate?

Scrunch uses multiple methodologies to collect data from AI platforms like ChatGPT, Perplexity, Gemini, Claude, and others, including browser automation and official platform APIs.

Additional context: Scrunch uses the appropriate methodology for each AI platform. All data, regardless of collection method, is measured against a large and continually updated dataset of responses collected directly from inside AI platforms to make sure responses are accurately surfaced in Scrunch.

## Example

For example, imagine a Scrunch user tracks the prompt, 'How can I optimize my brand for AI search engines like ChatGPT?'

Scrunch will use platform-specific methodologies to collect responses across AI platforms and, via machine learning and natural language processing, display results, including:

* Brand presence in AI answers by percentage over a set time period
* Competitive presence in AI answers by percentage over a set time period
* Brand position in AI answers (e.g., top, middle, bottom) by percentage over a set time period
* Brand sentiment in AI answers (e.g., positive, mixed, negative) by percentage over a set time period
* Citations in AI answers (including the user's brand, competitors, and third parties) by percentage over a set time period

If you want to go deeper: Scrunch allows you to self-serve any combinat[note: truncated at 3000 characters]"

### How does Scrunch help improve brand visibility across AI platforms?

"Also asked as: How can Scrunch increase my AI search presence? / How does Scrunch optimize content for AI platforms?

Scrunch helps improve brand visibility by monitoring performance across AI platforms, auditing technical and content issues, optimizing content for AI consumption, and delivering AI-optimized content directly to AI user agents.

Additional context: Each step builds on the previous one—monitoring identifies problems, auditing diagnoses root causes, optimization fixes issues, and content delivery accelerates implementation without disrupting human website visitor experience.

## Example

For example, a Scrunch user at a B2B software company would improve brand visibility by:

Monitoring — They use Scrunch to track category-relevant prompts across major AI platforms. Monitoring reveals that they appear in only 23% of responses while competitors appear in 67%, with citation data showing specific weaknesses.

Auditing — Scrunch analyzes their webpages and identifies problems: robots.txt file issues, too much JavaScript, missing metadata, and more that makes content difficult for AI to access and interpret.

Optimization — The team updates low-performing pages using Scrunch's recommendations or uses Optimizer to enhance and restructure content automatically.

Content delivery — They enable Scrunch's Agent Experience Platform (AXP), which automatically serves AI-optimized versi[note: truncated at 3000 characters]"

## Pull notes — mechanical only

- Both FAQ pages fetched via mcp__MCP_DOCKER__fetch, simplified/markdown rendering, capped at 3000 characters each.
- The "23% vs 67%" figures in the second excerpt are stated as a worked example ("For example, a Scrunch user at a B2B software company would...") not a named real customer — not counted as a case study or a real-world number; flagged as an illustrative example, not evidence about an actual brand.
- No [note:] gaps beyond the fetch-cap truncation points marked inline above.
