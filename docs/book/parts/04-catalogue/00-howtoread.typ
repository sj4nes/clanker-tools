// AUTHORED. The chapters that follow this one are generated; this one is not,
// and deliberately states no number that the generator would have to keep true.

#import "../../preamble.typ": note, practice

= How to read an entry

Everything after this chapter is generated from the repository. Nothing in it
was written for the book, and nothing in it can be revised to make the corpus
look better than it is: the entries are read out of `SKILL.md` frontmatter,
`CHANGELOG.md`, and each skill's `verification/README.md` every time the book is
built, and a gate refuses the build if what is printed here has drifted from
what is on disk.

That is not a convenience. A catalog is the part of a book most likely to rot,
because it is the part whose facts live somewhere else and change without
telling the author. Part III is four audits of exactly that failure—checks
that had no way of failing, in a corpus that looked verified. A hand-written
catalog in the same book would be the same defect, committed on purpose.

== The four fields

Each entry names the skill, the version it is at, and its archetype, then gives
three facts.

*Displaces.* The counts from the skill's displacement table: how many sections
name a default behavior that the harness shows failing (#emph[covered]), how
many name a step no fixture can falsify because the fixture supplies what the
step is meant to find (#emph[judgment]), and how many could be falsified by a
fixture and are not (#emph[gaps]). The rule is in the standard; the counts are
the deliverable.

Where a skill has no table, the entry says so rather than printing zeros. Where
a skill has a table but states its counts only in prose, the entry says that
too, because the standard asks for the counts and prose is not the counts. Both
absences are read from the repository, so both disappear from the book the day
they are fixed in it.

*Harness.* Whether the skill has a verification directory, a runner, and a
README describing what the run proves. This is the weakest of the three fields
and should be read as the weakest: that a harness exists says nothing about
whether its checks can fail, which is the question Part III found the corpus
answering badly.

*Wrong.* The version history, read for one thing only—how many times this
skill turned out to be wrong. In this corpus a MAJOR bump has a defined
meaning: the skill said something false, and work done under the old text has
to be redone. Those entries are printed in full, with the date and what was
wrong. Everything else collapses to a count.

== Why a high count is the better sign

The temptation with a catalog is to read it as a scoreboard, and the entries
do not support that reading. A skill with four gaps has a harness good enough
to have located four places where it is trusting itself; a skill with none has
usually not been asked. A skill with two MAJOR bumps has been wrong twice in
public and says where; a skill that has never been revised has either survived
contact or not yet made it.

So read the gaps and the MAJOR bumps as evidence of attention, not of quality,
and read a long unbroken run at 1.0.0 as the thing most worth being suspicious
of. The entries are ordered by archetype rather than by any score, because the
archetype decides which standard applies: a tool-fact skill has no wrong default
to displace and is not failing the displacement rule by having no table, while a
behavior skill with no table has simply not been held to the standard this book
spends Part II describing.

== The running example, as an entry

`test-writing` has been this book's worked example since Part I: the skill whose
six behaviors displace six known ways a test fails to fail. Its entry is in the
next chapter, and reading it the way this one describes is a fair test of
whether the format carries anything.

It does, and not flatteringly. Its *displaces* field does not report counts. It
reports that the skill has a displacement table and states the counts in prose
instead—which is what the standard asks for, done in the form the standard
says not to use. That is the skill the standard's own documentation names as the
worked example of the rule.

Nobody noticed that by reading the skill, which has been read many times. It
surfaced because a generator tried to read the counts off the page and found
none, and it is in the backlog now. The entry format's contribution was to make
one skill's omission visible next to fifty-odd others that either have the
counts or have no table at all.

#practice[Find the nearest entry before writing the skill.][
  Before writing a new skill, find the entry closest to it in archetype and in
  shape, and open that skill's `verification/` directory. The question is not
  whether the neighbor is good. It is what its displacement table found, what
  its harness can demonstrate failing, and—where it has MAJOR bumps—what it
  turned out to be wrong about, since a skill in the same shape tends to be
  wrong in the same way.
]
