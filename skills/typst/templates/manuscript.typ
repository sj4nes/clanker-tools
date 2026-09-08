// manuscript.typ — the ONLY file passed to `typst compile` / `typst watch`.
//
//   typst watch  manuscript.typ build/manuscript.pdf     # while drafting
//   typst compile manuscript.typ build/manuscript.pdf    # the deliverable
//
// Body content is in sections/*.typ, spliced with #include in document order.
// Formatting is in preamble.typ.

#import "preamble.typ": apply-base, note, keyterm

#set document(
  title: "A Minimal Typst Manuscript",
  author: ("A. Researcher",),
)

#show: apply-base

// --- title block -----------------------------------------------------------
#align(center)[
  #text(17pt, weight: "bold")[A Minimal Typst Manuscript] \
  #v(0.4em)
  A. Researcher \
  #note[Institute of Example Studies]
  #v(0.3em)
  #datetime.today().display("[month repr:long] [year]")
]

#v(2em)

#align(center)[
  #block(width: 85%)[
    #set par(justify: true, first-line-indent: 0pt)
    #text(size: 10pt)[
      *Abstract.* This template compiles as-is. It shows a split body, a
      centralized preamble, a labelled figure with a cross-reference, a table,
      native Typst math, and a bibliography citation.
    ]
  ]
]

#v(1em)

// --- body ----------------------------------------------------------------
#include "sections/introduction.typ"
#include "sections/methods.typ"

// --- back matter -------------------------------------------------------------
#pagebreak()
= References
#bibliography("references.bib", style: "ieee", title: none)
