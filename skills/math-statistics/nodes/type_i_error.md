# type_i_error

## Type
definition

## Statement
A Type I error is rejecting H0 when it is true (probability <= the size alpha); a Type II error is failing to reject H0 when it is false (probability 1 - power at that alternative).

## Symbols
- `alpha` — the tolerated Type I rate
- `1 - beta_phi(theta_1)` — the Type II rate at alternative theta_1

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
power_function, size_of_test

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
The two error kinds, treated asymmetrically: alpha is fixed by convention (0.05, 0.01, 5 sigma), power is then maximized. Which error is 'Type I' depends on which hypothesis is labelled the null -- a modelling choice reflecting which mistake is worse.

## Specialization / boundary cases
- drug trial: Type I = approve an ineffective drug (H0: no effect); Type II = miss an effective one
- the trade-off at fixed n: lowering alpha raises the Type II rate; only increasing n lowers both
- 5-sigma in particle physics: alpha ~ 3e-7, an extremely low Type I tolerance

## Hypothesis-dropped counterexamples
- **H0_is_the_costlier_false_positive**: if the roles are mislabelled, the procedure rigidly protects the wrong error -- e.g. an equivalence trial must put 'the treatments differ' style framing correctly (H0: not equivalent)

## Common misuse
- treating a non-significant result as proof of H0 (ignoring the uncontrolled Type II rate)
- running many tests and reporting the significant ones without multiplicity adjustment -- the family-wise Type I rate balloons

## Related nodes (non-prerequisite)
- uses: size_of_test, power_function

## Sources
lehmann_romano_tsh, neyman_pearson_1933
