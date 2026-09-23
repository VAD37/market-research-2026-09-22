# National regulators — Ofcom (UK), CNMC (ES), AGCOM (IT): generative-AI / assistant usage figures, channel checks

```yaml
source:          Ofcom (ofcom.org.uk), CNMC (cnmc.es, data.cnmc.es, blog.cnmc.es), AGCOM (agcom.it) — and web.archive.org for Ofcom
url_or_doc_id:   https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/online-nation ; https://web.archive.org/web/2026/https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/online-nation ; https://www.cnmc.es/prensa ; https://www.cnmc.es/search/node?keys=inteligencia%20artificial%20hogares ; https://data.cnmc.es/ ; https://data.cnmc.es/panel-de-hogares ; https://data.cnmc.es/api/3/action/package_search?q=inteligencia%20artificial ; https://blog.cnmc.es/?s=inteligencia+artificial+generativa ; https://www.agcom.it/ ; https://www.agcom.it/comunicazione/avvisi/rapporto-intelligenza-artificiale-2026 ; https://www.agcom.it/sites/default/files/media/allegato/2026/I%20parte%20-%20ENG.pdf
published:       AGCOM "Rapporto Intelligenza Artificiale 2026" (2026, undated on the notice page); Ofcom and CNMC — no 2025/2026 document reached
pull_date:       2026-09-23
pull_method:     fetch (curl); pdftotext on the AGCOM PDF
pull_purpose:    evidence about a number (result: channel walls and one regulator report without the sought figure)
tier:            3
tier_reason:     regulator's own pages and report (platform-primary equivalent for a public body); the Ofcom and CNMC rows carry no number and only record the wall
source_label:    company-stated
lane:            B
sub_market:      n/a
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        access results per channel; AGCOM notice text excerpt; AGCOM Part I ENG excerpt where it names ChatGPT / Gemini
```

## Ofcom (UK) — access results

| URL | HTTP | Result |
|---|---|---|
| ofcom.org.uk/media-use-and-attitudes/online-habits/online-nation | 403 (5,752 bytes) | bot wall on plain curl |
| ofcom.org.uk/siteassets/.../online-nation/2025/online-nation-2025-report.pdf (guessed path) | 403 | same wall |
| web.archive.org/web/2026id_/…/online-nation (Wayback, capture 2026-09-05) | 200 (137 KB, rendered) | page lists Online Nation PDFs for 2019 and 2020 only in the fetched HTML; no 2025 report link found on the captured page |
| web.archive.org/web/2026/…/online-nation-2025/ and …/online-nation/online-nation-2025 | 404 | "Wayback Machine has not archived that URL" |
| web.archive.org CDX (`url=ofcom.org.uk/*&filter=original:.*online-nation-2025.*`) | connection failed (curl exit, no body) | not retried |
| web.archive.org CDX (`url=ofcom.org.uk/siteassets/*&filter=original:.*online-nation.*`) | 200 | 20 rows, all 2019–2024 assets (2024 report path returned 404 in the archive) |

Ofcom Online Nation 2025 figures: **unknown — checked ofcom.org.uk (403), web.archive.org page capture 2026-09-05 and CDX 2026-09-23.**

## CNMC (ES) — access results

| URL | HTTP | Result |
|---|---|---|
| cnmc.es/prensa | 200 (130 KB) | no line matching "inteligencia artificial", "ChatGPT" or "asistentes" on the press listing page |
| cnmc.es/search/node?keys=inteligencia artificial hogares | 404 | no site search at that path |
| data.cnmc.es | 200 (31 KB) | homepage links "/panel-de-hogares" ("Panel de Hogares … percepciones de los consumidores. Estos datos se obtienen mediante encuestas a hogares e individuos, además de la recogida de facturas.") |
| data.cnmc.es/panel-de-hogares | 200 (22 KB, 373 characters of text after script removal) | client-rendered; no dataset text served |
| data.cnmc.es/api/3/action/package_search?q=inteligencia artificial | 404 | no CKAN API at that path |
| blog.cnmc.es/?s=inteligencia+artificial+generativa | 200 (147 KB) | one result title parsed: "La inteligencia artificial en la industria audiovisual: cinco cifras clave en Europa" — audiovisual industry, not household assistant use |

CNMC Panel de Hogares generative-AI / assistant usage figure: **unknown — checked cnmc.es, data.cnmc.es, blog.cnmc.es 2026-09-23.**

## AGCOM (IT) — access results and excerpt

| URL | HTTP | Result |
|---|---|---|
| agcom.it | 200 (85 KB) | homepage carries a tile "Rapporto Intelligenza Artificiale 2026" linking `/comunicazione/avvisi/rapporto-intelligenza-artificiale-2026` |
| agcom.it/osservatorio-sulle-comunicazioni | 404 | — |
| agcom.it/avvisi/rapporto-intelligenza-artificiale-2026 | 404 | wrong path (the homepage href carries the `/comunicazione` prefix) |
| agcom.it/comunicazione/avvisi/rapporto-intelligenza-artificiale-2026 | 200 (38 KB) | notice page; links four PDFs: "I parte - ITA.pdf", "II parte - ITA.pdf", "I parte - ENG.pdf", "II parte - ENG.pdf" under `/sites/default/files/media/allegato/2026/` |
| …/2026/I parte - ENG.pdf | 200 (2,843,302 bytes; 4,685 text lines) | Part I, "TECHNICAL REPORT OF THE AI OFFICE" |

Notice page, verbatim:
> "La prima parte, curata dall'Ufficio Intelligenza Artificiale di AGCOM, presenta un'analisi tecnico-economica dell'evoluzione dell'IA: dalla sua origine storica fino all'affermazione dei modelli generativi, dei sistemi fondativi e dei Large Language Models."
> "La seconda parte, elaborata dal Comitato sull'Intelligenza Artificiale, sviluppa una riflessione giuridica, regolatoria e istituzionale sulle sfide poste dall'IA nei settori di competenza di AGCOM."

Part I (ENG), lines where ChatGPT or Gemini appear with a figure or Italy (grep "ChatGPT|Gemini" and "ital" with "%|million|users"):
> line 552: "ChatGPT was launched globally on 30 November 2022, making the service accessible to users in Italy from that date."
> lines 2116–2120: "according to the 2026 AI Index, in 2025 the United States accounted for 57.1% of the data centres considered in the figure, compared with 5.6% for Germany and 5.5% for the United Kingdom; for Italy, the share stood at around 1.8%."
> line 3653: "…estimating that a text request made by users to Gemini (the median text…" (energy-per-request passage)

AGCOM Italian assistant user share or engine share: **not found in Part I (ENG) by the greps above; Part II not opened** — `unknown — checked agcom.it Rapporto IA 2026 Part I ENG 2026-09-23`.

## Pull notes — mechanical only

- No login, no form submission, no CAPTCHA attempted on any of the three regulator sites.
- The AGCOM PDF has a text layer; only pattern-matched lines were read, not the full 4,685 lines.
- Eurostat's 2025 survey (separate file `a-eurostat-genai-use-individuals-2025-2026-09-23.md`) carries the Spain and Italy population-level generative-AI use figures that these regulator channels did not yield.
