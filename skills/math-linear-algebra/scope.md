# math-linear-algebra — Release 0.1 scope

Linear algebra as a curated, dependency-ordered knowledge capsule, built with
the [`math-theorem-tree`](../math-theorem-tree/SKILL.md) method.

Its job in the stack: **discharge `math-statistics`'s
`linear_algebra_background` node**, which currently cites — with no capsule
beneath it — "vector spaces and subspaces, rank, transpose, inverse; symmetric
and positive-(semi)definite matrices; the spectral theorem for real symmetric
matrices; orthogonal projection onto a subspace and its idempotent symmetric
projection matrix; trace; quadratic forms `x^T A x`". Every item on that list is
a developed node here (see `edges/cross-capsule.md`).

## Included

**Vector spaces.** Field axioms (as a `structure` node, `R` cited from
`math-number-systems`); vector space and subspace; linear combination and span;
linear independence; basis; the Steinitz exchange lemma and dimension
well-definedness; coordinates relative to an ordered basis; sums, direct sums,
and the dimension formula; quotient spaces; existence of a basis in the
finite-dimensional case (choice-free) and in general (Zorn).

**Linear maps.** Linear map, kernel, image, rank, nullity; the rank–nullity
theorem; injectivity/surjectivity criteria and isomorphism; the matrix of a
linear map relative to bases; change of basis and similarity; the dual space,
dual basis, the transpose/dual map, and double duality in finite dimension.

**Matrices and elimination.** Matrices as arrays and as maps; matrix
multiplication as composition; transpose; invertibility and the inverse;
elementary row operations and elementary matrices; row echelon and reduced row
echelon form with uniqueness; Gaussian elimination; LU factorisation with the
pivoting caveat; the four fundamental subspaces; row rank = column rank; rank
inequalities; block matrices and the Schur complement.

**Determinants.** The determinant as the unique alternating multilinear
normalised form on columns; the Leibniz formula; Laplace/cofactor expansion;
multiplicativity; `det A != 0 <=> A invertible`; the adjugate and Cramer's rule;
determinant of a triangular matrix, of a transpose, under row operations;
trace, its cyclic property, and similarity invariance of both.

**Eigentheory.** Eigenvalue, eigenvector, eigenspace; the characteristic
polynomial; algebraic and geometric multiplicity; the diagonalisability
criterion; independence of eigenvectors for distinct eigenvalues;
Cayley–Hamilton; the minimal polynomial; Schur triangularisation; nilpotent
operators, generalised eigenspaces, the primary decomposition, and a statement
of the Jordan normal form.

**Inner product spaces.** Inner product (real and Hermitian), induced norm,
Cauchy–Schwarz, the triangle inequality, the parallelogram law and the
polarisation identity; orthogonality, orthonormal sets, Bessel's inequality and
Parseval's identity; Gram–Schmidt; orthogonal complement and the orthogonal
decomposition theorem; the orthogonal projection onto a subspace, its
idempotent-and-self-adjoint matrix, and the best-approximation theorem; least
squares and the normal equations; QR factorisation.

**Spectral theory and quadratic forms.** The adjoint; self-adjoint (real
symmetric), orthogonal/unitary, and normal operators; the spectral theorem for
real symmetric matrices and for normal matrices over `C`; the Rayleigh quotient
and Courant–Fischer min–max; positive definite and positive semidefinite
matrices with their equivalent characterisations; the Gram matrix; the Cholesky
factorisation; quadratic forms, congruence, and Sylvester's law of inertia;
simultaneous diagonalisation of a pair with one definite; the singular value
decomposition; the Moore–Penrose pseudoinverse; the Eckart–Young low-rank
approximation theorem; the spectral and Frobenius norms and the condition
number.

## Excluded

- **Infinite-dimensional functional analysis.** Hilbert/Banach space theory,
  bounded operators, the spectral theorem for compact or unbounded operators.
  General vector spaces appear only far enough to state basis existence via
  Zorn and to say where finite-dimensionality is load-bearing.
- **Modules over a ring**, the structure theorem for finitely generated modules
  over a PID (the general home of Jordan/Smith normal form), and tensor
  products, exterior algebra, multilinear algebra beyond the determinant's
  defining alternating-form property.
- **Numerical linear algebra as a discipline**: backward-error analysis,
  iterative solvers (CG, GMRES), Krylov methods, QR/eigenvalue algorithms.
  Condition number and the LU pivoting caveat are in, as `diagnostic` and
  `regime` nodes; algorithm stability analysis is not.
- **Representation theory, Lie algebras, algebraic geometry.**
- **Proof of the Jordan normal form.** Stated as a boundary node
  (`status: draft`) with its prerequisites (primary decomposition, nilpotent
  structure) developed; the full cyclic-subspace construction is Release 0.2.
- **Fundamental theorem of algebra.** Cited from outside the stack (no capsule
  develops it); it is what makes `C` algebraically closed and therefore what
  Schur triangularisation and the complex spectral theorem rest on. Flagged as
  a cited root, not proved here.

## Level and audience

Upper-undergraduate / first-year-graduate linear algebra (Axler, Hoffman–Kunze,
Horn–Johnson, Strang). Written for a reader — human or agent — who needs to know
*which hypothesis a matrix result actually needs* and *over which field it
holds*.

## Foundational stance

- **Sets and functions are primitive**, cited from
  `math-sets-functions-cardinality` (`set`, `function`, `bijection`,
  `equivalence_relation`, `quotient_set`, `finite_set`, `zorns_lemma`,
  `axiom_of_choice`). Not rebuilt here.
- **`R` is a complete ordered field**, cited from `math-number-systems`; `C` is
  cited as its algebraic closure. Their *construction* is out of scope. The
  general **field** axioms are a `structure` node here, because the
  field-dependence of results is one of this capsule's two headline tags.
- **Finite-dimensionality is a first-class `hypothesis` node**, not an ambient
  assumption. A result that needs it has a `tsort` edge to it. This is the
  single most-dropped hypothesis in applied linear algebra (rank–nullity,
  double duality, "injective implies surjective", det-based invertibility).
- **The determinant is defined as the unique normalised alternating multilinear
  function of the columns**, with the Leibniz formula a *theorem*. Eigenvalues
  are defined by `Av = lambda v, v != 0`, independently of the characteristic
  polynomial — this breaks the determinant ↔ eigenvalue cycle (see
  `edges/cycles.md`).
- **Proofs are sketched with the technique named**; key algebraic cores are
  Lean-checked (Mathlib-free — see `validation/proof-checks.md` for the
  kernel-verified vs cited split), and concrete instances are `bc`-checked.

## Per-result tags

Two tags, both load-bearing in this domain, both generated into an index.

**`field_scope`** — the field a result actually needs. This capsule's analogue
of `math-statistics`'s `regime` and `math-probability`'s `convergence_mode`.

| value | meaning | example |
|---|---|---|
| `any_field` | holds over any field | rank–nullity, `det(AB) = det(A)det(B)` |
| `char_not_2` | needs `1 + 1 != 0` | polarisation identity, symmetric ↔ quadratic-form correspondence |
| `ordered_field` | needs an order on the scalars | Sylvester's law of inertia, positive-definiteness |
| `real_or_complex` | needs `R` or `C` specifically (an inner product, hence completeness of the scalars for the norm argument) | Cauchy–Schwarz, Gram–Schmidt, spectral theorem, SVD |
| `algebraically_closed` | needs every polynomial to split | Schur triangularisation, Jordan form, existence of an eigenvalue |

**`choice_grade`** — inherited from `math-sets-functions-cardinality`'s
vocabulary (`choice_free` / `needs_countable_choice` / `needs_full_AC`). Almost
everything here is `choice_free`; the exception is the real content of the tag:
**every vector space has a basis** is equivalent to AC, while the
finite-dimensional case is not.

## Release boundary

Release 0.1 is the graph, the entries, the Lean cores, and the `bc` instances.
Boundary nodes carried as `draft` (stated, not developed): `jordan_normal_form`,
`fundamental_theorem_of_algebra` (cited), `smith_normal_form_boundary`,
`infinite_dimensional_boundary`.

Release 0.2 territory: the Jordan form proved via cyclic subspaces; tensor and
exterior algebra (which would make the determinant's alternating-form definition
a *consequence* rather than a definition); a numerical-stability layer; modules
over a PID.
