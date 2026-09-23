# National job boards — S1 postings with paid-placement and agentic-commerce terms: Hellowork (FR) with three postings opened and one employer headcount check, Tecnoempleo (ES); UK and NL boards walled

```yaml
source:          hellowork.com (FR) search and posting pages; alan.com careers page (employer headcount); tecnoempleo.com (ES) search pages; access probes of cv-library.co.uk, totaljobs.com (UK), werkzoeken.nl, indeed.nl (NL); recherche-entreprises.api.gouv.fr (Sirene) lookup
url_or_doc_id:   https://www.hellowork.com/fr-fr/emploi/recherche.html?k=agentic+commerce ; …?k=ChatGPT+ads ; …?k=commerce+agentique ; …?k=ChatGPT ; …?k=publicité+IA ; https://www.hellowork.com/fr-fr/emplois/79332669.html ; https://www.hellowork.com/fr-fr/emplois/83492047.html ; https://www.hellowork.com/fr-fr/emplois/80876230.html ; https://alan.com/en/careers ; https://www.tecnoempleo.com/ofertas-trabajo/?te=agentic+commerce ; …?te=chatgpt+ads ; …?te=publicidad+IA ; …?te=comercio+agentico ; …?te=ChatGPT ; https://recherche-entreprises.api.gouv.fr/search?q=Alan%20assurance&per_page=5
published:       Hellowork postings datePosted 2026-09-02, 2026-09-17, 2026-09-22; Tecnoempleo postings 2026-08-31; alan.com careers page undated — no date on page
pull_date:       2026-09-23
pull_method:     fetch (curl), 3 s between calls; no login, no form submission
pull_purpose:    evidence about a number (S1 per country, paid placement and agentic commerce sub-markets)
tier:            3
tier_reason:     employer's own posting via a national board (S1 default 3); board result counts are the board's for its own normalised query; the alan.com headcount line is the employer's own careers page (company-stated); the Sirene lookup returned no Alan entity in five results and is recorded as a failed check
source_label:    company-stated
lane:            F
sub_market:      agentic commerce (Alan posting); paid placement (queries only — no posting names AI ads)
engine:          "a GPT app" and "LLM ecosystems" (Alan posting); ChatGPT / Claude / Gemini as creative tools (Havea posting)
metric_kind:     none
supersedes:      none (docs/raw/f-jobboards-S1-eu-national-2026-09-23.md holds the organic-term access checks of the same boards; reed.co.uk, infojobs.net, infojobs.it and nationalevacaturebank.nl were walled or closed there and were not retried)
captured:        board counts and served card titles; three posting pages — title, employer, datePosted, every sentence naming an AI, agentic or advertising term; employer headcount line; access table
```

## Hellowork (FR) — counts and served card titles

| Query `k=` | HTTP | Board count ("Afficher N offres") | Card titles served (title - employer), in order |
|---|---|---|---|
| agentic commerce | 200 | 2 | Consultant Senior - Transformation des Services de Paiement H/F - Square Management; Product Lead - Growth H/F - Alan |
| ChatGPT ads | 200 | 3 | Alternance Chargé Marketing Data et IA - Marseille H/F - ISCOD; Stage - Creative Strategy & Content Intern H/F - Havea; Chef de Projet H/F - Prélude Paris |
| commerce agentique | 200 | 7 | Business Manager Consulting - IA & Transformation Agentique H/F - Hardis Group; Founding Sales H/F - Team.is; Senior Sales Manager Cross Industries H/F - Accenture France; Product Owner Senior -E-Commerce B2b - Chilly-Mazarin H/F - Easypartner; Sre - DevOps - System Engineer H/F - iAdvize; Consultant Implémentation Saas H/F - iAdvize; Architecte - Lead Back Engineer H/F - iAdvize |
| ChatGPT | 200 | 15 | Formateur - Formatrice IA - Recrutement Paie & Facturation H/F - SOREDI; Développeur Python IA - Agentic Coding & Innovation K106 H/F - Kaiman Services; Account Executive Recruitment H/F - Team.is; Sales Recruitment H/F - Team.is; Talent Partner H/F - Team.is; Alternance - Consultant en Recrutement H/F - Team.is; Développeur IA - Applications sur Mesure & Gestion H/F - Nextep HR; Alternant Chef de Projet IA & Transformation Digitale H/F - CEVA LOGISTICS; Alternance Communication - Marketing H/F - MyDigitalSchool Montpellier; Chargé Marketing & Growth H/F - Proxiteam; Consultant SEO - Geo Senior H/F - Search Booster; Product Owner Senior Data & IA - CDI H/F - Talan |
| publicité IA | 500 | — | server error (203 bytes) |

## Hellowork posting 79332669 — Alan, "Product Lead - Growth H/F", datePosted 2026-09-22T00:09:44Z

> You'll set the agenda and ship against it: Conversational AI that guides prospects through our sales flows. AI-native acquisition surfaces. Alan inside LLM ecosystems. Picture a GPT app where a prospect can shop for and buy health insurance, and agentic commerce more broadly. You don't need to have built all of this before. You do need a real, opinionated view of where AI is going, and the drive to turn it into …
> You're close to AI. Either you've built AI products, or you follow the space closely and have a clear view on where to bet and how LLM systems behave in production.
> You talk to members and prospects often, you like doing it, and what you hear actually changes your mind. You care about healthcare.

[note: the posting text is in English on the French board; no salary, headcount or budget line on the page. hiringOrganization name "Alan".]

## Hellowork posting 83492047 — Havea, "Stage - Creative Strategy & Content Intern H/F", datePosted 2026-09-17T18:52:18Z

> … valoriser l'expertise de nos produits et performer sur les plateformes publicitaires. Meta, TikTok, UGC, contenus organiques, shootings, nouveaux formats, IA générative... les besoins créatifs se multiplient …
> 3. IA appliquée à la création - 15 % Utiliser ChatGPT / Claude / Gemini pour accélérer la recherche d'angles, hooks et scripts. Tester des outils de génération et d'édition d'images/vidéos par IA.
> … veiller à ce que les contenus générés restent cohérents avec l'identité et le niveau d'exigence de Biocyte. 4. Consumer & Competitive Insights - 15 % Analyser les publicités des concurrents … Suivre les tendances skincare, beauté, compléments alimentaires, wellness
> Compétences et outils Canva / CapCut / IA générative (ChatGPT, Claude, Gemini) / Ahrefs / Shopify / GA4 / Meta x TikTok Ads Manager / Notion

[note: an internship for the Biocyte brand (supplements); the ad platforms named are Meta and TikTok; ChatGPT, Claude and Gemini appear as creative tools, not as ad surfaces. Matched the board's "ChatGPT ads" query on separate tokens.]

## Hellowork posting 80876230 — Square Management, "Consultant Senior - Transformation des Services de Paiement H/F", datePosted 2026-09-02T00:16:20Z

> Analyse des marchés : Savoir guider son client au travers des innovations comme l'Euro Numérique, les Stablecoins, l'Agentic Commerce etc.

[note: a consultancy posting (sell-side).]

## Employer headcount check — Alan

- alan.com/en/careers (HTTP 200): "… funding round bringing the company's total valuation to €4bn. The team is 800+ people and growing."
- alan.com/en (HTTP 200), alan.com/fr-fr/a-propos, /en-fr/about-us, /fr-fr/qui-sommes-nous, /fr-fr/carrieres (404): no headcount line.
- linkedin.com/company/alan-healthcare, /company/alan: 404 to the guest fetch.
- recherche-entreprises.api.gouv.fr `q=Alan assurance`, 5 results: GIE SINTIA, TODAY ASSURANCES, YVES ALAN BOULET, SARL LE MOULLEC ASSURANCES, INEXA ASSURANCES — the Alan insurer did not surface in the first five; not retried.

## Tecnoempleo (ES) — counts and served cards

| Query `te=` | HTTP | Board count | Cards |
|---|---|---|---|
| agentic commerce | 200 | "2 Ofertas Trabajo de agentic commerce" | Agentic Commerce & AI Lead - Consumer Goods — Accenture, Madrid, 31/08/2026 ("Buscamos un/a Agentic Commerce & AI Lead con experiencia en estrategia, arquitectura y transformación digital para impulsar la adopción de soluciones basadas en Generative …"; tags Generative AI, Agentic AI, IA Generativa; Jefe de Proyecto); Data & AI Architect Agentic Commerce — Accenture, Barcelona, 31/08/2026 ("En Accenture Song buscamos profesionales con amplia experiencia en datos e inteligencia artificial …"; tags Inteligencia Artificial, Machine Learning, LLMs; Arquitecto TIC) |
| chatgpt ads | 200 | no count string served | no card titles served |
| publicidad IA | 200 | "1 Ofertas Trabajo de publicidad IA" | Creative content & Sales support |
| comercio agentico | 200 | no count string served | no card titles served |
| ChatGPT | 200 | "7 Ofertas Trabajo de ChatGPT" | Salesforce Sales Senior Consultant; Senior AI Engineer; Analista de Auditoría Interna y Analítica; Senior Fullstack Java/ Angular; Arquitecto/a Senior desarrollo software; Android Lead Engineer; Product Owner con Ingles (100% remoto) |

## Access table — UK and NL boards

| Country | Site | HTTP | Result |
|---|---|---|---|
| UK | cv-library.co.uk /search-jobs?q=agentic+commerce ; ?q=chatgpt+ads | 403 | "CV-Library.co.uk - Blocked" |
| UK | totaljobs.com /jobs/agentic-commerce | 403 | 400-byte block page |
| NL | werkzoeken.nl /vacatures/agentic-commerce | 403 | "Just a moment..." (Cloudflare) |
| NL | indeed.nl /jobs?q=agentic+commerce | 403 | "Security Check - Indeed.com" |
| IT | — | — | no national board tried beyond infojobs.it (closed, per the organic-term file) |

## Pull notes — mechanical only

- Hellowork search pages are server-rendered (347–468 KB); the count is the board's "Afficher N offres" string for its normalised query; card titles are the `title` attributes served, first page only.
- Tecnoempleo result pages are server-rendered; where the count string was absent the page carried no offer cards for the query.
- Posting pages were fetched once each; text extracted by tag-stripping and string search on AI, agentic and advertising terms; surrounding board chrome (job-coach widget text) was excluded.
