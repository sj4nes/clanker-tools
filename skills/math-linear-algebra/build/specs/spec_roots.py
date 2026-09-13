"""Cited bridge roots, the field structure, the four first-class hypotheses,
and the four notation conventions.  Roots are thin stubs: statement, citation,
lean_status: cited."""
from nodespec import N, ROOT

# --- cited from the math-* stack --------------------------------------------
ROOT("set", "math-sets-functions-cardinality:set",
     "A set in ZFC; the underlying carrier of every structure in this capsule.")
ROOT("function", "math-sets-functions-cardinality:function",
     "A function f: X -> Y, i.e. a relation that is total and single-valued.")
ROOT("bijection", "math-sets-functions-cardinality:bijection",
     "A function that is both injective and surjective; equivalently one with a two-sided inverse.")
ROOT("equivalence_relation", "math-sets-functions-cardinality:equivalence_relation",
     "A reflexive, symmetric, transitive relation; its classes partition the underlying set.")
ROOT("quotient_set", "math-sets-functions-cardinality:quotient_set",
     "X/~, the set of equivalence classes, with the canonical projection x -> [x] and the well-definedness criterion for maps out of it.")
ROOT("finite_set", "math-sets-functions-cardinality:finite_set",
     "A set equinumerous with {1,...,n} for some n in N; n is well-defined (pigeonhole).")
ROOT("indexed_family", "math-sets-functions-cardinality:indexed_family",
     "A family (x_i)_{i in I}: a function from an index set I. Allows infinite index sets while only finite subsums are ever formed.")
ROOT("zorns_lemma", "math-sets-functions-cardinality:zorn_lemma",
     "Every nonempty partially ordered set in which every chain has an upper bound contains a maximal element.")
ROOT("axiom_of_choice", "math-sets-functions-cardinality:axiom_of_choice",
     "Every family of nonempty sets admits a choice function; equivalent over ZF to Zorn's lemma and to the well-ordering theorem.")
ROOT("induction_principle", "math-logic-and-proof:weak_induction",
     "Weak and strong induction on N, with the well-ordering principle as the equivalent minimal-counterexample form.")
ROOT("real_number", "math-number-systems:real_number",
     "R is a complete ordered field: an ordered field in which every nonempty bounded-above subset has a least upper bound.")
ROOT("compactness_cited", "math-real-analysis:heine_borel",
     "A subset of R^n is compact iff it is closed and bounded; in particular the unit sphere {x : ||x|| = 1} is compact.")
ROOT("extreme_value_cited", "math-real-analysis:extreme_value_theorem",
     "A continuous real-valued function on a nonempty compact set attains its supremum and infimum.")

# --- cited from outside the stack (honest gaps) -----------------------------
N("complex_number", "bridge", "foundations",
  "C = R[i] with i^2 = -1: a field of characteristic 0 carrying the conjugation a + bi -> a - bi, with |z|^2 = z conj(z) >= 0. Cited: NO capsule in this stack constructs C.",
  parseable="C := R[t]/(t^2 + 1);  conj(a + bi) = a - bi;  |z|^2 = z conj(z)",
  symbols={"C": "the complex field, type: field of characteristic 0",
           "conj(z)": "complex conjugation, type: field automorphism C -> C fixing R",
           "|z|": "modulus, type: function C -> R_{>=0}"},
  tcn="Cited. Well-formed as a quotient of the polynomial ring R[t] by the maximal ideal (t^2 + 1); the quotient is a field because that polynomial is irreducible over R.",
  proof=("cited from math-number-systems (R) plus the standard quadratic extension; the extension itself is NOT developed in this stack", None, "cited", None),
  field_scope=None,
  spec=["restricting conjugation to R gives the identity, which is why every real result is the b = 0 case of its complex counterpart"],
  cxd={"positive_definiteness_of_the_form": "over C the bilinear form sum z_i w_i is NOT positive definite (take z = (1, i): sum z_i^2 = 0 with z != 0). This is exactly why the complex inner product must conjugate one slot -- see inner_product_convention"},
  misuse=["treating C as an ordered field -- it admits no order compatible with its arithmetic, which is why positive_definite is tagged ordered_field and stated over R"],
  sources=["hoffman_kunze_2e"], status="reviewed")

N("fundamental_theorem_of_algebra", "bridge", "foundations",
  "Every nonconstant polynomial in C[t] has a root in C; equivalently every such polynomial splits into linear factors. C is algebraically closed. CITED, NOT PROVED -- every known proof needs analysis or topology that no capsule in this stack develops.",
  parseable="for all p in C[t] with deg p >= 1, there exists z in C with p(z) = 0",
  symbols={"p": "a polynomial, type: element of C[t]", "z": "a root, type: element of C"},
  tcn="Well-formed. Note the statement is about C specifically, not about fields in general -- most fields are not algebraically closed.",
  proof=("cited; standard proofs use Liouville's theorem, the argument principle, or a minimum-modulus/compactness argument, none available in this stack", None, "cited", None),
  field_scope="algebraically_closed",
  spec=["degree 2 over R: t^2 + 1 has no real root but factors over C, which is the minimal instance of why R is not algebraically closed"],
  cxd={"the_field_being_C": "over R the theorem is false: t^2 + 1 is irreducible. This is precisely the hypothesis that eigenvalue_existence_closed needs, and why a real rotation matrix can have no real eigenvalue",
       "nonconstant": "a nonzero constant polynomial has no root; the degree >= 1 hypothesis is not decorative"},
  misuse=["citing FTA to claim a REAL matrix has real eigenvalues -- it gives complex ones, and realness for symmetric matrices is a separate theorem (self_adjoint_real_eigenvalues)",
          "treating this capsule's use of it as proved: it is the capsule's single largest cited gap"],
  related={"required_by": ["schur_triangularisation", "spectral_theorem_normal"]},
  sources=["hoffman_kunze_2e", "horn_johnson_2e"], status="draft")

N("polynomial_ring", "bridge", "foundations",
  "F[t], the ring of polynomials in one indeterminate over a field F: a Euclidean domain under degree, so it has division with remainder, gcds, and unique factorisation into irreducibles. Every ideal is principal.",
  parseable="F[t] Euclidean under deg;  for g != 0, f = qg + r with r = 0 or deg r < deg g;  every ideal = (m) for a unique monic m",
  symbols={"F[t]": "the polynomial ring, type: commutative ring, in fact a PID",
           "deg": "degree, type: function F[t]\\{0} -> N",
           "(m)": "the principal ideal generated by m"},
  tcn="Well-formed over any field. Principality is what makes 'the' minimal polynomial a definite description: the annihilator of an operator is an ideal, hence generated by a unique monic element.",
  proof=("cited; the division algorithm is induction on degree, principality follows by taking a nonzero element of least degree", None, "cited", None),
  field_scope="any_field",
  spec=["F = R, deg g = 1: division with remainder is evaluation, f(t) = q(t)(t - a) + f(a) -- the factor theorem"],
  cxd={"F_being_a_field": "over a general commutative ring, Z[t] say, division with remainder fails (t does not divide 2t + 1 with remainder of lower degree) and ideals need not be principal. Minimal polynomials of matrices over a ring are correspondingly badly behaved -- see smith_normal_form_boundary"},
  misuse=["assuming irreducible means degree 1: that holds only over an algebraically closed field"],
  related={"required_by": ["characteristic_polynomial", "minimal_polynomial", "cayley_hamilton"]},
  sources=["hoffman_kunze_2e", "dummit_foote_3e"], status="reviewed")

# --- the field structure ----------------------------------------------------
N("field", "structure", "vector_spaces",
  "A field (F, +, *, 0, 1) is a commutative ring with 0 != 1 in which every nonzero element has a multiplicative inverse: (F,+) is an abelian group, (F\\{0}, *) is an abelian group, and * distributes over +.",
  parseable="(F,+,0) abelian group;  (F\\{0},*,1) abelian group;  a(b+c) = ab + ac;  0 != 1",
  symbols={"F": "the field, type: set with two binary operations",
           "0, 1": "the additive and multiplicative identities, type: elements of F, required distinct",
           "a^{-1}": "the multiplicative inverse of a != 0, type: element of F"},
  tcn="Well-formed. The exclusion of 0 from the multiplicative group is essential: 0 has no inverse in any ring with 0 != 1, since 0*x = 0 for all x.",
  hyps=["0 != 1 (excludes the zero ring)"],
  field_scope="any_field",
  spec=["F = Q, R, C: the fields this capsule actually uses",
        "F = F_2 = {0,1}: the two-element field, where 1 + 1 = 0 -- the standing counterexample for every char_not_2 result",
        "F = F_p for p prime: finite fields, over which all the any_field results still hold"],
  cxd={"existence_of_inverses": "Z is a commutative ring but not a field; over Z 'vector spaces' become modules, bases need not exist, and rank is replaced by invariant factors (smith_normal_form_boundary)",
       "commutativity_of_multiplication": "over a division ring (the quaternions H) left and right vector spaces differ and the determinant theory breaks: det(AB) = det(A)det(B) has no direct analogue",
       "zero_not_equal_one": "in the zero ring every module is trivial and dimension is meaningless"},
  misuse=["assuming char F = 0 -- half the hypothesis-dropped counterexamples in this capsule are at char 2",
          "assuming F is ordered: 'x^2 >= 0' is meaningless over C and false over F_p"],
  apps=["the scalars of every vector space in the capsule; coding theory and cryptography run the same linear algebra over F_2 and F_p",
        "F_2 linear algebra is the engine of linear block codes (Hamming, Reed-Muller) and of Gaussian elimination in SAT/XOR solvers"],
  related={"generalizes": []},
  sources=["hoffman_kunze_2e", "dummit_foote_3e"], status="reviewed")

# --- first-class hypothesis nodes -------------------------------------------
N("finite_dimensional", "hypothesis", "vector_spaces",
  "V is finite-dimensional if it has a finite spanning set. A FIRST-CLASS HYPOTHESIS, never ambient: every result that needs it carries a tsort edge to this node.",
  parseable="exists a finite S subset V with span(S) = V",
  symbols={"V": "a vector space over F", "S": "a finite spanning set, type: finite subset of V"},
  tcn="Well-formed before dimension is available -- it says a finite spanning set EXISTS, not that any number is well-defined. That ordering is what lets steinitz_exchange and dimension_well_defined come afterwards.",
  field_scope="any_field",
  spec=["F^n is finite-dimensional with the standard spanning set of size n",
        "the space of polynomials of degree <= d is finite-dimensional (dimension d+1); the space of ALL polynomials is not"],
  cxd={"finiteness": "F[t] (all polynomials) has no finite spanning set. Dropping the hypothesis breaks rank_nullity (the shift operator on F[t] is injective, not surjective, with zero nullity), injective_surjective_equivalence, double_dual, and the existence of an eigenvalue -- see infinite_dimensional_boundary for the catalogue"},
  misuse=["assuming it silently because the examples are all F^n: most of this capsule's sharpest theorems are FALSE without it",
          "confusing it with 'has a basis' -- every vector space has a basis given AC (basis_existence_general); what finite-dimensionality buys is that the basis is finite and choice-free"],
  related={"illustrated_by": ["infinite_dimensional_boundary"]},
  sources=["axler_lada_4e"], status="reviewed")

N("characteristic_not_two", "hypothesis", "vector_spaces",
  "char F != 2, i.e. 1 + 1 != 0 in F. Required wherever a factor of 1/2 is taken, and wherever a symmetric bilinear form must be recoverable from its quadratic form.",
  parseable="1 + 1 != 0 in F",
  symbols={"char F": "the characteristic: the least n > 0 with n*1 = 0, or 0 if none"},
  tcn="Well-formed for any field. Note char F is either 0 or a prime.",
  field_scope="char_not_2",
  spec=["F = Q, R, C all have characteristic 0, so every char_not_2 result applies unconditionally there",
        "F = F_3: 1 + 1 = 2 != 0, so the hypothesis holds over odd finite fields too"],
  cxd={"char_not_2": "over F_2 the polarisation identity fails: the map q(x) = x^T A x determines A only up to adding an alternating matrix, since q(x+y) - q(x) - q(y) = 2 x^T A y = 0. Symmetric and alternating forms cease to be distinguishable, and quadratic_form's uniqueness of the symmetric representative is false"},
  misuse=["writing (A + A^T)/2 to symmetrise a matrix without checking the characteristic"],
  related={"required_by": ["polarisation_identity", "quadratic_form"]},
  sources=["hoffman_kunze_2e", "lang_algebra_3e"], status="reviewed")

N("algebraically_closed_field", "hypothesis", "eigentheory",
  "F is algebraically closed if every nonconstant polynomial in F[t] has a root in F, equivalently splits into linear factors. The hypothesis behind every 'there exists an eigenvalue' statement.",
  parseable="for all p in F[t] with deg p >= 1, there exists a in F with p(a) = 0",
  symbols={"F": "the scalar field"},
  tcn="Well-formed over any field. C is the instance this capsule uses, supplied by the cited fundamental_theorem_of_algebra.",
  hyps=["F algebraically closed"],
  field_scope="algebraically_closed",
  spec=["F = C by the fundamental theorem of algebra",
        "the algebraic closure of any field exists (needs AC in general), so every capsule result tagged algebraically_closed can be reached by passing to F-bar -- at the cost of leaving the original field"],
  cxd={"algebraic_closure": "over R the rotation by 90 degrees, [[0,-1],[1,0]], has characteristic polynomial t^2 + 1 and NO real eigenvalue. Every statement of the form 'an operator has an eigenvalue', 'is triangularisable', 'has a Jordan form' fails over R for this matrix",
       "over_Q": "even worse: [[0,2],[1,0]] has char poly t^2 - 2, with no root in Q"},
  misuse=["applying Jordan form or Schur triangularisation to a real matrix and expecting real output -- the output is complex unless the spectrum happens to be real, which for SYMMETRIC matrices is guaranteed by a different theorem"],
  related={"required_by": ["eigenvalue_existence_closed", "schur_triangularisation", "primary_decomposition", "jordan_normal_form"]},
  sources=["axler_lada_4e", "hoffman_kunze_2e"], status="reviewed")

N("ordered_field_hyp", "hypothesis", "spectral",
  "F carries a total order compatible with its arithmetic: a < b implies a + c < b + c, and 0 < a, 0 < b implies 0 < ab. Needed to say a scalar is POSITIVE, hence for positive-definiteness and inertia.",
  parseable="(F, <) totally ordered;  a < b => a + c < b + c;  0 < a and 0 < b => 0 < ab",
  symbols={"<": "the order, type: total order on F compatible with + and *"},
  tcn="Well-formed. An ordered field necessarily has characteristic 0 (since 1 > 0 forces 1 + 1 + ... > 0), so ordered_field implies char_not_2 -- recorded as a note, not as an edge, to keep the tags independent.",
  field_scope="ordered_field",
  spec=["F = R, the case every spectral result in this capsule is stated over",
        "F = Q is ordered too, so Sylvester's law of inertia holds over Q -- but the spectral theorem does not, because the eigenvalues need not be rational"],
  cxd={"the_order": "C admits no compatible order (i^2 = -1 < 0 contradicts squares being nonnegative). So 'positive definite' over C must be read as 'the HERMITIAN form x^* A x takes positive REAL values', which is a different statement needing self-adjointness to even be real-valued",
       "over_a_finite_field": "F_p has no compatible order at all; positive_definite and sylvester_law_of_inertia are simply not statable there"},
  misuse=["calling a complex symmetric (not Hermitian) matrix positive definite -- x^T A x is complex-valued and the phrase is meaningless"],
  related={"required_by": ["positive_definite", "sylvester_law_of_inertia"]},
  sources=["hoffman_kunze_2e", "horn_johnson_2e"], status="reviewed")

# --- notation conventions ---------------------------------------------------
N("index_convention", "notation_convention", "matrices",
  "Vectors are COLUMNS. A in F^{m x n} has m rows and n columns; A_{ij} is the entry in row i and column j; indices start at 1. A row vector is written x^T.",
  parseable="x in F^n means x is n x 1;  A in F^{m x n};  A_{ij} = row i, column j;  i in {1..m}, j in {1..n}",
  symbols={"A_{ij}": "the (i,j) entry, type: element of F",
           "e_i": "the i-th standard basis column of F^n, type: element of F^n"},
  tcn="A convention, so there is nothing to prove -- but it is load-bearing: it fixes that Ax is a column, that the matrix of a map has the IMAGES of basis vectors as its columns (matrix_of_linear_map), and hence that [S o T] = [S][T] rather than the reverse.",
  field_scope=None,
  spec=["under the opposite (row-vector) convention the composition rule becomes [S o T] = [T][S] and every matrix identity in this capsule transposes"],
  cxd={"none_all_hypotheses_essential": "a convention has no hypotheses; the failure mode is INCONSISTENCY, not falsity -- mixing conventions mid-derivation silently transposes results"},
  misuse=["reading x^T A x with x a row vector: the shapes then do not conform",
          "0-based indexing when quoting the Leibniz formula or the cofactor sign (-1)^{i+j}, which shifts every sign"],
  sources=["hoffman_kunze_2e", "strang_5e"], status="reviewed")

N("transpose_convention", "notation_convention", "matrices",
  "A^T is the TRANSPOSE (A^T)_{ij} = A_{ji}; A^* is the CONJUGATE TRANSPOSE (A^*)_{ij} = conj(A_{ji}). They coincide over R. Every Hermitian statement in this capsule says which one it means.",
  parseable="(A^T)_{ij} = A_{ji};  (A^*)_{ij} = conj(A_{ji});  A^* = A^T when A is real",
  symbols={"A^T": "transpose, type: F^{m x n} -> F^{n x m}",
           "A^*": "conjugate transpose, type: C^{m x n} -> C^{n x m}"},
  tcn="A convention. The substantive point is that the ADJOINT with respect to an inner product is A^*, not A^T, over C -- adjoint_operator proves this, and getting it wrong makes the complex spectral theorem false.",
  field_scope=None,
  spec=["over R the two coincide, which is why the statistics-facing half of the capsule can be written entirely with A^T"],
  cxd={"none_all_hypotheses_essential": "a convention; the failure mode is using A^T over C, under which A^T A need not be positive semidefinite -- take A = [[1, i]], where A^T A has a zero eigenvalue direction while A^* A does not"},
  misuse=["defining a complex symmetric matrix as A^T = A and expecting real eigenvalues: that is the HERMITIAN condition A^* = A, and complex-symmetric matrices can have any spectrum"],
  related={"dual_of": ["dual_map"]},
  sources=["horn_johnson_2e"], status="reviewed")

N("inner_product_convention", "notation_convention", "inner_product",
  "The complex inner product is LINEAR IN THE FIRST argument and conjugate-linear in the second: <ax, y> = a<x,y>, <x, ay> = conj(a)<x,y>, <y,x> = conj(<x,y>). The mathematician's convention (Axler, Hoffman-Kunze), NOT the physicist's.",
  parseable="<ax + by, z> = a<x,z> + b<y,z>;  <x, y> = conj(<y, x>);  <x,x> > 0 for x != 0",
  symbols={"<x,y>": "the inner product, type: V x V -> F with F in {R, C}"},
  tcn="A convention, but conjugate-symmetry is FORCED, not chosen: without it <x,x> need not be real and 'positive definite' is meaningless. What is conventional is only WHICH slot is conjugated.",
  field_scope="real_or_complex",
  spec=["over R conjugation is the identity and the form is simply bilinear and symmetric",
        "the standard inner product on C^n under this convention is <x,y> = sum_i x_i conj(y_i) = y^* x"],
  cxd={"conjugate_symmetry": "the plain bilinear form sum_i x_i y_i on C^n is NOT positive definite: x = (1, i) gives sum x_i^2 = 1 + (-1) = 0 with x != 0. Every norm, projection, and spectral result in the inner-product half of the capsule collapses without the conjugation"},
  misuse=["mixing this with the physicist's convention mid-proof, which swaps a with conj(a) and turns the adjoint identity <Tv,w> = <v,T^*w> into its conjugate",
          "reading <x,y> = y^* x as y^T x over C"],
  sources=["axler_lada_4e", "hoffman_kunze_2e"], status="reviewed")

N("characteristic_polynomial_convention", "notation_convention", "eigentheory",
  "p_A(t) = det(tI - A), which is MONIC of degree n. The common variant det(A - tI) equals (-1)^n p_A(t): same roots, opposite sign when n is odd, and a different constant term.",
  parseable="p_A(t) := det(tI - A) = t^n - tr(A) t^{n-1} + ... + (-1)^n det(A)",
  symbols={"p_A": "the characteristic polynomial, type: monic element of F[t] of degree n",
           "t": "the indeterminate, type: element of F[t]"},
  tcn="A convention. Monicity is what makes 'the' characteristic polynomial a definite description and makes the coefficient identities (char_poly_coefficients) hold with the signs stated.",
  field_scope="any_field",
  spec=["n = 1: p_A(t) = t - A_{11} under this convention, versus A_{11} - t under the other",
        "n = 2: p_A(t) = t^2 - tr(A) t + det(A), the form used throughout the capsule's 2x2 instance checks"],
  cxd={"none_all_hypotheses_essential": "a convention; the failure mode is a sign error. Under det(A - tI) the constant term is det(A), not (-1)^n det(A), and quoting char_poly_coefficients across conventions produces wrong signs for odd n"},
  misuse=["quoting 'the constant term is det A' without saying which convention -- true for det(A - tI), off by (-1)^n for det(tI - A)"],
  sources=["hoffman_kunze_2e", "horn_johnson_2e"], status="reviewed")
