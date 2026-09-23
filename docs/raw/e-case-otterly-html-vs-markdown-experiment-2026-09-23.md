# OtterlyAI — HTML vs Markdown GEO experiment (14 days)

```yaml
source:          OtterlyAI (otterly.ai) blog
url_or_doc_id:   https://otterly.ai/blog/geo-experiment-html-vs-markdown/
published:       2026-04-01 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, browser User-Agent); links read from otterly.ai/case-studies and otterly.ai/blog/geo-gsvo/
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-published case or experiment with n/dates/method stated; vendor measuring with its own product, no third-party replication — bias flagged
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Google AI Overviews named; AI crawlers
metric_kind:     visibility (citations); crawler visits
supersedes:      none
captured:        article body from 'Last updated' line to related-posts footer
verbatim:        partial — section named in captured
```

## Verbatim

> Last updated April 1, 2026
> GEO Experiments
> A recurring suggestion in GEO circles is that brands should publish Markdown (.md) versions of their web pages alongside standard HTML. The reasoning sounds plausible: LLMs process plain text more efficiently than HTML, so giving them a clean Markdown file should make your content easier to consume, and therefore more likely to be cited.
> To find out, we ran a controlled experiment on the OtterlyAI website. We published .md versions of live pages alongside their HTML counterparts, gave both formats equal discoverability through footer links, and tracked AI crawler behavior and citation outcomes over 14 days.
> Key Findings (TL;DR)
> 7.4% vs. 0% – Only HTML pages were cited: Over 14 days, HTML test pages received 7.4% of total AI bot visits. Only the HTML versions appeared as citation sources in AI-answers. No AI search platform cited a .md URL.
> Results were consistent across both test scenarios: Whether the HTML page was pre-existing or newly created, the outcome was the same. AI crawlers visited the HTML version and skipped the .md version entirely.
> No evidence that .md files offer a GEO advantage: Publishing Markdown versions of your pages did not attract AI crawlers or earn citations. AI search platforms treated .md files as if they didn’t exist.
> Why Testing Markdown (.md) Files Matters for GEO
> The idea that .md files help with AI visibility often gets bundled with related concepts like llms.txt and llms-full.txt (which we tested in a previous experiment ). The shared assumption is that reducing HTML noise, stripping out navigation, scripts, and styling, will give AI systems a “cleaner” version of your content to work with.
> It sounds logical on the surface. But it conflates two different things: how AI Search Platforms process text at inference time, and how AI search engines discover and select sources to cite.
> AI search visibility is increasingly determined by citation selection. When ChatGPT, Perplexity, or Google AI Overviews answer a query, they retrieve and cite sources, and the logic that determines which sources they pull from is built around standard web infrastructure. If AI platforms already have mature pipelines for extracting useful content from HTML, then .md files may solve a problem these systems don’t have.
> That’s the question this experiment was designed to answer with real data.
> Scope of Study
> Everything in this article is based on OtterlyAI’s own website and brand data. This is not an industry-wide study; it is a controlled experiment run on a single brand’s web presence, across a defined set of pages and a specific 14-day window. The findings were very clear after testing, however we’d encourage running your own test before drawing conclusions.
> This GEO Experiment was conducted over a continuous 14-day period using OtterlyAI’s Agent Analytics tool for AI bot traffic measurement and Search Prompt Monitoring for citation tracking across AI search platforms.
> The following test pages were used:
> Scenario A (existing content):
> One existing HTML page that was already live and indexed
> One newly created .md file containing the same content as that HTML page
> Scenario B (new content):
> One newly created HTML page
> One newly created .md file with the same content as the new HTML page
> Both HTML and .md URLs were placed in the OtterlyAI website footer and had the exact same URL structure, giving all crawlers an equal structural opportunity to discover them. Neither version was hidden, blocked, or deprioritized in any way.
> The study has 2 distinct tests:
> An AI crawler behavior test: Measured total AI bot visits to HTML test pages vs. .md test pages over 14 days, using OtterlyAI’s Agentic Analytics tool.
> A citation tracking test: Tracked whether AI search platforms cited .md URLs or HTML URLs in AI-generated answers, using OtterlyAI’s Search Prompt Monitoring.
> One interpretive note applies throughout: OtterlyAI is a SaaS brand, not an ecommerce business or developer documentation site. .md file behavior may differ in contexts where Markdown is an established content format (e.g., GitHub-hosted documentation). These findings are strongest for SaaS, content, and service-category brands.
> Methodology
> Step 1: Select Test Pages That Represent Real GEO Scenarios
> Two scenarios were chosen to cover the most common situations a brand might face when considering .md file publication:
> Scenario A: An existing, indexed HTML page paired with a newly created .md version of the same content. This tests whether adding a .md mirror to an established page attracts additional AI crawler attention.
> Scenario B: A brand-new HTML page published simultaneously with a .md version of the same content. This tests whether .md files have any advantage when both formats launch at the same time.
> These scenarios were chosen because they represent the two ways brands typically consider deploying .md files: retrofitting existing pages and launching new content in both formats.
> Step 2: Create Markdown (.md) Files with Identical Content
> Each .md file contained the same substantive content as its HTML counterpart. The Markdown versions were clean, properly formatted, and readable. The only difference between the paired pages was the file format: .md vs. HTML.
> Step 3: Place Both Formats in Equal Discovery Positions
> Both the HTML and .md URLs were linked from the OtterlyAI website footer. This gave all crawlers, including AI bots, the same structural opportunity to discover and visit both versions. No format was given preferential placement or additional internal links.
> Step 4: Monitor AI Bot Traffic and Citation Outcomes
> Over 14 days, OtterlyAI tracked two things:
> AI bot visits each URL using OtterlyAI’s Agentic Analytics tool, which records crawler activity by bot identity and URL.
> Citation appearances across AI search platforms using Search Prompt Monitoring, checking whether any AI-generated answer referenced a .md URL as a source.
> This setup isolated file format as the variable. Same content, same placement, same discovery path. The only difference was .md vs. HTML.
> GEO Experiment Results
> Test 1: Do AI Crawlers Visit .md Files?
> The AI crawler behavior test returned a decisive result.
> Results: 2.8 – 4.6% AI Crawler visits to HTML, 0% to Markdown pages
> Both HTML pages were were crawled more by AI Crawlers than the median page (1.8%)
> Noticeably a .pdf file was was crawled more (15.82%) than the average AI visits per page (4.91%)
> Top URLs visited by Agents in the last 14 days % of total AI Agent visits
> otterly.ai/ 39.69%
> https://otterly.ai/OtterlyAI_Generative_Engine_Optimization_Guide.pdf 15.82%
> otterly.ai/pricing 9.59%
> otterly.ai/features 7.74%
> otterly.ai/agencies-ai-search-monitoring 4.73%
> https://otterly.ai/enterprise-ai-search-visibility-tool 4.64%
> otterly.ai/geo-tools 3.00%
> https://otterly.ai/best-ai-search-analytics-tool-for-seo-teams 2.76%
> otterly.ai/agencies 2.60%
> otterly.ai/robots.txt 2.12%
> https://otterly.ai/ai-search-monitoring-semrush-app 1.50%
> otterly.ai/about 1.30%
> otterly.ai/marketing-teams 1.02%
> otterly.ai/privacy 0.91%
> otterly.ai/case-studies 0.73%
> otterly.ai/security 0.41%
> otterly.ai/llms.txt 0.39%
> otterly.ai/agency-partners 0.39%
> otterly.ai/example_call1.php 0.36%
> www.otterly.ai/robots.txt 0.30%
> Total 100.00%
> The HTML test pages, both the existing page and the newly created one, received a combined 7.4% of all AI bot visits across the 14-day window. The Markdown versions received 0%. The median visits per page lies at 1.8% of total traffic, placing these 2 pages well above the median.Here’s a breakdown of which AI Crawler bots visited those pages:
> Page 1: Existing HTML page
> https://otterly.ai/enterprise-ai-search-visibility-tool
> ChatGPT-User On-Demand Fetcher 97.31%
> Gemini Deep Research Fetcher 1.54%
> Claude On-Demand Fetcher 0.77%
> GoogleOther / R&D Fetcher 0.38%
> Total 100.00%
> Page 2: Newly made HTML page
> https://otterly.ai/best-ai-search-analytics-tool-for-seo-teams
> ChatGPT-User On-Demand Fetcher 96.13%
> GoogleOther / R&D Fetcher 1.29%
> Perplexity AI Crawler 0.65%
> OpenAI GPTBot (Training) 0.65%
> Claude On-Demand Fetcher 0.65%
> OpenAI Search Crawler (OAI-SearchBot) 0.65%
> Total 100.00%
> This wasn’t a case of .md pages performing worse or receiving fewer visits. They received none at all. AI crawlers did not request the .md URLs even once, despite both versions being equally discoverable from the same footer links.
> Markdown Version of HTML Page 1:
> https://otterly.ai/Best_AI_Search_Analytics_Tool_for_SEO_Teams.md
> Total URLs visited by AI Agents 0%
> Markdown Version of HTML Page 2:
> https://otterly.ai/Enterprise_AI_Search_Visibility_Tool.md
> Total URLs visited by AI Agents 0%
> The pattern held across both scenarios
> Scenario A (existing content): AI bots continued visiting the established HTML page on their regular cadence. The newly added .md mirror was never requested.
> Scenario B (new content): AI bots discovered and visited the new HTML page. The simultaneously published .md version was ignored.
> Why AI crawlers skip .md files
> Three practical factors explain this behavior:
> HTML is the web’s native format. AI search engines are built to crawl the web as it exists. Their infrastructure, from URL discovery to content extraction to rendering, is optimized for HTML documents. A .md file is an unfamiliar format in this pipeline. Crawlers have no reason to look for it.
> AI crawlers already solve the “noisy HTML” problem. The core argument for .md files assumes AI systems struggle with HTML noise: navigation bars, cookie banners, JavaScript, footer links. In reality, major AI search engines have sophisticated content extraction processes. They can isolate main content blocks from boilerplate without any help from a Markdown alternative. This is table-stakes infrastructure for any system that crawls billions of pages.
> Metadata and structure live in HTML. HTML carries signals that .md files lack: structured data (Schema.org), Open Graph tags, canonical URLs, meta descriptions, heading hierarchy in rendered DOM, and internal linking context. These signals help AI systems understand what a page is about, how it relates to other pages, and whether it’s a credible source. A plain .md file strips all of that away.
> Test 2: Did Any AI Search Platform Cite a .md URL?
> Results: Zero .md citations.
> When we checked citation data across tracked prompts, only the HTML pages appeared as sources in AI-generated answers. No AI search platform, not ChatGPT, not Google AI Overviews, not Perplexity, cited a .md URL.
> The citation result follows logically from the crawler result. If AI bots never visit a .md file, that file never enters the retrieval pipeline. Content that isn’t crawled can’t be cited.
> This is consistent with what we found in our llms.txt experiment , where only 0.1% of AI bot traffic visited the /llms.txt file over 90 days, performing 3x worse than the average content page. The broader pattern is clear: AI search platforms rely on existing web standards for discovery and citation, not on alternative file formats.
> What This Means for How You Approach .md Files in GEO
> .md Files Are Not an AI Citation Signal
> Based on our testing on the OtterlyAI website, .md files did not attract AI crawler visits or influence citation behavior in any measurable way. The gap wasn’t marginal; it was binary. Zero visits, zero citations.
> This is not a reason to stop using Markdown where it serves a real purpose. It is a reason to stop treating .md file publication as a GEO tactic.
> The Core Misconception: Inference vs. Retrieval
> The flawed logic follows a familiar pattern: “LLMs work with text. Markdown is cleaner text than HTML. So if I give AI search engines a Markdown version of my page, they’ll prefer it.”
> This breaks down because AI search engines and LLMs at inference time are two different things. When an LLM processes a document during a conversation, cleaner text can be easier to work with. But AI search engines don’t pick sources based on file format convenience. They pick sources based on relevance, authority, structure, and existing web signals, all of which are embedded in HTML.
> Publishing a .md file doesn’t make your content more authoritative or more relevant. It makes it less discoverable, because AI crawlers aren’t looking for it.
> Platform Behavior Is Consistent on This One
> Unlike our schema markup experiment , where platform behavior was fragmented (Gemini could read schema while others couldn’t), the .md file result was uniform. No AI search platform crawled or cited a .md URL. The consistency across platforms makes this one of the more definitive findings in our GEO experiment series.
> The .md File Playbook for AI Search (The Honest Version)
> 1. Don’t create .md mirrors of your pages for GEO purposes. In our test, .md files received zero AI crawler visits and zero citations. There is no evidence that publishing Markdown versions of your web pages improves AI search visibility. Your time is better spent elsewhere.
> 2. Focus on HTML page quality and structure. AI search platforms cite HTML pages. That’s where your GEO effort belongs: clear, well-structured HTML with proper heading hierarchy; structured data where appropriate (FAQ, HowTo, Article, SoftwareApplication schemas); content that is accessible without requiring client-side JavaScript rendering; and strong topical coverage with citable, evidence-backed statements.
> 3. Reserve Markdown for its actual use cases. Markdown has real value in specific contexts: developer documentation, API references, README files, and content that gets consumed by tools and integrations. If your audience includes developers building on top of your content, a well-maintained Markdown version can reduce integration friction. That’s a product decision, not a GEO tactic.
> 4. Use OtterlyAI to measure what actually gets cited. Instead of guessing which formats AI engines prefer, use Search Prompt Monitoring and citation tracking to see which of your pages are being cited, and where competitors appear instead. The Citations report turns that data into a prioritized action plan: content updates for owned pages, outreach targets for PR, and engagement targets for forums and community sources.
> 5. Connect this finding to the broader alternative-format pattern. This experiment builds on OtterlyAI’s 90-day llms.txt study , and the findings reinforce the same core lesson. In the llms.txt experiment, only 0.1% of AI bot traffic visited /llms.txt over 90 days. In this .md experiment, the gap was even wider: zero visits vs. 137 over 14 days. Both experiments point to the same conclusion: AI search platforms discover and cite content through standard web infrastructure. Alternative file formats do not meaningfully change AI crawler behavior or citation outcomes today.
> Pro Tip: Discover our GEO experimentation sheet to track live updates on the latest AI Search studies
> Closing Thoughts
> OtterlyAI’s 14-day experiment shows no evidence that publishing .md versions of web pages improves AI search visibility. Across two controlled test scenarios, .md files received zero AI bot visits while their HTML counterparts received 137. No AI search platform cited a .md URL.
> The right interpretation is straightforward. AI search crawlers are built to crawl HTML. They do not look for or prioritize .md files. Publishing Markdown mirrors of your web pages will not earn you additional citations or mentions in AI-generated answers.
> Spending time creating and maintaining Markdown mirrors of your pages is effort that could go toward improving the content, structure, and citability of your actual HTML pages. The GEO fundamentals remain unchanged: high-quality, well-structured HTML content, strong entity coverage, and earning citations across the web.
> For SEOs and GEO practitioners, the takeaway is clear: skip the .md mirrors. Put that effort into making your HTML pages more citable, more structured, and more authoritative. Then use OtterlyAI’s AI Search Monitoring to track whether AI search engines are citing them.
> Have You Tested .md Files on Your Own Site?
> The findings above are based entirely on OtterlyAI’s own website and data. .md file behavior may look different for developer documentation sites, high-authority domains, or sites operating in technical verticals where Markdown is an established content format. We’d genuinely love to hear what you’ve found.
> Have you published .md versions of your pages and tracked the impact on AI crawler behavior or citation outcomes? Did your results align with ours, or did you see something different? Share your findings with us. Real-world data from across different site types is how this field moves forward, and every experiment adds to the picture.
> Share your .md experiment results with the OtterlyAI team at rick.tousseyn@otterly.ai . We may feature your findings in a future update to this research.
> Social Share or Summarize with AI ChatGPT Google AI Perplexity Claude Gemini X (Twitter) LinkedIn
> Related Posts:
> Multi-Country AI Search Monitoring: Track Google…
> Llms.txt Experiment: What Marketers Get Wrong about llms.txt

## Pull notes — mechanical only

- Server-rendered page; tag-stripped, one line per block element; figures and embedded video not captured.
- Provenance: new — found via otterly.ai/blog/geo-gsvo/.
