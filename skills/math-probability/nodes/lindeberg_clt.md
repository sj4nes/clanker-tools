# lindeberg_clt

## Type
theorem

## Statement
For each n let X_{n,1}, ..., X_{n,k_n} be independent, mean 0, with s_n^2 = sum_i Var(X_{n,i}). If the Lindeberg condition holds -- for every eps > 0, (1/s_n^2) sum_i E[X_{n,i}^2 1_{|X_{n,i}| > eps s_n}] -> 0 -- then (sum_i X_{n,i})/s_n -> N(0,1) in distribution.

## Symbols
- `X_{n,i}` — a triangular array of row-independent, mean-0 variables, type: array of L^2(P)
- `s_n^2` — the row variance sum, type: positive real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
central_limit_theorem, convergence_in_distribution, levy_continuity_theorem

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: CF expansion of prod_i phi_{X_{n,i}}(t/s_n); the Lindeberg condition controls the third-order remainder uniformly, giving -> e^{-t^2/2}; then Levy
derives_from: levy_continuity_theorem
lean_status: cited — Billingsley Thm 27.2; Durrett Thm 3.4.5

## Type / well-formedness check
the definitive CLT for NON-identically-distributed independent summands: the Lindeberg condition says no single term contributes a non-negligible fraction of the total variance. It implies (and under a uniform-asymptotic-negligibility assumption, is equivalent to) asymptotic normality; Lyapunov's (2 + delta)-moment condition is a convenient sufficient case.

## Specialization / boundary cases
- X_{n,i} iid mean 0 variance sigma^2: Lindeberg reduces to E[X_1^2 1_{|X_1| > eps sqrt n}] -> 0, true by DCT -- recovers the classical CLT
- Lyapunov: if (1/s_n^{2+delta}) sum E|X_{n,i}|^{2+delta} -> 0 for some delta > 0, then Lindeberg holds
- regression residuals, weighted sums with bounded weights, m-dependent sequences

## Hypothesis-dropped counterexamples
- **lindeberg_condition**: X_{n,1} ~ N(0, n), X_{n,2}, ..., X_{n,n} ~ iid N(0,1): s_n^2 = 2n - 1 but the first term carries ~half the variance; the normalized sum is NOT asymptotically normal (it stays a 50-50 mix). One dominant term breaks the CLT.
- **independence_within_rows**: strong dependence needs a different CLT (martingale CLT, mixing conditions)

## Common misuse
- applying the classical CLT to non-identical summands without checking a Lindeberg/Lyapunov condition
- ignoring a single heavy-weighted observation

## Related nodes (non-prerequisite)
- generalizes: central_limit_theorem
- sufficient_condition: Lyapunov
- uses: levy_continuity_theorem

## Sources
billingsley_probability_measure, durrett_pte
