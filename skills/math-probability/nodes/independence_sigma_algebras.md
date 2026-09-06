# independence_sigma_algebras

## Type
definition

## Statement
Sub-sigma-algebras G_1, ..., G_n of F are independent if P(bigcap_i A_i) = prod_i P(A_i) for every choice of A_i in G_i. Equivalently, generating pi-systems can be checked (via pi-lambda).

## Symbols
- `G_i` — sub-sigma-algebras, type: sigma-algebra subset F
- `A_i` — A_i in G_i, type: element of G_i

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
independence_events, sigma_algebra

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the set of A_1 for which the factorization holds (with A_2, ..., A_n fixed in generating pi-systems) is a lambda-system; pi-lambda extends it to all of G_1, then iterate.

## Type / well-formedness check
the right level of generality: independence of random variables is independence of the sigma-algebras they generate. By the pi-lambda theorem it suffices to verify the factorization on generating pi-systems (this is what makes it checkable).

## Specialization / boundary cases
- G_i = sigma(X_i): recovers independence_random_variables
- G = { empty, Omega }: independent of every sigma-algebra
- the tail sigma-algebra of an independent sequence is independent of every finite prefix -- Kolmogorov's zero-one law

## Hypothesis-dropped counterexamples
- **factorization_on_a_pi_system_that_generates**: checking factorization on a generating family that is not intersection-closed does not extend (dynkin_pi_lambda counterexample)

## Common misuse
- verifying independence on a non-pi-system and extending
- conflating independence of G_1, G_2 with G_1 cap G_2 = { empty, Omega }

## Related nodes (non-prerequisite)
- uses: dynkin_pi_lambda
- specializes_to: independence_random_variables
- generalizes: independence_events

## Sources
billingsley_probability_measure, durrett_pte
