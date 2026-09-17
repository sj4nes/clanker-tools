# Changelog — skill-authoring

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/skill-authoring/

## 1.2.0 — 2026-09-17

**MINOR: an example's evidence restated; nothing to re-do.** Behaviour 5 said
both `role-deck` premises were "refuted 8/8". One was; the other has 3 of 8
subjects' execution proven (`claim-fixture` F10, `role-deck` 2.5.0).

## 1.1.0 — 2026-09-17

**MINOR: behaviour 3 asks for more, and one caution is restated.** Re-read
both. Nothing prescribed before was wrong.

- **Behaviour 3: commit the harness on its own, before the prose.** Measured
  over the 21 behaviour skills, 17 landed harness and prose in one commit, this
  skill included, so the commit-order check proposed in verification gap 2
  would be silent on them. The order leaves a trace only if it is committed.
- **"What this cannot do" cited Luu's eval as showing tutorial-style documents
  "worse than no document at all", and added that all would pass this
  standard.** Read against the article (book ledger C-I-04), the result is
  narrower: one skill worse than no instructions on the runs it influenced,
  one worse possibly by chance, one confounded. The second clause was never
  checked. Both replaced with the measured case.
- `verification/README.md` no longer restates the current failure count, which
  had drifted (35 in prose, 34 in `baseline.txt`).

Found drafting the book's II.7 (ledger C-II-56..59).

## 1.0.0 — 2026-09-15

First release. Found by building the book's fat outline as a concept dependency
graph: 10 of 23 concepts were backed only by `docs/`, so the standard governing
50 skills was not itself invocable. Adds the organizing idea those docs lack —
**the archetype decides which standard applies** — plus an `archetype:` field
migrated across all 50 skills (behaviour 19, capsule 15, tool-fact 10, meta 6)
and a checker that holds each to its own requirements. First run: 35 failures
across 29 skills, with two of the first corrections going to the checker rather
than to any skill.
