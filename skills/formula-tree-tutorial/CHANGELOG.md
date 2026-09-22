# Changelog — formula-tree-tutorial

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

Entries are **version-anchored, not per-commit**: one entry per version this
skill has held. Everything before 2026-09-14 was reconstructed on 2026-09-14
from git history and `docs/skill-versioning.md`, so it records the version
history rather than every change. The full record is

    git log -- skills/formula-tree-tutorial/

## 1.1.0 — 2026-09-22

**The skeleton was missing a beat, and the corpus had been telling us so.**
Nineteen of the 24 shipped tutorials opened with a lead paragraph; the five that
did not (`pendulum`, `why-heat-engines-have-a-ceiling`,
`how-fast-does-sound-travel`, `designing-an-organ-pipe`,
`horns-and-reciprocity`) were the ones that followed
`references/document-structure.md` exactly. The skeleton went from the
provenance blockquote straight to `## How to run this`, so a reader browsing a
tutorial directory saw install text identical in every file. Nineteen
independent departures is the skeleton being wrong, not nineteen authors being
inconsistent — so **the lead is now a required beat** (workflow step 3, and a
"The lead" section in the skeleton reference), and the five tutorials were
given one.

MINOR rather than MAJOR: nothing authored under 1.0.0 is wrong, and the five
affected tutorials are fixed in the same commit. Re-read step 3 before writing
the next one.

Also added: **`verification/`, which this skill did not have** — `check_beats.py`
(the prescribed beats, across every shipped tutorial), `mutation_check.py`
(12 guards, one mutant each), `run.sh`, and a README carrying the displacement
table (5 covered · 3 judgement · 0 gaps).

Found by the harness on its first runs: `hole-in-the-rationals` was missing
`## Where to go next` (added), and **two defects in the checker itself** — the
capstone guard matched only headings starting with "Capstone", and `^#\s+`
matched shell comments inside fenced code blocks, so a title-less tutorial still
reported a title. Both were caught by the mutation check and invisible to the
corpus check, which passed 24/24 before and after the fix.

## 1.0.0 — 2026-09-05

First release, verified at release. (`910df4e`)
