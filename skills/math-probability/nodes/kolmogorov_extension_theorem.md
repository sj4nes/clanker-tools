# kolmogorov_extension_theorem

## Type
bridge

## Statement
Given a family of finite-dimensional distributions mu_{t_1,...,t_k} on R^k that is CONSISTENT (marginalizing mu over a coordinate gives the lower-dimensional mu, and permuting coordinates permutes the measure), there is a probability space carrying a process (X_t) with exactly those finite-dimensional distributions. STATED and CITED.

## Symbols
- `mu_{t_1..t_k}` — the prescribed finite-dimensional laws, type: probability measures on R^k
- `(X_t)` — the resulting process, type: T -> (Omega -> R)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
joint_distribution, lebesgue_measure_caratheodory, stochastic_process

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Caratheodory extension: the consistent f.d.d.s define a premeasure on the algebra of cylinder sets of R^T; consistency makes it well-defined and countably additive on that algebra (using compactness of R and inner regularity), so it extends to the product sigma-algebra
derives_from: lebesgue_measure_caratheodory
lean_status: cited — Billingsley Thm 36.1; Durrett Thm 6.1.1 (Kolmogorov); Tao

## Type / well-formedness check
the existence theorem underlying every stochastic-process construction (iid sequences, Markov chains from a transition kernel, Gaussian processes from a covariance function). Consistency is exactly the compatibility needed; the built measure lives on the product sigma-algebra of R^T.

## Specialization / boundary cases
- iid sequences: mu_{t_1,...,t_k} = mu^{tensor k} is trivially consistent -- gives the infinite product measure
- Markov chains: mu built from an initial law and a transition kernel via Chapman-Kolmogorov consistency
- Gaussian processes: any symmetric positive-semidefinite covariance function K(s,t) yields a centered Gaussian process

## Hypothesis-dropped counterexamples
- **consistency_of_the_f_d_d_s**: an inconsistent family (e.g. mu_{1,2} with a marginal on coordinate 1 disagreeing with mu_1) realizes no process -- consistency is necessary and sufficient
- **the_product_sigma_algebra_only**: the resulting measure only sees cylinder events; { t |-> X_t continuous } is NOT in the product sigma-algebra -- path properties need a separate modification argument (Kolmogorov-Chentsov)

## Common misuse
- expecting path regularity (continuity, boundedness) from the extension -- it gives only the f.d.d.s
- applying it to an index set where the underlying space is not standard Borel (the theorem needs Polish coordinate spaces)

## Related nodes (non-prerequisite)
- uses: lebesgue_measure_caratheodory (Caratheodory extension)
- constructs: iid, stochastic_process
- companion: Kolmogorov-Chentsov continuity criterion

## Sources
billingsley_probability_measure, durrett_pte
