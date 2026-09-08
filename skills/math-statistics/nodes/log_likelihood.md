# log_likelihood

## Type
definition

## Statement
The log-likelihood is ell(theta) = log L(theta) = sum_{i=1}^n log f(x_i; theta).

## Symbols
- `ell(theta)` — the log-likelihood, type: function Theta -> [-inf, inf)
- `ell_i(theta) = log f(x_i; theta)` — the i-th contribution

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
likelihood_function

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Same theta-free additive constant ambiguity as L (from the choice of mu). Differences ell(theta_1) - ell(theta_2) are unambiguous.

## Type / well-formedness check
ell is well defined (possibly -inf) wherever L >= 0; the product becoming a SUM is the point -- it makes the score a sum of iid terms and hands the CLT its hypothesis.

## Specialization / boundary cases
- Bernoulli: ell(p) = (sum x_i) log p + (n - sum x_i) log(1 - p)
- the maximizer of ell is the maximizer of L (log is increasing) -- this is why one always works with ell
- at a data point with f(x_i; theta) = 0, ell(theta) = -inf: theta is excluded

## Common misuse
- differentiating L instead of ell and drowning in product rule
- forgetting ell can be -inf on part of Theta (support constraints)

## Related nodes (non-prerequisite)
- required_by: score_function, likelihood_ratio_test

## Sources
casella_berger_2e
