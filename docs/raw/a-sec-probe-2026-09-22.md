# SEC EDGAR — access probe (blocked)

```yaml
source:          SEC EDGAR (sec.gov)
url_or_doc_id:   https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=CHGA&type=10-K&dateb=&owner=include&count=10
published:       n/a — access probe, not a filing pull
pull_date:       2026-09-22
pull_method:     fetch (curl, User-Agent: "market-research-2026-09-22 research-agent contact@example.invalid" — browser-style UA naming contact per SEC fair-access policy)
pull_purpose:    evidence about category noise (access blocker, not a number)
tier:            7
tier_reason:     probe record of a blocked access attempt, not a source of any number — tiered at the discard floor per trust-rubric.md; kept only to document the block and the deferral
source_label:    n/a — no filing content retrieved
lane:            A
sub_market:      n/a
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        response headers in full; response body first ~4400 characters (of 7747 total)
```

## Verbatim

Request timestamp (UTC): 2026-09-22 16:28:55 (Date header, server-supplied) / 2026-09-22 16:28:56 (client date -u at completion)

HTTP status: `503 Service Unavailable`

Response headers, verbatim:

```
HTTP/1.1 503 Service Unavailable
Content-Type: text/html
ETag: "ea3469ed6f56095717b550884a6a0143:1765825277.092986"
Last-Modified: Mon, 15 Dec 2025 19:01:17 GMT
Server: AkamaiNetStorage
Date: Tue, 22 Sep 2026 16:28:55 GMT
Connection: close
Cache-Control: max-age=0, no-cache, no-store
```

Response body excerpt, verbatim (title tag and core message block; full body was 7747 bytes, an Akamai-served static "apology" page, not EDGAR application content):

```html
<title>SEC.gov | File Unavailable</title>
```

```html
<div id="main-content" class="row">
    <div class="small-8 small-offset-2 columns" style="padding: 25px 0px 150px 0px;">
        <h1 class="goodbye text-center">This page is temporarily unavailable.</h1><hr/>
        <p>SEC.gov is undergoing maintenance. During this time, webforms will not be available.</p>
        <p>Comments regarding Commission and SRO rulemaking should be submitted via email to rule-comments@sec.gov during this time.</p>
    </div>
```

Also present in body (page-search-form label text, concatenated with an unrelated apology fragment by the page's own markup — reproduced as served):

```html
<label class="overlabel" for="global-search-Please check back again soon. We regret any inconvenience, and we thank you for your interest in the SEC website.box">Search SEC.gov</label>
```

Server identity: `Server: AkamaiNetStorage` — response served from Akamai edge/CDN infrastructure, not directly from an EDGAR application server.

`result: blocked — re-pull deferred`

## Pull notes — mechanical only

- Single fetch made, per task instruction (probe-gated, no retry).
- Tool: `curl` via Bash, with explicit `-A` (User-Agent) flag naming this agent and a contact address, per SEC fair-access guidance. Not a bare-default-UA request.
- No redirect occurred; the 503 apology page was served directly at the requested URL.
- No other host or endpoint tried this pull, per task instruction (stop after one blocked probe).
- No browser or browser-extension tool used for this pull.
