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
- `#outline()` emits its own level-1 heading, which the chapter show-rule
  styled as a chapter and which stepped the counter — every chapter was off by
  one. Fixed with `title: none`.
