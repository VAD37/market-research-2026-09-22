# MAICON 2026 — speaker list (Seer Interactive and Fire&Spark qualifying source)

```yaml
source:          Marketing AI Institute (MAICON 2026 conference, a SmarterX Ventures, LLC brand)
url_or_doc_id:   https://www.marketingaiinstitute.com/events/marketing-artificial-intelligence-conference/agenda/speakers
published:       undated on the page itself; conference dates stated as Oct. 13-15, 2026, Cleveland
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP, dedicated new tab) — the page's speaker roster is loaded via an iframe and did not render in a plain fetch; claude-in-chrome was not connected at the time this pull ran (checked via tabs_context_mcp, reported not connected), so per task instructions the MCP_DOCKER Playwright browser was used in a dedicated new tab, distinct from another agent's already-open tab on this shared browser (courtlistener.com, untouched)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — conference's own speaker-roster page, reliable on existence (who is speaking, their stated employer and title), biased on framing (a speaking slot is not proof of a company's market position)
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        accessibility-tree snapshot (browser_snapshot) of the rendered speaker grid — all 32 speaker cards visible in the viewport at capture time; page may paginate or load additional speakers below the fold not captured
```

## Verbatim

Speaker cards as rendered (name — title — employer, in the order captured):

> Liza Adams — Founder, AI Advisor & GTM Strategist — GrowthPath Partners
> Kris Beck — SVP Strategic Operations — Veroot
> Dale Bertrand — President — Fire&Spark
> Pam Boiros — CMO — Bridge Marketing Advisors
> Brian Brinkman — Partner — Stream Creative
> Sandy Carter — CEO & Best-Selling Author — (no employer listed)
> Andy Crestodina — Co-founder & CMO — Orbit Media
> Kate Dobbs — Chief Marketing & Communications Officer — formerly Solventum
> Alec Foster — Chief Agent Officer & Responsible AI Lead — Marketing + Media Alliance (MMA)
> Nicole Franco — Head of Digital PR, AI Innovation — Fractl
> Karen Hao — Award-Winning Journalist and Best-Selling Author of Empire of AI | TIME 100 Most Influential People in AI — (no employer listed)
> Matt Heinz — Founder & President, Heinz Marketing Inc — Heinz Marketing Inc
> Jessica Hreha — Director, Marketing AI Transformation — Veeam Software
> Mitch Joel — Executive Director — Next Era Institute
> Mike Kaput — Chief Content Officer — SmarterX & Marketing AI Institute
> Craig Karmazin — Founder and CEO — Good Karma Sports
> Greg Kihlström — Advisor and Host of The Agile Brand Podcast — The Agile Brand
> Keith Moehring — CEO — L2 Digital
> Tamra Moroski — Head of Partnerships — SmarterX & Marketing AI Institute
> Christopher S. Penn — Co-founder & Chief Data Scientist — Trust Insights
> Brian W. Piper — Founder — AIreFlow Solutions
> Claire Potter-Schneider — Head of AI Transformation — Dynatrace
> Joe Pulizzi — Founder — The Tilt
> Taylor Radey — Director of Research — SmarterX
> Suraj Rajdev — Head of Data, Measurement & Analytics — Google
> Wil Reynolds — Founder & Co-CEO — Seer Interactive
> Katie Robbert — CEO — Trust Insights
> Paul Roetzer — Founder & CEO — SmarterX & Marketing AI Institute
> Kevin Roose — Bestselling Author, Futureproof, Award-Winning Technology Columnist, The New York Times — (no employer listed)
> Lauren Schiavone — Founder & Lead Consultant — Wonder Consulting
> Dan Slagen — CMO & CAITO — Zapier
> Vinny Sosa — Lead Marketing AI Solutions Architect — ServiceTitan
> Jim Sterne — Founder — Coastal Intelligence
> Rachel Woods — CEO & Co-founder — AMP (AI Momentum Protocols)
> Guy Yalif — Chief Evangelist — Webflow
> Andrew Yang — Tech & Economic Futurist, Best-Selling Author — (no employer listed)
> Amanda Yoho — Chief Executive Officer — Proformex

## Pull notes — mechanical only

- Page title: "AI Speakers | Marketing AI Conference | MAICON." Page includes a promotional interstitial dialog ("Get $200 off MAICON 2026") which was not interacted with; speaker grid was captured from the underlying accessibility tree regardless.
- Did not click "More Info" on any speaker card (which opens per-speaker bio dialogs) — only the name/title/employer visible on each card face was captured.
- Speaker count captured: 32 (may not be the full roster if the page paginates beyond the initial render — not verified this pull).
- Two speakers are agency-affiliated and cited as qualifying sources in this census: **Dale Bertrand** (President, Fire&Spark) and **Wil Reynolds** (Founder & Co-CEO, Seer Interactive). Additional agency-affiliated speakers not pursued to a second source this pull are held in `f-agency-census-c5-2026-09-22.md` §3 (Fractl via Nicole Franco).
- Playwright tab was closed at session end after navigating to `about:blank`; did not touch the other open tab in the shared browser (courtlistener.com, belonging to another concurrent agent per task instructions).
