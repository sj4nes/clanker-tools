# Result index by node type (generated)

## primitive
- **set** (foundations) — -

## axiom
- **axiom_of_choice** (foundations) — every family of nonempty sets has a choice function
- **countable_choice** (foundations) — a countable family of nonempty sets has a choice function
- **peano_axioms** (naturals) — 0 in N; S injective; 0 not a successor; induction

## structure
- **natural_number** (naturals) — a system (N,0,S) satisfying the Peano axioms
- **commutative_monoid** (structures) — associative commutative binary op with identity
- **commutative_semiring** (structures) — two monoids + distributivity, no additive inverses required
- **commutative_ring** (structures) — commutative semiring with additive inverses
- **integral_domain** (structures) — commutative ring, 1!=0, no zero divisors
- **field** (structures) — commutative ring in which every nonzero element is a unit
- **ordered_ring** (structures) — ring with a total order compatible with + and with * by positives
- **ordered_integral_domain** (structures) — integral domain that is an ordered ring
- **ordered_field** (structures) — field with a total order compatible with + and *

## notation_convention

## principle_law
- **well_defined_on_quotient** (foundations) — [x] -> [h(x)] is a function iff x~x' implies h(x)~h(x')
- **induction_principle** (naturals) — X contains 0 and is S-closed implies X = N

## definition
- **cartesian_product** (foundations) — X x Y = { (x,y) : x in X, y in Y }
- **relation** (foundations) — a subset of X x X
- **function** (foundations) — a relation that is single-valued and total
- **injection** (foundations) — f(x)=f(y) implies x=y
- **surjection** (foundations) — every y has a preimage
- **bijection** (foundations) — injective and surjective
- **composition** (foundations) — (g o f)(x) = g(f(x))
- **inverse_function** (foundations) — f o f^{-1} = id and f^{-1} o f = id
- **equivalence_relation** (foundations) — reflexive, symmetric, transitive
- **equivalence_class** (foundations) — [x] = { y : y ~ x }
- **nat_addition** (naturals) — a+0=a ; a+S(b)=S(a+b)
- **nat_multiplication** (naturals) — a*0=0 ; a*S(b)=a*b+a
- **nat_exponentiation** (naturals) — a^0=1 ; a^{S(b)}=a^b * a
- **nat_order** (naturals) — a <= b iff exists c, a + c = b
- **integer_addition** (integers) — [(a,b)] + [(c,d)] = [(a+c, b+d)]
- **integer_multiplication** (integers) — [(a,b)] * [(c,d)] = [(ac+bd, ad+bc)]
- **integer_negation** (integers) — -[(a,b)] = [(b,a)]
- **integer_order** (integers) — [(a,b)] <= [(c,d)] iff a+d <= b+c in N
- **rational_addition** (rationals) — [(a,b)] + [(c,d)] = [(ad+bc, bd)]
- **rational_multiplication** (rationals) — [(a,b)] * [(c,d)] = [(ac, bd)]
- **rational_inverse** (rationals) — [(a,b)]^{-1} = [(b,a)] for a != 0
- **rational_order** (rationals) — [(a,b)] with b>0 is <= [(c,d)] with d>0 iff ad <= bc in Z
- **rational_absolute_value** (rationals) — |x| = x if x>=0 else -x ; triangle inequality holds
- **cauchy_sequence_rational** (rationals) — forall eps>0 in Q exists N forall m,n>=N |x_m - x_n| < eps
- **dedekind_cut** (reals) — a nonempty proper downward-closed subset of Q with no greatest element
- **real_order** (reals) — A <= B iff A is a subset of B ; this order is total
- **real_addition** (reals) — A + B = { a + b : a in A, b in B } ; again a cut
- **real_additive_inverse** (reals) — -A = { p in Q : -p is an upper bound of A but not the least one }
- **real_multiplication** (reals) — defined for positive cuts then extended by sign
- **real_absolute_value** (reals) — |x| = max(x, -x) ; triangle inequality holds
- **finite_set** (cardinality) — in bijection with { k in N : k < n } for some n
- **countable_set** (cardinality) — admits an injection into N

## construction
- **quotient_set** (foundations) — X/~ is the set of equivalence classes
- **integer** (integers) — Z = (N x N)/~ , (a,b) ~ (c,d) iff a+d = b+c
- **rational_number** (rationals) — Q = (Z x Z*)/~ , (a,b) ~ (c,d) iff ad = bc
- **real_number** (reals) — R is the set of Dedekind cuts of Q
- **cauchy_completion** (reals) — R' = (Cauchy sequences of rationals)/(null sequences)

## proposition
- **partition_equiv** (foundations) — equivalence relations correspond bijectively to partitions
- **strong_induction** (naturals) — if P holds at n whenever it holds below n then P holds everywhere
- **well_ordering_principle** (naturals) — every nonempty subset of N has a least element
- **nat_semiring_laws** (naturals) — + and * are associative and commutative, * distributes over +
- **nat_cancellation** (naturals) — a+c=b+c implies a=b ; a*c=b*c and c!=0 implies a=b
- **nat_no_zero_divisors** (naturals) — a*b=0 implies a=0 or b=0
- **nat_order_trichotomy** (naturals) — exactly one of a<b, a=b, a>b
- **nat_order_compatible** (naturals) — a<=b implies a+c<=b+c and a*c<=b*c
- **integer_relation_equivalence** (integers) — ~_Z is reflexive symmetric transitive
- **integer_operations_well_defined** (integers) — + , * , - respect ~_Z
- **nat_embeds_in_integer** (integers) — n -> [(n,0)] is an injective semiring and order homomorphism
- **integer_cancellation** (integers) — ac = bc and c != 0 imply a = b
- **integer_well_ordering** (integers) — a nonempty subset of Z bounded below has a least element
- **rational_relation_equivalence** (rationals) — ~_Q is an equivalence relation (transitivity uses that Z is a domain)
- **rational_operations_well_defined** (rationals) — + , * , inverse respect ~_Q
- **integer_embeds_in_rational** (rationals) — a -> [(a,1)] is an injective ordered ring homomorphism
- **rational_lowest_terms** (rationals) — every rational equals a/b with gcd(a,b)=1 and b>0, uniquely
- **rational_archimedean** (rationals) — for every x in Q there is n in N with n > x
- **rational_order_dense** (rationals) — between any two rationals lies a third
- **rational_embeds_in_real** (reals) — q -> q* = { p in Q : p < q } is an injective ordered field homomorphism
- **integer_countable** (cardinality) — Z is a countable union of finite sets
- **rational_countable** (cardinality) — Q injects into Z x Z* which is countable

## theorem
- **recursion_theorem** (naturals) — unique f with f(0)=a and f(S n)=g(n,f n)
- **nat_division_with_remainder** (naturals) — for b>0, unique q,r with a = bq + r and 0 <= r < b
- **integer_is_commutative_ring** (integers) — (Z,+,*,0,1) satisfies the ring axioms
- **integer_is_integral_domain** (integers) — Z has no zero divisors and 1 != 0
- **integer_is_ordered_integral_domain** (integers) — the order on Z is total and compatible with + and *
- **integer_division_with_remainder** (integers) — for b != 0, unique q,r with a = bq + r and 0 <= r < |b|
- **gcd_bezout** (integers) — gcd(a,b) exists and equals ax + by for some integers x,y
- **rational_is_field** (rationals) — every nonzero rational has a multiplicative inverse
- **rational_is_ordered_field** (rationals) — the order on Q is total and compatible with + and *
- **field_of_fractions** (rationals) — Q is the smallest field containing Z, up to unique isomorphism
- **sqrt2_irrational** (rationals) — no rational x satisfies x^2 = 2
- **rational_incomplete_lub** (rationals) — { x in Q : x^2 < 2 } is nonempty and bounded above but has no supremum in Q
- **rational_incomplete_cauchy** (rationals) — there is a Cauchy sequence of rationals with no limit in Q
- **real_is_ordered_field** (reals) — (R,+,*,0*,1*,<=) satisfies the ordered-field axioms
- **lub_property** (reals) — every nonempty subset of R bounded above has a supremum, namely the union of its cuts
- **real_archimedean** (reals) — for every x in R there is n in N with n > x
- **rational_dense_in_real** (reals) — between any two reals lies a rational
- **nth_root_exists** (reals) — for x > 0 in R and n in N+ there is a unique y > 0 with y^n = x
- **dedekind_cauchy_equivalent** (reals) — the Dedekind and Cauchy constructions are isomorphic ordered fields
- **real_uniqueness** (reals) — any two Dedekind-complete ordered fields are uniquely order-isomorphic
- **nat_pairing_bijection** (cardinality) — pi(m,n) = (m+n)(m+n+1)/2 + n is a bijection N x N -> N
- **countable_union_countable** (cardinality) — a countable union of countable sets is countable (uses countable choice)
- **cantor_theorem** (cardinality) — there is no surjection from X onto its power set
- **cantor_diagonal_argument** (cardinality) — from any sequence of reals in [0,1] one can construct a real it omits
- **schroeder_bernstein** (cardinality) — injections X -> Y and Y -> X give a bijection X -> Y
- **real_uncountable** (cardinality) — there is no surjection from N onto R

## corollary

## mathematical_identity

