# jensen_inequality

## Type
theorem

## Statement
If phi is convex and X, phi(X) are integrable, then phi(E[X]) <= E[phi(X)]. If phi is strictly convex, equality holds iff X is a.s. constant.

## Symbols
- `phi` — a convex function, type: R -> R (or on an interval containing the range of X)
- `X` — an integrable random variable, type: L^1(P)

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
convex_function, expectation, expectation_linearity, expectation_monotonicity

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: supporting-line inequality phi(x) >= phi(c) + m(x - c) with c = E[X], then take expectations
derives_from: convex_function
lean_status: core — validation/proof-checks.lean Prob.jensen_sq (phi = square, GENUINE universal in t,x,y,n via the factorization t(n-t)(x-y)^2)

## Type / well-formedness check
take a supporting line L(x) = phi(E[X]) + m(x - E[X]) <= phi(x) at the point E[X]; then E[phi(X)] >= E[L(X)] = L(E[X]) = phi(E[X]) by linearity and monotonicity of expectation.

## Specialization / boundary cases
- phi(x) = x^2: E[X]^2 <= E[X^2], i.e. Var(X) >= 0
- phi(x) = |x|: |E[X]| <= E[|X|]
- phi(x) = e^x: e^{E[X]} <= E[e^X] (used in the Chernoff/entropy bounds)
- phi(x) = -log x on X > 0: log E[X] >= E[log X] (AM-GM in expectation form)

## Hypothesis-dropped counterexamples
- **convexity_of_phi**: phi concave (e.g. sqrt, log): the inequality REVERSES, phi(E[X]) >= E[phi(X)] -- applying Jensen the wrong way is the single most common error
- **integrability**: phi(x) = x^2 on a Cauchy X: E[phi(X)] = inf, the inequality is vacuous

## Common misuse
- wrong direction for a concave phi
- assuming strict inequality without strict convexity AND a non-degenerate X
- applying to phi convex only on part of the range of X

## In the wild
- information theory: Gibbs' inequality (KL divergence >= 0) IS Jensen applied to -log -- the source-coding theorem (the entropy bound behind every ZIP, PNG, FLAC) and channel capacity rest on it
- the EM algorithm: the E-step maximises a Jensen lower bound on the log-likelihood -- how Gaussian mixture models, HMMs for speech recognition, and LDA topic models are trained (Dempster-Laird-Rubin 1977; Neal-Hinton 1998)
- variational inference / the ELBO: the objective that trains variational autoencoders and Bayesian neural nets is a Jensen bound on log p(x) (Kingma-Welling 2013; Blei-Kucukelbir-McAuliffe 2017)
- finance: 'volatility drag', E[log(1+R)] <= log(1+E[R]), is why a volatile asset compounds slower than its arithmetic mean suggests; and concave utility => a risk-averse agent prefers the mean to the gamble, which is why insurance markets exist

## Related nodes (non-prerequisite)
- requires: convex_function
- generalizes: variance >= 0, the moment ladder, AM-GM
- conditional_version: conditional Jensen -- note on tower_property

## Sources
boucheron_lugosi_massart, durrett_pte
