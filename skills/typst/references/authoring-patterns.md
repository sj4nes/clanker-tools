# Typst authoring patterns

Reusable patterns for a maintainable manuscript: a centralized preamble, `#show`
recipes, semantic figures / tables / notes, cross-references, and bibliography.

## Preamble anatomy

Everything about *how the document looks* goes in `preamble.typ`, imported once
from `manuscript.typ`. Nothing here is content.

```typst
// preamble.typ

#let apply-base(body) = {
  set page(
    paper: "us-letter",
    margin: (top: 1in, bottom: 1in, left: 1in, right: 1in),
    numbering: "1",
  )
  set text(font: "Libertinus Serif", size: 11pt, lang: "en")
  set par(justify: true, leading: 0.65em, first-line-indent: 1.25em)
  set heading(numbering: "1.1")

  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(above: 0pt, below: 1em, text(size: 15pt, weight: "bold", it))
  }
  show heading.where(level: 2): set text(size: 12.5pt)
  show raw.where(block: true): set block(fill: luma(245), inset: 8pt, radius: 3pt)
  show link: set text(fill: rgb("#1a5fb4"))

  body
}

// reusable helpers
#let note(body) = text(size: 9pt, fill: luma(90))[#body]
#let keyterm(t) = strong(emph(t))
```

```typst
// manuscript.typ
#import "preamble.typ": apply-base, note, keyterm

#set document(title: "Effects of Sleep on Memory", author: ("A. Researcher",))
#show: apply-base

#align(center)[
  #text(17pt, weight: "bold")[Effects of Sleep on Memory] \
  #v(0.4em)
  A. Researcher #super[1] and B. Collaborator #super[2] \
  #note[1. Dept. of Example Studies  2. Institute of Things]
]

#v(2em)

#include "sections/introduction.typ"
#include "sections/methods.typ"

#pagebreak()
= References
#bibliography("references.bib", style: "apa", title: none)
```

Why `#show: apply-base` and not bare `#set` lines at file top: wrapping the
document in one function makes the whole style set a single reusable unit you can
swap for a journal template's function later without editing section bodies.
Bare top-level `#set` rules work too and are simpler for a one-off.

### The anti-pattern to avoid

```typst
#text(size: 16pt, weight: "bold")[Methods]          // DON'T: visual, not semantic
```

```typst
== Methods                                          // DO
```

```typst
#show heading.where(level: 2): set text(size: 12.5pt)   // ...styled once, in the preamble
```

The second survives retargeting to a new template; the first must be hand-edited
at every occurrence.

## `#show` recipes

```typst
// start each top-level section on a new page, no blank leading page
#show heading.where(level: 1): it => { pagebreak(weak: true); it }

// unnumbered abstract heading
#show heading.where(level: 1): it => if it.body == [Abstract] {
  align(center, strong(it.body))
} else { it }

// figures: caption above, smaller caption text
#show figure.caption: set text(size: 9.5pt)
#show figure: set block(breakable: false)

// tighter lists
#show list: set block(spacing: 0.6em)

// small caps for a specific term everywhere
#show "Typst": name => smallcaps(name)

// draft watermark, toggled by a variable
#let draft = true
#show: it => if draft {
  place(center + horizon, rotate(-30deg, text(60pt, fill: luma(230))[DRAFT]))
  it
} else { it }
```

## Figures

```typst
#figure(
  image("figures/results.svg", width: 100%),
  caption: [
    Mean recall by condition. Error bars are 95% CIs.
  ],
  placement: top,          // float to the top of a nearby page
) <fig:results>

Recall was higher in the intervention condition (@fig:results).
```

- `kind: "table"` / `kind: image` controls the counter and the "Figure"/"Table"
  label. `#figure(table(...), caption: [...], kind: table)` numbers tables
  separately.
- `supplement: [Fig.]` overrides the word used in references.
- `placement: none` (default) keeps it inline; `top` / `bottom` / `auto` floats.

## Tables

```typst
#figure(
  table(
    columns: (auto, 1fr, 1fr),
    align: (left, center, center),
    stroke: none,
    table.hline(),
    table.header([Measure], [Control], [Intervention]),
    table.hline(stroke: 0.5pt),
    [Recall],        [0.62],   [0.74],
    [Reaction time], [512 ms], [486 ms],
    table.hline(),
  ),
  caption: [Primary outcomes by condition.],
  kind: table,
) <tab:outcomes>
```

- `columns`: a count, or a tuple of track sizes (`auto`, `1fr`, `3cm`, `20%`).
- `table.header(...)` repeats on page breaks and is styleable via
  `#show table.cell.where(y: 0): strong`.
- For journal-grade tables, prefer a Typst Universe table package over
  hand-tuning strokes.

## Code blocks

````typst
```python
def mean(xs):
    return sum(xs) / len(xs)
```
````

Style via `#show raw.where(block: true): set block(fill: luma(245), inset: 8pt)`.
`#set raw(syntaxes: "…", theme: "…")` adds languages / color themes.

## Footnotes, quotes, links

```typst
A claim.#footnote[Source and nuance here.]

#quote(block: true, attribution: [Walker, 2017])[
  Sleep is the single most effective thing we can do to reset brain and body health.
]

See the #link("https://typst.app/docs/")[official documentation].
```

## Cross-references

```typst
== Methods <methods>
== Results <results>

#figure(...) <fig:x>
$ ... $ <eq:model>

As described in @methods, ... The model (@eq:model) ... shown in @fig:x ...
As @results shows, ...
```

- `#set ref(supplement: "Section")` changes the default word.
- `#show ref: it => …` for full control (e.g. "§3" instead of "Section 3").
- Equation references need the equation to be a display block with a `<label>`.
- A dangling `@foo` renders as visible broken text — catch it by reading the PDF.

## Bibliography

```typst
#bibliography("references.bib", style: "ieee")          // or "apa", "chicago-author-date", a CSL file path
```

- Cite in prose with `@walker2017`; `#cite(<walker2017>, form: "prose")` for
  "Walker (2017) showed…"; `@walker2017[p.~42]` for a locator.
- `.bib` (BibLaTeX) and Hayagriva `.yml` are both accepted.
- `style:` takes a built-in name or a path to a CSL file — use the journal's CSL
  when they publish one.
- Put `#bibliography(...)` where the list should render; `title: none` if a
  manual `= References` heading precedes it.

## Structure with `#include`

- One `manuscript.typ` entrypoint; `#include "sections/foo.typ"` per section.
- Section files contain **markup only** — no `#set page`, no `#import` of the
  preamble (the entrypoint already applied it via `#show: apply-base`).
- Shared `#let` helpers: `#import "preamble.typ": note, keyterm` at the top of a
  section file if it needs them.
- `#include` splices at the point it appears — order in `manuscript.typ` is the
  document order.

## Typst Universe

- Templates: `typst init @preview/<template>:<version> my-doc` scaffolds a
  project from a published template (IEEE, ACM, thesis templates, letters,
  CVs, …). Browse <https://typst.app/universe/>.
- Packages: `#import "@preview/<name>:<x.y.z>"` — **always pin the exact
  version**. Common ones: `cetz` (drawing), `fletcher` (diagrams), `tablex` /
  `tabut` (tables), `mitex` (LaTeX math), `cmarker` (Markdown), `glossarium`
  (glossaries), `hydra` (running headers).
- First fetch of any `@preview` package needs network; it is then cached under
  the Typst package cache.
