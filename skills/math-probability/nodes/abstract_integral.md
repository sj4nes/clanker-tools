# abstract_integral

## Type
bridge

## Statement
For a measure space (Omega, F, mu) and a measurable f: Omega -> [0, inf], integral f dmu is defined as sup over simple 0 <= s <= f of integral s dmu; for general f it is integral f^+ dmu - integral f^- dmu when at least one part is finite. f is integrable if integral |f| dmu < inf.

## Symbols
- `f` — a measurable function, type: Omega -> R (or [0, inf])
- `mu` — the measure, type: measure on F
- `integral f dmu` — the integral, type: real or +-inf

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
measurable_function, measure, real_field

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: standard three-step construction: indicators -> nonnegative simple functions (finite sums) -> nonnegative measurable via MCT -> integrable via f = f^+ - f^-
lean_status: cited — Folland Real Analysis 2e SS2.2-2.4; Billingsley SS15-16

## Type / well-formedness check
CITED, not constructed. The integral is linear, monotone, and satisfies MCT / DCT / Fatou; E[X] is this integral against P. f measurable is required for the sup to be over a well-defined set.

## Specialization / boundary cases
- mu = P: integral X dP = E[X]
- mu = counting measure on N: integral f dmu = sum_n f(n) -- series are integrals
- f = 1_A: integral 1_A dmu = mu(A)

## Hypothesis-dropped counterexamples
- **measurability_of_f**: a non-measurable f has no well-defined integral -- the defining sup is over an ill-specified family and Fubini/Tonelli fail

## Common misuse
- swapping limit and integral without MCT/DCT/Fatou justification
- assuming integral f dmu is finite for every measurable f

## Related nodes (non-prerequisite)
- specializes_to: expectation
- developed_in: a future math-measure-and-integration capsule

## Sources
folland_real_analysis, billingsley_probability_measure
