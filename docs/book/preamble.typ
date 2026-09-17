// preamble.typ — every formatting decision for the document lives here.
// manuscript.typ does:  #import "preamble.typ": *   then   #show: apply-base
//
// Nothing in this file is content. To retarget the document to a journal or
// thesis template, replace `apply-base` (or `#show: apply-base` with the
// template's own show rule) and leave every section file untouched.

#let chapno = counter("chapter")

// The sidebar face. Sidebars are the ONLY sans in the book: practices already
// own the grey panel, so a second boxed device would compete with them rather
// than read as a different kind of thing. Switching typeface instead separates
// them on a channel nothing else uses.
//
// Libertinus ships no sans companion, so this is a fallback stack rather than a
// single face. Lato leads: humanist like Libertinus, open-licensed so the book
// sets on someone else's machine, and — the deciding property — it has a REAL
// ITALIC.
//
// Inter was first here for one render. The copy installed on this machine is the
// upright-only variable font, so `#emph` inside a sidebar silently set roman:
// the emphasis vanished and nothing warned, which is the same defect class as
// `**bold**` rendering as two empty bolds (see README). check-book.sh now gates
// the leading family for an italic.
#let sans = ("Lato", "Helvetica Neue", "Avenir Next", "Arial")

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
  set math.equation(numbering: "(1)")

  // Chapters are numbered, sections are not. The chapter number is not drawn
  // (the opener below prints `it.body` only); it exists so the PDF bookmarks,
  // which Typst builds from numbering + title, read "7 Version what ...".
  set heading(numbering: none)
  show heading.where(level: 1): set heading(numbering: "1")

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
      #text(size: 19pt, weight: "bold", hyphenate: false)[#it.body]
    ]
  }
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

  // Sidebars: an aside from the book's own construction. Deliberately unlike
  // `practice` — no fill, hairline rules top and bottom — because a practice is
  // something the reader DOES and a sidebar is something that happened.
  show figure.where(kind: "sidebar"): it => block(
    width: 100%, inset: (x: 0pt, y: 10pt), breakable: true,
    stroke: (top: 0.6pt + luma(160), bottom: 0.6pt + luma(160)),
  )[
    #set align(left)
    // Sans runs optically larger than the serif at the same point size, so the
    // body drops from 9.8pt to 9.3pt to sit level with the text around it.
    // Off-black rather than black: the sans already runs darker on the page than
    // the serif at the same size, and full black made the aside compete with the
    // body it is an aside to.
    #set text(font: sans, size: 9.4pt, fill: luma(62))
    #set par(first-line-indent: 0pt, justify: true, leading: 0.68em)
    // Tracked uppercase rather than smallcaps: the stack's faces have no true
    // small-capital variants, and synthesised ones look like shrunk capitals.
    #text(size: 7.4pt, fill: luma(95), weight: "semibold", tracking: 0.09em)[
      #upper[Sidebar #context it.counter.display(it.numbering) · from building this book]
    ]
    #v(0.35em)
    #text(size: 10.5pt, weight: "bold")[#it.caption.body]
    #v(0.45em)
    #it.body
  ]

  // Part markers: invisible in the body, a heading row in the contents.
  show figure.where(kind: "part"): none
  show outline.entry: it => {
    if it.element.func() == figure and it.element.kind == "part" {
      set par(first-line-indent: 0pt)
      block(above: 1.4em, below: 0.6em, text(size: 10pt, weight: "bold")[
        #smallcaps[Part #(it.element.numbering)(1)] #h(0.5em) #it.element.caption.body
      ])
    } else if it.element.func() == heading and it.level == 1 {
      // chapter number in the contents; the counter steps inside the heading's
      // show rule, so its value at the heading is one short (as in chref)
      let n = chapno.at(it.element.location()).first() + 1
      // plain text colour, like the default entries (not the link colour)
      link(it.element.location(), text(fill: black, it.indented([#n.], it.inner())))
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

// A Part IV catalogue entry. The generator (tools/gen-catalogue.py) emits
// calls to this and nothing else, so an entry's LOOK stays a decision of this
// file while its CONTENT stays a fact of the repository.
//
// `facts` is an array of (label, body) pairs; a label with an empty body is
// dropped by the generator rather than set as a blank row.
#let skillentry(name, version, archetype, claim, facts) = block(
  width: 100%, breakable: false, above: 1.5em, below: 0.4em,
)[
  #set par(first-line-indent: 0pt, justify: false)
  #text(size: 12pt, weight: "bold")[#raw(name)]
  #h(0.45em)
  #text(size: 9pt, fill: luma(110))[#version #sym.dot.c #archetype]
  #v(0.35em)
  #text(size: 10pt)[#claim]
  #v(0.5em)
  #block(inset: (left: 10pt), stroke: (left: 1.5pt + luma(210)))[
    #set par(first-line-indent: 0pt, justify: false, leading: 0.58em)
    #grid(columns: (4.6em, 1fr), row-gutter: 0.55em, column-gutter: 0.6em,
      ..facts.map(((label, body)) => (
        text(size: 8.5pt, fill: rgb("#40566b"), weight: "bold")[
          #smallcaps[#label]
        ],
        text(size: 9.5pt)[#body],
      )).flatten())
  ]
]

// A Part V backlog item. Generated by tools/gen-open.py, which passes the
// item's subject, its trailing date if it has one, and a body already broken
// into paragraphs and enumerated points.
//
// Set as a titled block rather than a list item: the items run to hundreds of
// words and several carry their own "(1) ... (5)" enumerations, which as a
// single justified paragraph read as a wall. The subject line is the only
// thing a reader skimming for their own skill needs to hit.
#let backlogitem(subject, date, body) = block(
  width: 100%, above: 1.35em, below: 0.9em, breakable: true,
)[
  #set par(first-line-indent: 0pt, justify: true, leading: 0.62em)
  #if subject != none or date != none {
    block(below: 0.45em)[
      #if subject != none [#text(size: 10.5pt, weight: "bold")[#subject]]
      #if date != none [
        #if subject != none [#h(0.4em)]
        #text(size: 8.5pt, fill: luma(130))[#date]
      ]
    ]
  }
  #block(inset: (left: 9pt), stroke: (left: 1.5pt + luma(215)))[
    #set par(first-line-indent: 0pt, justify: true, leading: 0.62em)
    #set text(size: 9.8pt)
    #body
  ]
]

// The enumerated points inside a backlog item: "(1) ... (2) ...", set as a
// real list so the reader can count them.
#let points(..items) = enum(
  spacing: 0.65em, tight: false, indent: 0.2em, body-indent: 0.55em,
  ..items,
)

// A Part VI tutorial entry. Same shape as `skillentry`, but the meta line
// carries the capsule and the method that cut the tutorial from it rather than
// a version and an archetype.
#let tutorialentry(title, meta, facts) = block(
  width: 100%, breakable: false, above: 1.4em, below: 0.4em,
)[
  #set par(first-line-indent: 0pt, justify: false)
  #text(size: 11.5pt, weight: "bold")[#title]
  #v(0.2em)
  #text(size: 8.5pt, fill: luma(110))[#meta]
  #v(0.5em)
  #block(inset: (left: 10pt), stroke: (left: 1.5pt + luma(210)))[
    #set par(first-line-indent: 0pt, justify: true, leading: 0.6em)
    #grid(columns: (4.4em, 1fr), row-gutter: 0.55em, column-gutter: 0.6em,
      ..facts.map(((label, body)) => (
        text(size: 8.5pt, fill: rgb("#40566b"), weight: "bold")[
          #smallcaps[#label]
        ],
        text(size: 9.5pt)[#body],
      )).flatten())
  ]
]

// An aside from the book's own construction: a moment where the standard this
// book describes, applied to the book's own toolchain, caught something reading
// had not. The running record — including the candidates not yet cut into a
// chapter — is docs/book/sidebars.md.
//
// A sidebar is not a practice. A practice is what the reader should do; a
// sidebar is what happened when the author did it.
#let sidebar(title, body) = figure(
  kind: "sidebar", supplement: [Sidebar], numbering: "1",
  caption: title, body,
)
