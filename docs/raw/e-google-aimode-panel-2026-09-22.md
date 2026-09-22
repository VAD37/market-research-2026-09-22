# Google AI Mode / AI Overviews — Pass 10 panel, day 0

```yaml
source:          Google — AI Mode and AI Overviews, search-integrated surfaces
url_or_doc_id:   primary arm https://www.google.com/search?q=<query>&udm=50 ; secondary arm https://www.google.com/search?q=<query>
published:       n/a — live surface, not a document
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP) — claude-in-chrome extension not connected this session, see deviations
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us
source_label:    measured-by-us
lane:            E
sub_market:      n/a
engine:          Google AI Mode / Google AI Overviews — model_version_shown: unknown — surface displays none reachable; every request this session was intercepted before any AI Mode or AI Overviews content rendered
metric_kind:     visibility
supersedes:      none
captured:        none — every navigation to google.com/search this session returned Google's own bot-check ("/sorry/") page instead of a search result page; that block page is captured verbatim below
prompt_set:      panel-protocol v1
runs_n:          0 of 175 planned achieved. Planned: primary arm (AI Mode) 14 C x n=5 (70) + 9 P x n=5 (45) + 9 X x n=5 (45) + 1 toggle-arm run = 161; secondary arm (AI Overviews) 14 C x n=1 (14, protocol deviation per task instructions) = 14. Achieved: 0/161 primary, 0/14 secondary
surface:         Google AI Mode (primary, search-integrated) / Google AI Overviews (secondary, search-integrated)
region:          intended US — observed: unknown — surface blocked before any region, language or country-selector signal could render
pass:            P10
```

## Deviations

- **Browser tool fallback.** Task instructions: try `claude-in-chrome` `tabs_context_mcp` first. Called at the start of this session; it returned "Browser extension is not connected. Please ensure the Claude browser extension is installed and running..." — a connection failure, not a missing capability. Fell back to the `mcp__MCP_DOCKER__browser_*` Playwright tools per task instructions and per the standing decision already recorded in `docs/method/STATE.md` ("Samplers may fall back to the MCP_DOCKER Playwright browser when the claude-in-chrome extension reports not connected"). `pull_method: browser (Playwright MCP)` recorded above accordingly.
- **Shared browser, dedicated tab.** The Playwright browser already held two tabs opened by other concurrently-running agents: tab 0 (`courtlistener.com`, a docket page — evidently a `b-court-*` pull) and tab 1 (`gemini.google.com/app/...` — evidently the live `P10-d0-gemini` or a related session). A new tab (index 2) was opened via `browser_tabs {action:"new", url:<AI Mode URL>}` for all sampling in this file; neither tab 0 nor tab 1 was read, clicked, navigated, or closed at any point. Tab 2 was closed after the block was confirmed persistent, once no further sampling in it was possible.
- **Immediate bot-check block, primary arm (AI Mode).** The very first navigation this session — to `https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50` (SK-01, intended run 1) — did not return a search results page. It redirected to `https://www.google.com/sorry/index?continue=...` and rendered Google's "unusual traffic" reCAPTCHA interstitial. Poll immediately after: `timestamp_utc: 2026-09-22T14:20:51Z` (from the block page's own "Time:" field, corroborated by the tool's response timing). Verbatim block-page text, captured via accessibility snapshot:

  > About this page
  > Our systems have detected unusual traffic from your computer network. This page checks to see if it's really you sending the requests, and not a robot.
  > Why did this happen?
  > IP address: 159.26.119.97
  > Time: 2026-09-22T14:20:51Z
  > URL: https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50&sei=wY6yaq2OOM_g2roPmNzMwAw

  The page body also embeds a reCAPTCHA `iframe` with a "I'm not a robot" checkbox widget. Per the hard constraints (no CAPTCHA solving), this was not interacted with in any way — not clicked, not inspected further than the accessibility tree already returned.
- **Retry once, per protocol.** Waited approximately 45 seconds (background timer, confirmed elapsed via a `wait`/monitor call, not a guessed delay), then retried the identical URL once via a fresh `navigate` call in the same tab. Result: identical block pattern, new `/sorry/` page, `sei` parameter changed (`3o6yaqKINrrl2roP-fTuiQ8`), same "unusual traffic" text and same IP `159.26.119.97`. Poll: this second block page loaded at approximately `2026-09-22T14:21:18Z` (screenshot/tool-response timestamp; the block page's own embedded "Time:" field was not re-read verbatim for this second instance since the pattern match to the first was already unambiguous from the URL, title and snapshot structure).
- **Cross-arm check, secondary arm (AI Overviews).** To determine whether the block was specific to the `udm=50` AI Mode parameter or domain-wide, one additional navigation was made to the plain-search secondary-arm URL for the same query, `https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin` (no `udm=50`). Result: identical `/sorry/` block page, confirming the block is **domain-wide across `google.com/search`**, not an AI-Mode-specific gate. This one plain-search attempt stands in for what would otherwise have been AI-Overviews run 1 of SK-01; it is counted in the Not-sampled table below rather than as a second, separate attempt.
- **No further per-prompt attempts.** Per the hard constraint against CAPTCHA-solving, and because the protocol's own retry allowance ("record it verbatim, wait, retry once, and if it persists record `surface blocked`") was exhausted and had already produced two independent confirmations (one retry on the primary arm, one cross-check on the secondary arm) of a domain-wide block, no further navigations to `google.com/search` were attempted this session. Continuing to hammer an already-confirmed-blocked domain with 170+ more requests would itself have been the kind of automated traffic pattern the block exists to catch, and would not have produced different evidence. `surface blocked — Google "unusual traffic" / reCAPTCHA interstitial on every google.com/search request this session, confirmed by one retry and one cross-arm check, none solved` applies to every remaining planned run in both arms; see Not-sampled below.
- **Login state.** Not established — the block occurred pre-search, so no login-state UI (account chip, sign-in prompt) was ever reached. Recorded per run as `login_state: unknown — surface blocked before login UI reached` throughout.
- **Search toggle, toggle arm.** Not exposed / not reached for the same reason — no AI Mode page ever rendered, so no toggle control was ever visible. The protocol's toggle-arm re-run could not be attempted.
- **Region/personalization signals.** None observed — the `/sorry/` interstitial carries no locale, currency or country-selector content beyond the plain "IP address" and "Time" fields quoted above.
- **No settings changed, no CAPTCHA solved, no sign-in attempted, no ads clicked** — consistent with the hard constraints throughout this session.

## Records

No run in this file reached `answer_outcome: answered` (or any other outcome besides a pre-search block). No `sample_id` record carries an answer, brand list, citation list, or sponsored-unit observation — every planned run is recorded in the Not-sampled table below with `answer_outcome: not-sampled` and the shared reason `surface blocked — Google "unusual traffic" / reCAPTCHA interstitial, confirmed by retry, not solved`.

`achieved_n: 0/5` for every C, P and X prompt on the primary arm (Google AI Mode); `achieved_n: 0/1` (planned n) for every C prompt on the secondary arm (Google AI Overviews); the toggle arm was not attempted (0/1).

## Not-sampled

All prompts, both arms, `not-sampled: surface blocked — Google "unusual traffic" / reCAPTCHA interstitial on every google.com/search request this session (verbatim text and retry evidence in Deviations above); CAPTCHA not solved per hard constraints`.

**Primary arm — Google AI Mode (`udm=50`), planned n=5 each, achieved 0/5:**

| id | kind | vertical | prompt |
|---|---|---|---|
| SK-01 | C | Skincare | best moisturizer for dry sensitive skin |
| SK-02 | C | Skincare | best vitamin C serum under $50 |
| SK-03 | C | Skincare | best sunscreen for daily use under makeup |
| SK-04 | C | Skincare | best retinol for beginners |
| SK-05 | X | Skincare | {A} vs {B} for dry skin — which is better? |
| SK-06 | X | Skincare | is {A} worth the price compared to {B}? |
| SK-07 | X | Skincare | {A} vs {B}: which has better ingredients for acne-prone skin? |
| SK-08 | P | Skincare | what should I use for hormonal acne on my chin? |
| SK-09 | P | Skincare | my skin barrier is damaged from over-exfoliating — what should I use? |
| SK-10 | P | Skincare | I have melasma and nothing is working. what should I try? |
| BS-01 | C | B2B SaaS | best help desk software for a 50-person support team |
| BS-02 | C | B2B SaaS | best CRM for a B2B startup under 20 employees |
| BS-03 | C | B2B SaaS | best project management tool for a remote engineering team |
| BS-04 | C | B2B SaaS | best HR and payroll platform for a US company with 200 staff |
| BS-05 | X | B2B SaaS | {A} vs {B} for a mid-market company — which should we buy? |
| BS-06 | X | B2B SaaS | {A} vs {B}: which is cheaper at 100 seats? |
| BS-07 | X | B2B SaaS | we are moving off {A}. is {B} the right replacement? |
| BS-08 | P | B2B SaaS | our sales team is losing deals because follow-ups get missed. what software fixes that? |
| BS-09 | P | B2B SaaS | we need SOC 2 evidence collection without hiring anyone. what should we use? |
| BS-10 | P | B2B SaaS | what should we use to stop paying for SaaS licences nobody uses? |
| HR-01 | C | High-CPA regulated | best travel rewards credit card for someone who flies twice a year |
| HR-02 | C | High-CPA regulated | best cashback credit card with no annual fee |
| HR-03 | X | High-CPA regulated | {A} vs {B} — which credit card earns more on groceries? |
| HR-04 | P | High-CPA regulated | I have a 640 credit score and need a card that will approve me. what should I apply for? |
| HR-05 | C | High-CPA regulated | best term life insurance for a 35-year-old non-smoker |
| HR-06 | C | High-CPA regulated | best pet insurance for a puppy |
| HR-07 | X | High-CPA regulated | {A} vs {B} for car insurance — which is cheaper for a clean driving record? |
| HR-08 | P | High-CPA regulated | my home insurance was just non-renewed. what do I do and who should I go to? |
| HR-09 | C | High-CPA regulated | best creatine supplement |
| HR-10 | C | High-CPA regulated | best magnesium supplement for sleep |
| HR-11 | X | High-CPA regulated | {A} vs {B}: which protein powder is better tested for heavy metals? |
| HR-12 | P | High-CPA regulated | I'm always tired in the afternoon. what supplement should I take? |

X-prompt note: no slot fill was computed for `{A}`/`{B}` — protocol rule 2 (first sample date, fill from this date's own C answers) requires completed C answers, and zero C runs were achieved on either arm. `slot_fill: not-sampled — no C-prompt pool available, engine blocked before any C prompt could be answered`.

Toggle arm: 1 planned run (re-run the first-sampled vertical's first C prompt, SK-01, with the search toggle flipped) — not attempted, `not-sampled: surface blocked, and no toggle control was ever reached to flip`.

**Secondary arm — Google AI Overviews (plain search, no `udm=50`), planned n=1 each per task deviation, achieved 0/1:**

| id | kind | vertical | prompt |
|---|---|---|---|
| SK-01 | C | Skincare | best moisturizer for dry sensitive skin |
| SK-02 | C | Skincare | best vitamin C serum under $50 |
| SK-03 | C | Skincare | best sunscreen for daily use under makeup |
| SK-04 | C | Skincare | best retinol for beginners |
| BS-01 | C | B2B SaaS | best help desk software for a 50-person support team |
| BS-02 | C | B2B SaaS | best CRM for a B2B startup under 20 employees |
| BS-03 | C | B2B SaaS | best project management tool for a remote engineering team |
| BS-04 | C | B2B SaaS | best HR and payroll platform for a US company with 200 staff |
| HR-01 | C | High-CPA regulated | best travel rewards credit card for someone who flies twice a year |
| HR-02 | C | High-CPA regulated | best cashback credit card with no annual fee |
| HR-05 | C | High-CPA regulated | best term life insurance for a 35-year-old non-smoker |
| HR-06 | C | High-CPA regulated | best pet insurance for a puppy |
| HR-09 | C | High-CPA regulated | best creatine supplement |
| HR-10 | C | High-CPA regulated | best magnesium supplement for sleep |

One of these fourteen (SK-01) was the actual plain-search attempt made as the cross-arm check described in Deviations; it is not double-counted as two separate not-sampled entries.

## Pull notes — mechanical only

- Every navigation this session (2 to the AI Mode URL, 1 to the plain-search URL) produced the same redirect target pattern: `https://www.google.com/sorry/index?continue=<original URL, percent-encoded>&q=<opaque token>`. The `continue` parameter round-trips the exact originally-requested URL including the `udm=50` parameter where present, confirming the block is applied ahead of, not instead of, normal query routing.
- Console showed 2 errors and 1-2 warnings on each block-page load; not inspected further, as they relate to the reCAPTCHA widget's own script (third-party `recaptcha` iframe), not to any panel-relevant content.
- No screenshot saved to disk (`screenshot_ref: none` throughout) — the block page carries no account identity or panel content worth preserving as an image; the accessibility-tree snapshot already captured the full verbatim text and is quoted above.
- `get_current_time` (UTC) was polled at session start context-gathering (14:20:55Z, informational) and again at session end (14:22:24Z) to bound the whole blocked-sampling window; no answer ever rendered, so no per-run "answer completion" timestamp exists.
- Region/country signals: the block page's only location-adjacent field is the IP address `159.26.119.97` it printed back, which is an artifact of Google's own bot-check logging, not a `region_observed` signal about search results (none rendered).

## Caveats

- **Zero runs achieved.** This file measures a block, not the AI Mode or AI Overviews surfaces themselves. It says nothing about what brands either surface would mention, cite or recommend on 2026-09-22; it says only that this session's traffic pattern (shared IP `159.26.119.97`, likely already elevated by other concurrently-running research agents on the same shared browser/network path per `docs/method/STATE.md`'s "Decisions taken" log) tripped Google's automated bot-check before any query could be answered.
- The block is most plausibly attributable to aggregate automated-traffic volume from this IP across the whole multi-agent research session (courtlistener.com, gemini.google.com and other concurrent pulls sharing the same egress), not to anything specific about the AI Mode query text or the udm=50 parameter — the cross-arm check found the identical block on plain search with no `udm=50`.
- A later sample attempt, ideally after a longer cooldown than the one retry this protocol allows and/or from a different network path, may clear the block; this file does not attempt to predict that.
- Every field that would normally carry a per-run observation (`model_version_shown`, `region_observed`, `login_state`, `search_toggle`, brand lists, sponsored units) is `unknown — surface blocked before render` or `not-sampled` throughout, per the explicit task instruction that unreached fields record the reason rather than being omitted.
- This file's Google AI Mode row in `panel-protocol.md`'s engine table already carried the note "loaded 2026-09-22, browser extension" from an earlier verification — that verification evidently succeeded before this session's traffic pattern (or a different session's) triggered today's block; this file does not amend `panel-protocol.md`, per task instructions.
