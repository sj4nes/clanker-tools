# strong_law_large_numbers

## Type
theorem

## Statement
If X_1, X_2, ... are iid with E|X_1| < inf and mean mu, then Xbar_n -> mu ALMOST SURELY. If E|X_1| = inf, then limsup |Xbar_n| = inf a.s.

## Symbols
- `X_i` — an iid sequence, type: N -> L^1(P)
- `mu` — the common mean, type: real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
borel_cantelli_first, convergence_almost_sure, expectation, iid, moment, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Etemadi: reduce to X_i >= 0 by splitting into positive/negative parts; truncate Y_i = X_i 1_{X_i <= i}; show sum Var(Y_i)/i^2 < inf so Xbar along a geometric subsequence n_k ~ alpha^k converges a.s. (Chebyshev + Borel-Cantelli 1); fill gaps by monotonicity; let alpha -> 1
derives_from: borel_cantelli_first
lean_status: cited — Durrett Thm 2.4.1 (Etemadi); Williams 12.10 (martingale proof)

## Type / well-formedness check
convergence mode: ALMOST SURELY -- strictly stronger than the WLLN. A finite mean is necessary AND sufficient. Etemadi's proof needs only pairwise independence and uses truncation + a fourth-moment-free Borel-Cantelli argument (choice-free).

## Specialization / boundary cases
- X_i ~ Bernoulli(p): the relative frequency -> p for almost every infinite sequence of trials (Borel's normal number theorem is the p = 1/2, base-2 case)
- the empirical CDF F_n(x) -> F(x) a.s. for each x (and uniformly -- Glivenko-Cantelli)
- renewal theory: N(t)/t -> 1/E[interarrival] a.s.

## Hypothesis-dropped counterexamples
- **finite_mean**: X_i ~ Cauchy or any law with E|X_1| = inf: limsup |Xbar_n| = inf a.s. -- the sample mean has no a.s. limit and in fact oscillates unboundedly
- **identically_distributed**: Kolmogorov's SLLN for independent non-identical X_i needs sum Var(X_i)/i^2 < inf

## Common misuse
- assuming a rate of a.s. convergence (the law of the iterated logarithm gives the a.s. envelope +- sqrt(2 sigma^2 n log log n))
- believing the SLLN needs a finite variance (it does not -- only a finite mean)
- the gambler's fallacy again

## Related nodes (non-prerequisite)
- strengthens: weak_law_large_numbers
- uses: borel_cantelli_first
- refined_by: law of the iterated logarithm
- tag: a.s.

## Sources
durrett_pte, williams_probability_martingales
