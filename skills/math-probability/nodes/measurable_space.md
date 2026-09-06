# measurable_space

## Type
structure

## Statement
A measurable space is a pair (Omega, F) where F is a sigma-algebra on Omega. Its members are the measurable sets (events).

## Symbols
- `Omega` — underlying set, type: set
- `F` — sigma-algebra, type: subset of 2^Omega

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
sigma_algebra

## Hypotheses
(none — unconditional within scope)

## Well-definedness
any set with any sigma-algebra on it is a measurable space; morphisms are measurable functions (preimage of measurable is measurable).

## Type / well-formedness check
no measure is attached yet; a measurable space is the domain on which measures and measurable functions are defined.

## Specialization / boundary cases
- (R, B(R)) is the canonical target for a real random variable
- (Omega, {empty, Omega}) -- the trivial sigma-algebra: only constants are measurable

## Common misuse
- conflating the measurable space with the probability space (which adds P)

## Related nodes (non-prerequisite)
- category: objects of Meas; morphisms are measurable maps

## Sources
billingsley_probability_measure, folland_real_analysis
