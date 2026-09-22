# Census — Pass 4 second sweep, cluster P4-c12: EU-brand sweep, set X aliases

```yaml
task_id:         P4-c12
pull_date:       2026-09-22
pull_method:     fetch (curl, direct) plus one WebFetch-tool fallback where curl returned HTTP 403
scope:           EU brands, retailers, agencies, or vendors publishing a result about AI-assistant visibility, AI referral traffic, or AI-attributed sales, in German, French, Dutch, Spanish, Italian, or English, on EU outlets, as of 2026-09-22
lane:            E, F
moves:           H3, H6, H10, H11
```

No interpretation below beyond what grading rule 1 requires (matching a page's own disclosure against the seven-item bar). Every figure is the source's own, quoted in its raw file.

## Discovery log — outlets, queries, screened counts

**Access note.** WebSearch budget was exhausted for this session (per this task's brief and `STATE.md`). Every query below ran either as a channel's own native search box (found by inspecting its search form, not guessed) or as `lite.duckduckgo.com/lite/` with a `kl=<region>-<region>` parameter, per this task's browser boundary — no Chrome extension, no Playwright.

| Outlet (channel) | Language | Method | Query / page | Screened (title-level hits) | Opened |
|---|---|---|---|---|---|
| t3n.de (C64) | German | native search (`t3n.de/suche/?q=`) | `KI-Sichtbarkeit` | 10 | 0 |
| t3n.de (C64) | German | native search | `Werbung in ChatGPT` | 10 | 0 |
| onlinemarketing.de (C64) | German | native search (`?s=`) | `KI-Sichtbarkeit` | 10 | 0 |
| onlinemarketing.de (C64) | German | DDG lite, `kl=de-de` | `site:onlinemarketing.de Fallstudie KI-Sichtbarkeit` | 0 | 0 |
| onlinemarketing.de + t3n.de (C64) | German | DDG lite, `kl=de-de` | `site:t3n.de Fallstudie KI-Sichtbarkeit Marke` | 6 (partial view, tool truncated) | 0 |
| onlinemarketing.de (C64) | German | direct fetch | `welche-quellen-chatgpt-google-perplexity-zitieren-studie` (found via own search) | 1 | 1 (blinq/AI-citation-sources vendor study — no single-brand claim; not filed) |
| horizont.net (C64) | German | native search (`horizont.net/suche/?i_q=`, form field discovered by inspecting the page markup) | `KI-Sichtbarkeit` (764 total hits claimed; first page, date-sorted, screened) | 9 | 0 |
| horizont.net (C64) | German | DDG lite, `kl=de-de` | `site:horizont.net KI-Sichtbarkeit` | 5 | 0 |
| horizont.net (C64) | German | DDG lite, `kl=de-de` | `site:horizont.net Fallstudie Marke KI-Sichtbarkeit` | 7 (all Yext/Ipsos/Roland Berger vendor consumer-survey pieces, no single-brand result) | 0 |
| wuv.de (C64) | German | DDG lite, `kl=de-de` (native search form not found on the homepage) | `site:wuv.de KI-Sichtbarkeit` | 8 | 3 — all three paywalled past a 2–4-paragraph teaser: E.ON interview, Seowerk/Niko Steeb interview (both filed), and a Reddit-and-AI-citations piece (checked, same paywall pattern, not separately filed) |
| wuv.de (C64) | German | DDG lite, `kl=de-de` | `site:wuv.de "generative engine optimization" OR GEO Marke` | 0 | 0 |
| omr.com / OMR Reviews (C65) | German | direct fetch, category page | `omr.com/de/reviews/category/ai` | 2 ContentHub links surfaced directly | 0 (led to further queries below) |
| omr.com (C65) | German | DDG lite, `kl=de-de` | `site:omr.com Praxisfall KI-Sichtbarkeit` | 10 | 4 (sixclicks/Albrink, "Von Traffic zur KI-Shortlist" [rapidmail/Brevo], "AI Visibility messen" [sponsored, no brand claim, not filed], PR interview with Laurent Bussmann) |
| — (German, cross-outlet) | German | DDG lite, `kl=de-de` | `Hautpflege OR Kosmetik "KI-Sichtbarkeit" OR GEO Fallstudie Marke` | 7 | 0 (all generic GEO-tool/vendor pages, no EU skincare-brand case) |
| — (German, cross-outlet) | German | DDG lite, `kl=de-de` | `Beautymarke ChatGPT Empfehlung Sichtbarkeit Studie` | 10 | 1 (etailment.de / Estée Lauder — no metric, filed as screened-no-claim) |
| etailment.de (German retail trade press, not on C64/C65 but surfaced by the query above) | German | direct fetch | Estée Lauder / Profound GEO partnership | — | 1 (filed) |
| claneo.com (Berlin Digital PR agency, surfaced via the OMR PR interview) | English (site's `/en/` path fetched) | direct fetch, case-studies index + 2 individual pages | Case-studies index (18 named EU clients: MediaMarktSaturn, Bosch Power Tools, HelloFresh ×3, toom Baumarkt, BLACKROLL, Coop Bau+Hobby, Henkel Adhesive Technologies, Pattex, Doctolib, Lieferando, Jungheinrich PROFISHOP, SOLARWATT, hundemagazin.com) | 18 | 2 (MediaMarktSaturn, Doctolib) — **both off-topic**: traditional Digital-PR media-clippings case studies (print/online clippings counts), zero mention of ChatGPT, GEO, AI Overviews, or any LLM anywhere on either page; screened out as wrong subject matter, not graded, not filed as raw cases |
| rankscale.ai (Vienna, Austria — EU AI-visibility vendor, English-language site) | English | direct fetch, case-studies index + individual pages | 7 case studies total, 6 industries | 7 | 3 new (Spanish Bank, MiniFinder/Germany, European Public-Sector Pilot — all filed); 2 already pulled by cluster P4-c4 per `STATE.md` (Austrian optical retailer, AI SMS platform — not re-pulled, filename-glob collision avoided); 2 non-EU on their face (US online grocer, unstated-country SoWork) not opened |
| eu-startups.com | English | native search (`?s=`) | `AI visibility` | 10 | 0 — all hits are vendor funding-round announcements (Searchable, Peec AI, others already in the Pass-3 roster), no brand-side AI-visibility result |
| sifted.eu | English | native search (`?s=`) | `AI search visibility` | `unknown — checked sifted.eu 2026-09-22` | 0 — search results are client-side-rendered; the fetched HTML returns only the homepage shell (confirmed: page title, nav, and homepage article list only, no search-result markup); added to browser backlog |
| uclic.fr (French growth-marketing agency, EU outlet) | French | DDG lite, `kl=fr-fr` | `"trafic IA" ChatGPT marque étude de cas` | 2 | 1 (filed — aggregates non-EU figures, no named EU brand) |
| — (French, cross-outlet) | French | DDG lite, `kl=fr-fr` | `"cas client" "visibilité IA" marque résultats` | 0 | 0 |
| quotative.com (French AI-visibility vendor, EU) | French | DDG lite, `kl=fr-fr` → direct fetch | `"visibilité IA" caso studio marchio` region query surfaced `barometre-cosmetique-ia-2026` (29 French cosmetic brands audited, avg. score 37/100, April 2026) | 1 | attempted, not opened — site is a client-side-rendered SPA; direct fetch returns only the homepage shell (`364+ marques`, `90,8%`, `30,7/100` stats), not the blog article body; added to browser backlog |
| see-geo.com (French-language GEO vendor) | French | DDG lite, `kl=fr-fr` | `cosmétique OR beauté "visibilité IA" cas client résultats` | 2 | 1 (filed — 7-case roundup, all non-EU or unnamed subjects) |
| marketing4ecommerce.net (Spanish e-commerce trade press, EU) | Spanish | DDG lite, `kl=es-es` | `"visibilidad en IA" caso de estudio marca resultados` | 6 | 1 (filed — Semrush AI Visibility Index relay, no EU brand named; direct `curl` 403, resolved via WebFetch tool) |
| — (Spanish, cross-outlet) | Spanish | (same query as above) | other 5 hits: amicited.com (Apple/McKinsey benchmarks — no EU brand), ilifebelt.com (Semrush relay, Central-American outlet, not EU), surfeo.ai (aggregate 1,066-business audit, no single brand named), aurametrics.io (benchmark tool page, no case), surmado.com (El Tianguis restaurant, US, San Diego) | 5 | 0 — none names an EU brand |
| — (Italian, cross-outlet) | Italian | DDG lite, `kl=it-it` | `"visibilità IA" caso studio marchio risultati` | 8 | 0 — every hit is a generic AI-visibility-checker/tool product page (ailabsaudit.com, twaino.com, Adobe Experience League, elfsight.it, squarespace, diagnoseo.com, rankfender.com ×2); none is a named-brand case |
| — (Dutch, cross-outlet) | Dutch | DDG lite, `kl=nl-nl` | `"AI zichtbaarheid" merk case resultaten` | 0 | 0 — "No results found" |
| DAX/CAC/AEX consumer, beauty, SaaS, insurance filers' own IR pages | — | not run this session | — | `unknown — checked DAX/CAC/AEX issuer IR pages 2026-09-22` | 0 — given the number of possible filers (dozens across three indices × four sectors) and the session's remaining budget, no individual issuer IR/newsroom page was fetched directly; the one large-cap EU-market brand result found (Estée Lauder/Profound) came via German trade press, not via the brand's own IR page |

## Candidate table — every case opened

| Source | Language | Country (brand's market) | Vertical | Type | Date | Engine(s) | Metric | Figure (verbatim) | Direction | Grade — missing items | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OMR Reviews — Sascha Albrink/sixclicks | German | Germany | none named | company-stated (PR/GEO campaign) | 2026-08-24 | Google AI Overviews, ChatGPT, Perplexity | visibility | "68 Prozent Share of Voice ... Position 1,06"; "24 gegenüber 11 Prozent"; "6 von 8 Prompts"; "48 / 38 Citations" | up | **Bronze** — missing 3 (no absolute date window), 4 (no baseline) | `e-case-c12-omr-sixclicks-albrink-2026-09-22.md` |
| OMR Reviews — own "Rapidmail vs. Mailchimp" article | German | Germany | B2B SaaS | vendor-reported | 2026-03-01 (article); Oct 2025 (compared piece) | not named for this figure | visibility | "120 Citations"; "Platz 3 im gesamten Set" | up | **Bronze** — missing 2 (no engine), 4 (no baseline) | `e-case-c12-omr-rapidmail-brevo-2026-09-22.md` |
| Rankscale — Spanish bank | English | Spain | high-CPA regulated | vendor-reported | undated | "major AI engines" (unnamed) | visibility | "+180% Visibility Increase"; "+215% Top-3 Ranking Growth"; "#1 Share of Voice" | up | **Bronze** — missing 2 (no engine), 3 (no date), 4 (no baseline value) | `e-case-c12-rankscale-spanish-bank-2026-09-22.md` |
| Rankscale — MiniFinder (German market) | English | Germany (client HQ: Sweden) | none named | vendor-reported | "90 days"; May 2026 (traffic figure only) | ChatGPT, Google AI Overview, Copilot, Perplexity, Gemini | visibility, traffic | "36.2% AI Visibility (from 2.4% baseline)"; "25.6% Share of Citations"; "+36.2% Organic traffic MoM" | up | **Bronze** — missing 3 (no absolute date window), full 7 (no paid-by-outcome) | `e-case-c12-rankscale-minifinder-germany-2026-09-22.md` |
| Rankscale — European public-sector pilot | English | unstated (EU, no member state named) | none named | vendor-reported | undated | "major answer engines" (unnamed) | none | no figure of any kind | n/a | **screened — no claim** | `e-case-c12-rankscale-eu-publicsector-2026-09-22.md` |
| etailment.de — Estée Lauder/Profound | German | global ("weltweit"); trade-press outlet is German | skincare and beauty | company-stated | 2026-09-17 | ChatGPT, Gemini (named as examples only) | none | no figure of any kind | n/a | **screened — no claim** | `e-case-c12-etailment-estee-lauder-2026-09-22.md` |
| OMR Education — PR interview, Bussmann/Claneo | German | Germany | none named | company-stated (advice interview) | 2026-08-16 | Google AI Overviews (named generically) | none | "über 60 Prozent aller Google-Suchen enden ohne Klick" (category-level, no brand, no source) | n/a | **screened — no claim** | `e-case-c12-omr-pr-interview-bussmann-2026-09-22.md` |
| Uclic (uclic.fr) — "Trafic IA vs Google" | French | France (agency); cited data is US | none named | vendor-reported (secondary aggregation) | 2026-06-04 | ChatGPT (headline); Claude/Gemini/Perplexity (B2B share only) | traffic | "1,81 % ... contre 1,39 %"; "+31 %"; one named non-EU case (Seer Interactive, 16% vs 1.8%) | up | **screened — no EU brand named** | `e-case-c12-uclic-trafic-ia-2026-09-22.md` |
| marketing4ecommerce.net — Semrush AI Visibility Index | Spanish | Spain (outlet); brands are all US | none named | vendor-reported (relayed) | 2025-10-09 (stale) | ChatGPT, Google AI Mode | visibility | per-brand % (Microsoft 52.9%, Samsung 58.1%, Patagonia 21.9%, etc.) | mixed | **screened — no EU brand named** | `e-case-c12-m4e-semrush-index-2026-09-22.md` |
| SeeGeo — "7 cas réels de visibilité IA" | French | outlet unconfirmed; all 7 subjects US or unnamed | none named | vendor-reported (secondary aggregation, self-declared self-reported) | 2026-08-13 | Google AI Overviews, ChatGPT | visibility, traffic, sales | 7 cases, e.g. "+540% mentions", "+4 900% de revenus", "32% des leads" | up | **screened — no EU brand named** | `e-case-c12-seegeo-sept-cas-2026-09-22.md` |
| W&V (wuv.de) — E.ON interview | German | Germany | none named | company-stated | 2026-01-26 | unstated (paywalled) | none | teaser carries no figure | n/a | **screened — not opened** (paywall) | `e-case-c12-wuv-eon-2026-09-22.md` |
| W&V (wuv.de) — Seowerk/Niko Steeb interview | German | Germany | none named | company-stated | 2026-07-22 | unstated (paywalled) | none | teaser carries no figure | n/a | **screened — not opened** (paywall) | `e-case-c12-wuv-seowerk-2026-09-22.md` |

## Screened-out list — opened but not filed as a separate raw case

- OMR Reviews, "AI Visibility messen – so steigerst du den Share of Voice" (`omr.com/de/education/articles/ai-visibility-messen-share-of-voice-chatgpt`, sponsored/PIA Media, 2026-03-31): opened in full, educational content only, no brand-specific metric anywhere on the page — same disposition as the filed no-claim cases, not filed separately to hold the file count to a representative set.
- onlinemarketing.de, "Diese Websites zitieren ChatGPT und Co. am häufigsten" (blinq study, 250,000 AI answers analysed Jan–Jun 2026): opened in full — a category-level citation-source study (YouTube, Reddit, Wikipedia, news domains), not a single EU brand's own result; not filed.
- Claneo case-studies index (18 named EU clients) plus 2 opened pages (MediaMarktSaturn, Doctolib): both off-topic — traditional Digital-PR media-clippings metrics (71 print/online clippings for MediaMarktSaturn), zero AI-assistant-visibility content; not filed. The remaining 16 listed clients were not opened individually given this pattern.
- Rankscale case-studies index: "Online Grocer" (US, 15 metros) and "SoWork" (virtual-office SaaS, country unstated) — index descriptions gave no EU signal; not opened.
- EU-Startups (10 funding-round hits: Searchable €11.9M, Peec AI €18M, and others) — all vendor-funding announcements, no brand-side AI-visibility result; consistent with the Pass-3 vendor roster, not opened individually.

## Browser backlog

URLs that need the Chrome extension or Playwright (out of scope for this fetch-only task) to render:

1. `quotative.com/blog/barometre-cosmetique-ia-2026` — client-side-rendered SPA; the one hard number found ("29 marques auditées en avril 2026, score moyen 37/100") comes only from the DuckDuckGo search snippet, not from an opened page, and per grading rule 1 is therefore **not** treated as opened or graded above.
2. `sifted.eu/?s=AI+search+visibility` — client-side-rendered search results; fetched HTML returns the homepage shell only.

## Counts — per language

| Language | Screened (title-level) | Opened | Graded (Bronze-or-better attempted) | Cleared (Bronze or better) |
|---|---|---|---|---|
| German | ~116 (t3n 20, onlinemarketing.de ~17, horizont.net 21, wuv.de 8, OMR-adjacent 19, beauty/skincare queries 17, Claneo index 18 — rows counted per query, not fully deduplicated across overlapping queries) | 10 | 4 | 2 (sixclicks/Albrink, rapidmail/Brevo — both Bronze) |
| English (EU vendors/outlets: Rankscale, EU-Startups, Sifted) | 17 (Rankscale 7, EU-Startups 10) + Sifted `unknown — checked` | 10 (Rankscale 7 case-study pages read across the index screening, 3 filed as new + 2 already covered + 2 screened-out on index text; EU-Startups 10 titles screened at snippet level, 0 opened) | 2 (Rankscale Spanish Bank, MiniFinder) | 2 (both Bronze) |
| French | 4 (uclic 2, beauty query 2) | 2 (uclic, see-geo) + 1 attempted-blocked (quotative) | 0 | 0 |
| Spanish | 6 | 1 (marketing4ecommerce.net) | 0 | 0 |
| Italian | 8 | 0 | 0 | 0 |
| Dutch | 0 (no results returned) | 0 | 0 | 0 |

Total distinct cases opened and filed as raw/ pulls this cluster: **12**. Graded under rule 1: **4**, all Bronze. Screened — no claim: **3**. Screened — no EU brand named: **3**. Screened — not opened (paywall): **2**.

## Counts — per vertical

| Vertical | Screened (among opened cases) | Opened | Graded | Cleared (Bronze or better) |
|---|---|---|---|---|
| Skincare and beauty | 1 (etailment/Estée Lauder) | 1 | 1 (no-claim, not gradeable past intake) | 0 |
| B2B SaaS | 1 (OMR/rapidmail-Brevo) | 1 | 1 | 1 (Bronze) |
| High-CPA regulated | 1 (Rankscale/Spanish bank) | 1 | 1 | 1 (Bronze) |
| None named (outside the three programme verticals) | 9 | 9 | 2 | 2 (Bronze — sixclicks/Albrink, MiniFinder) |

No Silver, Gold, or Fools-gold case was found in this cluster. All four graded cases are Bronze under grading rule 1: each carries at least one missing bar item (most commonly item 3, an absolute date window, and item 4, a numeric baseline), and none crosses from visibility into a disclosed, baselined revenue or sales figure.

## Unknowns

- `unknown — checked sifted.eu 2026-09-22` — search results are client-side-rendered; no brand-side AI-visibility case confirmed present or absent.
- `unknown — checked quotative.com/blog/barometre-cosmetique-ia-2026 2026-09-22` — client-side-rendered; the "29 marques françaises, score moyen 37/100" figure is known only from a search snippet, not from an opened page.
- `unknown — checked DAX/CAC/AEX issuer IR/newsroom pages 2026-09-22` — no individual large-cap issuer's own IR or newsroom page was fetched this session; the only large-cap brand result found (Estée Lauder/Profound) came via German trade press (etailment.de), not via the brand's own IR page, and Estée Lauder itself is US-headquartered, not an EU issuer.
- `unknown — checked horizont.net beyond its first search-results page 2026-09-22` — the site's own search reports 764 total hits for "KI-Sichtbarkeit"; only the first page (9 results, date-sorted) plus two DuckDuckGo-routed queries (12 more) were screened. The remainder is unscreened.
- `unknown — checked Dutch-language EU outlets by name 2026-09-22` — no Dutch equivalent of C64/C65 is named in `channels.md`; the one Dutch-language open-web query run returned zero results, and no Dutch trade-press domain (e.g., Emerce, Marketingfacts) was queried directly by name.
- `unknown — checked Italian-language EU trade press by name 2026-09-22` — no Italian equivalent of C64/C65 is named in `channels.md`; the one Italian-language open-web query returned only generic AI-visibility-checker tool pages, no named-brand case; no Italian trade-press domain was queried directly by name.

## Caveats

- Set X (`query-book.md` amendment 4) covers German, French and Spanish only; Dutch and Italian aliases used above were constructed for this task from the same English seed terms (translation only, not carried into `query-book.md`) since the task brief named all five non-English languages plus English. No brand or figure below was recalled from memory; every item traces to a URL fetched today, listed in its own raw file.
- Every graded case in this cluster is Bronze; none discloses all seven bar items. The two Rankscale cases (Spanish bank, MiniFinder) are vendor-authored case studies published by the AI-visibility tool being sold (Rankscale GmbH, Vienna) with no independent replication — flagged per trust-rubric.md "vendor measuring the thing it sells" in each file's `tier_reason`.
- The three "screened — no EU brand named" cases (Uclic, marketing4ecommerce.net, SeeGeo) all carry real numeric claims and were opened in full, but attach only to non-EU companies or unnamed/unconfirmed subjects; they are filed here as evidence of category noise and of the search surface's own bias toward US-sourced figures even on EU-outlet pages, per `pull_purpose: evidence about category noise`.
- wuv.de (one of the four required C64 outlets) was paywalled on every one of the three articles opened this session past a short teaser; this is recorded as a channel-level finding (not re-tested per article) and flagged to the browser backlog only in the sense that a login credential, not a rendering engine, is what would unblock it — no browser tool would help without a subscription.
- Survivorship and thin-market caveats from `plan.md` apply here as everywhere: the category's published EU-brand cases are, by construction, self-selected winners, and this sweep's screened-to-cleared ratio (12 opened, 4 cleared, all Bronze) is itself the finding, not a shortfall to be explained away.
