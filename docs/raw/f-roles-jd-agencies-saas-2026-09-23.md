# SEO agency + SaaS in-house ATS boards - GEO/AEO job posting bodies, full text

```yaml
source:          Ashby posting-api (Victorious, Siege Media) and Greenhouse boards-api (Asana, Stripe, Mercury, Similarweb)
url_or_doc_id:   https://api.ashbyhq.com/posting-api/job-board/<victorious|siegemedia>; https://boards-api.greenhouse.io/v1/boards/<asana|stripe|mercury|similarweb>/jobs?content=true; each posting's own URL given per section below
published:       per section - source's own date field, verbatim
pull_date:       2026-09-23
pull_method:     fetch (curl, default User-Agent) - public Ashby posting-api and Greenhouse boards-api JSON endpoints, no auth, no login
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default - employer's own posting text on the employer's own ATS-hosted job board
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        full posting body for each job listed below (Ashby descriptionPlain / Greenhouse content field, HTML tags stripped); job-board listing totals given per company in pull notes
```

## Verbatim - Victorious (jobs.ashbyhq.com/victorious) - SEO agency, conventional-title comparison postings

Victorious is a US SEO agency; these two postings do not mention AEO/GEO/AI search anywhere in the body (checked full text) - captured as the pay/duty comparison baseline against the GEO-titled agency roles below (Siege Media) and vendor roles (see companion file f-roles-jd-vendors-2026-09-23.md).

### Victorious - "Senior SEO Strategist" (Remote, US only, no visa sponsorship)

- URL: https://jobs.ashbyhq.com/victorious/a836fb49-7deb-4f4e-a260-2fcf5254bbe8
- Team: SEO | Published: 2023-10-20 (listing still open as of pull date) | Pay: not printed

> The ask: Drive and refine high-impact SEO strategies for assigned accounts, acting as the primary point of contact for their SEO services at Victorious.
> The expectation: Execute SEO strategies for Victorious customers, proactively driving performance; identify and address issues related to SEO performance, technical challenges, implementation issues; drive SEO innovation, identifying opportunities for service enhancements and staying ahead of industry trends; work cross-functionally with content, web, and account management departments; provide SEO expertise and guidance when consulted by team members or cross-functional partners; stay up-to-date on the latest SEO strategies and trends.
> Qualifications: robust experience in SEO; 7+ years working for a digital marketing agency in an SEO strategy role; experience working with SEO tools (Ahrefs, SEMrush, Screaming Frog, etc.); advanced experience in Asana or related project management tools; understanding of HTML/CSS and website administration.
> Benefits: Excellent Medical/Dental/Vision/Life/LTD Insurance; 401(k)/Roth Retirement Plan & Company Match; 100% Remote Work Environment; Unlimited Paid Time Off; Company-Paid Holidays + Wellness Days; Monthly Remote Work Stipend.

### Victorious - "Content Strategist" (Remote, US only, no visa sponsorship)

- URL: https://jobs.ashbyhq.com/victorious/84e9c75c-0176-4e49-b2b8-3b12a0181971
- Team: Content | Published: 2024-12-09 | Pay: not printed

> The expectation: manage customer accounts and content production timelines using content calendars; ideate content topics that support customer objectives; work with freelance writers to plan and organize production of high-quality, SEO-optimized content, including blog posts and web copy; maintain proactive communication with customers, explaining SEO strategies and results in a non-technical manner; analyze competitors' websites and content strategies; create in-depth writers' briefs following SEO best practices; optimize existing website content for search.
> Required experience: minimum 3-5 years of work experience in a content marketing role across a variety of industry verticals; proficiency in project management programs such as Asana.
> Good-to-haves: familiarity with Ahrefs, Google Search Console, or other SEO tools; published content and/or regular contributions to industry blogs.
> Benefits: same package as Senior SEO Strategist above (medical/dental/vision/life/LTD, 401k match, 100% remote, unlimited PTO, company-paid holidays + wellness days, remote work stipend).

## Verbatim - Siege Media (jobs.ashbyhq.com/siegemedia) - remote-first "GEO agency"

Siege Media describes itself in its own postings as "a growing and remote-first GEO agency" / "organic/AI growth agency." All three roles below are on the "SEO/GEO" or adjacent team and are current listings (published 2026-09-22, the day before this pull).

### Siege Media - "SEO/GEO Team Lead" (Chicago, USA - remote)

- URL: https://jobs.ashbyhq.com/siegemedia/2a559ce9-29a2-4df3-9838-4007d6aee908
- Team: SEO/GEO | Published: 2026-09-22
- Pay: "The salary range for this position is $85,000.00-$95,000.00 DOE."

> "In this role you'll lead your clients, not a team of people. You own the client relationship and strategy from end to end, building the plan, doing the work, and presenting it, with no direct reports."
> RESPONSIBILITIES: own clients end to end (build SEO/GEO strategy, execute deliverables, lead client calls); ideate SEO/GEO roadmaps based on client KPIs, competitor analysis, site audits; suggest and implement SEO/GEO best practices across eCommerce, Fintech, SaaS; audit and optimize high-value pages across SEO, GEO, and CRO, "balancing search rankings, AI citation, and on-page conversion"; read and interpret site code for technical SEO/GEO issues; build checklists showing expected opportunity, lift, and ownership; coordinate SEO/GEO content creation via optimized briefs; run weekly performance analyses (Google Search Console, Google Analytics, Ahrefs, Peec AI, and other tools), compile client reports in Data Studio.
> REQUIRED SKILLS: 3-5 years of experience in an SEO/GEO role; experience analyzing websites with Ahrefs, Screaming Frog, GA4, GSC, and Peec AI or similar AI tracking tools; "experience tracking and reporting AI search visibility (share of voice, citation and reference rate, and AI-referral traffic) and translating it into clear, actionable recommendations for clients"; deep experience with eCommerce, Fintech, SaaS clients; comfort using LLMs to speed up SEO/GEO workflows; "a deep understanding of on-page, content, technical, and off-page GEO strategies that support client performance in AI search"; working knowledge of HTML/CSS/JavaScript.
> SUGGESTED SKILLS: experience with a CMS like WordPress, Shopify, Webflow (headless a plus); 2-3 years agency experience; "experience with product feed optimization and agentic commerce is a major bonus."
> Hiring process includes a JSON-LD Schema Person Markup writing exercise ("What would the Schema Person Markup for Michael Scott from The Office look like?") and a paid 3-hour timed project later in the process ($150 for your time).

### Siege Media - "Senior SEO/GEO Analyst" (Chicago, USA - remote)

- URL: https://jobs.ashbyhq.com/siegemedia/9809831c-d354-4fe6-9d47-2bcf6a42665d
- Team: SEO/GEO | Published: 2026-09-22
- Pay: "The salary range for this position is $75,000 to $85,000 DOE."

> "This is a senior execution role and a step up on our GEO/SEO career path. You'll take on our more complex and independent SEO and GEO work... while Team Leads still own the overall client relationship and strategy. There are no direct reports... this can also be a natural path toward a Team Lead role."
> RESPONSIBILITIES: independently execute advanced/higher-stakes SEO and GEO work with minimal direction; lead complex analysis (technical audits, diagnostics, competitive and AI-answer research); deliver polished, QA'd work; conduct keyword and prompt research plus competitor analysis; implement/troubleshoot structured data and content optimizations that improve visibility in traditional search and AI-generated answers; build/interpret reports in GA4, GSC, Ahrefs, and Peec AI; "track and analyze AI search visibility (citations, share of voice, and AI-referral traffic) and recommend actions to improve it"; mentor Analysts.
> REQUIRED SKILLS: 3-5 years of hands-on SEO experience, including meaningful GEO or AI search work; deep command of on-page and technical SEO; strong experience with Ahrefs, Screaming Frog, GA4, GSC, Peec AI or similar AI tracking tools; "a strong understanding of how AI search engines surface, rank, and cite content, and how to influence it."
> Hiring process includes the same Schema Person Markup exercise as the Team Lead posting, plus "a brief GEO/SEO skills test after your second interview."

### Siege Media - "Content Marketing Specialist" (Chicago, USA - remote) - conventional-title comparison, same agency

- URL: https://jobs.ashbyhq.com/siegemedia/dd5355e4-a3ac-47c1-ba5d-bc17a2d8ce24
- Team: Content Marketing | Published: 2026-09-22
- Pay: "The salary range for this position is $52,000.00-$64,000.00 DOE. This position is 100% remote and based in the United States."

> Responsibilities: conduct keyword research to identify content opportunities; write comprehensive articles with minimal supervision; adapt tone/complexity to audience and style guides; implement feedback from editors/clients/teammates; "hit client SEO traffic goals month over month by creating content that ranks and/or generates passive links"; "apply GEO best practices to make client content more discoverable by LLMs"; "leverage AI tools to drive productivity across the content workflow while upholding Siege's editorial quality standards"; help pilot and evaluate new AI tools and workflows for the team.
> Required skills: 2+ years as a content marketer; working knowledge of SEO/GEO tools; working familiarity with leading LLMs and AI writing tools; demonstrated adoption of AI tools to increase productivity.
> [note: this is Siege Media's conventional/junior content role, posted the same day as the two SEO/GEO roles above, on the same ATS board - pay is roughly 40-60% of the SEO/GEO Analyst and Team Lead bands at the same company]

## Verbatim - Asana (Greenhouse, job-boards.greenhouse.io/asana)

### Asana - "Head of Global SEO/AEO" (job title field: "Head of SEO & AEO"; San Francisco or Vancouver, hybrid)

- URL: https://www.asana.com/jobs/apply/8100442?gh_jid=8100442 (San Francisco posting; an identical req, job id 8163596, is also listed for Vancouver, BC)
- Updated: 2026-09-15 | Office-centric hybrid, in-office Mon/Tue/Thu
- Pay: "For this role, the estimated base salary range is between $218,000 -$256,000. The actual base salary will vary based on various factors, including market and individual qualifications objectively assessed during the interview process."

> "We're looking for a data-driven Head of Global SEO/AEO to own our worldwide organic growth strategy and execution. In this role, you will scale SEO and Answer Engine Optimization (AEO) into high-performing acquisition channels, driving results against business-critical metrics like trial starts, MQLs, and pipeline. You will manage an in-house team alongside external agencies and contractors, pioneering our approach to AI-mediated discovery to win in the new AI-search era."
> What you'll achieve: set the global organic strategy and roadmap, owning SEO/AEO as growth channels feeding PLG & SLG GTM motions, directly accountable for trial-start (PLG) and MQL/pipeline (SLG) targets; build the business case for investment, owning channel forecast/budget/reporting to executive leadership; "own and evolve our end-to-end AEO strategy by bringing proven frameworks, building measurement for brand visibility and citation in AI answer engines, and setting the standard for AI-mediated discovery"; direct SEO content roadmap and "agent-led content strategies"; partner with Marketing Ops and Analytics on attribution tying organic activity to PLG/SLG conversion; lead technical SEO strategy (site architecture, structured data, Core Web Vitals, international/multi-region SEO); build/hire/lead a high-performing SEO/AEO team, "making critical resource decisions around agency partners and agent vs. human deployment"; serve as executive-facing SME on SEO/AEO.
> About you: 10+ years in SEO with senior team leadership experience in B2B SaaS, proven track record scaling organic into a major revenue-generating channel across global regions; demonstrated experience owning organic across both PLG and SLG motions; "hands-on experience building an AEO strategy, running experiments, establishing measurement, and driving results in AI answer engines"; deep technical SEO fluency (site architecture, structured data/schema, Core Web Vitals, international SEO); rigorous data-driven operating style, SQL skills; proven team leadership hiring/coaching/developing talent across regions; executive presence to influence Product, Engineering, and Marketing leadership.

## Verbatim - Stripe (Greenhouse, stripe.com/jobs)

### Stripe - "AEO and GEO Marketing Manager" (Remote in the US)

- URL: https://stripe.com/jobs/search?gh_jid=7844214
- Updated: 2026-09-10 | Team: Growth Marketing | Pay: not printed in posting body

> About the team: "Growth Marketing is a team of performance-driven marketers and channel specialists... In this role, you'd be joining a global, cross-functional team dedicated to testing and scaling cutting-edge acquisition channels. Our team helps Stripe increase the GDP of the internet by ensuring our web presence is perfectly optimized for the next generation of artificial intelligence and search technologies."
> What you'll do: "Stripe is seeking an AEO and GEO Marketing Manager to lead the channel. This individual will play a critical role in growing new user acquisition from platforms including ChatGPT, Perplexity, and Google AI Overviews. The scope of the role includes Generative Engine Optimization (GEO), also known as Answer Engine Optimization (AEO) or Large Language Model (LLM) Search Optimization, improving AI agent experience, and integrating AI capabilities to improve the performance and efficiency of search and answer engine channels."
> Responsibilities: lead growth and user-acquisition strategy for the AEO channel; "optimize Stripe.com so artificial intelligence agents can efficiently access and take action on behalf of users"; spearhead development/integration of AI capabilities to improve search and answer engine channels; deliver regular reports on channel performance; partner with content, engineering, and data analytics on a testing roadmap.
> Minimum requirements: 5+ years of experience creating/executing SEO strategies, with direct experience in AEO and GEO; proven technical experience making websites SEO and AEO-friendly; experience with Tableau, Looker, Adobe Analytics, or Google Analytics; experience applying user-intent analysis. Preferred: experience/familiarity with NLP, vector search, and Retrieval-Augmented Generation (RAG); B2B SaaS in-house search experience; SQL.

### Stripe - "Head of AEO & SEO" (US Remote; Chicago, Atlanta, Canada)

- URL: https://stripe.com/jobs/search?gh_jid=8128634
- Updated: 2026-09-10 | Team: Growth Marketing | Pay: not printed in posting body

> About the team: "The SEO & AEO function specifically drives organic discovery ensuring Stripe is found, cited, and recommended when developers, founders, and finance leaders are searching for or asking about payments, financial infrastructure, and related topics."
> What you'll do: "This role owns one of the most strategically important and evolving acquisition channels at Stripe. Organic search is already one of our largest and most efficient growth channels and the emergence of AI-powered answer engines represents a once-in-a-generation shift in how businesses discover software... This is a rare opportunity to define what AEO means for a company like Stripe and to build the playbook that others will follow."
> Responsibilities: own organic growth strategy end-to-end across SEO and AEO, "including technical optimizations, content strategy, on-site experience, and visibility in general purpose assistants (ChatGPT, Google AI Overviews, Gemini, Perplexity, etc.) and coding assistants (e.g. Claude, Codex, etc.)"; lead/develop/retain a high-performing team of SEO and AEO specialists; drive measurable improvements in organic visibility, rankings, citations, traffic, signups, sales inbound, downstream activations; drive improvements in "how well AI tools are able to understand how Stripe's products work and how to properly integrate them"; build/evolve measurement framework (attribution models, leading/lagging indicators, revenue impact); own strategic AEO roadmap; represent organic growth performance across Stripe to execs.
> Minimum requirements: 10+ years of SEO experience, at least 3 years leading a team, 2+ years at senior/leadership level engaging executives; demonstrated expertise in technical SEO and content strategy at scale; "deep understanding of how AI-powered search and answer engines work (LLM-based retrieval, citation behavior, entity recognition)"; proven ability to communicate complex technical concepts to executives; track record building/developing/retaining high-performing teams. Preferred: developer-focused/technical B2B product experience; international SEO background; programmatic/product-led SEO at scale; "demonstrated early-mover advantage in AEO - evidence of monitoring, optimizing for, or measuring visibility in AI-generated answers."

## Verbatim - Mercury (Greenhouse, job-boards.greenhouse.io/mercury)

### Mercury - "Organic Search Marketer - SEO/AEO" (SF, NYC, Portland OR, or Remote US/Canada)

- URL: https://job-boards.greenhouse.io/mercury/jobs/6114209004
- Updated: 2026-09-01
- Pay: "US employees in New York City, Los Angeles, Seattle, or the San Francisco Bay Area: $158,200-$197,800 USD. US employees outside of those metros: $142,400-$178,000 USD. Canadian employees (any location): $149,500-$186,900 CAD."

> "For decades, online search followed a simple exchange: customers typed keywords, engines returned links, and brands competed for clicks. AI search has changed that... Mercury's Organic Search team is hiring an Organic Search Marketer (SEO/AEO) to help define how Mercury shows up across search engines, answer engines, and AI-native discovery."
> In this role: "identify high-impact opportunities, develop SEO and AEO strategies that drive traffic and AI visibility for Mercury products (like Mercury's Business Credit Cards), experiment with new workflows and formats... We're looking for someone with strong commercial instincts, deep SEO/AEO fluency, an AI-native mindset."
> In this role you will: define and own high-impact SEO and AI Search strategies across priority products, using performance data, competitor deep dives, and audience insights; partner cross-functionally with Social, Product, Product Marketing, Engineering, Community to turn SEO/AEO opportunities into shipped work; own the technical SEO/AEO roadmap for Mercury.com with Engineering (page speed, rendering, site architecture); build repeatable systems, AI workflows, and guidelines; drive SEO-driven evergreen content optimizations; "identify and scope high-value tools, templates, calculators, downloadable PDFs... that make Mercury content more useful, shareable, linkable, and cite-worthy"; "relentlessly test new plays for improving traditional and AI search traffic and visibility - from new page types to edge caching for bots."
> You have: 5+ years of SEO experience, with 2-3 years focused on AEO, ideally in a fast-moving startup environment; deep technical fluency paired with "a clear grasp of how LLMs interpret and weight content differently from traditional search engines"; hands-on experience with AI agents and automation tools; demonstrated ability to influence senior and cross-functional stakeholders. Application requires a cover letter ("Applications without a cover letter will not be considered").

## Verbatim - Similarweb (Greenhouse, job-boards.greenhouse.io/similarweb)

### Similarweb - "Strategist - SEO & AEO" (job-board title; page body title "Solution Business Manager, Search & Ads Intelligence"; Burlington, MA, hybrid)

- URL: https://job-boards.greenhouse.io/similarweb/jobs/8082486
- Updated: 2026-07-23
- Pay: "The base salary range for this position in the Burlington, Massachusetts area is $130,000 to $170,000, plus benefits, including: medical, dental, and vision insurance, 401K plan, potential equity, employee stock purchase plan, and paid sick and parental leave. The base salary range above is for the Burlington, Massachusetts area, and could vary for candidates in other locations."

> "Search is changing fast. AI-powered answers, generative results, and new ad formats are reshaping how people find information and how brands compete for attention. Similarweb sits at the center of that shift, giving marketers the intelligence they need to stay ahead." "This is not a generalist role. We want someone who has lived inside a performance marketing agency or large retailers or eCommerce with hands-on experience managing campaigns across organic and paid channels."
> Why This Role, Why Now: "Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) are creating entirely new strategies for organic and paid visibility that most clients are still figuring out."
> What You'll Do - Client & Revenue Impact: partner with sales/account management on deal cycles, RFPs, renewals; run discovery sessions on clients' channel mix across "SEO, AEO/GEO, Paid Search, Paid Social, Display, and Affiliate"; build tailored use-case demos.
> Search, AEO & GEO Strategy: "Guide clients on organic search strategy, including AEO and GEO, helping them understand how AI-generated results, featured snippets, and answer boxes are affecting their visibility"; "Help clients optimize for new search paradigms: LLM-referenced content, structured data, entity optimization, and topic-aligned content strategies"; monitor SERP landscape evolution and AI-overview-driven CTR shifts.
> Must-Haves: 6+ years hands-on performance marketing experience with deep expertise in both SEO and paid media, ideally at a performance marketing agency; practical experience across at least 3 of: Organic Search (SEO), Paid Search (PPC/SEM), Paid Social, Programmatic Display, Affiliate; "solid understanding of AEO and GEO: what it means to optimize for AI-generated answers, how LLMs surface content, and what marketers need to do differently now"; comfortable building with AI tools.
> "Please note: We're unable to sponsor employment visas at this time."

## Pull notes - mechanical only

- Search method: fetched full job listings (with content=true / descriptionPlain) from each company's Greenhouse or Ashby board, then grepped titles in Python for the regex /\bseo\b|\bgeo\b|\baeo\b|generative engine|answer engine|ai search|ai visibility|llm seo|ai discovery|ai-powered search|search optimization/i before reading matched bodies in full.
- Greenhouse boards probed and scanned in this pull (company: total listings on board / GEO-AEO-SEO title hits): webflow 27/0, klaviyo 144/0, squarespace 34/0, intercom 116/0, asana 103/2 (both captured, SF + Vancouver duplicate), airtable 4/0, mozilla 85/0, figma 159/0, stripe 691/2 (both captured), chime 67/0, hootsuite 10/0, sproutsocial 27/0, similarweb 66/1 (captured), mercury 63/1 (captured). Boards checked with 0 title hits (coinbase, robinhood, instacart, tripadvisor, glossier, brex, gusto, discord, reddit, pinterest, lyft, duolingo, dropbox, anthropic, salesloft, yext) were not read further - title-only scan, bodies not opened.
- 404 (no board under that slug) on Greenhouse: hubspot (302/blocked - returned 200 with 30-byte empty body, likely moved ATS), zapier, notion, canva, monday, wix, shopify, clickup, miro, mailchimp, rippling, ramp, servicenow, gong, buffer, doordash, wayfair, etsy, zillow, chewy, yelp, expedia, allbirds, warbyparker, remitly, deel, expensify, plaid, squareup, canva-1, box, evernote, byte-dance, bytedance, perplexity, perplexityai, openai, scale-ai, together-ai, elevenlabs, runwayml, mistral, cohere, jasper-ai, jasper, copy-ai, copyai, clay, clayhq, apollo-io, outreach, chorus, gong-io, wix-com, bigcommerce, woocommerce, automattic, wordpress-com. Agency slugs tried and not found on Ashby: directiveconsulting, directive-consulting, ignitevisibility, ignite-visibility, portent, bounteous, riseinteractive, rise-interactive, searchdiscovery, search-discovery, whitehatseo, powerdigital, power-digital, thriveagency, thrive-agency, tinuiti, seerdata, sevenatoms, overdrivemarketing, gofishdigital, go-fish-digital, ipullrank, foundationinc, foundation-inc, npdigital, np-digital, seerinteractive, seer-interactive, victoriousseo (only "victorious" without suffix resolved), siege-media (only "siegemedia" no hyphen resolved), growth-machine, growthmachine, amsive, rankiq, marketmuse, market-muse.
- Live boards reached but returning 200 with no relevant title hit (agency-adjacent 200s not otherwise captured): none of the additional agency slugs above resolved live; only victorious and siegemedia resolved among the ~35 agency-name guesses tried.
- Adobe, coinbase, robinhood, instacart, tripadvisor, glossier, brex, mercury (see above), gusto, discord, reddit, pinterest, lyft, duolingo, dropbox, anthropic, salesloft, yext all returned HTTP 200 live Greenhouse boards; each was title-scanned only (see hit counts above), not manually browsed further given time budget.
- No login, CAPTCHA, or paywall encountered on any Greenhouse boards-api or Ashby posting-api endpoint; all responses HTTP 200 (except explicit 404s on non-existent slugs), JSON, unauthenticated. The Chrome browser extension held for this run was not needed for any pull in this file.
