#import "../preamble.typ": keyterm

= Method <sec:method>

The procedure below was not designed in advance. It was extracted after the
fact from what the two experiments actually required, and is stated here as six
conditions because that is how it is now written down as a reusable skill.

== Split the claim, and fixture only the behavioural half

Most default-behaviour claims are two claims. #emph[An agent will skip the
step, so the process must force it] contains a structural half — does the
process in fact make skipping impossible — and a behavioural half — would
anyone actually skip it.

The structural half needs no subjects. In our case it was already settled by an
exhaustive gate over the reachable state space: no path to a terminal state can
omit a required role. That half therefore left the experiment entirely, which
removed an arm and halved the cost. What remained was a single question with a
single arm.

== The author cannot be a subject

Knowing the hypothesis destroys the measurement and no discipline repairs it.
Subjects must be naive. We used fresh language-model agents with no shared
context, given the task and nothing else: no mention of the skill, no
suggestion that a particular behaviour was of interest, no indication that
anything was being measured.

== The measurement must be unforgeable

Self-report is worthless here. An agent asked whether it considered
alternatives will say yes. Two forms of measurement survive that objection, and
we used one in each case study:

+ #keyterm[An artefact of doing the work] — a string, file or side effect that
  appears only if the work happened and cannot be reached from the material the
  subject was given.
+ #keyterm[Executing the subject's own output] — apply their patch and score
  what it does, rather than what they wrote about it.

== Pre-register in a separate commit

Write the interpretation for every outcome, including those that refute you;
implement the scoring mechanically; then commit that, alone, before any result
exists. Pre-registration that cannot be proved is pre-registration nobody need
believe, and the proof is cheap — the scorer's commit must strictly precede the
results'.

We failed this on the first case study and pass it on the second. The failure
is discussed in #ref(<sec:limitations>) and is asserted, permanently, by a check
that ships with the method.

== Build from a real failure, and let the shortcut pass its own check

A contrived puzzle generalises to nothing, so both fixtures were rebuilt from
defects that had actually occurred in the repository's history.

The subtler condition is the second. The failing behaviour must #emph[succeed on
its own terms]. If a subject who stops early gets an obviously wrong answer, the
experiment has measured competence rather than the default. The shortcut has to
feel sufficient — which, in the second case study, meant designing a bug whose
visible cause completely explains the visible symptom.

== Strike a refuted claim; do not reword it

The reflex on a negative result is to substitute a similar-sounding claim that
was not tested. That is the original failure relocated one level up, and it is
how a methodology survives indefinitely on a rotating cast of untested premises.

This is not hypothetical. The second case study exists precisely because the
reflex after the first refutation was to say #emph[well, but agents do not
enumerate alternatives]. Turning that reflex into a measurement killed it too.
