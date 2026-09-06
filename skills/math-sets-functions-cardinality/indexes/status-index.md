# Result index by node type (generated)

## primitive
- **proposition_logic** (logic) — connectives and truth-functional reasoning
- **predicate_logic** (logic) — quantifiers over a domain, bound variables
- **set** (sets) — an element of a model of ZFC

## axiom
- **axiom_extensionality** (axioms) — sets with the same elements are equal
- **axiom_empty_set** (axioms) — there is a set with no elements
- **axiom_pairing** (axioms) — for any a,b the set {a,b} exists
- **axiom_union** (axioms) — for any set F the union of its members exists
- **axiom_power_set** (axioms) — for any set X the set of all subsets of X exists
- **axiom_separation** (axioms) — { x in X : phi(x) } is a set for any formula phi
- **axiom_replacement** (axioms) — the image of a set under a definable class function is a set
- **axiom_infinity** (axioms) — there is an inductive set
- **axiom_foundation** (axioms) — membership is well-founded; no infinite descending epsilon-chains
- **axiom_of_choice** (axioms) — every family of nonempty sets has a choice function
- **countable_choice** (axioms) — a countable family of nonempty sets has a choice function
- **dependent_choice** (axioms) — a total relation admits an infinite chain

## structure
- **zf** (axioms) — the nine ZF axioms
- **zfc** (axioms) — ZF plus the axiom of choice

## notation_convention
- **quantifier_order** (logic) — forall x exists y is weaker than exists y forall x

## principle_law
- **quantifier_negation** (logic) — not forall x P(x) iff exists x not P(x) ; not exists iff forall not
- **proof_methods** (logic) — classical proof strategies
- **well_defined_on_quotient** (equivalence) — [x] -> f(x) is a function iff x~x' implies f(x)=f(x')

## definition
- **empty_set** (sets) — the unique set with no elements
- **subset** (sets) — A subset B iff every element of A is in B
- **power_set** (sets) — P(X) is the set of all subsets of X
- **binary_union_intersection** (sets) — A cup B, A cap B
- **family_union_intersection** (sets) — union F ; intersection F (F nonempty)
- **indexed_family** (sets) — a function i -> A_i on an index set I
- **indexed_union_intersection** (sets) — union over i of A_i ; intersection over i (I nonempty)
- **set_difference** (sets) — A minus B = { x in A : x not in B }
- **relative_complement** (sets) — X^c = U minus X relative to an ambient U
- **ordered_pair** (sets) — (a,b) = {{a},{a,b}} ; (a,b)=(c,d) iff a=c and b=d
- **cartesian_product** (sets) — X x Y = { (x,y) : x in X, y in Y }
- **disjoint_union** (sets) — X + Y = (X x {0}) cup (Y x {1})
- **relation** (relations) — a subset of X x Y
- **domain_range** (relations) — dom R and ran R
- **relation_composition_inverse** (relations) — S o R and R^{-1}
- **relation_properties** (relations) — reflexive, symmetric, antisymmetric, transitive, connex
- **relation_restriction** (relations) — R restricted to A
- **equivalence_relation** (equivalence) — reflexive, symmetric, transitive
- **equivalence_class** (equivalence) — [x] = { y : y ~ x }
- **partition** (equivalence) — nonempty pairwise-disjoint sets covering X
- **canonical_projection** (equivalence) — pi : X -> X/~ , x -> [x]
- **function** (functions) — a single-valued relation, total on its domain, with a fixed codomain
- **injection** (functions) — f(x)=f(y) implies x=y
- **surjection** (functions) — every y in the codomain has a preimage
- **bijection** (functions) — injective and surjective
- **image** (functions) — f[A] = { f(x) : x in A }
- **preimage** (functions) — f^{-1}[B] = { x : f(x) in B } , defined for every f
- **function_composition** (functions) — (g o f)(x) = g(f(x))
- **identity_function** (functions) — id_X(x) = x
- **inverse_function** (functions) — g with g o f = id and f o g = id
- **function_space** (functions) — Y^X is the set of all functions X -> Y
- **characteristic_function** (functions) — 1_A : X -> {0,1} , 1_A(x)=1 iff x in A
- **partial_order** (orders) — reflexive, antisymmetric, transitive
- **total_order** (orders) — a partial order in which any two elements are comparable
- **strict_order** (orders) — irreflexive and transitive
- **order_morphism** (orders) — x <= y implies f(x) <= f(y) ; bijective order embedding
- **bounds_extrema** (orders) — upper/lower bound, sup/inf, max/min
- **chain_antichain** (orders) — a totally ordered / pairwise-incomparable subset
- **maximal_element** (orders) — m with no element strictly above it
- **well_order** (orders) — a total order in which every nonempty subset has a least element
- **ordinal** (ordinals) — a transitive set well-ordered by membership
- **finite_ordinal** (naturals) — an element of omega
- **equinumerous** (cardinality) — |X| = |Y| iff there is a bijection X -> Y
- **cardinal_le** (cardinality) — |X| <= |Y| iff there is an injection X -> Y
- **cardinal_lt** (cardinality) — |X| < |Y| iff |X| <= |Y| and not |X| = |Y|
- **finite_set** (cardinality) — equinumerous with some finite ordinal
- **infinite_set** (cardinality) — not finite
- **dedekind_infinite** (cardinality) — equinumerous with a proper subset of itself
- **countable_set** (cardinality) — admits an injection into omega
- **uncountable_set** (cardinality) — infinite and not countable
- **aleph_hierarchy** (cardinality) — aleph_alpha enumerates the infinite well-ordered cardinals
- **continuum** (cardinality) — c = 2^aleph0 = |R|

## construction
- **quotient_set** (equivalence) — X/~ is the set of equivalence classes
- **omega_construction** (naturals) — omega is the smallest inductive set ; 0 = empty set, S x = x cup {x}

## proposition
- **de_morgan_laws** (sets) — complement of a union is the intersection of complements, and dually
- **distributive_laws** (sets) — A cap union B_i = union (A cap B_i)
- **image_algebra** (functions) — f[union A_i] = union f[A_i] ; f[intersection A_i] subset intersection f[A_i]
- **left_inverse_iff_injective** (functions) — f has a left inverse iff f is injective (domain nonempty)
- **right_inverse_iff_surjective** (functions) — f has a right inverse iff f is surjective (uses choice)
- **composition_preserves_properties** (functions) — composites of injections are injections, etc.

## theorem
- **equivalence_partition_correspondence** (equivalence) — equivalence relations on X are in bijection with partitions of X
- **universal_property_quotient** (equivalence) — functions X/~ -> Z are exactly functions X -> Z constant on classes
- **preimage_algebra** (functions) — f^{-1} commutes with arbitrary union, arbitrary intersection, and complement
- **inverse_iff_bijective** (functions) — f has a two-sided inverse iff f is a bijection
- **powerset_iso_two_power** (functions) — A -> 1_A is a bijection P(X) -> 2^X
- **pigeonhole_principle** (functions) — no injection from a finite set into a strictly smaller one
- **zorn_lemma** (orders) — a poset in which every chain has an upper bound has a maximal element
- **well_ordering_theorem** (orders) — every set can be well-ordered
- **ac_equivalences** (orders) — AC iff Zorn iff well-ordering iff cardinal comparability
- **transfinite_induction** (ordinals) — if a property passes to alpha whenever it holds below alpha it holds for all ordinals
- **transfinite_recursion** (ordinals) — a class function on ordinals is uniquely determined by a rule using its earlier values
- **order_type_theorem** (ordinals) — every well-order is isomorphic to a unique ordinal
- **peano_holds_in_omega** (naturals) — (omega, 0, S) satisfies the Peano axioms
- **recursion_theorem** (naturals) — unique f on omega with f(0)=a and f(S n)=g(n, f n)
- **cantor_schroeder_bernstein** (cardinality) — injections both ways give a bijection ; no choice needed
- **cantor_theorem** (cardinality) — |X| < |P(X)| for every set X
- **finite_iff_not_dedekind_infinite** (cardinality) — over ZF + countable choice, the two notions of infinite coincide
- **nat_times_nat_countable** (cardinality) — the Cantor pairing is a bijection omega x omega -> omega
- **countable_closure_properties** (cardinality) — subsets, images, finite products, and countable unions of countable sets are countable
- **cantor_diagonal** (cardinality) — 2^omega is uncountable
- **powerset_nat_equinumerous_reals** (cardinality) — |P(omega)| = |2^omega| = |R|
- **cardinal_comparability** (cardinality) — for any X,Y either |X| <= |Y| or |Y| <= |X| (uses AC)
- **infinite_cardinal_arithmetic** (cardinality) — aleph0 + aleph0 = aleph0*aleph0 = aleph0 ; kappa*kappa = kappa for infinite kappa (AC)
- **hartogs_number** (cardinality) — for every X there is a well-ordered cardinal that does not inject into X ; no choice

## corollary

## mathematical_identity

