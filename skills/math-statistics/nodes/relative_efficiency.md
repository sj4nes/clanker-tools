# relative_efficiency

## Type
definition

## Statement
The asymptotic relative efficiency of estimator A to estimator B (both sqrt(n)-normal for the same estimand) is ARE(A, B) = AVar(B) / AVar(A); A is more efficient when ARE > 1.

## Symbols
- `ARE` — asymptotic relative efficiency, type: positive real (may depend on theta)

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
asymptotic_variance

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A ratio of asymptotic variances. ARE(A, B) = c means B needs about 1/c times as many observations as A to match precision (large n).

## Specialization / boundary cases
- sample mean vs sample median for a NORMAL location: ARE(median, mean) = 2/pi ~ 0.64 -- the median wastes ~36% of the data
- for a Laplace (double-exponential) location: ARE(median, mean) = 2 -- the median is twice as efficient
- for t_3 errors the median beats the mean; the crossover is around 'tails heavier than t_5'

## Hypothesis-dropped counterexamples
- **same_rate**: comparing a sqrt(n) estimator to an n-rate estimator (uniform endpoint) by an ARE is meaningless -- the ratio degenerates to 0 or inf

## Common misuse
- quoting a single ARE number when it depends on the (unknown) error distribution
- ignoring finite-sample robustness -- an efficient-at-the-normal estimator can be terrible under contamination

## Related nodes (non-prerequisite)
- generalizes_from: asymptotic_variance

## Sources
van_der_vaart_asymptotic, lehmann_casella_tpe
