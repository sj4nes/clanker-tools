# glivenko_cantelli

## Type
theorem

## Statement
The empirical CDF converges uniformly to the true CDF almost surely: sup_x | F_hat_n(x) - F(x) | -> 0 a.s. as n -> inf, for EVERY distribution F. (The 'fundamental theorem of statistics'.)

## Symbols
- `the sup over all x` — uniform, not merely pointwise, convergence -- this is the strengthening over the pointwise SLLN

## Epistemic status
proved_theorem  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, prob_conv_as, prob_slln

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: pointwise SLLN at finitely many quantiles + monotonicity sandwiching to control the sup between them; refine the partition
derives_from: prob_slln
lean_status: cited — CITED -- Glivenko 1933, Cantelli 1933; van der Vaart Thm 19.1. The monotonicity-sandwich reduction to finitely many pointwise SLLNs is the elementary content.

## Type / well-formedness check
An almost-sure uniform-convergence statement, distribution-free. Proof: pointwise SLLN at a fixed grid of quantile levels, monotonicity of F and F_hat_n to fill in between grid points, then let the grid refine. It is the archetype of a 'uniform law of large numbers' over a class of sets (here, half-lines).

## Specialization / boundary cases
- justifies the plug-in principle: T(F_hat_n) -> T(F) for any sup-norm-continuous functional T
- the basis of the bootstrap's first-order validity (resampling from F_hat_n approximates resampling from F)
- generalizes to VC classes (Vapnik-Chervonenkis): uniform convergence over any class of sets with finite VC dimension -- the foundation of statistical learning theory

## Hypothesis-dropped counterexamples
- **iid**: for dependent data (a time series) F_hat_n still converges pointwise under ergodicity but the uniform / rate results need mixing conditions
- **the_class_is_not_too_rich**: uniform convergence FAILS over an arbitrary class of sets -- e.g. over all finite sets, sup |P_hat_n(A) - P(A)| = 1 always (A = the sample). Half-lines (VC dim 1) are simple enough; this is why VC dimension matters.

## Common misuse
- invoking 'Glivenko-Cantelli' to claim uniform convergence of the empirical measure over a class richer than a Donsker/VC class
- assuming it gives a RATE -- it is a qualitative a.s. statement; DKW gives the rate

## In the wild
- the theoretical license for the entire bootstrap and for empirical risk minimization in machine learning (uniform convergence of training error to test error over the hypothesis class)
- M-estimation consistency proofs (uniform LLN for the criterion function) are Glivenko-Cantelli over a function class

## Related nodes (non-prerequisite)
- required_by: bootstrap_consistency, donsker_theorem
- strengthened_by: dvoretzky_kiefer_wolfowitz, donsker_theorem
- uses: empirical_cdf, prob_slln

## Sources
glivenko_1933, van_der_vaart_asymptotic, vapnik_statistical_learning_theory
