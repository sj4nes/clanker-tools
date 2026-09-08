# null_hypothesis

## Type
definition

## Statement
The null hypothesis H0: theta in Theta_0 is the statement about theta put on trial; it is retained unless the data provide strong evidence against it. Theta_0 subset Theta.

## Symbols
- `Theta_0` — the null parameter set (a point for a 'simple' null, a set for a 'composite' null)
- `'on trial'` — the asymmetry -- Type I error (wrongly rejecting H0) is controlled, Type II is not

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
parameter_space

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A subset of Theta, chosen before seeing the data. The test controls the probability of rejecting H0 when it is true; it does NOT control the probability of accepting a false H0. 'Fail to reject' is not 'accept'.

## Specialization / boundary cases
- simple: H0: mu = 0 (Theta_0 a single point)
- composite one-sided: H0: mu <= 0
- composite with nuisance: H0: mu = 0, sigma^2 > 0 arbitrary

## Hypothesis-dropped counterexamples
- **specified_in_advance**: choosing Theta_0 after seeing the data (testing the hypothesis the data suggest) invalidates the Type I error control -- 'the garden of forking paths'

## Common misuse
- interpreting 'fail to reject H0' as 'H0 is true' -- it may just be low power
- testing a point null (mu exactly 0) that is known a priori to be false, then declaring 'significance' at large n as if it were news

## Related nodes (non-prerequisite)
- required_by: alternative_hypothesis, test_function, size_of_test, neyman_pearson_lemma

## Sources
lehmann_romano_tsh, casella_berger_2e
