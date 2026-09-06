# stochastic_process

## Type
bridge

## Statement
A stochastic process is a collection (X_t)_{t in T} of random variables on one probability space, indexed by a set T (time). Its law lives on the product space R^T via the finite-dimensional distributions. STATED as a boundary node.

## Symbols
- `(X_t)` — the process, type: T -> (Omega -> R)
- `T` — the index set (e.g. N, [0, inf)), type: set

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
probability_space, random_variable

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: definition only; existence from consistent finite-dimensional distributions is kolmogorov_extension_theorem; path regularity (continuity, cadlag) requires the Kolmogorov-Chentsov criterion -- all deferred
derives_from: random_variable
lean_status: cited — Billingsley SS36; Durrett ch. 6-8; Karatzas-Shreve ch. 1-2

## Type / well-formedness check
for fixed omega, t |-> X_t(omega) is a sample path; for fixed t, X_t is a random variable. The finite-dimensional distributions (laws of (X_{t_1}, ..., X_{t_k})) are the observable data; Kolmogorov's extension theorem builds the process from consistent f.d.d.s.

## Specialization / boundary cases
- T = N: a discrete-time sequence (e.g. a Markov chain, a time series)
- T = [0, inf), continuous paths: Brownian motion, diffusions
- T = [0, inf), piecewise-constant paths: the Poisson process, continuous-time Markov chains

## Hypothesis-dropped counterexamples
- **one_common_probability_space**: a process is more than its marginals -- the joint law across times (the dependence) is the object of interest
- **path_regularity_is_extra**: the f.d.d.s do not determine path properties; { X_t continuous } may not even be measurable without choosing a good modification

## Common misuse
- confusing the process with its one-dimensional marginals
- assuming a version with continuous (or measurable) paths exists without a regularity criterion

## Related nodes (non-prerequisite)
- constructed_by: kolmogorov_extension_theorem
- special_cases: martingale, Markov chain, Poisson process, Brownian motion
- developed_in: a future stochastic-processes capsule

## Sources
billingsley_probability_measure, durrett_pte
