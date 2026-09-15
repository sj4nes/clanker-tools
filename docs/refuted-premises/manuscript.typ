// manuscript.typ — the ONLY file passed to `typst compile` / `typst watch`.
//
//   typst watch   manuscript.typ build/note.pdf     # while drafting
//   typst compile manuscript.typ build/note.pdf     # the deliverable

#import "preamble.typ": apply-base, note, keyterm, verdict

#set document(
  title: "Two Refuted Premises",
  author: ("Simon Janes",),
)

#show: apply-base

#align(center)[
  #text(17pt, weight: "bold")[Two Refuted Premises] \
  #v(0.3em)
  #text(12pt)[Measuring the default behaviours a methodology was built to correct]
  #v(0.7em)
  Simon Janes \
  #note[Interim research note · #datetime.today().display("[day] [month repr:long] [year]")]
]

#v(1.4em)

#align(center)[
  #block(width: 88%)[
    #set align(left)          // else the last line inherits the centre
    #set par(justify: true, first-line-indent: 0pt)
    #text(size: 10pt)[
      *Abstract.* Methodology is routinely justified by an unmeasured assertion
      about what goes wrong without it. We built an agent-process skill on two
      such assertions — that an unconstrained agent skips the expensive step,
      and that it confirms its first explanation rather than discriminating
      between rivals — then fixtured both against naive subjects. Both were
      refuted, 8 of 8 each, in the worst pre-registered band. Half of the second
      cohort exceeded the fixture, closing a defect that had not been planted.
      We report the method that produced these results, the two case studies,
      and the discipline that made the negatives usable: striking a refuted
      claim rather than rewording it into a similar untested one. We also report
      the limitation that should temper every conclusion here — the method has
      so far produced only refutations, and no control demonstrates it can
      confirm a claim that is true.
    ]
  ]
]

#v(1.2em)

#include "sections/01-problem.typ"
#include "sections/02-method.typ"
#include "sections/03-case-one.typ"
#include "sections/04-case-two.typ"
#include "sections/05-discussion.typ"
#include "sections/06-limitations.typ"

#v(1.5em)
#line(length: 100%, stroke: 0.5pt + luma(180))
#v(0.5em)
#text(size: 9pt)[
  Artifacts, fixtures, scorers and full result records are in the
  `clanker-tools` repository @clankertools2026 under
  `skills/role-deck/verification/` and `skills/claim-fixture/`.
  Written with the assistance of Claude Opus 5, which also served as the
  fixture designer and is therefore a subject of #ref(<sec:limitations>).
]

#v(1em)
= References
#bibliography("references.bib", style: "ieee", title: none)
