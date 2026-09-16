#import "../../preamble.typ": keyterm, headline, verdict, practice, chref

= Two premises, measured <ch-premises>

#headline[8 of 8, twice][
  Both behavioural claims that justified a newly built skill were fixtured
  against naive agents. Both were refuted, in the worst pre-registered band.
]

== What role-deck does

// DRAFT 2026-09-16 (agent-written, at the author's request). Ledger: C-III-02..04.
Ask an agent to diagnose a bug and it will produce a diagnosis. Ask it to
diagnose the bug #emph[properly] — gather the facts, consider more than one
cause, test the one that matters — and it will produce a diagnosis and say it
did those things. The transcript reads the same whether it did or not. A
procedure an agent follows on its own honour leaves no evidence that it was
followed.

`role-deck`, first met in #chref(<ch-claim>), turns the procedure into an
object that does leave evidence. The procedure is written as a deck of cards. Each card is one role the
agent must play, and each role is a thinking mode borrowed from Edward de
Bono's #emph[Six Thinking Hats]:#footnote[Edward de Bono, #emph[Six Thinking
Hats] (Little, Brown, 1985). The corpus adds a seventh role, EXECUTE, for the
step that spends real resources.] white for facts only, red for a gut feeling,
green for alternatives, yellow for what an idea gets right, black for what
could be wrong with it, and blue for running the process. Each card declares
what it needs before it can be played and what it must produce.

The deck for diagnosing a problem has eight cards:

#table(
  columns: (auto, auto, 1fr, auto),
  align: (left, left, left, left),
  table.header([*card*], [*hat*], [*what the agent must do*], [*needs*]),
  [open], [blue], [name the question, its scope, and what would end it], [—],
  [hunch], [red], [state a gut call in one line, with no justification], [question],
  [gather], [white], [record observations only, from a command that actually runs], [question, hunch],
  [hypothesize], [green], [propose at least two competing explanations], [evidence],
  [support], [yellow], [say what each explanation would account for], [hypotheses],
  [falsify], [black], [design a test whose result #emph[differs] between them], [hypotheses, support],
  [run], [execute], [run that test and record what happened], [a test],
  [close], [blue], [conclude, state what is still uncertain, and check the hunch], [result, hunch],
)

The agent does not choose the order. At each step a runner works out which
cards are playable — whose needs are met, and which still leave enough budget
to finish — and rolls a seeded die to pick one. The agent fills in that card's
artifact and plays it. Two details make the record trustworthy. A card that
declares an instrument, like `gather` or `run`, cannot be played without a
command, and the runner executes the command and stores its output, so a test
the agent never ran cannot be reported. And every draw is a function of the
seed and the step, so the whole run can be replayed from nothing and any edited
entry fails the replay.

Two more decks follow the same pattern: `decide`, for choosing between options
(ending in commit, defer, or drop), and `invent`, for when something new is
wanted and nobody knows what yet.

== A real run

The first real use was a diagnosis of drift in an authoring tool the author is
building: had the product brief's picture of what was built fallen out of step
with the code? The run took ten plays and the whole budget of eleven. The hunch
came second, before any evidence. Two `gather` plays read the brief and then
the code. The agent proposed four explanations, tested one with a four-part
measurement, found its own test had probed the wrong file, and spent its one
reroll to record a corrected test rather than draw a fifth explanation.

The conclusion was wrong. The run recommended updating a tracker the project
had already abandoned: #keyterm[every fact gathered was true, and the
conclusion was not]. The ledger did not prevent that — nothing in the skill
checks whether a command was aimed at something still in use. What it did was
make the mistake diagnosable in seconds, because it recorded exactly which
files were read.

== Checking a deck before anyone runs it

Because a deck is a small state machine, every reachable state can be
enumerated. The diagnose deck has 36 reachable states and eight distinct
complete runs, and its checker applies seventeen gates to all of them before
the deck is used: every card is playable somewhere, no state is a dead end, an
ending is always reachable, every produced artifact is consumed.

The gates found real defects in every deck written, all of them invisible on
reading. Two cards were decorative — they produced artifacts nothing
consumed. An ending was reachable before any evidence had been gathered. And a
simulator showed the gut-call card landing #emph[after] the evidence in half of
all runs, which defeats its purpose: a hunch recorded after the facts is no
longer a hunch.

== The sentence nobody checked

The three preceding audits found checks that could not fail. This one found
something adjacent: #keyterm[a justification that had never been checked at
all].

The gates check the deck. But the reason the skill existed was a sentence at the top of its own
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

The fixture was a real bug from this repository's own history — the marker grep
that could never match, from #chref(<ch-bc>), rebuilt small. Reading it yields a confident wrong
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
