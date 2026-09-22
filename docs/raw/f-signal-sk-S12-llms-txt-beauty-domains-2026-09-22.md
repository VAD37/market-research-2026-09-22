# Measured-by-us — /llms.txt on five public beauty brand domains

```yaml
source:          our own HTTP checks against five beauty brand domains
url_or_doc_id:   https://www.elfbeauty.com/llms.txt; https://www.esteelauder.com/llms.txt; https://www.sephora.com/llms.txt; https://www.ulta.com/llms.txt; https://www.lorealparisusa.com/llms.txt
published:       undated — live domain checks
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header, redirects followed)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us per demand-signals.md S12
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          n/a — artifact readable by any crawler naming itself, not engine-specific
metric_kind:     none
supersedes:      none
captured:        HTTP status code and first ~1,500 characters of response body per domain; full bodies not captured
```

<!-- measured-by-us pulls add these four lines: -->
prompt_set: n/a — not a panel run
runs_n: 5 domains checked
surface: n/a — HTTP artifact check, not a chat surface
region: n/a — single unauthenticated check per domain, no region parameter set

## Query — verbatim

`curl -s -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" https://<domain>/llms.txt` run against each of five domains, redirects followed. An earlier pass without the browser User-Agent and without `-L` was also run and is recorded below where it produced a different status.

## Verbatim — results table

| Domain | Brand | Status (no UA, no -L) | Status (browser UA, -L) | Body first bytes |
|---|---|---|---|---|
| www.elfbeauty.com | e.l.f. Beauty (NYSE: ELF) | 200 | 200 | `# e.l.f. Beauty` — genuine llms.txt: markdown index of "Core Documentation" pages (Ethos & Values, Impact Report, Innovation & Community) |
| www.esteelauder.com | The Estée Lauder Companies (NYSE: EL) | 200 | 403 | Akamai "Access Denied" HTML page, `Reference #18.92813417.1790092663.11da668c` — the unauthenticated no-UA check returned 200 status text but the body was itself a 404-style "Not Found" HTML page (`<title>404 Not Found</title>`); the browser-UA check was blocked outright at 403 |
| www.sephora.com | Sephora (LVMH) | 404 | 200 | `# Sephora` — genuine llms.txt: markdown index headed "Notes for LLMs", listing shopping categories (Makeup, Skincare, Fragrance, Hair, Bath & Body) |
| www.ulta.com | Ulta Beauty (NASDAQ: ULTA) | 403 | 200 | Not a genuine llms.txt: Akamai ESI/waiting-room HTML template, `<title>ULTA.com :: Our Apologies</title>`, `<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">` — a generic soft-error/waiting-room page served at HTTP 200 for this and (per spot-check) other nonexistent paths, not brand-specific llms.txt content |
| www.lorealparisusa.com | L'Oréal Paris (Euronext Paris: OR) | 404 | 200 | `# LLMs.txt - Master File`, `Generated: 2025-10-05`, `Owner: L'Oreal Paris`, `Contact: DMCA@loreal.com` — genuine llms.txt: explicit crawler policy block (`User-agent: *` / `Allow: /`), licensing terms (`Attribution: required`, `Training: disallow`, `Derivative-Works: allow`), rate limits (`Crawl-Delay: 5`, `Max-Request-Rate: 120/hour`), and a named agent-specific policy section beginning `User-agent: ChatGPT-User` |

Tally: 3 of 5 domains (elfbeauty.com, sephora.com, lorealparisusa.com) serve a genuine, brand-authored llms.txt artifact under the browser-UA check. 1 of 5 (ulta.com) returns HTTP 200 to the path but the body is a generic error/waiting-room template, not an llms.txt artifact — recorded as **not present** despite the 200 status. 1 of 5 (esteelauder.com) is blocked (403 Akamai, or a soft-404 body depending on request headers) — recorded as **not present, access-blocked**.

## Pull notes — mechanical only

- Two request profiles were run per domain because the first (no custom User-Agent, no redirect-following) produced inconsistent status codes against several of these Akamai/Vercel/Cloudflare-fronted domains compared to a standard browser User-Agent with redirects followed; both are recorded in the table rather than choosing one silently.
- `www.ulta.com`'s 200 status is a false positive for artifact presence: the response body is a generic WAF/waiting-room page (title "Our Apologies") that a spot-check suggests is served for other non-existent paths on the same domain too, not confirmed to be llms.txt-specific. Recorded as `none` for adoption purposes despite the 200.
- No login wall or paywall encountered on any of the five domains. No JavaScript rendering was needed — all five domains served their `/llms.txt` response (or the substitute page) as static HTTP content.
- Additional domains spot-checked in the same style, not part of the five-domain sample but consistent with the pattern above (recorded here for transparency, not counted in the S12 tally): `www.glossier.com` (200, genuine "Agent Instructions — Glossier" llms.txt), `www.rarebeauty.com` (200, genuine "Agent Instructions — Rare Beauty"), `www.maccosmetics.com` (200, genuine "Agent Instructions — MAC Cosmetics"), `www.drunkelephant.com` (410 Gone), `www.charlottetilbury.com` (200, generic SPA HTML shell, not llms.txt), `theordinary.com` (404).
