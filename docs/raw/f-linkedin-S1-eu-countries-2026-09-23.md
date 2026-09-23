# LinkedIn Jobs (guest search API) — S1 job postings by country: UK, France, Spain, Italy, Netherlands; three terms each; eleven job pages opened

```yaml
source:          LinkedIn Jobs, public guest search endpoint and public guest job-posting endpoint (no login)
url_or_doc_id:   https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=<term>&location=<country>&start=0 — terms "generative engine optimization", "AI visibility", "answer engine optimization"; countries United Kingdom, France, Spain, Italy, Netherlands (15 calls) ; https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<id> for ids 4442217551, 4441092689, 4469212558, 4465566607, 4464980839, 4461673134, 4469896706, 4452991061, 4455365173, 4439323459, 4450244205
published:       posting dates per card, 2026-04-01 to 2026-09-23; job pages show relative "posted" text at pull time
pull_date:       2026-09-23
pull_method:     fetch (curl, 12 s between search calls, 8 s between job-page calls); first result page only (10 cards) per query
pull_purpose:    evidence about a number (S1 per country)
tier:            3
tier_reason:     employer's own posting via the platform's public listing (demand-signals.md S1 default 3); relevance-sorted first page, not a count; LinkedIn's "GEO"/"AI" matching is loose and returns unrelated AI-engineering roles
source_label:    company-stated
lane:            F
sub_market:      organic recommendation (all category hits below)
engine:          ChatGPT, Perplexity, Google AI Overviews, Claude — as the postings name them
metric_kind:     none
supersedes:      none (docs/raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md covered Worldwide searches and opened the Pennylane posting; this file is the per-country cut)
captured:        category-relevant cards per country (title | employer | location | posted | URL); job-page fields for eleven postings; non-category cards summarised by count
```

## Category-relevant cards per country (cards whose title names SEO/GEO/AEO/AI search; all other cards on the page were AI-engineering, computer-vision or data roles)

United Kingdom — `"answer engine optimization"` (10 cards; 1 of 10 names GEO in the title, 3 name AI/LLM search):
```
Senior Technical SEO Manager | Proton | London, England, United Kingdom | 2026-09-13 | uk.linkedin.com/jobs/view/senior-technical-seo-manager-at-proton-4439323459
Search Optimisation Specialist | Phoenix Software | Pocklington, England, United Kingdom | 2026-08-27
Senior SEO Editor | The Sun | London Area, United Kingdom | 2026-09-17
Senior SEO Executive | emap | City Of London, England, United Kingdom | 2026-09-02
SEO Content Executive | Charle Agency - Shopify Plus Partner Agency | London Area, United Kingdom | 2026-08-13
Senior SEO & Website Optimisation Specialist | Cyberlogical | Reading, England, United Kingdom | 2026-09-16
SEO & AI Search Specialist | Elixirr | London, England, United Kingdom | 2026-09-04 | …/seo-ai-search-specialist-at-elixirr-4436303917
Head of SEO | 1st Formations | London, England, United Kingdom | 2026-09-03
Programmatic SEO + GEO | Arithmos | Harrow, England, United Kingdom | 2026-09-04 | …/programmatic-seo-%2B-geo-at-arithmos-4463619462
Senior Manager - Search & LLM Discovery | Compare the Market | Peterborough, England, United Kingdom | 2026-09-08 | …/senior-manager-search-llm-discovery-at-compare-the-market-4455365173
```
United Kingdom — `"generative engine optimization"` and `"AI visibility"`: 10 cards each, 0 category-relevant (AI engineers, safety and evaluation roles, e.g. Reflection, AISI, Bumble, Fitch, G-Research, Lovable, Granola).

France — `"answer engine optimization"` (10 cards; 7 category-relevant):
```
SEO & AI Content Specialist | Pennylane | Nice / Paris / Greater Lille (three postings, same role) | 2026-09-18 | fr.linkedin.com/jobs/view/seo-ai-content-specialist-at-pennylane-4469211663 ; -4469212558 ; -4469214077
Head of SEO - M/W | ManoMano | Paris | 2026-09-21
Responsable SEO et GEO (H/F) | Hello Watt | Paris | 2026-07-20 | …/responsable-seo-et-geo-h-f-at-hello-watt-4442217551
SEO & AI Search Manager H/F | Feu Vert France | Écully, Auvergne-Rhône-Alpes | 2026-09-08 | …/seo-ai-search-manager-h-f-at-feu-vert-france-4451407600
Senior SEO Spécialist H/F ; Senior SEO Specialist H/F | Plus que pro | Obernai, Grand Est | 2026-06-26 ; 2026-09-22
Head of Organic Performance – SEO and GEO (x/f/m) | leboncoin | Paris | 2026-09-18 | …/head-of-organic-performance-…-at-leboncoin-4450244205
Technical SEO expert | North Star Network | Levallois-Perret | 2026-06-22
```
France — `"generative engine optimization"`: 10 cards, 4 category-relevant (leboncoin, Feu Vert, Pennylane ×3 — same as above). `"AI visibility"`: 0 category-relevant (computer-vision and data roles).

Spain — `"answer engine optimization"` (10 cards; 8 category-relevant):
```
SEO & GEO Specialist | BeRepublic | Barcelona | 2026-09-21 | es.linkedin.com/jobs/view/seo-geo-specialist-at-berepublic-4469896706
Especialista SEO Técnico & Estrategia Orgánica | Modern Talent Hub (consultora IT) | Zaragoza | 2026-09-15
SEO/GEO Specialist Jr (Barcelona) ; SEO/GEO Specialist Jr (Madrid) | Good Rebels | 2026-07-20
Brand Visibility Product Expert, SEO & AI Visibility (Enterprise Solution Unit) | Semrush | Spain | 2026-09-04 | …-at-semrush-4452991061
Search Engine Optimization / VBET | VBET | Spain | 2026-08-27
SEO Technical Lead - Madrid based ; SEO Technical Lead | Fever | Barcelona ; Madrid | 2026-09-22
SEO Manager | iSpeedToLead | Madrid | 2026-08-21
Especialista GEO & SEO en Omnia | Candee | Marín, Galicia | 2026-05-29
```
Spain — `"generative engine optimization"`: 10 cards, 1 category-relevant: `Senior GEO Manager - LLM Search Optimization | Make | Madrid | 2026-09-03 | …/senior-geo-manager-llm-search-optimization-at-make-4441092689`. `"AI visibility"`: 0 category-relevant.

Italy — `"answer engine optimization"` (10 cards; 9 category-relevant):
```
Senior SEO & AI Search Lead (SEO / GEO / AEO) | Pete Tong DJ Academy | Rome | 2026-09-09 | it.linkedin.com/jobs/view/…-at-pete-tong-dj-academy-4464980839
SEO Specialist ×2 ; Senior SEO Specialist ×2 | Webranking | Correggio ; Milan | 2026-07-29 ; 2026-07-30
SEO Specialist | Immobiliare.it | Rome | 2026-08-31
Specialista SEO | Markeven srl | Modena | 2026-09-18
SEO/GEO Specialist - 38-42K | Untamed | Milan | 2026-09-16 | …/seo-geo-specialist-38-42k-at-untamed-4465566607
SEO Manager | Cerved | Milan | 2026-09-17
```
Italy — `"generative engine optimization"`: 10 cards, 2 category-relevant (Pete Tong DJ Academy as above; `AI Search Innovation Lead - Madrid based | Fever | Rome | 2026-09-22`). `"AI visibility"`: 0 category-relevant.

Netherlands — `"answer engine optimization"` (10 cards; 10 SEO roles, 1 names GEO in the title):
```
SEO Specialist (SEO & GEO) | Social Brothers NL | Utrecht | 2026-09-03 | nl.linkedin.com/jobs/view/seo-specialist-seo-geo-at-social-brothers-nl-4461673134
Senior SEO Specialist ×4 | iO | Den Bosch / Rotterdam / Utrecht / Amsterdam | 2026-09-05/06
SEO-specialist | Traffic Builders | Almere | 2026-09-10
SEO Manager | iSpeedToLead | Amsterdam | 2026-08-21
SEO Specialist | TO BE FOUND | Dordrecht | 2026-07-07
Senior SEO-specialist | Brandfirm | Amsterdam | 2026-08-04
SEO Specialist | Small Giants | Utrecht | 2026-09-07
```
Netherlands — `"generative engine optimization"`: 10 cards, 0 category-relevant except `Staff AI Engineer - Agentic Shopping | Picnic Technologies | Amsterdam | 2026-09-04` (agentic-commerce engineering, not a marketing role). `"AI visibility"`: 0 category-relevant.

## Job pages opened (guest jobPosting endpoint) — fields verbatim

| id | title | employer | location | applicants | posted (relative, at pull) | criteria (Seniority / Employment / Function / Industries) |
|---|---|---|---|---|---|---|
| 4455365173 | Senior Manager - Search & LLM Discovery | Compare the Market | Peterborough, England, United Kingdom | 26 applicants | 2 weeks ago | Not Applicable / Full-time / Marketing and Sales / Software Development |
| 4439323459 | Senior Technical SEO Manager | Proton | London, England, United Kingdom | 125 applicants | 1 week ago | Mid-Senior level / Full-time / Marketing and Sales / Technology, Information and Internet |
| 4442217551 | Responsable SEO et GEO (H/F) | Hello Watt | Paris, Île-de-France, France | 88 applicants | 2 months ago | Not Applicable / Full-time / Sales / Software Development |
| 4469212558 | SEO & AI Content Specialist | Pennylane | Paris, Île-de-France, France | 75 applicants | 4 days ago | Not Applicable / Full-time / Marketing and Sales / Accounting |
| 4450244205 | Head of Organic Performance – SEO and GEO (x/f/m) | leboncoin | Paris, Île-de-France, France | 162 applicants | 4 days ago | Not Applicable / Full-time / Marketing and Sales / Software Development |
| 4441092689 | Senior GEO Manager - LLM Search Optimization | Make | Madrid, Community of Madrid, Spain | 151 applicants | 2 weeks ago | Mid-Senior level / Full-time / Information Technology and Marketing / Software Development |
| 4469896706 | SEO & GEO Specialist | BeRepublic | Barcelona, Catalonia, Spain | 62 applicants | 1 day ago | Entry level / Full-time / Marketing and Sales / Marketing Services |
| 4452991061 | Brand Visibility Product Expert, SEO & AI Visibility (Enterprise Solution Unit) | Semrush | Spain | 75 applicants | 2 weeks ago | Not Applicable / Full-time / Sales and Business Development / Software Development |
| 4464980839 | Senior SEO & AI Search Lead (SEO / GEO / AEO) | Pete Tong DJ Academy | Rome, Latium, Italy | 70 applicants | 2 weeks ago | Mid-Senior level / Full-time / — / Education and Artists and Writers |
| 4465566607 | SEO/GEO Specialist - 38-42K | Untamed | Milan, Lombardy, Italy | 63 applicants | 1 week ago | Entry level / Full-time / Marketing and Sales / Advertising Services |
| 4461673134 | SEO Specialist (SEO & GEO) | Social Brothers NL | Utrecht, Utrecht, Netherlands | Be among the first 25 applicants | 2 weeks ago | Mid-Senior level / Full-time / Marketing / Advertising Services |

## Description excerpts naming the category (verbatim sentences)

Compare the Market (4455365173):
> "We are looking for an experienced LLM Discovery & Optimisation Lead to define and lead our organic growth strategy across SEO and emerging AI-powered discovery environments." — "Act as the organisation's authority on generative AI discovery, monitoring developments across search engines, AI platforms and LLM ecosystems, translating emerging trends into actionable strategic direction." — "If you are excited by the future of search, generative AI, and digital growth, this is an opportunity to build a new capability at the heart of our business." — "Function: Growth Location: London / Peterborough"

Proton (4439323459): no sentence in the description matched answer engine / AEO / LLM / ChatGPT / AI; the card matched LinkedIn's query expansion. Description states "Our 700+ team members across 50+ countries come from leading organizations and elite academic backgrounds" and "Millions of people trust Proton with their privacy."

Hello Watt (4442217551):
> "Avec l'avènement de l'IA et du GEO (Generative Engine Optimization), le paysage du Search évolue radicalement." — "Stratégie SEO & GEO (Generative Engine Optimization) Définir et exécuter la roadmap SEO pour dominer le marché français et soutenir notre expansion en Espagne." — "Piloter la transition du SEO vers le GEO pour garantir qu'Hello Watt reste la réponse de référence des moteurs génératifs (AI Overviews, LLMs)." — "Suivre et reporter précisément les performances SEO/GEO (volume d'articles publiés, positions, citations LLM, trafic, conversions,…"

Pennylane (4469212558):
> "At Pennylane, SEO and Generative Engine Optimization (GEO) are central to making our product easier to discover and understand, while helping us reach new customers." — "…how people discover products through search engines and AI assistants such as ChatGPT and Perplexity." — "Help develop our GEO approach — Build an understanding of the questions and prompts prospects use in AI-powered discovery tools."

leboncoin (4450244205):
> "…alimentés par l'intelligence artificielle — nous recherchons un·e Head of Organic Performance pour définir et piloter notre stratégie SEO et GEO (Generative Engine Optimization)."

Make (4441092689):
> "What You'll Own — GEO / AEO strategy — build and run Make's approach to being cited (correctly, favorably, and often) across ChatGPT, Perplexity, Google AI Overviews, and Claude." — "Authority & source repair — identify and close the gaps in the sources LLMs actually draw from (this includes unglamorous work like earning back reinstated, high-trust reference sources)." — "Entity-based content architecture — work with the content team to restructure key topics into the clusters and schema that both traditional crawlers and LLM retrieval reward." — "…ai, or equivalent LLM-citation tracking (or the instinct to build your own when off-the-shelf isn't enough)." — "Automation & AI — Python (or similar scripting) plus LLM APIs (Claude, OpenAI) to build monitoring and reporting that runs itself."

BeRepublic (4469896706):
> "En BeRepublic Barcelona buscamos un/a SEO & GEO Specialist para diseñar, ejecutar y optimizar estrategias de posicionamiento orgánico para nuestros clientes." — "Analizar la presencia y visibilidad de las marcas en nuevos entornos de búsqueda basados en IA y LLMs."

Semrush (4452991061) — vendor, sell-side:
> "We unify SEO authority and AI visibility, so brands are found, cited, and chosen everywhere search happens." — "All thanks to 1700+ employees who build the company every day"

Pete Tong DJ Academy (4464980839):
> "You will own everything organic: technical SEO, the topic and keyword strategy our content team executes, visibility in AI search (being cited by ChatGPT, Perplexity and Google AI Overviews), YouTube search, and the backlinks and growth loops that compound over time." — "(GEO / AEO): making PTDJA the source AI assistants cite for DJ and production questions: entity building, citations, content structured for answer engines." — "…serving members in more than 140 countries"

Untamed (4465566607) — agency:
> "…sarà responsabile della visibilità organica dei siti in portafoglio, sia sui motori di ricerca tradizionali sia sui motori generativi (GEO/AEO) e avrà il compito di costruire il metodo di audit e strategia interno." — "GEO & Motori Generativi — Generare e mantenere file llms." — title carries the salary band "38-42K".

Social Brothers NL (4461673134) — agency: description text not extracted (page 18,887 bytes; description block absent from the guest render).

## Employer headcount checks (for the buyer-size band)

| Employer | Source tried | Result |
|---|---|---|
| Pennylane | already recorded: "Pennylane 1,100+" in `docs/customers/b2b-saas.md` cell reads (from `f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md`) | enterprise band by headcount |
| Proton | job description | "700+ team members across 50+ countries" |
| Semrush | job description | "1700+ employees" |
| Compare the Market | comparethemarket.com/about-us/ | HTTP 403 — headcount `unknown — checked 2026-09-23` |
| Make | make.com/en/about-us (404), make.com/en/company (403) | `unknown — checked 2026-09-23` |
| Hello Watt | hellowatt.fr/a-propos (404), welcometothejungle.com company page (403) | `unknown — checked 2026-09-23` |
| leboncoin, Feu Vert, ManoMano, Fever, Pete Tong DJ Academy | not checked | — |

## Pull notes — mechanical only

- 15 search calls and 11 job-page calls, all HTTP 200. Cards are the first page (10) in LinkedIn's relevance order; a query with fewer than 10 matches would return fewer cards, and none did, so these pages are not counts.
- LinkedIn's guest search expands `"AI visibility"` and `"generative engine optimization"` to generic AI/ML roles in every country; only the `"answer engine optimization"` pages were dominated by SEO/GEO roles.
- Job-page "applicants" and "posted" are as displayed at pull time (2026-09-23). Company headcount is not a field on the guest job page.
