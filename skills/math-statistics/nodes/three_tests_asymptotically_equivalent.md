# three_tests_asymptotically_equivalent

## Type
theorem

## Statement
Under H0 and local alternatives theta_n = theta_0 + h/sqrt(n), the Wald, score, and likelihood-ratio statistics differ by o_p(1) and share the same limiting (noncentral) chi^2_{d-r} distribution; asymptotically the three tests have identical size and power.

## Symbols
- `o_p(1)` — converges to 0 in probability
- `local alternatives h/sqrt(n)` — the regime where power is non-degenerate (between alpha and 1)

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
prob_continuous_mapping, score_test, wald_test, wilks_theorem

## Hypotheses
true_parameter_interior, fisher_information_positive_definite, log_likelihood_smooth

## Proof provenance
technique: Taylor-expand each statistic around theta_0; the leading quadratic term is common; the differences are O_p(1/sqrt n) under H0 and local alternatives
derives_from: wilks_theorem
lean_status: cited — CITED -- Engle 1984 (Handbook of Econometrics Ch. 13); van der Vaart Ch. 16. The shared quadratic form is the content.

## Type / well-formedness check
An asymptotic-equivalence statement. All three are, to first order, the same quadratic form in the asymptotically-normal score; they differ only in whether the information is evaluated at theta_hat (Wald), theta_0 (score), or effectively averaged (LRT), and in second-order terms.

## Specialization / boundary cases
- scalar linear-normal case: all three reduce EXACTLY (not just asymptotically) to the t^2 / F statistic
- for a proportion: Wald uses p_hat(1-p_hat), score uses p_0(1-p_0) -- the score (Wilson) test/interval has far better small-sample coverage though they agree in the limit
- ordering in finite samples is problem-dependent, but often -2 log Lambda is between W and S

## Hypothesis-dropped counterexamples
- **regularity_all_three**: at a boundary or in a non-regular model the three can have DIFFERENT (non-chi^2) limits and are no longer equivalent
- **far_from_local**: against a FIXED (non-local) alternative all three have power -> 1 but at different rates; 'equivalent' is a local statement

## Common misuse
- citing the equivalence to justify using the most convenient test (Wald) at a small n where they visibly disagree -- pick the one with the best finite-sample properties (usually score or LRT)
- assuming equal power against a fixed large alternative

## Related nodes (non-prerequisite)
- uses: wald_test, score_test, wilks_theorem

## Sources
engle_1984, van_der_vaart_asymptotic
