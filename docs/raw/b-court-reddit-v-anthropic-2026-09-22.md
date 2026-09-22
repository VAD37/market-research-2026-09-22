# Reddit, Inc. v. Anthropic PBC — docket, notice of removal, and (image-only) state-court complaint

```yaml
source:          CourtListener / RECAP, N.D. Cal. PACER docket 3:25-cv-05643 (removed from San Francisco County Superior Court, Case No. CGC-25-625892)
url_or_doc_id:   https://www.courtlistener.com/docket/70704683/reddit-inc-v-anthropic-pbc/ ; Notice of Removal PDF https://storage.courtlistener.com/recap/gov.uscourts.cand.452341/gov.uscourts.cand.452341.1.0_1.pdf ; Exhibit A (state-court Complaint and Jury Demand, image-only scan) https://storage.courtlistener.com/recap/gov.uscourts.cand.452341/gov.uscourts.cand.452341.1.1.pdf
published:       2025-06-04 (original Complaint filed in San Francisco County Superior Court, per the Notice of Removal's own recitation); 2025-07-03 (Notice of Removal filed in N.D. Cal.)
pull_date:       2026-09-22
pull_method:     direct curl fetch of www.courtlistener.com (200, after this session's WAF challenge — see pull notes) and storage.courtlistener.com (200 for both PDFs); Notice of Removal PDF converted with pdftotext -layout (text-layer PDF); Exhibit A PDF attempted with pdftotext -layout but returned only page markers, no body text — it is an image-only scan of the original state-court filing, and no OCR tool (tesseract, PyMuPDF, ImageMagick, ghostscript) was available in this environment to recover it
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed court document (Notice of Removal, itself quoting and paraphrasing the underlying state-court Complaint with pinpoint paragraph citations); the underlying Complaint itself (Exhibit A) could not be read past its caption due to the scan/no-OCR limitation above, so its own verbatim wording is not captured here beyond what the Notice of Removal quotes
source_label:    filed
lane:            B
sub_market:      organic recommendation
engine:          Anthropic PBC (Claude) — priority-1 engine
metric_kind:     traffic
supersedes:      none
captured:        Notice of Removal (6 pages) captured in full via pdftotext. Exhibit A (state-court Complaint and Jury Demand, 43 pages) — caption/page markers only; body text is an uncaptured image scan, per the pull-method note above. Docket entry list captured via the docket HTML page (case caption, case numbers, filed/terminated dates, assigned judge, cause, nature of suit, and the full procedural history through case termination).
```

## Case caption

UNITED STATES DISTRICT COURT
NORTHERN DISTRICT OF CALIFORNIA
SAN FRANCISCO DIVISION

REDDIT, INC., Plaintiff, v. ANTHROPIC PBC, Defendant.

Case No. 3:25-cv-05643 — NOTICE OF REMOVAL OF ACTION TO UNITED STATES DISTRICT COURT
[San Francisco County Superior Court Case No. CGC-25-625892]

- **Court:** U.S. District Court, Northern District of California, San Francisco Division (removed from the Superior Court of California, County of San Francisco)
- **Docket number:** 3:25-cv-05643 (federal, N.D. Cal.); CGC-25-625892 (original, San Francisco County Superior Court)
- **Filed:** June 4, 2025 (original Complaint, state court, per the Notice of Removal's own recitation at Statement of the Case ¶1); July 3, 2025 (Notice of Removal to federal court)
- **Assigned to:** Judge Trina L. Thompson (originally assigned to Judge Susan Illston, who entered an Order of Recusal on 2025-10-01; case reassigned to Judge Thompson the same day per General Order No. 44)
- **Parties:** Plaintiff Reddit, Inc.; Defendant Anthropic PBC
- **Cause:** 28 U.S.C. §1331, Federal Question; Nature of Suit: 820 Copyright; Jury Demand: Plaintiff
- **Status shown on docket (as of pull):** Last Updated Aug. 24, 2026, 10:30 p.m.; Date of Last Known Filing May 29, 2026. **Date Terminated: March 30, 2026.** Procedural history: Anthropic removed the case to federal court on federal-question/copyright-preemption grounds (2025-07-03) and simultaneously stipulated to stay the case pending mediation; Reddit moved to remand (Doc #19); the parties completed one round of private mediation on 2025-08-01 that "did not result in a settlement" (per the court's 2025-12-15 order, which reset the ADR deadline to 2026-08-21); a case management and scheduling order dated 2025-12-17 set a jury trial for 2028-02-14 through 2028-03-08 contingent on the pending motion to remand; the court issued a Tentative Order on the remand motion 2026-03-20, then an **Order Granting Defendant's Motion to Remand**, signed 2026-03-28 and filed 2026-03-30, after which the docket shows "***Civil Case Terminated" the same date. The case returns to San Francisco County Superior Court, Case No. CGC-25-625892; this pull did not check the state-court docket for post-remand activity.
- **Sealed items:** none marked "SEALED" among the docket entries reached (the full docket-entry list, read in this pull). Several attachments are marked "Buy on PACER," a PACER-purchase gate, not a seal — not separately itemized in this pull.

## Claims as captioned — per the Notice of Removal's paraphrase of the underlying Complaint (the Complaint's own wording was not recoverable; see pull notes)

The Notice of Removal states, quoting the Complaint by paragraph: "In its Complaint, Reddit asserts five causes of action against Anthropic: 1) breach of contract; 2) unjust enrichment; 3) trespass to chattels; 4) tortious interference with contract; and 5) unfair competition under California's Business and Professional Code section 17200." (Notice of Removal ¶2, citing Compl. ¶¶64-96.)

## Verbatim — the Notice of Removal's own text, including its pinpoint quotations from and citations to the Complaint's numbered paragraphs

> **Notice of Removal ¶1** (quoting/paraphrasing Compl. ¶3): "On June 4, 2025, Reddit, Inc. filed suit against Anthropic in the Superior Court of the State of California, San Francisco County, in Reddit, Inc. v. Anthropic, PBC, Case No. CGC-25-625892. (Exhibit A, Complaint and Jury Demand.) Reddit is a social media website delivering an 'online discussion platform' for purportedly **over 100 million users**. (Compl. ¶ 3.) Anthropic is an artificial intelligence safety and research company developing reliable, interpretable, and steerable artificial intelligence systems, including a family of large language models named Claude. (See Compl., ¶¶ 23-25.)"

> **Notice of Removal ¶3** (citing Compl. ¶¶7, 46, 61, 69-70, 73, 77, 87, 93): "All of Reddit's causes of action are based on its allegation that Anthropic improperly 'scraped' the 'posts' of Reddit users without authorization and used that content for 'commercial gain' in support of its development of the artificial intelligence product offering, 'Claude.' ... Reddit asserts that Anthropic's alleged conduct violates Sections 3, 5, and 7 of the Reddit User Agreement, which together purportedly prohibit data scraping and the use of Reddit content for commercial gain, and further permit Reddit users to retain ownership rights over their posts. (Id., ¶¶ 27-28, 30-31.)"

> **Notice of Removal ¶6** (citing Compl. ¶¶18-20, and quoting Exhibit A to the Complaint, i.e. Reddit's own User Agreement, at its ¶5): "This content includes written stories, links, images, polls, and videos that Reddit users post online... Reddit does not purport to own this content and is instead only a nonexclusive licensee. (See Exhibit A to Compl. at ¶ 5 ('You retain any ownership rights you have in Your Content but you grant Reddit the following [non-exclusive] license to use that Content'))."

> **Notice of Removal ¶7** (citing Compl. ¶¶72-74): "Reddit's claim for unjust enrichment is based exclusively on Reddit's assertion that Anthropic used Reddit users' content without permission or compensation." No dollar figure for the alleged uncompensated value is stated anywhere in the Notice of Removal's text.

> **Notice of Removal ¶8** (citing Compl. ¶¶64-71, 83-96): "Reddit's claims for breach of contract, tortious interference with contract, and at least portions of its unfair competition claim under California Business & Professions Code § 17200 are also premised on its allegations that Anthropic scraped Reddit content without authorization and that Reddit suffered damages as a result." No dollar figure for the alleged damages is stated in the Notice of Removal's text.

> **Notice of Removal ¶10**: "Anthropic was served with Reddit's Complaint on June 6, 2025."

No traffic, referral, revenue, ad-spend, or licence-fee dollar figure beyond the "over 100 million users" figure (Compl. ¶3, quoted above) appears anywhere in the Notice of Removal's own text. The underlying Complaint (Exhibit A) may state further figures — for example on the value of Reddit's data-licensing business, which the complaint's causes of action reference by implication ("commercial gain," "unjust enrichment," "damages") — but its body text could not be recovered from the image-only scan pulled in this session; see pull notes.

## Pull notes — mechanical only

- This is the docket referenced by the prior agent's session-ending note as a candidate ("same case number 1:25-cv-03192") — that note proved to be a mis-transcription or confusion with the unrelated docket *Penske Media Corp. v. Google*, Case No. 1:25-cv-03192, pulled separately in this session (`b-court-penske-v-google-2026-09-22.md`). This Reddit v. Anthropic docket was found independently via a CourtListener case-name/keyword search ("Anthropic advertising," 2026-09-22) while attempting to identify further Anthropic-naming dockets for this cluster, not from the "1:25-cv-03192" note.
- Access to `www.courtlistener.com` was intermittently blocked during this session by what presented as an AWS CloudFront/WAF challenge page (HTTP 202, empty body) rather than the channel's documented `403→ext` behavior (`channels.md` C62). This docket's page returned HTTP 202 on the first nine consecutive attempts (spread across two background polling runs, roughly 11 minutes total, at 25-40 second intervals) before succeeding (HTTP 200) on the tenth attempt with no change in request method, user-agent, or URL — the block appears to be a time-based rate limit rather than a permanent block on this URL. The Chrome extension (the task's named fallback) reported "Browser extension is not connected" throughout this session and was not usable at any point.
- Exhibit A (the state-court Complaint and Jury Demand) is a 43-page scanned image PDF with no embedded text layer — `pdftotext -layout` returned only the per-page "Case 3:25-cv-05643-SI Document 1-1 Filed 07/03/25 Page N of 43" boilerplate that PDF viewers overlay, not the document's own content. No OCR tool was available in this environment (`tesseract`, Python `pymupdf`/`fitz`, `pdf2image`, ImageMagick's `convert`/`magick`, and `ghostscript`/`gs` were all checked and none is installed; the only `convert` found on PATH is the unrelated Windows `convert.exe` disk-format utility). The Complaint's content is therefore captured in this file only indirectly, through the Notice of Removal's own paraphrase and pinpoint paragraph citations (quoted above) — per the raw-pull template's instruction to mark what a pull could not capture rather than omit it silently. `[note: Exhibit A / the underlying Complaint's own body text, pages 1-43, is an uncaptured image scan — no OCR available this session]`.
- The federal docket is **closed** (terminated 2026-03-30) by an order granting Anthropic's motion to remand back to the San Francisco County Superior Court (state court) on jurisdictional grounds specific to this case's procedural posture — this is not a ruling on the merits of any claim, and not a settlement (the docket's own 2025-12-15 order states the parties' one mediation session "did not result in a settlement"). This pull did not check the state-court docket (CGC-25-625892) for any activity after the 2026-03-30 remand; state-court PACER/RECAP-equivalent coverage is outside the channels available to this pull.
- Full docket-entry list (all entries from 2025-07-03 through 2026-03-30) was read from the single-page docket view; no entry marked "SEALED" was found. Coverage of every entry's own attachments was not individually verified.
