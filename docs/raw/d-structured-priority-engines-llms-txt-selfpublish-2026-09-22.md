# Measured-by-us — /llms.txt on the six priority-1/2 engines' own developer/marketing domains

```yaml
source:          our own HTTP checks against six engine-operator domains
url_or_doc_id:   https://developers.openai.com/llms.txt ; https://docs.anthropic.com/llms.txt ; https://ai.google.dev/gemini-api/docs/llms.txt ; https://docs.perplexity.ai/llms.txt ; https://perplexity.ai/llms.txt ; https://about.ads.microsoft.com/llms.txt ; https://learn.microsoft.com/llms.txt ; https://advertising.amazon.com/llms.txt ; https://developer.amazon.com/llms.txt
published:       undated — live domain checks
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header, redirects followed)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us per demand-signals.md S12, applied here to the engine operators themselves rather than to brand-sample domains
source_label:    measured-by-us
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Perplexity, Microsoft Copilot (Microsoft Advertising), Amazon
metric_kind:     none
supersedes:      none
captured:        HTTP status code and first ~400 bytes of response body per URL; full bodies not captured
```

<!-- measured-by-us pulls add these four lines: -->
prompt_set: n/a — not a panel run
runs_n: 9 URLs checked across 6 engine operators
surface: n/a — HTTP artefact check, not a chat surface
region: n/a — single unauthenticated check per URL, no region parameter set

## Query — verbatim

`curl -s -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" <url>` run against each URL below, redirects followed, headers and first bytes of body inspected per hit.

## Verbatim — results table

| Engine operator | URL checked | HTTP code | Result |
|---|---|---|---|
| OpenAI (ChatGPT) | `developers.openai.com/llms.txt` | 200 | Genuine, substantial. `Content-Length: 5861`, `Content-Disposition: inline; filename="llms.txt"`, `Last-Modified: Tue, 22 Sep 2026 15:37:16 GMT`. Opens: "# OpenAI Developers / > Complete documentation hub for OpenAI API, Ads, Plugins, Workspace Agents, Codex, Agentic Commerce, the developer blog, Cookbook, learning resources, and learning tracks." |
| Anthropic (Claude) | `docs.anthropic.com/llms.txt` | 200 | Genuine, very large. `Content-Length` not captured (body truncated at ~1,500 chars for this pull); opens as a full index of the Claude Developer Platform docs across 12 languages, "634 pages" for English alone per the file's own header. Served from `privacy.claude.com`/`platform.claude.com` infrastructure, `Server: cloudflare`, `Last-modified: Mon, 21 Sep 2026 10:42:52 GMT` |
| Google (Gemini) | `ai.google.dev/gemini-api/docs/llms.txt` | 302 | **Inconclusive — redirects to an OAuth login flow**: `location: https://ai.google.dev/oauth2authorize?return_url=...&scopes=...developerprofiles...`. This URL is the one the llmstxt.org proposal itself names as Gemini's self-published llms.txt (see `d-structured-llmstxt-org-spec-2026-09-22.md`); as checked today it does not resolve to a public file without authentication. Recorded as `unknown — checked https://ai.google.dev/gemini-api/docs/llms.txt 2026-09-22, redirects to Google OAuth sign-in` rather than as a confirmed absence or presence |
| Perplexity | `docs.perplexity.ai/llms.txt` | 200 | Genuine. Served via Mintlify (`X-Matched-Path: /_sites/[subdomain]/llms.txt`, `Server: Vercel`). Opens: "# Perplexity / > Perplexity API documentation for building with the Agent API, the default for web-grounded AI and multi-provider applications, plus Search, Embeddings, and Sonar APIs." A companion `docs.perplexity.ai/llms-full.txt` path also found via search (not independently status-checked in this pull) |
| Perplexity | `perplexity.ai/llms.txt` (marketing root domain, distinct from the docs subdomain above) | 403 | Blocked at the root consumer-facing domain — not present/accessible there, distinct result from the docs subdomain |
| Microsoft (Copilot / Microsoft Advertising) | `about.ads.microsoft.com/llms.txt` | 200 | Genuine. `Content-Length: 10604`, `Last-Modified: Tue, 20 Jan 2026 15:21:35 GMT`. Opens: "# about.ads.microsoft.com / > Microsoft Advertising is building a new world of advertising possibilities to empower growth for all." |
| Microsoft | `learn.microsoft.com/llms.txt` | 404 | Absent at this second, separate Microsoft documentation domain |
| Amazon | `developer.amazon.com/llms.txt` | 200 | Genuine, large (`Content-Length: 69083`). Opens: "# Amazon Developer Portal Documentation / ## Instructions for LLMs / This file contains comprehensive documentation for Amazon's developer ecosystem..." |
| Amazon | `advertising.amazon.com/llms.txt` | 404 | Absent at the advertising-specific Amazon domain (separate from the general developer portal above) |

**Tally, one artefact per engine operator, using the most favourable domain checked for each:** 5 of 6 priority engines (OpenAI, Anthropic, Perplexity, Microsoft, Amazon) serve a genuine, substantial llms.txt on at least one of their own primary developer/marketing domains. Google's named URL (per the llmstxt.org proposal's own citation) is login-gated as checked today and could not be confirmed either way. Every operator that does serve one serves it on a **developer-documentation or advertising-marketing** domain, not on the consumer chat-product domain itself (no check was made of `chatgpt.com/llms.txt`, `claude.ai/llms.txt`, `gemini.google.com/llms.txt`, or `copilot.microsoft.com/llms.txt` in this pull — out of scope for this cluster's own-domain check, which followed the URLs the llmstxt.org proposal and each operator's own developer/ads portal actually name).

## Pull notes — mechanical only

- All nine URLs resolved via `curl -L`; no browser extension needed except where noted (none needed — all are plain HTTP/HTTPS, no JS rendering wall).
- This measures **self-publication by the engine operators**, i.e. these companies acting as *publishers* of their own developer documentation — it is evidence of adoption of the artefact by AI labs as content owners, not evidence of whether the same companies' AI assistants *read* llms.txt files published by third-party brand websites when crawling or answering. That question is separately addressed by the measured-behaviour study in `d-structured-arxiv-borysenko-http-fingerprints-2026-09-22.md` (controlled test: none of ChatGPT, Claude, Google Gemini, Google NotebookLM, MistralAI or Perplexity requested llms.txt from a third-party test endpoint) and by the explicit platform-primary statement in `d-structured-google-ai-optimization-guide-2026-09-22.md` (Google: "Google Search itself doesn't use them... Google Search ignores them").
- The OpenAI and Amazon files are self-described as machine-generated documentation indexes ("Instructions for LLMs" heading on Amazon's), not brand-marketing content — both are structured the way the llms.txt spec itself recommends (H1 + blockquote + linked sections).
- Anthropic's file is unusually large (per its own header, 634 English-language pages indexed) and multi-lingual (12 languages listed) — the largest of the five confirmed files by page-count claim, though `Content-Length` in bytes was not captured for direct byte-size comparison against OpenAI's 5,861 and Amazon's 69,083.
