// AUTHORED, and states no count: the chapters after it are generated from
// BACKLOG.md, and a number written here would be the first thing to go stale.

#import "../../preamble.typ": note, practice

= What this part is

The chapters after this one are the open items of `BACKLOG.md`, generated at
build time. They are not a summary of the backlog, a selection from it, or a
version of it written for a reader. They are the file, minus the work already
finished.

This is the only arrangement that survives its own incentives. A closing chapter
about unsolved problems is the chapter an author most wants to quietly let
close, and the only defence against that is to not be the one writing it. The
backlog is maintained because the work needs tracking; the book prints whatever
it currently says.

== What is in here that a book would normally leave out

Three things in particular, which a chapter written for the reader would have
softened.

The first is that the central method of this book's fourth chapter — measuring a
claimed default behaviour before building on it — has never returned a positive
result. Every case study run under it refuted the claim it tested. That is
either a method that works and a set of claims that were wrong, or a method that
can only refute, and nothing in the corpus currently distinguishes those. It is
in the backlog as an item owed a positive control, and it is in this part
because the item is open.

The second is that a run of that method was invalidated by the conditions it was
run under rather than by its result, and that its subjects could read the
repository they were being tested about — which is the one thing a subject must
not be able to do. The re-run is scheduled. Until it lands, what the method has
established about this corpus is less than what the earlier chapters would like
it to have established.

The third is that this book has no reader interviews. Its account of what a
person writing their fourth skill needs was assembled from one author's corpus
and one author's mistakes, and every claim it makes about the reader's situation
is that author's model of it. That is a gap of the same kind as the harness gaps
in Part IV: something a fixture could falsify, that nothing has yet.

== Where the items come from

// intro: gap-reporting
Most of them are not plans. When a displacement table finds a gap — a claim a
fixture could falsify and does not — the standard does not ask you to fix it
there and then. It asks you to write it down as a concrete harness section in
the one file the work is tracked in, named precisely enough that someone can
build it later: which claim, which fixture, what the fixture would have to
show. That convention is the reason this part can be generated at all, and it
is why a gap found on a Tuesday is still legible in November.

The effect is that the audits of Part III mostly did not produce fixes. They
produced entries. A skill whose harness was found to have no way of failing
gets a row here for each way it could have one, and the row survives until the
harness does.

== How to use it

Not as a roadmap. The items are not ordered by importance, they close without
ceremony, and many of them were opened by the audits of Part III rather
than by anyone planning the work — which is the pattern to take from this part
rather than any particular entry. A standard that is working generates backlog.

#practice[Keep the open list where the work is, not where the reader is.][
  If you write up your own method, generate the open problems from whatever file
  you actually track them in, and let the write-up print what that file says on
  the day it is built. A hand-maintained list of open problems in a document is
  optimised by the same person it is supposed to hold to account, and it shortens
  over time whether or not the problems do.
]
