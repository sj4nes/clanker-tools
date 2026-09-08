# bernstein_von_mises

## Type
theorem

## Statement
Under the same regularity as MLE asymptotic normality and any prior with positive continuous density near theta_0, the posterior distribution of sqrt(n)(theta - theta_hat_n) converges (in total variation, in P_{theta_0}-probability) to N(0, I(theta_0)^{-1}); consequently Bayesian credible sets have frequentist coverage 1 - alpha asymptotically.

## Symbols
- `pi(. | X)` — the posterior
- `TV` — total variation distance
- `consequence` — a 95% credible interval is asymptotically a 95% confidence interval

## Epistemic status
proved_theorem  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
bayes_estimator, credible_interval, fisher_information, mle_asymptotic_normality

## Hypotheses
true_parameter_interior, fisher_information_positive_definite, log_likelihood_smooth, identifiability

## Proof provenance
technique: Taylor-expand the log-posterior about theta_hat_n; the quadratic term dominates, the prior contributes O(1/n), the remainder is o_p(1) uniformly on sqrt(n)-neighbourhoods
derives_from: mle_asymptotic_normality
lean_status: cited — CITED -- van der Vaart Asymptotic Statistics Ch. 10; Le Cam. Not formalized.

## Type / well-formedness check
A convergence-of-measures statement about the posterior, holding in P_{theta_0}-probability (a frequentist statement about a Bayesian object). The prior washes out at rate 1/sqrt(n).

## Specialization / boundary cases
- Beta(a,b)-Bernoulli: the Beta(a + s, b + n - s) posterior is asymptotically N(p_hat, p_hat(1-p_hat)/n) -- matches the Wald interval
- the prior choice affects only the O(1/n) correction for large n
- the practical upshot: for regular parametric models, large-sample Bayesian and frequentist intervals agree

## Hypothesis-dropped counterexamples
- **true_parameter_interior**: boundary parameter (a variance component at 0): the posterior piles up against the boundary and is NOT asymptotically normal; credible intervals do NOT have frequentist coverage
- **fixed_finite_dimension**: in nonparametric / high-dimensional models Bernstein-von Mises can FAIL -- credible bands can badly under- or over-cover (Cox 1993, Freedman 1999); this is an active research area
- **identifiability**: non-identified parameter: the posterior does not concentrate and coverage is prior-driven

## Common misuse
- citing it to claim Bayesian and frequentist intervals 'always' agree -- it is parametric, regular, large-n only
- assuming a credible interval has frequentist coverage in a hierarchical or nonparametric model

## Related nodes (non-prerequisite)
- approximates: mle_asymptotic_normality
- required_by: 
- uses: credible_interval

## Sources
van_der_vaart_asymptotic, le_cam_asymptotic_methods, freedman_1999
