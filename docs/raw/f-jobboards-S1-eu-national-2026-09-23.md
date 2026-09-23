# National job boards and software directories — S1 / S2 access checks: UK, FR, ES, IT, NL

```yaml
source:          reed.co.uk; hellowork.com (FR); infojobs.net (ES); infojobs.it (IT); nationalevacaturebank.nl (NL); capterra.fr; appvizer.fr
url_or_doc_id:   https://www.reed.co.uk/jobs/generative-engine-optimisation-jobs ; https://www.hellowork.com/fr-fr/emploi/recherche.html?k=generative+engine+optimization ; https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=generative%20engine%20optimization ; https://www.infojobs.it/offerte-lavoro/generative-engine-optimization ; https://www.nationalevacaturebank.nl/vacature/zoeken?query=generative%20engine%20optimization ; https://www.capterra.fr/search?q=AI%20visibility ; https://www.appvizer.fr/recherche?q=generative%20engine%20optimization
published:       n/a
pull_date:       2026-09-23
pull_method:     fetch (curl)
pull_purpose:    evidence about a number (S1 count per national board; S2 local-language directory listing)
tier:            3
tier_reason:     board's own result page (platform primary) — only Hellowork returned a server-rendered count; the rest record the wall or an empty render
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP results; Hellowork result count and card titles as served
```

## Verbatim — access results

| Country | Site | HTTP | Bytes | Result |
|---|---|---|---|---|
| UK | reed.co.uk /jobs/generative-engine-optimisation-jobs | 403 | 5,632 | bot wall |
| FR | hellowork.com search `k=generative+engine+optimization` | 200 | 495,577 | server-rendered results; the page normalised the query to "generatif engin optimisation" and states **"18 offres"** ("Afficher 18 offres"); card titles served (first 20 title attributes, in order): "SEO Specialist H/F - Plus que pro", "Senior SEO Spécialist H/F - Plus que pro", "Account Executive - Italian Speaker H/F - Meteoria", "Account Executive - Spanish Speaker H/F - Meteoria", "Responsable de Pôle Digital H/F - Neoma Business School" (×2), "Webmarketeur H/F - GBH", "Account Executive H/F - Meteoria" |
| ES | infojobs.net search-results list.xhtml | 405 | 31,737 | method not allowed on GET without session |
| IT | infojobs.it /offerte-lavoro/… | 200 | 3,948 | page text: "InfoJobs - Grazie Italia — Questa piattaforma è ufficialmente chiusa e non più disponibile." (platform closed) |
| NL | nationalevacaturebank.nl /vacature/zoeken?query=… | 200 | 87,607 | client-rendered (Next.js); no vacancy count or titles in the served HTML |
| FR (S2) | capterra.fr /search?q=AI visibility | 403 | 5,600 | bot wall |
| FR (S2) | appvizer.fr /recherche?q=generative engine optimization | 200 | 102,308 | search shell only (i18n strings incl. "Désolé, aucun résultat ne correspond à votre recherche"); no result cards in the served HTML |

[note: the Hellowork "18 offres" figure is the board's count for its normalised phrase; the served titles are generic SEO, sales and digital roles, so the 18 is not a count of GEO-titled postings. Cards beyond the first 20 title attributes were not parsed.]

## Pull notes — mechanical only

- One request per URL, no retries, no login, no form submission.
- infojobs.it's closure notice is the site's own page text; infojobs.net (Spain) is a separate, live site that refused the GET.
- LinkedIn per-country results for the same terms are in `docs/raw/f-linkedin-S1-eu-countries-2026-09-23.md`.
