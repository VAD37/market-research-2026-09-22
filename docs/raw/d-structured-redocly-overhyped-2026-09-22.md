# Redocly blog — "LLMS.txt is overhyped" (Adam Altman, CEO and Founder, Redocly)

```yaml
source:          Redocly (redocly.com blog)
url_or_doc_id:   https://redocly.com/blog/llms-txt-overhyped
published:       2025-08-20 (byline date)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     vendor blog (Redocly sells API-documentation tooling and built the llms.txt feature it tested); named author and a stated general method ("full Phronesis project," "pulled logs") but no disclosed n, no named model list, no date window, no third-party replication. Meets trust-rubric.md's discard-on-sight pattern for missing n/date/method; kept only as category-noise/practitioner-corroboration evidence per pull_purpose, never as a number
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Unnamed — "across models" tested, no specific engine or model version named anywhere in the post
metric_kind:     none
supersedes:      none
captured:        full page (blog post body)
```

## Verbatim

By Adam Altman, August 20, 2025, CEO and Founder, Redocly

"LLMS.txt is overhyped"

"Every now and then, the industry invents a new "standard" that's supposed to solve everything. Right now the hype train is parked at llms.txt. People call it the robots.txt for AI. Cute analogy. The problem is: it doesn't actually work that way."

"We built it anyway — At Redocly, we like to experiment. So we added automatic llms.txt support to our platform. Turn it on, it generates the file. Easy. We even ran a full Phronesis project on it — testing across models, prompts, and scenarios. The results? Pretty underwhelming. Unless you explicitly paste the llms.txt file into the LLM, it doesn't do anything. When you do paste it, you'd get better results just pasting the actual Markdown docs. **No model we tested spontaneously "read" or respected llms.txt on its own.** That's not a governance breakthrough. That's a parlor trick."

"The logs don't lie — We also pulled logs. How often are llms.txt and llms-full.txt even being accessed? Answer: basically never. When they are, it looks like someone experimenting in a single LLM session, not systematic use by the models. Michael O'Neill at the University of Iowa checked too — same conclusion: don't lose sleep over llms.txt."

"The silver lining — The best thing about building llms.txt wasn't llms.txt. It was what came after: one-click copy of any page in Markdown, links you can drop straight into ChatGPT or Claude, smooth handoff from docs → AI assistant. That's useful today. That's how people actually want to interact with docs in an AI-first world."

"A tale of two experiments — Not all experiments flop. Last week, we ran another Phronesis project, this time on two of our new MCP features (not yet public). The difference was night and day. With Docs MCPs, we saw real value. They made docs instantly more useful inside AI workflows. The debriefs weren't full of head-scratching like with llms.txt — they were full of smiles. That's the difference between smoke and fire. LLMS.txt is smoke. Docs MCPs are fire."

"What really matters — Focus on making good content. If we want content governance in AI, it won't come from a text file no one reads. It'll come from: licensing, attribution, legal clarity, real standards AI companies can't ignore. Until then, llms.txt is just… there. More checkbox than standard."

"My take — We tried it. We measured it. We learned from it. And now we can say it out loud: llms.txt is overhyped. The sooner we move past the illusion, the sooner we can focus on solutions that actually matter."

## Pull notes — mechanical only

- Discovered via a link inside `d-structured-llmstxtio-adoption-blog-2026-09-22.md`'s citation list; fetched directly with `curl`. Page is a heavy client-side-styled blog (large inline CSS-in-JS payload, ~343KB raw HTML for one blog post) but the article body text rendered in the static HTML and was extracted with `sed`-based tag-stripping without needing a browser.
- **Corroborates, in direction, both `d-structured-arxiv-borysenko-http-fingerprints-2026-09-22.md`'s measured finding (zero llms.txt requests observed in a controlled test) and the John Mueller quote reported secondhand in `d-structured-llmstxtio-adoption-blog-2026-09-22.md`** ("The consumer LLMs/chatbots will fetch your pages... but none of them fetch the llms.txt file") — three independent sources (one measured/tier-4, one platform-primary/tier-3, one vendor-practitioner/tier-6) converge on the same direction: no engine spontaneously reads or acts on llms.txt as of the respective check dates (2026-07 Google statement, Feb–Mar 2026 measured study, this 2025-08-20 vendor test).
- No n disclosed for "testing across models, prompts, and scenarios" (how many of each), no list of which specific models were tested, no date window for when "we pulled logs" or over what period, and no third-party replication — this is why the pull sits at tier 6 rather than tier 5 despite naming a real author and company. Filed per `pull_purpose: evidence about category noise` only, never as a number.
- Author (Adam Altman) is Redocly's CEO/founder; Redocly is an API-documentation platform, not itself a seller of llms.txt-optimization or GEO/AEO services — the "vendor measuring what it sells" bias is present but weaker/more oblique than in `d-structured-arxiv-volpini-rag-2026-09-22.md`, where the vendor's own product is the exact thing being tested favourably. Here the vendor's own test result is *negative* on the standard it built support for, which trust-rubric.md notes raises trust ("Result runs against the publisher's commercial interest") — Redocly had a commercial reason to report llms.txt working (they built and shipped the feature) and instead reported it does not.
- No mention of schema.org or product feeds anywhere on this page — llms.txt only.
