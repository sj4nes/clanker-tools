# The Missing Manual — a PDF release of this corpus

    typst compile docs/book/book.typ build/book.pdf
    typst watch   docs/book/book.typ build/book.pdf   # drafting

typst **0.15.1**. US Letter, single column, chapter openers, running heads.
`build/` is gitignored: the PDF is a **release artifact**, not a tracked file.

## Why a book

The corpus's most valuable content is its findings, and they are currently in
the least readable artifact a project has. At the time of writing: 4,122 lines
of commit-message body across 161 commits, 24 of whose subject lines report a
finding. Nobody reads a git log as a document.

## Status: Parts I (draft), II (draft), III, IV, V and VI

| Part | Source | Rots? | Built |
|---|---|---|---|
| I — The pile | authored | no | **draft** (2026-09-16, agent-written, awaiting author rewrite; evidence in `claim-ledger.md`) |
| II — The standard (verification bar, displacement tables, versioning) | authored | no | **II.1–II.7 draft** (2026-09-16/17, agent-written; ledger C-II-01..62) |
| **III — What the standard found** | authored | no | **yes**; evidence pass 2026-09-17 (ledger C-III-01..21) |
| IV — The catalogue (53 skills) | **generated** from frontmatter | cannot | **yes** (2026-09-17); framing chapter authored |
| V — What's still wrong | **generated** from `BACKLOG.md` | cannot | **yes** (2026-09-17); framing chapter authored |
| VI — What the checks turned into (24 tutorials) | **generated** from `skills/*/tutorial/` | cannot | **yes** (2026-09-17); framing chapter authored |

Parts IV and V are *generated* so they cannot go stale, and gated by
`tools/check-book.sh` in the spirit of `tools/check-skills.sh` — a book that can
silently rot is the failure this repo spends its time closing.

    sh docs/book/tools/check-book.sh         gate: stale? warns? compiles?
    sh docs/book/tools/check-book.sh --fix   regenerate first, then gate
    python3 docs/book/tools/check-book-mutations.py   prove the gate can fail

The gate has named gates (`typstlib`, `part4`, `part5`, `part6`, `compile`,
`warnings`, plus each generator's own refusal), and
`check-book-mutations.py` breaks each one on a scratch copy and requires it to
fire **alone** — the standard of `docs/verifying-skills.md` §8, and the same
one `check-intro-order-mutations.py` is held to. It runs a no-mutation control
too, without which a broken scratch copy would score every mutation as caught.

    tools/corpus.py        reads skills/*/ into records (both generators)
    tools/typstlib.py      Markdown -> Typst escaping, with a self-test
    tools/gen-catalogue.py Part IV, from frontmatter/CHANGELOG/verification
    tools/gen-open.py      Part V, from the open `- [ ]` items of BACKLOG.md
    tools/gen-tutorials.py Part VI, from skills/*/tutorial/*.md
    tools/gen-facts.py     corpus-facts.typ — the corpus counts as constants

Part VI is a **catalogue, not a reprint**: the tutorials run under `upmd` in a
terminal, which is the point of them, and they come to ~58,000 words. The entry
gives what each teaches, how much of it the reader runs rather than reads, and
the command.

The generators **report absence rather than guessing**: a skill with no
displacement table says so, and a skill with a table whose counts are only in
prose says that instead. Those absences are the corpus's, and they leave the
book the day they are fixed in the repository.

Part III was built first deliberately: it is the content that would justify the
rest. If it does not read well, little is lost.

## The corpus-count registry

`corpus-facts.typ` holds every corpus figure as a named constant, so a chapter
writes `#n-skills` and a number is typed once:

    #import "../../corpus-facts.typ": corpus-asof, n-skills

It exists because the same figures were retyped into four places and had already
drifted apart (`drift-check.md` §4). It is a sibling of `preamble.typ`, not part
of it: the preamble's first line is that nothing in it is content, and these are
content.

Two kinds of value, and the split is the point:

- **gated** — structural counts (skills, archetypes, tables, tutorials, MAJOR
  bumps). Regenerated and diffed by `check-book.sh` like any generated part.
- **stamped** — the as-of date, commit count, corpus age. These move with *every
  commit*, so diff-gating them would fail the build after each one, and a gate
  that cries wolf gets switched off. They are carried forward untouched and move
  only on `gen-facts.py --stamp`. The mutation suite asserts both halves: a
  hand-edited structural count fails the gate, a stale stamp does not.

## Rewrite-pass markers

Parts I and II are agent drafts awaiting the author's rewrite. Defects that must
be decided *during* that rewrite are marked in place, as Typst comments, so they
cannot be missed by reading the PDF:

    grep -rn "REWRITE-PASS" docs/book/parts/

Each names the finding in [`drift-check.md`](drift-check.md) it comes from and
the decision needed. They are comments, so they never render. Four are open, all
from §4 (corpus counts stated with inconsistent as-of discipline). Delete a
marker when its decision is made.

## Sidebars — what the standard caught while the book was built

[`sidebars.md`](sidebars.md) — the running record of moments where the method
this book describes, applied to the book's own construction, caught something
reading had not. Eleven so far, in both directions: a corpus practice catching a
defect in the book's toolchain, and writing the book catching a defect in the
corpus. Each is a candidate for a `#sidebar[...]` in a chapter; one is cut in
(II.2). Add a row whenever it happens — the bar is that the check has to have
been the thing that caught it.

## Drift checks

[`drift-check.md`](drift-check.md) — the built book audited against the
positioning brief, fat outline, claim ledger and GAPS, per the `nonfiction-book`
skill's Pass 1. Last run 2026-09-17 at `845ea24`: Parts I–III match the outline
chapter for chapter and all four promised outcomes are delivered; five findings
open, one of which (Part VI against the brief's exclusions) needs an author
decision. Re-run it whenever a part is added or the brief changes.

## Layout

    book.typ                 the ONLY file compiled
    preamble.typ             every formatting decision
    parts/03-findings/       chapters, spliced with #include
    build/                   output, gitignored

Each chapter imports the helpers it uses from `../../preamble.typ`: `#include`
evaluates a file in its own scope, so the entrypoint's imports are invisible
inside it.

## Defects found by looking at the PDF, not the exit code

Four, all of which compiled cleanly:

- `let h = query(...)` shadowed Typst's `h()` spacer, so `#h(1fr)` in the
  running head resolved to `none` — *"expected function, found none"*.
- `**bold**` is Markdown, not Typst: it renders as two *empty* bolds. Typst
  warns `no text within stars`, which is easy to scroll past.
- `counter(heading)` never advances when `numbering: none`, so every chapter
  eyebrow read "Chapter 0". Fixed with a dedicated counter.
- A changelog entry styled `**MAJOR.** **The headline.** body` put its second
  pair of stars into Part IV as literal `\*\*`: the parser read the headline
  as everything after the level, markers included. Found by the mutation test,
  not by reading — the page looked plausible.
- Sidebars set in a sans with no italic variant (the installed Inter is
  upright-only) rendered every `#emph` inside them as roman. No warning: Typst
  has the family, just not the style. `check-book.sh` now gates the sidebar
  family for a real italic, and the mutation suite sets it back to Inter to
  prove the gate fires.
- `#outline()` emits its own level-1 heading, which the chapter show-rule
  styled as a chapter and which stepped the counter — every chapter was off by
  one. Fixed with `title: none`.
