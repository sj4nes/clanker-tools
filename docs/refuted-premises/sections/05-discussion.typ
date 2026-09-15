#import "../preamble.typ": keyterm

= What survives <sec:discussion>

Two refutations do not make the tool worthless; they remove two justifications
for it. Saying precisely what remains is the whole discipline of the sixth
condition, and it is easier to state than to practise.

== What is gone

The skill claimed to make an agent more thorough. It does not, and its
documentation now says so in a table rather than in an assertion. Both
behavioural claims were struck rather than reworded.

== What remains, and is demonstrated rather than assumed

#keyterm[The deck-checking machinery], which is independent of any claim about
agents. It found decorative roles, an exit reachable without evidence, an
ordering defect in which a prior was recorded after the evidence in half of all
runs, and — through an extremal query over paths rather than a safety property —
a process satisfiable by padding with the cheapest available step. Those are
defects in a written-down procedure, and they would be defects if a person
followed it.

#keyterm[An auditable, replayable record]. This earned its keep exactly once,
and instructively. In a real diagnosis of a separate codebase, the tool produced
a conclusion that was wrong — not because any fact gathered was false, but
because the evidence-gathering step had been aimed at a file describing a
process the project had abandoned a month earlier. Every fact was true; the
conclusion was not. The ledger recorded which sources had been read, so the
error was diagnosable in seconds rather than mysterious.

== The failure neither fixture tests

That episode is the more useful finding of the whole exercise, and neither case
study touches it. Grounding a step in an instrument proves a command #emph[ran].
It says nothing about whether the command was aimed at something alive. An
authoritative-looking dead file is indistinguishable from a live one at the
instrument layer, and no amount of discrimination discipline catches it — the
subject had already asked #emph[what else would explain this?] and had simply
never asked #emph[is this source current?]

This suggests the productive direction is not more behavioural forcing but
#keyterm[source authority]: letting a process declare which sources are
authoritative, and warning when a step reads outside that set or reads a file
older than the artifact it purports to describe. Neither is a judgement call,
and both are mechanizable.

== A note on where the effort went

The uncomfortable summary is worth stating plainly. A day was spent building
machinery to force behaviours that the subjects already exhibited unprompted,
and the one failure actually encountered in practice is one the machinery does
not address. The measurements cost sixteen agents and roughly four minutes of
wall time. They should have been taken first.
