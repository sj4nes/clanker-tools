# measurable_function

## Type
definition

## Statement
f: (Omega, F) -> (E, E') is measurable if f^{-1}(B) in F for every B in E'. For E' = B(R) it suffices that { f <= x } in F for every x.

## Symbols
- `f` — the function, type: Omega -> E
- `(E, E')` — the target measurable space, type: measurable space

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
borel_sigma_algebra, measurable_space, preimage_algebra

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the collection { B : f^{-1}(B) in F } is a sigma-algebra, so it suffices to check measurability on a generating collection of E' (the half-lines for B(R)).

## Type / well-formedness check
measurability is preservation of structure BACKWARD (preimage), which is why the preimage algebra -- not the image -- is the tool. Continuous functions R -> R are Borel measurable; measurable functions are closed under +, x, sup_n, liminf_n, limits.

## Specialization / boundary cases
- f = 1_A: measurable iff A in F
- f continuous: Borel measurable
- f = sup_n f_n of measurable f_n: measurable

## Hypothesis-dropped counterexamples
- **generating_collection_check**: checking f^{-1} of a non-generating family is not enough; and a pointwise limit of measurable functions is measurable but a limit of continuous functions need not be continuous

## Common misuse
- checking the forward image instead of the preimage
- assuming an arbitrary function Omega -> R is measurable

## Related nodes (non-prerequisite)
- used_by: random_variable, abstract_integral, conditional_expectation_abstract
- developed_in: math-sets-functions-cardinality (preimage algebra)

## Sources
billingsley_probability_measure, folland_real_analysis
