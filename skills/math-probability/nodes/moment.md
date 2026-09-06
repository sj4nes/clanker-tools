# moment

## Type
definition

## Statement
The k-th (raw) moment of X is m_k = E[X^k]; the k-th central moment is mu_k = E[(X - E[X])^k]. Skewness = mu_3 / sigma^3, (excess) kurtosis = mu_4 / sigma^4 - 3.

## Symbols
- `X` — a random variable, type: Omega -> R
- `k` — a nonnegative integer, type: natural number

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, lotus

## Hypotheses
(none — unconditional within scope)

## Well-definedness
E[|X|^k] in [0, inf] always exists; m_k finite iff X in L^k(P). The central moments are polynomials in the raw moments via the binomial expansion.

## Type / well-formedness check
m_k is defined (finite) when E[|X|^k] < inf; by the moment ladder this then implies all lower moments are finite. mu_1 = 0, mu_2 = Var.

## Specialization / boundary cases
- k = 1: the mean; k = 2 central: the variance
- symmetric law: all odd central moments are 0
- normal: mu_{2k} = sigma^{2k} (2k-1)!! -- so kurtosis 0 (the baseline for 'excess')

## Hypothesis-dropped counterexamples
- **finite_k_th_absolute_moment**: Student's t with nu degrees of freedom has E[|X|^k] = inf for k >= nu -- moments beyond a point simply do not exist for heavy-tailed laws

## Common misuse
- assuming a distribution is determined by its moments (the moment problem can be indeterminate -- e.g. the lognormal)
- estimating high moments from small samples (enormous variance)

## Related nodes (non-prerequisite)
- generated_by: mgf (mgf_moments)
- ordered_by: moment_ladder

## Sources
billingsley_probability_measure, grimmett_stirzaker
