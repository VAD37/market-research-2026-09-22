# uclic.fr — "Trafic IA vs Google" article, no named EU brand

```yaml
source:          Uclic (uclic.fr), agency blog, author Wladimir Delcros
url_or_doc_id:   https://uclic.fr/blog/trafic-ia-conversion-acquisition-b2b-2026
published:       2026-06-04
pull_date:       2026-09-22
pull_method:     fetch (curl -L, direct — one 301 redirect from www. to bare domain, followed automatically)
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     French growth-marketing agency's blog post that aggregates other publishers' figures (Visibility Labs via ALM Corp, Ahrefs, Search Engine Land, Conductor) with no primary measurement of its own and no named EU brand; per trust-rubric.md this is a marketing/pointer post, not a source for any number — pulled only as evidence of the category's secondary-aggregation noise, per templates/raw-pull.md `pull_purpose: evidence about category noise`
source_label:    vendor-reported
lane:            E, F
sub_market:      organic recommendation
engine:          ChatGPT (named throughout); Perplexity, Gemini, Claude given only as a B2B referral-share breakdown, no per-engine conversion figures
metric_kind:     traffic (conversion-rate comparison, click-through-rate decline); no sales figure
supersedes:      none
captured:        full page
language:        French
country:         France (Uclic is a Paris-based B2B growth-marketing agency; the article's own case citations are US — ALM Corp/Visibility Labs, Ahrefs, Seer Interactive, Conductor)
vertical:        none named — the "94 marques" (94 brands) figure is an unnamed, sector-unspecified aggregate; the one named case (Seer Interactive) is a US agency, already covered by cluster P4-c2 per STATE.md
evidence_grade:  screened — no EU brand named (per grading rule 1: page opened in full; the numbers on the page belong to non-EU aggregates and a non-EU named case, not to any EU brand)
paid_by_outcome: unknown — not stated on page
```

## Verbatim

Titre: "Le trafic IA convertit-il mieux que Google ? Ce que les données 2026 changent pour l'acquisition B2B"

Sous-titre: "Le trafic ChatGPT a converti 31 % mieux que l'organique non-marque en 2025. Ce que la recherche IA change vraiment pour l'acquisition B2B en 2026, données à l'appui."

Par Wladimir Delcros, 04 juin 2026

"Sur 94 marques analysées par Visibility Labs entre janvier et décembre 2025, le trafic issu de ChatGPT a converti à 1,81 % contre 1,39 % pour la recherche organique non-marque — soit 31 % de mieux."

"Key Takeaways: Le trafic référé par ChatGPT a converti 31 % mieux que l'organique non-marque sur 94 marques en 2025 (Visibility Labs). La présence d'un AI Overview fait chuter de 58 % le taux de clic de la première page Google (Ahrefs, décembre 2025). ChatGPT a dépassé 900 millions d'utilisateurs hebdomadaires en février 2026 (OpenAI). ChatGPT concentrerait 87,4 % du trafic de référence IA, mais Claude et Gemini montent vite côté B2B."

"Une étude de cas de Seer Interactive rapporte un taux de conversion de 16 % pour le trafic ChatGPT, contre 1,8 % pour l'organique Google. C'est un cas isolé, pas une moyenne de marché."

"Taux de conversion : trafic ChatGPT vs organique non-marque — 94 marques, janv.–déc. 2025 (Visibility Labs). 1,81 % ChatGPT / 1,39 % Organique non-marque. +31 % de conversion pour le trafic ChatGPT. Source : Visibility Labs, via ALM Corp, 2026."

"Qui envoie ce trafic IA en B2B ? ... Sur la moyenne mars–avril 2026, la part de ChatGPT dans les références IA B2B mesurables est tombée à 62,6 %, pendant que Claude atteignait 18,5 %, Gemini 10,6 % et Perplexity 7,3 %."

Sources (as listed on page): "Ahrefs, AI Overviews reduce clicks update, récupéré 2026-06-04, https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/"; "Search Engine Land, Google AI Overviews drive drop in organic and paid CTR, récupéré 2026-06-04, https://searchengineland.com/google-ai-overviews-drive-drop-organic-paid-ctr-464212"; "ALM Corp, ChatGPT Traffic Converts 31% Higher Than Non-Branded Organic Search (Visibility Labs), récupéré 2026-06-04, https://almcorp.com/blog/chatgpt-vs-organic-search-conversion-rate/"; "ALM Corp, ChatGPT Reaches 900 Million Weekly Active Users, récupéré 2026-06-04, https://almcorp.com/blog/chatgpt-900-million-weekly-active-users/"

Footer: "40+ clients B2B ... Uclic est une agence d'experts en Intelligence Artificielle et Growth Marketing" — Paris/France-based per site chrome ("🇫🇷 La French Tech").

## gloss (agent translation):

Across 94 brands analysed by Visibility Labs (Jan–Dec 2025), ChatGPT-referred traffic converted at **1.81%** vs. **1.39%** for non-branded organic search — **+31%**. An AI Overview's presence cuts the top-ranked page's click-through rate by **58%** (Ahrefs, Dec 2025). ChatGPT passed **900 million weekly users** in Feb 2026 (OpenAI). ChatGPT holds **87.4%** of total AI-referral traffic overall, but its share of *measurable B2B* AI referrals fell to **62.6%** (Mar–Apr 2026 average), with Claude at 18.5%, Gemini 10.6%, Perplexity 7.3%. One named case, Seer Interactive (a US SEO agency, not itself the client), reports 16% ChatGPT-traffic conversion vs. 1.8% organic — flagged in the source text itself as "un cas isolé, pas une moyenne de marché" (an isolated case, not a market average).

## Evidence bar — seven items, evaluated against this full page

Not fully applicable — the page names no EU brand's own AI-visibility result. All quantified claims trace to (a) an aggregate 94-brand US-sourced study (Visibility Labs, via a secondary US relay, ALM Corp) with no company named, or (b) a single named case, Seer Interactive, which is a US agency (not EU) already covered elsewhere in this programme (STATE.md P4-c2). Per this cluster's brief ("which EU brands... have published... a result"), neither qualifies as an EU-brand case; screened out on that basis rather than graded item-by-item.

## Pull notes — mechanical only

- Fetched via `curl -L` (redirect-following), one 301 from `https://www.uclic.fr/...` to `https://uclic.fr/...`, then HTTP 200; full article, FAQ, and source list captured in one pull.
- "Visibility Labs" and "ALM Corp" were not independently verified as EU or non-EU entities beyond what this page states (both read as US-context brands from the surrounding prose and the `.com` domain `almcorp.com`); recorded as found, not further chased, since neither is named as EU.
- Included in this file set (rather than left as a discovery-log line only) because it is a genuine French-language EU-outlet hit on the set-X-style query and was opened in full, per grading rule 1's requirement that a page be opened before being marked anything other than `screened — not opened`.
