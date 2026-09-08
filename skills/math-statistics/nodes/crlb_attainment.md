# crlb_attainment

## Type
proposition

## Statement
An unbiased estimator attains the Cramer-Rao bound Var = 1/(n I(theta)) for EVERY theta if and only if the model is a one-parameter exponential family in its natural parametrization and theta_hat is (an affine function of) its natural sufficient statistic; equivalently, the score is a.s. affine in theta_hat.

## Symbols
- `the equality condition` — Cauchy-Schwarz is tight iff theta_hat - E[theta_hat] and the score are a.s. proportional

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
cramer_rao_lower_bound, exponential_family, exponential_family_sufficient_statistic

## Hypotheses
unbiased_estimator

## Proof provenance
technique: Cauchy-Schwarz equality: Var(theta_hat) Var(U) = Cov(theta_hat, U)^2 iff theta_hat - E theta_hat proportional a.s. to U; integrating the resulting score
derives_from: cramer_rao_lower_bound
lean_status: cited

## Type / well-formedness check
The 'iff' comes from the Cauchy-Schwarz equality condition in the CRLB proof. Tightness forces score = c(theta)(theta_hat - theta), which integrates to an exponential-family log-density.

## Specialization / boundary cases
- Bernoulli / Poisson / normal-mean: Xbar attains the CRLB for all n -- these are one-parameter exponential families with T = x
- normal VARIANCE (mu known): sum(x_i - mu)^2 / n attains it for sigma^2? -- yes, T = (x - mu)^2 is the natural statistic; but the UNBIASED version /(n) with mu known does attain, while with mu unknown S^2 does not
- estimating p(1-p), or sigma (not sigma^2), or 1/lambda: NOT the natural parameter -- no unbiased estimator attains the CRLB at finite n

## Hypothesis-dropped counterexamples
- **natural_parameter**: estimating sigma (SD, not variance) in a normal model: even the UMVUE has variance strictly above 1/(nI) for every n, because sigma is a nonlinear function of the natural parameter -- the CRLB is unattainable, though approached as n -> inf

## Common misuse
- expecting the MLE to attain the CRLB at finite n for a general model -- it only does so for the natural parameter of an exponential family
- concluding an estimator is suboptimal because Var > CRLB when the bound is provably unattainable

## Related nodes (non-prerequisite)
- uses: exponential_family, exponential_family_sufficient_statistic

## Sources
lehmann_casella_tpe, casella_berger_2e
