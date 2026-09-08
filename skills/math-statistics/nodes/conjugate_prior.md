# conjugate_prior

## Type
definition

## Statement
A family of priors F is conjugate to a likelihood model if for every prior in F and every dataset the posterior is again in F; the update is then a closed-form change of the family's hyperparameters.

## Symbols
- `F` — the conjugate family (Beta, Gamma, Normal-inverse-Gamma, Dirichlet, ...)
- `hyperparameters` — the parameters of the prior, updated by simple sufficient-statistic arithmetic

## Epistemic status
definition  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
bayes_estimator, prob_beta, prob_binomial, prob_poisson

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A closure property of a prior family under Bayesian updating for a given likelihood. Every exponential family has a conjugate prior (the exp-family prior on the natural parameter with T-plus-count hyperparameters).

## Specialization / boundary cases
- Beta is conjugate to Bernoulli/binomial: Beta(a, b) + s successes in n => Beta(a + s, b + n - s)
- Gamma is conjugate to Poisson: Gamma(a, b) + counts summing to S in n obs => Gamma(a + S, b + n)
- Normal-inverse-Gamma is conjugate to the normal with unknown mean and variance
- Dirichlet is conjugate to the multinomial

## Hypothesis-dropped counterexamples
- **exists_and_is_flexible_enough**: conjugate priors can be too rigid -- e.g. the Beta cannot be bimodal, the Gamma cannot have a heavy left tail; a genuinely different prior belief forces non-conjugate computation (MCMC)

## Common misuse
- choosing a conjugate prior for computational convenience and then interpreting it as 'objective'
- reading the pseudo-count hyperparameters as data when reporting the effective sample size

## In the wild
- Latent Dirichlet Allocation (topic models): Dirichlet-multinomial conjugacy is what makes the collapsed Gibbs sampler tractable
- Thompson sampling for Bernoulli bandits uses the Beta-Bernoulli conjugate update per arm
- Bayesian A/B testing dashboards update Beta posteriors in closed form in real time

## Related nodes (non-prerequisite)
- uses: prob_beta, prob_binomial, bayes_estimator
- illustrated_by: exponential_family

## Sources
gelman_bda3, robert_bayesian_choice
