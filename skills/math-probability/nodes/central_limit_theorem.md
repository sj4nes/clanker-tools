# central_limit_theorem

## Type
theorem

## Statement
X_i iid, mean mu, variance sigma^2 in (0, inf) => sqrt(n)(Xbar_n - mu)/sigma -> N(0,1) in distribution. See results/central_limit_theorem.yaml.

## Symbols
- `X_i` — an iid sequence with finite nonzero variance, type: N -> L^2(P)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
characteristic_function, convergence_in_distribution, expectation, iid, levy_continuity_theorem, mgf_sum_independent, standard_normal, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: CF of the standardized sum -> e^{-t^2/2}, then Levy's continuity theorem
derives_from: levy_continuity_theorem
lean_status: cited — Billingsley Thm 27.1

## Type / well-formedness check
see the hand-written results/central_limit_theorem.yaml for the full treatment. Convergence mode: IN DISTRIBUTION (not a.s. or in probability).

## Specialization / boundary cases
- Bernoulli(p): de Moivre-Laplace
- normal X_i: exact for every n

## Hypothesis-dropped counterexamples
- **finite_nonzero_variance**: Cauchy: Xbar_n stays Cauchy -- no normal limit

## Common misuse
- claiming a rate (that is Berry-Esseen)
- treating finite n as exactly normal in the tails

## Related nodes (non-prerequisite)
- full_entry: results/central_limit_theorem.yaml
- uses: levy_continuity_theorem

## Sources
billingsley_probability_measure, durrett_pte
