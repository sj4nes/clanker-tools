# measure

## Type
definition

## Statement
A measure on (Omega, F) is a function mu: F -> [0, inf] with mu(empty) = 0 that is countably additive: for pairwise-disjoint A_1, A_2, ... in F, mu(bigcup_n A_n) = sum_n mu(A_n).

## Symbols
- `mu` — the measure, type: F -> [0, inf]
- `(A_n)` — a countable disjoint family, type: N -> F

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
countable_set, measurable_space, real_field, series_convergence, sigma_algebra

## Hypotheses
(none — unconditional within scope)

## Well-definedness
mu(empty) = 0 follows from countable additivity unless mu is identically +inf; monotonicity and countable subadditivity are consequences. Counting measure, Lebesgue measure, and Dirac delta_x are the standard examples.

## Type / well-formedness check
countable additivity is over a COUNTABLE disjoint family; the sum is a series in [0, inf] and always has a value. mu is sigma-finite if Omega is a countable union of finite-measure sets -- the hypothesis of Radon-Nikodym and Fubini.

## Specialization / boundary cases
- mu(Omega) = 1: a probability measure (kolmogorov_axioms)
- mu = counting measure on a countable Omega: mu(A) = |A|
- mu = delta_x: mu(A) = 1 if x in A else 0

## Hypothesis-dropped counterexamples
- **countable_additivity**: a merely finitely additive set function (e.g. a Banach limit / finitely additive extension of density on N) is not a measure and breaks continuity from below and Borel-Cantelli

## Common misuse
- assuming finite additivity is enough
- forgetting sigma-finiteness for Radon-Nikodym / Fubini
- treating mu(A) = inf results carelessly in subtractions

## In the wild
- measure-theoretic probability is the foundation under empirical process theory and the modern analysis of stochastic gradient descent (a.s. convergence, rates) -- Bottou-Curtis-Nocedal 2018
- the pushforward / change-of-variables machinery is what normalising flows (RealNVP, Glow) exploit to turn a simple base measure into a complex learned density

## Related nodes (non-prerequisite)
- specializes_to: probability_measure
- generalizes: finitely additive set function

## Sources
billingsley_probability_measure, folland_real_analysis
