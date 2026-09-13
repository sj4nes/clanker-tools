# vector_space

## Type
structure

## Statement
A vector space over F is an abelian group (V, +, 0) together with a scalar multiplication F x V -> V satisfying a(bv) = (ab)v, 1v = v, a(u+v) = au + av, and (a+b)v = av + bv.

## Symbols
- `V` — the vector space, type: set with + and scalar multiplication
- `F` — the scalar field
- `v, u` — vectors, type: elements of V
- `a, b` — scalars, type: elements of F
- `0` — the zero VECTOR (distinct from the zero SCALAR)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
field, set

## Hypotheses
F is a field
## Type / well-formedness check
Well-formed: + has type V x V -> V and scalar multiplication F x V -> V, so every expression above type-checks. The overloading of 0 (scalar and vector) and of + (in F and in V) is resolved by position.

## Specialization / boundary cases
- V = F^n with componentwise operations -- the model for the whole capsule
- V = F itself, a one-dimensional space over F
- V = {0}, the zero space: a legitimate vector space with the empty basis and dimension 0
- V = F[t], or the set of functions X -> F -- infinite-dimensional instances showing the axioms alone do not give finiteness

## Hypothesis-dropped counterexamples
- **the_axiom_1v_equals_v**: without it, the map a*v := 0 for all a satisfies every other axiom on any abelian group, making scalar multiplication trivial. It is the axiom that ties the field action to the group and is the one most often omitted from informal lists
- **F_being_a_field**: over a ring the structure is a MODULE: Z/6 as a Z-module has torsion, no basis, and no well-defined dimension

## Common misuse
- assuming an inner product, a norm, or coordinates: none is part of the definition. A bare vector space has no notion of length, angle, or preferred basis
- assuming finite-dimensionality (see finite_dimensional)

## In the wild
- the ambient structure for every linear model in statistics, every state space in control theory, and every feature space in machine learning
- solution sets of homogeneous linear ODEs are vector spaces, which is why superposition works

## Related nodes (non-prerequisite)
- required_by: subspace, linear_map, inner_product

## Sources
axler_lada_4e, hoffman_kunze_2e
