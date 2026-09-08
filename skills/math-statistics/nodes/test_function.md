# test_function

## Type
definition

## Statement
A test is a function phi: X^n -> [0, 1] giving the probability of rejecting H0 when the data are x; a nonrandomized test takes values in {0, 1} with rejection region { x : phi(x) = 1 }.

## Symbols
- `phi(x) = 1` — reject
- `phi(x) = 0` — do not reject
- `phi(x) in (0,1)` — reject with that probability (randomized -- needed for exact size on discrete data)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
null_hypothesis, statistic

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A [0,1]-valued statistic. Randomization matters only for discrete data where no nonrandomized region has exactly the target size; in practice one reports the p-value instead.

## Specialization / boundary cases
- phi(x) = 1{ T(x) > c } -- reject for large values of a test statistic T
- two-sided: phi(x) = 1{ |T(x)| > c }
- randomized: phi(x) = gamma when T(x) = c, to hit an exact size on a lattice

## Hypothesis-dropped counterexamples
- **measurable**: a non-measurable rejection region has no size -- excluded

## Common misuse
- treating a randomized test's coin flip as scientifically meaningful (report the p-value)
- choosing the rejection region's shape to reject the observed data

## Related nodes (non-prerequisite)
- specializes_from: statistic
- required_by: size_of_test, power_function, neyman_pearson_lemma
- dual_of: confidence_set

## Sources
lehmann_romano_tsh, casella_berger_2e
