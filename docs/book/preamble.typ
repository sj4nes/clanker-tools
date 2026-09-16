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
      let divider = query(<part-divider>).find(d => d.location().page() == here().page())
      if here().page() > 2 and opener == none and divider == none [
        #set text(size: 9pt, fill: luma(110))
        #smallcaps[The Missing Manual] #h(1fr) #counter(page).display()
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
    // the body's first-line indent otherwise lands on the title's first line
    set par(first-line-indent: 0pt)
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

  show figure.where(kind: "practice"): it => block(
    width: 100%, inset: (x: 13pt, y: 12pt), radius: 3pt,
    fill: rgb("#f4f6f8"), stroke: (left: 3pt + rgb("#40566b")),
    breakable: false,
  )[
    #set align(left)
    #set par(first-line-indent: 0pt, justify: false, leading: 0.62em)
    #text(size: 8.5pt, fill: rgb("#40566b"), weight: "bold")[#smallcaps[
      Practice #context it.counter.display(it.numbering)
    ]]
    #v(0.3em)
    #text(size: 12pt, weight: "bold")[#it.caption.body]
    #v(0.5em)
    #text(size: 10pt)[#it.body]
  ]

  // Part markers: invisible in the body, a heading row in the contents.
  show figure.where(kind: "part"): none
  show outline.entry: it => {
    if it.element.func() == figure and it.element.kind == "part" {
      set par(first-line-indent: 0pt)
      block(above: 1.4em, below: 0.6em, text(size: 10pt, weight: "bold")[
        #smallcaps[Part #(it.element.numbering)(1)] #h(0.5em) #it.element.caption.body
      ])
    } else { it }
  }

  body
}

// Part divider: a page of its own, no heading (a level-1 heading would step
// the chapter counter and land in the outline as a chapter).
#let part(number, title, blurb) = {
  pagebreak(weak: true)
  [#metadata("part") <part-divider>]
  // Invisible, but outlinable: a metadata marker cannot appear in #outline, a
  // figure can. Hidden by the show rule in apply-base; styled there too.
  figure(kind: "part", supplement: [Part], numbering: _ => number,
         outlined: true, caption: title, [])
  v(2.6in)
  align(center)[
    #text(10pt, fill: luma(110))[#smallcaps[Part #number]]
    #v(0.6em)
    #text(24pt, weight: "bold")[#title]
    #v(1.6em)
    #block(width: 70%)[
      #set align(left)
      #set par(justify: true, first-line-indent: 0pt)
      #text(size: 10.5pt, fill: luma(60))[#blurb]
    ]
  ]
  pagebreak()
}

// "Chapter N" for a labelled chapter heading, so inserting a chapter never
// leaves a stale number in the prose. The counter steps inside the heading's
// show rule, so its value at the heading is one short.
#let chref(lbl) = context [Chapter #(chapno.at(locate(lbl)).first() + 1)]

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
//
// A figure of kind "practice", so the practices are numbered and get their own
// list after the contents. The box itself is drawn by the show rule in
// apply-base, which is where the number is available.
#let practice(title, body) = figure(
  kind: "practice", supplement: [Practice], numbering: "1",
  caption: title, body,
)

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
