# preimage_algebra

## Type
primitive

## Statement
For any function f, the preimage operator f^{-1} on sets commutes with arbitrary union, arbitrary intersection, and complement: f^{-1}(bigcup B_i) = bigcup f^{-1}(B_i), etc.

## Symbols
- `f` — any function X -> Y, type: function
- `B_i` — subsets of the codomain Y, type: element of 2^Y

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
(root)

## Hypotheses
(none — unconditional within scope)

## Well-definedness
f^{-1}(B) := { x : f(x) in B } is defined for every f and every B; the three commutation identities are immediate from the definition of membership.

## Type / well-formedness check
f^{-1} here is the preimage OPERATOR ON SETS, defined for every f (not an inverse function). It is a Boolean-algebra homomorphism 2^Y -> 2^X; the forward image is only a join-homomorphism.

## Specialization / boundary cases
- f measurable iff f^{-1}(generating sets) are all measurable -- this is why the preimage algebra, not the image, drives measurability
- image only satisfies f[A cap B] subset f[A] cap f[B], with equality iff f injective

## Common misuse
- expecting the forward image to commute with intersection or complement

## Related nodes (non-prerequisite)
- developed_in: math-sets-functions-cardinality
- contrast_with: image (weaker laws)

## Sources
enderton_set_theory, folland_real_analysis
