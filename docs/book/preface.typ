// AUTHORED front matter. Deliberately outside parts/, so the intro-order gate
// does not check it: a preface is read before any term has been introduced, and
// has to make sense cold. Keep it free of the book's vocabulary.

#import "preamble.typ": frontmatter, note, chref, sidebar

#frontmatter("Preface: this book is inside its own subject")[

This is a book about how to tell whether a document written for an AI agent
does anything. It was written by a person and an agent working together, which
is also what it is about, and the loop closes tighter than that.

It is worth being explicit about the layers, because they are load-bearing and
because one of them is a problem.

An agent and I wrote fifty-odd instruction documents. To find out whether any of
them worked, we built checks—small harnesses that would fail if a document's
claim were false—and then, because a check nobody has seen fail is not a
check, we broke each one on purpose to watch it fail. That produced a standard,
which is Part II. Applying the standard to the documents produced four audits,
which is Part III, and most of what they found was that the checks could not
have failed.

Then this book was written to that same standard, by the same pair. Three of its
six parts are not written at all: they are generated from the repository every
time the book is built, and a gate refuses the build if what they say has
drifted from what is on disk. That gate has its own checks. Those checks are
broken on purpose too, one at a time, by a script that also runs one case it
expects to *pass*—and twice, that unbroken case was the only thing that
noticed the whole apparatus was measuring nothing.

So: an agent helped write the skills, helped write the checks on the skills,
helped audit the checks, helped write the book about the audits, and helped
build the machinery that checks the book. Where that produced something worth
reading, it is reported here. Where it produced a defect, that is reported too,
and there is a running log of the second kind.

That includes these sentences. Most of the prose in this book was drafted by the
agent, from an outline, a ledger of claims and a set of decisions that are mine,
and then revised by me. I am not going to pretend otherwise in a book whose
argument is that you should say what a document actually is. The judgements are
mine and I stand behind them; the majority of the words arrived by proxy, which
is the same working relationship the rest of the book describes—and the
reason it can describe it in any detail.

== The problem with that

#chref(<ch-oracle>) of this book tells you not to check a thing with an oracle
that shares its assumptions. Two implementations that share a helper are one implementation.
A test whose expected value came out of the code proves the code agrees with
itself.

By that standard, this book's evidence is not independent of this book. The
corpus is mine. The standard is mine. The audits were run by me and the agent,
on our own work, using instruments we wrote. Nobody else has adopted the method,
and the one experiment designed to test the book's central premise on strangers
has not produced a valid run.

That does not make the findings false. A harness that exits zero on a false
claim is a fact about that harness, and a Lean proof that proves nothing is a
fact about that proof; those hold regardless of who noticed. But it does mean
that everything here is one practitioner's corpus, held to one practitioner's
standard, and you should read the general claims— about what agents do by
default, about what other people's documents are like— as hypotheses with an n
of one, not as findings.

== How to read it, given that

The parts differ in how much they can be checked, and the difference is worth
using.

Parts IV, V and VI are generated from the repository. Every count in them was
read off disk at build time, and if the repository changes and the book does
not, the build fails. You can disbelieve the argument and still trust the
numbers.

Parts I, II and III are argument, and their evidence is the corpus. Trust them
the way you would trust a careful practitioner describing their own practice.

The most credible things in the book are the places where it went against me. Two premises this method was built on were measured and struck. A skill
written to demonstrate the standard turned out, while its own chapter was being
drafted, to have been overstating what it had measured. An audit of this book's
plan produced five findings and then withdrew two of them on closer reading.
None of those results were wanted, which is the only reason they are worth
much.

== What would settle it

A second person, with their own corpus, running the method and reporting what it
found—including a run where it finds nothing. Until then this is a detailed,
honestly-reported single case, and the method's own rules say a single case is
where you start, not where you stop.

#v(0.6em)
#note[Parts I and II are still at an earlier stage of that process than the
rest: drafted from the outline and the claim ledger and not yet taken through a
revision pass. The division of labour does not change when they are—only the
voice.]

]
