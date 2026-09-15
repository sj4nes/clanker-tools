#import "../../preamble.typ": keyterm, headline, verdict, practice

= Two premises, measured

#headline[8 of 8, twice][
  Both behavioural claims that justified a newly built skill were fixtured
  against naive agents. Both were refuted, in the worst pre-registered band.
]

== A different kind of unfalsifiable

The three preceding audits found checks that could not fail. This one found
something adjacent: #keyterm[a justification that had never been checked at
all].

`role-deck` makes a multi-phase process into an executable rulebook whose next
step is drawn externally. Seventeen gates verify a deck exhaustively before
anyone runs it, and they found real defects in every deck written — roles whose
output nothing consumed, an exit reachable having gathered no evidence, a
gut-call card landing *after* the evidence in half of all runs.

But the reason the skill existed was a sentence at the top of its own
documentation, asserting what an agent does when left alone. That sentence had
no evidence behind it whatsoever.

== The first claim

#verdict[
  An agent left to choose its own sequence will skip the expensive step.
][
  Refuted. 8 of 8 fresh agents ran it unprompted.
]

The claim splits in two, and only half needed subjects. *Does a deck make
skipping impossible?* was already settled by an exhaustive gate. *Would anyone
actually skip?* was the open question, and it reduced the experiment to one arm.

The fixture was a real bug from this repository's own history — the dead marker
grep from the first chapter, rebuilt small. Reading it yields a confident wrong
answer; running it prints a string that occurs #keyterm[zero times in the
source], making execution unforgeable and self-report unnecessary.

Eight fresh agents, no deck, no suggestion to run anything. All eight ran it.
Several went further than asked, applying the fix and verifying both directions.

== The second claim

The reflex after a refutation is to substitute a similar-sounding claim that was
not tested. That reflex produced this:

#verdict[
  Having formed a plausible explanation, an agent asks #emph[how do I confirm
  this?] rather than #emph[what else would produce this symptom?]
][
  Refuted. 8 of 8 found a second cause invisible in the output.
]

This one is measurable where "do they enumerate alternatives" is not, because a
confirmatory fix #keyterm[passes its own confirmation] while the defect
survives — and whether it survives is decided by execution, not by reading.

The fixture was a build gate with two real causes: an anchored pattern that
completely explains the visible symptom, and a stdout-only capture while the
suite reports some failures on stderr. Fix the first and the presented bug is
caught. A stderr-reported failure still slips through.

Eight subjects applied their fix; the scorer executed it against a case absent
from the fixture they were given. All eight caught both channels. All eight
built the stderr-only test case themselves. All eight also tested the all-pass
case unprompted — several noting that a gate wedged at *fail* is as broken as
one wedged at *ok*. And #keyterm[four of eight closed a third defect that had
never been planted]: the suite always exits zero, so a suite dying partway
through reads as green.

== What was done about it

Both claims were struck rather than reworded. The skill's documentation now
states in a table that it does not make an agent more thorough, and says what
survives instead: an auditable, replayable record, and a deck-checking apparatus
that is independent of any claim about agents.

The measurements cost sixteen agents and roughly four minutes of wall time. They
should have been taken first.

#practice[Measure the sentence your skill rests on.][
  Find the sentence that justifies your document — the one asserting what goes
  wrong without it. #emph[Agents skip verification. Reviewers rubber-stamp.
  People do not read the spec.] Write it down as a claim.

  Then split it. Part of it is usually structural and already settled by
  inspection; only the behavioural half needs subjects, and dropping the other
  half often halves the work. Recruit subjects who cannot know the hypothesis —
  which means not you. Make the measurement an artefact of doing the work or an
  execution of the subject's own output, never a self-report. Commit the scorer
  and the outcome bands #emph[before] any result exists, in their own commit.

  Sixteen fresh agents and four minutes of wall time refuted both claims this
  skill was built on. That is cheaper than the day spent building on them.
]
