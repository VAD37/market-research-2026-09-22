# CourtListener — Chegg v. Google / Penske Media v. Google consolidated MTD hearing outcome; Amazon/Meta/xAI docket search re-attempt

```yaml
source:          CourtListener (courtlistener.com), Free Law Project — docket pages for Chegg, Inc. v. Google LLC (1:25-cv-00543) and Penske Media Corporation v. Google LLC (1:25-cv-03192), D.D.C.
url_or_doc_id:   https://www.courtlistener.com/docket/69668109/chegg-inc-v-google-llc/ ; https://www.courtlistener.com/docket/71332589/penske-media-corporation-v-google-llc/
published:       docket entries through 2026-09-02 (most recent entry each docket as pulled)
pull_date:       2026-09-23
pull_method:     fetch (curl, browser User-Agent); docket IDs located via CourtListener's `?q=&type=r&docket_number=<no>&court=dcd` search (case-name/docket-number search returned HTTP 200; free-text keyword search returned HTTP 202 WAF challenge, see Pull notes)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — CourtListener docket record, filed
source_label:    filed
lane:            B
sub_market:      organic recommendation
engine:          Google (AI Overviews, AI Mode)
metric_kind:     traffic
supersedes:      none — supplements b-court-dockets-table-2026-09-22.md, which recorded both dockets as "Active, motions to dismiss pending" with the consolidated hearing outcome `unknown — checked docket entry list, 2026-09-22`; this pull resolves that unknown
captured:        full docket entry list, both dockets (Chegg: 236,896 bytes; Penske: 208,797 bytes)
```

## Verbatim

**Chegg, Inc. v. Google LLC, 1:25-cv-00543 (D.D.C.), docket entries (most recent captured):**

> Jul 29, 2026 — MINUTE ORDER granting Defendants' 19 Motion to Consolidate Oral Argument on Motions to Dismiss. The parties shall appear for a consolidated hearing on the pending motions to dismiss in this case and in Chegg, Inc. v. Google LLC, No. 25-cv-543, on August 25, 2026, at 2:00 p.m. in Courtroom 10. Signed by Judge Amit P. Mehta on 7/29/2026.

> Aug 25, 2026 — Minute Entry for proceedings held before Judge Amit P. Mehta: Motion Hearing held on 8/25/2026 re 19 MOTION to Dismiss the Amended Complaint filed by GOOGLE LLC, ALPHABET, INC. **Matter taken under advisement.** (Court Reporter William Zaremba.)

> Aug 27, 2026 — Motion Hearing [docket entry, no further text captured]

> 26 · Sep 2, 2026 — TRANSCRIPT OF HEARING ON MOTION TO DISMISS PROCEEDINGS before Judge Amit P. Mehta held on August 25, 2026; Page Numbers: 1-104. Court Reporter/Transcriber: William Zaremba. Main Document: Transcript Unavailable.

No docket entry dated after 2026-09-02 was found on this docket as pulled 2026-09-23.

**Penske Media Corporation v. Google LLC, 1:25-cv-03192 (D.D.C.), docket entries (most recent captured):**

> Jul 29, 2026 — Order on Motion for Miscellaneous Relief AND Set/Reset Hearings. MINUTE ORDER granting Defendants' 19 Motion to Consolidate Oral Argument on Motions to Dismiss. The parties shall appear for a consolidated hearing on the pending motions to dismiss in this case and in Chegg, Inc. v. Google LLC, No. 25-cv-543, on August 25, 2026, at 2:00 p.m. in Courtroom 10. Signed by Judge Amit P. Mehta on 7/29/2026.

> Aug 27, 2026 — Motion Hearing [docket entry, no further text captured]

> 31 · Sep 2, 2026 — [Transcript entry; Main Document: Transcript, no further descriptive text captured]

No docket entry dated after 2026-09-02 was found on this docket as pulled 2026-09-23; no separate minute entry recording the hearing itself (distinct from Chegg's own minute entry) was found in the portion captured — the two cases were heard at the same consolidated hearing per the 2026-07-29 order, so Chegg's "taken under advisement" minute entry is read as covering both matters, not independently confirmed on Penske's own docket text.

## Amazon / Meta / xAI docket search — re-attempted, still blocked

Five free-text queries attempted via `courtlistener.com/?q=<query>&type=r`: "Amazon Rufus publisher", "Amazon advertising AI publisher", "Meta AI advertising publisher", "xAI Grok publisher", "xAI advertising", plus a quoted variant `"Amazon" "Rufus" advertising`. All six returned **HTTP 202** with an empty body (the same WAF/rate-limit challenge recorded in the prior pull), across three attempts spaced 12-15 seconds apart. By contrast, the docket-number-scoped searches used to locate the Chegg and Penske dockets above (`?q=&type=r&docket_number=<no>&court=dcd`) both returned HTTP 200 on the first attempt. The wall is specific to open free-text keyword search, not to CourtListener generally, and not to a fixed docket-number lookup.

## Pull notes — mechanical only

- Docket IDs for Chegg and Penske were not carried over from the 2026-09-22 pull (not recorded there); relocated this session via the docket-number search pattern above. Two earlier guessed docket-ID URLs (69626807, 70115887) resolved to unrelated cases (a bankruptcy matter and a search-warrant matter) and were discarded, not cited.
- `Ctrl+F`-equivalent text search performed via Python regex over the fetched HTML (tag-stripped), not a rendered browser view; entry ordering, formatting artifacts (`&shy;`, stray "Buy on PACER" fragments) reproduced as extracted.
- The full entry-by-entry docket table (all ~26-31 entries per docket) was not transcribed; only entries relevant to the motion-to-dismiss hearing and its aftermath were extracted, per this row's claim scope.
