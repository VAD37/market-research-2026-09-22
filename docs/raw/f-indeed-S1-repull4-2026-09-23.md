# Indeed — S1 posting bodies, re-pull 4: remaining 28 of 35 cards, employer career sites by curl only

```yaml
source:          employer career sites and ATS JSON/HTML endpoints — Workday CXS, Greenhouse boards-api, Lever api, Ashby posting-api (checked, no hit this pull), Workable widget API, Paylocity, CareerPlug, JobScore, Recruitee, JobTarget, plus DuckDuckGo html.duckduckgo.com/html/ used only to locate each employer's own career-site URL (no aggregator content quoted)
url_or_doc_id:   per employer, listed in each section below; Indeed itself (indeed.com) was not touched this pull per brief (Cloudflare-walled per repull2/repull3, R-BLOCKED-2, P16-c4b)
published:       per section — datePosted / postedOn / published_at as the employer's own ATS states it
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "Mozilla/5.0 ... market-research"); no browser, no extension, no Indeed
pull_purpose:    evidence about a number
tier:            3
tier_reason:     demand-signals.md S1 default ("3, employer's own posting"); every body below is the employer's own ATS text
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          per section — engines named in each body listed under its "Phrase check" line
metric_kind:     none
supersedes:      none — continues docs/raw/f-indeed-S1-repull2-2026-09-23.md (35 cards, card-fields only) and docs/raw/f-indeed-S1-repull3-2026-09-23.md (6 of 35 bodies read); this file covers the remaining 28 unread cards from that 35-card set (card #0 was already read directly on Indeed in repull2 and is not repeated)
captured:        full posting body for 13 of 28 cards (11 with GEO/AEO/AI-search duty language, 2 read with none); employer-board search results and non-hits for the other 15
verbatim:        posting bodies verbatim as the ATS returned them, HTML tags stripped by the pull script, list items one per line; boilerplate (EEO/benefits legalese) kept in full except where noted "[note: ... removed]"
```

## Access log — verbatim page states, mechanical only

No Indeed request made this pull. For each employer: (1) DuckDuckGo html.duckduckgo.com/html/ query to find the employer's own career-site domain; (2) curl to that domain or its ATS API/endpoint; (3) if a job list came back, matched by the Indeed card's exact title, employer, and location from `f-indeed-S1-repull2-2026-09-23.md`. Full command/response log kept in the pull script's scratch output, not reproduced here; salient HTTP codes are given per employer below.

## Cards read in full — GEO/AEO/AI-search duty language present

### Card #5 — Fresenius Kabi, "Director, Ecommerce"

- Employer URL: https://freseniusglobal.wd3.myworkdayjobs.com/wday/cxs/freseniusglobal/FK_Careers/job/Lake-Zurich-IL/Director--Marketing-Clinical-Nutrition--E-Commerce-_R-10210218
- Indeed card: jobkey 5ed892e192423d0d, "30+ days ago" as of 2026-09-23, "$180,000 - $210,000 a year", Lake Zurich, IL 60047
- Workday jobPostingInfo: `startDate: "2026-07-16"`, `postedOn: "Posted 30+ Days Ago"`, `jobReqId: "R-10210218"`, title on the ATS "Director, Marketing, Clinical Nutrition & E-Commerce" (Indeed's card title truncated to "Director, Ecommerce")
- Phrase check (body, case-sensitive substring counts): "GEO" 2; "AEO" 2; "Generative Engine Optimization" 1; "Answer Engine Optimization" 1; engines named: "ChatGPT, Perplexity, Google AI Overviews, etc."
- Salary in body: "$180,000-210,000", bonus target 16% of base
- Employer size text in body: none stated (global Fresenius Kabi/Fresenius SE context implied, not quantified in this posting)

> Job SummaryThe Director, Ecommerce is a pivotal role in the company and is responsible for developing, scaling, and leading the digital commercial strategy for the portfolio. This role owns the performance, revenue growth, and operational excellence across digital sales channels, including direct to consumer (DTC), Amazon and other marketplaces, and B2B online purchasing platforms.This leader serves as the architect of our digital commerce capability in the U.S., driving seamless online customer experiences, executing performance marketing and SEO strategies, and building the technology and analytics foundation needed for sustained growth. The Director partners closely with IT, Supply Chain, Quality, Regulatory, Medical Affairs, Legal, Finance, and Brand Marketing to ensure compliant, high performing systems and customer pathways within a regulated healthcare environment. The position requires an entrepreneurial mindset, strong cross functional leadership, and a proven track record of scaling ecommerce businesses.
> Salary Range: $180,000-210,000. Position is eligible to participate in an annual bonus plan with a target of 16% of the base salary. Position is eligible to participate in our medium-term incentive plan.
> Responsibilities
> E-Commerce Strategy & Leadership
> - Own the P&L and growth roadmap for all digital commerce channels (DTC, marketplace, B2B online).
> - Build the business case, onboarding plan, and operational model for each new channel, including content syndication, pricing architecture, fulfillment approach, and performance measurement.
> - GEO & AEO: Build and lead Generative Engine Optimization and Answer Engine Optimization strategies to ensure the brand and portfolio are surfaced, cited, and recommended within AI-powered search experiences (ChatGPT, Perplexity, Google AI Overviews, etc.).
> - Partner with Supply Chain & Customer Service to optimize online fulfillment, inventory availability, delivery SLAs, and return processes.
> Requirements include: Strong command of SEO, plus working knowledge of emerging GEO and AEO practices for AI-powered search environments.
> The Company's primary business language is English... Additional Information: We offer an excellent salary and benefits package including medical, dental and vision coverage, as well as life insurance, disability, 401K with company contribution, and wellness program. Fresenius Kabi is an Equal Opportunity/Affirmative Action employer.

### Card #9 — Rational 360, "Associate, Insights & Intelligence"

- Employer URL: https://apply.workable.com/rational/j/7AECD74B8B/ (found via https://apply.workable.com/rational/j/E55A4587FD/, a 302 redirect to the same account's widget)
- Indeed card: jobkey 31b38374c6520b12, "30+ days ago" as of 2026-09-23, "$60,000 - $65,500 a year", Washington, DC 20036
- Workable fields: `published_on: "2026-08-05"`, `department: "Digital"`, `city: "Washington"`, `state: "District of Columbia"`, `country: "United States"`
- Phrase check: "generative engine optimization (GEO)" 2; "AI simulations" 1; "SEO" 2; no engine named by brand
- Salary in body: "60,000 to 65,500 USD annually" — matches card exactly
- Employer size text in body: "a staff of approximately 120 and growing" — maps to Mid-market band (100–999 headcount)

> About This RoleRational 360 is hiring an Associate, Insights & Intelligence to support and grow the firm's integrated research and analytics offerings... About Rational 360: Rational 360 is a full-service strategic communications and digital company that helps organizations win in high-stakes public affairs, corporate communications, and reputation management... With a staff of approximately 120 and growing, Rational 360 is partially employee-owned...
> AI and Emerging Methodologies
> - Develop working familiarity with AI-enhanced research approaches, including AI simulations and generative engine optimization (GEO), supporting senior team members in executing and iterating on these methodologies.
> - Stay current on new research tools, AI applications, and emerging technologies; bring awareness of relevant developments back to the team.
> - Participate in experimentation with new methodologies, contributing to the team's culture of curiosity and rigor.
> Requirements: ... Demonstrated hands-on experience in at least one of the following: Social listening or media monitoring platforms ...; Primary research methods ...; SEO or generative engine optimization (GEO). ... Genuine curiosity about AI and a willingness to experiment with and apply AI tools in a professional context.
> Salary range for this role is 60,000 to 65,500 USD annually. This role is not eligible for visa sponsorship.

### Card #10 — Safe Life US LLC, "SEO Specialist"

- Employer URL: https://recruiting.paylocity.com/recruiting/jobs/Details/4108444/Safe-Life-US-LLC/SEO-Specialist
- Indeed card: jobkey 43f8fcc9c7d922ab, "30+ days ago" as of 2026-09-23, no salary shown on card, Nashville, TN
- Paylocity JSON-LD: `"datePosted":"2026-04-22T17:12:50-05:00"`, hiringOrganization "Safe Life US LLC"
- Phrase check: "Generative Engine" 1; "GEO" 2; "LLM" 2
- Salary in body: none stated — matches the card's blank salary field
- Employer size text in body: none quantified ("one of the fastest-growing providers of AEDs", "growing team")

> Safe Life is one of the fastest-growing providers of AEDs and life-saving readiness programs, united by a clear mission: helping communities Prevent Heartbreak. We deliver more than products - we provide end-to-end programs that combine equipment, training, and compliance support to keep organizations rescue-ready.We are seeking a results oriented, detailed and reliable SEO Specialist to join our growing team!... The SEO Specialist is responsible for driving and improving our search visibility. This role partners closely with content and paid media teams to identify technical issues, optimize content, enhance site crawlability, and stay ahead of evolving SEO trends, including LLM (Large Language Model) and Generative Engine Optimization (GEO).
> Position Highlights
> - Run technical SEO audits and implement high-impact fixes.
> - Lead backlink outreach and build authoritative links.
> - Optimize content for organic search, local SEO, and visibility in LLM-driven search results.
> Requirements: ... Proficiency with HTML, CSS, Schema markup, and Shopify SEO best practices; Solid understanding of e-commerce SEO; A sharp mix of strategic thinking and executional follow-through; Understanding of LLMs and GEO search; Bonus: Experience with local SEO, international SEO, or medical device SEO; Extra bonus: Familiarity with AEDs or emergency medical markets.
> Toolkit: SEMrush [truncated by pull script after tool list]

### Card #11 — Giftogram, "Content Editor & AEO Strategist"

- Employer URL: https://job-boards.greenhouse.io/giftogram/jobs/4398247009
- Indeed card: jobkey cf461bb5797236e7, "14 days ago" as of 2026-09-23, no salary shown on card, Whippany, NJ 07981 (Indeed's card title was truncated by the extraction step to "Content Editor   AEO Strategist")
- Greenhouse fields: `updated_at: "2026-09-08T14:57:52-04:00"`, `location.name: "200 Jefferson Park, Whippany NJ 07981"`
- Phrase check: "AEO" (as a standalone term or inside "Answer Engine Optimization") 4; "Answer Engine Optimization" 1; "ChatGPT" 1; "Perplexity" 1; "Gemini" 1; "Google AI Overviews" 1; "generative engine optimization" 1
- Salary in body: "Competitive base salary based on experience" — no figure
- Employer size text in body: none quantified; self-description "leading B2B digital gift card and rewards platform"

> About Giftogram: Giftogram is the leading B2B digital gift card and rewards platform, helping companies send meaningful incentives, recognition, and rewards at scale. We work with enterprise clients across industries and integrate with the tools their teams already use — HubSpot, Salesforce, Slack, Workday, and more. We're a fast-moving team that operates with intention, and we're looking for someone to help us harness AI to do our best work.
> About the Role: Giftogram is looking for a Content Editor & AEO Strategist to own how our content performs where buyers now start their research: AI assistants like ChatGPT, Perplexity, Gemini, and Google AI Overviews, alongside traditional search. This position reports to the Head of Revenue and partners with sales, marketing, and customer success to decide what we publish, hold it to a high editorial and factual standard, and prove it drives pipeline.
> This is not a writing role. ... Deciding what deserves to be written, making sure it is true, making it sound like Giftogram, and showing that it earned citations and leads is the hard part.
> What You'll Do: Map the questions our buyers ask AI assistants across our core use cases (employee rewards and recognition, customer loyalty and incentives, disbursements and settlements, promotions and giveaways, surveys) and decide which ones Giftogram should be the cited source for; Edit every page before it ships...; Own the editorial standard, style guide, and QA checklist...; Verify product, redemption, pricing, and compliance claims...; Manage site architecture for citation: hub-and-spoke structure, internal linking, schema and structured data recommendations, and refresh cadence for pages losing ground; Track share of AI citations by topic, AI referral traffic, engagement, and assisted pipeline in HubSpot and our AEO tooling; report monthly on what worked, what did not, and what changes as a result.
> What We're Looking For: 5+ years in content, editorial, or SEO roles, with at least 2 years accountable for outcomes rather than output; Hands-on experience with answer engine or generative engine optimization; ... Fluency with HubSpot or a comparable CMS and marketing platform, GA4 or similar analytics, and at least one SEO or AEO measurement tool.
> Bonus Points: B2B SaaS or fintech experience selling to HR, marketing, or finance buyers; Background in payments, rewards, incentives, or gift card products; Familiarity with schema.org markup, structured data, and technical SEO fundamentals; Experience reviewing compliance-sensitive content (SOC 2, PCI DSS, GDPR language); Experience building or scaling a content operation, including the tooling and process behind it.
> What We Offer: Competitive base salary based on experience; Ownership of a function that directly shapes how buyers find Giftogram; Direct access to leadership and influence over where the content program goes next.

[note: Giftogram's own self-description is "leading B2B digital gift card and rewards platform" — it does not use the word "SaaS" of itself anywhere in this posting; "B2B SaaS" appears once, in "Bonus Points", describing a candidate's prior employer background, not Giftogram]

### Card #12 — Playboy Enterprises, Inc., "Deputy Editor"

- Employer URL: https://www.jobtarget.com/jobs/jt-4n39t1d537/deputy-editor-miami-beach-florida (Playboy's own applicant-tracking widget, job-id 41199622, site-id 38027)
- Indeed card: jobkey 9fc681c34ad1afb0, "30+ days ago" as of 2026-09-23, "$140,000 - $160,000 a year", Miami Beach, FL 33139
- ATS fields: `Posted on July 30, 2026`, salary shown as "$140000 - $160000"
- Phrase check: "GEO" 3 ("GEO (Generative Engine Optimization)" once, "SEO/GEO" once, plus a bare "GEO"); "Generative Engine Optimization" 1; "AI-assisted" 2; no third-party AI engine named
- Salary in body: "$140000 - $160000" — matches card exactly
- Employer size text in body: none stated (context: "consumer lifestyle business... available in 180 countries")

> Position Summary: The Deputy Editor is the senior editorial leader of Playboy's daily content operation... Reporting to the Chief Brand Officer & Editor-in-Chief, this role is responsible for the daily editorial output of Playboy.com, the quarterly print magazine, and Playboy's most iconic editorial franchises...
> Core Responsibilities — Digital Editorial & Content Strategy: Own and manage the editorial calendar for Playboy.com...; Apply SEO, GEO (Generative Engine Optimization), and AI-assisted publishing tools to maximize content discoverability and search performance across traditional and AI-driven search surfaces.
> Key Performance Indicators: ... Search Performance: Improvements in organic search rankings and SEO/GEO visibility. ...
> What You'll Bring: ... Deep expertise in content strategy, SEO, and digital publishing best practices — including working knowledge of Generative Engine Optimization (GEO) and AI-assisted editorial tools. ...
> What We'll Be Part Of: Playboy is one of the most recognizable, iconic brands in the world... Today, Playboy is a consumer lifestyle business with digital and physical products available in 180 countries across entertainment, events, fashion, lifestyle, sexual wellness, consumer products and more.

### Card #18 — Solventum, "Search Engine Optimization Specialist"

- Employer URL: https://healthcare.wd1.myworkdayjobs.com/wday/cxs/healthcare/Search/job/Remote---Minnesota/Subject-Expert-Optimization-Specialist_R01131160-1 (Workday tenant "healthcare", site "Search" — not the guessed "solventum" tenant, which returned HTTP 500 on every wd1/wd3/wd5 guess)
- Indeed card: jobkey 30a76aa9f9555acc, "30+ days ago" as of 2026-09-23, "$107,600 - $147,950 a year", Minnesota
- Workday jobPostingInfo: `postedOn: "Posted 23 Days Ago"`, `startDate: "2026-08-31"`, `jobReqId: "R01131160"`, location "Remote - Minnesota", remoteType "Remote"
- Phrase check: "Generative Engine Optimization (GEO)" 1; "answer engines" 2; no third-party AI engine named
- Salary in body: "$107,600 - $147,950" — matches card exactly; "includes base pay plus variable incentive pay, if eligible"
- Employer size text in body: none stated; "Solventum is a new healthcare company" (2024 spin-off of 3M Health Care), regulated-industry language throughout ("Healthcare technology, B2B, or other regulated industry experience")

> Job Description: Search Engine Optimization (Solventum) — 3M Health Care is now Solventum. At Solventum, we enable better, smarter, safer healthcare to improve lives...
> The Impact You'll Make in this Role: As an Search Engine Optimization (SEO) Specialist, you will have the opportunity to tap into your curiosity and collaborate with some of the most innovative and diverse people around the world. Here, you will make an impact by:
> - Developing and executing strategies that improve organic visibility, drive qualified traffic, and support business growth across the Health Information Systems business globally.
> - Identifying and applying Generative Engine Optimization (GEO) best practices to improve discoverability in AI-powered search, answer engines, and conversational discovery experiences.
> - Conducting keyword, content, and competitive research to uncover opportunities, inform optimization priorities, and strengthen digital performance across priority solution areas.
> - Partnering with integrated marketing, product marketing, marketing communications, and web stakeholders to translate search insights into actionable recommendations, content enhancements, and measurable business outcomes.
> - Leading the digital asset upload and metadata management process within our Digital Asset Management (DAM) system...
> Your Skills and Expertise: ... Bachelor's degree ... AND Seven (7) years of hands-on experience in SEO, digital marketing, website optimization, content strategy... Additional qualifications: (3) three years of experience with core SEO disciplines...; Experience with GEO or optimizing content for AI-driven search, answer engines, and emerging discovery experiences; Experience with platforms and tools such as Adobe Experience Manager (AEM), DAM platforms, Adobe Analytics, Google Search Console, SEMrush, Answer the Public, or Screaming Frog; ... Healthcare technology, B2B, or other regulated industry experience.
> Applicable to US Applicants Only: The expected compensation range for this position is $107,600 - $147,950, which includes base pay plus variable incentive pay, if eligible.

### Card #19 — Ann & Robert H. Lurie Children's Hospital of Chicago, "Sr. Digital Marketing Specialist – Paid Media, Performance & AI Search"

- Employer URL: https://luriechildrens.wd1.myworkdayjobs.com/wday/cxs/luriechildrens/externalportal/job/Streeterville-Chicago-IL/Sr-Digital-Marketing-Specialist---Paid-Media--Performance---AI-Search_JR2026-2405-1
- Indeed card: jobkey 2ac7d8da6b4601c5, "25 days ago" as of 2026-09-23 (Workday says "Posted 23 Days Ago" — small clock drift between the two captures), "$70,720.00 - $115,627.20 a year", Streeterville, IL
- Workday jobPostingInfo: `postedOn: "Posted 23 Days Ago"`, `startDate: "2026-08-31"`, `jobReqId: "JR2026-2405"`
- Phrase check: "generative engine optimization (GEO)" 2; "ChatGPT" 1; "Perplexity" 1; "Google's AI Overviews" 1
- Salary in body: "$70,720.00-$115,627.20 Salary" — matches card exactly
- Employer size text in body: "the largest pediatric provider in the region", "140-year legacy"; headcount not quantified

> General Summary: The Sr. Digital Marketing Specialist – Paid Media, Performance & AI Search is responsible for supporting and optimizing the Medical Center's digital advertising efforts across paid search, paid social, and other digital channels, while also monitoring and adapting to the rapidly evolving AI search landscape. ... This role requires a digital marketing professional who stays current with evolving AI and search trends — including generative engine optimization (GEO), AI-driven search behavior, and how tools like ChatGPT, Perplexity, and Google's AI Overviews are reshaping how patients and families discover pediatric healthcare — and who applies AI-assisted tools responsibly to improve marketing performance and brand visibility.
> ... Working knowledge of search engine optimization (SEO) and generative engine optimization (GEO) principles, website UX best practices, and conversion optimization. Demonstrated understanding of how AI-driven search experiences are reshaping how patients, families, and referring providers find pediatric healthcare information, and how paid and organic strategies must evolve to maintain brand visibility and patient acquisition in this environment.
> ... Familiarity with generative engine optimization (GEO) concepts, including how to structure content, schema markup, and digital authority signals to improve institutional visibility in AI-generated answers and citations — with a particular understanding of how these dynamics apply to pediatric healthcare queries and patient decision journeys.
> Pay Range: $70,720.00-$115,627.20 Salary. ... AI Notice: Lurie Children's utilizes certain AI-enabled features within our recruiting platform to support candidate engagement and assist recruiters in identifying and prioritizing applicants whose experience aligns with job requirements. All employment decisions are made by individuals.

### Card #23 — CuriOdyssey, "Director of Marketing, Communications, and Membership"

- Employer URL: https://curiodyssey.org/wp-content/uploads/2026/09/CuriOdyssey_Director_of_Marketing_Job_Posting_2026_FINAL_rev1.docx.pdf (linked from curiodyssey.org/about/employment/); 4-page PDF, extracted with `pdftotext`
- Indeed card: jobkey ac7d83940408a711, "11 days ago" as of 2026-09-23, "$140,000 a year", San Mateo, CA 94401
- PDF fields: no datePosted field (static PDF); body states "Status and Salary: Full-time, exempt, $140,000 annual salary"
- Phrase check: "answer-engine optimization" 1; "generative-engine optimization" 1; "AI-search" 2
- Salary in body: "$140,000 annual salary" — matches card exactly
- Employer size text in body: "annual operating budget of approximately $7 million"; "manage the department's approximately $550,000 annual budget"; headcount not stated — nonprofit museum/zoo, small organization

> POSITION SUMMARY: Celebrating our 72nd year, CuriOdyssey is a children's science museum and zoo located in Coyote Point Recreation Area, San Mateo County, California... We are seeking a strategic, growth-oriented Director of Marketing, Communications and Membership to lead audience development and strengthen earned revenue for a nonprofit science museum and zoo with an annual operating budget of approximately $7 million.
> ESSENTIAL RESPONSIBILITIES: ... Website and search. Own the marketing roadmap for website content, user journeys, and conversion. Lead SEO and evolving AI-search visibility practices, including technical and content improvements, structured data, local discovery, and measurement through analytics and search platforms.
> REQUIRED QUALIFICATIONS: ... Experience with SEO and AI-search optimization, including the evolving practices often described as answer-engine optimization or generative-engine optimization. Ability to distinguish durable, evidence-based search practices from short-lived tactics.
> WORK ARRANGEMENT AND ENVIRONMENT: Status and Salary: Full-time, exempt, $140,000 annual salary. Hybrid schedule: Four days on-site and one day working remotely each week...

### Card #27 — CCYP / Impulse Universe Inc, "CCYP Marketing Operations Specialist"

- Employer URL: https://impulse-universe-inc.careerplug.com/jobs/3575235 (the Indeed jobkey's own careerplug listing had rotated off; found by re-querying the employer's live job list at /jobs and matching the exact title)
- Indeed card: jobkey 9ecbc868eb0dfe6f, "22 days ago" as of 2026-09-23, "$46,000 - $60,000 a year", Rosemead, CA 91770
- CareerPlug JSON-LD: `"datePosted":"2026-09-01T00:36:31+00:00"`, `"baseSalary":{"unitText":"YEAR","minValue":"46000.00","maxValue":"60000.00"}`
- Phrase check: "Answer Engine Optimization (AEO)" 2; "SEO/AEO" 1; "Agentic AI" 1
- Salary in body: "$46,000.00-$60,000.00 YEAR" — matches card exactly
- Employer size text in body: none stated; "a 45-year proprietary database"

> We are looking for a highly organized, detail-oriented Marketing Operations Specialist to help power CCYP's next stage of digital growth. In this role, you will serve as an integrational member behind our marketing initiatives: managing digital platforms, coordinating content and campaign workflows, maintaining web properties, and ensuring that projects move smoothly from planning through execution.
> The Role: Marketing Operations & Workflow Management...; Website & Digital Property Management...; Content & Data Quality Control...; AI & Marketing Technology Support: Help test, implement, and manage emerging AI tools and automation workflows as CCYP expands its AI-first marketing and business services ecosystem.
> Requirements: ... Digital Marketing Literacy: Working knowledge of modern digital marketing fundamentals, including websites, SEO/AEO, social media, email marketing, content marketing, video, lead generation, and digital analytics. ...
> Preferred Qualifications: ... Familiarity with AI tools, workflow automation, Answer Engine Optimization (AEO), local search, structured business data, or emerging marketing technologies is a strong plus.
> Why CCYP: A Legacy of Excellence, A Future of Innovation: Founded in the 1980s, CCYP has served as the definitive cornerstone of the Chinese-American business community for over four decades... from the foundational days of high-authority print directories to the rapid expansion of the digital age, and now, to the frontier of Agentic AI. Our success is built on an unparalleled foundation: a 45-year proprietary database that serves as the "Knowledge Database" for the North American Chinese business ecosystem. We are currently architecting CCYP's transition into an AI-first B2B ecosystem. From Answer Engine Optimization (AEO) and Verified Business Certification to intelligent business data, digital visibility, web, video, and AI-powered marketing solutions, we are building the operational infrastructure that will empower the next generation of professional services across North America.

### Card #28 — CCYP / Impulse Universe Inc, "CCYP Digital Content & Web Coordinator"

- Employer URL: https://impulse-universe-inc.careerplug.com/jobs/3575239
- Indeed card: jobkey c623b42d89cd1c27, "22 days ago" as of 2026-09-23, "$3,900 - $4,500 a month", Rosemead, CA 91770
- CareerPlug JSON-LD: `"datePosted":"2026-09-01T00:45:15+00:00"`, `"baseSalary":{"unitText":"MONTH","minValue":"3900.00","maxValue":"4500.00"}`
- Phrase check: "Answer Engine Optimization" 2 (once as "AEO" abbreviation on first use, once spelled out standalone); "SEO & AEO Content Support" 1 (section heading)
- Salary in body: "$3,900.00-$4,500.00 MONTH" — matches card exactly
- Employer size text in body: same "AI-first B2B ecosystem" self-description as card #27 (same employer)

> We are looking for a detail-oriented, digitally savvy Digital Content & Web Coordinator to help maintain and strengthen CCYP's growing portfolio of web properties, business directories, digital content, and online business information... This is not a web development or programming position.
> The Role: Website Content Management...; SEO & AEO Content Support: Apply basic SEO and Answer Engine Optimization best practices when publishing content, including page titles, descriptions, headings, internal links, structured information, business categories, and other content elements that improve digital discoverability. Bilingual Content Coordination...
> Preferred Qualifications: ... Familiarity with SEO, local search, structured data, schema markup, or Answer Engine Optimization (AEO) is a plus. Experience using AI tools for research, content preparation, categorization, summarization, data cleanup, or content quality control is a plus.
> Why CCYP: ... CCYP is currently building our transition into an AI-first B2B ecosystem. We are developing the infrastructure for a new generation of business discovery and visibility services, including Answer Engine Optimization (AEO), Verified Business Certification, structured business intelligence, digital media, and AI-powered business solutions. Search engines, answer engines, AI agents, consumers, and businesses all depend on reliable digital information to understand who a business is, what it does, where it operates, and why it should be trusted.

### Card #30 — Accel Marketing Solutions, Inc., "Legal Content Writer"

- Employer URL: https://careers.jobscore.com/careers/accelmarketingsolutionsinc/jobs/legal-content-writer-aXiU5D9DXaukzZj4Eiq5ZC
- Indeed card: jobkey 0b56a079db3fb1a6, "30+ days ago" as of 2026-09-23, "$50,000 - $60,000 a year", Montvale, NJ 07645
- JobScore listing: no datePosted field captured by the pull script
- Phrase check: "Answer Engine Optimization" 3; "AI search" 2; "AI-powered search experiences" 1; "ChatGPT" 1; "Google AI Overviews" 1
- Salary in body: "$50,000" / "$60,000" appear three times in a range context — matches card
- Employer size text in body: none stated; agency serving "law firms or legal organizations"

> ... is to position attorneys as trusted authorities in their fields while improving their visibility in traditional search results, Google AI Overviews, ChatGPT, and other AI-powered search experiences. This position requires strong writing and editing skills, knowledge of SEO, and professional experience...
> ... Experience working for a digital marketing, advertising, or content agency. Experience with Answer Engine Optimization and AI-powered search. Experience managing editorial or client content calendars. Familiarity with professional-services [marketing] ...
> Duties: Website copywriting; Landing-page content; Email marketing; Keyword research; SEO content optimization; Answer Engine Optimization; AI prompting and AI-assisted editing; WordPress; Google Docs; Grammarly or comparable editing tools.
> ... Review and substantially edit AI-assisted material to ensure it is accurate, original, engaging, and aligned with the client's voice. Apply SEO, Answer Engine Optimization, and AI-search best practices. Perform keyword research and incorporate relevant search topics naturally into content. ... Manage multiple clients, assignments, revisions, and deadlines simultaneously. Stay current on changes involving SEO, AI search, legal marketing, and content strategy. Help improve Accel's internal AI-assisted content processes without sacrificing quality or originality.

[note: Accel Marketing Solutions is itself a marketing agency serving law-firm clients — this posting evidences the agency's own hiring, not a purchase by a regulated buyer (per `demand-signals.md` cell-attribution rule, an agency's own posting about serving a vertical's clients does not attribute to that vertical's buyer-side cell)]

## Cards read in full — no GEO/AEO/AI-search duty language found

### Card #25 — HCVT, "Senior Marketing Specialist"

- Employer URL: https://jobs.lever.co/hcvt/f499cf72-0d2c-40da-ab14-d8ba991665e7 (`api.lever.co/v0/postings/hcvt`, 31 open roles enumerated)
- Indeed card: jobkey b88fa3fcf2679273, "30+ days ago" as of 2026-09-23, "$80,000 - $90,000 a year", West Los Angeles, CA
- Lever fields: `createdAt` epoch 1786559116253 (2026-08-09), `team: "Growth"`, `commitment: "Full-time"`
- Phrase check: 0 hits for GEO, AEO, generative engine, answer engine, AI search, AI visibility, ChatGPT, Gemini, Perplexity, Claude, LLM. Body names only "AI-enabled tools, automation, and innovative technologies that enhance marketing effectiveness and operational efficiency" — generic, undifferentiated from any modern marketing-ops role
- Salary in body: none found in the fetched section (page truncated by the pull script; Lever posting pages are often split into separate description/salaryDescription fields and the latter returned `null` for this posting)

> Come for the Challenge. Stay for the Experience. At HCVT, we believe every challenge presents an opportunity to positively impact our clients and people... We offer Tax, Audit, Advisory, and Business Management services to our clients... We are seeking a highly motivated and adaptable marketing professional to join our Growth team. This individual will play a critical role in supporting firm growth initiatives through proposal development, digital presence, and marketing execution, while also contributing to ongoing transformation efforts including the adoption of AI-enabled tools, automation, and innovative technologies that enhance marketing effectiveness and operational efficiency. This role plays a key role within a small, collaborative Growth team, supporting proposals, digital visibility, and marketing execution while contributing to process improvements and innovation initiatives.

### Card #29 — Viderity Inc., "Senior Writer Project Manager"

- Employer URL: https://viderity.recruitee.com/o/senior-writer-project-manager
- Indeed card: jobkey 02e2f5fabc842d6a, "30+ days ago" as of 2026-09-23, "$108,292 - $128,292 a year", Alexandria, VA
- Recruitee fields: `published_at: "2026-08-06 16:19:27 UTC"`, `created_at: "2026-03-06 03:45:43 UTC"`, `city: "Alexandria"`
- Phrase check: 0 hits for GEO, AEO, generative engine, answer engine, AI search, AI visibility, ChatGPT, Gemini, Perplexity, Claude, LLM, salary, or "$" — the posting is a federal-contractor (HUBZone/WOSB) speechwriting role for NSF leadership, unrelated to search or AI-assistant visibility
- Salary in body: none — Recruitee's `description` field for this posting carries no compensation figure

> About Viderity: Viderity is a HUBZone-certified and Woman-Owned Small Business (WOSB) delivering award-winning IT, digital, and creative solutions across federal and commercial markets... Position Overview: The Speechwriting and leadership support services will include drafting speeches, remarks, talking points, internal communications, congressional testimony, and presentations for NSF leadership...

[note: this card's Indeed match on the GEO/AEO/AI-visibility search terms appears to be a false positive — the posting body contains none of the queried phrases; either the match came from Indeed's own fuzzy ranking or from a since-edited version of the listing]

## Cards checked, not found on the employer's own board

| Card | Employer | Title (Indeed card) | Channel checked, 2026-09-23 | Result |
|---|---|---|---|---|
| #17 | Astellas | Associate Director, Global Media Relations | careers.astellas.com (SuccessFactors `/search/`) — 50-row listing enumerated, closest match "External Corporate Communications Specialist" in Northbrook, IL (same city) | title not present on the returned page; SF search endpoint appears to ignore the query string and return a fixed static-first-page list; not paginated further |
| #24 | CWILL INC | Bilingual Mandarin Product Manager (SEO SaaS Product) | cwill.com/jobs/ (JS-rendered, no static job data); Glassdoor mirror of the exact listing (job-listing/product-manager-seo-saas-product-cwill-inc) | cwill.com/jobs/ returned no job JSON in the static HTML; Glassdoor returned HTTP 403, title "Security \| Glassdoor", a captcha/bot-block page |
| #33 | Smith & Wesson Brands, Inc | Web Content Specialist I | store.smith-wesson.com/company/careers/ → ADP Recruiting (recruiting.adp.com/srccar/public/RTI.home?d=External&c=1055241) | ADP RTI page is an Angular SPA; the fetched HTML carries no job data, only a script-loader shell (2,394 bytes) |
| #31 | CAL Financial, Inc. | Independent Contractor Opportunity: Fractional IT Manager (1099) | cal-financial.com/careers (Duda site builder, JS-rendered); app.idealtraits.com/career/CAL-Financial,-Inc./317723vie | cal-financial.com/careers returned a Duda bootstrap shell with no static job list; idealtraits mirror returned HTTP 410 Gone |
| #15 | The Pond Guy | SEO Content Strategist | thepondguy.com/jobs/ | job entry present only as a linked image (`.../content/jobs/seo-content-strategist.jpg`), no extractable text; not OCR'd this pull |
| #13 | MPI Label Printing | Website Marketing Specialist | mpilabels.com/employment/ | employment page lists an application form, no job-description text matching this title; only "geoip" (a tracking-script term) matched the GEO/AEO grep, a false positive |
| #7 | Liliuokalani Trust | Specialist, Digital Platforms | onipaa.org/job-openings, onipaa.org/pages/careers | neither page returned a job list in the fetched HTML (176,624 bytes, likely JS-rendered) |
| #26 | Gwynedd Mercy University | Vice President for Marketing Communications | gmercyu.edu/about-gmercyu/careers-gmercyu → apply.gmercyu.edu/portal/visit | the university's careers page links an applicant portal; no static job list or job-detail text was reachable by curl |
| #32 | The Advocates | Content Writer | advocates.org/careers (a Massachusetts refugee/immigrant-services nonprofit; possibly not the same "The Advocates" as the Indeed card, which gave no city) | page lists career-fair events, no job postings; ambiguous employer match, not resolved further |

## Cards not newly attempted this pull — already resolved as not-found in the superseded file

Per `docs/raw/f-indeed-S1-repull3-2026-09-23.md` §"Checked, not found" and its "Cards not attempted" list, re-confirmed as still the best available read, not re-probed this pull: #1 and #14 RestauNax ("AI-Native Marketing Lead" ×2 — restaunax.com careers/jobs/join-us all 404); #3 Intuit ("Staff AI Scientist" — jobs.intuit.com results are script-rendered); #8 Vasion ("Head of Search & AI Visibility" — 5 open Workable roles, none matching); #16 Ziggi's Coffee ("Senior Manager, Performance Marketing" — store roles only); #34 GESA Credit Union ("Brand Content Strategist" — 0 matches in the Paycom listing).

## Vendor naming — none new this pull

No body in this pull names a dedicated AI-visibility vendor (Profound, Scrunch, Bluefish, Evertune, Otterly, AthenaHQ, Peec, Brandlight, etc.). Solventum's tool list names general SEO/content tools only (Adobe Experience Manager, Adobe Analytics, Google Search Console, SEMrush, Answer the Public, Screaming Frog). The one prior vendor-naming find in this vertical remains The Cigna Group ("Profound, Scrunch, Bluefish, Evertune"), `docs/raw/f-indeed-S1-repull3-2026-09-23.md`, not re-found here.

## Pull notes — mechanical only

- No Indeed request made. DuckDuckGo's `html.duckduckgo.com/html/` endpoint was used only to locate each employer's own domain/ATS URL from its name and city; no DuckDuckGo result content is quoted as evidence above.
- ATS families reached this pull, by count: Workday CXS JSON (Fresenius Kabi, Lurie Children's, Solventum — 3), Greenhouse boards-api JSON (Giftogram — 1), Lever API JSON (HCVT — 1), Workable widget JSON (Rational 360 — 1), Paylocity HTML+JSON-LD (Safe Life US — 1), CareerPlug JSON-LD (CCYP/Impulse Universe — 2), JobScore HTML (Accel Marketing — 1), Recruitee JSON API (Viderity — 1), JobTarget HTML (Playboy — 1), static PDF (CuriOdyssey — 1). No Ashby or SmartRecruiters endpoint returned a hit this pull (Ashby was tried for A Place for Mom in the superseded file, not repeated here).
- Astellas: guessed Workday tenant names (`astellas.wd1/astellas_careers`, etc.) all returned HTTP 500 before the real system was found to be SuccessFactors, not Workday; recorded so a future pull does not repeat the guesswork.
- Several employers' ATS pages are Angular/React SPAs that return only a script-loader shell to a plain curl (ADP RTI for Smith & Wesson, Duda for CAL Financial, and the unresolved trust/university pages) — these need a JS-executing fetch (or the Chrome extension, excluded from this pull's brief) to read further.
- IMPULSE UNIVERSE INC's CareerPlug job IDs on the original Indeed cards (3426467, 3426535) had rotated to different, currently-open postings ("CCYP Sales Support Assistant", "CCYP B2B Account Executive") by 2026-09-23; the original two titles were re-found at new IDs (3575235, 3575239) by re-fetching the employer's live `/jobs` list and matching on exact title and salary.
- Character encoding: CCYP body text required `encode('latin1').decode('utf-8')` re-interpretation to render correctly (source served JSON-escaped UTF-8 bytes double-encoded); other bodies needed no such correction.
- No data image on any page this pull; nothing saved to `docs/raw/img/`.
