# Boily — two-dental-clinic GEO comparison (treated 11% → 27%, untreated 11% → 10%)

```yaml
source:          Boily (boily.co.kr), Korean hospital AI-search measurement and GEO service
url_or_doc_id:   https://boily.co.kr/guide/geo-repair-case-2026-06 ; discussion post https://news.hada.io/topic?id=31001 ; secondary reconstruction https://braindetox.kr/en/posts/geo_generative_search_optimization_2026.html
published:       2026-06 (URL slug); GeekNews post dated '3달전' as rendered 2026-09-23
pull_date:       2026-09-23
pull_method:     fetch (Python urllib); found via DuckDuckGo html search, then primary followed from GeekNews link
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor measuring its own GEO service on a client, N=2, no code; the vendor itself labels it a comparison observation, not a controlled A/B
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Gemini, Perplexity (web search on)
metric_kind:     visibility (mention rate over 100 fixed queries, biweekly)
supersedes:      none
captured:        primary article body (Korean, verbatim); GeekNews post body and three comments; secondary blog not reproduced beyond its URL
verbatim:        partial — section named in captured
```

## Verbatim

### Primary — boily.co.kr

> 같은 출발점, 한 곳만 홈페이지를 정비했더니 — GEO 정비 전후 관찰 | 보일리
> BOILY 가이드
> 같은 출발점, 한 곳만 홈페이지를 정비했더니 — GEO 정비 전후 관찰
> 2026-06-30
> 같은 출발점(AI 검색 노출 약 11%)의 두 치과 중, 홈페이지 GEO·AEO를 정비한 곳은 정비 후 약 27%로 올랐고 정비하지 않은 비교군은 제자리(약 10%)였다. 단, 이는 통제된 A/B 실험이 아니라 N=2 관찰이고, ‘홈페이지 정비’ 효과를 GEO 단독으로 분리하지는 못하며, 노출 변화가 정착하는 데는 보통 몇 주~몇 달이 걸린다. 인과로 단정하거나 효과를 보장하지 않으며, 같은 중립 측정으로 전후를 관찰한 사례다.
> “홈페이지를 정비하면 AI 검색 노출이 오를까?” 말로는 누구나 합니다. 그래서 우리는 측정으로 확인해봤습니다. 병원명을 가린 실측 사례를 공개합니다.
> 관찰 설계 — 비교군을 뒀습니다 (통제 실험은 아닙니다)
> AI 검색 노출이 똑같이 약 11%이던 두 치과가 있었습니다. 한 곳(영통OOO치과)은 홈페이지에 GEO·AEO 정비(환자 질문별 정보 페이지·구조화 데이터·의료진 소개)를 했고, 다른 한 곳(강남OOO치과)은 그 홈페이지 정비를 하지 않았습니다(비교군). 같은 기간, 같은 질문 세트, 같은 측정.
> 다만 두 병원은 지역·경쟁 강도 등 조건이 완전히 같지 않고 표본도 두 곳뿐이라, 이건 변수를 통제한 A/B 실험이 아니라 ‘비교 관찰’로 봐주세요.
> 결과
> 정비한 영통OOO치과는 약 11% → 27%(+16%p). 정비하지 않은 비교군(강남OOO치과)은 약 11% → 10%로 제자리였습니다. 같은 출발점에서 한 곳만 올랐습니다.
> 같은 11%에서 출발 — 정비한 영통OOO치과만 27%로, 정비 안 한 비교군은 제자리. (병원명 비공개) 왜 비교군을 뒀나
> AI 답변은 실행할 때마다 분산이 커서, 한 병원만 보면 ‘오른 게 정비 덕인지, 그냥 그날 변동인지’ 구분이 어렵습니다. 조건이 비슷한 비교군이 같은 기간 안 움직였는데 정비한 곳만 올랐다면, 적어도 ‘시간이 지나 저절로 오른 것’은 아니라는 힌트가 됩니다. 다만 이것으로 인과를 증명하지는 못합니다.
> 한계 — 단정하지 않습니다
> N=2 관찰입니다. 변수를 통제한 A/B 실험이 아니라서, 한 번의 상승을 ‘정비 때문’이라고 단정할 수 없습니다.
> ‘GEO 정비’와 ‘일반적인 홈페이지·콘텐츠 개선’을 완전히 분리하지 못합니다 — 사실 GEO는 상당 부분 구조화된 좋은 콘텐츠와 겹칩니다.
> 노출 변화가 정착하는 데는 보통 6~12주가 걸립니다. 이번 상승이 유지·재현되는지는 앞으로 추세로 계속 봐야 합니다.
> 관련 글
> 8.9% — 여섯 번째 자기 측정, 정체가 말해주는 것
> 우리 병원이 AI 검색에 나오는지 직접 확인하는 법
> 14.1% → 9.4% — 다섯 번째 자기 측정, 오른 숫자가 되돌아왔다
> AI 검색 노출은 왜 6~12주 걸릴까 — 정비 후 반영되는 과정
> GEO와 SEO는 뭐가 다른가 — SEO는 했는데 왜 AI 검색엔 안 뜰까
> 측정을 이어가면 무엇이 보이나 — 한 치과의 노출률 관찰 기록
> AI 검색 노출 리포트, 어떻게 읽어야 할까 — 숫자 5가지
> 리뷰가 많으면 AI가 우리 병원을 더 추천할까?
> AI가 우리 병원을 틀리게 말할 때 — AI 답변 속 오정보·옛 정보
> 지금 홈페이지 그대로, AI가 읽는 홈페이지로 — 병원 홈페이지 클로닝
> 구글 비즈니스 프로필(GBP) 정비 실전 — 원장이 직접 하는 AI·지역 검색 노출 강화
> 아임웹 홈페이지 vs 보일리 홈페이지 — AEO·GEO에는 무엇이 유리할까?
> 한국인은 AI로 병원을 고를까? — 데이터로 본 현재
> 병원 GEO·AEO란? — 환자가 AI에게 병원을 물어보는 시대의 노출 측정 가이드
> ChatGPT는 병원을 무엇을 보고 추천할까? — AI가 병원을 고르는 기준
> AI 검색 노출, 어떻게 측정하나 — 노출률·SoV·추세
> GEO vs 전통 SEO — 무엇이 같고 무엇이 다른가
> 병원이 AI 검색에서 자주 놓치는 5가지
> SEO·AEO·GEO 차이 한눈에 — 병원이 알아야 할 3가지 검색 최적화
> 네이버 블로그는 AI 검색에 안 통할까? — 글로벌 AI와 네이버 AI는 정반대입니다
> 측정 도구가 자기 자신을 측정했다 — 보일리의 2주 GEO 실험 공개
> 0 → 2.1 → 3.1 → 14.1% — 네 번째 자기 GEO 측정, 한 엔진이 끌어올린 상승
> 0 → 2.1% → 3.1% — 측정 회사가 공개하는 세 번째 자기 GEO 측정
> 정비 4일 만에, AI가 우리가 쓴 내용을 그대로 인용했다
> AI 검색 노출은 왜 ‘한 번’으로 끝나지 않나 — 계속 측정해야 하는 이유
> 왜 AI마다 병원 추천이 다를까 — ChatGPT·Claude·Gemini·Perplexity 편차
> 신규 개원 병원은 왜 AI 검색에 안 뜰까 — 새 병원이 AI 추천에 등장하는 법
> AI 엔진별 노출 공략법 — ChatGPT는 Bing, Gemini는 구글을 본다

### GeekNews post and comments — news.hada.io/topic?id=31001

> 생성형 AI 검색 최적화(GEO), 대조군 두고 측정해봤다 — 정비한 치과만 2주새 11% | GeekNews
> GeekNews 최신글 최신 예전글 예전 쓰레드 댓글 BeeBS ↗ Ask Show GN⁺ 아티클 Weekly Bots Badge 후원 | 글등록 등록
> 검색
> 로그인
> ▲
> 생성형 AI 검색 최적화(GEO), 대조군 두고 측정해봤다 — 정비한 치과만 2주새 11%→27%
> (boily.co.kr)
> 1 P by liveforownhappiness 3달전 | ★ favorite | 댓글 3개
> ChatGPT·Claude·Gemini·Perplexity에게 "○○동 치과 추천"을 물으면 어떤 병원을 답할까?
> 이걸 측정하는 도구를 만들며, 직접 대조 실험을 해봤습니다.
> ■ 세팅
> 질문 100개를 고정(동결)하고, 4개 AI에 각각 웹검색 켠 상태로 격주 측정
> 응답에서 특정 병원이 추천·언급되는 비율(노출률)을 집계
> 출발점이 거의 같던 두 치과(둘 다 AI 노출 ~11%)로 A/B
> ■ 결과 (2주)
> A 치과: 홈페이지 GEO·AEO 정비(구조화된 진료·의료진 정보, 크롤 가능한 콘텐츠, 내부링크)
> → 약 27% (+16%p), 3개 엔진에서 고르게 상승
> B 치과(대조군, 정비 안 함): 약 10%로 제자리
> 대조군을 둔 이유는 "그냥 시간이 지나서/AI가 업데이트돼서 오른 것"과 구분하기 위해서입니다.
> 정비한 쪽만 올랐다는 건, 최소한 이번 관찰에선 정비가 변화를 만들었다는 신호로 봅니다.
> ■ 한계 (정직하게)
> 단일 회차·소수 사례라 인과로 단정하지 않습니다.
> 2주 뒤 다시 측정해 유지·재현되는지 추세로 확인할 예정입니다.
> 병원명은 비공개(지역만 표기).
> 자세한 수치·차트: https://boily.co.kr/guide/geo-repair-case-2026-06
> 함께 보면 좋은 글
> β
> 내 신생 서비스가 ChatGPT·Claude·Perplexity 추천에 0번 떴다 — AI 검색 노출(GEO/AEO) 직접 측정해본 기록
> AI Overviews, ChatGPT, Claude, Gemini, Perplexity를 위한 AEO와 GEO
> Google의 생성형 AI 검색 기능 최적화 공식 가이드
> Google 검색의 생성형 AI 기능을 위한 웹사이트 최적화
> AI 답변 조작은 얼마나 쉬울까, 상품 설명만 바꿔도 90% 승률
> GeekNews는 개발·기술·스타트업 소식을 빠르게 전달합니다.
> Weekly 뉴스레터로 구독하거나, 더 편하게 GeekBots로 받아보세요.
> Weekly 구독
> GeekBots로 받기
> GeekNews 소개
> 숨기기
> 댓글과 토론
> 인증 이메일 클릭후 다시 체크박스를 눌러주세요
> ▲
> yhpat1 3달전    [-]
> 실험 설계에 문제가 있네요. 정말 'GEO'때문에 오른 것인지를 보고자 한다면, GEO를 제외한 가능한 모든 변수를 통제해야죠. 이 경우에는 대조군으로 "아무것도 안 한 치과"가 아니라, "SEO만 한 치과"가 더 적절해 보입니다. 본문 내용만으로는 GEO를 해서 오른 건지, 방치하던 홈페이지를 개선해서 오른 건지 알 수가 없어요.
> 답변달기
> ▲
> aliveornot 3달전    [-]
> 홍보하시려면 당당하게 showGN에서 합시다. 정작 본인 사이트도 ai 추천 못받고 계신거 같습니다만
> 답변달기
> ▲
> xguru 3달전    [-]
> "대조군을 두고 비교 했더니 오른게 보였다" 라는 글이 무슨 인사이트가 있는건가요?
> 이 사례는 “대조군을 둔 A/B 실험”이라기보다는 “두 병원의 전후 관찰”에 가까워 보입니다.
> seo 도 아닌 geo/aeo 를 2주 만에 측정이 가능하다는 것도 믿기가 어렵고요,
> 솔직히 말씀드리면 해당 서비스에 대한 마이너스가 되는 글이라고 생각됩니다.
> 답변달기

## Pull notes — mechanical only

- Korean text kept verbatim, not translated.
- Related-post titles on the Boily page (self-measurement series: '14.1% → 9.4%', '8.9% — 여섯 번째 자기 측정') captured as link text only; those posts not opened.
- Chart images not captured.
