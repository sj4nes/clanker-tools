// book.typ — the ONLY file passed to `typst compile` / `typst watch`.
//
//   typst watch   book.typ build/book.pdf
//   typst compile book.typ build/book.pdf
//
// Builds Parts I, II (II.1–II.4) and III. Parts I and II are agent DRAFTS (2026-09-16) pending the
// author's rewrite. Parts IV and V will be GENERATED from the repository rather
// than authored, so they cannot go stale. See README.md.

#import "preamble.typ": apply-base, note, part

#set document(
  title: "The Missing Manual",
  author: ("Simon Janes",),
)

#show: apply-base

// --- half-title -------------------------------------------------------------
#v(3.5in)
#align(center)[
  #text(10pt, fill: luma(110))[#smallcaps[clanker-tools]]
  #v(1.2em)
  #text(30pt, weight: "bold")[The Missing Manual]
  #v(0.5em)
  #text(14pt)[Building skills for AI agents, with an AI agent,\ and knowing whether they work]
  #v(2.5em)
  #note[Simon Janes · #datetime.today().display("[month repr:long] [year]") ·
        draft: Parts I, II (in part) and III of five]
]

#pagebreak()

#block(above: 1.5em, below: 1.1em, text(size: 19pt, weight: "bold")[Contents])
#outline(title: none, indent: auto,
  target: heading.where(level: 1).or(figure.where(kind: "part")))

#block(above: 2.2em, below: 1.1em, text(size: 19pt, weight: "bold")[Practices])
#outline(title: none, target: figure.where(kind: "practice"))

#part("I", "The Pile")[
  This part asks one question before the rest of the book answers it: what are
  you actually accumulating when you write another skill? The first chapter is
  about the pile, and why a growing set of documents you cannot evaluate is a
  cost rather than a neutral one. The second is about the single idea that makes
  the pile evaluable: a skill makes a claim, and a claim can be wrong.

  #v(0.8em)
  #note[Draft, 2026-09-16: agent-written from the fat outline and the Part I
  rows of `claim-ledger.md`, to be rewritten in the author's voice.]
]
#include "parts/01-pile/01-asset.typ"
#include "parts/01-pile/02-claim.typ"

#part("II", "The Standard")[
  Part I argued that a skill is a claim. This part is how to check one, one
  move per chapter, each depending on the one before: name the default the
  skill displaces, build a check that can fail, choose an oracle independent of
  the thing checked, measure the premise, and version what turns out wrong.

  #v(0.8em)
  #note[Draft, 2026-09-16: agent-written from the fat outline and the Part II
  rows of `claim-ledger.md`, to be rewritten in the author's voice. Chapters
  II.1 to II.4 are drafted.]
]
#include "parts/02-standard/01-default.typ"
#include "parts/02-standard/02-harness.typ"
#include "parts/02-standard/03-oracle.typ"
#include "parts/02-standard/04-premise.typ"

#part("III", "What the Standard Found")[
  Four audits of a corpus of verified agent skills, run over three days in
  September 2026. Each asked a different verification technology whether its
  checks had any way of failing. Mostly they did not.
]
#include "parts/03-findings/00-intro.typ"
#include "parts/03-findings/01-bc.typ"
#include "parts/03-findings/02-lean.typ"
#include "parts/03-findings/03-graph.typ"
#include "parts/03-findings/04-premises.typ"
#include "parts/03-findings/05-shape.typ"
