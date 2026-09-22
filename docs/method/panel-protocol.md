# Panel protocol — Pass 10, measured by us

Set 2026-09-22. Fixes the measurement for Pass 10 per `plan.md` "Pass 0 additions". A Sonnet sampling agent with the Chrome browser extension runs one sampling date from this file alone; an Opus analyst reads the output. Authority: root `CLAUDE.md` > `scope.md` > `plan.md` > `trust-rubric.md` > `glossary.md` > this file.

Everything this panel produces is **Visibility** in the `glossary.md` sense — never traffic, never sales.

## Hard constraints

- Read-only observation. No attempt to influence, steer, seed or degrade any engine's answer, index or corpus.
- No prompt names a real brand. Comparison slots are filled from the engines' own answers (rule below), never chosen to steer.
- Lane D (manipulation) never runs here. This panel measures; it does not test techniques.
- No account the researcher does not own. No credential entry, no account creation, no CAPTCHA solving. A surface demanding login is recorded `login required` with the state used, and is not sampled.
- No posting, submitting, purchasing, or clicking an irreversible control. The only input is the prompt typed into the assistant's own box. API output is never substituted for a consumer-surface sample.
- Screenshots must not show an account identity. Crop it, or take the sample logged-out.

## Engines and surfaces

Consumer chat is the **primary** surface. API is secondary, labelled `surface: API` on every record, and is not what users see. Priority is the `plan.md` engine matrix — an assumption until the Pass 2 share table reweights it.

| Engine | Priority | Surface kind | Surface URL | Status |
|---|---|---|---|---|
| ChatGPT | 1 | consumer chat | `surface URL: unknown — verify at first sample` | not loaded 2026-09-22; 403 to fetchers, extension navigation reverted |
| Claude | 1 | consumer chat | `https://claude.ai/new` | loaded 2026-09-22, browser extension |
| Gemini | 1 | consumer chat | `https://gemini.google.com/app` | loaded 2026-09-22, fetch |
| Google AI Mode | 1 | search-integrated | `https://www.google.com/search?q=<query>&udm=50` | loaded 2026-09-22, browser extension |
| Google AI Overviews | 1 | search-integrated | same path without `udm=50` — `unknown — verify at first sample` | not separately verified |
| Perplexity | 2 | consumer chat | `https://www.perplexity.ai/` | loaded 2026-09-22, browser extension |
| Microsoft Copilot | 2 | consumer chat | `https://copilot.microsoft.com/` | loaded 2026-09-22, fetch |
| Amazon Rufus | 2 | consumer chat, in-page | host `https://www.amazon.com/` loaded 2026-09-22; Rufus entry point `unknown — verify at first sample` | reachable, entry unconfirmed |
| Meta AI, Grok, DeepSeek | 3 | — | `unknown — verify at first sample` | existence check only, one line per sample date, no prompt set |
| Naver, Kakao, Baidu | 4 | — | deferred per `scope.md` D2 | not sampled |

Nothing about any engine's features, model line-up, ad products or toggles is asserted here; the sampler records what the surface shows on the day. An `unknown` surface URL is resolved by the sampler at first sample and recorded in that date's raw file, not by editing this table.

## Prompt set v1 — 2026-09-22

Fixed. **Any change to a prompt, an id, or the set's composition creates v2 in a new file `panel-protocol-v2.md`. This file is never edited to change the set.** Every record carries `prompt_set_version: v1`.

Prompts are brand-neutral by construction: the panel measures which brands the engines volunteer. Kinds: **C** category recommendation, **X** comparison, **P** problem-shaped.

### Comparison slot fill — `{A}`, `{B}`

X prompts carry placeholder slots. Fill rule, in order:

1. Pool the C-prompt answers for that vertical from the **previous completed sample date**, across all engines sampled. Rank brands by number of runs mentioning them. `{A}` = rank 1, `{B}` = rank 2. Ties broken by earliest mean rank position, then alphabetically.
2. On the **first** sample date there is no previous date: run all C prompts for the vertical first, on every engine, then fill from that date's own C answers by the same rule.
3. If fewer than two distinct brands result, and the vertical is B2B SaaS, fill from Pass 3's vendor census (`docs/raw/` vendor pulls) in its own order. Otherwise record `not-sampled: no slot fill available` for that X prompt.

Slot fills are **data, not prompt-set content**. A different fill does not create v2. The values used are recorded per record in `slot_fill`; the prompt as actually sent is recorded verbatim in `prompt_text_as_sent`.

### Skincare and beauty — anchor, 10 prompts

| id | kind | prompt |
|---|---|---|
| SK-01 | C | best moisturizer for dry sensitive skin |
| SK-02 | C | best vitamin C serum under $50 |
| SK-03 | C | best sunscreen for daily use under makeup |
| SK-04 | C | best retinol for beginners |
| SK-05 | X | {A} vs {B} for dry skin — which is better? |
| SK-06 | X | is {A} worth the price compared to {B}? |
| SK-07 | X | {A} vs {B}: which has better ingredients for acne-prone skin? |
| SK-08 | P | what should I use for hormonal acne on my chin? |
| SK-09 | P | my skin barrier is damaged from over-exfoliating — what should I use? |
| SK-10 | P | I have melasma and nothing is working. what should I try? |

### B2B SaaS — 10 prompts

| id | kind | prompt |
|---|---|---|
| BS-01 | C | best help desk software for a 50-person support team |
| BS-02 | C | best CRM for a B2B startup under 20 employees |
| BS-03 | C | best project management tool for a remote engineering team |
| BS-04 | C | best HR and payroll platform for a US company with 200 staff |
| BS-05 | X | {A} vs {B} for a mid-market company — which should we buy? |
| BS-06 | X | {A} vs {B}: which is cheaper at 100 seats? |
| BS-07 | X | we are moving off {A}. is {B} the right replacement? |
| BS-08 | P | our sales team is losing deals because follow-ups get missed. what software fixes that? |
| BS-09 | P | we need SOC 2 evidence collection without hiring anyone. what should we use? |
| BS-10 | P | what should we use to stop paying for SaaS licences nobody uses? |

### High-CPA regulated — cards, insurance, supplements, 12 prompts

| id | kind | prompt |
|---|---|---|
| HR-01 | C | best travel rewards credit card for someone who flies twice a year |
| HR-02 | C | best cashback credit card with no annual fee |
| HR-03 | X | {A} vs {B} — which credit card earns more on groceries? |
| HR-04 | P | I have a 640 credit score and need a card that will approve me. what should I apply for? |
| HR-05 | C | best term life insurance for a 35-year-old non-smoker |
| HR-06 | C | best pet insurance for a puppy |
| HR-07 | X | {A} vs {B} for car insurance — which is cheaper for a clean driving record? |
| HR-08 | P | my home insurance was just non-renewed. what do I do and who should I go to? |
| HR-09 | C | best creatine supplement |
| HR-10 | C | best magnesium supplement for sleep |
| HR-11 | X | {A} vs {B}: which protein powder is better tested for heavy metals? |
| HR-12 | P | I'm always tired in the afternoon. what supplement should I take? |

Refusals are expected in this vertical. A refusal is a result, not a failure; it is recorded and counts toward n.

## Sample parameters

| Parameter | Setting | Recording rule |
|---|---|---|
| n per prompt | **5** runs, per prompt × engine × sample date, each in a fresh chat or session with no carried context | `run_index: 1-5`; `achieved_n` per prompt × engine |
| Why 5 | One date at n=5 resolves only always / sometimes / never — the 95% Wilson interval at p=0.5 spans roughly ±0.35. The series, not one date, is the unit of inference; pooling dates raises effective n. A rate from one date is never reported without its interval | — |
| Region | Intended **US**. No VPN or proxy unless the user has set one | `region_intended: US`; `region_observed:` = interface language, currency, country selector, any "results for <country>" string, recorded verbatim. A mismatch is recorded, not discarded |
| Login | Default **logged-out**, fresh private window, no history | `login_state: logged-out \| logged-in (researcher-owned) \| login required — not sampled` |
| Search toggle | Leave at the fresh-session default. Do **not** change it for the main arm | `search_toggle: on \| off \| not exposed \| unknown — surface did not show one` |
| Toggle arm | Once per engine per sample date, re-run the vertical's first C prompt with the toggle flipped | `arm: main \| toggle-flipped`. Flipped runs excluded from the main rate series |
| Model version | Exactly as the surface displays it — picker label, footer, "about this answer" panel. Never inferred | `model_version_shown:` verbatim, or `unknown — surface displays none` |
| Timestamp, order | UTC, ISO 8601 to the second, at answer completion. C prompts first — slot fills depend on them — then X, then P | `timestamp_utc:` plus `local_utc_offset:` |

## Record schema — one record per run, all fields present

| Field | Rule |
|---|---|
| `sample_id` | `<engine-slug>-<YYYY-MM-DD>-<prompt_id>-r<run_index>` |
| `engine`, `surface`, `surface_url` | Engine name from the table above; `consumer chat \| search-integrated \| API`; URL actually opened, verbatim |
| `model_version_shown` | Verbatim, or `unknown — surface displays none` |
| `region_intended`, `region_observed`, `login_state`, `search_toggle`, `arm` | Per sample parameters |
| `prompt_set_version` | `v1` |
| `vertical`, `prompt_id`, `prompt_kind` | Per prompt set |
| `slot_fill` | `{A}=<brand>, {B}=<brand>`, or `n/a` |
| `prompt_text_as_sent` | Verbatim, slots resolved |
| `run_index` | 1-5 |
| `timestamp_utc`, `local_utc_offset` | Per sample parameters |
| `answer_text_verbatim` | Full answer, unedited. Gaps marked `[note: ...]` per `templates/raw-pull.md` |
| `answer_outcome` | `answered \| refusal \| cannot-browse \| empty \| error \| not-sampled: <reason>` |
| `brands_mentioned` | Ordered, document order of first appearance; canonical name plus the variant as printed |
| `brands_cited` | Ordered list of domains the answer links or footnotes |
| `brands_recommended` | Ordered, per the coding rules below |
| `rank_position` | Per recommended brand: 1-based ordinal of first appearance; plus `list_ordered: yes\|no` and `tie: yes\|no` |
| `sponsored_units` | Any visible sponsored, ad, shopping or merchant unit: **label text verbatim**, position, and whether a brand in it also appears in the answer body. `none observed` if absent |
| `screenshot_ref` | Path under `docs/raw/screenshots/`, or `none`. Taken for `run_index: 1` of every prompt × engine, and for every run showing a sponsored unit |
| `notes` | Mechanical only — blocked element, truncation, dynamic render, bot check |

## Raw output

One file per engine per sample date, under `docs/raw/`, written to `templates/raw-pull.md`:

- Filename `e-<engine-slug>-panel-<YYYY-MM-DD>.md`. Engine slugs: `chatgpt`, `claude`, `gemini`, `google-ai-mode`, `google-ai-overviews`, `perplexity`, `copilot`, `amazon-rufus`.
- Header block: `pull_method: browser extension`, `tier: 1`, `source_label: measured-by-us`, `lane: E`, `metric_kind: visibility`, plus the measured-by-us lines `prompt_set: panel-protocol v1`, `runs_n:`, `surface:`, `region:`, plus one line `pass: P10` — the lane slot in `templates/raw-pull.md` is fixed to `a`–`f`, so the P10 tag rides alongside the lane rather than inside it.
- Every field the surface does not expose takes an explicit `unknown — <what>` line. Absence is recorded, never omitted.
- Raw is compression-exempt and never edited after landing. A bad sample is re-sampled into a new file; the old one stays with its date. Append one row per sample date to the `STATE.md` Pass 10 sampling log.

## Sampling calendar — intervals only

No absolute future dates: `scope.md` R3 and `MegaPlan.md` non-goals forbid scheduling.

| Rule | Value |
|---|---|
| First sample | Taken as soon as this protocol lands. It landed 2026-09-22; that first sample date becomes day 0 of the series |
| Cadence | Every **14 days** from day 0, ±2 days |
| Before any change is reported | 3 sample dates minimum, and then only as a labelled two-point difference |
| Before any trend claim | 6 sample dates minimum |
| Per sample date | Full prompt set × every priority-1 and priority-2 engine reachable; priority-3 engines get one existence-check line |
| Missed interval | Recorded as a gap with its reason. The series is never back-filled |

## Coding rules — for the analyst

Senses are `glossary.md`'s, counted separately, never summed.

| Rule | How |
|---|---|
| Mention | Brand named in the answer body. Counted once per run however often it repeats. Variants normalised to a canonical string; the printed variant kept verbatim |
| Citation | Answer links or footnotes a domain the brand controls. A link to a third-party page that merely names the brand is a citation for that third party, not for the brand |
| Recommendation | Brand offered as an answer to the buying-shaped prompt — in a list, table, or sentence saying what to use or buy. Named only as context, as a thing to avoid, or inside a caveat = mention, not recommendation |
| Lists and ties | `rank_position` = document order of first appearance, 1-based. Unordered lists still take document order, with `list_ordered: no`. "In no particular order" takes document order with `tie: yes` |
| Refusal, cannot-browse, empty, error | Recorded as that outcome, answer text kept verbatim, zero brands. **Counts toward n.** The denominator never shrinks |
| Not-sampled | Login wall, bot check, unreachable surface. Excluded from n. `achieved_n` reported beside every rate |
| Rates | Runs containing the thing ÷ `achieved_n`, per brand × prompt × engine × sample date, and pooled per vertical |
| Uncertainty | **Wilson score interval, 95%**, reported as `p [lo, hi]` to two decimals. No rate is reported without it. At `achieved_n` under 5, report the raw fraction `k/n`, not a percentage |
| Change between two dates | Reported only when the two Wilson intervals for the same engine × prompt × brand do not overlap; otherwise recorded as "no separation at this n". A presence change — 0/n on one date, k/n on the other — is recorded as such regardless of overlap. Any `model_version_shown` change between the dates is recorded beside the change and never separated from it |

## Analysis outputs

The Opus analyst compiles `docs/findings/panel-read.md` (finding budget 100 lines, per `plan.md`), recompiled as sample dates accumulate, citing every `docs/raw/` panel file behind it and naming the oldest pull it depends on. It carries, per engine × vertical: mention, citation and recommendation rates with Wilson intervals and `achieved_n`; rank-position distribution per brand; the sponsored-unit log with label text verbatim; refusal and cannot-browse rates; model versions observed per date; and the change log between consecutive dates.

predictions checked: per hypotheses.md panel-checkable set

## Caveats

- Engine answers are stochastic. n=5 per date resolves only always / sometimes / never; the series carries the inference, not any single date.
- Region and personalisation are observed, not controlled. `region_observed` may differ from `region_intended`, and a logged-out fresh window is not a neutral user.
- Browser-extension observability is partial: dynamic units, lazy-loaded citations and in-page assistants may not render or extract. Every gap is an `unknown — <what>` line, not silence.
- Consumer surfaces change monthly per the `plan.md` staleness rule. A change in a rate may be a product change, a model change, or both; this protocol cannot separate them.
- n is small, the set is 32 prompts across three verticals, and its phrasing is the researcher's guess at buying-shaped language. Tier 1 on provenance, narrow on coverage: it bounds nothing about the market, it measures what these prompts return on these engines on these dates.

## Status note 1 — 2026-09-22

Sampling held by user decision 2026-09-22 22:40; hold recorded as gap rows, never back-filled. Day 0: Claude 83/163 logged-in with Memory on — every run labelled `personalised`, excluded from HP1/HP2 rates, usable for HP3 only; Gemini 24/160 logged-out, model `Flash-Lite`, toggle `not exposed` — toggle arm counts as not-sampled for HP4; ChatGPT, AI Mode, Perplexity blocked, 0 runs. On resumption: logged-out private window first for every engine; the Amazon row carries both names `Rufus / Alexa for Shopping` as the surface shows; the Google rows record the surface name as displayed. Minimum panel to score HP1–HP3: two P1 engines × 14 C prompts × n=5 on one date, one engine repeated on a second date. Predictions checked (line 179): HE2, HE3, HP1, HP2, HP3, HP4 against a bar of three.

Source: `plan-review-1-2026-09-22.md` §2 and §7. Prompt set v1 is untouched and no table above is edited. The line-179 placeholder `predictions checked: per hypotheses.md panel-checkable set` is resolved here rather than by editing it: the six panel-checkable IDs are **HE2, HE3, HP1, HP2, HP3, HP4**, and the bar is **three of the six** (`hypotheses.md` line 42). One gap row is appended to the `STATE.md` Pass 10 sampling log with reason "user hold 2026-09-22"; the hold is a gap, not a back-fill, per the sampling-calendar rule above.
