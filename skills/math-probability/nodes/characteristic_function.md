# characteristic_function

## Type
definition

## Statement
The characteristic function of X is phi_X(t) = E[e^{i t X}] = E[cos tX] + i E[sin tX]. It exists for EVERY random variable and every real t, with |phi_X(t)| <= 1 and phi_X(0) = 1.

## Symbols
- `phi_X` — the characteristic function, type: R -> C, |phi_X| <= 1
- `t` — a real parameter, type: real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, lotus, real_field

## Hypotheses
(none — unconditional within scope)

## Well-definedness
|e^{itX}| = 1 so e^{itX} is bounded, hence integrable against the probability measure P; phi_X is defined for all t.

## Type / well-formedness check
the Fourier transform of the law P_X. Unlike the MGF it always exists because |e^{itX}| = 1 is bounded. It determines the law (inversion), is uniformly continuous, and turns sums of independents into products.

## Specialization / boundary cases
- N(0,1): phi(t) = e^{-t^2/2}
- Cauchy: phi(t) = e^{-|t|} (exists! even though no moments do)
- X = c: phi(t) = e^{itc}
- Bernoulli(p): phi(t) = 1 - p + p e^{it}

## Hypothesis-dropped counterexamples
- **none_always_defined**: the CF is the tool precisely because it needs no hypothesis -- every law has one

## Common misuse
- expecting phi to be real (it is real iff the law is symmetric about 0)
- reading phi_X'(0) as E[X] without E|X| < inf (the derivative may fail to exist)

## Related nodes (non-prerequisite)
- always_exists_unlike: mgf
- determines: the law (cf_properties)
- used_by: levy_continuity_theorem, central_limit_theorem

## Sources
billingsley_probability_measure, durrett_pte
