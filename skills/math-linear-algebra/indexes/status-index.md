# Result index by node type (generated)

## primitive

## axiom

## structure
- **field** (vector_spaces) — A commutative ring in which every nonzero element is invertible: (F,+,*,0,1) with 0 != 1
- **vector_space** (vector_spaces) — An abelian group (V,+) with scalar multiplication F x V -> V satisfying distributivity, associativity, and 1v = v
- **space_of_linear_maps** (linear_maps) — L(V,W) is a vector space under pointwise operations; dim L(V,W) = (dim V)(dim W) in finite dimension
- **inner_product** (inner_product) — A positive-definite form on V over R or C, linear in the first slot and conjugate-symmetric, with <v,v> > 0 for v != 0
- **inner_product_space** (inner_product) — A vector space over R or C equipped with an inner product

## notation_convention
- **index_convention** (matrices) — Vectors are columns; A in F^{m x n} has m rows and n columns; indices start at 1; A_{ij} is row i column j
- **transpose_convention** (matrices) — A^T is the transpose, A^* the conjugate transpose; they coincide over R. Every Hermitian result says which it uses
- **inner_product_convention** (inner_product) — The complex inner product is linear in the FIRST argument and conjugate-linear in the second (the mathematician's convention)
- **characteristic_polynomial_convention** (eigentheory) — p_A(t) = det(tI - A), monic. The variant det(A - tI) differs by (-1)^n

## principle_law

## definition
- **subspace** (vector_spaces) — A subset U of V containing 0 and closed under + and scalar multiplication; equivalently a subset that is a vector space under the restricted operations
- **linear_combination** (vector_spaces) — A finite sum sum_{i=1}^k a_i v_i with a_i in F and v_i in V
- **span** (vector_spaces) — span(S) is the set of all finite linear combinations of elements of S: the smallest subspace containing S. span(empty) = {0}
- **linear_independence** (vector_spaces) — (v_i) is independent iff the only finite linear combination of them equal to 0 has all coefficients 0
- **basis** (vector_spaces) — A linearly independent spanning set. Defined without reference to any number, so that dimension can be proved well-defined
- **dimension** (vector_spaces) — dim V is the common cardinality of any basis of V; dim {0} = 0
- **ordered_basis** (vector_spaces) — An ordered basis B = (b_1,...,b_n) gives the coordinate map [.]_B : V -> F^n, a linear bijection
- **sum_of_subspaces** (vector_spaces) — U + W = {u + w : u in U, w in W}, the smallest subspace containing both
- **direct_sum** (vector_spaces) — V = U (+) W iff V = U + W and U ∩ W = {0}; equivalently every v decomposes uniquely as u + w
- **linear_map** (linear_maps) — T: V -> W with T(au + bv) = aT(u) + bT(v) for all a,b in F and u,v in V
- **kernel** (linear_maps) — ker T = {v in V : T(v) = 0}, a subspace of V
- **image_subspace** (linear_maps) — im T = T(V) = {T(v) : v in V}, a subspace of W
- **rank** (linear_maps) — rank T = dim(im T). Defined without the determinant, breaking the rank-determinant cycle
- **nullity** (linear_maps) — nullity T = dim(ker T)
- **linear_isomorphism** (linear_maps) — A bijective linear map; its set-inverse is automatically linear
- **linear_operator** (linear_maps) — A linear map from V to itself; L(V) is an associative algebra under composition
- **invertible_operator** (linear_maps) — T in L(V) with a two-sided inverse in L(V); in finite dimension a one-sided inverse suffices
- **dual_space** (linear_maps) — V^* = L(V, F), the space of linear functionals on V
- **dual_map** (linear_maps) — T^t: W^* -> V^* with T^t(g) = g o T; its matrix in dual bases is the transpose of the matrix of T
- **annihilator** (linear_maps) — U^0 = {f in V^* : f(u) = 0 for all u in U}; dim U + dim U^0 = dim V in finite dimension
- **matrix** (matrices) — A in F^{m x n} is a function {1..m} x {1..n} -> F, written as a rectangular array
- **matrix_addition_scalar** (matrices) — Entrywise operations making F^{m x n} a vector space of dimension mn
- **matrix_multiplication** (matrices) — (AB)_{ij} = sum_k A_{ik} B_{kj}, defined when the inner shapes agree
- **transpose** (matrices) — (A^T)_{ij} = A_{ji}; (AB)^T = B^T A^T and (A^T)^T = A
- **conjugate_transpose** (matrices) — (A^*)_{ij} = conj(A_{ji}); over R it is the transpose. The correct adjoint for the complex inner product
- **identity_matrix** (matrices) — I_n with (I_n)_{ij} = delta_{ij}, the multiplicative identity of F^{n x n}
- **invertible_matrix** (matrices) — A in F^{n x n} with AB = BA = I for some B; the inverse is unique and (AB)^{-1} = B^{-1}A^{-1}
- **elementary_row_operation** (matrices) — Row swap, scaling a row by a nonzero scalar, and adding a multiple of one row to another
- **row_equivalence** (matrices) — A ~_r B iff B = EA for a product E of elementary matrices; preserves the row space and the null space
- **row_echelon_form** (matrices) — Leading entries strictly rightward down the rows, zero rows last; RREF additionally has leading 1s that are the only nonzero entry in their column
- **pivot_columns** (matrices) — Pivot columns of the RREF index a basis of the column space of A; free columns parameterise the null space
- **row_space** (matrices) — The span of the rows of A, a subspace of F^n, invariant under row operations
- **column_space** (matrices) — The span of the columns of A; equals the image of x  maps to  Ax
- **null_space** (matrices) — {x : Ax = 0}, the kernel of x  maps to  Ax
- **left_null_space** (matrices) — {y : A^T y = 0}, the null space of A^T
- **matrix_rank** (matrices) — rank A = dim col(A); equals the number of pivots in any row echelon form of A
- **linear_system** (matrices) — Ax = b is consistent iff b is in col(A); its solution set is x_p + null(A), an affine subspace
- **block_matrix** (matrices) — Partitioned matrices multiply blockwise when the partitions are conformable
- **trace** (matrices) — tr(A) = sum_i A_{ii}, a linear functional on F^{n x n}
- **triangular_matrix** (matrices) — Upper and lower triangular and diagonal matrices; closed under products, invertible iff no diagonal entry is zero
- **similarity** (matrices) — A ~ B iff B = P^{-1} A P for some invertible P; an equivalence relation whose classes are the operators up to choice of basis
- **permutation_sign** (determinants) — S_n and the sign homomorphism sgn: S_n -> {+1,-1}, well-defined by the parity of any decomposition into transpositions
- **multilinear_alternating_form** (determinants) — D: (F^n)^n -> F linear in each column and zero whenever two columns are equal
- **determinant** (determinants) — det is the unique multilinear alternating function of the columns with det(I) = 1. Defined without eigenvalues, breaking the det-eigenvalue cycle
- **eigenvalue** (eigentheory) — lambda in F is an eigenvalue of T if Tv = lambda v for some v != 0; such a v is an eigenvector. Defined without the determinant
- **eigenspace** (eigentheory) — E_lambda = ker(T - lambda I), consisting of 0 and the eigenvectors for lambda
- **characteristic_polynomial** (eigentheory) — p_A(t) = det(tI - A), monic of degree n and a similarity invariant
- **algebraic_geometric_multiplicity** (eigentheory) — Algebraic multiplicity is the multiplicity as a root of p_A, geometric is dim E_lambda; always geometric <= algebraic
- **diagonalisable** (eigentheory) — T is diagonalisable if some basis of V consists of eigenvectors, equivalently A = PDP^{-1} with D diagonal
- **minimal_polynomial** (eigentheory) — The monic generator m_T of the ideal of polynomials annihilating T; it divides every annihilating polynomial
- **invariant_subspace** (eigentheory) — U with T(U) contained in U; the restriction is an operator on U and its minimal polynomial divides m_T
- **nilpotent_operator** (eigentheory) — N with N^k = 0 for some k; its only eigenvalue is 0 and N^{dim V} = 0
- **generalised_eigenspace** (eigentheory) — G_lambda = ker((T - lambda I)^{dim V}); its dimension is the algebraic multiplicity of lambda
- **induced_norm** (inner_product) — The norm ||v|| = sqrt(<v,v>): positive definite, absolutely homogeneous, and subadditive
- **orthogonality** (inner_product) — u perp v iff <u,v> = 0; a set is orthogonal if its elements are pairwise orthogonal
- **orthonormal_basis** (inner_product) — Pairwise orthogonal unit vectors; an orthonormal basis gives coordinates by <v, e_i> with no matrix inversion
- **orthogonal_complement** (inner_product) — U^perp = {v : <v,u> = 0 for all u in U}, a subspace; U^perp = (span U)^perp
- **adjoint_operator** (inner_product) — The unique T^* with <Tv, w> = <v, T^*w>; its matrix in orthonormal bases is the conjugate transpose
- **self_adjoint** (spectral) — T = T^*; over R, A = A^T. The class for which the real spectral theorem holds
- **orthogonal_matrix** (spectral) — Q^TQ = I over R and U^*U = I over C; equivalently the columns are orthonormal and the map preserves the inner product
- **normal_matrix** (spectral) — AA^* = A^*A; contains the self-adjoint, skew-adjoint, and unitary matrices
- **rayleigh_quotient** (spectral) — R(x) = <Ax,x>/<x,x> for x != 0. A DEFINITION only: that its extrema over the unit sphere are the extreme eigenvalues is proved downstream (see courant_fischer), which is what keeps it usable inside the spectral theorem's own proof
- **quadratic_form** (spectral) — q(x) = x^T A x with A symmetric; the symmetric A is unique when the characteristic is not 2
- **congruence** (spectral) — A ~_c B iff B = P^T A P with P invertible: the change-of-variable relation for quadratic forms, distinct from similarity
- **positive_definite** (spectral) — Symmetric A with x^T A x > 0 for every x != 0; positive semidefinite if the inequality is not strict
- **singular_values** (spectral) — The nonnegative square roots of the eigenvalues of A^*A; rank A is the number of nonzero singular values
- **matrix_norms** (spectral) — A||_2 = sigma_1 and ||A||_F = sqrt(tr(A^*A)) = root-sum-of-squares of the singular values; both submultiplicative
- **spectral_radius** (spectral) — rho(A) = max of the absolute values of the eigenvalues; rho(A) <= ||A|| for every submultiplicative norm, with equality for normal A in the spectral norm

## construction
- **quotient_space** (vector_spaces) — V/U with (v + U) + (w + U) = (v + w) + U and a(v + U) = av + U; well-defined because U is a subspace
- **elementary_matrix** (matrices) — Each elementary row operation is left multiplication by an invertible elementary matrix
- **lu_factorisation** (matrices) — A = LU with L unit lower triangular and U upper triangular when no pivoting is required; PA = LU in general
- **schur_complement** (matrices) — For M = [[A,B],[C,D]] with A invertible, the Schur complement is D - C A^{-1} B, and det M = det A * det(D - CA^{-1}B)
- **matrix_of_linear_map** (matrices) — [T]_{C<-B} has as its j-th column the C-coordinates of T(b_j), which makes [S o T] = [S][T]
- **adjugate** (determinants) — adj(A)_{ij} = (-1)^{i+j} M_{ji}; A adj(A) = adj(A) A = det(A) I, so A^{-1} = adj(A)/det(A) when det A != 0
- **orthogonal_projection** (inner_product) — P_U v = sum_i <v, e_i> e_i for an orthonormal basis (e_i) of U, independent of which orthonormal basis is chosen
- **hat_matrix** (inner_product) — H is the orthogonal projection onto col(A): symmetric, idempotent, of rank equal to rank A, with tr(H) = rank A
- **qr_factorisation** (inner_product) — A = QR with Q having orthonormal columns and R upper triangular, from Gram-Schmidt on the columns; solves least squares without forming A^TA
- **gram_matrix** (spectral) — G_{ij} = <v_i, v_j> is positive semidefinite, positive definite iff the v_i are independent, and rank G = dim span(v_i)
- **cholesky_factorisation** (spectral) — A positive definite real symmetric A factors uniquely as A = LL^T with L lower triangular with positive diagonal
- **moore_penrose_pseudoinverse** (spectral) — A^+ = V Sigma^+ U^*, the unique matrix satisfying the four Penrose conditions; A^+b is the minimum-norm least-squares solution

## proposition
- **vector_space_basic_consequences** (vector_spaces) — 0v = 0, (-1)v = -v, a0 = 0, and av = 0 implies a = 0 or v = 0
- **subspace_criterion** (vector_spaces) — Nonempty U is a subspace iff au + bw is in U for all a,b in F and u,w in U
- **subspace_intersection** (vector_spaces) — An arbitrary intersection of subspaces is a subspace; a union of two subspaces is a subspace only if one contains the other
- **span_is_smallest_subspace** (vector_spaces) — span(S) is a subspace and is contained in every subspace containing S
- **dimension_of_subspace** (vector_spaces) — If U is a subspace of finite-dimensional V then dim U <= dim V, with equality iff U = V
- **basis_unique_representation** (vector_spaces) — B is a basis iff every v in V is a unique finite linear combination of elements of B
- **quotient_dimension** (vector_spaces) — For finite-dimensional V and a subspace U, dim(V/U) = dim V - dim U
- **injective_iff_trivial_kernel** (linear_maps) — A linear map is injective exactly when its kernel is the zero subspace
- **composition_of_linear_maps** (linear_maps) — The composite of linear maps is linear; composition is associative and bilinear over L
- **one_sided_inverse_square** (matrices) — For square A over a field, AB = I implies BA = I. Fails for non-square A and in infinite dimension
- **trace_cyclic** (matrices) — tr(AB) = tr(BA), hence tr(P^{-1}AP) = tr(A): trace is a property of the operator, not the basis
- **determinant_row_operations** (determinants) — A row swap negates det; scaling a row by c scales det by c; adding a multiple of a row leaves det unchanged
- **determinant_triangular** (determinants) — The determinant of a triangular matrix is the product of its diagonal entries
- **determinant_volume** (determinants) — Over R, the absolute value of det A is the factor by which A scales n-dimensional volume, and its sign records orientation
- **char_poly_coefficients** (eigentheory) — p_A(t) = t^n - tr(A)t^{n-1} + ... + (-1)^n det(A); when p_A splits, tr is the sum and det the product of the eigenvalues with multiplicity
- **similar_invariants** (eigentheory) — Similar matrices share rank, trace, determinant, characteristic polynomial, minimal polynomial, and eigenvalue multiplicities; the characteristic polynomial alone does not determine similarity
- **pythagorean_theorem** (inner_product) — If u perp v then ||u+v||^2 = ||u||^2 + ||v||^2; over C the converse needs only the real part of <u,v> to vanish
- **orthogonal_implies_independent** (inner_product) — Pairwise orthogonality plus nonvanishing forces linear independence
- **bessel_inequality** (inner_product) — The sum of the squared coefficients over any orthonormal set is at most ||v||^2
- **self_adjoint_real_eigenvalues** (spectral) — Every eigenvalue of a self-adjoint operator is real, and eigenvectors for distinct eigenvalues are orthogonal

## theorem
- **basis_existence_finite** (vector_spaces) — A finite spanning set contains a basis and every independent set extends to a basis. Choice-free
- **basis_existence_general** (vector_spaces) — Every vector space has a basis. Equivalent to the axiom of choice over ZF
- **dimension_well_defined** (vector_spaces) — Any two bases of a finitely generated vector space have the same number of elements
- **coordinate_isomorphism** (vector_spaces) — dim V = n implies V is isomorphic to F^n via coordinates; the isomorphism depends on the chosen basis
- **dimension_formula_sum** (vector_spaces) — dim(U + W) = dim U + dim W - dim(U ∩ W) for finite-dimensional U and W
- **linear_map_determined_by_basis** (linear_maps) — Given a basis (b_i) of V and any (w_i) in W there is exactly one linear T with T(b_i) = w_i
- **rank_nullity** (linear_maps) — For T: V -> W with V finite-dimensional, dim V = rank T + nullity T
- **first_isomorphism_theorem** (linear_maps) — V/ker T is isomorphic to im T via v + ker T  maps to  T(v)
- **dual_basis** (linear_maps) — A basis (b_1,...,b_n) of finite-dimensional V yields a basis (b_1^*,...,b_n^*) of V^* with b_i^*(b_j) = delta_{ij}; hence dim V^* = dim V
- **double_dual** (linear_maps) — Evaluation v  maps to  (f  maps to  f(v)) is injective always and an isomorphism when dim V is finite. Basis-independent, unlike V to V^*
- **matrix_mult_is_composition** (matrices) — [S o T]_{D<-B} = [S]_{D<-C} [T]_{C<-B}; associativity of the matrix product follows from associativity of composition
- **rref_uniqueness** (matrices) — Every matrix is row equivalent to exactly one matrix in reduced row echelon form
- **four_subspaces** (matrices) — row(A) and null(A) live in F^n with dimensions r and n-r; col(A) and null(A^T) in F^m with dimensions r and m-r. Orthogonality of the pairs needs an inner product
- **row_rank_equals_column_rank** (matrices) — dim row(A) = dim col(A) = rank A, over any field
- **rank_inequalities** (matrices) — rank(AB) <= min(rank A, rank B); rank(A+B) <= rank A + rank B; Sylvester: rank(AB) >= rank A + rank B - n
- **invertibility_equivalences** (matrices) — For square A: invertible iff rank n iff null(A) = {0} iff RREF is I iff a product of elementary matrices iff det A != 0 iff 0 is not an eigenvalue
- **change_of_basis** (matrices) — [T]_{B'} = P^{-1} [T]_B P where P is the change-of-basis matrix
- **determinant_existence_uniqueness** (determinants) — There is exactly one normalised alternating multilinear form on the columns of F^{n x n}
- **leibniz_formula** (determinants) — det A = sum_{sigma in S_n} sgn(sigma) prod_i A_{i,sigma(i)}. A theorem here, not the definition
- **determinant_transpose** (determinants) — The determinant is unchanged by transposition, so every row statement has a column counterpart
- **determinant_multiplicative** (determinants) — The determinant is multiplicative over any field
- **determinant_invertible_iff** (determinants) — A square matrix over a field is invertible exactly when its determinant is nonzero; then det(A^{-1}) = 1/det(A)
- **laplace_expansion** (determinants) — det A = sum_j (-1)^{i+j} A_{ij} M_{ij} along any row i, and likewise along any column
- **determinant_rank_minors** (determinants) — rank A is the largest r such that some r x r minor of A is nonzero. A theorem, not the definition of rank
- **char_poly_roots_are_eigenvalues** (eigentheory) — lambda is an eigenvalue of A iff p_A(lambda) = 0. The theorem linking the two independent definitions
- **eigenvalue_existence_closed** (eigentheory) — Over an algebraically closed field every operator on a nonzero finite-dimensional space has an eigenvalue. Fails over R
- **distinct_eigenvalues_independent** (eigentheory) — Eigenvectors belonging to pairwise distinct eigenvalues are linearly independent
- **diagonalisability_criterion** (eigentheory) — T is diagonalisable iff p_T splits and every eigenvalue's geometric multiplicity equals its algebraic multiplicity, equivalently V is the direct sum of the eigenspaces
- **cayley_hamilton** (eigentheory) — Every square matrix satisfies its own characteristic polynomial: p_A(A) = 0
- **minimal_polynomial_diagonalisable** (eigentheory) — T is diagonalisable iff m_T splits into distinct linear factors over F
- **schur_triangularisation** (eigentheory) — Over C every square matrix is unitarily similar to an upper triangular matrix: A = QTQ^*
- **primary_decomposition** (eigentheory) — If p_T splits, V is the direct sum of the generalised eigenspaces and T acts on each as lambda I plus a nilpotent
- **jordan_normal_form** (eigentheory) — Over an algebraically closed field every operator has a basis in which its matrix is block diagonal with Jordan blocks, unique up to block order. STATED, not proved in Release 0.1
- **cauchy_schwarz** (inner_product) — The absolute value of <u,v> is at most ||u|| ||v||, with equality iff u and v are linearly dependent
- **parseval_identity** (inner_product) — For an orthonormal BASIS, ||v||^2 equals the sum of the squared coefficients, and the inner product is the coefficient inner product
- **orthogonal_decomposition** (inner_product) — For a finite-dimensional subspace U, V = U (+) U^perp and (U^perp)^perp = U
- **projection_matrix_characterisation** (inner_product) — Over R, P represents orthogonal projection onto col(P) exactly when P is idempotent and symmetric. The result math-statistics uses for the hat matrix
- **best_approximation** (inner_product) — P_U v is the unique closest point of U to v: ||v - P_U v|| < ||v - u|| for every other u in U
- **least_squares** (inner_product) — A minimiser of ||Ax - b|| is exactly a solution of A^T A x = A^T b, unique iff A has full column rank, and then x = (A^TA)^{-1}A^Tb
- **adjoint_kernel_image** (inner_product) — The four fundamental subspaces form two orthogonal pairs: null(A) = row(A)^perp and null(A^T) = col(A)^perp
- **isometry_characterisation** (spectral) — For a linear map on a finite-dimensional inner product space, preserving the norm, preserving the inner product, and U^*U = I are equivalent
- **spectral_theorem_symmetric** (spectral) — A real symmetric A has an orthonormal basis of eigenvectors: A = Q D Q^T with Q orthogonal and D real diagonal
- **spectral_theorem_normal** (spectral) — Over C, A is unitarily diagonalisable iff A is normal: A = U D U^*
- **courant_fischer** (spectral) — Each eigenvalue is a min-max of the Rayleigh quotient over subspaces of fixed dimension; yields eigenvalue interlacing under rank-one and submatrix perturbation
- **psd_characterisations** (spectral) — For real symmetric A: positive definite iff all eigenvalues positive iff all leading principal minors positive (Sylvester's criterion) iff A = B^TB with B of full column rank iff A has a Cholesky factorisation
- **sylvester_law_of_inertia** (spectral) — The numbers of positive, negative, and zero eigenvalues of a real symmetric matrix are invariant under congruence; the signature classifies real quadratic forms
- **simultaneous_diagonalisation** (spectral) — Two real symmetric matrices with one positive definite are simultaneously diagonalisable by congruence; two normal matrices are simultaneously unitarily diagonalisable iff they commute
- **singular_value_decomposition** (spectral) — Every A in F^{m x n} factors as A = U Sigma V^* with U and V unitary and Sigma diagonal with nonnegative nonincreasing entries
- **eckart_young** (spectral) — The best rank-k approximation to A in the spectral and Frobenius norms is the truncated SVD, with errors sigma_{k+1} and the root-sum-of-squares of the discarded singular values
- **smith_normal_form_boundary** (boundary) — Over a PID every finitely generated module is a direct sum of cyclic modules; the common home of the Jordan and Smith normal forms. STATED, out of scope

## corollary
- **injective_surjective_equivalence** (linear_maps) — If dim V = dim W < infinity then T: V -> W is injective iff surjective iff bijective. Fails without finite-dimensionality
- **cramers_rule** (determinants) — For invertible A the unique solution of Ax = b has x_i = det(A_i)/det(A), where A_i replaces column i of A by b
- **determinant_similarity_invariant** (determinants) — det(P^{-1}AP) = det(A), so det is a property of the operator
- **distinct_eigenvalues_diagonalisable** (eigentheory) — An n x n matrix with n distinct eigenvalues in F is diagonalisable. Sufficient, not necessary
- **triangle_inequality** (inner_product) — u + v|| <= ||u|| + ||v||, a consequence of Cauchy-Schwarz
- **spectral_decomposition** (spectral) — A self-adjoint A equals the sum over distinct eigenvalues of lambda_i P_i with P_i the orthogonal projections onto the eigenspaces, P_iP_j = 0 and sum P_i = I
- **svd_four_subspaces** (spectral) — The first r columns of U and V give orthonormal bases of col(A) and row(A); the remaining columns give null(A^T) and null(A)

## mathematical_identity

