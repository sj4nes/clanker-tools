# geometric_distribution

## Type
definition

## Statement
X ~ Geometric(p): the trial index of the first success in iid Bernoulli(p) trials. P(X = k) = (1-p)^{k-1} p for k = 1, 2, .... E[X] = 1/p, Var(X) = (1-p)/p^2. Memoryless.

## Symbols
- `X` — the first-success index, type: Omega -> {1,2,...}
- `p` — success probability, type: real in (0,1]

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, memorylessness, pmf, variance

## Hypotheses
(none — unconditional within scope)

## Well-definedness
sum_{k>=1} (1-p)^{k-1} p = p / (1 - (1-p)) = 1 (geometric series); needs p > 0.

## Type / well-formedness check
the unique memoryless distribution on the positive integers: P(X > m + k | X > m) = P(X > k). (Convention varies: some define X as the number of FAILURES before the first success, support {0,1,2,...}, E = (1-p)/p.)

## Specialization / boundary cases
- p = 1: X = 1 a.s.
- P(X > k) = (1-p)^k -- a clean survival function
- min of independent geometrics with rates p_i is geometric with rate 1 - prod(1 - p_i)

## Hypothesis-dropped counterexamples
- **memorylessness_pins_it_down**: any non-geometric law on {1,2,...} fails P(X > m+k | X > m) = P(X > k) for some m, k
- **p_gt_0**: p = 0 gives no success ever -- X = inf, not a proper random variable

## Common misuse
- mixing the two conventions (first-trial index vs failure count) -- they differ by 1 in mean
- assuming the memoryless property for a non-geometric discrete law

## Related nodes (non-prerequisite)
- continuous_analogue: exponential_distribution
- characterized_by: memorylessness
- sum_of_r_iid: negative binomial

## Sources
grimmett_stirzaker, durrett_pte
