# information_equality

## Type
identity

## Statement
Under regularity, I(theta) = Var_theta(U_1(theta)) = -E_theta[ d^2/dtheta^2 log f(X_1; theta) ]: the two information formulas agree.

## Symbols
- `I(theta)` — Fisher information
- `d^2/dtheta^2 log f` — the observation's log-likelihood curvature
- `-E[d^2 ell]` — the 'expected information'; its sample analogue -d^2 ell(theta_hat) is the OBSERVED information

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
fisher_information, interchange_derivative_integral, log_likelihood_smooth, score_identity

## Hypotheses
interchange_derivative_integral, log_likelihood_smooth

## Proof provenance
technique: differentiate the score identity a second time under the integral sign; product rule
derives_from: score_identity
lean_status: core — validation/proof-checks.lean Stat.information_equality -- given int f = 1 and the two interchanges, E[d2 log f] + E[(d log f)^2] = 0

## Type / well-formedness check
An identity, per observation. Proof: differentiate the score identity int (d log f) f dx = 0 once more; product rule gives int (d^2 log f) f + int (d log f)^2 f = 0, i.e. E[d^2 log f] + E[(d log f)^2] = 0.

## Specialization / boundary cases
- Bernoulli: -E[d^2/dp^2 ell_1] = -E[-X/p^2 - (1-X)/(1-p)^2] = 1/(p(1-p)) = Var((X-p)/(p(1-p)))
- exponential family: both sides equal A''(eta) -- the cumulant function's curvature
- lets you estimate I(theta) either by the sample variance of the scores or by the negative average Hessian (the latter is what optimizers return for free)

## Hypothesis-dropped counterexamples
- **interchange_derivative_integral**: same failure as score_identity: without the second interchange the two formulas disagree and the 'sandwich' variance A^{-1} B A^{-1} (with A != B) is the correct one -- this is exactly the misspecification-robust case
- **log_likelihood_smooth**: a non-twice-differentiable log-density (Laplace / double-exponential at its median) -- the second-derivative form does not exist though the variance form may

## Common misuse
- reporting the negative-Hessian (observed information) standard errors when the model is misspecified -- use the sandwich estimator
- assuming the equality to justify dropping the score-variance computation in a quasi-likelihood setting where it does NOT hold

## In the wild
- every optimizer that reports standard errors from the inverse Hessian at the optimum is using this identity (Hessian = -observed information ~ -n I)
- the score test statistic U(theta_0)^2 / (n I(theta_0)) uses the expected-information form under the null

## Related nodes (non-prerequisite)
- equivalent_to: fisher_information
- required_by: score_test, mle_asymptotic_normality

## Sources
casella_berger_2e, cox_hinkley_theoretical_statistics
