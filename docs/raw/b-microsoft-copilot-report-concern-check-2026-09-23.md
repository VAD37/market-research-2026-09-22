# Microsoft — Copilot / Bing "report a concern" channel, access check

```yaml
source:          Microsoft (microsoft.com concern portal; support.microsoft.com)
url_or_doc_id:   https://www.microsoft.com/en-us/concern/bing ; https://support.microsoft.com/en-us/topic/copilot-in-bing-our-approach-to-responsible-ai-45b5eae8-7466-43e1-ae98-b48f8ff8fd44
published:       n/a
pull_date:       2026-09-23
pull_method:     fetch (curl)
pull_purpose:    evidence about a number (existence of a correction channel; result: no server-rendered text reached)
tier:            3
tier_reason:     platform primary; only the shell of the portal and a retirement notice were captured
source_label:    company-stated
lane:            B
sub_market:      n/a
engine:          Microsoft Copilot, Bing
metric_kind:     none
supersedes:      none
captured:        portal shell metadata; support-article retirement notice
```

## Verbatim

microsoft.com/en-us/concern/bing (HTTP 200, 1,051 bytes; redirected to `/digitalsafety/report-a-concern/`):
> `<meta name="description" content="Microsoft Digital Trust & Safety Customer Concerns Portal"/>` — single-page application; no form text served to curl.

support.microsoft.com "Copilot in Bing: our approach to responsible AI" (HTTP 200):
> This article has been retired — The content of the article you were trying to reach is no longer available. Try a new search below in Need more help.

## What the repository already holds on this point

- `docs/raw/b-eu-microsoft-dsa-bing-2026-09-22.md`: Microsoft's Bing DSA page names DigitalServicesAct@microsoft.com as the Article 11 point of contact for authorities and links the Microsoft Ad Library as the EU advertising repository; the page "does not separately name 'Copilot' anywhere in its text".

Copilot-specific channel for a business to report an inaccurate answer about itself: **unknown — checked microsoft.com/en-us/concern/bing (SPA, no text), support.microsoft.com (article retired) 2026-09-23.**

## Pull notes — mechanical only

- No form opened or submitted. No Chrome extension or Playwright available to render the portal.
