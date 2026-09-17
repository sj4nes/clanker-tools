#import "../../preamble.typ": keyterm, verdict, practice, chref

// DRAFT 2026-09-16. Ledger rows: C-I-01..03, C-I-11..14; the role-deck introduction leans on C-III-02.

= A skill makes a claim <ch-claim>

== What does a skill assert?

Read almost any SKILL.md and you will find instructions: do this, prefer that,
never the other. Instructions do not look like claims. They cannot be true or
false; they can only be followed or not.

But every skill carries an unstated claim, and it is the one that matters:
#keyterm[that an agent given this document will behave differently, and better,
than it would have without it].

// intro: default-behaviour
That is a claim about a #keyterm[default behaviour] — what the agent does when
you have said nothing — and about displacing it. Written out, it has a shape
// intro: displacement-claim
you can disagree with: #emph[without this, agents do X; with it, they do Y; and
Y is better]. Each clause can be wrong. The agent may not do X. The document
may not move it to Y. Y may be no improvement.

A skill whose claim you can write out is the start of a check. One whose claim
you cannot write out is advice.

== The default is real, and hard to move

Luu's experiment is the clearest public evidence that default behaviour exists
and that naming a technique does not dislodge it.#footnote[Luu, "How well do
agents use test/verification techniques?" See the previous chapter for scope
and caveats.] Agents were told to use TDD, property-based testing, fuzzing,
mutation testing, Lean, TLA+, and a dozen more. In his reading of the
transcripts, they tended to "just write the tests they would normally write,
but inside a framework for a different type of test technique." A proof
assistant produced proofs of irrelevant properties. Property-based testing
produced random inputs that mostly hit rejection paths.

The condition with no testing instructions at all scored #emph[above average].
Luu's explanation: "not telling agents to do things that will make them do
useless work does better than telling them to do things that will make them do
useless work."

Two lessons sit in that result, and the second is easy to miss. The first is
that the default is poor. The second is that #emph[a document can make it
worse]. Doing nothing is not the worst a skill can do. The default is the
result your skill has to beat.

The highest-scoring condition was a skill Luu wrote in a couple of minutes: five
bullets aimed at nudging agents away from their usual failures rather than
teaching them testing. His own reasoning afterwards is close to this chapter's
thesis:

#quote(block: true)[
  The model is already going to have some kind of default behavior
  distribution, so I feel like the more natural thing to do is to give
  statements that will modify that behavior, not write instructions that would
  allow a human or non-knowledgeable agent to do the behavior at all.
]

He is careful about how far it goes, and this book should be too. He calls it a naive
guess from someone who has written one skill. Of the skill itself he writes,
"This got the highest score, but didn't work as intended": its instruction to
re-derive results in a fresh context was almost never followed, so nobody knows
whether that instruction helps.
#emph[Highest score] and #emph[known to work] are different claims, and the
experiment only supports the first.

== Defaults you assume can be false

If the default is the thing a skill displaces, the author has to know what it
is. Usually the author assumes it. This corpus shows how that goes wrong.

// intro: role-deck
Take `role-deck`, which comes up again later in this book. It exists because a
procedure an agent follows on its own honour leaves no evidence that it was
followed: ask for a careful diagnosis and the transcript reads the same whether
the care happened or not. `role-deck` writes the procedure as a
#keyterm[deck] of cards — gather facts, propose rival explanations, design a
test that tells them apart, run it, conclude — and takes the ordering away
from the agent. A runner decides which card comes next, cards that call for
evidence execute a real command and store its output, and the whole run can be
replayed from its seed. #chref(<ch-premises>) goes through a deck card by card.

The skill was built on two claims about what agents do when left alone. Both
were measured against fresh agents who did not know what was being tested.

#verdict[
  An agent left to choose its own sequence will skip the expensive step.
][
  8 of 8 ran it unprompted.
]

#verdict[
  An agent that has a plausible explanation will look for confirmation rather
  than for alternatives.
][
  0 of 8 took the confirmatory path.
]

Both were struck from the skill. Part III tells the whole story, including the
limit that goes with it: the measuring method has never yet confirmed a claim,
so these two results mean #emph[no effect was detected] by an instrument whose
sensitivity is still untested.

Even hedged that far, they make the point this chapter needs. A default is an
empirical claim about what agents do. The author of a skill is the person most
motivated to believe it, and the least likely to have checked.

== Not every skill has a default

#emph["My skill teaches the agent something it doesn't know. There's no default
behaviour to displace."]

That is a real case, not an evasion. Some skills carry facts an agent cannot
// intro: tsort
// intro: bc
work out for itself: that BSD `tsort`, the Unix utility that puts
dependencies in order, exits 0 on a cyclic graph, or that `bc`, the Unix
calculator, truncates where you expected it to round. There is no poor habit to displace
there, only a gap to fill, and such a skill fails by leaving something out, not
by restating what the model already does.

// intro: tool-fact
This corpus treats that as a #keyterm[second kind of skill], judged by a
different standard, and it classifies each section rather than each document.
A behaviour skill may carry one reference table whose payload is fact, and a
tool skill may carry one habit worth displacing. The question is asked of every
section: #emph[is this displacing a default, or supplying a fact?] Part II
takes up both answers.

== The running example's claim

`test-writing` was built after the Luu result and in its spirit. Its first two
behaviours track the first bullet of his five: name the risky area, then state
the likely mistake before writing the assertion. Written out, its claim reads:

#quote(block: true)[
  Without this skill, an agent writing tests takes expected values from what the
  code printed, uses fixtures symmetric enough to hide reversal bugs, and never
  runs a new check against wrong code. With it, expected values come from
  somewhere other than the code, and every check has been seen to fail.
]

That is a sentence someone could disagree with. Its verification half —
#emph[do the prescribed checks catch planted bugs the default checks miss?] —
has a checking script, and it passes. Its behavioural half — #emph[does an agent handed
the skill actually do this, where it would not otherwise?] — has never been
fixtured. The nearest attempt, a neighbouring claim about how verification
work is requested, has been run three times, and all three runs were invalid
for reasons that had nothing to do with the claim. As of this writing, that
half is unmeasured.

Being able to state that is the point of this chapter, not an embarrassment.
Before the claim was written out, there was no way to know which half was
missing.

#practice[Write the sentence your skill is trying to make true.][
  Pick one skill. Complete: #emph[Without this, an agent does \_\_\_. With it,
  the agent does \_\_\_ instead.]

  If the first blank will not fill, you are either describing a fact skill —
  say so, and move to what it must not omit — or you do not yet know what the
  document is for.

  If it fills easily, ask the harder question: #emph[how do I know the agent
  does that without it?] If the answer is that you assumed it, you have found
  the first thing to measure.
]

If a skill is a claim, it can be checked. Part II is how.
