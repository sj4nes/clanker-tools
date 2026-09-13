# dependence_lemma

## Type
lemma

## Statement
If (v_1,...,v_k) is dependent and v_1 != 0, then there is a j >= 2 with v_j in span(v_1,...,v_{j-1}), and removing that v_j does not change the span.

## Symbols
- `j` — the index of the first redundant vector, type: element of {2,...,k}

## Epistemic status
proved_lemma  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_independence, span

## Hypotheses
the list is dependent, v_1 != 0, the list is finite

## Proof provenance
technique: take a nontrivial vanishing combination, let j be the largest index with a_j != 0; j >= 2 since v_1 != 0; solve for v_j using a_j^{-1}
derives_from: linear_independence
lean_status: cited

## Type / well-formedness check
Well-formed. The ordering matters: the lemma identifies the FIRST redundant vector in the given order, which is what makes it usable as an induction step.

## Specialization / boundary cases
- k = 2: if v_2 = c v_1 then removing v_2 leaves the span unchanged

## Hypothesis-dropped counterexamples
- **v_1_not_zero**: if v_1 = 0 the list is dependent but no LATER vector need be redundant -- (0, e_1) is dependent, yet removing e_1 changes the span. The conclusion must then be about removing v_1 itself
- **invertibility_of_a_j**: solving for v_j divides by a_j, which needs F to be a field; over Z this step fails and is the origin of the module-theoretic complications in smith_normal_form_boundary

## Common misuse
- concluding the LAST vector is always the removable one -- the lemma names the largest index with a nonzero coefficient, which depends on the relation chosen

## Related nodes (non-prerequisite)
- required_by: steinitz_exchange, basis_existence_finite

## Sources
axler_lada_4e
