# sigma_algebra

## Type
definition

## Statement
A family F of subsets of Omega is a sigma-algebra if Omega in F, F is closed under complement, and F is closed under countable unions (hence countable intersections).

## Symbols
- `Omega` — the sample space, type: set
- `F` — the family of events, type: subset of 2^Omega

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
countable_set, set_algebra

## Hypotheses
(none — unconditional within scope)

## Well-definedness
{empty, Omega} is a sigma-algebra and 2^Omega is a sigma-algebra, so the notion is non-vacuous; an arbitrary intersection of sigma-algebras is a sigma-algebra, which is what makes sigma(C) well-defined.

## Type / well-formedness check
closure is under COUNTABLE unions, not arbitrary; the three axioms give closure under countable intersection and set difference. The pair (Omega, F) is a measurable space.

## Specialization / boundary cases
- Omega countable: F = 2^Omega is the usual choice
- Omega = R: F = B(R), strictly smaller than 2^R (non-measurable sets exist under AC)

## Hypothesis-dropped counterexamples
- **countable_union_closure**: the family of finite-or-cofinite subsets of N is closed under complement and FINITE unions but not countable ones -- it is an algebra, not a sigma-algebra

## Common misuse
- assuming closure under arbitrary unions
- treating every subset of an uncountable Omega as an event

## In the wild
- stochastic calculus: the filtration (F_t) is an increasing family of sigma-algebras modelling information over time -- the object Ito integration and the Black-Scholes derivation are built on (Karatzas-Shreve 1991)
- the reason a probability model on [0,1] cannot use every subset: the Vitali / Banach-Tarski constructions force F = B(R), and every rigorous statement about a continuous random variable is implicitly relative to it

## Related nodes (non-prerequisite)
- generalizes: algebra of sets (finite closure only)
- special_case_of: Dynkin lambda-system + closure under intersection

## Sources
billingsley_probability_measure, folland_real_analysis
