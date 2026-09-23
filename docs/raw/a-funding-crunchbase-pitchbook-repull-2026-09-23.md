# Crunchbase and PitchBook — AthenaHQ, Peec AI, Profound, Scrunch free-preview profile fields

```yaml
source:          Crunchbase (crunchbase.com) organization pages; PitchBook (pitchbook.com) free-preview company profiles
url_or_doc_id:   https://www.crunchbase.com/organization/{athenahq,peec-ai,scrunch-ai} ; https://pitchbook.com/profiles/company/{759029-50,741876-13,633268-54,708134-32}
published:       live profiles, undated
pull_date:       2026-09-23
pull_method:     browser (Chrome extension) — logged out
pull_purpose:    evidence about a number
tier:            5
tier_reason:     funding aggregators; neither discloses the source of each round figure on the free view (hidden method drops the tier-4 panel default one tier)
source_label:    analyst-derived
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none — 2026-09-22 attempts on crunchbase.com and pitchbook.com returned 403 and produced no raw file
captured:        header fields, funding-table rows and FAQ lines visible without login; obfuscated fields recorded as shown
verbatim:        partial
```

## Verbatim — Crunchbase

[note: fields Crunchbase renders as "obfuscation" are recorded as that literal text]

```
AthenaHQ https://www.crunchbase.com/organization/athenahq : "AthenaHQ | Growth Score | 84 | CB Rank | 23016 | Heat Score | 75 | ... AthenaHQ is the one-stop-shop for marketers on everything AI Search. | Founded | obfuscation | Private | Seed | San Francisco, California, United States | 11-50 | athenahq.ai" ; "Total Funding | obfuscation | obfuscation | Seed raised" ; "Unlock company funding data, including rounds, dates, amounts, and investors." ; "Unlock best-in-class private company insights with Crunchbase Pro | Get real-time funding and financial data | ... | Try Pro Free"
Peec AI https://www.crunchbase.com/organization/peec-ai : "Peec AI | Growth Score | 86 | CB Rank | 3098 | Heat Score | 68 | ... Peec AI provides tools for marketing teams to analyze brand performance across various AI platforms. | Founded | obfuscation | Private | Series A | Berlin, Berlin, Germany | 51-100 | peec.ai" ; "This year, Peec AI is projected to spend $2.5M on IT, according to Aberdeen."
Profound https://www.crunchbase.com/organization/profound-e4a1 : "Page not found | Oops." (slug guessed; not resolved)
Scrunch https://www.crunchbase.com/organization/scrunch-ai : "Scrunch | Growth Score | 60 | CB Rank | 8374 | Heat Score | 31 | ... Scrunch, a platform designed to help businesses optimize their presence in AI-driven search. | Acquired by | Sitecore | Founded | obfuscation | Private | Series A | Salt Lake City, Utah, United States | 51-100 | scrunch.com/" ; "Scrunch was acquired by Sitecore on " [date blank/obfuscated] ; "Announced Date" [blank]; no price shown ; "This year, Scrunch is projected to spend $289.9K on IT, according to Aberdeen."
```

## Verbatim — PitchBook

[note: tab characters in funding tables are PitchBook's own column separators; empty columns are empty on the page]

```
Search https://pitchbook.com/profiles/search?q=AthenaHQ -> AthenaHQ /profiles/company/759029-50
AthenaHQ https://pitchbook.com/profiles/company/759029-50 : "AthenaHQ Overview | Update this profile | Year Founded | 2024 | Status | Private | Employees | 18 | Latest Deal Type | Early Stage VC | Latest Deal Amount | $2.1M | Investors | 4" ; "Description | Developer of a generative engine optimization platform designed to enhance business visibility and ranking in artificial intelligence-driven search results. The company's platform provides a real-time prompt monitoring to understand brand mentions in generated content, identifies content gaps where artificial intelligence lacks knowledge about the business, and pinpoints websites cited by chatbots to enhance bran[truncated in capture]" ; "Website | www.athenahq.ai | Ownership Status | Privately Held (backing) | Financing Status | Venture Capital-Backed | Primary Industry | Business/Productivity Software | Other Industries | Media and Information Services (B2B) | Vertical(s) | SaaS, Marketing Tech, Artificial Intelligence & Machine Learning | Corporate Office | 800 Indiana Street | San Francisco, CA 94107 | United States" ; Valuation & Funding: "Deal Type	Date	Amount	Raised to Date	Post-Val	Status	Stage | 1. Early Stage VC	01-Apr-2025	$2.1M			Completed	Generating Revenue | To view AthenaHQ’s complete valuation and funding history, request access »"
Search q=Peec%20AI -> Peec AI /profiles/company/741876-13
Peec AI https://pitchbook.com/profiles/company/741876-13 : "Year Founded | 2025 | Status | Private | Employees | 100 | Latest Deal Type | Early Stage VC | Investors | 15" ; "Description Developer of a conversational artificial intelligence platform designed to help companies improve brand visibility and product discovery. The company's platform helps in mastering optimization for LLM-based answer engines, tracking visibility tren[truncated in capture]" ; "Deal Type	Date	Amount	Raised to Date	Post-Val	Status	Stage | 3. Early Stage VC	25-Jun-2026				Completed	Generating Revenue | 2. Early Stage VC (Series A)	18-Nov-2025				Completed	Generating Revenue | 1. Seed Round	02-Jul-2025	$8.08M	$8.08M		Completed	Generating Revenue"
Search q=Profound -> 8 hits incl. "Profound Company /profiles/company/633268-54" (others: Profound Commerce, ProFound Network, Profound Medical, Profound Works, Profound Services, Profound Research, ProFound Therapeutics)
Profound https://pitchbook.com/profiles/company/633268-54 : "Year Founded | 2024 | Status | Private | Employees | 300 | Latest Deal Type | Series D | Latest Deal Amount | $180M | Investors | 22" ; "Description Developer of a search engine optimization tool designed for artificial intelligence (AI) search optimization. The company's software provides deep visibility analysis and clear recommendations by tracking how websites are interpreted and crawled b[truncated in capture]" ; "Deal Type	Date	Amount	Raised to Date	Post-Val	Status	Stage | 7. Later Stage VC (Series D)	15-Sep-2026	$180M			Completed	Generating Revenue | 6. Later Stage VC (Series C)	24-Feb-2026				Completed	Generating Revenue | 5. Early Stage VC (Series B)	23-Jul-2025				Completed	Generating Revenue | 4. Early Stage VC (Series A)	04-Apr-2025				Completed	Generating Revenue | 3. Seed Round	13-Aug-2024				Completed	Generating Revenue | 2. Accelerator/Incubator					Completed	Generating Revenue | 1. Accelerator/Incubator					Completed	Generating Revenue | To view Profound’s complete valuation and funding history, request access »" ; FAQ "Profound was founded in 2024."
Search q=Scrunch -> "Scrunch AI Company /profiles/company/708134-32"
Scrunch AI https://pitchbook.com/profiles/company/708134-32 : "Year Founded | 2023 | Status | Acquired/Merged | Employees | 77 | Latest Deal Type | Buyout/LBO | Financing Rounds | 3" ; "Description Developer of a leading platform designed to help brands gain visibility in artificial intelligence (AI) search results. The company offers tools to interpret brand presence across large language models and AI agents, enabling marketers to shape br[truncated in capture]" ; Valuation & Funding: "This information is available in the PitchBook Platform. To explore Scrunch AI‘s full profile, request access. | Request a free trial" ; FAQ: "When was Scrunch AI acquired? | Scrunch AI was acquired on 28-May-2026. | Who acquired Scrunch AI? | Scrunch AI was acquired by Sitecore." Deal value: not shown.
```

## Pull notes — mechanical only

- Crunchbase: Cloudflare "Just a moment... We must verify your session before you can proceed" cleared on its own after ~8 s; no challenge interacted with. Funding amounts, dates and investors sit behind Crunchbase Pro ("Try Pro Free", "Start Free Trial"): needs payment/subscription. Profound's Crunchbase slug was guessed (`profound-e4a1`) and returned "Page not found"; not searched further.
- PitchBook: free previews rendered without login; full history behind "request access" / "Request a free trial". Round amounts shown only where printed (AthenaHQ $2.1M; Peec AI seed $8.08M; Profound Series D $180M); other rounds show date and type with the amount column empty.
- Scrunch/Sitecore deal value: not on either aggregator's free view — see `a-bloomberg-scrunch-sitecore-repull-2026-09-23.md`.
- No login, no account, no trial started.
