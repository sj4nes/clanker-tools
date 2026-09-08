# The research system

Research quality is not the quantity of facts collected. It is the ability to
make claims that are **accurate, traceable, proportionate, and useful**. Build a
system, not a pile of notes.

## The claim ledger

Before drafting, list the claims the book will make. A spreadsheet, database, or
note system with one row per assertion. Fields (full schema in
[`templates/claim-ledger.md`](../templates/claim-ledger.md)):

| Field | Purpose |
|---|---|
| Claim text | The exact assertion as it may appear in the book |
| Claim type | fact / statistic / interpretation / recommendation / quote / anecdote / prediction |
| Evidence needed | Primary study, official dataset, interview, archival record, expert source |
| Source | Full citation and link or document location |
| Source tier | primary / secondary-high-quality / tertiary / discovery |
| Date checked | Essential for changing subjects |
| Confidence | high / medium / low / unresolved |
| Caveats | Limits, counterevidence, population limits, conflicts of interest |
| Chapter | Where the claim may appear |
| Citation status | footnote/endnote / bibliography / permission-required / no-citation-needed |
| Citation check | The `citation-check` calibrated status |

This prevents the most common nonfiction failure: writing persuasive prose around
a remembered fact, then discovering the original source does not support the
sentence.

## The source hierarchy

Prefer sources closest to the underlying evidence.

1. **Primary** — original studies, official reports, court records, datasets,
   transcripts, archival documents, direct interviews, original speeches,
   firsthand documents.
2. **Secondary, high quality** — scholarly books, serious investigative
   reporting, reputable reviews, expert syntheses.
3. **Tertiary** — encyclopedias, general explainers, summaries, broad media
   coverage.
4. **Discovery** — social media, newsletters, blogs, forums, search snippets,
   AI-generated summaries.

Discovery sources help you find leads. They should rarely carry the evidentiary
weight of an important assertion. If a load-bearing claim has only a discovery
source, it is unresolved.

## Verifying citations

Run [`citation-check`](../../citation-check/SKILL.md) on every load-bearing
citation. Treat it as record linkage against authoritative registries plus an
evidence trail — not "I found something similar". Its status
(`verified` / `verified-with-correction` / `likely` / `ambiguous` /
`unresolved` / `contradicted`) is copied into the ledger. A `high`-confidence
claim carrying a formal citation must be `verified` or `verified-with-correction`.

Do arithmetic in the book's own claims (rates, percentages, conversions,
fixed-point financial formulas) with [`bc`](../../bc/SKILL.md) — exact and
reviewable, lowercase identifiers, no `_` or single uppercase letters. Bc
truncates; round explicitly.

## Separate fact from interpretation

A strong book lets the reader see the difference among:

- **What happened** — "The survey found…"
- **What it may mean** — "One interpretation is…"
- **What you recommend** — "For readers in this situation, a prudent next step
  is…"

Keep these as separate ledger rows even when they will share a paragraph. Do not
disguise advice as settled evidence or present interpretation as inevitable fact.
The more controversial, consequential, technical, medical, legal, political, or
financial the subject, the more carefully you state scope, uncertainty, and
competing views.

## Interviewing

If interviews are central:

- Research the subject before speaking to them.
- Prepare open questions, then follow the most specific or surprising answers.
- Ask for scenes, examples, decisions, failures, and documents — not only
  opinions. A useful prompt: *"Take me to the specific moment when you realized
  the old approach was not working. Where were you, what had happened, and what
  did you do next?"* — this invites a scene rather than a generalization.
- Record only with permission; retain notes or transcripts.
- Confirm titles, names, dates, numbers, and quotations.
- **Establish the basis before relying on the material:** on the record /
  background / not for attribution / off the record.
- Never fabricate or "clean up" a quote in a way that changes meaning.

## Permissions and consent

Keep a permissions log (text quotations over fair-use limits, images, figures,
tables, song lyrics) and an interview-consent register (who, when, recording
consent, attribution basis, any review agreed). Close both before production.
