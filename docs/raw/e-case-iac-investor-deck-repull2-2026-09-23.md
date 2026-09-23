# IAC Inc. — Q4'25 Investor Presentation, slide 7 image (re-pull, resolves chart-vs-callout note)

```yaml
source:          IAC Inc. (NASDAQ: IAC), filed via 8-K Exhibit 99.2
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1800227/000162828026004988/iacq42025earningscallpre007.jpg (accession 0001628280-26-004988, slide image 7 of 21)
published:       2026-02-03
pull_date:       2026-09-23
pull_method:     fetch (curl, contact User-Agent "Research contact research@example.org")
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — SEC 8-K exhibit, filed; same filing as e-case-iac-investor-deck-2026-02-03-2026-09-22.md, image component only
source_label:    filed
lane:            E
sub_market:      organic recommendation
engine:          Google Search (referral channel); Google AI Overviews (named on same slide)
metric_kind:     traffic
supersedes:      none — supplements e-case-iac-investor-deck-2026-02-03-2026-09-22.md (that pull's text extraction flattened this chart and could not reconcile the "50%" callout against the printed bar totals; this pull retrieves the chart as an image, which resolves it, see img transcription)
captured:        one slide image (slide 7 of 21, "Q4 Audience Trends"); accession folder also listed 20 further slide images (001-021, minus 007), not fetched — out of scope for this claim
```

## Verbatim

Not applicable — this file records an image pull. The image itself is filed as `docs/raw/img/e-case-iac-investor-deck-repull2-2026-09-23/01-slide7-q4-audience-trends-core-sessions.jpg`; its content is transcribed in `docs/raw/e-case-iac-investor-deck-repull2-2026-09-23-img-2026-09-23.md` per the image-pull pipeline (`plan.md` "Orchestration — image pulls, 2026-09-23").

[image: docs/raw/img/e-case-iac-investor-deck-repull2-2026-09-23/01-slide7-q4-audience-trends-core-sessions.jpg]

## Pull notes — mechanical only

- Accession folder `https://www.sec.gov/Archives/edgar/data/1800227/000162828026004988/` listed via `curl -A "Research contact research@example.org"`, HTTP 200. Folder holds slide images `iacq42025earningscallpre001.jpg` through `021.jpg`; slide 7 (index `007`) matches the "Q4 Audience Trends" slide cited in the prior pull's Verbatim section (same headline text, same footnote text).
- Image fetched directly by URL, HTTP 200, 92,662 bytes, no wall. Neighbor slides `006.jpg` (Q4 Digital Revenue/EBITDA) and `008.jpg` (Q4 Digital Revenue Growth breakdown) were also fetched to confirm slide-7 identification by position, then discarded — decorative to this claim, not saved to `img/`.
- Contact User-Agent used per SEC's fair-access policy: `Research contact research@example.org` (the literal string "research vadprimary@gmail.com" is not SEC-compliant per task brief; a real contact address/domain is required in the UA string).
