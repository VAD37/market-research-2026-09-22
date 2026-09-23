# Yext — Scout product pages in French and Italian (localised vendor listings), and locale coverage from the sitemap

```yaml
source:          Yext, Inc. (yext.com)
url_or_doc_id:   https://www.yext.com/fr/scout ; https://www.yext.com/it/scout ; https://www.yext.com/sitemap1.xml (via https://www.yext.com/sitemap.xml index, lastmod 2026-09-22T07:10:47-04:00)
published:       undated — no date on page
pull_date:       2026-09-23
pull_method:     fetch (curl)
pull_purpose:    evidence about a number (S2 vendor listing in a local language — existence only; no customer count on these pages)
tier:            3
tier_reason:     vendor's own product page — reliable on existence, biased on framing (table default 3)
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          "recherche basée sur l'IA" / "ricerca tramite IA" — engines not named on the captured text
metric_kind:     none
supersedes:      none (English Scout page is docs/raw/a-yext-scout-product-2026-09-22.md)
captured:        page title, H1 and opening navigation blurbs verbatim; sitemap locale list for /scout
```

## Verbatim — /fr/scout

> Title: "Yext Scout | Yext" — H1: "Yext Scout"
> "Plateforme — Explorez la plateforme de marketing agentique enterprise de Yext — Scout — Surveillez votre visibilité dans la recherche basée sur l'IA et suivez vos concurrents en temps réel — Listings — Gérez et optimisez les informations de vos établissements partout sur le web"

## Verbatim — /it/scout

> Title: "Yext Scout | Yext" — H1: "Yext Scout"
> "Piattaforma — Scopri la piattaforma di marketing agentico per grandi aziende di Yext — Scout — Monitora la visibilità nella ricerca tramite IA e tieni traccia della concorrenza in tempo reale. — Listings — Gestisci e ottimizza le informazioni sulla tua posizione in tutto il web."

## Sitemap — locale paths for /scout

`<loc>` entries matching `https://www.yext.com/<xx>/scout`: `/de/scout`, `/fr/scout`, `/it/scout`. No `/es/scout`, `/nl/scout` or `/en-gb/scout` entry in sitemap1.xml.

## Pull notes — mechanical only

- Both pages HTTP 200 (186 KB and 178 KB); only the title, H1 and the first navigation blurbs were extracted. No customer names, counts or prices on the extracted text.
- sitemap.xml is an index pointing to a single sitemap1.xml (3.5 MB); the locale check is a string match on that file.
