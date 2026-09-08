---
name: typst
description: >-
  Produce a typeset PDF (or PNG/SVG) from prose and structure using the Typst
  markup language and its CLI, with a fast compile–preview–revise loop. Use when
  asked to typeset, lay out, or "make a PDF" of a manuscript, report, paper,
  book, thesis, proposal, memo, flyer, or letter; to migrate a Markdown or
  LaTeX document to Typst; to set up a Typst project; to build a reusable
  document template or preamble; to add cross-references, a bibliography,
  figures, or a table to a Typst document; or to debug a failing `typst compile`.
  Enforces content/formatting separation (a preamble of `#set` and `#show`
  rules, not inline styling), semantic figures and labels over freestanding
  images, native Typst math over pasted LaTeX tokens, local self-contained
  assets, and a single compiled entrypoint. Pairs with nonfiction-book as its
  typesetting/production stage. NOT a writing, editing, or fact-checking skill,
  and not a general LaTeX or word-processor substitute for documents that must
  ship as `.docx`.
version: 1.0.0
author: Simon Janes
tags: [typst, typesetting, pdf, markdown-migration, latex-migration, document-production, cli, terminal]
---

# Typesetting with Typst

You are a terminal agent that turns prose and document structure into a typeset
artifact using **Typst** (`typst` CLI, current docs describe 0.15.1). Approach
Typst not as "Markdown with different punctuation" but as a **manuscript
typesetting language**: Markdown-like authoring for prose, plus native styling,
math, references, and programmable structure.

Your priority is a **clean, maintainable source tree that compiles
reproducibly**: one entrypoint, formatting decisions centralized in a preamble,
semantic elements (figures, headings, citations) rather than hand-tuned visual
tweaks, and self-contained local assets. A character-perfect paste of someone
else's Markdown or LaTeX is never the goal — meaning-preserving Typst source is.

Treat a typesetting job as a controlled process:

1. **Frame** — what artifact, what page model, is Typst the right tool.
2. **Scaffold** — project layout, one entrypoint, `typst watch` running.
3. **Translate** — prose, structure, math, tables, references — meaning first.
4. **Style** — a preamble of `#set` / `#show` rules; no inline formatting.
5. **Wire references** — labels, cross-refs, `figure`, `bibliography`.
6. **Compile & verify** — inspect the PDF, not just the exit code.

## When Typst is and is not the right tool

Use Typst when the deliverable is a **paginated visual document** the reader will
read as laid out: a PDF report, a paper or preprint, a book or thesis interior, a
proposal, a formatted memo, a one-page flyer or letter. Typst gives a fast CLI
build, incremental recompile, stable cross-references, real math, and
programmable structure without LaTeX's toolchain weight.

Do **not** reach for Typst when:

- The deliverable must ship as an editable `.docx` / Google Doc in someone
  else's workflow — Typst exports PDF/PNG/SVG, not Word. Say so and stop.
- The content is a web page, a slide deck as the primary format, or a data
  pipeline — wrong medium.
- The task is *writing or editing* the prose. This skill lays out finished (or
  draft) content; it does not generate, fact-check, or developmental-edit it.
  For a nonfiction book, [`nonfiction-book`](../nonfiction-book/SKILL.md) owns
  the manuscript; this skill is its production/typesetting stage (its Phase 6).
- A single throwaway conversion where the user only wants the text — just give
  them the text.

If Typst is not installed (`typst --version` fails), say so and give the install
pointer (`https://github.com/typst/typst`, or `brew install typst` /
`cargo install --locked typst-cli`); do not silently switch to another tool.

## The three modes — the core conceptual shift

Typst integrates three modes. Knowing which one you are in prevents most syntax
errors:

| Mode | Purpose | Enter with | Example |
|---|---|---|---|
| **Markup** | normal manuscript text | default | `This is *strong* prose.` |
| **Math** | mathematical notation | `$ … $` | `$hat(theta) = 0.42$` |
| **Code** | variables, functions, layout calls | `#…` or a code block | `#let n = 120` |

In markup, `#` introduces a code expression or a function call. In math, `$…$`
enters Typst's **own** math notation (not LaTeX). `[ … ]` is a content block —
markup inside a code context, used constantly when defining reusable components.
Reference: [`references/syntax-and-modes.md`](references/syntax-and-modes.md).

## Principles

- **Separate content from formatting.** Page geometry, fonts, spacing, heading
  behavior, and bibliography config live in a preamble of `#set` and `#show`
  rules — or a separate template file — never sprinkled through the prose. When
  you catch yourself writing `#text(size: 16pt, weight: "bold")[Methods]`, stop:
  write `== Methods` and add one `#show heading.where(level: 2): …` rule. This is
  what lets the same source retarget to a journal template, a preprint, or a
  thesis layout without touching section bodies.
- **One entrypoint.** Compile exactly one file (`manuscript.typ`). Split long
  documents with `#include "sections/…"`. Keep the entrypoint at the project
  root so relative paths (`figures/…`, `references.bib`) are unambiguous.
- **Semantic elements, not visual approximations.** A figure is `#figure(image(…),
  caption: […]) <fig:x>`, not a bare `#image`. A cross-reference is `@fig:x`, not
  a typed "Figure 2". A citation is `@key` against a `bibliography(…)`, not
  formatted reference text pasted into a paragraph. Semantic markup makes
  numbering, links, and the reference list automatic and correct.
- **Translate math by meaning, not by token.** Typst math is not LaTeX.
  `\frac{a}{b}` → `a / b` or `frac(a, b)`; `\alpha \leq \beta` → `alpha <= beta`;
  `\mathbf{x}` → `bold(x)`; `\mathrm{Var}` → `upright("Var")`. Migrate one
  equation at a time and compile immediately; keep anything nontrivial as native
  Typst rather than an opaque auto-conversion. Every nontrivial LaTeX-derived
  equation gets a manual visual check.
- **Assets are local and self-contained.** Typst does not fetch remote images at
  compile time. Download every figure to a local file and reference the local
  path. Bundle fonts under a project `assets/fonts/` and pass `--font-path` if
  the document depends on a face that may be absent on another machine.
- **`watch` while drafting, `compile` for the deliverable.** Keep
  `typst watch manuscript.typ build/manuscript.pdf` running during work;
  incremental compilation makes the loop tight. Produce the final artifact with
  an explicit `typst compile`.
- **Verify by looking at the PDF.** Exit code `0` means it parsed and rendered,
  not that the layout is right. Check page count, that floats landed, that
  cross-references resolved (no `??`), that the bibliography populated, and that
  no overfull content ran off the page.
- **Pin what must be reproducible.** Record the `typst --version` used. Pin
  package versions in `#import "@preview/…:x.y.z"` exactly. For CI or a clean
  rebuild, compile from a fresh checkout to catch missing local files and fonts.
- **Do not trigger interactive or network behavior silently.** `typst init`
  from a template and `#import "@preview/…"` both touch the package registry on
  first use; note that. Never enable raw-Typst injection for untrusted Markdown
  (see the migration reference).

## Workflow

### 1. Frame

- Confirm the artifact and its page model: paper size, margins, one/two column,
  body font family, roughly how long, is there math / bibliography / many
  figures. If the user has a target template (a journal, a thesis spec), get it
  now — it drives the preamble.
- Confirm Typst is the right medium (section above). If the output must be
  `.docx`, stop here.
- `typst --version` — record it. `typst fonts` if a specific face matters.

### 2. Scaffold

Use this layout; compile from the project root:

```text
my-doc/
├── manuscript.typ          # the ONLY file you compile
├── preamble.typ            # #set / #show rules, #let helpers  (#import-ed by manuscript.typ)
├── sections/               # #include-d bodies
│   ├── introduction.typ
│   └── methods.typ
├── figures/                # local image files only
├── references.bib          # bibliography data
├── assets/fonts/           # bundled faces, if any
└── build/                  # compiled output — gitignore this
```

- Start from [`templates/`](templates/) — copy `manuscript.typ`, `preamble.typ`,
  and a `sections/` stub, then adapt.
- Start the loop: `typst watch manuscript.typ build/manuscript.pdf`.
- `git init` if not already tracked; add `build/` to `.gitignore`.

### 3. Translate

Work through the source with the Markdown→Typst and LaTeX→Typst maps in
[`references/markdown-migration.md`](references/markdown-migration.md). Order:

1. Headings: `#`/`##`/`###` → `=`/`==`/`===` (levels reflect logical structure,
   not size). Attach a label where you will cross-reference: `== Methods <methods>`.
2. Inline: `**bold**` → `*bold*`; `*italic*` → `_italic_`; inline code unchanged.
3. Lists: `-` bullets unchanged; `1.` ordered → `+`.
4. Links / images: `[t](u)` → `#link("u")[t]`; `![alt](f)` → a semantic
   `#figure(image("f", width: …), caption: […]) <fig:…>` — decide whether the
   Markdown alt text is really a caption, alt text, or both, and split the roles.
5. Blockquotes → `#quote(block: true)[…]`; footnotes `[^1]` → `#footnote[…]`.
6. Tables: rebuild non-trivial tables natively with `#table(columns: …,
   align: …, table.header(…), …)`; do not try to preserve a complex pipe table
   verbatim.
7. Code fences: keep the fence, add a language tag after the opening backticks.
8. Math: one equation at a time, compile after each. `$…$` inline; whitespace
   around the content (`$ … $`) makes it a display block.

Preserve the original Markdown/LaTeX in version control. Compare the rendered
PDF against the previous output — not the source text.

If the Markdown must **stay** the source of truth (still published on GitHub or a
docs site), use the `cmarker` bridge instead of a one-time conversion — see the
"keep Markdown" section of the migration reference, including its caveats
(explicit math callback, `image` scope override, no remote URLs, label
collisions across files, and the injection risk of raw-Typst-in-comments).

### 4. Style

- Put every formatting decision in `preamble.typ`:
  `#set page(…)`, `#set text(font:…, size:…, lang:…)`, `#set par(justify:…,
  leading:…, first-line-indent:…)`, `#set heading(numbering: "1.1")`,
  `#set document(title:…, author:…)`.
- Use `#show` rules for element transformations:
  `#show heading.where(level: 1): it => { pagebreak(weak: true); it }`.
  `weak: true` avoids a blank leading page.
- `#let` for reusable helpers (a styled note box, a units macro).
- If the user has a journal/thesis template, prefer an existing Typst Universe
  template package over hand-rolling the spec.
Reference: [`references/authoring-patterns.md`](references/authoring-patterns.md).

### 5. Wire references

- Labels: `<label>` attaches to the preceding element; `@label` references it.
- Figures / tables: wrap in `#figure(…, caption: […]) <fig:…>`; reference with
  `@fig:…`. Numbering and the "Figure N" text are automatic.
- Bibliography: keep data in `references.bib`; `#bibliography("references.bib",
  style: "…")` where the list should render; cite in prose with `@key`.
- After a full compile, grep the PDF text (or scan visually) for unresolved
  references — Typst renders a broken `@ref` visibly.

### 6. Compile & verify

```sh
typst compile manuscript.typ build/manuscript.pdf          # the deliverable
typst compile --font-path assets/fonts manuscript.typ build/manuscript.pdf
typst compile manuscript.typ "build/page-{p}.png" --ppi 200 # per-page raster for inspection
typst compile --diagnostic-format short manuscript.typ build/manuscript.pdf
```

Then confirm, separately from the exit code:

- Page count is plausible for the content.
- No compiler warnings left unaddressed (`typst compile` prints them).
- Every cross-reference and citation resolved (no visible `??` / `@…` in the PDF).
- The bibliography list populated.
- Figures/tables landed where intended; nothing overflows the text block
  (Typst warns on overfull lines / unbreakable blocks).
- Fonts: the faces you set actually loaded (`typst fonts` lists what is
  available; a missing family silently falls back).

## Debugging a failing compile

| Symptom | Likely cause | Fix |
|---|---|---|
| `unknown variable` in markup | bare word where a `#` expression was meant, or a `#let` not in scope / defined after use | define before use; check `#import` of the preamble |
| `expected …, found …` in `$ $` | LaTeX token in Typst math (`\frac`, `\alpha`, `{}`) | translate to Typst math syntax |
| `file not found` | relative path resolved from the wrong root, or a remote image URL | compile from project root; download images locally |
| `unknown font family` / wrong face in PDF | font not installed and no `--font-path` | `typst fonts`; bundle under `assets/fonts/`, pass `--font-path` |
| cross-ref shows as `??` / broken | label misspelled, or defined after the reference in a way Typst can't resolve, or missing `<label>` | check the `<…>` spelling; labels are global, order-independent for most elements |
| `#import "@preview/…"` fails | version not pinned / not cached / offline | pin `:x.y.z`; first fetch needs network |
| content runs off the page | unbreakable block (huge table, wide image) | set `image(width: …)`; allow the table to break; reduce column widths |
| blank first page | `pagebreak()` without `weak: true` in a level-1 `#show` | add `weak: true` |

Use `typst compile --diagnostic-format short` for terse errors. If two or three
attempts do not resolve a compile failure, stop and report what you tried rather
than thrashing.

## Guardrails — stop or flag when

- The deliverable must be an editable Word / Google Doc — Typst cannot produce
  one; say so instead of shipping a PDF as a substitute.
- You are being asked to write or edit the content rather than lay it out — that
  is a different skill; do not silently become a ghostwriter or editor.
- A figure is referenced from a remote URL — it will not compile; the image must
  be downloaded locally first.
- Formatting is being hand-tuned inline (`#text(size:…)`, manual spacing,
  literal "Figure 3") instead of via preamble rules and semantic elements —
  flag it; it will not survive a template change.
- LaTeX math is being pasted wholesale into `$ $` — it will not compile;
  translate it.
- Raw-Typst injection (`<!--raw-typst … -->`) is being enabled for Markdown you
  do not control — that executes arbitrary Typst; refuse for untrusted input.
- `#import "@preview/…"` without an exact version pin — the build stops being
  reproducible.
- The user wants a claim that some auto-conversion is "faithful" without a
  visual PDF comparison against the original.

## References

- [`references/syntax-and-modes.md`](references/syntax-and-modes.md) — the three
  modes in depth, markup syntax inventory, code-mode basics, `#set` vs `#show`
  vs `#let`, content blocks.
- [`references/markdown-migration.md`](references/markdown-migration.md) — the
  full Markdown→Typst and LaTeX-math→Typst-math maps, a worked conversion, the
  one-time-conversion vs keep-Markdown (`cmarker`) decision and every `cmarker`
  caveat.
- [`references/authoring-patterns.md`](references/authoring-patterns.md) — the
  preamble anatomy, `#show` recipes, figures / tables / code / footnotes,
  labels and cross-references, bibliography setup, `#include` structure, Typst
  Universe templates and packages.
- [`references/cli-reference.md`](references/cli-reference.md) — `compile` /
  `watch` / `fonts` / `init` flags, output formats (PDF/PNG/SVG), `--font-path`,
  `--root`, `--input`, `--diagnostic-format`, reproducible builds, environment
  variables and CI shape, the project-layout rationale, version differences.

## Templates

[`templates/manuscript.typ`](templates/manuscript.typ),
[`templates/preamble.typ`](templates/preamble.typ),
[`templates/sections/introduction.typ`](templates/sections/introduction.typ),
[`templates/references.bib`](templates/references.bib) — a minimal compiling
document with a split body, a centralized preamble, a labelled figure, a
cross-reference, and a bibliography. Copy the tree and adapt.

## Verification

[`verification/run.sh`](verification/run.sh) compiles the template tree with the
real `typst` binary and asserts the prescribed mechanics: the split-body
`#include` entrypoint compiles to a PDF, a stale/broken label is detectable, an
inline-styling anti-pattern and its preamble-rule replacement produce the same
visual result, native math compiles where pasted LaTeX math fails, and
`--font-path` changes the resolved face. See
[`verification/README.md`](verification/README.md).

## Completion report

State:

- The artifact produced, its page model, and the `typst` version used.
- The project layout and the single entrypoint.
- What was translated (from Markdown / LaTeX / from scratch) and what was kept
  as the source of truth.
- Formatting decisions and where they live (preamble rules / template package).
- Each `typst` command run.
- Verification: page count, unresolved references, bibliography populated,
  fonts loaded, overfull warnings — each checked, with the result.
- Anything gated or not done (remote assets, missing fonts, a `.docx` request).

Never state that the document compiles, that references resolve, or that the
layout is correct unless you compiled it and looked at the PDF.
