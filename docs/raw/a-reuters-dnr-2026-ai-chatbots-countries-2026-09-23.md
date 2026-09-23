# Reuters Institute Digital News Report 2026 — "Emerging uses of AI chatbots for news", per-market use and trust (Datawrapper datasets)

```yaml
source:          Reuters Institute for the Study of Journalism, University of Oxford — Digital News Report 2026, chapter "Emerging uses of AI chatbots for news and what it means for journalism"; chart data served by Datawrapper
url_or_doc_id:   https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/emerging-uses-ai-chatbots-news-and-what-it-means-journalism ; datasets https://datawrapper.dwcdn.net/AkjEw/3/dataset.csv , /cN3Fo/1/dataset.csv , /b6TfY/1/dataset.csv , /FYsU9/3/dataset.csv ; methodology https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/methodology ; country pages /digital-news-report/2026/united-kingdom , /france , /spain , /italy , /netherlands
published:       2026 (report year); fieldwork "from the middle of January to the end of February 2026" (methodology page)
pull_date:       2026-09-23
pull_method:     fetch (curl) of the chapter page, the methodology page, five country pages, and the Datawrapper dataset CSV and full.png endpoints embedded in the chapter
pull_purpose:    evidence about a number
tier:            4
tier_reason:     survey panel (YouGov online panel) with published method, sample per market and fieldwork dates on the methodology page — table default for a panel with method disclosed
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          n/a — "AI chatbots" as a class; engines not broken out in the datasets pulled
metric_kind:     visibility
supersedes:      none
captured:        chapter text excerpts; Datawrapper dataset AkjEw in full (48 markets); cN3Fo and b6TfY heads; methodology excerpt; the three chart images
```

## Verbatim — chapter text (excerpts, sentences carrying numbers)

> "…evidence of rising weekly use of AI chatbots for news, up from 7% to 10% globally since last year, driven largely by growth in parts of Asia, Africa, and Latin America, as well as Southern and Eastern Europe – markets where platformisation of news is stronger."

> "The proportion of respondents in the youngest age group using chatbots for news (17%) is three times higher than that in the oldest age group (5%), although the most significant growth relative to 2025 was recorded among those 25–34 (up 4pp)."

> "In a context of already low trust in news (37% of people trust most news most of the time), this year's data show that trust in news from AI chatbots among the general population is lower still at just 20% globally."

> "Across 45 markets, asking chatbots a follow-up question is the clear front-runner, reported by 42% of users."

> "In Canada and the UK, summarisation ranks highest, whereas in Austria the most frequently reported use is making news easier to understand, an application that also ranks highly in Germany and Japan."

> "We see that, across 27 markets where the question was asked, just 4% of respondents overall say they always or often click through to underlying news sources from AI, compared with 19% from search, and 17% from social media." (…"just 1% in the UK compared with 3% in Spain and 4% in Argentina").

> Footnote 1: "Per Google's documentation in March 2026, AI Overviews had been rolled out in all the markets covered by our survey, except France: https://support.google.com/websearch answer/14901683#zippy=%2Chow-to-control-your-data%2Ccountries-and-territories"

## Verbatim — methodology page (excerpt)

> "Research was conducted by YouGov using this online questionnaire from the middle of January to the end of February 2026."

[note: per-market sample sizes are on the methodology page in a table that this pull did not extract; the page text says "Even with relatively large sample sizes it is not possible to meaningfully analyse many minority groups."]

## Verbatim — Datawrapper dataset AkjEw (chart: use of / trust in AI chatbots for news, by market), full

[image: docs/raw/img/a-reuters-dnr-2026-ai-chatbots-countries-2026-09-23/01-use-and-trust-ai-chatbots-for-news-by-market.png]

```
Continent	Market	Use AI chatbots for news	Trust news from AI chatbots
Americas	US	6%	11%
Europe	UK	4%	6%
Europe	Germany	5%	13%
Europe	France	5%	15%
Europe	Italy	6%	16%
Europe	Spain	8%	18%
Europe	Portugal	7%	24%
Europe	Ireland	7%	14%
Europe	Norway	7%	12%
Europe	Sweden	7%	14%
Europe	Finland	5%	13%
Europe	Denmark	5%	8%
Europe	Belgium	7%	11%
Europe	Netherlands	7%	11%
Europe	Switzerland	10%	16%
Europe	Austria	6%	15%
Europe	Hungary	5%	16%
Europe	Slovakia	6%	12%
Europe	Czech Republic	9%	13%
Europe	Poland	10%	18%
Europe	Romania	8%	19%
Europe	Bulgaria	9%	14%
Europe	Croatia	5%	15%
Europe	Greece	12%	13%
Europe	Turkey	14%	25%
Asia-Pacific	Japan	9%	14%
Asia-Pacific	South Korea	14%	20%
Asia-Pacific	Taiwan	7%	16%
Asia-Pacific	Hong Kong	13%	30%
Asia-Pacific	Malaysia	11%	18%
Asia-Pacific	Singapore	11%	18%
Asia-Pacific	Australia	9%	19%
Americas	Canada	8%	13%
Americas	Brazil	13%	24%
Americas	Argentina	9%	20%
Americas	Chile	7%	20%
Americas	Mexico	10%	25%
Africa	South Africa*	18%	33%
Africa	Kenya*	26%	51%
Asia-Pacific	Philippines	9%	15%
Americas	Colombia	9%	21%
Asia-Pacific	India*	22%	38%
Asia-Pacific	Indonesia	12%	22%
Africa	Nigeria*	32%	62%
Americas	Peru	11%	26%
Asia-Pacific	Thailand	8%	31%
Africa	Morocco	15%	25%
Europe	Serbia	9%	17%
```

[note: the dataset carries no column header defining the period; the chapter text frames the same measure as "weekly use of AI chatbots for news". Markets marked * are, per the DNR convention, urban/younger online samples; the footnote text was not extracted.]

## Verbatim — dataset cN3Fo (head) and b6TfY (head)

[image: docs/raw/img/a-reuters-dnr-2026-ai-chatbots-countries-2026-09-23/02-ai-chatbot-news-use-by-age-and-frequency.png]

```
Type	Range	Value
Age	18-24	17
Age	25-34	15
Age	35-44	11
Age	45-64	8
Age	55+	5
Frequency	10+ times a day	18
Frequency	Several times a day	12
```

[image: docs/raw/img/a-reuters-dnr-2026-ai-chatbots-countries-2026-09-23/03-ai-chatbot-news-uses-by-market.png]

```
Q_AI_newstype. 	All	Brazil	Taiwan	Canada	Hong Kong	Austria
I asked a follow-up question about a news story	42%	44%	37%	34%	38%	37%
I asked it to give me the latest news	35%	37%	45%	37%	37%	37%
I asked it to summarise a news story	34%	33%	32%	41%	37%	35%
I asked it to find or evaluate a news source	33%	34%	26%	31%	41%	35%
I asked it to make a news story easier to understand	30%	32%	33%	26%	37%	40%
I asked it a question about how the news media works	23%	23%	29%	31%	40%	23%
I asked it to turn an article from text into audio or video (or vice-versa)	21%	25%	22%	20%	33%	23%
```

## Pull notes — mechanical only

- Chapter page HTTP 200 (79,587 bytes). Four Datawrapper iframes found in the page: cN3Fo/1, AkjEw/3, FYsU9/3 (social media use/trust by market — not an AI series, dataset fetched but not reproduced), b6TfY/1. `dataset.csv` returned HTTP 200 for all four; `<id>/full.png` returned the chart image for AkjEw, cN3Fo, b6TfY (the versioned `/3/full.png` path returned 404).
- The five country pages (united-kingdom, france, spain, italy, netherlands) returned HTTP 200 but their text carried no sentence with a percentage and the word chatbot/ChatGPT/Gemini; the per-market AI figures live in the chapter's chart data above.
- The DNR 2026 landing page linked a companion podcast episode and a "how people are using AI chatbots for news" news item; not pulled.
