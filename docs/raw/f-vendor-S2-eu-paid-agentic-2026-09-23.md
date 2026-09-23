# Vendor pages in local languages — S2 listings naming ChatGPT Ads, agentic storefronts and agentic checkout for UK, FR, ES, IT, NL: OpenAI (es-ES, it-IT, nl-NL via Wayback), Shopify (uk, fr, es, it, nl), Adyen Agentic, Adform press release; walls and 404s

```yaml
source:          OpenAI (openai.com locale pages via web.archive.org); Shopify (shopify.com/<locale>/agentic-storefronts, /nl/agentic-plan); Adyen N.V. (adyen.com/agentic-commerce); Adform (site.adform.com newsroom); probes of Stripe, Mollie, Worldline, Nexi, PayPal, Klarna, Microsoft Advertising locale pages
url_or_doc_id:   http://web.archive.org/web/20260826063327id_/https://openai.com/es-ES/index/chatgpt-ads-expands-across-europe/ ; http://web.archive.org/web/20260829230209id_/https://openai.com/it-IT/index/chatgpt-ads-expands-across-europe/ ; http://web.archive.org/web/20260904032425id_/https://openai.com/nl-NL/index/chatgpt-ads-expands-across-europe/ ; https://www.shopify.com/uk/agentic-storefronts ; https://www.shopify.com/fr/agentic-storefronts ; https://www.shopify.com/es/agentic-storefronts ; https://www.shopify.com/it/agentic-storefronts ; https://www.shopify.com/nl/agentic-storefronts ; https://www.shopify.com/nl/agentic-plan ; https://www.adyen.com/agentic-commerce ; https://site.adform.com/resources/newsroom/adform-is-one-of-openai-s-technology-platform-partners-as-chatgpt-ads-arrive-in-europe/
published:       OpenAI post "Oorspronkelijk gepubliceerd op 18 augustus 2026" (NL page, with a later update note); Wayback captures 2026-08-26 (es-ES), 2026-08-29 (it-IT), 2026-09-04 (nl-NL); Adform release 2026-09-10; Shopify and Adyen pages undated — no date on page
pull_date:       2026-09-23
pull_method:     fetch (curl; Wayback `id_` raw captures, gzip-decoded)
pull_purpose:    evidence about a number (S2 vendor listing in a local language naming AI ads or agentic checkout; named customers where the page carries any)
tier:            3
tier_reason:     vendor's own product page or press release — reliable on existence, biased on framing (table default 3); the Wayback captures are archive copies of the vendor's page, tier unchanged
source_label:    vendor-reported
lane:            F
sub_market:      paid placement (OpenAI, Adform); agentic commerce (Shopify, Adyen)
engine:          ChatGPT (OpenAI, Adform); ChatGPT, Gemini, Google AI Mode, Copilot, Perplexity (Shopify NL plan page); engines unnamed on the Adyen page
metric_kind:     none
supersedes:      none (German locale page is docs/raw/b-openai-de-chatgpt-ads-europe-2026-09-22.md; English Shopify Agentic Storefronts and Adyen were not previously pulled)
captured:        opening paragraphs and every line naming a country, an engine, availability, a price or a customer; access table for every probe
```

## Access table

| Target | HTTP | Result |
|---|---|---|
| openai.com/index/chatgpt-ads-expands-across-europe/ (EN) | 200, 404,030 B | body is the JS challenge "Enable JavaScript and cookies to continue"; not archived on Wayback |
| openai.com/fr-FR/…/chatgpt-ads-expands-across-europe/ | 200, 419,001 B | same challenge; not archived on Wayback |
| openai.com/en-GB/… ; /es-ES/… ; /it-IT/… ; /nl-NL/… (live) | 403 | Cloudflare; en-GB not archived on Wayback; es-ES, it-IT, nl-NL archived (used below) |
| shopify.com/{uk,fr,es,it,nl}/agentic-storefronts | 200 | localised pages exist in all five |
| shopify.com/{uk,fr}/agentic-readiness ; /nl/agentic-plan | 200 | "Product Page Audit for Agentic Commerce - Shopify UK"; "Audit de page de produit pour le commerce agentique - Shopify France"; "Shopify Agentic-abonnement: verkoop rechtstreeks in AI-kanalen - Shopify Nederland" |
| shopify.com/{uk,fr,es,nl}/agentic-commerce, /agentic-commerce | 404 (IT: connection reset) | no such page |
| stripe.com/{gb,fr,es,it,nl}/agentic-commerce, /agentic-commerce | 404 | no such page |
| adyen.com/agentic-commerce ; /knowledge-hub/agentic-commerce | 200 | product page (below); knowledge-hub page not extracted |
| mollie.com/agentic-commerce ; /en/agentic-commerce | 404 | — |
| worldline.com …/blogs/2025/agentic-commerce ; nexigroup.com/en/agentic-commerce/ ; paypal.com/uk/business/agentic-commerce | 404 | — |
| klarna.com/uk/agentic-commerce/ | 202, 0 B | script-rendered, nothing served |
| about.ads.microsoft.com/{en-gb,fr-fr}/solutions/copilot | 404 (redirects to /en/ and /fr/, both 404) | no localised Copilot ads page at that path; /{en-gb,fr-fr}/blog redirect to the English blog |

## Verbatim — OpenAI, es-ES (Wayback 2026-08-26)

> ChatGPT Anuncios se expande por Europa | OpenAI
> Seis meses después de empezar a probar anuncios en EE. UU., llevamos ChatGPT Anuncios a 31 mercados europeos.
> El 24 de agosto, ChatGPT Anuncios estará disponible en 31 países europeos, entre ellos Alemania, Francia, España, Italia, Suecia, Noruega, Dinamarca, Países Bajos y Austria. Al principio, se podrá acceder a ChatGPT Anuncios a través del equipo de Soluciones Publicitarias de OpenAI, agencias publicitarias asociadas y socios tecnológicos. El autoservicio a través del Gestor de anuncios llegará más adelante este trimestre. Los profesionales del marketing de toda Europa tendrán ahora nuevas formas de llegar a las personas mientras exploran, comparan o toman decisiones.
> Las personas acuden a ChatGPT con objetivos. Puede que estén planificando un viaje, eligiendo software para su empresa, amueblando una casa o aprendiendo a iniciarse en una nueva afición.
> De acuerdo con los [principios publicitarios] de OpenAI, los anuncios en ChatGPT están claramente identificados y separados de las respuestas de ChatGPT. La publicidad no influye en las respuestas que proporciona ChatGPT.
> En febrero, empezamos a probar anuncios en ChatGPT con un proyecto piloto en Estados Unidos. En los últimos seis meses, nos hemos expandido a otros ocho mercados y próximamente incorporaremos 31 mercados europeos.
> Empezamos con las pujas por CPM y después añadimos el CPC. Ahora admitimos el coste por clic optimizado para conversiones (oCPC), lo que permite a los anunciantes optimizar sus campañas en función de sus objetivos empresariales.
> Hemos añadido la segmentación geográfica y la función de audiencias personalizadas para ayudar a las empresas a llegar a los clientes más relevantes.
> Hemos ampliado nuestros informes más allá de los clics con la incorporación de OpenAI Pixel, la API de conversiones y las integraciones de medición de terceros.
> Hasta la fecha, decenas de miles de anunciantes han utilizado ChatGPT para hacer crecer sus negocios, y la plataforma sigue mejorando.

## Verbatim — OpenAI, it-IT (Wayback 2026-08-29)

> ChatGPT Ads si espande in Europa | OpenAI
> Dal 24 agosto, ChatGPT Ads sarà disponibile in 31 Paesi europei, tra cui Germania, Francia, Spagna, Italia, Svezia, Norvegia, Danimarca, Paesi Bassi e Austria. Inizialmente, ChatGPT Ads sarà accessibile tramite il team Ads Solutions di OpenAI, le agenzie pubblicitarie partner e i partner tecnologici. La modalità self-service tramite Ads Manager sarà disponibile nel corso del trimestre.
> A oggi, decine di migliaia di inserzionisti hanno utilizzato ChatGPT per far crescere la propria attività e la piattaforma continua a migliorare.

## Verbatim — OpenAI, nl-NL (Wayback 2026-09-04)

> ChatGPT-advertenties breiden uit in Europa | OpenAI
> Zes maanden nadat we in de VS advertenties zijn gaan testen, brengen we ChatGPT‑advertenties naar 31 Europese markten.
> [Update]: Selfservicetoegang tot ChatGPT‑advertenties via Ads Manager is nu beschikbaar in alle 31 hieronder aangekondigde Europese markten. Bedrijven die aan de slag willen, kunnen zich aanmelden via [link]
> Oorspronkelijk gepubliceerd op 18 augustus 2026
> Volgende week worden ChatGPT‑advertenties beschikbaar in 31 Europese landen, waaronder Duitsland, Frankrijk, Spanje, Italië, Zweden, Noorwegen, Denemarken, Nederland en Oostenrijk.
> Adverteerders krijgen in eerste instantie toegang tot ChatGPT‑advertenties via het OpenAI Ads Solutions-team, bureaupartners en technologiepartners. Selfservicetoegang via Ads Manager volgt later deze zomer.
> Net als in onze bestaande markten worden advertenties alleen weergegeven aan gebruikers met een Free- of Go-abonnement. Plus-, Pro- en Enterprise-abonnementen blijven advertentievrij.
> Tienduizenden marketeers hebben inmiddels geadverteerd op ChatGPT, en we blijven het platform verbeteren op basis van wat we leren van mensen en bedrijven.

[note: no advertiser is named on any of the three locale pages; the United Kingdom is not in the named-country list on any of them. The update line's date is not printed on the NL page; the capture is 2026-09-04.]

## Verbatim — Shopify Agentic Storefronts, five locales

- UK (`/uk/agentic-storefronts`, title "Sell in AI chats with Shopify UK"): "With Agentic Storefronts, your products show up instantly in ChatGPT, Gemini, and more. Shoppers discover and buy without leaving the chat." — "Sales run through Shopify Checkout, powering 14% of US e-commerce. Fast, flexible, secure, and works with your payment processor."
- FR (title "Vendez sur les plateformes d'IA conversationnelle avec Shopify France"): "Disponible dans toutes les boutiques" — "Avec Agentic Storefronts, vos produits apparaissent instantanément sur ChatGPT, Gemini et d'autres plateformes. Les acheteurs peuvent les découvrir et les acheter sans quitter la conversation." — "Les ventes sont traitées par Shopify Checkout, qui propulse 14 % de l'e-commerce aux États-Unis."
- ES (title "Vende en los chats de IA con Shopify"): "Con Agentic Storefronts, tus productos aparecen al instante en ChatGPT, Gemini y mucho más. Los compradores descubren y compran sin salir del chat." — "Las ventas se procesan a través de Shopify Checkout, que impulsa el 14% del ecommerce de EE. UU."
- IT (title "Vendi nelle chat IA con Shopify Italia"): "Con Agentic Storefront, i tuoi prodotti compaiono all'istante su ChatGPT, Gemini e non solo. Gli acquirenti scoprono e acquistano senza uscire dalla chat."
- NL (title "Verkopen in AI-chats met Shopify Nederland"): "Met Agentic Storefronts verschijnen producten direct in ChatGPT, Gemini en meer. Shoppers ontdekken en kopen zonder de chat te verlaten." — "Dankzij de Shopify Catalogus en Knowledge Base tonen AI-agenten geverifieerde product- en merkgegevens rechtstreeks uit je winkel." — "Agentic Storefronts wordt automatisch ingeschakeld voor in aanmerking komende winkels." — customer quote: "Doordat we Shopify gebruiken, zijn we automatisch overal waar onze klanten winkelen, dus ook binnen AI-gesprekken." — Steve Madden, Colleen Waters — VP E-commerce
- NL plan page (`/nl/agentic-plan`): "Publiceer je producten direct in AI-chats en laat kopers afrekenen in het gesprek. Een Shopify-webshop is niet nodig." — "Geen maandelijkse kosten. Kaarttarieven vanaf 3,2% + $ 0,50 SGD online." — "De snelste weg naar agentic commerce. Laat actuele productgegevens verschijnen in ChatGPT, Google AI Mode en Gemini, Copilot, Perplexity, de Shop-app en binnenkort nog veel meer." — "Jouw merk zou wel eens de volgende kunnen zijn. Blijf op de hoogte van de beschikbaarheid."

[note: the only named merchant on the five localised pages is Steve Madden (US footwear), the same quote as the global template; no UK, FR, ES, IT or NL merchant is named. The NL plan page prints a card rate in SGD. Country availability of in-chat checkout is not stated on any locale page beyond "in aanmerking komende winkels" / "Disponible dans toutes les boutiques".]

## Verbatim — Adyen Agentic (adyen.com/agentic-commerce)

> Adyen Agentic: Commerce infrastructure for the agent economy
> Your universal translator for agentic commerce — One integration to scale your commerce stack for the agent economy.
> The three stages of AI-assisted checkout — Customer searches for products and instantly receives accurate catalog data inside the AI chat. — Selected products are converted into a dynamic cart with live pricing, tax, and delivery information. — Customer approves payment. Transactions are screened for fraud and securely processed.
> Deliver a single product feed that automatically adapts to each AI platform's requirements, with accurate, real-time catalog and inventory data.
> Accept payments across all the major agentic protocols and channels while staying compliant, secure and fully in control.
> Regardless of where your customers buy, remain the merchant of record and the post-purchase relationship is yours.
> "The rapid evolution of Agentic Commerce protocols means retailers need a trusted partner who stays ahead of the curve. With Adyen Agentic, we were able to build on proven, battle-tested foundations to deploy quickly and confidently." — Nicolas Benoist, CTO at Sezane
> "The future of commerce is agentic, and ESW's partnership with Adyen puts the world's leading enterprise brands at the center of it." — Eric Eichmann, CEO, ESW
> FAQ headings: What is the difference between agentic and traditional e-commerce? — Do we have to adopt all three modules (Agentic Feed, Agentic Cart, and Agentic Payments) at the same time? — How does Adyen Agentic prevent fraud? — How does Adyen Agentic ensure compliance? — Is this available to all merchants?

[note: FAQ answers are collapsed accordion panels; the answer to "Is this available to all merchants?" was not in the served text. No engine, protocol name, price or country is named on the extracted text. Sezane is named as a customer; its country and vertical are not stated on the page.]

## Verbatim — Adform press release, 2026-09-10

> Adform is one of OpenAI's technology platform partners as ChatGPT Ads arrive in Europe
> Adform clients can now access ChatGPT Ads, as strong client adoption signals growing momentum across the region.
> [Adform,] the integrated advertising platform built for the agentic age, has been selected as one of the technology platform partners supporting the European rollout of ChatGPT Ads in Europe, offering a new advertising environment for European brands and agencies. Early client adoption is strong and already building momentum across the region.
> The expansion gives European advertisers the opportunity to start building early learnings from an advertising environment already live in over 40 markets, including the United States, United Kingdom and Canada.
> European advertisers are already putting ChatGPT Ads to the test
> Petter Mååg, Digital Media & Online Sales Manager, Volkswagen, commenting on the rollout, said: "At Volkswagen, understanding how consumer behaviour evolves is essential to staying relevant and customer-centric. As people increasingly turn to AI-powered experiences for information and decision-making, testing ChatGPT Ads allows us to explore how our brand can engage meaningfully in this emerging environment and how it can create value alongside our existing media investments."
> Marian Hanke, Senior Online Marketing Manager, Vodafone, added: "For us, testing a new channel is not just about being early. We need to understand how it performs as part of the wider customer journey. Running ChatGPT Ads through Adform gives us the opportunity to test the format while connecting the results to our broader campaign measurement and building the learnings we need to decide how we scale from here."
> Stefan Sommer, Chief Growth Officer at Adform, comments: "The arrival of ChatGPT Ads in Europe opens an important new advertising environment for brands and agencies, and we're pleased to have been selected as a technology partner supporting the rollout. … Through Adform, advertisers can connect ChatGPT-driven conversions with their other Adform campaigns and build a clearer view of the customer journey."

[note: the release names two advertisers (Volkswagen, Vodafone) without stating the country entity, the spend or the campaign dates; no client count is given.]

## Pull notes — mechanical only

- OpenAI live locale pages are Cloudflare-walled (403) or serve a JS challenge (200 with challenge body) to curl; the three archived locale captures were fetched as raw `id_` snapshots and gzip-decoded. archive.org/wayback/available reported no capture for the EN, fr-FR and en-GB URLs.
- Shopify locale pages served full HTML (456–522 KB); text extracted by tag-stripping and filtered to lines naming an engine, availability, a price or a merchant. Adyen page 1.1 MB; the customer quotes sit in a carousel and were extracted by string search.
- Adform's newsroom index is server-rendered; the release page was found by grepping the index for "chatgpt".
