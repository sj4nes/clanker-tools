# Two Refuted Premises — interim research note

    typst compile docs/refuted-premises/manuscript.typ build/note.pdf
    typst watch   docs/refuted-premises/manuscript.typ build/note.pdf   # drafting

Built with typst **0.15.1**. 7 pages, US Letter, single column. No figures, so
no local assets; bibliography in `references.bib`, four entries, IEEE style.

| | |
|---|---|
| entrypoint | `manuscript.typ` — the only file compiled |
| formatting | `preamble.typ` — adapted from the `typst` skill's template; the level-1 pagebreak was removed (a six-page note runs on) and a `verdict` block added |
| body | `sections/01`…`06`, spliced with `#include` in document order |
| output | `build/` — gitignored |

Each section imports the helpers it uses from `../preamble.typ`: `#include`
evaluates a file in its own scope, so the entrypoint's imports are not visible
inside it.

## What it reports

Two claims that justified the `role-deck` skill, both fixtured against naive
agents, both struck (case two refuted 8/8 by execution; case one 3/8 proven —
corrected 2026-09-17, see the top of
`skills/role-deck/verification/premise-fixture/RESULT.md`). The method is now `skills/claim-fixture`; the raw
records are under `skills/role-deck/verification/premise-fixture/` and
`ordering-fixture/`.

Interim: the control named in §6.1 has not been run, and until it is, every
result here is provisional in the direction the note states.
