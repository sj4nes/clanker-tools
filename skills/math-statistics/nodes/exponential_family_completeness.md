# exponential_family_completeness

## Type
theorem

## Statement
If the natural parameter space H contains a nonempty open set (the family is full-rank), then the natural sufficient statistic sum_i T(X_i) is complete.

## Symbols
- `complete` — E_eta[g(sum T)] = 0 for all eta implies g = 0 a.s.
- `full-rank / regular` — int(H) nonempty and T has no a.s. affine dependency

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
completeness_statistic, exponential_family, natural_parameter_space

## Hypotheses
natural_parameter_space

## Proof provenance
technique: uniqueness of the (two-sided) Laplace transform on an open set
derives_from: natural_parameter_space
lean_status: cited — Laplace-transform uniqueness is the analytic input; CITED to Lehmann-Romano TSH Thm 4.3.1

## Type / well-formedness check
A completeness claim. Proof: E_eta[g(S)] = 0 for all eta in an open set makes the two-sided Laplace transform of g times the S-density vanish on an open set; by uniqueness of the Laplace transform g = 0 a.e.

## Specialization / boundary cases
- N(mu, sigma^2) full family: (sum X_i, sum X_i^2) is complete -- hence (Xbar, S^2) is, so any unbiased function of it is UMVUE (Lehmann-Scheffe)
- Bernoulli, Poisson, exponential: sum X_i is complete
- used to get Xbar _||_ S^2 for a normal sample via Basu

## Hypothesis-dropped counterexamples
- **full_rank**: the CURVED family N(theta, theta^2) (one parameter, T two-dimensional constrained to a parabola): the sufficient statistic is NOT complete -- there exist nonzero unbiased-of-zero functions. UMVUE claims via Lehmann-Scheffe then do not go through.
- **H_open**: N(mu, sigma^2) with sigma^2 KNOWN and mu restricted to integers: H is not open, sum X_i is sufficient but not complete

## Common misuse
- assuming completeness for a curved exponential family or a family with a constrained parameter
- concluding an estimator is UMVUE from sufficiency alone, without completeness

## Related nodes (non-prerequisite)
- required_by: basu_theorem, lehmann_scheffe_theorem
- commonly_confused_with: minimal_sufficiency

## Sources
lehmann_romano_tsh, lehmann_casella_tpe
