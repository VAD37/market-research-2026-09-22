# Boily — "GEO 정비 전후 AI 검색 노출률 비교" (dental clinic GEO comparison, N=2) — the inline SVG chart extracted, with its text values

```yaml
source:          boily.co.kr (Korean GEO vendor guide page)
url_or_doc_id:   https://boily.co.kr/guide/geo-repair-case-2026-06
published:       2026-06 (URL slug; as recorded in the substitute)
pull_date:       2026-09-23
pull_method:     fetch (curl, HTTP 200, 53,077 bytes); the chart is an inline `<svg role="img">` element in the page HTML, saved as .svg
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor comparison, N=2, stated on the chart itself as "N=2 관찰(통제 실험 아님)" — as graded in the substitute
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Gemini, Perplexity (as in the substitute)
metric_kind:     visibility (mention rate over 100 fixed queries)
supersedes:      e-case-boily-dental-geo-comparison-2026-09-23.md (text complete; chart images not captured)
captured:        the one SVG chart (file + text nodes) and its figcaption; body text is in the substitute and not duplicated
```

## Verbatim

[image: docs/raw/img/e-case-boily-dental-geo-comparison-primary-2026-09-23/01-geo-ai.svg] — aria-label "GEO 정비 전후 AI 검색 노출률 비교(익명)"

Text nodes in the SVG: "AI 검색 노출률 — 정비 전 → 정비 후 (병원명 비공개)" · "영통OOO치과 · 정비함" · "11% → 27% (+16%p)" · "강남OOO치과 · 비교군(정비 안 함)" · "11% → 10% (제자리)" · "N=2 관찰(통제 실험 아님) · 인과 단정 아님 · 효과 보장 아님 · 같은 중립 측정으로 전후 비교"

Figcaption: "같은 11%에서 출발 — 정비한 영통OOO치과만 27%로, 정비 안 한 비교군은 제자리. (병원명 비공개)"

## Pull notes — mechanical only

- curl HTTP 200; the chart is inline SVG with `role="img"`, so the values are read from markup. Saved as `.svg` with an XML header; row in `docs/raw/img/INDEX.csv`. No wall; the bypass extension was not involved.
- The only other image reference in the HTML is a Facebook pixel; no raster chart on the page.
