# hoeffding_inequality

## Type
theorem

## Statement
If X_1, ..., X_n are independent with a_i <= X_i <= b_i a.s., and S = sum X_i, then for s > 0: P(S - E[S] >= s) <= exp(-2 s^2 / sum_i (b_i - a_i)^2), and the two-sided bound doubles the right side.

## Symbols
- `X_i` — independent bounded random variables, type: Omega -> [a_i, b_i]
- `s` — the deviation, type: positive real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
chernoff_bound, hoeffding_lemma, independence_random_variables, mgf_sum_independent

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Chernoff + mgf_sum_independent + hoeffding_lemma per factor, then optimize over t
derives_from: hoeffding_lemma
lean_status: core — validation/proof-checks.lean Prob.markov_finite (Markov/Chernoff core); the assembly is algebra

## Type / well-formedness check
Chernoff on S - E[S]: P(S - E[S] >= s) <= e^{-ts} prod_i E[e^{t(X_i - E X_i)}] <= e^{-ts} exp(t^2 sum (b_i - a_i)^2 / 8) by independence (MGFs multiply) and Hoeffding's lemma; optimize t = 4s / sum (b_i - a_i)^2.

## Specialization / boundary cases
- X_i in [0, 1], sample mean Xbar: P(Xbar - E[Xbar] >= eps) <= e^{-2 n eps^2} -- the workhorse bound for empirical means, bandit algorithms, and PAC learning
- n coin flips: P(#heads - n/2 >= s) <= e^{-2 s^2 / n}
- gives the sample size n >= (1/(2 eps^2)) log(2/delta) for an eps-accurate mean with confidence 1 - delta

## Hypothesis-dropped counterexamples
- **boundedness_of_each_X_i**: one unbounded X_i (even with tiny variance) breaks the sub-Gaussian MGF bound -- use Bernstein's inequality (needs a variance bound + a one-sided bound) instead
- **independence**: for dependent X_i the MGF does not factor; McDiarmid's / Azuma's inequality handles bounded-difference dependence

## Common misuse
- applying it to unbounded variables
- using it for dependent data
- forgetting the factor 2 in the two-sided version
- ignoring that it can be very loose when the variances are much smaller than the ranges (Bernstein is tighter then)

## In the wild
- statistical learning theory / PAC learning (Valiant 1984, Turing Award 2010): a union bound over a finite hypothesis class H plus Hoeffding per hypothesis gives generalisation gap <= sqrt(ln(|H|/delta) / (2n)) with probability 1 - delta -- the founding guarantee of ML
- the UCB1 multi-armed bandit (Auer-Cesa-Bianchi-Fischer 2002): the exploration bonus sqrt(2 ln t / n_i) added to each arm's empirical mean is a Hoeffding confidence radius -- deployed for ad selection and Yahoo front-page news recommendation (LinUCB, Li et al. 2010), adaptive clinical trials
- Monte Carlo Tree Search / UCT (Kocsis-Szepesvari 2006): the same confidence bound is the tree-search selection rule -- the exploration mechanism inside AlphaGo
- Hoeffding trees / VFDT (Domingos-Hulten 2000): a streaming decision tree splits a node once a Hoeffding bound certifies the best-looking attribute really is best -- real-time data-stream mining
- differential privacy: the accuracy of a private mechanism (RAPPOR at Google, Apple's iOS telemetry, the 2020 US Census) is stated as a Hoeffding/Chernoff-type bound on the noise

## Related nodes (non-prerequisite)
- derives_from: hoeffding_lemma, chernoff_bound
- sharpens: chebyshev_inequality
- relatives: Bernstein, Azuma-Hoeffding, McDiarmid

## Sources
boucheron_lugosi_massart, durrett_pte
