# convergence_in_distribution

## Type
definition

## Statement
X_n -> X in distribution if F_{X_n}(x) -> F_X(x) at every x where F_X is continuous. Equivalently E[g(X_n)] -> E[g(X)] for every bounded continuous g (portmanteau).

## Symbols
- `(X_n)` — a sequence of random variables on one probability space, type: N -> (Omega -> R)
- `X` — the limit random variable (or law), type: Omega -> R (or a law)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
cdf, cdf_properties, sequence_limit

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
the WEAKEST mode: it is a statement about the LAWS, not the random variables, so X_n and X need not live on the same space. The 'continuity point' clause is essential -- CDFs can converge everywhere except at jumps of the limit.

## Specialization / boundary cases
- the CLT delivers this mode: standardized sample mean -> N(0,1) in distribution
- equivalent forms (portmanteau_theorem): E[g(X_n)] -> E[g(X)] for bounded continuous g; limsup P(X_n in C) <= P(X in C) for closed C; phi_{X_n}(t) -> phi_X(t) for all t (Levy)

## Hypothesis-dropped counterexamples
- **continuity_points_only**: X_n = 1/n (constant): F_{X_n} is a step at 1/n, F_X a step at 0; F_{X_n}(0) = 0 for all n but F_X(0) = 1 -- convergence fails AT the jump but X_n -> 0 in distribution is still true

## Common misuse
- expecting F_{X_n}(x) -> F_X(x) at jump points of F_X
- concluding X_n -> X in probability (only true when X is a constant)
- reading 'X_n -> X in distribution' as any statement about X_n(omega)

## In the wild
- every asymptotic confidence interval and hypothesis test in classical statistics is a convergence-in-distribution statement about a test statistic (t, Wald, likelihood-ratio, score) -- FDA drug trials, econometrics, quality control, A/B testing
- the continuous-mapping and Slutsky theorems that make this mode composable are the daily tools for deriving the asymptotic distribution of an estimator (van der Vaart 1998)

## Related nodes (non-prerequisite)
- implied_by: convergence_in_probability
- characterized_by: portmanteau_theorem, levy_continuity_theorem
- delivered_by: central_limit_theorem
- tag: d

## Sources
durrett_pte, billingsley_probability_measure
