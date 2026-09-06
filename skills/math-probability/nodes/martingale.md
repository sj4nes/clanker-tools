# martingale

## Type
bridge

## Statement
A sequence (X_n) adapted to a filtration (F_n) with E|X_n| < inf and E[X_{n+1} | F_n] = X_n for all n. (Supermartingale: <= ; submartingale: >= .) STATED here as the doorway to stochastic processes; not developed in this release.

## Symbols
- `(X_n)` — an adapted integrable sequence, type: N -> L^1(P)
- `(F_n)` — a filtration, type: increasing sequence of sub-sigma-algebras

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_expectation_abstract, tower_property

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: definition only; the theory (Doob's convergence theorem, optional stopping, L^p maximal inequalities, the martingale CLT) is CITED to Williams / Durrett ch. 5 and deferred to Release 0.2
derives_from: tower_property
lean_status: cited — Williams Probability with Martingales chs. 10-14; Durrett ch. 5

## Type / well-formedness check
the model of a fair game: the best forecast of tomorrow given everything known today is today's value. By the tower property E[X_n] = E[X_0] for all n. The convergence theorem, optional stopping, and the maximal / Doob inequalities are the content of a future release.

## Specialization / boundary cases
- S_n = sum of iid mean-0 increments: a martingale w.r.t. its natural filtration
- M_n = E[Y | F_n] for a fixed integrable Y (a Doob martingale): converges a.s. and in L^1 to E[Y | F_inf]
- the likelihood ratio prod (q(X_i)/p(X_i)) under p: a nonnegative martingale

## Hypothesis-dropped counterexamples
- **adaptedness_and_integrability**: if X_n is not F_n-measurable or not integrable the conditional expectation is ill-posed
- **the_equality_(fair_game)**: E[X_{n+1} | F_n] > X_n (submartingale) models a favorable game -- convex functions of a martingale are submartingales (conditional Jensen)

## Common misuse
- assuming a martingale converges without an L^1-boundedness or uniform-integrability condition
- applying optional stopping without a boundedness / integrability side condition (the St Petersburg / doubling paradox)

## Related nodes (non-prerequisite)
- uses: conditional_expectation_abstract, tower_property
- developed_in: Release 0.2 / a stochastic-processes capsule

## Sources
williams_probability_martingales, durrett_pte
