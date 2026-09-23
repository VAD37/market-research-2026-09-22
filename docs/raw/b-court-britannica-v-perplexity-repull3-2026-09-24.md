# CourtListener — Encyclopaedia Britannica, Inc. v. Perplexity AI, Inc., S.D.N.Y. 1:25-cv-07546: docket entries after 2025-12-17 (amended complaint, re-filed motion to dismiss, revised schedule)

```yaml
source:          CourtListener (Free Law Project) REST API v4 search endpoint, RECAP docket 71313411
url_or_doc_id:   https://www.courtlistener.com/api/rest/v4/search/?type=r&q=docket_id:71313411 ; https://www.courtlistener.com/api/rest/v4/search/?type=rd&q=docket_id:71313411 ; docket https://www.courtlistener.com/docket/71313411/encyclopaedia-britannica-inc-v-perplexity-ai-inc/
published:       docket entries 2025-11-03 through 2026-09-22 (latest entry #125)
pull_date:       2026-09-24
pull_method:     fetch (curl, anonymous, browser User-Agent; API search endpoint HTTP 200, type=r and type=rd, ordered by entry_date_filed desc)
pull_purpose:    evidence about a number (case status)
tier:            2
tier_reason:     filed court docket record (PACER/RECAP mirror); table default for filed
source_label:    filed
lane:            B
sub_market:      organic recommendation
engine:          Perplexity AI
metric_kind:     none
supersedes:      none — supplements b-court-britannica-v-perplexity-2026-09-22.md, whose status line stops at the 2025-12-17 case-management order
captured:        docket-level fields (type=r) and selected entry descriptions verbatim (type=rd); no PDFs opened
```

## Verbatim — docket fields (type=r)

```json
{"caseName": "Encyclopaedia Britannica, Inc. v. Perplexity AI, Inc.", "court": "District Court, S.D. New York", "dateFiled": "2025-09-10", "dateTerminated": null, "docketNumber": "1:25-cv-07546", "assignedTo": "Jennifer L. Rochon", "referredTo": "Sarah L. Cave", "suitNature": "820 Copyright", "cause": "17:101 Copyright Infringement", "document_count": 242}
```

## Verbatim — entry descriptions (type=rd), matched on "dismiss OR opinion" plus the latest entries

> #48 · 2026-03-18 — "JOINT STIPULATION REGARDING AMENDED COMPLAINT AND PERPLEXITY'S MOTION TO DISMISS: NOW WHEREFORE, IT IS HEREBY STIPULATED BY AND BETWEEN THE PARTIES THAT, Perplexity consents to amendment of the Complaint with the amendments set forth in the Amended Complaint attached hereto as Exhibit A on the terms and conditions set forth in this Stipulation; Plaintiffs shall file the Amended Complaint on March 17, 2026; Perplexity shall file the notice of motion to dismiss the Amended Complaint [...] The Parties further agree that Exhibits B through E, as filed on March 17, 2026, shall constitute the briefing with respect to Perplexitys motion to dismiss the Amended Complaint and that motion shall be deemed fully briefed as of the filing of Perplexity's reply memorandum of law on March 17, 2026. IT IS SO STIPULATED: The Clerk of Court is respectfully directed to terminate the motion at Dkt. 29. SO ORDERED. Motions terminated: 29 MOTION to Dismiss [...] (Signed by Judge Jennifer L. Rochon on 3/18/20246) (jca) (Entered: 03/18/2026)"

> #44 · 2026-03-17 — "MOTION to Dismiss // Notice of Defendant's Motion to Dismiss. Document filed by Perplexity AI, Inc...(Wetzel, Joseph) (Entered: 03/17/2026)"

> #46 · 2026-03-17 — "RESPONSE in Opposition to Motion re: 44 MOTION to Dismiss [...] Document filed by Encyclopaedia Britannica, Inc., Merriam-Webster, Inc...(Crosby, Ian) (Entered: 03/17/2026)"

> #47 · 2026-03-17 — "REPLY MEMORANDUM OF LAW in Support re: 44 MOTION to Dismiss [...] Document filed by Perplexity AI, Inc...(Wetzel, Joseph) (Entered: 03/17/2026)"

> #89 · 2026-07-28 — "NOTICE of Supplemental Authority re: 44 MOTION to Dismiss // Notice of Defendant's Motion to Dismiss.. Document filed by Perplexity AI, Inc.. (Attachments: # 1 Exhibit 1 - Epidemic Sound, AB v. Meta Platforms, Inc., 2026 WL 2001154).(Wetzel, Joseph) (Entered: 07/28/2026)"

> #116 · 2026-09-09 — "ORDER: The Court held a telephone conference on September 8, 2026 (the "Conference") to discuss the status of discovery and the parties' discovery disputes [...] the parties confirmed at the Conference that Plaintiffs requested certain information from Perplexity concerning Perplexity's process for evaluating Plaintiffs' works. By September 11, 2026, Perplexity shall respond to Plaintiffs' request. [...] Another telephone conference [...] is scheduled for September 29, 2026 at 3:00 p.m. ET [...] (Signed by Magistrate Judge Sarah L. Cave on 9/9/2026)"

> #119 · 2026-09-16 — "JOINT REVISED CIVIL CASE MANAGEMENT PLAN AND SCHEDULING ORDER: [...] The Revised Plan modifies the deadlines in the Civil Case Management Plan and Scheduling Order entered on December 17, 2025 (Dkt. No. 39) [...] Deposition due by 8/23/2027. Fact Discovery due by 3/26/2027. Expert Discovery due by 8/23/2027. Case Management Conference set for 9/29/2026 at 03:00 PM before Magistrate Judge Sarah L. Cave. SO ORDERED. (Signed by Magistrate Judge Sarah L. Cave on 9/16/2026)"

> #123 · 2026-09-21 — "LETTER MOTION to Seal Portions of Transcript of Proceedings Held on August 26, 2026 addressed to Magistrate Judge Sarah L. Cave from Brett M. Sandford dated September 21, 2026. Document filed by Perplexity AI, Inc.."

> #124 · 2026-09-21 — "***SEALED***REDACTION to Transcript of Proceedings Held on August 26, 2026 by Perplexity AI, Inc."

> #125 · 2026-09-22 — short_description "Memo Endorsement"; description empty in API record.

## Pull notes — mechanical only

- Query `docket_id:71313411 AND description:(dismiss OR opinion)` returned 19 entries; none is an order or opinion deciding motion #44. No ruling on #44 found in entries returned; entries not matching the query were not enumerated beyond the 12 most recent.
- "3/18/20246" reproduced as printed in the entry text.
- One sealed entry (#124) observed; the 2026-09-22 raw recorded 0 sealed in entries it reached.
