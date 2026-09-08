# Migrating Markdown (and LaTeX math) to Typst

Two sensible routes:

- **A. One-time conversion to native Typst** — the document lives in Typst now.
- **B. Keep Markdown, render it through Typst** (`cmarker`) — the same `.md` must
  stay publishable on GitHub / a docs site.

Pick A unless something external still needs the Markdown.

## Markdown → Typst map

| Markdown | Typst | Notes |
|---|---|---|
| `# Title` | `= Title` | one `=` per level; `##` → `==` |
| `**bold**` | `*bold*` | single asterisk pair is strong |
| `*italic*` / `_italic_` | `_italic_` | `_…_` is conventional Typst emphasis |
| `` `code` `` | `` `code` `` | inline raw, unchanged |
| ` ```lang ` fence | ` ```lang ` fence | keep the fence; language tag after the backticks |
| `- item` | `- item` | unchanged |
| `1. item` | `+ item` | Typst ordered lists use `+` |
| `> quote` | `#quote(block: true)[quote]` | |
| `[text](url)` | `#link("url")[text]` | bare URLs autolink |
| `![alt](img.png)` | `#figure(image("img.png", width: 85%), caption: [alt])` | decide: caption, alt text, or both — Typst keeps them distinct (`image(..., alt: "…")`) |
| `---` (rule) | `#line(length: 100%)` | a typographic rule, not a syntax token |
| `[^1]` / `[^1]: …` | `#footnote[…]` | inline function, placed where the marker goes |
| `<!-- comment -->` | `// comment` or `/* … */` | |
| `| a | b |` table | `#table(columns: …, …)` | rebuild non-trivial tables natively |
| front matter (`--- … ---`) | `#set document(...)` + `#let` | no YAML front matter concept |
| `$x^2$` (MathJax/KaTeX) | `$x^2$` | similar delimiters, **different math language** — see below |
| `$$ … $$` | `$ … $` with surrounding whitespace | whitespace inside the dollars makes it display |
| Mermaid / PlantUML fences | a diagram package, or an external SVG via `image(...)` | no built-in Mermaid |
| GitHub task list `- [ ]` | `cmarker` supports it when configured; native: a custom `#let` | |

## LaTeX math → Typst math map

Typst math is **not** LaTeX. This is where auto-conversion breaks most often.

| LaTeX | Typst | |
|---|---|---|
| `x^2 + y_i` | `x^2 + y_i` | same |
| `x_{i+1}` | `x_(i+1)` | braces → parens for grouping |
| `\frac{a}{b}` | `a / b` or `frac(a, b)` | |
| `\sqrt{x}` | `sqrt(x)` | |
| `\alpha \beta \gamma` | `alpha beta gamma` | symbol names, space-separated |
| `\leq \geq \neq \approx` | `<= >= != approx` | |
| `\times \cdot \pm` | `times dot plus.minus` | |
| `\sum_{i=1}^{n}` | `sum_(i=1)^n` | |
| `\int_0^\infty` | `integral_0^infinity` | |
| `\mathbf{x}` | `bold(x)` | |
| `\mathrm{Var}` / `\operatorname{Var}` | `upright("Var")` or `"Var"` | text in math |
| `\hat{x}` `\bar{x}` `\vec{x}` `\tilde{x}` | `hat(x)` `bar(x)` `vec(x)` `arrow(x)` `tilde(x)` | `vec(...)` with commas is a column vector; use `arrow(x)` for the accent |
| `\left( … \right)` | `( … )` | Typst auto-sizes delimiters |
| `\begin{matrix} 1 & 0 \\ 0 & 1 \end{matrix}` | `mat(1, 0; 0, 1)` | `,` columns, `;` rows |
| `\begin{cases} … \end{cases}` | `cases(a "if" x>0, b "else")` | |
| `\\` line break in align | newline, with `&` alignment points | |
| `\text{...}` | `"..."` or `text[...]` | |
| `\,` `\;` `\quad` | `thin` `med` `quad` (or `#h(1em)`) | |

Safe process for equations:

1. Copy equations that use only letters, sub/superscripts, fractions, and common
   symbols. Compile immediately.
2. Replace LaTeX commands one category at a time (accents, then operators, then
   delimiters, then environments).
3. Inspect line breaks, matrices, cases, and custom `\newcommand` macros by hand
   — reimplement macros as `#let`.
4. Keep anything genuinely complex as native Typst; do not ship an opaque
   auto-conversion.

## Worked conversion

**Markdown source:**

```md
# Effects of Sleep on Memory

## Introduction

Sleep is **important** for memory consolidation. Prior work highlights
*slow-wave sleep*.

- Adults aged 18–35
- Two laboratory sessions

The primary model was $y = \beta_0 + \beta_1 x + \varepsilon$.

> Sleep may actively support memory processing.

![Study workflow](figures/workflow.png)

[^1]: A short methodological note.
```

**Native Typst:**

```typst
= Effects of Sleep on Memory

== Introduction <intro>

Sleep is *important* for memory consolidation. Prior work highlights
_slow-wave sleep_.

- Adults aged 18–35
- Two laboratory sessions

The primary model was $y = beta_0 + beta_1 x + epsilon$.

#quote(block: true)[
  Sleep may actively support memory processing.
]

#figure(
  image("figures/workflow.png", width: 85%),
  caption: [Study workflow.],
) <fig:workflow>

As outlined in @intro, the design used two sessions (see @fig:workflow).

#footnote[A short methodological note.]
```

The conversion is not merely syntactic: the figure became a semantic object with
a caption and a label; the image width is deliberate; math uses Typst symbols;
the label makes the cross-reference stable.

## Route A: one-time conversion

1. Preserve the original in version control.
2. Create `manuscript.typ`; translate headings, inline marks, lists, links,
   images, tables, footnotes, equations, citations — in that order.
3. Replace Markdown-specific extensions (front matter, fenced divs, raw HTML
   styling, Pandoc attributes, `\newcommand`, Mermaid, renderer-specific
   anchors) with Typst-native equivalents.
4. Move all visual rules into `preamble.typ`.
5. `typst watch` throughout.
6. Compare the **rendered PDF** to the previous output, not the source text.

For a bulk first pass, Pandoc (`pandoc in.md -o out.typ`) beats hand-typing, but
its output needs cleanup before it is maintainable source — treat it as a draft,
not a result. The `cmarker` docs make the same recommendation.

## Route B: keep Markdown, render through `cmarker`

```typst
#import "@preview/cmarker:0.1.10"

#set page(paper: "us-letter", margin: 1in)
#set text(font: "Libertinus Serif", size: 11pt)

#cmarker.render(
  read("manuscript.md"),
  scope: (
    image: (source, ..args) => image(source, ..args),
  ),
)
```

Compile normally: `typst watch manuscript.typ build/manuscript.pdf`.

`cmarker` parses CommonMark + extensions (headings, lists, tables, footnotes,
blockquotes, links, images, figures, task lists when configured, configurable
heading-label generation) and can `read()` an external `.md`.

### `cmarker` caveats — it is an embedding bridge, not a universal converter

- **Math needs an explicit callback** — Typst does not parse LaTeX math. Wire
  `math:` in `scope` to e.g. `mitex` (`#import "@preview/mitex:…": mitex`).
- **Image paths / behavior** often need the `image` override in `scope` shown
  above.
- **No remote images.** Typst never fetches URLs at compile time — download
  figures locally first.
- **Label collisions.** Rendering multiple `.md` files separately can collide on
  generated heading labels — concatenate them, or set `label-prefix` / explicit
  IDs.
- **Raw-Typst injection.** If enabled, `<!--raw-typst … -->` comments execute
  arbitrary Typst. Fine in a trusted manuscript repo; **never enable it for
  Markdown you do not control.** `cmarker` also supports exclusion blocks for
  content meant only for non-Typst renderers.

### Hybrid source (portable prose, Typst only where Markdown is limiting)

```md
# Results

The primary outcome improved by **12%**.

<!--raw-typst
#figure(
  image("figures/results.png", width: 90%),
  caption: [Primary outcome by condition.],
) <fig:primary-result>
-->

As shown in [@fig:primary-result], the intervention performed better.
```

`cmarker`'s documented citation form is `[@key]`, integrating with Typst labels
and `#bibliography`.

Sources: <https://typst.app/docs/reference/syntax/>,
<https://typst.app/universe/package/cmarker/>.
