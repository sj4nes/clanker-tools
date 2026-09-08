# Typst syntax and the three modes

Typst docs current version: 0.15.1. Source: <https://typst.app/docs/reference/syntax/>.

## The three modes

Typst source is always in one of three modes. Most beginner errors are
mode confusion — a LaTeX token typed in math mode, a bare word typed in markup
where a `#` expression was meant.

| Mode | What it is for | How you enter it | Leaves it |
|---|---|---|---|
| **Markup** | ordinary document text | the default at the top of a `.typ` file, and inside any `[ … ]` content block | end of the block / file |
| **Math** | mathematical notation, Typst's own (not LaTeX) | `$` … `$` | the closing `$` |
| **Code** | expressions, bindings, function calls, control flow | `#` before a single expression in markup; or a `{ … }` code block; or the whole body of a `.typ` file `#import`-ed as a module | end of the expression / block |

### Markup mode

```typst
This is a paragraph. A blank line starts a new one.

*strong* and _emphasis_. Inline `raw text`. A line break \
is a trailing backslash.

= Heading level 1
== Heading level 2

- bullet item
- another
  - nested (indent)

+ numbered item
+ next numbered

/ Term: definition list entry

#link("https://typst.app")[link text]   // bare URLs autolink
#footnote[A footnote body.]

// line comment
/* block comment */
```

`#` in markup switches to code for one expression: `The value is #n.` or
`#calc.round(x, digits: 2)`. Wrap a multi-token expression in parentheses:
`#(a + b)`. Follow a function call with a content block to pass body markup:
`#emph[like this]`.

### Math mode

```typst
Inline: the estimator $hat(theta) = sum_(i=1)^n x_i / n$ is unbiased.

Display (whitespace inside the dollars):
$ R^2 = 1 - (sum_(i=1)^n (y_i - hat(y)_i)^2) / (sum_(i=1)^n (y_i - bar(y))^2) $
```

Key facts about Typst math:

- Multi-letter identifiers are **symbol names**: `alpha`, `beta`, `sum`, `integral`,
  `arrow`, `times`, `dot`, `infinity`. A single letter is a variable: `x`, `n`.
- Function-call syntax works: `frac(a, b)`, `sqrt(x)`, `vec(1, 2, 3)`,
  `mat(1, 0; 0, 1)`, `cases(...)`.
- `_` is subscript, `^` is superscript. Group with parens: `x_(i+1)`, `e^(-x^2)`.
- `/` is a fraction: `a / b`. `&` is an alignment point in multi-line math.
- Text inside math: `"Var"` or `upright("Var")`; `#` drops to code inside math:
  `$ x = #calc.pi $`.
- It is **not LaTeX** — see the LaTeX→Typst math map in
  [`markdown-migration.md`](markdown-migration.md).

### Code mode

```typst
#let n = 120
#let title = "Effects of Sleep on Memory"
#let note(body) = text(size: 9pt, fill: gray)[#body]

#let squared(x) = x * x
#let items = ("a", "b", "c")

#if n > 100 [The sample was large.] else [The sample was small.]

#for it in items [
  - #it
]
```

- `#let` binds a name (value, or a function with parameters).
- `[ … ]` is a **content block**: markup evaluated as a value, passable to
  functions and stored in variables. This is the bridge from code back to markup.
- `{ … }` is a **code block**: a sequence of statements; the last expression is
  its value.
- Named arguments use `name: value`; a trailing content block is sugar for a
  final `body:` argument.

## `#set`, `#show`, `#let` — the styling trio

| Rule | Effect | Example |
|---|---|---|
| `#set f(args)` | change the **default arguments** of element function `f` for the rest of the current scope | `#set text(font: "Libertinus Serif", size: 11pt)` |
| `#show sel: it => …` | **transform** every element matching `sel` | `#show heading.where(level: 1): it => { pagebreak(weak: true); it }` |
| `#show sel: set …` | shorthand: apply a `set` rule only to matched elements | `#show heading.where(level: 2): set text(size: 13pt)` |
| `#show: f` | wrap the **rest of the document** in `f` (template application) | `#show: template.with(title: "…")` |
| `#let name = …` | bind a reusable value or helper | `#let TODO = text(fill: red)[TODO]` |

Rules are **scoped**: a `#set` at file top applies document-wide; the same rule
inside `[ … ]` applies only there. Put document-wide rules in `preamble.typ` and
`#import` it (or `#include` it) from `manuscript.typ`.

Selectors for `#show`: an element function (`heading`, `figure`, `raw`, `table`,
`link`, `ref`, `cite`, `par`, `strong`, `emph`), `heading.where(level: 2)`, a
string or regex (`#show "Typst": name => …`), or a label
(`#show <intro>: …`).

## Labels and references

```typst
== Methods <methods>                       // label attaches to the heading

As shown in @methods, ...                  // @label references it

#figure(image("figures/x.png"), caption: [A caption.]) <fig:x>
See @fig:x.                                 // -> "See Figure 1."
```

- `<label>` binds to the element **immediately before** it.
- `@label` produces a context-appropriate reference (section number, "Figure N",
  citation). Customize with `#set ref(...)` / `#show ref: …`.
- Labels are global; for most elements the reference need not come after the
  definition in source order.
- A broken reference renders visibly in the output (not a silent blank) — grep
  the compiled PDF text for stray `@` or `??`.

## Modules and includes

- `#import "preamble.typ": *` — run that file as a module, bring its bindings
  into scope. Use for shared `#let` helpers and (via re-export) rules.
- `#include "sections/introduction.typ"` — splice that file's **markup** into the
  document at this point. Use for body content.
- `#import "@preview/cmarker:0.1.10"` — a Typst Universe package; **pin the exact
  version**; first fetch needs network.

## Common built-in functions worth knowing

`text`, `par`, `heading`, `strong`, `emph`, `underline`, `link`, `ref`, `cite`,
`footnote`, `quote`, `list`, `enum`, `terms`, `table`, `grid`, `figure`, `image`,
`box`, `block`, `stack`, `align`, `pad`, `pagebreak`, `colbreak`, `line`, `rect`,
`v`, `h`, `repeat`, `numbering`, `outline`, `bibliography`, `raw`, `math.equation`.
Calculation: `calc.round`, `calc.pow`, `calc.sqrt`, `calc.min`, `calc.max`, `calc.abs`.

Full reference: <https://typst.app/docs/reference/>.
