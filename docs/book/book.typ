// book.typ — the ONLY file passed to `typst compile` / `typst watch`.
//
//   typst watch   book.typ build/book.pdf
//   typst compile book.typ build/book.pdf
//
// Currently builds Part III alone. Parts I, II, IV and V are planned; IV and V
// will be GENERATED from the repository rather than authored, so they cannot
// go stale. See README.md.

#import "preamble.typ": apply-base, note

#set document(
  title: "The Missing Manual — Part III: What the Standard Found",
  author: ("Simon Janes",),
)

#show: apply-base

// --- half-title -------------------------------------------------------------
#v(3.5in)
#align(center)[
  #text(10pt, fill: luma(110))[#smallcaps[clanker-tools · the missing manual]]
  #v(1.2em)
  #text(30pt, weight: "bold")[Part III]
  #v(0.5em)
  #text(19pt)[What the Standard Found]
  #v(2.2em)
  #block(width: 74%)[
    #set align(left)
    #set par(justify: true, first-line-indent: 0pt)
    #text(size: 10.5pt, fill: luma(60))[
      Four audits of a corpus of verified agent skills, run over three days in
      September 2026. Each asked a different verification technology whether its
      checks had any way of failing. Mostly they did not.
    ]
  ]
  #v(2.5em)
  #note[Simon Janes · #datetime.today().display("[month repr:long] [year]") ·
        draft, Part III of five]
]

#pagebreak()

#block(above: 1.5em, below: 1.1em, text(size: 19pt, weight: "bold")[Contents])
#outline(title: none, depth: 1, indent: auto)

#include "parts/03-findings/00-intro.typ"
#include "parts/03-findings/01-bc.typ"
#include "parts/03-findings/02-lean.typ"
#include "parts/03-findings/03-graph.typ"
#include "parts/03-findings/04-premises.typ"
#include "parts/03-findings/05-shape.typ"
