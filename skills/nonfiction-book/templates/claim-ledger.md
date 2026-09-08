# Claim ledger

One row per assertion the book may make. Built **before** drafting, maintained
throughout. Prevents writing persuasive prose around a remembered fact and
discovering later that the source does not support the sentence.

A spreadsheet, database, or notes system. One row schema:

```yaml
claim:
  id: ""                        # stable, e.g. C-014
  claim_text: ""                # the EXACT assertion as it may appear in the book
  claim_type: ""                # fact | statistic | interpretation | recommendation |
                                #   quote | anecdote | prediction
  evidence_needed: ""           # primary study | official dataset | interview |
                                #   archival record | expert source | ...
  source: ""                    # full citation + link or document location
  source_tier: ""               # primary | secondary-high-quality | tertiary | discovery
  date_checked: ""              # ISO date — essential for changing subjects
  confidence: ""                # high | medium | low | unresolved
  caveats: ""                   # limits, counterevidence, population limits, conflicts of interest
  chapter: ""                   # where the claim may appear
  citation_status: ""           # footnote/endnote | bibliography | permission-required |
                                #   no-citation-needed
  citation_check: ""            # citation-check status: verified | verified-with-correction |
                                #   likely | ambiguous | unresolved | contradicted | n/a
  drafting_status: ""           # blocking | draft-anyway | resolved
```

## Rules

- **Separate fact, interpretation, and recommendation into distinct rows**, even
  when they will sit in one paragraph. "The survey found X" / "one reading of X
  is Y" / "for readers in this situation, a prudent step is Z" are three claims.
- **Source hierarchy.** Prefer sources closest to the evidence:
  1. **Primary** — original studies, official reports, court records, datasets,
     transcripts, archival documents, direct interviews, firsthand documents.
  2. **Secondary, high quality** — scholarly books, serious investigative
     reporting, reputable reviews, expert syntheses.
  3. **Tertiary** — encyclopedias, general explainers, broad media coverage.
  4. **Discovery** — social media, newsletters, blogs, forums, search snippets,
     AI summaries. These find leads. They do **not** carry a load-bearing claim.
- A `high`-confidence claim with a formal `citation_status` must have a
  `citation_check` of `verified` or `verified-with-correction`.
- A claim may enter drafting only when `drafting_status` is `resolved` or
  explicitly `draft-anyway` (with the gap logged in the unresolved-research
  list).
- Controversial, consequential, technical, medical, legal, political, or
  financial claims must state scope, uncertainty, and competing views in
  `caveats`.

## Example row

```yaml
claim:
  id: C-014
  claim_text: "Employees who lacked a first-week manager meeting left within a year
    at roughly twice the rate of those who had one, in the 2024 cohort studied."
  claim_type: statistic
  evidence_needed: primary dataset + methods note
  source: "Acme HR Analytics, 2024 onboarding cohort study, internal report v3, pp. 8-11"
  source_tier: primary
  date_checked: 2026-09-08
  confidence: medium
  caveats: "Single company; n=430; observational, not randomized; 'manager meeting'
    self-reported; attrition includes involuntary exits."
  chapter: 3
  citation_status: endnote
  citation_check: n/a
  drafting_status: draft-anyway
```

## Gate to Phase 4 (drafting)

- [ ] Every claim a chapter's draft depends on is `resolved` or `draft-anyway`.
- [ ] No `high`-confidence formally-cited claim has an unresolved `citation_check`.
- [ ] No load-bearing claim has `source_tier: discovery`.
- [ ] Fact / interpretation / recommendation are in separate rows.
