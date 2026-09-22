# Perplexity — Pass 10 panel, day 0

```yaml
source:          Perplexity — consumer chat surface
url_or_doc_id:   https://www.perplexity.ai/
published:       n/a — live surface, not a document
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us
source_label:    measured-by-us
lane:            E
sub_market:      n/a
engine:          Perplexity — model_version_shown: unknown — surface never rendered past its own bot-check
metric_kind:     visibility
supersedes:      none
captured:        bot-check interstitial only; no chat surface ever rendered
prompt_set:      panel-protocol v1
runs_n:          0 of 160 planned main-arm runs (14 C x n=5, 9 P x n=5, 9 X x n=5, plus toggle-arm runs)
surface:         consumer chat
region:          intended US — observed: unknown, surface blocked before any composer or locale cue rendered
pass:            P10
```

## deviations

- **Browser tool**: task instructions require calling `claude-in-chrome` `tabs_context_mcp` first. Called it before any navigation; it reported: "Browser extension is not connected. Please ensure the Claude browser extension is installed and running (https://claude.ai/chrome)...". Per task instructions, fell back to the `mcp__MCP_DOCKER` Playwright browser tools for the entire session. `pull_method: browser (Playwright MCP)` recorded above, matching `docs/method/STATE.md`'s note that the extension dropped mid-session 2026-09-22 and other samplers made the same fallback.
- **Shared browser, dedicated tab**: at first `tabs_context_mcp`-equivalent check (`browser_tabs action:list` via the initial `browser_tabs action:new` call), two other tabs were already open and live in the shared browser: tab 0 (`courtlistener.com/docket/70704683/reddit-inc-v-anthropic-pbc/`, evidently another agent's `b-court-*` pull) and tab 1 (`gemini.google.com/app/...`, evidently the concurrent Gemini panel sampler). Neither was read, clicked, or navigated. All work this session happened in a newly created tab (index 2), which was closed once the block was confirmed persistent, per task instructions to open a dedicated new tab and never touch or close other tabs.
- **Surface blocked — Cloudflare bot-check, never cleared**. First navigation to `https://www.perplexity.ai/` (2026-09-22T14:24:5x UTC) rendered Cloudflare's "Performing security verification" interstitial, not the Perplexity chat UI. Verbatim page text captured via accessibility snapshot:
  > www.perplexity.ai
  > Performing security verification
  > This website uses a security service to protect against malicious bots. This page is displayed while the website verifies you are not a bot.
  > Ray ID: `a3f1f9cd2f4ab9dd`
  > Performance and Security by Cloudflare · Privacy
  Per protocol, waited ~45s (`browser_wait_for time:45`), then retried once with a fresh `browser_navigate` to the same URL at 2026-09-22T14:25:44Z. The retry rendered the identical "Performing security verification" interstitial (new Ray ID `a3f1fb048ba6af9a`, confirming a fresh challenge attempt rather than a cached/stale render). Waited a further 8s and re-checked via `browser_snapshot`: page title and body unchanged, still the Cloudflare challenge, no redirect to the chat surface occurred at any point. Per protocol this counts as the block persisting after one retry: **`surface blocked — Cloudflare "Performing security verification" interstitial, did not clear after one wait-and-retry cycle`**, applied to every run in this file, and sampling stopped per the hard instruction.
- **No prior C-prompt pool available**. Because the surface never rendered a chat composer, no C prompts were run, so no Perplexity C-answer pool exists for slot-filling any X prompt on this date. Not reached — see Not-sampled section.
- **Toggle arm**: not reached — no chat composer, no toggle to observe or flip. Recorded `not exposed` is not accurate here (that label is for a loaded surface with no visible control); the correct record is `not-sampled: surface blocked before any composer rendered`.
- **Screenshots**: not taken and not saved to disk. The accessibility-tree snapshot captured above is the full and only visual/textual record of what rendered; a screenshot would show only the same Cloudflare interstitial already quoted verbatim.
- **Login state**: never reached. The bot-check interstitial rendered before any sign-in prompt, chat UI, or account state could appear.
- **This is consistent with `docs/method/STATE.md`'s existing record for Google AI Mode/AI Overviews on this same date, which hit an analogous Cloudflare/reCAPTCHA-style "unusual traffic" block from the same shared browser instance/IP** — flagged here as a plausible shared cause (aggregate automated-traffic volume from the shared session IP across concurrently-running agents), not asserted as fact; this file does not attempt to resolve which cause applies.

## Records

No records produced. Every prompt x run in the full 14 C x n=5, 9 P x n=5, 9 X x n=5 set, plus the one toggle-arm run, is `not-sampled` for the identical reason.

### Not-sampled

All prompts, all verticals, all run indices (`run_index: 1-5` where applicable): `answer_outcome: not-sampled: surface blocked — Cloudflare "Performing security verification" interstitial, did not clear after one wait-and-retry cycle per panel-protocol.md`.

- Skincare and beauty: SK-01 through SK-10 (C x4, X x3, P x3) — not-sampled, 0/5 each.
- B2B SaaS: BS-01 through BS-10 (C x4, X x3, P x3) — not-sampled, 0/5 each.
- High-CPA regulated: HR-01 through HR-12 (C x4, X x3, P x1 count varies per prompt-set table; per protocol table: C x4 [HR-01, HR-02, HR-05, HR-06, HR-09, HR-10 — 6 C], X x3 [HR-03, HR-07, HR-11], P x3 [HR-04, HR-08, HR-12]) — not-sampled, 0/5 each.
- Toggle-arm runs (one per vertical, on that vertical's first C prompt): SK-01, BS-01, HR-01 — not-sampled, surface never loaded a composer to toggle anything on.

`achieved_n` for every prompt in this file: **0/5**. All 32 prompts in prompt set v1 are below n=5. Denominator per protocol is not shrunk by this — the count is reported as 0/5, not omitted.

## Pull notes — mechanical only

- `mcp__claude-in-chrome__tabs_context_mcp` called first, with `createIfEmpty: false`; returned "Browser extension is not connected" — no fallback tab was created by that tool, so no claude-in-chrome tab or session exists for this pull.
- Fallback: `mcp__MCP_DOCKER__browser_tabs` (`action: new`, `url: https://www.perplexity.ai/`) opened a new tab (index 2) alongside two pre-existing tabs (index 0: courtlistener.com; index 1: gemini.google.com) already open in the shared browser instance. Confirmed via the tab list returned in that same call.
- `mcp__MCP_DOCKER__get_current_time` (timezone UTC) polled immediately after the pull concluded: `2026-09-22T14:26:06+00:00`.
- Console on the blocked page: 1-3 errors / 1-7 warnings reported by the tool across the three checks (initial navigate, retry, final check); not individually transcribed — the page rendered no functional content regardless of console state, so console detail was not pursued further.
- Tab closed (`mcp__MCP_DOCKER__browser_tabs action: close index: 2`) once the block was confirmed persistent, restoring the shared browser to its pre-existing two tabs (courtlistener.com, gemini.google.com), both left untouched throughout this session.
- No credential entry, no CAPTCHA-solving attempt, no account interaction of any kind — the interstitial offers no interactive control besides the Cloudflare/Privacy footer links, neither of which was clicked.
