# borel_cantelli_second

## Type
theorem

## Statement
If the events A_n are INDEPENDENT and sum_n P(A_n) = inf, then P(A_n infinitely often) = 1.

## Symbols
- `(A_n)` — an independent sequence of events, type: N -> F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
complement_rule, continuity_of_probability, independence_events, limsup_liminf, series_convergence

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: bound prod_{n=M}^{N} (1 - P(A_n)) by exp(-sum P(A_n)) -> 0; hence P(bigcup_{n>=M} A_n) = 1 for all M; intersect over M
derives_from: continuity_of_probability
lean_status: cited — Billingsley Thm 4.4

## Type / well-formedness check
the partial converse to BC1, and it does need independence. P(no A_n for n in [M, N]) = prod (1 - P(A_n)) <= prod e^{-P(A_n)} = e^{-sum} -> 0, so P(some A_n for n >= M) = 1 for every M.

## Specialization / boundary cases
- together with BC1: for INDEPENDENT events, P(A_n i.o.) is 0 or 1 according as sum P(A_n) converges or diverges -- a zero-one law
- A_n = { X_n > c_n } for iid X_n: P(X_n > c_n i.o.) is 0 or 1 by whether sum P(X_1 > c_n) converges

## Hypothesis-dropped counterexamples
- **independence**: A_n = A fixed with 0 < P(A) < 1: sum P(A_n) = inf but P(A i.o.) = P(A) != 1. Pairwise independence is not quite enough in general; mutual (or the Kochen-Stone refinement) is the clean hypothesis.

## Common misuse
- applying it to dependent events
- forgetting that BC1 needs NO independence but BC2 does

## Related nodes (non-prerequisite)
- dual_of: borel_cantelli_first
- special_case_of: Kolmogorov's zero-one law

## Sources
billingsley_probability_measure, durrett_pte
