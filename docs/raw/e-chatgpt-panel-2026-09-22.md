# ChatGPT — Pass 10 panel, day 0

```yaml
source:          OpenAI — ChatGPT consumer chat surface
url_or_doc_id:   https://chatgpt.com/
published:       n/a — live surface, not a document
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us, but zero runs achieved; see Pull notes
source_label:    measured-by-us
lane:            E
sub_market:      n/a
engine:          ChatGPT — model version unknown, surface not reached
metric_kind:     visibility
supersedes:      none
captured:        none — surface blocked before any page content rendered
prompt_set:      panel-protocol v1
runs_n:          0
surface:         consumer chat
region:          intended US — not observed, surface not reached
pass:            P10
```

## Verbatim

No answer content captured. The surface never rendered past a blank `chrome://newtab/` state — see Pull notes.

## Pull notes — mechanical only

- Task instruction: resolve the ChatGPT consumer surface URL first, via `tabs_context_mcp` then a new tab navigated to `https://chatgpt.com/`, per `docs/method/panel-protocol.md`'s open item (surface URL recorded there as `unknown — verify at first sample`; prior note: "not loaded 2026-09-22; 403 to fetchers, extension navigation reverted").
- `tabs_context_mcp` called with `createIfEmpty: true` — returned one existing tab (`chrome://newtab/`), tab group id `1500693496`.
- `tabs_create_mcp` opened a new tab, id `1697683896`, initial state `chrome://newtab/`.
- `navigate` to `https://chatgpt.com/` on tab `1697683896` returned success (`"Navigated to https://chatgpt.com/"`, tab context echoed title "chatgpt.com", url `https://chatgpt.com/`).
- Immediate follow-up call (`get_page_text`, then separately `computer: screenshot`) failed: `Can't interact with browser-internal or unparseable URLs. Navigate to a web page first.` A subsequent `tabs_context_mcp` call showed the tab had reverted to `title: "New Tab"`, `url: "chrome://newtab/"` — the navigation did not hold.
- Repeated the navigate call a second time on the same tab: same pattern — `navigate` reported success to `https://chatgpt.com/`, immediate `get_page_text` failed with the same browser-internal-URL error, and `tabs_context_mcp` again showed the tab reverted to `chrome://newtab/`.
- Ran a `browser_batch` of `[navigate to https://chatgpt.com/, wait 2s, screenshot]` on the same tab to rule out a timing race. Result: `navigate` and `wait` both completed; the `screenshot` step failed with `"Permission denied for this action on this domain (2 completed, 0 remaining)"`. A following `tabs_context_mcp` again showed the tab at `chrome://newtab/`.
- Reading: the Chrome extension does not hold site-level permission for `chatgpt.com`. The extension's own navigate call is allowed to reach the domain, but any content-reading or interaction call (`get_page_text`, `screenshot`) is denied by the extension's permission system, and the tab is reverted to `chrome://newtab/` between calls. This matches the protocol table's prior note ("extension navigation reverted") and explains the earlier 403 to plain fetchers separately.
- No login wall was observed — the block occurred before any ChatGPT page content rendered, so login state could not be determined. `model_version_shown`, `region_observed`, `search_toggle` and every other surface-exposed field are `unknown — surface blocked, no page content ever rendered`.
- No screenshot was saved: the one screenshot attempt itself returned the permission-denied error rather than an image, so there is no image file to reference. `screenshot_ref: none — capture itself was denied by the extension's site permission`.
- Tab `1697683896` closed after the failed attempts. No further navigation attempted per task instruction ("write the file with that status and zero runs, and stop").
- Per task instruction, treated as: `surface blocked — Chrome extension site permission not granted for chatgpt.com (navigate succeeds; every read/interact call on the resulting page — get_page_text, screenshot — returns "Permission denied for this action on this domain", and the tab reverts to chrome://newtab/ between calls)`.
- `login_state`: not determined — could not be `login required — not sampled` in the literal sense (no login wall was seen), so recorded as `unknown — surface blocked before any page rendered, login wall never reached`.
- Zero of the 32 prompt-set v1 prompts were run. `achieved_n: 0` for every prompt id (SK-01–SK-10, BS-01–BS-10, HR-01–HR-12). No toggle arm run. No comparison-slot fill performed (no C-prompt answers exist to pool from).
- This deviates from `panel-protocol.md`'s assumption that a surface reachable enough to attempt navigation is samplable; the protocol has no explicit branch for "navigate succeeds, every subsequent extension call on that domain is permission-denied." Recorded here under `deviations:` per task instruction rather than editing `panel-protocol.md`.

## deviations

- Protocol's Engines table (row: ChatGPT) carried the surface URL as `unknown — verify at first sample` with prior status "not loaded 2026-09-22; 403 to fetchers, extension navigation reverted." This pull resolves the URL to `https://chatgpt.com/` (navigation itself succeeds, is not a 403) but finds every subsequent extension action on that domain permission-denied, distinct from a plain-fetch 403 or a login wall. `panel-protocol.md` left untouched per task instruction; this finding recorded here only.
- Task instruction's two named fallback labels are `login required — not sampled` and `surface blocked — <reason>`. No login wall was observed (page content never rendered), so `login required` does not literally apply; used `surface blocked — <reason>` with the reason being extension site-permission denial, not a login wall.
- `screenshot description` requested by the task instruction for this fallback case: none could be captured — the screenshot action itself was the one denied by the extension permission system. No image exists to describe. This is noted rather than fabricated.
