# alternative_hypothesis

## Type
definition

## Statement
The alternative hypothesis H1: theta in Theta_1 is the set of parameter values the test is designed to detect; usually Theta_1 = Theta \ Theta_0.

## Symbols
- `Theta_1` — the alternative set -- one-sided (mu > 0) or two-sided (mu != 0)
- `the direction of H1` — determines whether a one- or two-tailed test is used

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
null_hypothesis, parameter_space

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A subset of Theta disjoint from (the closure of) Theta_0. The alternative is where POWER is measured; the choice of one- vs two-sided must be made before seeing the data.

## Specialization / boundary cases
- two-sided: H1: mu != 0 -- detect an effect in either direction
- one-sided: H1: mu > 0 -- more powerful against positive effects, blind to negative ones
- restricted: H1: theta in a cone (order-restricted alternatives)

## Hypothesis-dropped counterexamples
- **chosen_in_advance**: switching from two-sided to one-sided after seeing a positive Xbar doubles the effective alpha

## Common misuse
- choosing a one-sided alternative post hoc to cross the 0.05 threshold
- a one-sided test that would not reject even for an enormous effect in the unanticipated direction

## Related nodes (non-prerequisite)
- uses: null_hypothesis
- required_by: power_function

## Sources
lehmann_romano_tsh
