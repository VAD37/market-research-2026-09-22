# llms.txt presence check — GEICO, GNC (re-pull 2)

```yaml
source:          geico.com, gnc.com — direct fetch of /llms.txt
url_or_doc_id:   https://www.geico.com/llms.txt ; https://www.gnc.com/llms.txt
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
supersedes:      docs/raw/f-signal-hr-S12-llmstxt-sample-2026-09-22.md
captured:        HTTP status and first bytes of response body only
prompt_set:      n/a
runs_n:          1 per domain
surface:         n/a — HTTP endpoint fetch, not an assistant surface
region:          n/a
```

## Verbatim

### https://www.geico.com/llms.txt
HTTP 403. First lines of response body:
```
<html style="height:100%"><head><META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW"><meta name="format-detection" content="telephone=no"><meta name="viewport" content="initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"></head><body style="margin:0px;height:100%"><iframe id=
```
[note: bot-wall interstitial, not llms.txt content — same result class as the 2026-09-22 pull]

### https://www.gnc.com/llms.txt
HTTP 307, body served (PerimeterX challenge page). First lines of response body:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="px-captcha">
    <title>Access to this page has been denied</title>
```
[note: PerimeterX px-captcha wall, not llms.txt content — same result class as the 2026-09-22 pull]

## Pull notes — mechanical only

- Chrome browser extension (`ext`) was unavailable for this pull: `tabs_context_mcp` and `navigate` both returned "Browser extension is not connected" on three attempts (2026-09-23, spaced ~15s and ~45s apart). Fell back to `curl` with a Chrome-128 desktop User-Agent header, matching the assigning task's fallback allowance ("just fetch each /llms.txt").
- Both domains return the same wall class as the 2026-09-22 pull (bot wall / CAPTCHA interstitial), unchanged under a browser-like UA. No login prompt, no registration form — plain bot-detection wall, out of scope for the paywall-bypass extension.
- Result: status unresolved, unchanged from prior pull. No figure carried.
