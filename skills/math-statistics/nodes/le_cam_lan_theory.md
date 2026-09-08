# le_cam_lan_theory

## Type
theorem

## Statement
Local asymptotic normality (LAN): for a regular parametric model, the log-likelihood ratio for local parameters theta_0 + h/sqrt(n) vs theta_0 admits the expansion log [ L(theta_0 + h/sqrt(n)) / L(theta_0) ] = h^T Delta_n - (1/2) h^T I(theta_0) h + o_{P_{theta_0}}(1), where Delta_n -> N(0, I(theta_0)). The local experiments converge to a single Gaussian shift experiment N(h, I(theta_0)^{-1}).

## Symbols
- `h` — the local parameter (a direction and magnitude of a 1/sqrt(n) perturbation)
- `Delta_n = (1/sqrt n) sum score(X_i; theta_0)` — the normalized score, the LAN 'central sequence'
- `the limit experiment` — observing one draw from N(h, I(theta_0)^{-1}) -- everything asymptotic reduces to this

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
information_equality, mle_asymptotic_normality, prob_characteristic_function, prob_clt, prob_levy_continuity

## Hypotheses
log_likelihood_smooth, fisher_information_positive_definite, true_parameter_interior

## Proof provenance
technique: Taylor / differentiability-in-quadratic-mean expansion of the log-likelihood ratio; the cross term is the central sequence, converging by the CLT
derives_from: mle_asymptotic_normality
lean_status: cited — CITED -- Le Cam 1960; van der Vaart Asymptotic Statistics Ch. 7-9. Not formalized.

## Type / well-formedness check
The organizing theorem of modern asymptotic statistics (Le Cam). It says all regular parametric models look locally like a Gaussian location problem, so optimality questions (efficient estimation, most powerful testing) are answered ONCE, in the Gaussian shift experiment, and transferred back. Boundary node: stated, cited.

## Specialization / boundary cases
- MLE asymptotic normality, Wilks' theorem, and the asymptotic equivalence of the Wald/score/LR tests are all corollaries of LAN + properties of the Gaussian shift experiment
- contiguity (Le Cam's lemmas) lets you compute limiting power under alternatives from behaviour under the null
- semiparametric efficiency theory (LAN with an infinite-dimensional nuisance) generalizes it

## Hypothesis-dropped counterexamples
- **regular_model**: non-LAN models: uniform(0, theta) is locally asymptotically EXPONENTIAL (LAE, rate n); some models are locally asymptotically MIXED normal (LAMN, e.g. explosive AR, some diffusions). The Gaussian-shift reduction and its optimality conclusions do not apply.
- **fixed_dimension**: increasing-dimension / nonparametric models need the infinite-dimensional LAN theory and have their own (slower) efficiency bounds

## Common misuse
- applying LAN-based efficiency claims to a non-regular model (unit-root tests are the classic cautionary tale -- the limit is not normal)
- assuming local (h/sqrt n) optimality implies good behaviour against fixed alternatives

## Related nodes (non-prerequisite)
- uses: information_equality, prob_clt, mle_asymptotic_normality
- required_by: hajek_convolution_theorem, local_asymptotic_minimax

## Sources
le_cam_asymptotic_methods, van_der_vaart_asymptotic
