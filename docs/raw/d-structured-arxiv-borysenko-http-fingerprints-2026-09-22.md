# arXiv 2604.02544v2 — Developer Experience with AI Coding Agents: HTTP Behavioral Signatures in Documentation Portals

```yaml
source:          arXiv preprint, author Oleksii Borysenko
url_or_doc_id:   https://arxiv.org/abs/2604.02544v2 ; PDF https://arxiv.org/pdf/2604.02544v2 ; companion data https://github.com/oborys/AI-Agents-HTTP-level-behaviour
published:       2026-04-02 (v1); updated 2026-07-24 (v2, the version pulled)
pull_date:       2026-09-22
pull_method:     fetch (arXiv API for metadata; arxiv.org/html/2604.02544v2 for full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     academic table, "preprint with code and prompt set" — anonymized raw HTTP logs published in a companion GitHub repository (`github.com/oborys/AI-Agents-HTTP-level-behaviour`); single-author, not peer-reviewed, no independent replication found
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT (OpenAI), Claude (Anthropic), Google Gemini, Google NotebookLM, MistralAI, Perplexity — plus 9 AI coding agents (Aider, Antigravity, Claude Code, Cline, Cursor, Junie, OpenCode, GitHub Copilot VS Code agent mode, Windsurf), no model version named for any assistant
metric_kind:     visibility
supersedes:      none
captured:        full text (HTML rendering of the paper, tables and body prose; figures and raw per-request JSON listings partially captured, see pull notes)
```

## Verbatim

### Abstract

"The rapid adoption of AI coding agents and AI assistant web services is fundamentally changing how developers discover, consume, and interact with technical documentation. This paper studies that transformation across three interconnected dimensions: documentation accessibility, content analytics, and feedback systems. We present an empirical study of HTTP request fingerprints from nine AI coding agents (Aider, Antigravity, Claude Code, Cline, Cursor, Junie, OpenCode, GitHub Copilot (VS Code agent mode), and Windsurf) and six AI assistant services (ChatGPT, Claude, Google Gemini, Google NotebookLM, MistralAI, and Perplexity) accessing a live developer documentation endpoint, revealing identifiable behavioral signatures in HTTP runtime environments, pre-fetch strategies, User-Agent strings, and header patterns. Our study shows that AI agent access compresses multi-page navigation into a single or two requests, making traditional engagement metrics — session depth, time-on-page, click path, and bounce rate — unreliable indicators of actual documentation consumption. We discuss practical adaptations for developer portal teams, including tokenomics-aware documentation design, adoption of emerging machine-readable standards (AGENTS.md, llms.txt, skill.md, agent-permissions.json), MCP server-based feedback channels, and analytics instrumentation for AI referral traffic."

### 3.3 Endpoint and Experimental Environment

"Measurements used a purpose-built, publicly accessible developer documentation endpoint implemented with Node.js and Express. The endpoint served developer-oriented content and API documentation and exposed robots.txt (permitting crawlers) and llms.txt. This controlled environment allowed the same URL, content, and discovery files to be presented to every tested tool. The endpoint did not require authentication and did not rely on client-side rendering. The robots.txt file permitted all user agents to access the portal except the /guide path..."

"Each tool was tested in three independent trials during February–March 2026. Trials were conducted from the same local network and from external networks. All inbound requests were recorded exclusively by server-side Express middleware. For each request, the middleware captured the HTTP method and version, requested URL, complete header set, User-Agent string, client IP address. No client-side JavaScript instrumentation was used..."

"AI assistant services were tested by submitting the same prompt and URL through their chat interfaces."

### Table 1 — HTTP request fingerprints of AI coding agents (excerpt, columns: Agent, HTTP Runtime, Pre-fetch Behaviour, User-Agent, Header Signals Accept/Sec-Fetch-*)

Aider — Headless Chromium (Playwright) — On-demand GET — `...Aider/0.86.2 +https://aider.chat/` — Accept ✓, Sec-Fetch-* ✓
Antigravity — Go net/http — HEAD probe → GET — `Go-http-client/2.0` — Accept —, Sec-Fetch-* —
Claude Code — Node.js / Axios — On-demand GET — `axios/1.8.4` — Accept ✓, Sec-Fetch-* —
Cline — curl — GET + OpenAPI/Swagger sweep — `curl/8.4.0` — Accept ✓, Sec-Fetch-* —
Cursor — Node.js / got — HEAD probe → GET — `got (https://...)` — [remaining agents: Junie, OpenCode, GitHub Copilot VS Code agent mode, Windsurf — full row detail not captured beyond the stability table below]

### Table 2 — HTTP request fingerprints of six AI assistant web services, "observed when a URL was shared in the chat interface (server-side fetch)"

"Assistants are listed alphabetically. ✓ = header present; — = absent. [footnote a] Full User-Agent strings are available in the accompanying session data. [footnote b] MistralAI issues two distinct requests: a lightweight robot probe and a separate browser-mode fetch."

| Assistant | HTTP Runtime | Pre-fetch Behaviour | User-Agent | Accept | Sec-Fetch-* |
|---|---|---|---|---|---|
| ChatGPT | Custom HTTP (Envoy) | On-demand GET | `Mozilla/5.0 AppleWebKit/537.36 (…; ChatGPT-User/1.0; +https://openai.com/bot)` | ✓ | — |
| Claude | Custom HTTP client | Parallel GET /robots.txt + / (separate IPs) | `Mozilla/5.0 AppleWebKit/537.36 (…; Claude-User/1.0; +Claude-User@anthropic.com)` | ✓ | — |
| Google Gemini | Custom HTTP client | On-demand GET | `Google` | ✓ | — |
| Google NotebookLM | Custom HTTP client | On-demand GET | `Google-NotebookLM` | — | — |
| MistralAI | Custom HTTP + Headless Chromium | robots.txt probe; browser-mode GET / | `MistralAI-User` / `Mozilla/5.0 AppleWebKit/537.36 (…; MistralAI-User/1.0; +https://docs.mistral.ai/robots)` | ✓ | ✓ |
| Perplexity | Custom HTTP client | On-demand GET | (User-Agent string truncated in this extraction pass, see pull notes) | — | (not fully captured) |

### Table 3 — trial-level stability of observed HTTP fingerprints (excerpt, robots.txt / llms.txt columns)

"Every tool was tested in three independent trials (T1–T3). "Same" indicates that the attribute was unchanged across all trials."

For the six AI assistant services: "ChatGPT T1–T3 Same Same Same No No None ... Claude T1–T3 Same Same Same Yes No None Google Gemini T1–T3 Same Same Same No No None Google NotebookLM T1–T3 Same Same Same No No None MistralAI T1–T3 Same Same Same Yes No None Perplexity T1–T3 Same Same Same No No None"

"Table 3 summarizes the stability assessment. **No tool requested llms.txt**; access to robots.txt occurred only for Claude and MistralAI. All recorded User-Agent strings, header sets, and pre-fetch behaviors were unchanged across the three trials for each tool. Request counts were also stable..."

Summary row from the measured-signals discussion: "Measured Discovery-file access: No robots.txt or llms.txt requests observed [for coding agents]; robots.txt requested by Claude and MistralAI; **no llms.txt requests observed** [for AI assistant services]."

### 5.3 Implication: Documentation Standards for AI Discovery

"Documentation platforms are introducing machine-readable standards that go beyond traditional sitemaps and robots.txt. The llms.txt specification acts as a directory listing all documentation pages with descriptions so that AI agents know where to find information, while skill.md files provide structured capability summaries... Together, these emerging standards form a layered governance stack: llms.txt guides content discovery, skill.md describes product capabilities, and agent-permissions.json governs how AI agents may interact with web resources."

### Data Availability

"The HTTP fingerprint data reported in this work were collected from a purpose-built developer documentation endpoint operated by the authors. The endpoint served developer-oriented content and was configured with both robots.txt and llms.txt files to approximate the conditions of a production documentation portal. The anonymized raw HTTP logs are available in the companion repository: https://github.com/oborys/AI-Agents-HTTP-level-behaviour."

## Pull notes — mechanical only

- Retrieved via arXiv API (`export.arxiv.org/api/query`, search `abs:"llms.txt"`) for discovery and metadata, then the full paper text via `arxiv.org/html/2604.02544v2` (arXiv's native HTML rendering), tag-stripped with `sed` for verbatim text extraction. PDF not separately parsed. Some table cells (full remaining agent rows in Table 1; the Perplexity User-Agent string and Sec-Fetch-* value in Table 2) were not fully captured by this extraction pass and are marked incomplete above — the load-bearing llms.txt/robots.txt finding (Table 3 and its prose summary) was captured in full and is unambiguous.
- **This is the strongest evidence found in this cluster for the question "does the engine read llms.txt"**: a controlled, single-site, 3-trial, dated (February–March 2026) HTTP-fingerprinting study finds **zero llms.txt requests across all six AI assistant services tested (ChatGPT, Claude, Google Gemini, Google NotebookLM, MistralAI, Perplexity)** and all nine AI coding agents, despite the test endpoint serving a valid llms.txt file throughout. robots.txt, by contrast, was fetched by 2 of 6 assistant services (Claude, MistralAI).
- Scope limits stated by the author and carried here: single controlled endpoint (n=1 site), assistant services tested via their consumer chat interfaces by pasting a URL (server-side fetch triggered by the assistant, not a live open-web search/citation flow), no model version disclosed for any of the six assistants, sample "does not claim statistical representativeness of all AI coding products." Copilot and Amazon (Rufus/Alexa) are not covered by this paper — GitHub Copilot (VS Code agent mode) is tested as a *coding agent*, distinct from Microsoft Copilot the priority-2 chat assistant named in this repo's engine matrix.
- Single-author preprint (Oleksii Borysenko), `cs.SE` primary category, no peer-review venue stated on the arXiv page, no independent replication found. Data/code published (raw HTTP logs, companion GitHub repo) — this is what keeps the tier at 4 rather than 5 per `trust-rubric.md`'s academic table ("preprint with code and prompt set").
- Recorded verbatim, not requested or reproduced: no payload or exploit content; this paper does not describe or test prompt injection, and observing that a documentation endpoint was fetched is a passive server-log measurement of publicly available AI assistant behaviour against infrastructure the paper's own author controls — consistent with this task's Lane D constraint (research into manipulation/adoption evidence, not execution against a third party).
