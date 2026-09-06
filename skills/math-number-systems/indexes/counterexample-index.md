# Counterexample index (generated from results/*.yaml)

`dropped hypothesis`  ->  `witnessing counterexample`  (from which result)

- **cantor_diagonal_argument** — reals_not_rationals: 'the diagonal of a list of RATIONALS need not be rational, so this shows R (not Q) is uncountable -- consistent, since Q IS countable'
- **countable_union_countable** — countable_choice: 'consistent with ZF that R is a countable union of countable sets -- so the theorem genuinely needs CC'
- **countable_union_countable** — index_set_countable: 'an uncountable union of singletons (each countable) can be uncountable -- e.g. R = union of {x}'
- **dedekind_cut** — proper_subset: 'A = Q or A = {} are not cuts; they would be "+inf" and "-inf"'
- **dedekind_cut** — downward_closed: '{ 0, 2 } is not a cut -- a real is determined by ALL rationals below it'
- **dedekind_cut** — no_greatest_element: '{ p : p <= q } (closed) and { p : p < q } (open) would then be two different cuts for the same q -- the "no greatest" clause makes the rational embedding injective'
- **integer** — relation_is_transitive: 'a non-transitive relation does not partition N x N; "the set of classes" is ill-defined'
- **nth_root_exists** — x_positive: 'x = -1, n = 2 has no real square root -- roots of negatives live in C, out of scope'
- **nth_root_exists** — ambient_field_complete: 'in Q, sqrt(2) does not exist -- this theorem is a direct payoff of lub_property'
- **peano_axioms** — zero_not_a_successor: 'a finite cycle { 0, 1, ..., k-1 } with S = +1 mod k has 0 = S(k-1); induction from 0 covers everything but recursion over-constrains f(0)'
- **peano_axioms** — induction: 'N disjoint-union an extra Z-chain satisfies axioms 1-4; induction is what rules out such non-standard elements'
- **rational_number** — second_coordinate_nonzero: 'allowing b = 0 makes [(a,0)] ~ [(c,0)] for all a,c and breaks the field structure (division by 0)'
- **real_is_ordered_field** — sign_cases_in_multiplication: 'defining A*B by { ab : a in A, b in B } for all cuts gives all of Q once A or B contains arbitrarily negative rationals -- not a cut'
- **real_is_ordered_field** — no_greatest_element_of_a_cut: 'without it, -A is ambiguous and 0* has two representations'
- **real_number** — cut_axioms: 'dropping "proper subset" admits +-infinity; dropping "no greatest element" doubles every rational'
- **real_uniqueness** — dedekind_complete: 'Q and the field of real algebraic numbers are both Archimedean ordered fields, not isomorphic to R (both countable)'
- **real_uniqueness** — ordered: 'C is a field with the same cardinality as R but is not order-isomorphic to anything (it has no order); "field isomorphism" alone is a different, choice-dependent question'
- **real_uniqueness** — archimedean_hence_from_completeness: 'non-Archimedean ordered fields (hyperreals, rational functions with a suitable order) are not covered and are not isomorphic to R'
- **recursion_theorem** — successor_injective: 'if S is not injective the two attempts on overlapping segments can disagree; f is not well-defined'
- **recursion_theorem** — zero_not_a_successor: 'if 0 = S k for some k, the equation at 0 and the equation at S k both constrain f(0) and can conflict'
- **recursion_theorem** — induction_principle: 'without induction there may be "non-standard" naturals not reached from 0, on which f is unconstrained -- existence and uniqueness both fail'
- **sqrt2_irrational** — lowest_terms: 'the argument needs a minimal representative; without "gcd(p,q)=1" you only get an infinite descent, which still works but is the same content'
- **sqrt2_irrational** — n_not_a_perfect_square: 'sqrt(4) = 2 IS rational -- the theorem is specifically about non-squares'

