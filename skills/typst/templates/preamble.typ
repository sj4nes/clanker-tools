// preamble.typ — every formatting decision for the document lives here.
// manuscript.typ does:  #import "preamble.typ": *   then   #show: apply-base
//
// Nothing in this file is content. To retarget the document to a journal or
// thesis template, replace `apply-base` (or `#show: apply-base` with the
// template's own show rule) and leave every section file untouched.

#let apply-base(body) = {
  set page(
    paper: "us-letter",
    margin: (top: 1in, bottom: 1in, left: 1.1in, right: 1.1in),
    numbering: "1",
  )
  set text(font: ("Libertinus Serif", "New Computer Modern", "Georgia"), size: 11pt, lang: "en")
  set par(justify: true, leading: 0.65em, first-line-indent: 1.25em)
  set heading(numbering: "1.1")
  set math.equation(numbering: "(1)")

  // top-level sections start a new page; `weak: true` avoids a blank first page
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(below: 1em, text(size: 15pt, weight: "bold", it))
  }
  show heading.where(level: 2): set text(size: 12.5pt)
  show raw.where(block: true): set block(fill: luma(245), inset: 8pt, radius: 3pt, width: 100%)
  show link: set text(fill: rgb("#1a5fb4"))
  show figure.caption: set text(size: 9.5pt)

  body
}

// reusable helpers — import the ones a section needs
#let note(body) = text(size: 9pt, fill: luma(90))[#body]
#let keyterm(t) = strong(emph(t))
