# Zendesk — /llms.txt presence check, re-pull (wall cleared)

```yaml
source:          measured-by-us — direct HTTP request to zendesk.com's /llms.txt path
url_or_doc_id:   https://www.zendesk.com/llms.txt
published:       n/a — live site check, not a dated publication
pull_date:       2026-09-23
pull_method:     fetch (curl, this session's Bash tool, browser User-Agent, no browser extension)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default for S12 — measured-by-us, output in raw/
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none — supplements f-signal-bs-S12-llms-txt-domains-2026-09-22.md, which recorded zendesk.com as access-blocked ("the `www.` host then refuses the TLS handshake to this client (curl exit code 35, SSL connect error) on every retry"), excluded from that file's 10-domain sample. This re-pull finds the block cleared.
captured:        full /llms.txt body (741,350 bytes)
prompt_set:      n/a | runs_n: 1 domain | surface: n/a (static file check) | region: n/a
```

## Verbatim

Method: `curl -s -o /dev/null -w "%{http_code} %{size_download} %{content_type}" -L -A "<browser UA>" "https://www.zendesk.com/llms.txt"`.

Result: **HTTP 200, 741,350 bytes, Content-Type text/plain.**

First lines of body:

> # Zendesk.com
> \> Deliver beautifully simple service with Zendesk AI Agents. Powering over 20,000 AI customers and counting
>
> # Home
> - [Zendesk: Transform Customer & Employee Service with AI Agents](https://www.zendesk.com/): Transform customer and employee service with Zendesk AI Agents—trusted by 200,000+ companies. Deliver fast, personalized support across chat, email, voice, and more.
>
> ## Blog
> - [Customer experience, support and sales blog | Zendesk](https://www.zendesk.com/blog/): The Zende[content continues, truncated at 500 bytes for this excerpt]

## Pull notes — mechanical only

- Prior pull (2026-09-22) recorded a TLS handshake failure (curl exit 35) on `www.zendesk.com` specifically, excluding zendesk.com from that pull's 10-domain B2B SaaS sample. This re-pull, same method, same UA style, succeeded on the first attempt with no handshake error — the block is not standing as of 2026-09-23. Per `plan.md` "Orchestration — paywall-bypass revision" caveat pattern and the repull-audit-2 caveat ("per-request, may revert"), this is recorded as a point-in-time result, not a permanent fix.
- File is large (741,350 bytes, a full site-page directory in llms.txt format) — only the opening lines are reproduced verbatim above per the file's own scope (presence/absence check, not full-content capture); the number itself (presence = yes, HTTP 200, genuine text/plain) is the finding.
