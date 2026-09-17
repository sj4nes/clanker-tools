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

## Status: Parts I (draft), II.1–II.4 (draft) and III

| Part | Source | Rots? | Built |
|---|---|---|---|
| I — The pile | authored | no | **draft** (2026-09-16, agent-written, awaiting author rewrite; evidence in `claim-ledger.md`) |
| II — The standard (verification bar, displacement tables, versioning) | authored | no | **II.1–II.4 draft** (2026-09-16, agent-written; ledger C-II-01..31) |
| **III — What the standard found** | authored | no | **yes** |
| IV — The catalogue (50 skills) | **generated** from frontmatter | cannot | — |
| V — What's still wrong | **generated** from `BACKLOG.md` | cannot | — |

Parts IV and V are to be *generated* so they cannot go stale, and gated by a
`check-book.sh` in the spirit of `tools/check-skills.sh` — a book that can
silently rot is the failure this repo spends its time closing.

Part III was built first deliberately: it is the content that would justify the
rest. If it does not read well, little is lost.

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
- `#outline()` emits its own level-1 heading, which the chapter show-rule
  styled as a chapter and which stepped the counter — every chapter was off by
  one. Fixed with `title: none`.
