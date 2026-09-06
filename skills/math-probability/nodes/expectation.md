# expectation

## Type
definition

## Statement
The expectation of a random variable X is E[X] = integral_Omega X dP. It is defined (finite) when E[|X|] < inf, and in [0, inf] unconditionally when X >= 0.

## Symbols
- `X` — a random variable, type: Omega -> R
- `E[X]` — its mean, type: real or +-inf or undefined

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
abstract_integral, probability_measure, random_variable

## Hypotheses
(none — unconditional within scope)

## Well-definedness
for X >= 0, integral X dP in [0, inf] always exists (sup over simple functions); for signed X, E[X] = E[X^+] - E[X^-] provided not both are +inf. X integrable <=> X in L^1(P).

## Type / well-formedness check
E[X] is the Lebesgue integral of X against P; all its properties (linearity, monotonicity, MCT/DCT/Fatou) are the integral's, specialised. E[X] may FAIL to exist (Cauchy: E[X^+] = E[X^-] = inf).

## Specialization / boundary cases
- X = 1_A: E[X] = P(A)
- X discrete: E[X] = sum_x x p_X(x)
- X with density: E[X] = integral x f_X(x) dx
- X = c: E[X] = c

## Hypothesis-dropped counterexamples
- **integrability_E_abs_X_finite**: X ~ Cauchy: E[|X|] = (2/pi) integral_0^inf x/(1+x^2) dx = inf, so E[X] does not exist -- neither the LLN nor the CLT apply

## Common misuse
- assuming E[X] always exists
- writing E[X] for a variable whose positive and negative parts both have infinite integral
- confusing E[X] (a number) with X (a function)

## Related nodes (non-prerequisite)
- specializes: abstract_integral
- used_by: variance, lotus, markov_inequality

## Sources
billingsley_probability_measure, durrett_pte
