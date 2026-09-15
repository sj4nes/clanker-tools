= Limitations <sec:limitations>

== The method has never returned a positive

This is the limitation that should temper every conclusion above. Two
experiments, two refutations, and no confirmations. Nothing here demonstrates
that the method can confirm a claim that is #emph[true], rather than being
biased toward refutation by fixtures built to be winnable.

The control is specific and has not been run: a fixture reproducing the shape of
an already-established result — agents falling back to poor default testing
across every condition tested @danluu2026agents — should come back positive. If
it does not, the method is broken rather than the claims being false, and every
result in this note is suspect.

== Pre-registration was provable in only one of two cases

The scorer for case study 1 was written before any result existed, in-session,
while the subjects worked. It was then committed #emph[alongside] the results.
The record therefore cannot distinguish that from writing it afterwards.

This is asserted rather than repaired. A check shipped with the method compares
commit order and fails, permanently, on case study 1. Rewriting history to make
it pass would destroy the only honest demonstration the method has of why the
condition says #emph[separate commit].

== Subject naivety is asserted, not verified

Subjects were fresh agents with no shared context, but with filesystem access to
a repository documenting the hypotheses under test. Unforgeable scoring means
priming could not fabricate a result, but nothing measured what subjects read.
A primed subject inflates a positive; neither case study produced one, so the
direction of this bias is at least not toward the reported conclusion.

== Scope

Both fixtures are small, bounded, single-question tasks in a two-file directory,
where investigating costs nothing. #emph[Will an agent run a script handed to
it] is not #emph[will an agent commission an expensive experiment, wait on a
slow pipeline, or ask a human]. Whether the same holds when the second cause
costs an hour is untested, and these fixtures cannot answer it.

Both runs used one model on one day, eight subjects per claim, one bug
shape per claim. The confounds above are recorded because they are real, not in
order to rescue a claim the results refuted: 8 of 8 with half a cohort exceeding
the fixture is not a marginal outcome, and the honest response is to change the
methodology rather than to keep searching for a framing in which it was right.
