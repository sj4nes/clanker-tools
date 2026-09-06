# probability_space

## Type
structure

## Statement
A probability space is a triple (Omega, F, P): a sample space Omega, an event sigma-algebra F, and a probability measure P on F.

## Symbols
- `Omega` — sample space, type: set
- `F` — events, type: sigma-algebra
- `P` — probability, type: F -> [0,1]

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
measurable_space, probability_measure

## Hypotheses
(none — unconditional within scope)

## Well-definedness
any (Omega, F) with any probability measure P is a probability space; the canonical one for a real random variable with law mu is (R, B(R), mu).

## Type / well-formedness check
the single object every probabilistic statement is implicitly relative to. Random variables are measurable maps out of it; independence and conditioning are properties of sub-sigma-algebras of F.

## Specialization / boundary cases
- ([0,1], B, lambda): supports a random variable of ANY law via the quantile transform (probability_integral_transform)
- (Omega, {empty, Omega}, P): only P(empty)=0, P(Omega)=1 -- no non-trivial events

## Hypothesis-dropped counterexamples
- **F_a_sigma_algebra**: if F is only an algebra, countable additivity has no content and the limit theorems (which are about countable families) cannot even be stated

## Common misuse
- changing Omega mid-argument without a coupling
- assuming a single Omega carries an uncountable family of independent variables without checking (it can, but needs a product construction)

## Related nodes (non-prerequisite)
- used_by: random_variable, stochastic_process

## Sources
billingsley_probability_measure, durrett_pte
