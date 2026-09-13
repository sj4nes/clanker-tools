# Specialization & hypothesis-dropped counterexamples (generated from results/*.yaml)

For every node: at least one specialization / boundary case, and at least one
counterexample showing a named hypothesis cannot be dropped (or a note that
every hypothesis is essential / the statement is unconditional).


## set

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## function

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## bijection

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## equivalence_relation

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## quotient_set

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## finite_set

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## indexed_family

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## zorns_lemma

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## axiom_of_choice

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## induction_principle

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## real_number

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## complex_number

- **spec:** restricting conjugation to R gives the identity, which is why every real result is the b = 0 case of its complex counterpart
- **drop `positive_definiteness_of_the_form`:** over C the bilinear form sum z_i w_i is NOT positive definite (take z = (1, i): sum z_i^2 = 0 with z != 0). This is exactly why the complex inner product must conjugate one slot -- see inner_product_convention

## fundamental_theorem_of_algebra

- **spec:** degree 2 over R: t^2 + 1 has no real root but factors over C, which is the minimal instance of why R is not algebraically closed
- **drop `the_field_being_C`:** over R the theorem is false: t^2 + 1 is irreducible. This is precisely the hypothesis that eigenvalue_existence_closed needs, and why a real rotation matrix can have no real eigenvalue
- **drop `nonconstant`:** a nonzero constant polynomial has no root; the degree >= 1 hypothesis is not decorative

## compactness_cited

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## extreme_value_cited

- **drop `none_all_hypotheses_essential`:** every listed hypothesis is used; see the block above

## polynomial_ring

- **spec:** F = R, deg g = 1: division with remainder is evaluation, f(t) = q(t)(t - a) + f(a) -- the factor theorem
- **drop `F_being_a_field`:** over a general commutative ring, Z[t] say, division with remainder fails (t does not divide 2t + 1 with remainder of lower degree) and ideals need not be principal. Minimal polynomials of matrices over a ring are correspondingly badly behaved -- see smith_normal_form_boundary

## field

- **spec:** F = Q, R, C: the fields this capsule actually uses
- **spec:** F = F_2 = {0,1}: the two-element field, where 1 + 1 = 0 -- the standing counterexample for every char_not_2 result
- **spec:** F = F_p for p prime: finite fields, over which all the any_field results still hold
- **drop `existence_of_inverses`:** Z is a commutative ring but not a field; over Z 'vector spaces' become modules, bases need not exist, and rank is replaced by invariant factors (smith_normal_form_boundary)
- **drop `commutativity_of_multiplication`:** over a division ring (the quaternions H) left and right vector spaces differ and the determinant theory breaks: det(AB) = det(A)det(B) has no direct analogue
- **drop `zero_not_equal_one`:** in the zero ring every module is trivial and dimension is meaningless

## characteristic_not_two

- **spec:** F = Q, R, C all have characteristic 0, so every char_not_2 result applies unconditionally there
- **spec:** F = F_3: 1 + 1 = 2 != 0, so the hypothesis holds over odd finite fields too
- **drop `char_not_2`:** over F_2 the polarisation identity fails: the map q(x) = x^T A x determines A only up to adding an alternating matrix, since q(x+y) - q(x) - q(y) = 2 x^T A y = 0. Symmetric and alternating forms cease to be distinguishable, and quadratic_form's uniqueness of the symmetric representative is false

## algebraically_closed_field

- **spec:** F = C by the fundamental theorem of algebra
- **spec:** the algebraic closure of any field exists (needs AC in general), so every capsule result tagged algebraically_closed can be reached by passing to F-bar -- at the cost of leaving the original field
- **drop `algebraic_closure`:** over R the rotation by 90 degrees, [[0,-1],[1,0]], has characteristic polynomial t^2 + 1 and NO real eigenvalue. Every statement of the form 'an operator has an eigenvalue', 'is triangularisable', 'has a Jordan form' fails over R for this matrix
- **drop `over_Q`:** even worse: [[0,2],[1,0]] has char poly t^2 - 2, with no root in Q

## ordered_field_hyp

- **spec:** F = R, the case every spectral result in this capsule is stated over
- **spec:** F = Q is ordered too, so Sylvester's law of inertia holds over Q -- but the spectral theorem does not, because the eigenvalues need not be rational
- **drop `the_order`:** C admits no compatible order (i^2 = -1 < 0 contradicts squares being nonnegative). So 'positive definite' over C must be read as 'the HERMITIAN form x^* A x takes positive REAL values', which is a different statement needing self-adjointness to even be real-valued
- **drop `over_a_finite_field`:** F_p has no compatible order at all; positive_definite and sylvester_law_of_inertia are simply not statable there

## finite_dimensional

- **spec:** F^n is finite-dimensional with the standard spanning set of size n
- **spec:** the space of polynomials of degree <= d is finite-dimensional (dimension d+1); the space of ALL polynomials is not
- **drop `finiteness`:** F[t] (all polynomials) has no finite spanning set. Dropping the hypothesis breaks rank_nullity (the shift operator on F[t] is injective, not surjective, with zero nullity), injective_surjective_equivalence, double_dual, and the existence of an eigenvalue -- see infinite_dimensional_boundary for the catalogue

## index_convention

- **spec:** under the opposite (row-vector) convention the composition rule becomes [S o T] = [T][S] and every matrix identity in this capsule transposes
- **drop `none_all_hypotheses_essential`:** a convention has no hypotheses; the failure mode is INCONSISTENCY, not falsity -- mixing conventions mid-derivation silently transposes results

## transpose_convention

- **spec:** over R the two coincide, which is why the statistics-facing half of the capsule can be written entirely with A^T
- **drop `none_all_hypotheses_essential`:** a convention; the failure mode is using A^T over C, under which A^T A need not be positive semidefinite -- take A = [[1, i]], where A^T A has a zero eigenvalue direction while A^* A does not

## inner_product_convention

- **spec:** over R conjugation is the identity and the form is simply bilinear and symmetric
- **spec:** the standard inner product on C^n under this convention is <x,y> = sum_i x_i conj(y_i) = y^* x
- **drop `conjugate_symmetry`:** the plain bilinear form sum_i x_i y_i on C^n is NOT positive definite: x = (1, i) gives sum x_i^2 = 1 + (-1) = 0 with x != 0. Every norm, projection, and spectral result in the inner-product half of the capsule collapses without the conjugation

## characteristic_polynomial_convention

- **spec:** n = 1: p_A(t) = t - A_{11} under this convention, versus A_{11} - t under the other
- **spec:** n = 2: p_A(t) = t^2 - tr(A) t + det(A), the form used throughout the capsule's 2x2 instance checks
- **drop `none_all_hypotheses_essential`:** a convention; the failure mode is a sign error. Under det(A - tI) the constant term is det(A), not (-1)^n det(A), and quoting char_poly_coefficients across conventions produces wrong signs for odd n

## vector_space

- **spec:** V = F^n with componentwise operations -- the model for the whole capsule
- **spec:** V = F itself, a one-dimensional space over F
- **spec:** V = {0}, the zero space: a legitimate vector space with the empty basis and dimension 0
- **spec:** V = F[t], or the set of functions X -> F -- infinite-dimensional instances showing the axioms alone do not give finiteness
- **drop `the_axiom_1v_equals_v`:** without it, the map a*v := 0 for all a satisfies every other axiom on any abelian group, making scalar multiplication trivial. It is the axiom that ties the field action to the group and is the one most often omitted from informal lists
- **drop `F_being_a_field`:** over a ring the structure is a MODULE: Z/6 as a Z-module has torsion, no basis, and no well-defined dimension

## vector_space_basic_consequences

- **spec:** in F^n these are the componentwise facts, but the proof uses only the axioms and so holds in every V
- **drop `invertibility_of_nonzero_scalars`:** over the ring Z/6 as a module over itself, 2*3 = 0 with neither factor zero -- the no-zero-divisors clause genuinely needs F to be a field

## subspace

- **spec:** {0} and V are subspaces of V (the trivial ones)
- **spec:** in R^3: the origin, every line through the origin, every plane through the origin, and R^3 -- and nothing else
- **spec:** ker T and im T are subspaces, which is what makes rank and nullity dimensions
- **drop `containing_zero`:** the empty set is closed under both operations vacuously but is not a vector space -- the axioms require an identity
- **drop `closure_under_scalar_multiplication`:** the first quadrant of R^2 is closed under addition but not under multiplication by -1
- **drop `closure_under_addition`:** the union of the two coordinate axes in R^2 is closed under scalar multiplication but (1,0) + (0,1) leaves it -- this is why subspace_intersection is about INTERSECTIONS, not unions

## subspace_criterion

- **spec:** a = b = 0 recovers 0 in U; b = 0 recovers closure under scalars; a = b = 1 recovers closure under addition
- **drop `nonemptiness`:** the empty set satisfies the quantified condition vacuously; without nonemptiness the criterion would wrongly certify it as a subspace

## subspace_intersection

- **spec:** two distinct lines through the origin in R^2 intersect in {0}, a subspace, but their union is not
- **spec:** the intersection of all subspaces containing S is span(S) -- this is span_is_smallest_subspace
- **drop `intersection_rather_than_union`:** the x-axis and y-axis in R^2 are subspaces; their union contains (1,0) and (0,1) but not (1,1)

## linear_combination

- **spec:** J empty: the empty sum is 0 by convention, which is why span(empty) = {0}
- **spec:** |J| = 1: the combinations of a single v are the scalar multiples of v
- **drop `finiteness`:** allowing infinite sums requires convergence, hence a topology and completeness -- that is Hilbert space theory, not linear algebra. Under the algebraic definition, the standard basis of the space of ALL sequences does NOT span it: (1,1,1,...) is not a finite combination of the e_i. This single point is why a Hamel basis of an infinite-dimensional space is enormous and unusable

## span

- **spec:** span of a single nonzero v is the line Fv
- **spec:** span(empty) = {0}, so the empty set is a basis of the zero space and dim{0} = 0
- **spec:** span of the standard basis of F^n is F^n
- **drop `none_all_hypotheses_essential`:** span is a definition with no hypotheses; the only trap is the empty case, which is why the convention is stated

## span_is_smallest_subspace

- **spec:** S a subspace already: then span(S) = S
- **drop `U_being_a_subspace`:** the minimality claim fails for arbitrary supersets: S is contained in many sets that do not contain span(S)

## linear_independence

- **spec:** the empty family is independent vacuously
- **spec:** a single vector v is independent iff v != 0
- **spec:** any family containing 0 is dependent (take that coefficient 1, the rest 0)
- **spec:** two vectors are independent iff neither is a scalar multiple of the other
- **drop `all_coefficients_zero`:** requiring only SOME coefficient to be nonzero would make every family dependent; the quantifier is over ALL representations of 0
- **drop `the_field`:** over F_2 the vectors (1,1) and (1,1) are dependent, but independence is also field-sensitive in subtler ways: (1, sqrt 2) and (1, 1) are independent over Q as a Q-vector space and dependent over R in R^2 only if proportional -- always check which field

## dependence_lemma

- **spec:** k = 2: if v_2 = c v_1 then removing v_2 leaves the span unchanged
- **drop `v_1_not_zero`:** if v_1 = 0 the list is dependent but no LATER vector need be redundant -- (0, e_1) is dependent, yet removing e_1 changes the span. The conclusion must then be about removing v_1 itself
- **drop `invertibility_of_a_j`:** solving for v_j divides by a_j, which needs F to be a field; over Z this step fails and is the origin of the module-theoretic complications in smith_normal_form_boundary

## basis

- **spec:** the standard basis (e_1,...,e_n) of F^n
- **spec:** the empty family is a basis of {0}
- **spec:** (1, t, t^2, ...) is a basis of F[t]: infinite, but every element is still a FINITE combination
- **spec:** (1, i) is a basis of C as an R-vector space, but (1) is a basis of C as a C-vector space -- dimension depends on the field of scalars
- **drop `independence`:** a spanning set that is dependent gives non-unique coordinates: in R^2, (e_1, e_2, e_1+e_2) spans but 0 has infinitely many representations
- **drop `spanning`:** an independent family that does not span gives coordinates only on a proper subspace

## steinitz_exchange

- **spec:** m = 1: any single nonzero vector can replace some member of a spanning list
- **spec:** m = n: the u's themselves then span, which is the 'n independent vectors in an n-dimensional space form a basis' corollary
- **drop `independence_of_the_u`:** without it the bound is false: in F^1, (1, 1, 1) is a 'longer than spanning' list precisely because it is dependent
- **drop `finiteness`:** in F[t], (1, t, t^2, ...) is independent and infinite while no finite list spans -- the inequality is vacuous, and dimension theory must be redone with cardinals

## basis_existence_finite

- **spec:** S already independent: the basis is S itself
- **spec:** L empty: extending the empty list yields a basis from scratch
- **drop `finite_dimensionality`:** for an infinite-dimensional V the deletion process need not halt and the extension process needs transfinite recursion -- i.e. Zorn. See basis_existence_general, whose choice grade is needs_full_AC

## basis_existence_general

- **spec:** V finite-dimensional: reduces to basis_existence_finite, which needs no choice at all
- **spec:** V = R as a Q-vector space: a Hamel basis exists but none can be written down; its existence yields a non-measurable set and a discontinuous additive function R -> R
- **drop `the_axiom_of_choice`:** Blass showed that in ZF, 'every vector space has a basis' implies AC. So there are models of ZF containing a vector space with NO basis. This is the only genuinely non-choice-free result in the capsule

## dimension_well_defined

- **spec:** F^n: every basis has exactly n elements, so dim F^n = n
- **spec:** C over R has dimension 2; C over C has dimension 1 -- the theorem fixes the number only once the SCALAR FIELD is fixed
- **drop `finite_generation`:** for infinite-dimensional spaces the statement survives as a cardinality equality, but only with AC-dependent cardinal arithmetic; the elementary Steinitz argument does not apply
- **drop `F_being_a_field`:** over a general ring the analogous statement (the invariant basis number property) can FAIL: there are rings with R isomorphic to R^2 as modules. Fields always have IBN

## dimension

- **spec:** dim F^n = n
- **spec:** dim {0} = 0 with the empty basis
- **spec:** dim_R C = 2 but dim_C C = 1: the subscript is not decorative
- **spec:** dim F^{m x n} = mn, the fact behind matrix_addition_scalar
- **drop `well_definedness`:** without dimension_well_defined the notation dim V would depend on the basis chosen and every counting argument in the capsule would collapse
- **drop `the_scalar_field`:** R has dimension 1 over R and infinite (continuum) dimension over Q

## dimension_of_subspace

- **spec:** U = {0}: dimension 0 <= dim V
- **spec:** dim U = dim V - 1: a hyperplane, the kernel of a nonzero functional (see annihilator)
- **drop `finite_dimensionality_of_V`:** in F[t] the subspace of polynomials with zero constant term is a PROPER subspace with the same (infinite) dimension -- the equality clause fails outright. This is the same phenomenon as the infinite-dimensional failure of injective_surjective_equivalence

## basis_unique_representation

- **spec:** B the standard basis of F^n: the coordinates are the components themselves
- **drop `independence`:** with a dependent spanning family, 0 has more than one representation and coordinates are not functions
- **drop `spanning`:** with an independent non-spanning family, some v has no representation at all

## ordered_basis

- **spec:** V = F^n with the standard ordered basis: [v]_B = v, the identity
- **spec:** V = polynomials of degree <= 2 with B = (1, t, t^2): [3 + 5t^2]_B = (3, 0, 5)^T
- **drop `orderedness`:** an unordered basis gives coordinates only up to permutation, so no well-defined map to F^n and no well-defined matrix of a linear map

## coordinate_isomorphism

- **spec:** V = F^n, B standard: the isomorphism is the identity
- **spec:** every 3-dimensional real space -- polynomials of degree <= 2, symmetric 2x2 matrices, R^3 -- is isomorphic to R^3
- **drop `finite_dimensionality`:** two infinite-dimensional spaces of the same Hamel dimension are still isomorphic, but the isomorphism is AC-dependent and unusable; more importantly, as TOPOLOGICAL spaces they need not be isomorphic at all
- **drop `same_scalar_field`:** C and R^2 are isomorphic as R-spaces but not as C-spaces (dimensions 1 and 2 over C... and R^2 is not even a C-space without extra structure)

## sum_of_subspaces

- **spec:** U + {0} = U
- **spec:** U + U = U
- **spec:** in R^3, the sum of two distinct planes through the origin is all of R^3
- **drop `none_all_hypotheses_essential`:** a definition; the trap is the union, which is generally not a subspace

## direct_sum

- **spec:** R^2 = (x-axis) (+) (y-axis), but also R^2 = (x-axis) (+) (diagonal) -- a complement is NOT unique
- **spec:** V = U (+) U^perp for a finite-dimensional subspace of an inner product space (orthogonal_decomposition) -- the ORTHOGONAL complement is the canonical choice among many complements
- **drop `trivial_intersection`:** in R^2 with U = W = the x-axis, U + W = U but the decomposition is wildly non-unique. The sum formula dim(U+W) = dim U + dim W then fails (1 != 2)
- **drop `pairwise_triviality_for_three_or_more`:** for three subspaces, PAIRWISE trivial intersections do NOT suffice: the x-axis, y-axis, and diagonal in R^2 meet pairwise in {0}, yet the sum of the three is not direct -- (1,1) decomposes in more than one way. The correct condition is that each U_i meets the sum of the others trivially

## dimension_formula_sum

- **spec:** U ∩ W = {0}: recovers dim(U (+) W) = dim U + dim W
- **spec:** two planes in R^3: 3 = 2 + 2 - 1, so they must meet in a line -- the standard non-obvious consequence
- **spec:** U subset W: dim(U + W) = dim W and dim(U ∩ W) = dim U, so the identity is trivially true
- **drop `finite_dimensionality`:** for infinite-dimensional subspaces the cardinal arithmetic degenerates (infinity + infinity = infinity) and the formula carries no information
- **drop `two_summands`:** the three-subspace analogue dim(U+W+X) = sum dim - sum dim(pairwise) + dim(triple) is FALSE. The x-axis, y-axis and diagonal in R^2 give 2 versus 1+1+1-0-0-0+0 = 3. Unlike sets, subspaces do not satisfy inclusion-exclusion beyond two terms

## quotient_space

- **spec:** U = {0}: V/U is isomorphic to V
- **spec:** U = V: V/U = {0}
- **spec:** V = R^2, U = the x-axis: V/U is the set of horizontal lines, isomorphic to R by the y-value
- **drop `U_being_a_subspace`:** if U is merely a subset closed under addition but not scaling -- say the nonnegative x-axis in R^2 -- the scalar operation on cosets is not well-defined, since v + U = v' + U no longer implies av + U = av' + U
- **drop `closure_under_addition`:** similarly, a subset closed under scaling but not addition (the union of the axes) breaks coset addition

## quotient_dimension

- **spec:** U = {0}: dim(V/U) = dim V
- **spec:** U a hyperplane: codimension 1, and V/U is one-dimensional -- the setting of a single linear functional
- **drop `finite_dimensionality`:** codimension can be finite while both dimensions are infinite (the polynomials with zero constant term have codimension 1 in F[t]), so the SUBTRACTION is meaningless even though the quotient is fine. Codimension, not dimension, is the robust notion

## linear_map

- **spec:** T(0) = 0 always -- a linear map cannot be an affine translation
- **spec:** V = W = F: the linear maps are exactly x -> cx; the map x -> x + 1 is affine, NOT linear
- **spec:** differentiation on polynomials, and integration over a fixed interval, are both linear
- **drop `homogeneity`:** over C, complex CONJUGATION is additive and R-homogeneous but not C-homogeneous: conj(iz) = -i conj(z) != i conj(z). Such maps are called conjugate-linear (antilinear) and appear in the second slot of the complex inner product
- **drop `additivity`:** x -> |x| on R is homogeneous for positive scalars only and fails additivity
- **drop `same_field`:** a Q-linear map R -> R need not be R-linear: AC gives discontinuous additive functions (see basis_existence_general)

## linear_map_determined_by_basis

- **spec:** V = F^n with the standard basis: T is determined by the n columns T(e_j), which is exactly matrix_of_linear_map
- **drop `B_being_a_basis`:** for a merely SPANNING family the map need not exist: prescribing T(e_1) = T(e_2) = 0 but T(e_1 + e_2) = w != 0 is inconsistent. For a merely INDEPENDENT family T exists but is not unique -- it is unconstrained off the span

## kernel

- **spec:** T = 0: ker T = V
- **spec:** T injective: ker T = {0} (injective_iff_trivial_kernel)
- **spec:** T = differentiation on polynomials: ker T = the constants, dimension 1
- **drop `linearity_of_T`:** for a nonlinear f, f^{-1}(0) is generally not a subspace: the preimage of 0 under x -> x^2 - 1 on R is {-1, 1}
- **drop `the_target_being_zero`:** T^{-1}({w}) for w != 0 is an AFFINE subspace (a coset of ker T), not a subspace -- this is exactly the solution-set structure of linear_system

## image_subspace

- **spec:** T surjective: im T = W
- **spec:** T = 0: im T = {0}
- **spec:** T = x -> Ax: im T = col(A), the column space -- this identification is why column_space is defined as it is
- **drop `linearity`:** the image of a nonlinear map is usually not a subspace: x -> x^2 maps R onto [0, infinity)

## injective_iff_trivial_kernel

- **spec:** V = F^n: T injective iff Ax = 0 has only the trivial solution iff A has full column rank
- **drop `linearity`:** for nonlinear f, f^{-1}(0) = {0} does not give injectivity: x -> x^2 on R has only 0 in its zero set but is not injective

## rank

- **spec:** T = 0: rank 0
- **spec:** T an isomorphism: rank = dim V = dim W
- **spec:** T a projection onto a k-dimensional subspace: rank k
- **drop `finite_dimensionality_of_the_image`:** for an infinite-rank operator the number is a cardinal and the counting theorems below carry no content

## nullity

- **spec:** T injective: nullity 0
- **spec:** T = 0 on V: nullity = dim V
- **drop `none_all_hypotheses_essential`:** a definition; the content is entirely in rank_nullity

## rank_nullity

- **spec:** T injective: rank T = dim V, so im T is a copy of V inside W
- **spec:** T = 0: rank 0, nullity dim V
- **spec:** A in F^{m x n}: n = rank A + dim null(A), the count that drives gaussian_elimination's free-variable bookkeeping
- **drop `finite_dimensionality_of_V`:** the right shift S on F^infinity (sequences) is injective with nullity 0 but NOT surjective; and the left shift is surjective with nullity 1. Neither satisfies any finite count. Rank-nullity is the canonical casualty of dropping finite_dimensional
- **drop `linearity`:** for a nonlinear map neither side is defined

## injective_surjective_equivalence

- **spec:** V = W = F^n: a square matrix is injective iff surjective iff invertible -- one clause of invertibility_equivalences
- **spec:** the finite-field analogue of the pigeonhole principle for linear maps
- **drop `finite_dimensionality`:** on F[t], multiplication by t is injective but not surjective (nothing maps to the constant 1); formal differentiation is surjective but not injective. Both live on the SAME space, so equality of dimensions holds trivially and it is finiteness alone that fails
- **drop `equal_dimensions`:** F^2 -> F^3 can be injective and never surjective; F^3 -> F^2 can be surjective and never injective

## linear_isomorphism

- **spec:** the coordinate map [.]_B is an isomorphism V -> F^n (coordinate_isomorphism)
- **spec:** V isomorphic to W iff dim V = dim W, for finite-dimensional spaces over the same field
- **drop `bijectivity`:** an injective non-surjective linear map has a left inverse but no two-sided one
- **drop `linearity_of_T`:** a nonlinear bijection has a nonlinear inverse, and none of the structure transfers

## first_isomorphism_theorem

- **spec:** T injective: V/{0} isomorphic to V, so T is an isomorphism onto its image
- **spec:** taking dimensions recovers rank_nullity via quotient_dimension -- the two theorems are the same fact, one counted and one structural
- **drop `linearity`:** for a nonlinear map the fibres are not cosets of a subspace and there is no quotient to form
- **drop `none_all_hypotheses_essential`:** no finite-dimensionality is needed: this is the structural statement that SURVIVES in infinite dimension while its dimension-counting shadow (rank_nullity) does not

## space_of_linear_maps

- **spec:** W = F: L(V,F) = V^*, the dual space, of dimension n
- **spec:** V = W = F^n: L(V) is isomorphic to F^{n x n}, of dimension n^2
- **drop `finite_dimensionality`:** for infinite-dimensional V the algebraic dual and hence L(V,W) is strictly larger than V in cardinality, and dim L(V,F) > dim V -- which is exactly why double_dual fails

## composition_of_linear_maps

- **spec:** V = W = X: L(V) becomes an associative unital algebra, the setting for minimal_polynomial and cayley_hamilton
- **drop `conformability`:** composing non-conformable maps is not a false statement but an ill-typed one -- the type check is the whole content
- **drop `commutativity_is_NOT_available`:** ST != TS in general; see matrix_mult_noncommutative

## linear_operator

- **spec:** V = F^n: L(V) is isomorphic to the algebra F^{n x n}
- **spec:** p(T) for p in F[t] is defined because T^k makes sense -- the map p -> p(T) is the algebra homomorphism whose kernel defines minimal_polynomial
- **drop `equal_domain_and_codomain`:** for T: V -> W with V != W, T^2 is undefined, so eigenvalues, characteristic polynomials, and diagonalisability are all meaningless. This is why SVD (which handles rectangular A) needs two different bases

## invertible_operator

- **spec:** V = F^n: invertible operators correspond to invertible matrices (invertibility_equivalences)
- **drop `finite_dimensionality`:** on F[t] the shift operators L (delete the constant term) and R (multiply by t) satisfy LR = I but RL != I. A one-sided inverse is genuinely weaker in infinite dimension, and this pair is the standard witness

## dual_space

- **spec:** V = F^n: V^* is the space of row vectors, f(x) = a^T x -- the transpose convention made concrete
- **spec:** V = polynomials of degree <= d: evaluation at a point, and integration over an interval, are functionals
- **drop `finite_dimensionality`:** dim V^* = dim V only in finite dimension (dual_basis). For infinite-dimensional V the ALGEBRAIC dual is strictly larger in cardinality, which is why double_dual fails there

## dual_basis

- **spec:** V = F^n with the standard basis: b_i^* is the i-th coordinate function, the i-th row of I
- **drop `finite_dimensionality`:** for V = F[t] with basis (1, t, t^2, ...), the functionals t^i -> coefficient are independent but do NOT span V^*: the functional 'sum of all coefficients' is not a finite combination of them. dim V^* > dim V strictly
- **drop `the_whole_basis_matters`:** b_1^* changes if b_2 is replaced, even though b_1 is untouched -- the dual basis is not computed entrywise

## dual_map

- **spec:** in dual bases, the matrix of T^t is the TRANSPOSE of the matrix of T -- the conceptual content of the transpose operation
- **spec:** T = I: T^t = I
- **drop `none_all_hypotheses_essential`:** the definition needs only linearity; it is the MATRIX statement that needs finite-dimensionality and a choice of dual bases

## double_dual

- **spec:** V = F^n: ev identifies column vectors with functionals on row vectors, the familiar 'a vector is what it does to covectors'
- **drop `finite_dimensionality`:** for V = F[t], dim V^* > dim V and dim V^** > dim V^*, so ev is injective but far from surjective. In functional analysis the CONTINUOUS dual restores surjectivity for reflexive spaces only -- L^1 is a standard non-reflexive example
- **drop `canonicity_vs_existence`:** V is isomorphic to V^* in finite dimension too, but only after choosing a basis. The point of this node is that V -> V^** needs NO choice, which is what makes 'double dual' a genuine identification and 'dual' merely an isomorphism

## annihilator

- **spec:** U = {0}: U^0 = V^*
- **spec:** U = V: U^0 = {0}
- **spec:** U a hyperplane: U^0 is one-dimensional, spanned by any functional cutting it out
- **drop `finite_dimensionality`:** the dimension identity fails in infinite dimension, where it must be replaced by a statement about codimension
- **drop `no_inner_product_needed`:** U^0 lives in V^*, NOT in V. The analogous object inside V is the orthogonal complement U^perp, which requires an inner product; conflating them is the standard error

## matrix

- **spec:** m = n: a square matrix, the only shape for which eigenvalues, determinant, and trace are defined
- **spec:** n = 1: a column vector; m = 1: a row vector
- **spec:** m = n = 1: a scalar, under which every matrix identity in the capsule degenerates to field arithmetic
- **drop `none_all_hypotheses_essential`:** a definition. The trap is identifying the array with a map without naming the bases -- see matrix_of_linear_map

## matrix_addition_scalar

- **spec:** m = n = 1 recovers F itself
- **spec:** F^{n x 1} = F^n, so column vectors are the n x 1 case
- **drop `equal_shapes`:** adding a 2x3 and a 3x2 matrix is ill-typed, not merely false

## matrix_multiplication

- **spec:** B a column vector: Ab is the combination of the columns of A with coefficients b, the reading that drives column_space
- **spec:** A a row vector and B a column: a 1x1 product, the scalar a^T b
- **spec:** A = I: IB = B
- **drop `conformability`:** ill-typed otherwise
- **drop `commutativity_is_absent`:** see matrix_mult_noncommutative

## matrix_mult_is_composition

- **spec:** S = I: recovers [T] = [T]
- **spec:** all spaces equal with one basis: L(V) is isomorphic to F^{n x n} as an algebra
- **drop `same_middle_basis`:** using different bases for the codomain of T and the domain of S silently inserts a change-of-basis matrix; this is the most common source of wrong products in applied work
- **drop `finite_dimensionality`:** no matrix representation exists otherwise

## matrix_mult_noncommutative

- **spec:** tr(AB) = tr(BA) = 1 nevertheless -- the trace IS cyclic even though the product is not commutative (trace_cyclic)
- **spec:** det(AB) = det(BA) = 0, likewise: determinant is multiplicative hence commutative on products
- **drop `none_all_hypotheses_essential`:** this IS a counterexample node; it exists to block the scalar-algebra habit

## transpose

- **spec:** A symmetric: A^T = A
- **spec:** A a column vector: A^T is a row vector, and x^T y is the standard bilinear pairing
- **spec:** det(A^T) = det(A) -- see determinant_transpose
- **drop `order_reversal`:** assuming (AB)^T = A^T B^T is ill-typed unless the shapes happen to be square, and false even then -- take the noncommuting pair from matrix_mult_noncommutative
- **drop `over_C`:** the transpose is NOT the adjoint over C; A^T A can be singular for a full-rank complex A (take A = [[1, i]]), whereas A^* A cannot. Use conjugate_transpose

## conjugate_transpose

- **spec:** A real: A^* = A^T, which is why the whole statistics-facing half of the capsule can be written with T
- **spec:** A^*A is always positive SEMIdefinite with (A^*A)^* = A^*A -- the fact singular_values rests on
- **drop `conjugation`:** with A = [[1, i]] (1x2), A^T A = [[1, i],[i, -1]] has determinant 0 and is singular, while A^* A = [[1, -i],[i, 1]] is positive semidefinite of rank 1. Dropping the conjugate destroys positive semidefiniteness, hence the SVD and every least-squares argument over C

## identity_matrix

- **spec:** I represents the identity operator in any basis -- one of very few matrices that is basis-independent
- **spec:** det I = 1 and tr I_n = n
- **drop `none_all_hypotheses_essential`:** a definition

## invertible_matrix

- **spec:** n = 1: A = [a] is invertible iff a != 0
- **spec:** A diagonal: invertible iff no diagonal entry is 0, with the reciprocals on the diagonal
- **drop `squareness`:** a 2x3 matrix of rank 2 has a right inverse but no left inverse; the two one-sided inverses are not unique either
- **drop `order_reversal`:** (AB)^{-1} = A^{-1}B^{-1} is false whenever A and B do not commute

## one_sided_inverse_square

- **spec:** n = 1: ab = 1 in a field gives ba = 1 by commutativity
- **drop `squareness`:** for A in F^{2x3} and B in F^{3x2} one can have AB = I_2 with BA != I_3 -- BA has rank at most 2 < 3, so it cannot be I_3
- **drop `finite_dimensionality`:** on F[t] the shift pair LR = I, RL != I is the standing counterexample (see invertible_operator)
- **drop `F_a_field`:** over the ring Z, A = [2] has no inverse at all, though over the module-theoretic analogue one-sidedness can behave worse

## elementary_row_operation

- **spec:** R3 with c = 0 is the identity operation, harmless but useless
- **spec:** R1 is expressible via three R3's and one R2 over any field, so the swap is redundant in principle
- **drop `nonzero_scalar_in_R2`:** multiplying a row by 0 destroys information irreversibly, changes the row space, and can turn a nonsingular matrix singular
- **drop `distinct_rows_in_R3`:** r_i -> r_i + c r_i is R2 with factor (1 + c), which is NOT invertible when c = -1 -- allowing i = j would break reversibility

## elementary_matrix

- **spec:** E for R2 with factor c has inverse the R2 matrix with factor c^{-1}
- **spec:** E for R3 with factor c has inverse the R3 matrix with factor -c
- **spec:** E for R1 is its own inverse
- **drop `invertibility_of_each_operation`:** an 'operation' multiplying a row by 0 has a singular E and generates no equivalence relation

## row_equivalence

- **spec:** E = I: A ~_r A
- **drop `column_space_is_NOT_preserved`:** A = [[1],[1]] and its RREF [[1],[0]] have different column spaces (the diagonal line versus the x-axis in F^2). What IS preserved is the DIMENSION of the column space and WHICH columns are pivot columns -- this distinction is the whole subtlety of row_rank_equals_column_rank
- **drop `invertibility_of_E`:** a singular E gives a relation that is not symmetric

## row_echelon_form

- **spec:** A invertible: its RREF is I
- **spec:** A = 0: already in RREF with no pivots
- **spec:** the number of pivots is the same for EVERY echelon form of A -- this is what matrix_rank is counting
- **drop `none_all_hypotheses_essential`:** a definition; the substantive claim is uniqueness, stated separately

## rref_uniqueness

- **spec:** A invertible: rref(A) = I, giving one clause of invertibility_equivalences
- **spec:** A a single nonzero row: rref(A) has leading 1 in the first nonzero column
- **drop `reducedness`:** non-reduced echelon forms are NOT unique: [[1,2],[0,1]] and [[1,0],[0,1]] are both REF for the same matrix. Only the RREF is canonical
- **drop `F_a_field`:** over Z one cannot scale a pivot to 1; the canonical form is instead Hermite (or Smith) normal form -- see smith_normal_form_boundary

## gaussian_elimination

- **spec:** A invertible: applying the same operations to [A | I] yields [I | A^{-1}]
- **spec:** A singular: elimination halts with a zero row, exhibiting a dependence
- **drop `exact_arithmetic`:** in floating point, elimination WITHOUT pivoting is unstable: the 2x2 system with a tiny pivot epsilon loses all accuracy. See lu_pivoting_regime. This capsule's statements are all exact-arithmetic statements
- **drop `F_a_field`:** over Z the scaling step is unavailable

## pivot_columns

- **spec:** A invertible: every column is a pivot column
- **spec:** A = [[1,2],[2,4]]: one pivot, col(A) is spanned by (1,2)^T, and the second column is free
- **drop `using_A_not_its_RREF`:** the RREF's pivot columns span a DIFFERENT subspace: for A = [[1],[1]], rref(A) = [[1],[0]] and col(rref A) is the x-axis, not the diagonal. The index set transfers; the columns do not. This is the single most common elimination error

## row_space

- **spec:** row(A) = col(A^T), which is why every row statement has a transposed column counterpart
- **drop `none_all_hypotheses_essential`:** a definition; the substance is its invariance under row_equivalence and its equality of dimension with col(A)

## column_space

- **spec:** A a single column: col(A) is the line through it
- **spec:** A invertible n x n: col(A) = F^n
- **drop `none_all_hypotheses_essential`:** a definition. The trap is that column space is NOT preserved by row operations (see row_equivalence)

## null_space

- **spec:** A invertible: null(A) = {0}
- **spec:** dim null(A) = n - rank A by rank_nullity, so the free columns count the dimension
- **drop `none_all_hypotheses_essential`:** a definition

## left_null_space

- **spec:** A of full row rank: the left null space is {0}, and Ax = b is solvable for EVERY b
- **spec:** each left null vector y gives a consistency condition y^T b = 0 on b for Ax = b to be solvable
- **drop `none_all_hypotheses_essential`:** a definition

## four_subspaces

- **spec:** A square invertible: r = n, both null spaces trivial, both row and column space all of F^n
- **spec:** A = 0: r = 0, null(A) = F^n and null(A^T) = F^m
- **drop `orthogonality_is_not_part_of_this`:** over F_2 the vector (1,1) satisfies x^T x = 0, so 'orthogonal complement' is degenerate and null(A) need not complement row(A) in the orthogonal sense. The DIMENSIONS are still right. Orthogonality genuinely requires R or C -- this is exactly why adjoint_kernel_image is a separate node with field_scope real_or_complex

## row_rank_equals_column_rank

- **spec:** A a column vector: both ranks are 1 unless A = 0
- **spec:** A = [[1,2],[2,4]]: rank 1 both ways, though row(A) is spanned by (1,2) in F^2 and col(A) by (1,2)^T in F^2 -- here they coincide only because A is symmetric
- **drop `F_a_field`:** over a commutative ring the notion of rank splits into several inequivalent ones (McCoy rank, determinantal rank) and this equality can fail
- **drop `the_spaces_are_not_equal`:** for A = [[1,1],[0,0]], row(A) is spanned by (1,1) while col(A) is spanned by (1,0)^T -- equal dimension, different subspaces

## matrix_rank

- **spec:** rank A = 0 iff A = 0
- **spec:** rank A = min(m,n): full rank
- **spec:** rank of a rank-one matrix uv^T is 1 for nonzero u, v
- **drop `the_field`:** rank is FIELD-DEPENDENT for a matrix with entries in a subfield: [[1,1],[1,1]] has rank 1 over Q and over F_2; but consider [[1,1],[1,-1]] -- rank 2 over Q, rank 1 over F_2 since -1 = 1 there. Always state the field
- **drop `exact_arithmetic`:** numerically, rank is decided by a singular-value threshold, not by exact vanishing (condition_number)

## rank_inequalities

- **spec:** B invertible: rank(AB) = rank A -- multiplying by an invertible matrix never changes rank, the fact behind similarity invariance
- **spec:** A = B = I_n: Sylvester gives n >= n + n - n, tight
- **spec:** A, B nonzero with AB = 0 (the pair from matrix_mult_noncommutative squared): rank(AB) = 0 while both factors have rank 1, and Sylvester gives 0 >= 1 + 1 - 2 = 0, again tight
- **drop `upper_bound_is_not_equality`:** rank(AB) < min(rank A, rank B) happens whenever col(B) meets null(A) nontrivially: A = [[1,0],[0,0]], B = [[0,0],[0,1]] both have rank 1 and AB = 0
- **drop `conformability`:** otherwise ill-typed

## invertibility_equivalences

- **spec:** n = 1: [a] invertible iff a != 0 iff det != 0 iff 0 is not the eigenvalue a
- **spec:** A diagonal: all clauses reduce to 'no zero on the diagonal'
- **drop `squareness`:** for rectangular A the clauses split apart: full column rank gives injectivity and a left inverse only; full row rank gives surjectivity and a right inverse only; no clause gives two-sided invertibility
- **drop `finite_dimensionality`:** the operator analogue fails on F[t] -- see one_sided_inverse_square
- **drop `F_a_field`:** over Z, A = [[2]] has det 2 != 0 but no inverse IN Z. The clause 'det != 0 implies invertible' needs the determinant to be a UNIT, which over a field is automatic and over a ring is not

## linear_system

- **spec:** b = 0: the solution set is null(A), a genuine subspace
- **spec:** A invertible: a unique solution x = A^{-1}b
- **spec:** rank A = m < n: consistent for every b, with an (n - m)-dimensional family of solutions
- **drop `consistency`:** if b is not in col(A) there is NO solution; least_squares then replaces the equation by minimising ||Ax - b||, which always has a solution
- **drop `affine_not_linear`:** treating the solution set as a subspace leads to the false claim that a sum of two solutions is a solution -- it solves Ax = 2b

## lu_factorisation

- **spec:** A symmetric positive definite: L can be taken with U = L^T scaled, which is cholesky_factorisation
- **spec:** A already upper triangular: L = I
- **drop `nonvanishing_leading_minors`:** A = [[0,1],[1,0]] admits NO unpivoted LU: the first pivot is 0. Yet it is perfectly invertible -- existence of LU is strictly stronger than invertibility, which is precisely why P is needed
- **drop `exact_arithmetic`:** even when LU exists, a tiny pivot makes it numerically useless (lu_pivoting_regime)

## lu_pivoting_regime

- **spec:** A symmetric positive definite: all leading minors are positive (psd_characterisations), so no pivoting is needed for existence OR stability -- the reason Cholesky needs no pivoting
- **spec:** A strictly diagonally dominant: likewise pivot-free
- **drop `nonzero_leading_minors`:** [[0,1],[1,0]] again: invertible, no unpivoted LU
- **drop `exactness_versus_stability`:** A = [[1e-20, 1],[1, 1]] HAS an unpivoted LU in exact arithmetic, but computing it in double precision returns a factorisation whose product is nowhere near A. Existence and usability are different questions

## block_matrix

- **spec:** block diagonal: the product is block diagonal with the blocks multiplied separately
- **spec:** block upper triangular: det is the product of the diagonal blocks' determinants
- **drop `block_commutativity`:** the scalar 2x2 determinant formula ad - bc becomes AD - CB or AD - BC or ... none of which is generally right: det[[A,B],[C,D]] = det(AD - CB) requires C and D to COMMUTE. The correct general statement uses the schur_complement
- **drop `conformability`:** ill-typed otherwise

## schur_complement

- **spec:** A = [a] a 1x1 scalar: M/A = D - cb/a, the ordinary elimination step
- **spec:** C = B^T and M symmetric: the positive-definiteness criterion, which is exactly how conditional covariance matrices in statistics are shown to be PSD
- **drop `invertibility_of_A`:** if A is singular the Schur complement is undefined; a generalised Schur complement using the pseudoinverse recovers part of the theory (see moore_penrose_pseudoinverse)

## trace

- **spec:** tr(I_n) = n -- which over F_p can be 0, a genuine trap in finite characteristic
- **spec:** tr of a projection equals its rank (hat_matrix), the identity behind residual degrees of freedom
- **drop `squareness`:** undefined otherwise
- **drop `characteristic`:** over F_p, tr(I_p) = p = 0, so 'the trace of a rank-r projection is r' must be read mod p

## trace_cyclic

- **spec:** P^{-1}(AP) and (AP)P^{-1} = A: the similarity invariance is the cyclic identity applied once
- **spec:** tr(xy^T) = y^T x for column vectors: the rank-one case, used constantly in matrix calculus
- **drop `cyclic_not_arbitrary`:** tr(ABC) = tr(ACB) is FALSE in general. Take A = I and the noncommuting B, C of matrix_mult_noncommutative: tr(BC) = 1 while tr(CB) = 1 here, but with a third factor the identity genuinely breaks -- only CYCLIC rotations are valid
- **drop `conformability`:** otherwise ill-typed

## triangular_matrix

- **spec:** diagonal matrices commute with each other -- one of the few commuting families
- **spec:** the eigenvalues of a triangular matrix are exactly its diagonal entries, read off char_poly_roots_are_eigenvalues with determinant_triangular
- **drop `triangularity_is_basis_dependent`:** every matrix over C is SIMILAR to a triangular one (schur_triangularisation), so triangularity says nothing about the operator -- only about the basis chosen. Contrast diagonalisable, which IS a property of the operator
- **drop `upper_times_lower`:** the product of an upper and a LOWER triangular matrix is generally neither

## matrix_of_linear_map

- **spec:** V = W = F^n with standard bases: [T] is the matrix A with T(x) = Ax
- **spec:** T = I with B != C: [I]_{C<-B} is the change-of-basis matrix, which is generally NOT the identity matrix
- **drop `finite_dimensionality`:** no matrix exists otherwise
- **drop `the_bases_being_recorded`:** the SAME operator has different matrices in different bases; conversely the same matrix represents different operators. Dropping the subscripts is how sign and transposition errors enter

## change_of_basis

- **spec:** B = B': P = I and the formula is trivial
- **spec:** T diagonalisable: some P makes [T]_{B'} diagonal, which IS diagonalisable
- **drop `invertibility_of_P`:** a non-basis 'B'' gives a singular P and no conjugation formula
- **drop `vectors_versus_operators`:** vectors transform by P and operator matrices by P^{-1}(.)P. Applying the vector rule to an operator (or vice versa) is the standard covariance/contravariance error

## similarity

- **spec:** P a permutation matrix: similarity by simultaneous row and column permutation
- **spec:** A diagonalisable: A is similar to a diagonal matrix
- **drop `invertibility_of_P`:** with singular P the relation is neither symmetric nor transitive
- **drop `similarity_versus_congruence`:** P^{-1}AP and P^T A P agree only when P is ORTHOGONAL. Similarity preserves eigenvalues; congruence preserves only inertia. Confusing them is the standard quadratic-form error -- see congruence

## permutation_sign

- **spec:** n = 2: S_2 = {id, swap} with signs +1 and -1
- **spec:** a cycle of length k has sign (-1)^{k-1}
- **spec:** over a field of characteristic 2, +1 = -1 and sgn is trivial -- which is why the determinant over F_2 is the PERMANENT
- **drop `well_definedness_of_parity`:** if parity were decomposition-dependent, sgn would not exist and the alternating condition could not be expressed
- **drop `characteristic_two`:** over F_2 the alternating condition 'D = 0 when two columns are equal' is strictly stronger than 'D changes sign under a swap', because -1 = 1 makes the latter vacuous. This is why multilinear_alternating_form is defined by the VANISHING condition, not the sign-change condition

## multilinear_alternating_form

- **spec:** n = 1: the multilinear alternating forms on F^1 are exactly the scalar multiples of the identity, D(a) = ca
- **spec:** n = 2: D([a,c],[b,d]) = ad - bc up to a scalar
- **drop `the_vanishing_definition`:** over F_2, 'D changes sign under a swap' is satisfied by the PERMANENT (which never changes sign, and -1 = 1), yet the permanent is not the determinant. The vanishing definition excludes it
- **drop `multilinearity`:** a form that is merely additive in each slot, without homogeneity, does not pin down D even with alternation

## determinant

- **spec:** n = 1: det[a] = a
- **spec:** n = 2: det = ad - bc
- **spec:** n = 3: the six-term Sarrus expansion -- valid ONLY for n = 3 and not a general pattern
- **drop `squareness`:** there is no determinant of a rectangular matrix; the nearest analogues are the Gram determinant det(A^TA) and the singular values
- **drop `commutativity_of_F`:** over a noncommutative division ring no function with these properties exists (the Dieudonne determinant lands in an abelianisation instead)

## determinant_existence_uniqueness

- **spec:** n = 2: uniqueness forces D = ad - bc
- **spec:** dropping the normalisation D(I) = 1 leaves a ONE-DIMENSIONAL space of alternating forms, all scalar multiples of det -- normalisation is what selects one
- **drop `the_normalisation`:** without D(I) = 1, D = 0 also qualifies and uniqueness fails outright
- **drop `alternation`:** without it, many multilinear forms exist (the permanent among them)

## leibniz_formula

- **spec:** n = 2: two terms, ad - bc
- **spec:** n = 3: six terms
- **spec:** A triangular: only sigma = id contributes a nonzero product (determinant_triangular)
- **drop `none_all_hypotheses_essential`:** an identity for square A over any field

## determinant_row_operations

- **spec:** A with two equal rows: repeated R3 produces a zero row, so det = 0
- **spec:** A with a zero row: det = 0 by R2 with c = 0
- **drop `R3_requires_distinct_rows`:** r_i -> r_i + c r_i is R2 in disguise and DOES change det by (1+c); the i != j condition in elementary_row_operation is what makes R3 determinant-preserving
- **drop `R2_scales_ONE_row`:** scaling the whole matrix by c scales det by c^n, not by c -- det(cA) = c^n det(A) is the single most common determinant error

## determinant_triangular

- **spec:** A = I: det = 1, recovering the normalisation
- **spec:** combined with determinant_row_operations, this is the O(n^3) algorithm: eliminate to triangular, multiply the diagonal, correct for swaps and scalings
- **drop `triangularity`:** a general matrix's determinant is NOT the product of its diagonal: [[0,1],[1,0]] has diagonal product 0 but determinant -1
- **drop `block_version`:** for a BLOCK triangular matrix det is the product of the DIAGONAL BLOCKS' determinants -- but only when the off-diagonal block is on one side; see schur_complement for the general case

## determinant_transpose

- **spec:** A symmetric: the statement is trivially true
- **spec:** the reason 'det A != 0 iff the ROWS are independent' and 'iff the COLUMNS are independent' are the same criterion
- **drop `none_all_hypotheses_essential`:** true for every square matrix over every field. Over a noncommutative ring it fails, which is one reason determinants are a commutative-algebra notion

## determinant_multiplicative

- **spec:** B = A^{-1}: det(A)det(A^{-1}) = 1, so det(A^{-1}) = 1/det(A)
- **spec:** B = P^{-1}, A = PA': recovers determinant_similarity_invariant
- **spec:** det(A^k) = (det A)^k
- **drop `squareness_and_equal_size`:** for rectangular factors both sides are undefined; the Cauchy-Binet formula is the correct generalisation and is NOT a product of determinants
- **drop `addition_has_no_analogue`:** det(A+B) != det A + det B, and there is no useful formula

## determinant_invertible_iff

- **spec:** n = 1: [a] invertible iff a != 0
- **spec:** A triangular: invertible iff no diagonal entry is 0, combining this with determinant_triangular
- **drop `F_a_field`:** over Z, det[[2]] = 2 != 0 but [[2]] has no inverse with integer entries. The correct ring statement requires det to be a unit
- **drop `exact_arithmetic`:** in floating point, det A != 0 is not a usable invertibility test: a matrix with det = 10^{-300} may be perfectly well conditioned and one with det = 1 may be numerically singular. Use the condition number

## laplace_expansion

- **spec:** n = 2 along the first row: det = a(d) - b(c)
- **spec:** A with a row of mostly zeros: expanding along it is efficient -- the one case where cofactor expansion beats elimination
- **spec:** expanding along a row with a DIFFERENT row's cofactors gives 0, which is the identity behind the adjugate
- **drop `indexing_from_one`:** 0-based indexing negates every cofactor sign
- **drop `cost`:** recursive cofactor expansion costs O(n!) -- the same disaster as Leibniz. It is a structural tool, not an algorithm

## adjugate

- **spec:** n = 2: adj([[a,b],[c,d]]) = [[d,-b],[-c,a]], the familiar swap-and-negate rule
- **spec:** A singular: A adj(A) = 0, and adj(A) has rank at most 1 when rank A = n-1
- **spec:** over Z: adj(A) has INTEGER entries, so A^{-1} is integral exactly when det A = +-1 -- the ring statement determinant_invertible_iff needs
- **drop `the_transpose`:** omitting it gives the cofactor matrix, for which the identity is false already at n = 2 unless the matrix is symmetric
- **drop `cost`:** computing A^{-1} via the adjugate costs O(n!) or at best O(n^4); elimination costs O(n^3)

## cramers_rule

- **spec:** n = 2: x_1 = (b_1 d - b_2 b)/det, the two-equation formula from school algebra
- **spec:** over Z with det A = +-1: the solution is automatically integral
- **drop `invertibility`:** for singular A the formula divides by zero; a consistent singular system has infinitely many solutions and Cramer says nothing about them
- **drop `cost`:** n+1 determinants, so O(n * n^3) at best against O(n^3) for elimination -- Cramer is exponentially worse if the determinants are computed by expansion

## determinant_similarity_invariant

- **spec:** P orthogonal: det(P) = +-1, so det is also a CONGRUENCE invariant in that special case
- **spec:** but for general congruence det(P^TAP) = det(P)^2 det(A), which is NOT invariant -- only its SIGN is (see sylvester_law_of_inertia)
- **drop `similarity_versus_congruence`:** under congruence the determinant scales by det(P)^2 > 0 over R. So congruence preserves the SIGN of det but not its value -- which is exactly the one-dimensional shadow of Sylvester's law

## determinant_rank_minors

- **spec:** r = 1: rank >= 1 iff some entry is nonzero
- **spec:** r = n = m: rank n iff det A != 0, recovering determinant_invertible_iff
- **spec:** the leading principal minors version is Sylvester's criterion for positive definiteness (psd_characterisations) -- but that needs the LEADING PRINCIPAL minors, which is a strictly stronger condition than 'some minor'
- **drop `all_minors_versus_leading_ones`:** A = [[0,0],[0,-1]] has a nonzero leading... no: its leading 1x1 minor is 0 while it has a nonzero 2x2... take A = [[0,1],[1,0]]: both leading principal minors are 0 and -1, so 'leading minors nonzero' fails, yet rank A = 2. Only ALL minors, not the leading ones, characterise rank
- **drop `cost`:** there are C(m,r)C(n,r) minors -- this is a characterisation, never an algorithm

## determinant_volume

- **spec:** n = 1: |det[a]| = |a|, the length scaling
- **spec:** n = 2: |ad - bc| is the area of the parallelogram spanned by the columns
- **spec:** A orthogonal: |det A| = 1, so rigid motions preserve volume -- see orthogonal_matrix
- **spec:** A singular: det = 0 and the image lies in a proper subspace, of volume 0
- **drop `the_field_being_R`:** over C the analogue involves |det A|^2 as the real 2n-dimensional volume factor, not |det A|
- **drop `the_existence_of_volume`:** the measure-theoretic input is genuinely external; this node is the capsule's clearest example of a result whose INTUITION is standard and whose FOUNDATION is cited

## vandermonde_determinant

- **spec:** n = 2: det[[1,x_1],[1,x_2]] = x_2 - x_1
- **spec:** n = 3 at x = (1,2,3): det = (2-1)(3-1)(3-2) = 2
- **spec:** two equal nodes: a repeated row, so det = 0 -- consistent with the product having a zero factor
- **drop `distinctness_of_the_nodes`:** with a repeated node the matrix is singular, which is exactly the statement that polynomial interpolation at repeated points is not uniquely solvable (one needs derivative data -- Hermite interpolation)

## eigenvalue

- **spec:** lambda = 0 is an eigenvalue iff T is not injective, i.e. iff ker T != {0}
- **spec:** T = lambda I: every nonzero vector is an eigenvector
- **spec:** a projection has eigenvalues in {0,1}; a reflection in {1,-1} (when char F != 2)
- **drop `v_nonzero`:** without it every scalar would be an eigenvalue of every operator, and the notion would be empty
- **drop `the_field`:** the real rotation [[0,-1],[1,0]] has NO real eigenvalue but two complex ones (+-i). Eigenvalues are field-relative, which is why eigenvalue_existence_closed carries the algebraically_closed_field hypothesis
- **drop `squareness`:** a rectangular matrix has no eigenvalues; the correct analogue is singular_values

## eigenspace

- **spec:** lambda not an eigenvalue: E_lambda = {0}, dimension 0
- **spec:** T = lambda I: E_lambda = V
- **drop `including_zero`:** the eigenvectors alone do not form a subspace (they miss 0), which is why every statement about 'the space of eigenvectors' must mean E_lambda
- **drop `distinct_lambdas`:** E_lambda ∩ E_mu = {0} for lambda != mu, since a nonzero common element would give lambda v = mu v

## characteristic_polynomial

- **spec:** n = 1: p(t) = t - a
- **spec:** n = 2: p(t) = t^2 - tr(A) t + det(A)
- **spec:** A triangular: p(t) = prod_i (t - A_{ii}), by determinant_triangular
- **drop `the_sign_convention`:** under det(A - tI) the polynomial is (-1)^n p_A, with the same roots but different coefficient signs -- see characteristic_polynomial_convention
- **drop `does_not_determine_similarity`:** [[1,1],[0,1]] and I_2 share p(t) = (t-1)^2 but are not similar. The characteristic polynomial is an invariant, not a complete one (similar_invariants)

## char_poly_roots_are_eigenvalues

- **spec:** A triangular: the eigenvalues are exactly the diagonal entries
- **spec:** n = 2: the eigenvalues are the roots of t^2 - tr(A)t + det(A), so they sum to tr(A) and multiply to det(A)
- **drop `finite_dimensionality`:** the determinant does not exist for an operator on an infinite-dimensional space; spectral theory there is not polynomial
- **drop `the_field`:** p_A may have NO root in F (the real rotation), in which case A has no eigenvalue over F even though p_A exists and has degree n

## char_poly_coefficients

- **spec:** n = 2: p(t) = t^2 - (l_1 + l_2)t + l_1 l_2
- **spec:** A = [[0,-1],[1,0]] over R: tr = 0 and det = 1, and indeed the complex eigenvalues +-i sum to 0 and multiply to 1 -- the COEFFICIENT identities hold over R even though the eigenvalues do not live there
- **drop `splitting_of_p_A`:** over R the rotation above has no eigenvalues, so 'the sum of the eigenvalues' is literally undefined -- yet tr A = 0 is still a fact about A. The coefficient statement is field-independent; the eigenvalue reading is not
- **drop `algebraic_multiplicity`:** counting eigenvalues without multiplicity breaks both identities: [[1,1],[0,1]] has one distinct eigenvalue 1 but tr = 2

## eigenvalue_existence_closed

- **spec:** V = C^n: every complex square matrix has a complex eigenvalue
- **spec:** dim V = 1: T is multiplication by a scalar, which IS the eigenvalue
- **drop `algebraic_closedness`:** the real rotation [[0,-1],[1,0]] has no real eigenvalue. Every real operator on an ODD-dimensional space does have one (p_T has odd degree, hence a real root by the intermediate value theorem) -- so the failure is specifically an even-dimensional real phenomenon
- **drop `finite_dimensionality`:** the right shift on the space of sequences has no eigenvalue at all: Rx = lambda x forces x = 0. This is an infinite-dimensional operator over C, so algebraic closedness does not save it
- **drop `nonzero_V`:** on V = {0} there are no nonzero vectors, hence no eigenvectors

## distinct_eigenvalues_independent

- **spec:** k = 2: two eigenvectors for distinct eigenvalues cannot be proportional, since a proportional pair would satisfy both eigen-equations
- **spec:** k = n: n eigenvectors for n distinct eigenvalues form a basis, giving distinct_eigenvalues_diagonalisable
- **drop `distinctness`:** two eigenvectors for the SAME eigenvalue can certainly be dependent -- any two elements of a one-dimensional eigenspace are
- **drop `nonzero_eigenvectors`:** the zero vector satisfies every eigen-equation and would make any list dependent

## algebraic_geometric_multiplicity

- **spec:** A diagonalisable: geom = alg for every eigenvalue (diagonalisability_criterion)
- **spec:** A = [[1,1],[0,1]]: alg(1) = 2, geom(1) = 1 -- the minimal defective example
- **spec:** lambda a SIMPLE root (alg = 1): then geom = 1 forced, so simple eigenvalues never cause defectiveness
- **drop `the_inequality_is_strict_in_general`:** the Jordan block above; the deficiency alg - geom counts the number of Jordan blocks beyond the first
- **drop `the_reverse_inequality_is_false`:** geom > alg never happens, but assuming geom = alg is exactly the diagonalisability assumption

## diagonalisable

- **spec:** D itself is diagonalisable with P = I
- **spec:** any matrix with n distinct eigenvalues in F (distinct_eigenvalues_diagonalisable)
- **spec:** every real symmetric matrix, with P ORTHOGONAL (spectral_theorem_symmetric) -- a much stronger conclusion
- **drop `existence_of_a_full_eigenbasis`:** [[1,1],[0,1]] is not diagonalisable over ANY field
- **drop `the_field`:** [[0,-1],[1,0]] is not diagonalisable over R (no eigenvalues) but IS over C. Diagonalisability is field-relative
- **drop `similarity_versus_orthogonal_similarity`:** P is merely invertible here. Requiring P orthogonal is a strictly stronger property, available exactly for normal matrices

## diagonalisability_criterion

- **spec:** n distinct eigenvalues: every alg = 1 forces geom = 1, so diagonalisable
- **spec:** T = lambda I: one eigenvalue with alg = geom = n
- **drop `splitting`:** [[0,-1],[1,0]] over R: geom = alg vacuously (no eigenvalues) but p_T does not split, and it is not diagonalisable. So the multiplicity condition alone is insufficient
- **drop `multiplicity_equality`:** [[1,1],[0,1]]: p splits completely, but geom(1) = 1 < 2 = alg(1). So splitting alone is insufficient. The two counterexamples together show the conditions are independent

## distinct_eigenvalues_diagonalisable

- **spec:** n = 2 with tr^2 != 4 det over R: two distinct real roots, so diagonalisable
- **spec:** generic matrices have distinct eigenvalues, which is why diagonalisability is 'typical' -- but not robust, since the defective matrices are exactly where numerical eigenvector computation becomes ill-conditioned
- **drop `necessity_fails`:** I_n has one eigenvalue repeated n times and is diagonal. The converse is false and assuming it is the standard error
- **drop `eigenvalues_in_F`:** [[0,-1],[1,0]] has two distinct eigenvalues +-i, but not in R, and it is not diagonalisable over R

## non_diagonalisable_counterexample

- **spec:** J^k = [[1,k],[0,1]], which grows LINEARLY even though the only eigenvalue has modulus 1 -- the practical consequence of defectiveness
- **spec:** J is similar to no diagonal matrix, though it shares its characteristic polynomial with I_2
- **drop `none_all_hypotheses_essential`:** this IS the counterexample node. It witnesses: the converse of distinct_eigenvalues_diagonalisable, the multiplicity clause of diagonalisability_criterion, the incompleteness of p_A as a similarity invariant, and the necessity of (t-lambda) appearing to the first power in minimal_polynomial_diagonalisable

## minimal_polynomial

- **spec:** T = lambda I: m_T = t - lambda, of degree 1, while p_T = (t - lambda)^n
- **spec:** J = [[1,1],[0,1]]: m_J = (t-1)^2 = p_J
- **spec:** m_T and p_T always have the SAME ROOTS, but with possibly different multiplicities
- **drop `finite_dimensionality`:** on an infinite-dimensional space an operator need not satisfy any polynomial -- the annihilator can be {0} and there is no minimal polynomial
- **drop `monicity_and_principality`:** without the PID structure of F[t] there would be no single generator, hence no 'the' minimal polynomial

## cayley_hamilton

- **spec:** n = 1: p(t) = t - a and p(A) = A - aI = 0
- **spec:** n = 2: A^2 - tr(A) A + det(A) I = 0 -- the identity used to compute A^{-1} = (tr(A) I - A)/det(A) and every 2x2 matrix power
- **spec:** A diagonalisable: immediate, since p_A kills each eigenvector
- **drop `the_ill_typed_pseudo_proof`:** 'substitute t = A into det(tI - A)' is not a proof: det(tI - A) is computed in F[t] with t a SCALAR indeterminate, and substituting a matrix for a scalar inside a determinant is undefined. The adjugate argument is needed precisely because the shortcut is invalid
- **drop `squareness`:** no characteristic polynomial otherwise

## minimal_polynomial_diagonalisable

- **spec:** T a projection: T^2 = T so m_T divides t^2 - t = t(t-1), squarefree -- every projection is diagonalisable
- **spec:** T an involution with char F != 2: m_T divides t^2 - 1 = (t-1)(t+1), squarefree -- diagonalisable
- **spec:** J = [[1,1],[0,1]]: m_J = (t-1)^2, not squarefree -- not diagonalisable
- **drop `squarefreeness`:** the Jordan block above
- **drop `splitting`:** the real rotation has m_T = t^2 + 1, squarefree but not split over R -- not diagonalisable over R, diagonalisable over C
- **drop `characteristic_two`:** an involution over F_2 has m_T dividing t^2 - 1 = (t-1)^2, which is NOT squarefree there. Indeed [[1,1],[0,1]] over F_2 is an involution and is not diagonalisable -- the char_not_2 subtlety is real

## invariant_subspace

- **spec:** {0} and V are always invariant
- **spec:** every eigenspace E_lambda is invariant
- **spec:** ker p(T) and im p(T) are invariant for any polynomial p, since they commute with T
- **spec:** U^perp is T-invariant when U is and T is SELF-ADJOINT -- the induction step of spectral_theorem_symmetric
- **drop `invariance_of_the_complement`:** for a general T, U invariant does NOT make a complement invariant: for J = [[1,1],[0,1]], the x-axis is invariant but no complementary line is. This is exactly why J fails to decompose and hence fails to diagonalise
- **drop `self_adjointness_for_the_orthogonal_complement`:** U^perp is T-invariant when U is only if T^* preserves... precisely, U T-invariant implies U^perp T^*-invariant. For self-adjoint T these coincide, which is the whole mechanism of the spectral theorem

## schur_triangularisation

- **spec:** A normal: the triangular factor is forced to be DIAGONAL, giving spectral_theorem_normal
- **spec:** A real with real spectrum: Q can be taken real orthogonal (the real Schur form); with complex spectrum the real Schur form has 2x2 blocks
- **drop `algebraic_closedness`:** over R, [[0,-1],[1,0]] is not triangularisable at all -- a triangular real matrix has its diagonal as real eigenvalues, and this one has none
- **drop `triangular_is_not_diagonal`:** Schur does NOT diagonalise: the strictly upper part is generally nonzero and carries the defectiveness

## nilpotent_operator

- **spec:** N = 0: nilpotent with k_0 = 1
- **spec:** the strictly upper triangular shift on F^n: k_0 = n, the extreme case
- **spec:** N = J - I for the Jordan block J: nilpotent of index 2
- **drop `nilpotence_versus_zero_spectrum`:** over a NON-algebraically-closed field an operator can have empty spectrum without being nilpotent -- the real rotation has no real eigenvalue and is invertible, hence not nilpotent. 'Only eigenvalue 0' characterises nilpotence only when p splits
- **drop `finite_dimensionality`:** on F[t] the differentiation operator is locally nilpotent (every element is killed by some power) but no single power annihilates everything

## generalised_eigenspace

- **spec:** T diagonalisable: G_lambda = E_lambda for every lambda -- the two multiplicities agree
- **spec:** J = [[1,1],[0,1]]: E_1 is one-dimensional but G_1 = F^2, of dimension 2 = alg(1)
- **spec:** (T - lambda I) restricted to G_lambda is NILPOTENT, which is the content primary_decomposition exploits
- **drop `the_exponent`:** using exponent 1 gives E_lambda, which is too small; the whole point is to take a high enough power to capture the full algebraic multiplicity
- **drop `finite_dimensionality`:** the chain need not stabilise otherwise

## primary_decomposition

- **spec:** T diagonalisable: every N_lambda = 0 and the decomposition is into eigenspaces
- **spec:** T nilpotent: one generalised eigenspace G_0 = V, with D = 0
- **spec:** refining each nilpotent part into cyclic blocks gives jordan_normal_form -- the step NOT taken in this release
- **drop `splitting`:** over R the rotation has no eigenvalues, so no generalised eigenspaces and no decomposition. The RATIONAL canonical form is the field-independent substitute and is out of scope
- **drop `commutativity_of_D_and_N`:** without requiring DN = ND the decomposition into a diagonalisable plus a nilpotent part is NOT unique -- any matrix can be written as a sum of a diagonalisable and a nilpotent one in many ways

## jordan_normal_form

- **spec:** all blocks 1x1: the diagonalisable case
- **spec:** one block of size n: the cyclic (non-derogatory) case, where m_T = p_T
- **spec:** the number of blocks for lambda is geom(lambda); their sizes sum to alg(lambda)
- **drop `algebraic_closedness`:** no Jordan form over R for the rotation matrix; the real analogue uses 2x2 rotation blocks
- **drop `numerical_instability`:** the Jordan form is DISCONTINUOUS in the entries: an arbitrarily small perturbation of a Jordan block has distinct eigenvalues and is diagonalisable. It is therefore never computed numerically -- Schur form is used instead

## similar_invariants

- **spec:** A diagonalisable: the eigenvalue multiset IS complete among diagonalisable matrices
- **spec:** p and m together are complete for n <= 3, but not for n >= 4
- **drop `completeness_fails_for_p_alone`:** I_2 and [[1,1],[0,1]] share p(t) = (t-1)^2 and are not similar (they have different ranks of A - I)
- **drop `completeness_fails_for_p_and_m_together_at_n_equals_4`:** diag(J_2(0), J_2(0)) and diag(J_2(0), 0, 0) both have p = t^4 and m = t^2, yet have different numbers of blocks (2 versus 3) and hence different ranks -- they are not similar. This is the standard witness that p and m do not suffice
- **drop `these_are_not_congruence_invariants`:** trace and determinant are NOT preserved by congruence; only the inertia is (sylvester_law_of_inertia)

## inner_product

- **spec:** F^n with <x,y> = sum_i x_i conj(y_i) = y^* x: the standard inner product
- **spec:** weighted: <x,y> = y^* W x for a positive definite W (positive_definite) -- every inner product on F^n is of this form
- **spec:** continuous functions on [0,1] with <f,g> = integral f conj(g): infinite-dimensional, and the setting of Fourier series
- **drop `positive_definiteness`:** the Minkowski form <x,y> = x_1y_1 - x_2y_2 on R^2 is symmetric and bilinear but indefinite: the null vector (1,1) has <x,x> = 0 without being 0. There is then no norm, no Cauchy-Schwarz in the usual direction, and no orthogonal decomposition -- Lorentzian geometry, not Euclidean
- **drop `conjugate_symmetry`:** the plain bilinear form sum x_i y_i on C^2 gives <(1,i),(1,i)> = 1 - 1 = 0 with the vector nonzero (see inner_product_convention)
- **drop `the_field`:** over F_2, x^T x = sum x_i^2 = sum x_i, so (1,1) is 'self-orthogonal'. No ordered field, no positivity, no inner product

## inner_product_space

- **spec:** R^n with the dot product: Euclidean n-space
- **spec:** C^n with y^*x: unitary space
- **spec:** F^{m x n} with <A,B> = tr(B^*A): the Frobenius inner product, which is what matrix_norms uses
- **drop `completeness_is_NOT_assumed`:** finite-dimensional inner product spaces are automatically complete; infinite-dimensional ones need not be, and every theorem here that uses orthogonal_decomposition fails for a non-closed subspace of an incomplete space. That is the Hilbert-space boundary this capsule does not cross

## induced_norm

- **spec:** F^n standard: ||x|| = sqrt(sum |x_i|^2), the Euclidean norm
- **spec:** ||av|| = |a| ||v|| uses |a|, not a -- over C this matters: ||iv|| = ||v||
- **drop `positive_definiteness`:** for an indefinite form sqrt(<v,v>) is not even real for some v (Minkowski again)
- **drop `not_every_norm_is_induced`:** the 1-norm and infinity-norm on R^2 are genuine norms but come from NO inner product -- they fail the parallelogram_law, which is exactly the characterisation

## cauchy_schwarz

- **spec:** u = v: equality, both sides ||v||^2
- **spec:** v = 0: both sides 0, equality with the pair trivially dependent
- **spec:** F^n standard: (sum |x_i y_i|)^2 <= (sum |x_i|^2)(sum |y_i|^2), the classical inequality
- **spec:** random variables with <X,Y> = E[XY]: |E[XY]| <= sqrt(E[X^2]E[Y^2]), hence |corr| <= 1
- **drop `positive_definiteness`:** for the Minkowski form on R^2 the inequality REVERSES on timelike vectors -- the reverse Cauchy-Schwarz inequality of special relativity. So it is definiteness, not bilinearity, that gives the direction
- **drop `the_proof_needs_only_nonnegativity`:** positive SEMI-definiteness suffices for the inequality; strict definiteness is needed only for the equality clause

## triangle_inequality

- **spec:** v = -u: ||0|| = 0 <= 2||u||, strict unless u = 0 -- the multiple -1 is negative, so no equality, illustrating the sharper condition
- **spec:** the reverse triangle inequality | ||u|| - ||v|| | <= ||u - v|| follows by substitution
- **drop `the_equality_condition`:** u and v = -u are dependent (so Cauchy-Schwarz is tight) but ||u + v|| = 0 < 2||u||. Dependence gives equality in Cauchy-Schwarz, not in the triangle inequality

## parallelogram_law

- **spec:** v = 0: reduces to 2||u||^2 = 2||u||^2
- **spec:** u perp v: combined with pythagorean_theorem it gives ||u+v|| = ||u-v||
- **drop `the_norm_being_induced`:** on R^2 with the 1-norm, take u = (1,0), v = (0,1): ||u+v||_1 = 2 and ||u-v||_1 = 2, so the left side is 8, while the right side is 2 + 2 = 4. The 1-norm comes from no inner product -- this is the standard witness

## polarisation_identity

- **spec:** u = v over R: (||2u||^2 - 0)/4 = ||u||^2, correct
- **spec:** the real formula applied to a COMPLEX inner product recovers only Re<u,v>, which is why the complex version needs four terms
- **drop `characteristic_not_two`:** over F_2 the map q(x) = x^T A x satisfies q(u+v) = q(u) + q(v) (all cross terms double to zero), so q is ADDITIVE and carries none of the bilinear information. Symmetric and alternating forms become indistinguishable -- the single sharpest consequence of char 2 in this capsule
- **drop `using_the_real_formula_over_C`:** gives Re<u,v> only, losing the imaginary part entirely

## orthogonality

- **spec:** the standard basis of F^n is orthonormal
- **spec:** in R^2, (1,1) perp (1,-1)
- **spec:** uncorrelated centred random variables are orthogonal under <X,Y> = E[XY]
- **drop `positive_definiteness`:** over F_2 with the form sum x_iy_i, the vector (1,1) satisfies <x,x> = 1+1 = 0, so it is orthogonal to ITSELF while nonzero. Every orthogonality argument -- independence of orthogonal sets, orthogonal decomposition, projection -- collapses. This is why the four_subspaces theorem is stated over any field in DIMENSIONS only, with orthogonality deferred to adjoint_kernel_image

## pythagorean_theorem

- **spec:** extends by induction to any finite orthogonal family: ||sum v_i||^2 = sum ||v_i||^2
- **spec:** with u = P_U v and v - P_U v, it gives ||v||^2 = ||P_U v||^2 + ||v - P_U v||^2 -- the decomposition behind best_approximation and behind the ANOVA sum-of-squares identity
- **drop `the_complex_converse`:** in C^1 take u = 1 and v = i: <u,v> = conj(i) = -i, so Re<u,v> = 0 and ||u+v||^2 = |1+i|^2 = 2 = 1 + 1. Pythagoras holds, yet <u,v> != 0 so the vectors are NOT orthogonal

## orthogonal_implies_independent

- **spec:** an orthonormal set: automatically nonzero, hence independent
- **spec:** n orthonormal vectors in an n-dimensional space therefore form a BASIS with no further argument
- **drop `nonzeroness`:** {0, e_1} is orthogonal and dependent
- **drop `positive_definiteness`:** the proof divides by ||v_j||^2; over a degenerate form a self-orthogonal nonzero vector makes this step fail, and over F_2 the set {(1,1)} is 'orthogonal' to itself

## orthonormal_basis

- **spec:** the standard basis of F^n
- **spec:** existence in every finite-dimensional inner product space is gram_schmidt
- **spec:** the Fourier basis on L^2[0,2pi]: the infinite-dimensional analogue, where 'basis' means a convergent series, not a finite combination
- **drop `orthonormality`:** for a general basis, v = sum <v,b_i> b_i is FALSE -- the correct coefficients come from the inverse Gram matrix (gram_matrix), and the discrepancy is exactly the failure of orthogonality
- **drop `finite_dimensionality`:** an orthonormal SET need not be a basis in infinite dimension even if maximal -- the algebraic and topological notions of basis diverge (see linear_combination)

## gram_schmidt

- **spec:** k = 1: e_1 = v_1/||v_1||
- **spec:** the v's already orthogonal: Gram-Schmidt only normalises
- **spec:** recording the coefficients gives exactly qr_factorisation, with R upper triangular because e_j uses only v_1..v_j
- **drop `independence`:** applied to a dependent list, some w_j = 0 and the normalisation divides by zero. The MODIFIED algorithm skips such j and produces an orthonormal basis of the span -- but the span-matching property is then lost for that index
- **drop `numerical_stability`:** CLASSICAL Gram-Schmidt loses orthogonality catastrophically in floating point; MODIFIED Gram-Schmidt (subtract projections one at a time, updating as you go) is far better, and Householder reflections better still. This is a numerical-analysis fact, CITED, not established here

## bessel_inequality

- **spec:** k = 1: |<v,e>|^2 <= ||v||^2, which is Cauchy-Schwarz for a unit vector
- **spec:** (e_i) a BASIS: equality, which is parseval_identity
- **spec:** the deficit ||v||^2 - sum |<v,e_i>|^2 is exactly the squared distance from v to the span
- **drop `orthonormality`:** for a general independent set the sum of squared coefficients can EXCEED ||v||^2 -- take two nearly-parallel unit vectors in R^2 and v along their common direction
- **drop `equality_requires_a_basis`:** an orthonormal set that misses a direction leaves a strictly positive deficit

## parseval_identity

- **spec:** V = F^n with the standard basis: the identity is the definition of the norm
- **spec:** the Fourier series case: sum |c_n|^2 = (1/2pi) integral |f|^2, the classical Parseval theorem -- infinite-dimensional and CITED
- **drop `spanning`:** for a non-spanning orthonormal set only Bessel's INEQUALITY holds; the deficit is the squared distance to the span
- **drop `completeness_in_infinite_dimension`:** an orthonormal set can be maximal yet fail Parseval in an INCOMPLETE inner product space -- completeness is what upgrades maximal-orthonormal to Parseval, and this capsule does not develop it

## orthogonal_complement

- **spec:** {0}^perp = V and V^perp = {0} (the latter uses positive definiteness)
- **spec:** in R^3, a plane's complement is its normal line
- **spec:** U^perp = null(A^T) when U = col(A) -- this is adjoint_kernel_image
- **drop `positive_definiteness`:** for a degenerate form, V^perp can be nonzero (the radical), and U + U^perp need not be V. Over F_2 with sum x_iy_i, the span of (1,1) is contained in its OWN perp
- **drop `double_perp_needs_finite_dimension`:** U subset (U^perp)^perp always, but equality needs U to be a finite-dimensional (or closed) subspace -- see orthogonal_decomposition

## orthogonal_decomposition

- **spec:** U = {0}: V = {0} (+) V
- **spec:** U = V: V = V (+) {0}
- **spec:** U = col(A) in F^m: gives the least-squares decomposition of b into fitted values plus residual
- **drop `finite_dimensionality_of_U`:** in an incomplete inner product space, a NON-CLOSED infinite-dimensional subspace can have U^perp = {0} while U != V -- then V != U + U^perp and (U^perp)^perp = V != U. The standard witness is the space of finitely-supported sequences inside l^2. In a complete space (Hilbert) closedness of U is the right hypothesis
- **drop `positive_definiteness`:** a degenerate form allows a nonzero vector in U ∩ U^perp

## orthogonal_projection

- **spec:** U a line spanned by unit e: P_U v = <v,e> e, the familiar scalar projection
- **spec:** U = V: P = I; U = {0}: P = 0
- **spec:** I - P_U is the orthogonal projection onto U^perp
- **drop `orthonormality_of_the_basis`:** with a merely independent basis (b_i) of U, sum <v,b_i> b_i is NOT the projection; the correct formula is B(B^*B)^{-1}B^* v, i.e. the hat_matrix, and the discrepancy is the inverse Gram matrix
- **drop `orthogonality_versus_oblique`:** a general idempotent P is an OBLIQUE projection along ker P, which need not be U^perp. Self-adjointness is exactly what makes a projection orthogonal (projection_matrix_characterisation)

## projection_matrix_characterisation

- **spec:** P = I and P = 0: the trivial projections
- **spec:** the hat matrix H = X(X^TX)^{-1}X^T: symmetric and idempotent, hence orthogonal projection onto col(X)
- **spec:** tr P = rank P, since the eigenvalues of such a P are all 0 or 1 -- the identity behind residual degrees of freedom
- **drop `symmetry`:** P = [[1,1],[0,0]] satisfies P^2 = P and is a projection onto the x-axis, but ALONG the line x + y = 0, not along its orthogonal complement. It is oblique: P^T != P. In regression this is the difference between OLS and a general weighted or instrumental-variables fit
- **drop `idempotence`:** a symmetric non-idempotent matrix is not a projection at all

## best_approximation

- **spec:** U = span(e): the closest point on a line, the elementary projection formula
- **spec:** U = col(A): the least-squares problem, giving least_squares
- **drop `finite_dimensionality_or_closedness_of_U`:** for a non-closed subspace the infimum need not be ATTAINED -- there is a nearest-point sequence but no nearest point. The same witness as orthogonal_decomposition (finitely-supported sequences in l^2)
- **drop `the_norm_being_induced`:** in a general normed space the nearest point need not be unique: in R^2 with the infinity-norm, the nearest point on a line to an off-line point can be a whole segment. Uniqueness comes from strict convexity of the Euclidean ball, i.e. from the inner product

## least_squares

- **spec:** A square invertible: the normal equations reduce to Ax = b
- **spec:** A with orthonormal columns: A^TA = I, so x = A^Tb -- the projection coefficients directly
- **spec:** the 3-point regression design used in math-statistics' instance checks
- **drop `full_column_rank`:** if rank A < n the normal equations have a whole affine family of solutions; the minimum-NORM one is A^+b via the pseudoinverse (moore_penrose_pseudoinverse). Collinear predictors in regression are exactly this case
- **drop `conditioning`:** kappa(A^TA) = kappa(A)^2, so forming the normal equations SQUARES the condition number. For an A with kappa = 10^8 the normal equations lose all double precision, while qr_factorisation does not. This is why no serious least-squares solver forms A^TA

## hat_matrix

- **spec:** A a single column a: H = aa^T/(a^Ta), the rank-one projection onto its span
- **spec:** A = I_m: H = I, tr = m
- **spec:** the diagonal entries h_ii are the LEVERAGES in regression, with sum equal to the number of parameters
- **drop `full_column_rank`:** if A is rank deficient, A^TA is singular and H is undefined by this formula. The projection onto col(A) still exists -- use AA^+ with the pseudoinverse
- **drop `orthogonality_needs_symmetry`:** a weighted fit uses H_W = A(A^TW A)^{-1}A^TW, which is idempotent but NOT symmetric: an OBLIQUE projection. Quoting tr H = rank still works, but the Pythagorean decomposition of sums of squares does not

## qr_factorisation

- **spec:** A square invertible: QR with both factors square, and |det A| = prod |R_ii|
- **spec:** A with orthonormal columns already: Q = A, R = I
- **spec:** A^TA = R^TR, so R is the Cholesky factor of the Gram matrix -- the link to cholesky_factorisation
- **drop `full_column_rank`:** a rank-deficient A has no unique QR; column-pivoted QR (AP = QR) is the standard remedy and also reveals the numerical rank
- **drop `why_QR_over_the_normal_equations`:** solving Rx = Q^Tb has condition number kappa(A), while the normal equations have kappa(A)^2. For kappa(A) = 10^8 this is the difference between 8 lost digits and 16

## adjoint_operator

- **spec:** V = W = F^n standard: T^* is A^*
- **spec:** T unitary: T^* = T^{-1}
- **spec:** T self-adjoint: T^* = T
- **drop `orthonormality_of_the_basis`:** in a non-orthonormal basis with Gram matrix G, the adjoint's matrix is G^{-1}A^*G, not A^*. Assuming otherwise is the source of the 'why is my adjoint wrong in a weighted inner product' error
- **drop `finite_dimensionality`:** in infinite dimension the adjoint of an UNBOUNDED operator need not exist on the whole space -- densely defined adjoints and domain issues are the substance of unbounded operator theory, entirely outside this capsule
- **drop `adjoint_versus_dual`:** the dual map T^t: W^* -> V^* needs no inner product and does not conjugate; T^* does both. They correspond under the Riesz identification, which is CONJUGATE-linear over C

## adjoint_kernel_image

- **spec:** A with full column rank: null(A) = {0}, so row(A) = F^n
- **spec:** the consistency condition for Ax = b is exactly b perp null(A^T) -- the Fredholm alternative in finite dimension
- **drop `the_field_being_R_or_C`:** over F_2 the 'orthogonal complement' of the span of (1,1) contains (1,1) itself, so the pair is not complementary. The DIMENSIONS from four_subspaces are still correct; the orthogonality is not. This node is precisely where the capsule's any_field results end and the real_or_complex ones begin
- **drop `finite_dimensionality`:** in infinite dimension one gets ker(T^*) = (im T)^perp with the CLOSURE of the image, so im(T^*) = (ker T)^perp requires closed range

## self_adjoint

- **spec:** orthogonal projections are self-adjoint (projection_matrix_characterisation)
- **spec:** covariance matrices and Gram matrices are real symmetric
- **spec:** a real DIAGONAL matrix is self-adjoint
- **drop `the_complex_criterion_is_complex_only`:** over R, <Av,v> is real for EVERY A, so it cannot detect symmetry. Indeed [[0,-1],[1,0]] has <Av,v> = 0 for all v and is not symmetric. Over C the criterion is genuinely equivalent -- an asymmetry worth remembering
- **drop `complex_symmetric_is_not_Hermitian`:** A^T = A over C is a different, badly behaved class: [[1,i],[i,-1]] is complex symmetric, has p(t) = t^2, and is NILPOTENT -- nothing like a Hermitian matrix

## orthogonal_matrix

- **spec:** rotations and reflections in R^2; det = +1 for rotations, -1 for reflections
- **spec:** permutation matrices are orthogonal
- **spec:** the Q of a QR factorisation has orthonormal COLUMNS but is generally rectangular, so QQ^T is a projection
- **drop `squareness`:** for Q in R^{m x n} with m > n and Q^TQ = I, QQ^T is the projection onto col(Q), not I. Treating a reduced-QR Q as 'orthogonal' in the two-sided sense is a standard error
- **drop `det_pm_one_is_not_sufficient`:** det = +-1 does NOT imply orthogonal: [[1,1],[0,1]] has det 1 and is not orthogonal. Orthogonality is a much stronger, metric condition

## isometry_characterisation

- **spec:** T orthogonal/unitary: the matrix form of the theorem
- **spec:** T a permutation of an orthonormal basis: an isometry
- **drop `linearity`:** the Mazur-Ulam phenomenon aside, a NONLINEAR norm-preserving map need not preserve inner products -- e.g. any norm-preserving bijection of the sphere that is not a rotation
- **drop `finite_dimensionality`:** in infinite dimension T^*T = I (an isometry) does NOT give TT^* = I: the right shift on l^2 is a non-surjective isometry. Surjectivity is an extra hypothesis there, supplied automatically here by injective_surjective_equivalence
- **drop `char_two`:** polarisation fails, so norm-preservation would not recover the form

## normal_matrix

- **spec:** the three named subclasses above
- **spec:** a real ROTATION matrix is orthogonal hence normal, and is unitarily diagonalisable OVER C (eigenvalues e^{+-i theta}) though not over R
- **spec:** a diagonal matrix is normal
- **drop `normality_is_not_automatic`:** [[1,1],[0,1]] has AA^* = [[2,1],[1,1]] and A^*A = [[1,1],[1,2]] -- not equal. It is not normal, and indeed not diagonalisable at all
- **drop `normal_does_not_mean_self_adjoint`:** a unitary matrix is normal with eigenvalues on the unit circle, generally not real
- **drop `sums_and_products_of_normals_need_not_be_normal`:** normality is not preserved by addition or multiplication unless the matrices commute

## self_adjoint_real_eigenvalues

- **spec:** A = [[a,b],[b,d]] real symmetric: discriminant (a-d)^2 + 4b^2 >= 0 always, so both roots are real -- the 2x2 case verified directly
- **spec:** a covariance matrix has real (indeed nonnegative) eigenvalues, which is why PCA's variances are meaningful numbers
- **drop `self_adjointness`:** [[0,-1],[1,0]] is real but NOT symmetric, and its eigenvalues +-i are not real. Symmetry, not realness of the entries, is what forces real eigenvalues
- **drop `over_C_transpose_is_not_enough`:** the complex-symmetric [[1,i],[i,-1]] has A^T = A but eigenvalues both 0 with a defective eigenspace -- it is nilpotent. Hermitian (A^* = A) is the correct hypothesis

## spectral_theorem_symmetric

- **spec:** A diagonal already: Q = I
- **spec:** A = [[2,1],[1,2]]: eigenvalues 3 and 1 with orthonormal eigenvectors (1,1)/sqrt2 and (1,-1)/sqrt2
- **spec:** A a projection: D has only 0s and 1s, recovering projection_matrix_characterisation
- **spec:** A a covariance matrix: this IS the principal component decomposition
- **drop `symmetry`:** [[1,1],[0,1]] is not symmetric and is not diagonalisable at all; [[0,-1],[1,0]] is not symmetric and has no real eigenvalues. Both fail in different ways
- **drop `realness_of_the_field`:** the complex-symmetric [[1,i],[i,-1]] satisfies A^T = A over C and is NOT diagonalisable -- the correct complex hypothesis is Hermitian (spectral_theorem_normal)
- **drop `finite_dimensionality`:** for a self-adjoint operator on an infinite-dimensional Hilbert space there need be no eigenvectors at all (multiplication by x on L^2[0,1]); the spectral theorem becomes a statement about projection-valued measures, entirely outside this capsule

## spectral_theorem_normal

- **spec:** A Hermitian: D is real (self_adjoint_real_eigenvalues), recovering the complex form of spectral_theorem_symmetric
- **spec:** A unitary: D has entries of modulus 1
- **spec:** A skew-Hermitian: D is purely imaginary
- **drop `normality`:** [[1,1],[0,1]] is not normal and not diagonalisable
- **drop `the_field_being_C`:** a real orthogonal rotation is normal and is unitarily diagonalisable over C, but NOT orthogonally diagonalisable over R -- its eigenvalues are not real. Over R the correct statement is the real normal form with 2x2 rotation blocks
- **drop `unitary_versus_merely_invertible`:** a diagonalisable non-normal matrix (e.g. [[1,1],[0,2]]) has A = PDP^{-1} with P invertible but NOT unitary. Normality is exactly the obstruction

## spectral_decomposition

- **spec:** A with distinct eigenvalues: each P_i is a rank-one projection q_iq_i^T
- **spec:** f(t) = t^k: recovers A^k = sum lambda_i^k P_i
- **spec:** f(t) = 1/t on an invertible A: A^{-1} = sum (1/lambda_i) P_i
- **spec:** f(t) = e^t: the matrix exponential in closed form
- **drop `self_adjointness`:** for a general diagonalisable A the spectral projections are OBLIQUE (P_i = v_iw_i^* with w the LEFT eigenvectors) and are not self-adjoint; the resolution of the identity still holds but the geometry is skewed. For a defective A no such decomposition exists at all
- **drop `distinctness_of_the_lambda_i`:** summing over eigenvalues WITH multiplicity would double-count the projections

## rayleigh_quotient

- **spec:** x an eigenvector for lambda: R_A(x) = lambda exactly
- **spec:** A = I: R_A is constantly 1
- **spec:** the range of R_A over all x != 0 is the interval [lambda_min, lambda_max] for self-adjoint A (the numerical range)
- **drop `self_adjointness`:** for a non-self-adjoint A, R_A is complex-valued and its range is a REGION of C (the numerical range / field of values), not an interval. The extremal characterisation fails entirely -- [[0,-1],[1,0]] has R_A identically 0 on real vectors while having no real eigenvalue
- **drop `x_nonzero`:** the quotient is undefined at 0

## courant_fischer

- **spec:** k = 1: lambda_1 = max R_A over the unit sphere, and k = n: lambda_n = min
- **spec:** CAUCHY INTERLACING: deleting a row and the matching column of A gives B with lambda_k(A) >= lambda_k(B) >= lambda_{k+1}(A)
- **spec:** WEYL: |lambda_k(A+E) - lambda_k(A)| <= ||E||_2, so symmetric eigenvalues are perfectly conditioned
- **drop `symmetry`:** for a non-symmetric matrix the eigenvalues are not real, cannot be ordered, and are NOT well-conditioned: a Jordan block perturbed by epsilon in the corner has eigenvalues moving by epsilon^{1/n}. Everything in this node depends on symmetry
- **drop `finite_dimensionality`:** the min-max principle extends to compact self-adjoint operators, but not to general ones

## quadratic_form

- **spec:** n = 1: q(x) = ax^2
- **spec:** A = I: q(x) = ||x||^2
- **spec:** the second-order term of a Taylor expansion, with A the Hessian -- symmetric by equality of mixed partials
- **drop `characteristic_not_two`:** over F_2, q(x) = x_1x_2 comes from A = [[0,1],[0,0]] and from A = [[0,0],[1,0]] and from [[0,1],[1,0]] -- the symmetric representative is not unique, and worse, the polarisation b(x,y) = 2x^TAy = 0 vanishes identically. Quadratic forms in characteristic 2 are a genuinely separate theory
- **drop `symmetry`:** without restricting to symmetric A the representation is never unique in any characteristic

## congruence

- **spec:** P orthogonal: congruence and similarity COINCIDE, which is exactly why spectral_theorem_symmetric can be read either way
- **spec:** P diagonal with entries 1/sqrt(|lambda_i|): brings a diagonalised form to a matrix of +-1s and 0s, the canonical form of sylvester_law_of_inertia
- **drop `congruence_is_not_similarity`:** A = I_2 and B = diag(4,9) = P^T I P with P = diag(2,3) are CONGRUENT but not SIMILAR -- their eigenvalues differ entirely. So eigenvalues are NOT congruence invariants; only their SIGNS are (sylvester_law_of_inertia). Using similarity invariants (trace, determinant, eigenvalues) to compare quadratic forms is the standard error
- **drop `invertibility_of_P`:** a singular P can only degrade the form and gives no equivalence relation

## positive_definite

- **spec:** A = I: positive definite
- **spec:** A = 0: positive semidefinite but not definite
- **spec:** any Gram matrix is PSD, and definite iff the vectors are independent (gram_matrix)
- **spec:** a covariance matrix is PSD, and definite iff no linear combination of the variables is degenerate
- **drop `symmetry`:** for a NON-symmetric A the condition x^TAx > 0 depends only on (A+A^T)/2, so it cannot characterise A. [[1,-3],[3,1]] satisfies x^TAx = ||x||^2 > 0 yet has complex eigenvalues -- 'positive definite' in the eigenvalue sense fails while the quadratic-form condition holds. The two notions agree ONLY for symmetric A, which is why symmetry is built into the definition
- **drop `the_ordered_field`:** over C, x^TAx is complex; the Hermitian form x^*Ax is real exactly when A is Hermitian, and that is the correct complex definition
- **drop `definite_versus_semidefinite`:** diag(1,0) is PSD, singular, and NOT positive definite -- the distinction is exactly invertibility

## psd_characterisations

- **spec:** n = 1: [a] > 0 iff a > 0 iff its one minor is positive
- **spec:** n = 2: A > 0 iff a_{11} > 0 and det A > 0 -- the two leading minors
- **spec:** A a covariance matrix: PSD, definite iff no exact linear relation among the variables
- **drop `leading_versus_all_principal_minors`:** A = diag(0, -1) has leading principal minors 0 and 0 -- neither negative -- yet A is NOT positive semidefinite (x = e_2 gives -1). For SEMIdefiniteness one must check ALL principal minors, including det of the {2} block, which is -1. Sylvester's criterion with LEADING minors characterises DEFINITENESS only
- **drop `symmetry`:** for non-symmetric A the minor criterion says nothing: [[1,-3],[3,1]] has positive leading minors (1 and 10) and complex eigenvalues
- **drop `strictness`:** diag(1,0) has leading minors 1 and 0, so it fails strict Sylvester -- correctly, since it is semidefinite but not definite

## gram_matrix

- **spec:** k = 1: G = [||v_1||^2]
- **spec:** the v_i orthonormal: G = I
- **spec:** A^TA in the normal equations IS a Gram matrix, which is why least_squares has a unique solution exactly under full column rank
- **spec:** det G is the squared volume of the parallelepiped spanned by the v_i -- zero iff they are dependent
- **drop `independence_for_definiteness`:** with a repeated vector G is singular; in regression this is exact collinearity, and near-collinearity makes G nearly singular and the fit ill-conditioned (condition_number)
- **drop `null(A^*A) = null(A) needs the CONJUGATE`:** over C with A^TA instead, A = [[1, i]] gives a singular A^TA despite full rank -- see conjugate_transpose

## cholesky_factorisation

- **spec:** A = I: L = I
- **spec:** n = 1: A = [a] with a > 0 gives L = [sqrt a]
- **spec:** A = R^TR from qr_factorisation applied to the normal equations: the Cholesky factor of A^TA is exactly the R of the QR of A
- **drop `positive_definiteness`:** A = [[0,1],[1,0]] is symmetric, invertible, and INDEFINITE: the algorithm's first step needs sqrt(0) then divides by it. Cholesky failing is in fact the standard NUMERICAL TEST for positive definiteness -- attempt the factorisation and see whether it completes
- **drop `semidefinite_case`:** a singular PSD A has a Cholesky-like factorisation with a zero on the diagonal, but it is no longer unique

## sylvester_law_of_inertia

- **spec:** A positive definite: inertia (n,0,0)
- **spec:** A = diag(1,-1) and B = diag(4,-9): congruent (P = diag(2,3)) with the SAME inertia, though with completely different eigenvalues -- the sharpest illustration of similarity versus congruence
- **spec:** the index n_- is the Morse index of a critical point
- **drop `the_ordered_field`:** over C, diag(1,-1) = P^T I P with P = diag(1, i), so every nondegenerate complex symmetric form is congruent to I and the inertia is meaningless. Ordering is essential
- **drop `eigenvalues_are_not_preserved`:** only their SIGNS are, as the diag(4,-9) example shows. Quoting eigenvalues as form invariants is the standard error
- **drop `symmetry`:** no inertia is defined for a non-symmetric matrix

## simultaneous_diagonalisation

- **spec:** B = I: the congruence case reduces to the ordinary spectral theorem
- **spec:** A, B commuting Hermitian: BOTH theorems apply and give the same answer
- **spec:** the generalised eigenproblem Ax = lambda Bx is exactly the congruence case, and its solutions are the diagonal entries
- **drop `positive_definiteness_of_B`:** A = [[0,1],[1,0]] and B = [[1,0],[0,-1]] are both symmetric with B indefinite, and no congruence diagonalises both. Definiteness of ONE of the pair is essential
- **drop `commutativity_in_the_normal_case`:** the two Pauli-like matrices [[0,1],[1,0]] and [[1,0],[0,-1]] are Hermitian and do NOT commute; no single unitary diagonalises both. This is the linear-algebra core of the uncertainty principle
- **drop `congruence_is_not_similarity`:** the first theorem's P is not orthogonal, so the diagonal entries of P^TAP are NOT the eigenvalues of A -- they are the generalised eigenvalues of (A,B)

## singular_value_decomposition

- **spec:** A symmetric PSD: U = V and the SVD is the eigendecomposition
- **spec:** A orthogonal: Sigma = I
- **spec:** A = uv^*: a single term, sigma_1 = ||u|| ||v||
- **spec:** the geometric reading: every linear map is a rotation, then an axis-aligned scaling, then another rotation
- **drop `uniqueness_fails`:** the singular VALUES are unique, but U and V are not: any repeated singular value allows rotating within its subspace, and even for distinct values each pair (u_i, v_i) can be multiplied by a common unit scalar. Claims of a 'unique SVD' are wrong
- **drop `no_hypothesis_can_be_dropped_because_there_are_none`:** the only requirement is F in {R, C}. Over a general field there is no SVD, because there is no notion of nonnegative square root

## singular_values

- **spec:** A square symmetric PSD: the singular values ARE the eigenvalues
- **spec:** A square symmetric indefinite: sigma_i = |lambda_i| -- the absolute values, so SVD loses sign information the eigendecomposition keeps
- **spec:** A orthogonal: all singular values 1
- **spec:** A = uv^*: one nonzero singular value ||u|| ||v||
- **drop `singular_values_are_not_eigenvalues`:** [[0,1],[0,0]] has both eigenvalues 0 but singular values 1 and 0. A nilpotent matrix can have large singular values -- the two spectra measure different things (spectral_radius versus norm)
- **drop `the_conjugate_matters`:** over C, using A^TA instead of A^*A gives the wrong (possibly negative or complex) values -- see conjugate_transpose

## svd_four_subspaces

- **spec:** A of full column rank: no v's left over, null(A) = {0}
- **spec:** A square invertible: r = n = m and both null spaces are trivial
- **drop `numerical_rank`:** deciding r requires a THRESHOLD on the singular values in floating point; 'rank' is not a computable property of a floating-point matrix, and the SVD makes this explicit (small nonzero sigma) where elimination hides it

## moore_penrose_pseudoinverse

- **spec:** A invertible: A^+ = A^{-1}
- **spec:** A of full column rank: A^+ = (A^*A)^{-1}A^*, the least-squares formula
- **spec:** A of full row rank: A^+ = A^*(AA^*)^{-1}, the minimum-norm solution of an underdetermined system
- **spec:** A = 0: A^+ = 0
- **drop `discontinuity_in_A`:** A^+ is NOT a continuous function of A across a rank change: for A_eps = diag(1, eps), A_eps^+ = diag(1, 1/eps) blows up as eps -> 0, while A_0^+ = diag(1,0). This is the practical reason a truncated (regularised) pseudoinverse is used in practice, and the reason a rank tolerance is unavoidable
- **drop `(AB)^+ != B^+A^+`:** the reversal rule holds for inverses but FAILS for pseudoinverses in general -- a common and silent error

## eckart_young

- **spec:** k = rank A: zero error
- **spec:** k = 0: the error is ||A||_2 = sigma_1, correctly
- **spec:** A = diag(3,2): the best rank-1 approximation is diag(3,0) with spectral error 2
- **drop `the_norm_being_unitarily_invariant`:** under the ENTRYWISE max norm the truncated SVD is NOT optimal -- optimality is specific to unitarily invariant norms, and this is exactly Mirsky's generalisation
- **drop `uniqueness`:** if sigma_k = sigma_{k+1} the optimal A_k is not unique, because the truncation can be taken in different directions within the tied subspace
- **drop `structure_is_not_preserved`:** the truncated SVD of a nonnegative matrix generally has negative entries, and of a sparse matrix is dense. Structured low-rank approximation (NMF, sparse PCA) is a different and much harder problem with no closed form

## matrix_norms

- **spec:** A = I_n: ||I||_2 = 1 but ||I||_F = sqrt(n) -- the norms differ substantially
- **spec:** A of rank 1: the two norms coincide
- **spec:** A unitary: ||A||_2 = 1, ||A||_F = sqrt(n)
- **drop `the_entrywise_max_is_not_submultiplicative`:** max_{ij}|A_{ij}| is a norm but NOT submultiplicative: for A = B = [[1,1],[1,1]], the max norm of AB = [[2,2],[2,2]] is 2 > 1 * 1. Submultiplicativity must be checked, not assumed
- **drop `the_spectral_norm_is_not_from_an_inner_product`:** it fails the parallelogram law, so there is no 'spectral inner product' and no projection theory for it
- **drop `norms_are_not_the_spectral_radius`:** for the nilpotent [[0,1],[0,0]], rho = 0 while ||A||_2 = 1 -- see spectral_radius

## condition_number

- **spec:** A orthogonal: kappa = 1, the best possible -- which is why orthogonal transformations are the building block of stable algorithms
- **spec:** A = diag(1, 1e-10): kappa = 1e10, so about 10 digits are lost
- **spec:** kappa(A^TA) = kappa(A)^2 -- the reason the normal equations are avoided (least_squares)
- **spec:** the Hilbert matrix H_n has kappa growing like e^{3.5n}: catastrophic by n = 12
- **drop `determinant_is_not_conditioning`:** A = 1e-5 * I_{10} has det = 1e-50, vanishingly small, yet kappa = 1 -- perfectly conditioned. Conversely diag(1, 1e-10) has det = 1e-10 and kappa = 1e10. The determinant is scale-sensitive and conditioning is not; the two carry entirely different information. This is the single most important practical point in the node
- **drop `conditioning_is_a_property_of_the_PROBLEM`:** kappa bounds what ANY algorithm can achieve on this data; a backward-stable algorithm achieves it, an unstable one does worse. Conditioning and stability are different notions

## spectral_radius

- **spec:** A normal: rho(A) = ||A||_2
- **spec:** A^k -> 0 if and only if rho(A) < 1 -- the fundamental stability criterion for linear iterations and discrete dynamical systems
- **spec:** A a stochastic matrix: rho(A) = 1, attained at the stationary distribution
- **drop `rho_is_not_a_norm`:** the nilpotent [[0,1],[0,0]] has rho = 0 while A != 0, so rho(A) = 0 does not imply A = 0. It also fails subadditivity: rho(A+B) can exceed rho(A) + rho(B)
- **drop `rho_does_not_bound_finite_powers`:** with J = [[1,1],[0,1]], rho(J) = 1 but ||J^k||_2 grows LINEARLY in k. rho governs only the ASYMPTOTIC growth rate (Gelfand), not any individual power. Transient growth before eventual decay is a real and often decisive phenomenon in non-normal dynamics
- **drop `normality_for_equality`:** for non-normal A the gap ||A||_2 - rho(A) can be arbitrarily large

## infinite_dimensional_boundary

- **spec:** rank_nullity: S is injective (nullity 0) and not surjective -- no finite count relates the dimensions
- **spec:** injective_surjective_equivalence: S injective not surjective; L surjective not injective, both on the SAME space
- **spec:** one_sided_inverse_square: LS = I but SL != I
- **spec:** double_dual: dim V^* > dim V for V = F[t], so evaluation is injective but far from surjective
- **spec:** eigenvalue_existence_closed: S has NO eigenvalue over C
- **spec:** adjoint_operator: an unbounded densely-defined operator has an adjoint only on a proper domain
- **spec:** basis_existence: needs Zorn, hence full AC (basis_existence_general)
- **spec:** orthogonal_decomposition: the finitely-supported sequences U inside l^2 satisfy U^perp = {0} yet U != l^2
- **drop `none_all_hypotheses_essential`:** this node IS the counterexample catalogue

## smith_normal_form_boundary

- **spec:** R = F a field: every module is free, invariant factors are trivial, and the theorem degenerates to 'every vector space has a basis' -- which is why linear algebra over a field is so much simpler
- **spec:** R = F[t] with t acting as T: the invariant factors are the invariant factors of T, the last one being m_T; the primary decomposition into (t - lambda)^k pieces is exactly jordan_normal_form
- **spec:** R = Z: finitely generated abelian groups, and the Smith normal form diag(d_1,...,d_r,0,...) of an integer matrix
- **drop `R_being_a_PID`:** over a non-PID such as Z[x] or F[x,y] the structure theorem fails; modules can be badly behaved and no canonical form exists
- **drop `finite_generation`:** an infinitely generated module over a PID need not decompose (the rationals Q as a Z-module are not a direct sum of cyclics)
