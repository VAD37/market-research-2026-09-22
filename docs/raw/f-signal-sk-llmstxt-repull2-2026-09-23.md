# llms.txt presence check — Estée Lauder, Ulta (re-pull 2)

```yaml
source:          esteelauder.com, ulta.com — direct fetch of /llms.txt
url_or_doc_id:   https://www.esteelauder.com/llms.txt ; https://www.ulta.com/llms.txt
published:       n/a — live endpoint check
pull_date:       2026-09-23
pull_method:     fetch (curl, browser user-agent) — Chrome extension unavailable this session, see Pull notes
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us endpoint check
source_label:    measured-by-us
lane:            F
sub_market:      n/a
engine:          n/a
metric_kind:     none
supersedes:      docs/raw/f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md
captured:        HTTP status and first bytes of response body only
prompt_set:      n/a
runs_n:          1 per domain
surface:         n/a — HTTP endpoint fetch, not an assistant surface
region:          n/a
```

## Verbatim

### https://www.esteelauder.com/llms.txt
HTTP 403 (Akamai). First lines of response body:
```
<HTML><HEAD>
<TITLE>Access Denied</TITLE>
</HEAD><BODY>
<H1>Access Denied</H1>
You don't have permission to access "http://www.esteelauder.com/llms.txt" on this server.
Reference #18.caad617.1790177880.2a26768
```
[note: Akamai bot-wall interstitial, not llms.txt content — same result class as the 2026-09-22 pull]

### https://www.ulta.com/llms.txt
HTTP 200, but body is an Akamai ESI waiting-room page, not the llms.txt file. First lines of response body:
```
<esi:debug/>
<esi:remove>
</esi:remove>
<html lang="en">
<head>
...
<title>ULTA.com :: Our Apologies</title>
```
[note: HTTP 200 masks an Akamai "waiting room" challenge page (`vpwaitingroom`); real llms.txt content not served — same result class as the 2026-09-22 pull, status code differs (was reported as a waiting-room page, now confirmed 200 wrapping that same page) but substance is unchanged]

## Pull notes — mechanical only

- Chrome browser extension (`ext`) was unavailable for this pull: `tabs_context_mcp` and `navigate` both returned "Browser extension is not connected" on three attempts (2026-09-23, spaced ~15s and ~45s apart). Fell back to `curl` with a Chrome-128 desktop User-Agent header, matching the assigning task's fallback allowance ("just fetch each /llms.txt").
- Both domains still return bot-wall/challenge content, not real llms.txt bodies. Ulta's HTTP status reads 200 (not a redirect/wait code) but the payload is the same Akamai waiting-room template family as before — no llms.txt substance to carry.
- Result: status unresolved, unchanged from prior pull. No figure carried.
