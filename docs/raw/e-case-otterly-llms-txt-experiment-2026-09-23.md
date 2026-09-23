# OtterlyAI — llms.txt experiment (90 days)

```yaml
source:          OtterlyAI (otterly.ai) blog
url_or_doc_id:   https://otterly.ai/blog/the-llms-txt-experiment/
published:       2026-02-05 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, browser User-Agent); links read from otterly.ai/case-studies and otterly.ai/blog/geo-gsvo/
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-published case or experiment with n/dates/method stated; vendor measuring with its own product, no third-party replication — bias flagged
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          AI / LLM user agents (not broken out in captured text)
metric_kind:     crawler visits
supersedes:      none
captured:        article body from 'Last updated' line to related-posts footer
verbatim:        partial — section named in captured
```

## Verbatim

> Last updated February 5, 2026
> GEO Experiments
> Will llms.txt actually improve your AI visibility?
> In this OtterlyAI research piece, we test real AI crawler data to see whether llms.txt meaningfully affects how AI systems discover and use web content.
> Study Methodology
> About This Research: OtterlyAI implemented an /llms.txt file at the root of an experiment website and monitored AI bot traffic over a continuous 90-day period. Server logs captured data from AI- or LLM-oriented user agents (excluding generic crawler noise) to focus specifically on visits from AI search engines, AI assistants, and LLM-integrated tools that indicate generative use cases. For each AI bot request, the study tracked: the requesting bot (user agent/IP classification), the requested URL, timestamp, and frequency across the full 90-day window. The analysis measured total AI bot hits across the entire site, how many hits targeted /llms.txt specifically, and how /llms.txt visitation compared to normal content pages to determine whether the presence of an llms.txt file meaningfully changes AI crawler behavior.
> Key Findings (TL;DR)
> Only 0.1% of AI bot traffic accessed /llms.txt: Out of 62,100+ total AI bot visits over 90 days, just 84 requests targeted the /llms.txt file.
> llms.txt performed 3x worse than average pages: The site’s average content page received ~265 AI bot visits during the same period, while /llms.txt received only 84 visits.
> llms.txt ranks near the bottom for AI crawler interest: In a ranked list of most frequently crawled URLs, /llms.txt would sit near the bottom, far from being a primary AI touchpoint.
> No positive correlation between llms.txt presence and increased AI crawler activity: The presence of a correctly implemented llms.txt file did not correlate with any noticeable uptick in overall AI bot activity or shift in crawling patterns.
> Major AI platforms don’t rely on llms.txt: This aligns with Google’s statements that it doesn’t use llms.txt and with broader evidence that no major LLM provider has adopted the standard at scale.
> llms.txt isn’t privileged content: It receives no higher crawl priority than static assets like PDFs, indicating AI crawlers don’t treat it as a special signal.
> Context: The Hype Around llms.txt
> Over the past year, llms.txt has gone from a niche developer proposal to a recurring topic in SEO, GEO (Generative Engine Optimization), and AI search discussions. The core idea, originally proposed by Jeremy Howard , is simple: place a standardized Markdown file at /llms.txt to give large language models (LLMs) a clean, structured overview of your site so they can use it more effectively at inference time.​
> Crucially, the original proposal is about helping LLMs read and use your site more easily , not about manipulating rankings in Google AI Overviews, Perplexity, or ChatGPT-style answer boxes. Despite that, a growing number of SEO tools and blog posts have started positioning llms.txt as if it were the next robots.txt or XML sitemap for AI search.​
> To move this conversation from theory to data, OtterlyAI ran a 90‑day experiment to answer a narrow question:
> Does adding an llms.txt file meaningfully change how AI search crawlers visit and interact with a website?
> Experiment Design: How We Tested llms.txt
> OtterlyAI implemented an /llms.txt file at the root of the experiment website and monitored AI bot traffic over a continuous 90‑day period. The file was directly accessible from the website’s homepage. The focus was not on generic crawler noise, but on visits from AI- or LLM‑oriented user agents (e.g., AI search engines, AI assistants, and LLM-integrated tools) that indicate generative use cases.
> For each AI bot request, server logs captured:
> The requesting bot (user agent / IP classification)
> The requested URL
> Timestamp and frequency over the 90‑day window
> From this, OtterlyAI measured:
> Total AI bot hits across the entire site
> How many of those hits targeted /llms.txt
> How /llms.txt compared to “normal” content pages in terms of AI bot visitation
> This is exactly the kind of log‑level evidence that has been missing in much of the llms.txt debate.
> Headline Numbers: 62.1K AI Bot Hits, 84 to llms.txt
> Across 90 days of the experiment:
> Total AI bot visits to the site: 62,100+
> Total AI bot visits to /llms.txt: 84
> Share of AI bot traffic that went to /llms.txt: ~0.1%
> AI Bot Crawl Comparison llms.txt vs robots.txt :
> Even more telling:
> The site’s average page received around 265 AI bot visits in the same window.
> At just 84 visits, /llms.txt performed well below a typical page from the perspective of AI crawlers.
> /llms.txt hardly preformed better than an average .pdf file.
> In a ranked list of the most frequently crawled URLs, /llms.txt would sit near the bottom, far from being one of the primary AI touchpoints.
> In other words: as far as the bots are concerned, llms.txt is almost invisible.
> What the Data Actually Tells Us
> Despite the presence of a correctly implemented /llms.txt file, AI crawlers rarely requested it. Over three months and more than sixty thousand AI bot hits, the dedicated LLM entrypoint was used in just 0.1% of AI visits.
> This leads to a clear, evidence-backed conclusion for AI search behavior today :
> llms.txt is not a significant driver of AI crawl behavior.
> AI agents are overwhelmingly discovering and consuming content via standard web pages and existing site structure, not via llms.txt.
> The presence of llms.txt did not correlate with a noticeable uptick in AI bot activity, nor did it shift robots’ crawling patterns in any meaningful way.
> These findings are consistent with broader ecosystem signals. Independent analyses of llms.txt adoption have found hundreds of sites experimenting with the standard, but no major LLM provider has publicly committed to using it at scale , and Google has explicitly stated that it does not rely on llms.txt for AI features, comparing it to the deprecated keywords meta tag. Log audits from SEOs have similarly shown that many language-model‑branded bots either do not appear at all or very rarely request /llms.txt on participating domains.
> Taken together, OtterlyAI’s experiment fits into a larger pattern: there is a grassroots appetite to publish llms.txt, but very limited evidence that leading AI search systems read or rely on it today.
> Why AI Search Bots Don’t “Need” llms.txt (Yet)
> To understand why the experiment shows negligible impact, it helps to revisit what the llms.txt standard is actually for.
> According to the official proposal, llms.txt is:
> “A proposal to standardise on using an /llms.txt file to provide information to help LLMs use a website at inference time.”​
> Key implications:
> It is not an indexing protocol like robots.txt or XML sitemaps.
> It is an inference‑time helper: a curated, LLM‑friendly overview of key content, often linking to clean Markdown or structured text versions of important pages.
> It exists to solve a technical pain for LLMs: HTML is noisy, full of navigation, pop‑ups, scripts, and boilerplate that LLMs must strip before they can reason over the actual content.​
> Major platforms such as Google, Perplexity, and large commercial LLM providers already have robust content extraction, crawling, and ranking pipelines. They do not need llms.txt to de‑noise a page or identify main content blocks; they already invest heavily in doing exactly that at scale.
> From that perspective, the OtterlyAI results are unsurprising:
> AI search engines continue to rely on their existing crawl infrastructure and ranking models, not on a new, optional hint file that few sites have implemented.
> llms.txt, as a proposed standard, is still in an early, experimental stage. The ecosystem of bots that meaningfully use it is small and fragmented compared to the dominant AI and search players.
> What Marketers Get Wrong About llms.txt
> A key source of confusion is framing . Many marketers and SEOs have come to see llms.txt as a new GEO lever: a way to boost visibility in AI overviews and answer engines. That’s not how the standard was designed, and treating it like that leads to misplaced expectations and disappointment.
> Jan Schulte , an AI engineer,  has articulated this disconnect clearly in his discussion of llms.txt: most marketers view it as an SEO feature, when in reality it is a developer‑friendly way to make website content cheaper and easier for AI tools to consume.​
> Misconception: “llms.txt is for AI rankings”
> The common mental model goes something like this:
> “robots.txt controls crawlers; sitemaps help with discovery; therefore llms.txt will control or improve my visibility in AI search answers.”
> The problem with that analogy:
> The official spec never promises better visibility in AI search.
> Major players like Google and leading LLM providers have not adopted it for ranking or answer generation.​
> Crawlers already know how to strip boilerplate, parse layout, and isolate main content blocks without any help from llms.txt.
> Result: SEOs implement llms.txt, watch logs for a short period, see almost no bot traffic to the file (as OtterlyAI did), and conclude it “doesn’t work” — when in fact they were measuring it against the wrong objective.
> Reality: It’s About Reducing Friction for AI Tools
> Where llms.txt does make sense is for the thousands of AI‑powered tools, apps, and vertical products that integrate web content but don’t have Google‑scale crawling infrastructure.
> For these tools:
> Pulling raw HTML and cleaning it up on the fly is computationally expensive and messy.
> Calling a search API (e.g., from a major LLM vendor) to fetch and process a page can cost $10–$14 per 1,000 searches, which adds up quickly at scale.​
> When a user or integrator wants a specific page (e.g., your docs, pricing, or API reference), a pre‑curated Markdown snapshot is both faster and cheaper for them to use.
> In that context, llms.txt is a courtesy and an optimization layer:
> It tells tools: “Here is a clean, minimal, LLM‑ready representation of our most important content.”
> It reduces token counts (no cookie banners, pop‑ups, footers, or analytics noise), which in turn reduces latency and cost and often improves answer quality for users interacting with AI tools that rely on your content.​
> It makes your site “plug‑and‑play” for third‑party AI products that want to integrate or surface your content without building full-scale crawling and extraction pipelines.
> This is why some SaaS companies have already introduced “copy to Markdown” buttons or similar UX patterns: they make it trivial for users (and the tools they use) to move from HTML to a clean, LLM‑friendly representation of the page.​
> In short: llms.txt is infrastructure for AI integrations, not a ranking factor for AI search.
> Recommendations for Marketers and SEOs
> Combining OtterlyAI’s experiment with the broader ecosystem evidence, a few practical conclusions emerge.
> 1. For AI search visibility, llms.txt is not a lever today
> In OtterlyAI’s data, only 0.1% of AI crawler requests touched /llms.txt over 90 days.
> The file received far fewer AI visits than the average content page.
> Independent log studies and ecosystem analyses echo the same pattern: mainstream AI search and LLM providers are not meaningfully relying on llms.txt at this time.
> If your goal is to increase citations and mentions in AI overviews and answer engines, your effort is better spent on:
> Strong content and topical coverage
> Earning citations and references across the web
> Structuring content clearly and semantically
> Monitoring which queries and answers actually cite your brand (which is exactly what OtterlyAI specializes in)
> 2. Treat llms.txt as experimental infrastructure, not a core SEO requirement
> Given the current usage patterns, llms.txt should be seen as:
> Low risk, low cost, experimental: there is little downside to having it, but also little immediate upside in terms of AI search visibility.
> A nice‑to‑have component for developer‑heavy, documentation‑rich, or integration‑oriented sites that want to be friendly to AI tools and third‑party developers.
> A future‑oriented bet: if more LLM vendors and AI tools start supporting the spec, early adopters will already be prepared.
> But it is not something that should displace core SEO work or become a primary KPI in your AI search strategy.
> 3. The real opportunity is in AI-powered products, not search pages
> Where llms.txt is most aligned with marketing impact is in the growing ecosystem of AI:
> Product copilots embedded in SaaS
> Support bots leveraging your docs
> AI‑assisted analytics and BI tools
> Niche AI tools that rely on external knowledge bases
> For these use cases, llms.txt can:
> Lower integration friction: partners and tools can ingest your content without writing custom scrapers.
> Reduce compute and token costs: clean Markdown means fewer tokens and faster responses.
> Improve reliability: curated lists of key resources reduce the chance that tools latch onto outdated or irrelevant pages.
> This is where marketers and product teams should evaluate llms.txt: as a way to make their site a better data source for AI products used by their customers, not as a dial to turn for rankings inside Perplexity or ChatGPT.
> Should You Implement llms.txt Anyway?
> Based on the experiment and current ecosystem:
> If your goal is AI search visibility (GEO/SEO):
> Implementing llms.txt will likely have no measurable short‑term impact. Focus instead on the fundamentals of AI discoverability: high‑quality content, strong entity coverage, and monitoring how AI engines actually cite and describe your brand.
> If you have documentation, APIs, or content that others integrate into their own AI tools:
> Implementing llms.txt can be a smart, future‑proof move. It positions your site as easy to integrate, lowers friction for partners, and may improve the quality and consistency of AI‑driven experiences built on top of your content.
> If you’re resource‑constrained:
> Treat llms.txt as a secondary priority. It is worth exploring when you have the basics covered,  not instead of them.
> A practical middle ground is:
> Create a lean, curated /llms.txt that:
> Summarizes your product or site.
> Lists your most important docs, guides, and reference pages.
> Points (where relevant) to clean Markdown or structured versions of those resources.
> Monitor server logs specifically for AI‑branded bots and /llms.txt requests over time, just as OtterlyAI did, to see if adoption patterns change.
> Final Conclusion: llms.txt Is Not Dead, But It’s Not a GEO Lever
> OtterlyAI’s 90‑day experiment shows no significant impact of llms.txt on AI crawler behavior: just 84 AI bot visits to /llms.txt out of 62.1K total AI bot hits, far below the site’s average page. This aligns with broader evidence that most major AI search and LLM systems are not yet using llms.txt as a key input.
> The right way to interpret this is not “llms.txt is useless,” but rather:
> llms.txt is currently a niche, integration‑focused standard, not a primary touchpoint for AI search crawlers.
> Its impact on AI search visibility is marginal at best today and should be considered experimental.
> The marketing opportunity lies in making your content cheaper, faster, and easier for AI tools to process, not in chasing rankings inside AI answer boxes.
> For SEOs and GEO practitioners, the takeaway is clear: keep your eyes on real‑world AI citations, monitor how generative engines actually use your content, and treat llms.txt as a supporting file for AI integrations, not a magic switch for AI search.
> In fact, this is one of the reasons we’ve removed the LLMs checker from our GEO Audit . While llms.txt can have niche value for certain AI integrations, its current impact on AI crawler behavior and discovery is marginal at best, and it shouldn’t distract from the fundamentals that truly drive AI visibility and crawl effectiveness.
> If you haven’t yet, check out our updated GEO Audit Guide — now optimized to focus on crawlability, content quality, and real-world signals that matter for both human and AI traffic:
> 👉 OtterlyAI’s New GEO Audit: Crawlability & Content Checker
> Social Share or Summarize with AI ChatGPT Google AI Perplexity Claude Gemini X (Twitter) LinkedIn
> Related Posts:

## Pull notes — mechanical only

- Server-rendered page; tag-stripped, one line per block element; figures and embedded video not captured.
- Provenance: new — found via otterly.ai/blog/geo-gsvo/.
