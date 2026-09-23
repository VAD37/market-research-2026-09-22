# LinkedIn Jobs (guest search API) — S1 postings with paid-placement and agentic-commerce terms by country: UK, France, Spain, Italy, Netherlands; 38 searches, five job pages opened

```yaml
source:          LinkedIn Jobs, public guest search endpoint and public guest job-posting endpoint (no login)
url_or_doc_id:   https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=<term>&location=<country>&start=0 — paid terms "ChatGPT ads", "AI ads", "sponsored answers"; agentic terms "agentic commerce", "Instant Checkout", "agentic checkout"; local-language terms FR "commerce agentique", "publicité IA"; ES "comercio agéntico", "publicidad en IA"; IT "commercio agentico", "pubblicità IA"; NL "agentic commerce" checkout, "AI advertenties" — countries United Kingdom, France, Spain, Italy, Netherlands (38 calls) ; https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<id> for ids 4463610105, 4463988880, 4315855270, 4423938094, 4446325005
published:       posting dates per card, 2026-05-29 to 2026-09-23; job pages show relative "posted" text at pull time
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, 12 s between search calls, 8 s between job-page calls); first result page only (10 cards) per query
pull_purpose:    evidence about a number (S1 per country, paid placement and agentic commerce sub-markets)
tier:            3
tier_reason:     employer's own posting via the platform's public listing (demand-signals.md S1 default 3); relevance-sorted first page, not a count; LinkedIn's token matching returns unrelated AI-engineering and Microsoft Copilot roles for every term
source_label:    company-stated
lane:            F
sub_market:      paid placement; agentic commerce
engine:          ChatGPT, Gemini, Copilot — only where a posting names them (none of the five job pages names a consumer assistant as a sales or ad surface)
metric_kind:     none
supersedes:      none (docs/raw/f-linkedin-S1-eu-countries-2026-09-23.md is the organic-term cut of the same countries)
captured:        per query: HTTP, card count; cards whose title names advertising, agentic, commerce, checkout, conversational or an assistant (title | location | posted | URL); job-page fields for five postings
```

## Search results — every query returned HTTP 200 and a full first page of 10 cards

| Country | Query | Cards | Title-relevant cards (advertising, agentic, commerce, checkout, conversational, assistant) |
|---|---|---|---|
| United Kingdom | "ChatGPT ads" | 10 | Generative AI Engineer — McCabe Barton, London, 2026-09-10; Agentic Marketing Specialist, AI, Google Ads — Google, London, 2026-09-16 (uk.linkedin.com/jobs/view/agentic-marketing-specialist-ai-google-ads-at-google-4466886688) |
| United Kingdom | "AI ads" | 10 | none (AI-engineering, safety and data roles) |
| United Kingdom | "sponsored answers" | 10 | none |
| United Kingdom | "agentic commerce" | 10 | Head of Engineering (Agentic AI Systems) — ASOS.com, London, 2026-09-11 (…/head-of-engineering-agentic-ai-systems-at-asos-com-4463988880) |
| United Kingdom | "Instant Checkout" | 10 | none |
| United Kingdom | "agentic checkout" | 10 | none |
| France | "ChatGPT ads" | 10 | Développeur de prompt - Copilot / Power Automate — IT Mates, Paris, 2026-08-26 |
| France | "AI ads" | 10 | none |
| France | "sponsored answers" | 10 | none |
| France | "agentic commerce" | 10 | none |
| France | "Instant Checkout" | 10 | Account Executive, Enterprise (Card-Linked, intermediate level) — Joko, Paris, 2026-06-03 |
| France | "agentic checkout" | 10 | none |
| France | "commerce agentique" | 10 | Commercial e-commerce Italie – Vente & Conseil à distance — Arcane Industries, Aubagne, 2026-09-14; Compte Clé/KAM E-Commerce — Castel Frères, Thiais, 2026-09-09; Chargé développement Marketplace F/H — Auchan Retail, Villeneuve-d'Ascq, 2026-06-26 |
| France | "publicité IA" | 10 | none |
| Spain | "ChatGPT ads" | 10 | Consultor/a Senior Microsoft AI – Copilot & Copilot Studio — Arelance, Madrid, 2026-09-18; Agentic AI Engineer — MANGO, Palau-solità i Plegamans, 2026-09-22; Senior AI Data Scientist, Agentic Automation (Marketing) — team.blue, Barcelona, 2026-09-05 |
| Spain | "AI ads" | 10 | Senior AI Data Scientist, Agentic Automation (Marketing) — team.blue, Barcelona, 2026-09-05 |
| Spain | "sponsored answers" | 10 | none |
| Spain | "agentic commerce" | 10 | Agentic AI Engineer — MANGO, 2026-09-22; Agentic Commerce & AI Lead - Consumer Goods and Retail (Song) — Accenture España, Madrid, 2026-09-18 (es.linkedin.com/jobs/view/agentic-commerce-ai-lead-consumer-goods-and-retail-song-at-accenture-españa-4440283641); Data & AI Architect Agentic Commerce — Accenture España, Barcelona, 2026-09-18 (…-4443891408) |
| Spain | "Instant Checkout" | 10 | none |
| Spain | "agentic checkout" | 10 | CFO de Transformación (Sector E-commerce) — ATAA, Águilas, 2026-09-09 |
| Spain | "comercio agéntico" | 10 | none |
| Spain | "publicidad en IA" | 10 | Creative AI Specialist — Generative Media & Automation — Naiian, Madrid, 2026-09-18; Senior Generative AI Engineer — IQVIA, Madrid, 2026-08-07; Digital Growth & GEO Consultant \| WeAI — Jungle, Barcelona, 2026-09-16 |
| Italy | "ChatGPT ads" | 10 | Senior AI Data Scientist, Agentic Automation (Marketing) — team.blue, Florence, 2026-09-05; AI Software Engineer (GenAI, Virtual Agent, MS Copilot) — Avanade, Milan, 2026-09-03; Conversational Designer – AI & Customer Experience — See True Partners, Milan, 2026-09-23; Experienced – Agentic GenAI & Hyper-Automation Developer — Deloitte, Rome and Milan, 2026-09-22 |
| Italy | "AI ads" | 10 | Senior AI Data Scientist, Agentic Automation (Marketing) — team.blue, Florence, 2026-09-05 |
| Italy | "sponsored answers" | 10 | none |
| Italy | "agentic commerce" | 10 | none |
| Italy | "Instant Checkout" | 10 | none |
| Italy | "agentic checkout" | 10 | Generative AI & Copilot Specialist — Adecco, Rome, 2026-09-22; Junior AI / LLM Engineer – RAG & AI Agents — agap2 Italia, 2026-09-15 |
| Italy | "commercio agentico" | 10 | none |
| Italy | "pubblicità IA" | 10 | AI Software Engineer (GenAI, Virtual Agent, MS Copilot) — Avanade, Milan, 2026-09-03; Experienced Professional \| Generative AI Developer (J-Science) — Jakala, Milan, 2026-09-01 |
| Netherlands | "ChatGPT ads" | 10 | GenAI Specialist AI Commerce — Zonneplan, Zwolle, 2026-09-14 (nl.linkedin.com/jobs/view/genai-specialist-ai-commerce-at-zonneplan-4423938094); Conversational AI Specialist — Winparts, Groningen, 2026-09-04 |
| Netherlands | "AI ads" | 10 | Staff ML Engineer - Advertising — eBay, Amsterdam, 2026-09-11; Director Applied AI for Marketing and Commerce — Artefact, Utrecht, 2026-09-20; Senior Product Manager, Agentic AI Ad Solutions — Seedtag, Amsterdam Area, 2026-09-09 (…/senior-product-manager-agentic-ai-ad-solutions-at-seedtag-4446325005) |
| Netherlands | "sponsored answers" | 10 | none |
| Netherlands | "agentic commerce" | 10 | Staff AI Engineer - Agentic Shopping — Picnic Technologies, Amsterdam, 2026-09-04 (nl.linkedin.com/jobs/view/staff-ai-engineer-agentic-shopping-at-picnic-technologies-4463610105) |
| Netherlands | "Instant Checkout" | 10 | E-commerce & CRO specialist — Matt Sleeps, Amsterdam, 2026-05-29 |
| Netherlands | "agentic checkout" | 10 | Delivery Director – Shopify Plus & eCommerce, Netherlands, Remote-first, €80,000–€90,000 + Bonus + Car Allowance — Areti Group B Corp, 2026-09-04 |
| Netherlands | "agentic commerce" checkout | 10 | Picnic (above); Areti Group (above) |
| Netherlands | "AI advertenties" | 10 | Artefact, eBay, Seedtag (above) |

Every other card on the 38 pages carried an AI-engineering, data, Microsoft-Copilot-developer, sales or unrelated title.

## Job pages — five postings opened

```
4463610105 | Staff AI Engineer - Agentic Shopping | Picnic Technologies | posted "2 weeks ago" | 103 applicants | Not Applicable · Full-time · Engineering and Information Technology · Retail
  "Technical leadership & vision: As a Staff AI Engineer, you will be the hands-on technical lead for Agentic Shopping."
  "Build Picnic's shopping assistant: Lead the technical direction for agentic shopping experiences that help millions of people plan and shop effortlessly."
  "Lead the system architecture for multi-turn conversational agents, balancing latency, safety guardrails, and inference costs."
  "Design and implement systems architectures for multi-turn, conversational agents using open-weight models and techniques like fine-tuning, distillation, and RAG."
4463988880 | Head of Engineering (Agentic AI Systems) | ASOS.com | posted "1 week ago" | "Be among the first 25 applicants" | Mid-Senior level · Full-time · Information Technology · Retail
  "defining how AI agents augment teams, accelerate decision-making, and unlock entirely new ways of working."
  "Establish and embed best practices for agentic systems, AI workflows, LLM integrations, and AI-enabled tooling"
4315855270 | Agentic AI Engineer | MANGO | posted "17 hours ago" | "Over 200 applicants" | Not Applicable · Full-time · Engineering and Information Technology · Retail Apparel and Fashion
  "Implementar y mantener pipelines de observabilidad y evaluación de LLMs para medir y mejorar la calidad de las respuestas … detección y enmascaramiento de PII en conversaciones, gestión segura de secretos y cumplimiento con GDPR."
4423938094 | GenAI Specialist AI Commerce | Zonneplan | posted "1 week ago" | 68 applicants | Not Applicable · Full-time · Other · Energy Technology
  "Je hebt enkele jaren ervaring waarin je zelf prompts, agent-flows en conversational interfaces hebt gebouwd en in productie gezet"
  "Je AI-werk heeft aantoonbaar iets verkocht of geconverteerd: autonome verkoop, conversational commerce of AI-gedreven funnels."
4446325005 | Senior Product Manager, Agentic AI Ad Solutions | Seedtag | posted "1 week ago" | "Over 200 applicants" | Not Applicable · Full-time · Product Management and Marketing · Advertising Services
  "Seedtag is the leading Neuro-Contextual Advertising Company."
  "Define and own the roadmap for AI-powered advertising applications, with a focus on agentic systems that automate and optimise advertiser workflows."
```

[note: none of the five descriptions names ChatGPT, Gemini, Copilot or Perplexity as a sales or advertising surface, Instant Checkout, ACP or UCP; "agentic" in each refers to the employer's own assistant or internal tooling. Company headcount is not a field on the guest job page.]

## Pull notes — mechanical only

- 38 search calls and 5 job-page calls, all HTTP 200. Cards are the first page (10) in LinkedIn's relevance order; every query filled the page, so these pages are not counts.
- The guest search expands every quoted term to token matches: "ChatGPT ads" returns Microsoft Copilot developer roles; "agentic checkout" returns generic agentic-AI roles; "sponsored answers" returned no title containing either word in any country.
- Card employer names were not captured by the card parser (empty field); employers above are read from the job URL slug ("…-at-<employer>-<id>").
