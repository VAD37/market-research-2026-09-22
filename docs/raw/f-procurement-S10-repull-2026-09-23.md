# Procurement registers — sam.gov, UK Contracts Finder, TED: category-term search paths

```yaml
source:          SAM.gov (U.S. General Services Administration); Contracts Finder (UK Government, contractsfinder.service.gov.uk); TED — Tenders Electronic Daily (Publications Office of the EU, ted.europa.eu)
url_or_doc_id:   see per-register URLs below
published:       live search pages
pull_date:       2026-09-23
pull_method:     browser (Chrome extension) — logged out
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default for filed procurement records; no record matched, so the tier applies to the channel only
source_label:    filed
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      docs/raw/f-signal-hr-S10-procurement-2026-09-22.md (sam.gov API none; Contracts Finder keyword filter non-functional; TED 405)
captured:        result-count lines and first results as rendered
verbatim:        full
```

## Verbatim — SAM.gov

1. Exact phrase, active records: https://sam.gov/search/?index=opp&page=1&pageSize=25&sort=-modifiedDate&sfm%5Bstatus%5D%5Bis_active%5D=true&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=EXACT&sfm%5BsimpleSearch%5D%5BkeywordTags%5D%5B0%5D%5Bvalue%5D=generative%20engine%20optimization
   "generative engine optimization | Search Results | No matches found | Your search did not return any results for active records. | Would you like to include inactive records in your search results?"
2. "Any" of three quoted phrases ("generative engine optimization", "answer engine optimization", "AI visibility"): "Showing 1 - 25 of 3,666 results"; first results "Mental Health First Aid Instructor Certification Training" (Indian Health Service, Notice ID 75H70426Q00043A1) and "30--WEIGHT,COUNTERBALANCE" (Notice ID SPE7L426U1284). [note: the page appended `is_active=true`; results do not contain the phrases in their visible text — the ANY mode appears to match individual words]

## Verbatim — UK Contracts Finder

https://www.contractsfinder.service.gov.uk/Search/Results?keywords=%22generative+engine+optimisation%22 — "Search results | We’ve found 667 notices"; first results: Addingham Parish Council notice; UK PACT programme notice. Keyword field on the page read empty: the URL parameter was not applied.

## Verbatim — TED

https://ted.europa.eu/en/search/result?FT=%22generative%20engine%20optimization%22 — page title "Human Verification"; body "Let’s confirm you are human | Complete the security check before continuing. This step verifies that you are not a bot, which helps to protect your account and prevent spam. | Begin". Stopped; the check was not started.

## Pull notes — mechanical only

- SAM.gov: exact-phrase search on active opportunities returns zero; inactive records were not added (would need the on-page toggle).
- Contracts Finder: keyword search works only through the on-page form (POST); the form was not submitted. Result for the category term: unknown — checked Contracts Finder 2026-09-23.
- TED: human-verification wall; result unknown — checked ted.europa.eu 2026-09-23.
- No login, no account.
