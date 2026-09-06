# mgf_sum_independent

## Type
identity

## Statement
If X, Y are independent, then M_{X+Y}(t) = M_X(t) M_Y(t) (where the MGFs are finite), and phi_{X+Y}(t) = phi_X(t) phi_Y(t) always.

## Symbols
- `X, Y` — independent random variables, type: Omega -> R

## Epistemic status
mathematical_identity

## Prerequisites (tsort edges into this node)
characteristic_function, independence_expectation, independence_random_variables, mgf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[e^{t(X+Y)}] = E[e^{tX} e^{tY}] = E[e^{tX}] E[e^{tY}] by independence_expectation applied to g(X) = e^{tX}, h(Y) = e^{tY}
derives_from: independence_expectation
lean_status: core — validation/proof-checks.lean -- binomial MGF^n instance

## Type / well-formedness check
e^{t(X+Y)} = e^{tX} e^{tY} is a product of independent (functions of independent) variables, so its expectation factors by independence_expectation. Same for e^{it(X+Y)}.

## Specialization / boundary cases
- sum of n iid: M_{S_n} = M_X^n, phi_{S_n} = phi_X^n -- the engine of the CLT proof
- N(mu_1, s_1^2) + N(mu_2, s_2^2) independent = N(mu_1 + mu_2, s_1^2 + s_2^2), by exp adding in the exponent
- Poisson(lambda) + Poisson(mu) independent = Poisson(lambda + mu)

## Hypothesis-dropped counterexamples
- **independence**: X + X = 2X: phi_{2X}(t) = phi_X(2t) != phi_X(t)^2 in general -- the product rule is exactly the independence assumption
- **finiteness_for_the_MGF_version**: the CF version is unconditional; the MGF version needs both MGFs finite at t

## Common misuse
- multiplying CFs/MGFs of dependent variables
- using the MGF form when an MGF does not exist (use the CF)

## Related nodes (non-prerequisite)
- derives_from: independence_expectation
- used_by: central_limit_theorem, poisson_limit_theorem, normal_affine_closure

## Sources
billingsley_probability_measure, durrett_pte
