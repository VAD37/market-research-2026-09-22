# MVP mandate

Set by the user 2026-09-17, carried into this repo 2026-09-22. What must exist before a project is called done.

A research KILL verdict does not block a build the user has decided to do. Do not re-litigate a kill. Use the kill evidence as design input: it tells you what the product must NOT claim.

## What must exist per project when this is done

1. **A thing that runs.** `prototype/` — one command starts it, no account, no API key required for the demo path, no paid call. Works offline or with fixtures.
2. **A success vision, written first.** `docs/outcome/success-vision.md` — what winning looks like, before the sales page and before the review. Every downstream agent reads it. Concluding "the honest win is much smaller than the original ambition" is the most useful thing it can report.
3. **End-to-end user test.** A scripted fake user goes from landing on the product to getting the value, all the way through. Logged in `docs/execution/e2e-test.md` with actual command output pasted, not described.
4. **A sales page.** A single self-contained `site/index.html` that a stranger can read for 30 seconds and know:
   - what this is
   - what problem it solves
   - why it is different from the free/incumbent option (name the incumbent)
   - why you would need it
   - what value you get *right now*, with something to try on the page itself
5. **Outcome read.** `docs/outcome/` — what the demo proves, what it does not, what breaks at scale, and who exactly would pay.

## Hard constraints

- No account creation, no signups, no licence acceptance, no purchases, no paid API calls, no domain registration.
- Redact any token, key, OAuth value, email address or session identifier before writing anything into `raw/`.
- Never modify `C:\Users\vad\.claude\settings.json` or any global config. Test harnesses live in the project folder or the scratchpad.
- Other repos on this machine, and the predecessor repo `D:\researchs\market-research\`, are **read-only source material**.
- Agents write only inside their own project folder. Agents never run git.
- Authorized testing on owned infrastructure only. No third-party targeting.
- Never print a token, account id, zone id or tunnel secret — not in logs, not in errors, not in a dry-run. Mask to the last 4 characters. **The response body is the half that gets forgotten** — mask what comes back, not only what you send.

## Honesty rule for the sales page

The page is a sales page, not a lie. Every capability claim on it must be backed by something the prototype actually does, demonstrated in `docs/execution/e2e-test.md`. Roadmap items are labeled as roadmap. No fake logos, no fake testimonials, no invented customer counts, no fabricated benchmark numbers. A number on the page is either measured by the prototype (label it) or cited from `raw/` (label it). This is not optional — a page that fails it gets rejected in review.

A "what it does not do" section is not a weakness on the page. It is the product position.

## Stack constraints for `site/index.html`

Single file. Inline CSS and JS. No build step. No external fetch at page load — the demo on the page runs on embedded fixture data. It must be self-contained and must render with no network.

## Stack constraints for `prototype/`

Python 3 stdlib-first, or plain Node, or static HTML+JS. Third-party deps only when they are already installed on this machine — check before you depend on something. If you add a dep, pin it in `prototype/requirements.txt` and state the install command in the README. Prototype code is throwaway-grade but must RUN.

## Vision review is mandatory, not optional

A sales page is not accepted on source-read alone. The review agent loads it in a real browser at desktop AND mobile width, screenshots both, and looks at them. Findings about layout, hierarchy, legibility and whether the 30-second read actually lands come from the screenshot, not from reading the HTML.

Review widths: **1440x900 desktop** and **390x844 mobile**. Screenshot both. Scroll the whole page — a screenshot of the hero only is not a review. Judge from the image: hierarchy, legibility, whether the 30-second read lands, whether the demo is obviously interactive, whether anything overflows or collides at mobile width.

**Serve the page over HTTP, do not rely on `file://`** — the Chrome extension may not have local-file access. From the project's `site/` folder:

    python -m http.server 88NN

One distinct port per project so two agents never collide. Kill the server when done.

Browser paths, both verified working 2026-09-17:

    mcp__claude-in-chrome__tabs_context_mcp  { createIfEmpty: true }   call this FIRST
    mcp__claude-in-chrome__navigate          { tabId, url }
    mcp__claude-in-chrome__resize_window     { tabId, width, height }
    mcp__claude-in-chrome__computer          { tabId, action:"screenshot" }
    mcp__claude-in-chrome__computer          { tabId, action:"scroll", coordinate, scroll_direction }
    mcp__claude-in-chrome__read_page         { tabId }
    mcp__claude-in-chrome__tabs_close_mcp    { tabId }   clean up what you opened

Playwright MCP is the fallback and handles `file://` without fuss: `mcp__MCP_DOCKER__browser_navigate / browser_resize / browser_take_screenshot / browser_close`.

The browser is a single shared resource: **only one browser-driving agent runs at a time.** The orchestrator serializes them. Do not assume you have it unless your brief says so.

## Every review phase ends with a self-interrogation section

Verbatim heading:

    ## Is this enough? What else can we do to improve it?

Under it: an honest verdict on whether the thing is ready to put in front of a buyer, then a ranked list of concrete improvements — each with the effort it costs and what it would change for the user. No filler entries. If the answer is "not enough", say so plainly and say what the single most valuable next build is.

## Review lessons that cost real time to learn

Each of these was found by running something, in the predecessor repo. They are one-line rules now.

- Check every write in every `except` block. A safety guard on the happy path but not the exception path is the bug that ships.
- Read exit codes on the command, not on the pipe.
- Pre-register the rounding rule. Python rounds half-to-even; a spec written half-up disagrees, and it surfaces late.
- `wc -l` over-counts CSV rows with embedded newlines. Parse, don't count lines.
- Fix the code to match the spec, never the spec to match the code.

## Hosting

Public hosting is authorized in principle and **nothing is wired up in this repo.** The predecessor repo holds a working Cloudflare Tunnel + Traefik rig under `infra/`; copy it only when there is a page worth publishing. No agent deploys publicly — local serve, and a main-thread publish.

Credentials live in a gitignored `.env` at the repo root and must stay that way. The user's account runs tunnels belonging to other work, one of them a live clinic system. **Nothing may touch them.** Create our own; act only on what we created.

## Toolchain — measured 2026-09-17, re-verify before depending on it

- Python **3.9.25** (uv shim). No `match`, no `X | Y` annotations without `from __future__ import annotations`.
- Installed pip packages, complete: cffi, charset-normalizer, cryptography, pdfminer.six, pypdf, setuptools, typing_extensions, pip. **No requests, no pandas, no numpy, no torch.** Stdlib first. A `uv` venv install is allowed and free if genuinely needed, but the default demo path must run on bare stdlib with zero install.
- Node **v23.11.1**, Docker **29.6.2**.
