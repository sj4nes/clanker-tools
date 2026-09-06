# dynkin_pi_lambda

## Type
theorem

## Statement
If P is a pi-system (closed under finite intersection) and L is a lambda-system (contains Omega, closed under proper differences and increasing countable unions) with P subset L, then sigma(P) subset L.

## Symbols
- `P` — a pi-system, type: subset of 2^Omega
- `L` — a lambda-system, type: subset of 2^Omega

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
generated_sigma_algebra, set_algebra, sigma_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: let L' be the smallest lambda-system containing P; show L' is closed under intersection (fix A in L', the sets B with A cap B in L' form a lambda-system containing P), hence L' is a sigma-algebra, so sigma(P) = L' subset L
derives_from: sigma_algebra
lean_status: cited — Billingsley Thm 3.2; Durrett A.1.4

## Type / well-formedness check
the standard uniqueness engine: two measures agreeing on a generating pi-system (and on Omega, if finite) agree on the whole sigma-algebra -- because the agreement set is a lambda-system.

## Specialization / boundary cases
- two probability measures equal on { (-inf, x] : x in R } are equal on B(R) -- this proves cdf_determines_law
- independence checked on generating pi-systems extends to the generated sigma-algebras (independence_factorization)

## Hypothesis-dropped counterexamples
- **pi_system**: measures can agree on a generating collection that is NOT a pi-system yet differ: on Omega={1,2,3,4}, uniform vs the measure (3/8,1/8,1/8,3/8) agree on {1,2} and {1,3} but not on {1} = {1,2} cap {1,3}

## Common misuse
- applying it when the generating family is not intersection-closed
- forgetting the 'agree on Omega' clause for finite (non-probability) measures

## Related nodes (non-prerequisite)
- used_by: cdf_determines_law, independence_factorization, mgf_uniqueness

## Sources
billingsley_probability_measure, durrett_pte
