# cramer_rao_lower_bound

## Type
theorem

## Statement
Under regularity, any estimator theta_hat with E_theta[theta_hat] = theta + b(theta) satisfies Var_theta(theta_hat) >= (1 + b'(theta))^2 / (n I(theta)); for an unbiased estimator, Var_theta(theta_hat) >= 1 / (n I(theta)).

## Symbols
- `n I(theta)` — the sample Fisher information
- `b(theta)` — the bias; b'(theta) its theta-derivative
- `1/(n I(theta))` — the information bound / 'CRLB'

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
fisher_information, interchange_derivative_integral, prob_cauchy_schwarz, prob_covariance, score_identity, unbiased_estimator

## Hypotheses
unbiased_estimator, support_independent_of_theta, interchange_derivative_integral

## Proof provenance
technique: Cauchy-Schwarz applied to the covariance of theta_hat and the score, using E[score] = 0 and Cov(theta_hat, score) = 1 + b'
derives_from: prob_cauchy_schwarz
lean_status: core — validation/proof-checks.lean Stat.crlb_cauchy_schwarz -- the step Cov(a, s)^2 <= Var(a) Var(s) at sample covariances (bc grid for the equality case), plus Cov = 1 + b' from the score identity

## Type / well-formedness check
A variance lower bound holding for a FIXED n (not asymptotic). Proof: Cov_theta(theta_hat, U(theta)) = 1 + b'(theta) (differentiate E[theta_hat] = theta + b under the integral sign and use E[U] = 0); then Cauchy-Schwarz gives (1 + b')^2 = Cov(theta_hat, U)^2 <= Var(theta_hat) Var(U) = Var(theta_hat) . n I(theta).

## Specialization / boundary cases
- Bernoulli(p) unbiased: Var >= p(1-p)/n -- attained by Xbar, so Xbar is efficient
- Poisson(lambda) unbiased: Var >= lambda/n -- attained by Xbar
- N(mu, sigma^2), estimating sigma^2 unbiasedly: Var >= 2 sigma^4 / n -- S^2 has variance 2 sigma^4/(n-1) > the bound, so NO unbiased estimator of sigma^2 attains the CRLB
- biased form: for the MLE of sigma^2 (divisor n) the (1 + b')^2 numerator with b = -sigma^2/n gives a smaller bound, consistent with its smaller variance

## Hypothesis-dropped counterexamples
- **support_independent_of_theta**: uniform(0, theta): the naive CRLB gives Var >= theta^2/n, but (n+1)/n X_(n) has variance ~ theta^2/n^2 -- it BEATS the 'bound' by a factor n. The regularity failure makes the CRLB inapplicable, not merely loose.
- **interchange_derivative_integral**: if d/dtheta and int do not commute, Cov(theta_hat, U) != 1 + b' and the bound is simply wrong
- **unbiased_estimator**: for biased estimators the bound has the (1 + b')^2 numerator; quoting 1/(nI) for a biased estimator is a category error

## Common misuse
- quoting Var >= 1/(nI) for the MLE at finite n -- the MLE is biased at finite n and only ATTAINS the bound asymptotically
- concluding an estimator is 'bad' because Var > CRLB -- the bound may be unattainable by ANY unbiased estimator (the sigma^2 case)
- applying it to non-regular models (uniform, shifted exponential)

## In the wild
- the benchmark for every estimator in signal processing and physics: 'we are within 5% of the CRLB' is the standard claim for a sensor / phase estimator (GPS timing, gravitational-wave parameter estimation, radar)
- quantum metrology: the quantum CRLB (via the quantum Fisher information) sets the Heisenberg limit for phase estimation

## Related nodes (non-prerequisite)
- required_by: asymptotic_efficiency, crlb_attainment, local_asymptotic_minimax
- strengthened_by: hajek_convolution_theorem
- uses: score_identity, fisher_information

## Sources
casella_berger_2e, lehmann_casella_tpe, kay_estimation_theory
