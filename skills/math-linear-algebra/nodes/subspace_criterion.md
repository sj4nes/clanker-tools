# subspace_criterion

## Type
proposition

## Statement
A nonempty subset U of V is a subspace if and only if au + bw is in U for all a, b in F and all u, w in U.

## Symbols
- `a, b` — arbitrary scalars
- `u, w` — arbitrary elements of U

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
subspace

## Hypotheses
U nonempty

## Proof provenance
technique: forward by applying the two closures in turn; backward by specialising (a,b) to (1,1) and (a,0)
derives_from: subspace
lean_status: cited

## Type / well-formedness check
Well-formed. The single condition packages both closures; nonemptiness then supplies 0 by taking a = b = 0.

## Specialization / boundary cases
- a = b = 0 recovers 0 in U; b = 0 recovers closure under scalars; a = b = 1 recovers closure under addition

## Hypothesis-dropped counterexamples
- **nonemptiness**: the empty set satisfies the quantified condition vacuously; without nonemptiness the criterion would wrongly certify it as a subspace

## Common misuse
- checking only a = b = 1 (closure under addition) and concluding subspace -- see the quadrant counterexample on subspace

## Sources
axler_lada_4e
