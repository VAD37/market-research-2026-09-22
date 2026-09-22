# EU Digital Services Act (Regulation (EU) 2022/2065) — Articles 26, 27, 39

```yaml
source:          EUR-Lex, Official Journal of the European Union
url_or_doc_id:   https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065 (CELEX 32022R2065; ELI http://data.europa.eu/eli/reg/2022/2065/oj)
published:       2022-10-27 (OJ L 277, 27.10.2022)
pull_date:       2026-09-22
pull_method:     browser extension (eur-lex.europa.eu returns HTTP 202 empty body to plain fetch/curl, confirmed on this machine 2026-09-22)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed/binding EU legislative text on eur-lex.europa.eu
source_label:    filed
lane:            B, D
sub_market:      paid placement
engine:          n/a — cross-engine regulatory text
metric_kind:     none
supersedes:      none
captured:        section "Article 26 — Advertising on online platforms" (full); section "Article 27 — Recommender system transparency" (full); section "Article 39 — Additional online advertising transparency" (paragraph 1 full, paragraph 2 opening items (a)-(b), remainder not captured); section "Article 93 — Entry into force and application" (full)
```

## Verbatim

### Article 26

"Article 26

Advertising on online platforms

1.   Providers of online platforms that present advertisements on their online interfaces shall ensure that, for each specific advertisement presented to each individual recipient, the recipients of the service are able to identify, in a clear, concise and unambiguous manner and in real time, the following:

(a) that the information is an advertisement, including through prominent markings, which might follow standards pursuant to Article 44;

(b) the natural or legal person on whose behalf the advertisement is presented;

(c) the natural or legal person who paid for the advertisement if that person is different from the natural or legal person referred to in point (b);

(d) meaningful information directly and easily accessible from the advertisement about the main parameters used to determine the recipient to whom the advertisement is presented and, where applicable, about how to change those parameters.

2.   Providers of online platforms shall provide recipients of the service with a functionality to declare whether the content they provide is or contains commercial communications.

When the recipient of the service submits a declaration pursuant to this paragraph, the provider of online platforms shall ensure that other recipients of the service can identify in a clear and unambiguous manner and in real time, including through prominent markings, which might follow standards pursuant to Article 44, that the content provided by the recipient of the service is or contains commercial communications, as described in that declaration.

3.   Providers of online platforms shall not present advertisements to recipients of the service based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679 using special categories of personal data referred to in Article 9(1) of Regulation (EU) 2016/679."

### Article 27

"Article 27

Recommender system transparency

1.   Providers of online platforms that use recommender systems shall set out in their terms and conditions, in plain and intelligible language, the main parameters used in their recommender systems, as well as any options for the recipients of the service to modify or influence those main parameters.

2.   The main parameters referred to in paragraph 1 shall explain why certain information is suggested to the recipient of the service. They shall include, at least:

(a) the criteria which are most significant in determining the information suggested to the recipient of the service;

(b) the reasons for the relative importance of those parameters.

3.   Where several options are available pursuant to paragraph 1 for recommender systems that determine the relative order of information presented to recipients of the service, providers of online platforms shall also make available a functionality that allows the recipient of the service to select and to modify at any time their preferred option. That functionality shall be directly and easily accessible from the specific section of the online platform's online interface where the information is being prioritised."

### Article 39 (VLOP / VLOSE only — this article sits under Chapter IV of the DSA, the chapter applicable to very large online platforms and very large online search engines)

"Article 39

Additional online advertising transparency

1.   Providers of very large online platforms or of very large online search engines that present advertisements on their online interfaces shall compile and make publicly available in a specific section of their online interface, through a searchable and reliable tool that allows multicriteria queries and through application programming interfaces, a repository containing the information referred to in paragraph 2, for the entire period during which they present an advertisement and until one year after the advertisement was presented for the last time on their online interfaces. They shall ensure that the repository does not contain any personal data of the recipients of the service to whom the advertisement was or could have been presented, and shall make reasonable efforts to ensure that the information is accurate and complete.

2.   The repository shall include at least all of the following information:

(a) the content of the advertisement, including the name of the product, service or brand and the subject matter of the advertisement;

(b) the natural or legal person on whose behalf the advertisement is presented;

[note: paragraph 2 continues with further list items (c) through (g) or more, not captured in this pull — the tool's output-truncation limit was reached mid-list. Not filled from memory.]"

### Article 93 — Entry into force and application

"Article 93

Entry into force and application

1.   This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

2.   This Regulation shall apply from 17 February 2024.

However, Article 24(2), (3) and (6), Article 33(3) to (6), Article 37(7), Article 40(13), Article 43 and Sections 4, 5 and 6 of Chapter IV shall apply from 16 November 2022.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Strasbourg, 19 October 2022."

[note: Articles 26 and 27 sit in DSA Chapter III (obligations for all providers of intermediary services / online platforms), which is not among the Article 93 exceptions — so Articles 26 and 27 apply under the general rule, in force since 2024-02-17, i.e. in force as of this 2026-09-22 pull date. Article 39 sits in Chapter IV (VLOP/VLOSE-specific obligations); Article 93 states "Sections 4, 5 and 6 of Chapter IV" apply from 2022-11-16, but this pull did not independently confirm which numbered Section within Chapter IV contains Article 39, nor whether an individual designated service's Article 39 duty additionally depends on its own designation date under a separate provision (Article 92, not pulled here). Recorded as `unknown — checked eur-lex.europa.eu CELEX:32022R2065 2026-09-22` in the summary file, not asserted either way.]

## Pull notes — mechanical only

- Plain fetch/curl to `eur-lex.europa.eu/eli/reg/2022/2065/oj` and the legal-content TXT/HTML mirror both return HTTP 202 with empty body on this machine (matches `docs/sources/channels.md` C51/C52). Chrome extension used.
- Same extraction method as the AI Act pull in this cluster (`docs/raw/b-eu-regulator-ai-act-2026-09-22.md`): `document.body.textContent` (not `.innerText`, which omitted large sections of this page's markup), located via `indexOf` on a unique title phrase per article, extracted in overlapping ~1000-1100 character windows because the JS-execution tool truncates longer return strings, and joined by hand with visible overlap checked at each seam.
- `document.readyState` read as `loading` partway through this pull despite all searched strings already being present and consistently located across repeated same-tab evaluations for this document (unlike the AI Act `/eli/reg/.../oj` Angular page in the prior pull, this `legal-content/TXT/HTML` mirror gave stable, repeatable `indexOf` results across calls within this session).
- Article 39 paragraph 2's list (c) onward, and any recitals specifically discussing Articles 26, 27 or 39 (e.g. the advertising-transparency and recommender-system recitals in the DSA's preamble), were not pulled in this session — out of time budget for this cluster. Flagged as a gap in the summary file, not filled from memory.
- Did not navigate to `transparency.dsa.ec.europa.eu`, `digital-strategy.ec.europa.eu` designation pages, or any per-service Art. 39 ad repository — those are P2-c10's targets per `docs/sources/shortlist.md`, out of scope for this P2-c9 task. (A P2-c10 agent was observed operating concurrently in the same shared browser tab group during this pull, per shared-browser tab titles seen in tool output; no P2-c10 file was read or written by this task.)
