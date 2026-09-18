// book.typ — the ONLY file passed to `typst compile` / `typst watch`.
//
//   typst watch   book.typ build/book.pdf
//   typst compile book.typ build/book.pdf
//
// Builds Parts I, II and III. Parts I and II are agent DRAFTS (2026-09-16) pending the
// author's rewrite. Parts IV and V will be GENERATED from the repository rather
// than authored, so they cannot go stale. See README.md.

#import "preamble.typ": apply-base, note, part, colophon

#set document(
  title: "clanker-tools: The Missing Manual",
  author: ("Simon Janes",),
)

#show: apply-base

// --- half-title -------------------------------------------------------------
#v(3.5in)
#align(center)[
  #text(10pt, fill: luma(110))[#smallcaps[clanker-tools]]
  #v(1.2em)
  #text(30pt, weight: "bold")[clanker-tools: The Missing Manual]
  #v(0.5em)
  #text(14pt)[Building skills for AI agents, with an AI agent,\ and knowing whether they work]
  #v(2.5em)
  #note[Simon Janes · #datetime.today().display("[month repr:long] [year]") ·
        draft: Parts I and II of six]
]

#pagebreak()

// --- copyright page ---------------------------------------------------------
#colophon()

#pagebreak()

#block(above: 1.5em, below: 1.1em, text(size: 19pt, weight: "bold")[Contents])
#outline(title: none, indent: auto,
  target: heading.where(level: 1)
    .or(figure.where(kind: "part"))
    .or(figure.where(kind: "front")))

#block(above: 2.2em, below: 1.1em, text(size: 19pt, weight: "bold")[Practices])
#outline(title: none, target: figure.where(kind: "practice"))

#include "preface.typ"

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
  the thing checked, measure the premise, version what turns out wrong,
  direct the agent that does most of the checking, and then all of it at once,
  on a blank page.

  #v(0.8em)
  #note[Draft, 2026-09-16: agent-written from the fat outline and the Part II
  rows of `claim-ledger.md`, to be rewritten in the author's voice. All seven
  chapters are drafted.]
]
#include "parts/02-standard/01-default.typ"
#include "parts/02-standard/02-harness.typ"
#include "parts/02-standard/03-oracle.typ"
#include "parts/02-standard/04-premise.typ"
#include "parts/02-standard/05-version.typ"
#include "parts/02-standard/06-agent.typ"
#include "parts/02-standard/07-author.typ"

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

#part("IV", "The Corpus as Worked Examples")[
  Fifty-three skills, each an entry: what it claims to displace, what its
  displacement table found, what its harness consists of, and how many times it
  turned out to be wrong. The entries are generated from the repository at
  build time, so the catalog cannot drift from the corpus it describes. The
  first chapter is how to read one; the rest are the entries.
]
#include "parts/04-catalogue/00-howtoread.typ"
#include "parts/04-catalogue/01-entries.typ"

#part("V", "What Is Still Wrong")[
  The open backlog, generated from the file the work is actually tracked in.
  It includes the items a closing chapter would omit: a method that has never
  returned a positive result, a run invalidated by its own conditions, and a
  book with no reader interviews.
]
#include "parts/05-open/00-intro.typ"
#include "parts/05-open/01-backlog.typ"

#part("VI", "What the Checks Turned Into")[
  Twenty-four interactive tutorials, cut from the capsules of Part IV rather
  than written beside them: the prerequisite order is the #raw("tsort") order,
  the calculation closing a section is the capsule's own #raw("bc") check, and
  the identity the reader is asked to believe is its Lean core, run in their
  terminal. The catalog is generated from the tutorials themselves.
]
#include "parts/06-tutorials/00-intro.typ"
#include "parts/06-tutorials/01-entries.typ"
