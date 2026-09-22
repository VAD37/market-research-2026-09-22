# Assistant-share table — clickstream and panel publishers with method disclosure

```yaml
task:            P2-c1, Pass 2 raw wave A
compiled:        2026-09-22
purpose:         plan.md reweight rule input — one figure per publisher x engine x metric, clickstream/panel/telemetry publishers only, method disclosure checked per row
scope note:      No interpretation, ranking or averaging here. The reweight itself is a separate task (P2-reweight, per STATE.md).
```

No number below is converted, normalised or averaged. Where two publishers disagree, both rows stand. "Method disclosed" is yes / partial (source names data source or panel but not size/recruitment) / no, judged against `docs/method/trust-rubric.md`. Population as the publisher states it — not inferred.

## Table

| Publisher | Metric (publisher's own name) | Engine | Figure (verbatim) | Date window | Population | Method disclosed | Tier | Raw file |
|---|---|---|---|---|---|---|---|---|
| Similarweb (aisearch.similarweb.com) | share of worldwide generative AI web traffic | ChatGPT | ~76% | Jun 2025 | worldwide gen-AI web traffic | partial — panel named ("Similarweb's worldwide traffic panel"), no size/recruitment | 4 | `a-similarweb-share-gen-ai-stats-2026-09-22.md` |
| Similarweb | same | ChatGPT | ~53% | May 2026 | same | partial | 4 | same |
| Similarweb | same | Gemini | under 9% | Jun 2025 | same | partial | 4 | same |
| Similarweb | same | Gemini | ~27-28% | May 2026 | same | partial | 4 | same |
| Similarweb | same | Claude | ~2% | Jun 2025 | same | partial | 4 | same |
| Similarweb | same | Claude | ~9% | May 2026 | same | partial | 4 | same |
| Similarweb | "AI Mode query share" | Google (AI Mode) | 0.34% | Jan-Apr 2026 | all Google searches, US | partial — panel named, session def. stated, no size | 4 | `a-similarweb-share-zero-click-marketing-2026-09-22.md` |
| Similarweb | "AI Mode referral rate" | Google (AI Mode) | 1.6-2.5% | 2026 | AI Mode queries | partial | 4 | same |
| Pew Research, cited via Similarweb | click rate with/without AI Overview present | Google (AI Overviews) | 8% (with) / 15% (without) | 2026 | US searches | no — Pew primary not independently pulled in this cluster | 5 | same |
| SparkToro, citing Similarweb | "AI Mode query share" (corroborating figure) | Google (AI Mode) | 0.34% | Jan-Apr 2026 | US | partial | 4 | `a-sparktoro-share-zero-click-2026-09-22.md` |
| StatCounter Global Stats | "AI Chatbot Market Share" (referral-click based) | ChatGPT | 79.4% | Aug 2026 | worldwide | yes — FAQ states page-view/referral-tag method (1M+ sites, 3bn+ page views/mo); explicitly NOT a usage panel | 4 | `a-statcounter-share-ai-chatbot-market-share-2026-09-22.md` |
| StatCounter | same | Gemini | 10.9% | Aug 2026 | worldwide | yes | 4 | same |
| StatCounter | same | Perplexity | 4.31% | Aug 2026 | worldwide | yes | 4 | same |
| StatCounter | same | Copilot | 2.79% | Aug 2026 | worldwide | yes | 4 | same |
| StatCounter | same | Claude | 2.57% | Aug 2026 | worldwide | yes | 4 | same |
| StatCounter | same | DeepSeek | 0.02% | Aug 2026 | worldwide | yes | 4 | same |
| StatCounter (press release) | "chatbot referral share" — STALE, pre-dates 2026-06-22 cutoff | ChatGPT | 79.8% | May 2025 | worldwide | yes | 4 | `a-statcounter-share-referral-press-release-2026-09-22.md` |
| StatCounter (press release, stale) | same | Perplexity | 11.8% | May 2025 | worldwide | yes | 4 | same |
| StatCounter (press release, stale) | same | Copilot | 5.2% | May 2025 | worldwide | yes | 4 | same |
| StatCounter (press release, stale) | same | Gemini | 2% | May 2025 | worldwide | yes | 4 | same |
| StatCounter (press release, stale) | same | DeepSeek | 0.8% | May 2025 | worldwide | yes | 4 | same |
| StatCounter (press release, stale) | same | Claude | 0.5% | May 2025 | worldwide | yes | 4 | same |
| StatCounter (press release, stale) | same — Grok structurally excluded | Grok | not measured — "does not provide referral data in its header" | May 2025 | worldwide | yes (exclusion is itself method-disclosed) | 4 | same |
| StatCounter, cited via Search Engine Journal | "AI chatbot referral share" | Perplexity | 7.91% | Jun 2026 | worldwide | yes | 5 (pointer) | `a-searchenginejournal-share-ai-visibility-2026-09-22.md` |
| StatCounter, cited via SEJ | same | Gemini | 7.94% | Jun 2026 | worldwide | yes | 5 (pointer) | same |
| Similarweb, cited via Search Engine Journal | "worldwide web visits" among major AI assistants | ChatGPT | 53.9% | May 2026 | worldwide | partial (per Similarweb's own disclosure; breakdown not confirmed on Similarweb primary directly) | 5 (pointer) | same |
| Similarweb via SEJ | same | Gemini | 27.9% | May 2026 | worldwide | partial | 5 (pointer) | same |
| Similarweb via SEJ | same | Claude | 9.2% | May 2026 | worldwide | partial | 5 (pointer) | same |
| Similarweb via SEJ | same | DeepSeek | 4.1% | May 2026 | worldwide | partial | 5 (pointer) | same |
| Similarweb via SEJ | same | Grok | 2.4% | May 2026 | worldwide | partial | 5 (pointer) | same |
| Similarweb via SEJ | same | Perplexity | 1.3% | May 2026 | worldwide | partial | 5 (pointer) | same |
| Similarweb via SEJ | same | Copilot | 1.3% | May 2026 | worldwide | partial | 5 (pointer) | same |
| Comscore | "desktop conversations" | ChatGPT | 244 million (+55% YoY) | Mar 2026 | not stated (population unspecified in release) | no — panel size/recruitment not disclosed on this page | 5 | `a-comscore-share-q1-2026-ai-intelligence-2026-09-22.md` |
| Comscore | same | Claude | 22 million (+1,858% vs. Oct 2025) | Mar 2026 | not stated | no | 5 | same |
| Comscore | "desktop visitors" | ChatGPT | 87 million | Mar 2026 | not stated | no | 5 | same |
| Comscore | same | Copilot | 44 million | Mar 2026 | not stated | no | 5 | same |
| Comscore | same | Gemini | 30 million | Mar 2026 | not stated | no | 5 | same |
| Comscore | "AI assistant tools reach" | all engines (combined) | 36% of desktop users, 23% of mobile users | Mar 2026 | not stated | no | 5 | same |
| Comscore | "US desktop unique visitors" (ranked) | ChatGPT | 33.86M (+18.9% MoM) | Mar 2026 | US desktop | no | 5 | `a-comscore-share-march-2026-rankings-2026-09-22.md` |
| Comscore | same | Gemini | 10.66M (+29.1% MoM) | Mar 2026 | US desktop | no | 5 | same |
| Comscore | same | Copilot | 5.02M (+44.4% MoM) | Mar 2026 | US desktop | no | 5 | same |
| Comscore | same | Claude | 2.66M (+130.1% MoM) | Mar 2026 | US desktop | no | 5 | same |
| Comscore | same | Grok | 1.65M (+9.9% MoM) | Mar 2026 | US desktop | no | 5 | same |
| Comscore | same | DeepSeek | 0.41M (+46.2% MoM) | Mar 2026 | US desktop | no | 5 | same |
| Comscore | same | Perplexity | 0.36M (+20.5% MoM) | Mar 2026 | US desktop | no | 5 | same |
| Comscore | "mobile unique visitors," CustomIQ | ChatGPT | 34.5M (+84% YoY) | Dec 2025 | not stated (mobile) | yes — "CustomIQ cross-platform measurement" named, no size | 4 | `a-comscore-share-jan-2026-mobile-desktop-2026-09-22.md` |
| Comscore | same | Gemini | 12.8M (+137% YoY) | Dec 2025 | not stated (mobile) | yes | 4 | same |
| Comscore | same | Copilot | 10.6M (+246% YoY) | Dec 2025 | not stated (mobile) | yes | 4 | same |
| Comscore | same | Perplexity | 4.7M (+265% YoY) | Dec 2025 | not stated (mobile) | yes | 4 | same |
| Comscore | same | Meta AI | 1.3M (+50% vs. May 2025 — different comparison base) | Dec 2025 | not stated (mobile) | yes | 4 | same |
| Comscore | "desktop unique visitors," CustomIQ | ChatGPT | 56.4M (+83% YoY) | Dec 2025 | not stated (desktop) | yes | 4 | same |
| Comscore | same | Copilot | 33.4M (-28% YoY) | Dec 2025 | not stated (desktop) | yes | 4 | same |
| Comscore | same | Gemini | 12.3M (+648% YoY) | Dec 2025 | not stated (desktop) | yes | 4 | same |
| Comscore | same | Perplexity | 1.4M (+516% YoY) | Dec 2025 | not stated (desktop) | yes | 4 | same |
| Comscore | same | Claude | 1.1M (+297% YoY) | Dec 2025 | not stated (desktop) | yes | 4 | same |
| Datos (Semrush/Adobe), via PPC Land | "share of total desktop visits" (single-engine penetration, not category share) | ChatGPT | US 34.80% (Q1 2026, peak Sept 2025 37.08%) | Mar 2025-Mar 2026 | US desktop web population | partial — panel size ("tens of millions"), 3-country population, date window all stated; no exact n | 5 (pointer; would be 4 at Datos primary) | `a-ppc-land-share-datos-q1-2026-2026-09-22.md` |
| Datos via PPC Land | same | ChatGPT | EU/UK 44.82% | Mar 2026 | EU/UK desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same | Gemini | US 16.06% (from 10.41% Nov 2025) | Mar 2026 | US desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same | Gemini | EU/UK 18.88% (from 12.29% Nov 2025) | Mar 2026 | EU/UK desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same | Claude | US 8.54% (from 3.58% Jan 2026) | Mar 2026 | US desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same | Claude | EU/UK 9.61% (from 3.77% Jan 2026) | Mar 2026 | EU/UK desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same, no exact % given | Perplexity, Copilot, DeepSeek | "single-digit or sub-5% levels, no significant movement" | Mar 2026 | US + EU/UK desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | "share of total desktop visits," combined | all engines (combined) | US 0.93% (from 0.41% Jan 2025); Q1 2026 US 1.65% (from Q1 2025 1.31%) | Jan 2025-Mar 2026 | US desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same, combined | all engines (combined) | EU/UK 1.08% (from 0.54% Jan 2025) | Jan 2025-Mar 2026 | EU/UK desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | "Google AI Mode, share of total desktop visits" | Google (AI Mode) | US 0.16% (from 0.01% May 2025) | Mar 2026 | US desktop | partial | 5 (pointer) | same |
| Datos via PPC Land | same | Google (AI Mode) | EU/UK 0.21% (from 0.01% Aug 2025) | Mar 2026 | EU/UK desktop | partial | 5 (pointer) | same |

## Screened vs. pulled

- **Pulled and filed as raw:** 12 files (this table plus 11 source pulls, all listed above).
- **Screened, not filed:** 29 —
  - 26 distinct marketing/listicle/vendor-blog domains returned by web search and rejected on sight (not in `docs/sources/channels.md`, and/or no disclosed n, date window or method per `trust-rubric.md`): higoodie.com, seosherpa.com, sqmagazine.co.uk, organikpi.com, omnibound.ai, quickseo.ai, tech-insider.org, firstpagesage.com, momenticmarketing.com, kavout.com, aibusinessweekly.net, trakkr.ai, digitalapplied.com, seranking.com, averi.ai, azoma.ai, marketintelligencetools.com, onlysearch.ai, anicca.co.uk, almcorp.com, mediapost.com, aiemp.substack.com, statista.com, techtimes.com, seekingalpha.com, position.digital.
  - 2 Datos primary report pages, channel-listed (C22) but gated with no public figure at pull time: `datos.live/report/the-current-ai-landscape/`, `datos.live/report/state-of-search-q2-2026/` — substituted by the PPC Land pointer (`a-ppc-land-share-datos-q1-2026-2026-09-22.md`), which carries the same underlying Datos study with figures.
  - 1 Comscore whitepaper landing page (`comscore.com/Insights/Presentations-and-Whitepapers/2026/Q1-2026-AI-Intelligence-Report`), checked, added no figures or method beyond the press release already pulled.

## Unknowns — per engine, priority-1 and priority-2

| Engine | Status |
|---|---|
| ChatGPT | Covered — Similarweb, StatCounter, Comscore, Datos/PPC Land all report a figure |
| Claude | Covered — same four publishers |
| Google (AI Overviews / AI Mode / Gemini) | Covered — Gemini by Similarweb/StatCounter/Comscore/Datos; AI Mode specifically by Similarweb (0.34% query share) and Datos (0.16-0.21% desktop-visit share) |
| Perplexity | Covered — StatCounter, Comscore, Similarweb (via SEJ), Datos (qualitative only) |
| Copilot | Covered — StatCounter, Comscore, Similarweb (via SEJ), Datos (qualitative only) |
| Amazon Rufus | `unknown — checked Similarweb (aisearch.similarweb.com), Comscore, Datos/SparkToro, StatCounter 2026-09-22` — no channels.md-listed clickstream/panel publisher was found reporting an Amazon Rufus usage, referral or traffic-share figure with disclosed method. A non-channel item (MediaPost, citing Datos, on AI-referred Amazon purchases roughly doubling YoY with a stated 60,000-shopper panel) was found but is not a channels.md source and carries no engine-share percentage — not filed, not counted as coverage. |
| Meta AI | Thin coverage — Comscore Jan 2026 press release, mobile unique visitors 1.3M (Dec 2025), one publisher only |
| Grok | Covered — Comscore (March 2026 ranking), StatCounter (2025 press release; excluded from StatCounter's current series — see tier_reason in that file), Similarweb (via SEJ) |
| DeepSeek | Covered — StatCounter, Comscore, Similarweb (via SEJ), Datos (qualitative only) |

## Caveats

- Every clickstream and panel publisher pulled here sells something adjacent to what it measures (Similarweb, Datos/Semrush, StatCounter, Comscore all sell analytics or measurement products) — per `docs/sources/channels.md` caveats, this is not a discard reason on its own, but every figure above is vendor-reported or analyst-derived, never independently audited in this pull.
- No figure in this table is a recruited-and-disclosed-sample-size consumer panel. The closest to a stated sample: StatCounter (1M+ sites, 3bn+ page views/month — a site/tag network, not a person-panel); Datos ("tens of millions of active desktop users" — panel, but no exact n); Comscore (panel referenced by name — CustomIQ — but no size ever stated in any pulled page). None reaches trust-rubric's "sample size, date window and model versions all stated" full bar; all are held at tier 4-5 per the reasons stated in each raw file.
- Definitions are NOT harmonized across publishers. "Share of worldwide generative AI web traffic" (Similarweb), "AI Chatbot Market Share" as referral-click share (StatCounter), "desktop unique visitors" (Comscore), and "share of total desktop visits" as single-engine population penetration (Datos) are four different metrics measuring different things. Per glossary.md, none of these is a "visibility" metric — all fall under **traffic**, and specifically most are traffic to the AI assistant itself (a usage/reach metric), not traffic referred FROM the assistant to a third-party brand site, except the StatCounter "referral share" rows and the Similarweb "referral rate" rows, which are the narrower "traffic" metric glossary.md actually defines (AI-surface-to-brand-site referral). This distinction is the reweight task's job to resolve, not this file's — flagged here so it is not lost.
- Every publisher's figures disagree with every other publisher's figures for the same engine and roughly the same period (e.g., ChatGPT worldwide "share" ranges from ~53% (Similarweb, May 2026 web-visit share) to 79.4% (StatCounter, Aug 2026 referral-click share) to a US-desktop-penetration reading of 34.80% (Datos, Q1 2026) — these are not the same metric measured three ways with disagreement; they are three different metrics (web-visit share of category, referral-click share of category, and single-engine share of desktop population) that happen to all get called "market share" colloquially. Kept side by side, never averaged, per root `CLAUDE.md`.
- Amazon Rufus, being retail/app-embedded rather than a standalone destination site, may simply not register in web-traffic clickstream panels the way ChatGPT/Gemini/Claude do — this is a plausible structural reason for the unknown, not confirmed by any source pulled here.
- Grok's absence from StatCounter's *current* live dashboard series was not explicitly re-confirmed in the August 2026 pull (Grok does not appear in that table) but the 2025 press release states the mechanism (no referral header data) — treated as still-operative absence, not re-verified against a current StatCounter statement.
- Oldest pull this file depends on: 2025-05 data window (StatCounter press release, flagged stale in its own raw file); oldest *pull date* of any raw file cited: all pulled 2026-09-22.
