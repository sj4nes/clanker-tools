// preamble.typ — every formatting decision for the document lives here.
// manuscript.typ does:  #import "preamble.typ": *   then   #show: apply-base
//
// Nothing in this file is content. To retarget the document to a journal or
// thesis template, replace `apply-base` (or `#show: apply-base` with the
// template's own show rule) and leave every section file untouched.

#let chapno = counter("chapter")

#let apply-base(body) = {
  set page(
    paper: "us-letter",
    margin: (top: 1.1in, bottom: 1in, inside: 1.25in, outside: 1in),
    numbering: "1",
    header: context {
      // suppressed on the half-title and on any chapter opener, where the
      // title is already on the page
      let opener = query(heading.where(level: 1)).find(c => c.location().page() == here().page())
      if here().page() > 2 and opener == none [
        #set text(size: 9pt, fill: luma(110))
        #smallcaps[Two Refuted Premises and Three Audits] #h(1fr) #counter(page).display()
      ]
    },
    footer: context {
      let opener = query(heading.where(level: 1)).find(c => c.location().page() == here().page())
      if here().page() > 2 and opener != none { align(center, text(size: 9.5pt, counter(page).display())) }
    },
  )
  set text(font: ("Libertinus Serif", "New Computer Modern", "Georgia"), size: 11pt, lang: "en")
  set par(justify: true, leading: 0.65em, first-line-indent: 1.25em)
  set heading(numbering: "1.1")
  set math.equation(numbering: "(1)")

  // Chapters open a page. `weak: true` avoids a blank leaf before the first.
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    chapno.step()
    block(above: 2.2em, below: 1.3em)[
      #context text(size: 9pt, fill: luma(120), weight: "regular", smallcaps[
        Chapter #chapno.display()
      ])
      #v(0.25em)
      #text(size: 19pt, weight: "bold")[#it.body]
    ]
  }
  show heading.where(level: 2): set text(size: 12.5pt)
  set heading(numbering: none)
  show heading.where(level: 2): set text(size: 12.5pt)
  show raw.where(block: true): set block(fill: luma(245), inset: 8pt, radius: 3pt, width: 100%)
  show link: set text(fill: rgb("#1a5fb4"))
  show figure.caption: set text(size: 9.5pt)

  body
}

// reusable helpers — import the ones a section needs
#let note(body) = text(size: 9pt, fill: luma(90))[#body]
#let keyterm(t) = strong(emph(t))

// The headline number of an audit, stated once where the reader meets it.
#let headline(number, what) = block(
  width: 100%, inset: (x: 12pt, y: 11pt), radius: 3pt,
  fill: luma(247), stroke: (left: 2.5pt + luma(120)),
)[
  #set par(first-line-indent: 0pt, justify: false)
  #text(size: 22pt, weight: "bold")[#number]
  #v(0.15em)
  #text(size: 10.5pt)[#what]
]

// Closes a chapter in a prescriptive book: the thing the reader does to their
// own work. Without this, an audit chapter is a war story.
#let practice(title, body) = block(
  width: 100%, inset: (x: 13pt, y: 12pt), radius: 3pt,
  fill: rgb("#f4f6f8"), stroke: (left: 3pt + rgb("#40566b")),
  breakable: false,
)[
  #set par(first-line-indent: 0pt, justify: false, leading: 0.62em)
  #text(size: 8.5pt, fill: rgb("#40566b"), weight: "bold")[#smallcaps[The practice]]
  #v(0.3em)
  #text(size: 12pt, weight: "bold")[#title]
  #v(0.5em)
  #text(size: 10pt)[#body]
]

// A claim under test, and its verdict. Used once per case study.
#let verdict(claim, result) = block(
  width: 100%, inset: 9pt, radius: 3pt,
  fill: luma(246), stroke: (left: 2pt + luma(130)),
)[
  #set par(first-line-indent: 0pt, justify: false)
  #text(size: 10pt)[*Claim.* #claim]
  #v(0.35em)
  #text(size: 10pt)[*Result.* #result]
]
