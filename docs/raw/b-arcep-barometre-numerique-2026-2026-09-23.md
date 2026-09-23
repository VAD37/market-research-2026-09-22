# Arcep / Arcom / CGE / ANCT — Baromètre du numérique, édition 2026, infographic: generative-AI usage in France

```yaml
source:          Arcep (Autorité de régulation des communications électroniques, des postes et de la distribution de la presse), with Arcom, CGE and ANCT; survey conducted by Crédoc
url_or_doc_id:   https://www.arcep.fr/uploads/tx_gspublication/barometre-du-numerique-edition-2026_INFOGRAPHIE.pdf (linked from https://www.arcep.fr/cartes-et-donnees/nos-publications-chiffrees/barometre-du-numerique/le-barometre-du-numerique.html)
published:       édition 2026; fieldwork "du 5 au 21 juin 2025" per the PDF header
pull_date:       2026-09-23
pull_method:     fetch (curl) of the PDF; text extracted with pdftotext -layout; the PDF itself saved as a data image
pull_purpose:    evidence about a number
tier:            4
tier_reason:     regulator-commissioned representative survey with n, dates and sampling stated on the document (Crédoc for Arcep); treated as a panel/survey with method published (table default 4), not as a filing
source_label:    analyst-derived
lane:            B
sub_market:      n/a
engine:          ChatGPT ("Chat GPT" as printed), Gemini, "Autres IA"
metric_kind:     visibility
supersedes:      none
captured:        section "Intelligence artificielle générative — Usages et parties prenantes" of the infographic, verbatim as extracted; layout is a two-column infographic so extracted lines interleave — the PDF image is the authority
```

[image: docs/raw/img/b-arcep-barometre-numerique-2026-2026-09-23/01-barometre-du-numerique-edition-2026-infographie.pdf]

## Verbatim — header

> "Baromètre du numérique — Équipements et usages — édition 2026"
> "Le baromètre du numérique est une étude réalisée par le Crédoc pour l'Arcep, l'Arcom, le CGE et l'ANCT auprès d'un échantillon représentatif de la population française âgée de 12 ans et plus (3 544 personnes interrogées en ligne, dont 201 jeunes de 12 à 17 ans, et 601 personnes de 18 ans et plus « éloignées du numérique » interrogées par téléphone). Au total, 4 145 personnes ont été interrogées du 5 au 21 juin 2025."

## Verbatim — generative-AI panel (pdftotext -layout, lines as extracted; column interleaving preserved)

```
Intelligence                       Une explosion          2025                       48 %
artificielle                       massive des usages
générative                         dans la population     2024       33 %                                     85 %
Usages et                          notamment chez         2023 20 %                                           chez les
parties prenantes                  les jeunes adultes.                                                        18-24 ans
 34 %                               Usage quotidien       Chat GPT
                                   d'IA générative par
     des utilisateurs d'IA                                très nettement en tête des IA les plus
     générative l'utilisent           tranche d'âge       utilisées, loin devant Gemini (2e).
     au quotidien.
                                   26 %  12-17 ans            24 %                                            63 %
 51 %                              51 %  18-24 ans
                                   46 %  25-39 ans        Autres IA                                           Chat GPT
     des utilisateurs              27 %  40-59 ans
     recourent à plusieurs         17 %                       13 %
     IA génératives.                      > 60 ans
                                                             Gemini
Des usages multiples, motivés par l'efficacité                                             Raisons d'utilisation
Les utilisateurs souhaitent gagner du temps, quitte à ne                                        41 %
pas systématiquement vérifier l'information.
                                                                                               Gain de temps
Recherche d'information                  73 %                                                  et productivité
Traduction et                      58 %                   64 %                                  33 %
améliorations de texte
                                                          vérifient souvent,                   Ergonomie et
Trouver de nouvelles idées         57 %                   voire toujours,                      fonctionnalité
                                                          les informations
                                                          fournies par l'IA.
Aides aux devoirs            44 %                         Systématiquement
et apprentissages                                                              21 %
Création de contenus 42 %                                 Souvent
Discussions et               41 %                                  43 %
interactions avec l'IA
```

[note: read against the PDF layout, the panel pairs as follows — generative-AI use in the population: 2023 20 %, 2024 33 %, 2025 48 %; 85 % among 18-24-year-olds; 34 % of generative-AI users use it daily; 51 % use several generative AIs; daily use by age band 26 % (12-17), 51 % (18-24), 46 % (25-39), 27 % (40-59), 17 % (> 60); most-used AI: "Chat GPT" 63 %, "Autres IA" 24 %, Gemini 13 %; uses: information search 73 %, translation and text improvement 58 %, new ideas 57 %, homework and learning 44 %, content creation 42 %, discussions with the AI 41 %; 64 % verify the AI's information often or always (21 % systematically, 43 % often); reasons: time saving and productivity 41 %, ergonomics and functionality 33 %. This pairing is the extractor's reading of the layout and is recorded here as a note, not as source text.]

## Pull notes — mechanical only

- The Arcep landing page (HTTP 200, 62 KB) links the édition 2026 infographic PDF; the full édition 2026 report PDF was not linked on that page's fetched HTML (only the 2022 report PDFs and a 2025 institutional brochure were), and was not searched further.
- PDF HTTP 200, 725,161 bytes; text layer present (no OCR needed). Percent signs and accents rendered correctly by pdftotext; the layout interleaving above is the extractor's, not the document's.
- Other panels of the infographic (equipment, connectivity: "94 % / 84 % / 78 % / 61 %" access lines) were not captured.
