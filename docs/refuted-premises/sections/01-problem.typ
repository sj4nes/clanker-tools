#import "../preamble.typ": verdict

= The unmeasured premise

Most methodology rests on a claim about what goes wrong without it. #emph[Agents
skip verification. Reviewers rubber-stamp. Developers do not read the spec.]
The claim justifies the discipline; the discipline gets built; the claim is
never checked.

It is not checked for two reasons, and the second is the interesting one. It
sounds obviously true — which is exactly the property a claim has when nobody
has looked. And checking it risks discovering that the discipline was
unnecessary, after the discipline has been built.

That risk is the reason to check. A methodology with a false premise is not
merely unhelpful. It spends attention and credibility on a problem that is not
there, and in doing so it crowds out the problem that is.

This note reports two such checks, run against a skill the author had spent a
day building and was invested in. Both came back negative.

== What was built, and on what

The subject is `role-deck`, a tool that makes a multi-phase process — a
diagnosis, a decision — into an executable rulebook. Roles are cards; each card
declares the typed artifact it produces and the artifacts it requires; the next
card is drawn #emph[externally] rather than chosen by the agent. It descends
from de Bono's thinking hats @debono1985hats by way of a survey of recursive
self-improvement @duan2026rsi, whose central move — treating the improvement
loop rather than the algorithm as the unit of analysis — suggested that a
process could be made a checkable object.

Because a deck is a bounded state machine, it can be verified exhaustively
before anyone runs it. Seventeen gates check a deck's well-formedness over
every reachable state; a simulator computes exact per-card and per-ordering
marginals by dynamic programming. That machinery found real defects in every
deck written for it: roles whose output nothing consumed, an exit reachable
having gathered no evidence, and a gut-call card that landed #emph[after] the
evidence in half of all runs.

None of that is in question here. What is in question is the justification
printed at the top of the skill:

#verdict[
  A procedure an agent follows on its own honour is not a procedure. It will
  reach the answer by the cheapest route and skip the step that would have
  caught the error.
][
  Refuted. See #ref(<sec:case-one>).
]

and its successor, adopted after the first was refuted:

#verdict[
  Having formed a plausible explanation, an agent asks #emph[how do I confirm
  this?] rather than #emph[what else would produce this symptom?]
][
  Refuted. See #ref(<sec:case-two>).
]
