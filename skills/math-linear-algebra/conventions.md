# Conventions — math-linear-algebra Release 0.1

Notation, foundational stance, and the cycle resolutions this release commits
to. Every statement in `results/` is read under these conventions; changing one
is a broad semantic change (see `math-theorem-tree` step 10).

## Scalars and fields

- `F` denotes an arbitrary field. `R` and `C` are cited from
  `math-number-systems`; `C` is used as an algebraically closed field and its
  algebraic closedness is a **cited** root (`fundamental_theorem_of_algebra`),
  not proved here.
- **Characteristic.** Unless a node's `field_scope` says otherwise, `F` may have
  any characteristic. Results needing `1 + 1 != 0` carry
  `field_scope: char_not_2` and a `tsort` edge to `characteristic_not_two`.
- **Ordering.** "Positive definite" and Sylvester's law need an *ordered* field;
  those nodes carry `field_scope: ordered_field` and, where they are stated only
  over `R`, say so.

## Vectors and matrices

- Vectors are **columns**. `F^n` means `n x 1` column vectors; a row vector is
  written `x^T`.
- `A in F^{m x n}` has `m` rows and `n` columns. `A_{ij}` is the entry in row
  `i`, column `j`. Indices start at **1**.
- **`A^T` is the transpose; `A^*` is the conjugate transpose** (Hermitian
  adjoint). Over `R` they coincide; every result stated with `A^T` over `R` has
  its `C` analogue stated with `A^*` and the node says which it means.
- The matrix of a linear map `T : V -> W` relative to ordered bases `B` of `V`
  and `C` of `W` is written `[T]_{C<-B}`, with **columns the images of the basis
  vectors**: `[T]_{C<-B} e_j = [T(b_j)]_C`. This makes composition correspond to
  matrix product in the order `[S o T] = [S][T]`.
- `I_n` is the `n x n` identity; `e_i` the `i`-th standard basis vector; `0` is
  overloaded for the zero scalar, vector, and matrix — each node's `symbols`
  block types it.

## Inner products

- The real inner product `<x, y>` is **bilinear, symmetric, positive definite**.
- The complex inner product is **linear in the FIRST argument and conjugate-
  linear in the second** (`<ax, y> = a<x, y>`, `<x, ay> = conj(a)<x, y>`) — the
  mathematician's convention, matching Axler and Hoffman–Kunze, *not* the
  physicist's. Every Hermitian statement in the capsule is written under this
  convention and links to the `inner_product_convention` node.
- The induced norm is `||x|| = sqrt(<x, x>)`. `||.||_2` on `F^n` is the norm from
  the standard inner product `<x, y> = sum_i x_i conj(y_i)`.

## Spans, sums, dimension

- `span(S)` is the set of **finite** linear combinations of `S`, for any `S`
  (including infinite `S`); `span(empty) = {0}`, so the empty set is a basis of
  the zero space and `dim({0}) = 0`.
- `V = U (+) W` (direct sum) means `V = U + W` **and** `U ∩ W = {0}`; the node
  `direct_sum` records the equivalence with uniqueness of decomposition.
- `dim V` is a cardinal. Release 0.1 develops the theory for `dim V` **finite**;
  infinite-dimensional statements are confined to `basis_existence_general` and
  the `infinite_dimensional_boundary` node.

## Polynomials

- The characteristic polynomial is `p_A(t) = det(t I - A)` — **monic**, so
  `p_A(t) = t^n - tr(A) t^{n-1} + ... + (-1)^n det(A)`. (The other common
  convention `det(A - t I)` differs by `(-1)^n` and changes the sign of the
  Cayley–Hamilton statement's constant term; nodes that quote coefficients link
  to `characteristic_polynomial_convention`.)
- The minimal polynomial is the **monic** generator of the annihilator ideal of
  the operator.

## Epistemic and proof policy

- Every result carries an epistemic status label, a full hypothesis list, a type
  (well-formedness) check, >= 1 specialisation, >= 1 hypothesis-dropped
  counterexample, a proof provenance with an explicit `lean_status`, and >= 1
  source — the `math-theorem-tree` quality gate.
- **`lean_status` vocabulary.** The sibling capsules use `core` / `instance` /
  `partial` / `cited` / `stated_not_proved`. This capsule adds one value,
  **`dim_core`**, because linear algebra has a middle ground the others do not:

  | value | meaning |
  |---|---|
  | `core` | the **general** statement is proved in `validation/proof-checks.lean` |
  | `dim_core` | **universal in the matrix entries, at a fixed dimension** (n = 2, sometimes 3). Every entry is a bound variable, so it is strictly stronger than a numeric instance — it is a proof of the n = 2 case — and strictly weaker than the theorem, which quantifies over n |
  | `instance` | `decide`d at fixed numbers: a check, never a proof |
  | `partial` | part of the argument is formalised, the rest is not |
  | `cited` | proved elsewhere, referenced here |
  | `stated_not_proved` | stated as a boundary node with no proof in this release |

  `dim_core` exists because Mathlib-free Lean cannot quantify over the
  dimension without building a matrix library, which Release 0.1 does not
  attempt. Reporting `det(AB) = det(A)det(B)` at n = 2 as `core` would
  overclaim; reporting it as `instance` would underclaim, since every entry is
  universally quantified. 19 nodes carry `dim_core`.

- **Overclaiming is mechanically prevented.** `build/leanmap.py` is the single
  authoritative `lean_status` / `lean_ref` table; `build/nodespec.py` applies it
  over whatever a spec module claims, and **forces any node absent from the map
  to `cited`**. `build/check-lean-refs.py` (wired into `build/all.sh`) then
  verifies that every `LinAlg.*` named in a `lean_ref` actually exists in the
  `.lean` file, and that no `cited` node names one. The drift that had to be
  audited retrospectively in `math-logic-and-proof` and `math-probability`
  cannot occur here.
- The Lean file is **Mathlib-free** (Lean 4 core only). There is therefore no
  `Matrix`, no `ring`, no `linarith`, no real numbers. Universal cores are
  proved over `Nat`/`Int` with explicit small-dimension encodings; everything
  about `R`-specific analysis (Cauchy–Schwarz over `R`, the spectral theorem) is
  `cited` or `instance`. This is stated again in `validation/proof-checks.md`
  and is the honest boundary of what the kernel verified.
- `bc` instance checks are **necessary, not sufficient**: a passing numeric
  instance never promotes a `cited` status to `core`.

## Cycle resolutions

Recorded in full in [`edges/cycles.md`](edges/cycles.md). The three that shape
the graph:

1. **determinant ↔ eigenvalue.** Resolved by *defining* an eigenvalue as a
   scalar `lambda` with `Av = lambda v` for some `v != 0`, and the determinant
   independently as the unique normalised alternating multilinear form on
   columns. `char_poly_roots_are_eigenvalues` is then a **theorem** linking
   them, not a definition, and the edge runs determinant -> characteristic
   polynomial -> that theorem.
2. **rank ↔ determinant.** Resolved by defining rank as `dim(image)` (equally,
   column rank), so `rank` needs no determinant. The minor-based rank
   characterisation is a downstream theorem, not the definition.
3. **basis ↔ dimension.** Resolved by the Steinitz exchange lemma: `basis` is
   defined (independent spanning set) without reference to a number, and
   `dimension_well_defined` is the theorem that any two bases of a
   finitely-generated space are equinumerous. `dimension` is defined only after
   that theorem.

## Cross-capsule stance

This capsule sits **below `math-statistics`** and beside
`math-real-analysis`. It cites, and does not rebuild:
`math-sets-functions-cardinality` (sets, functions, quotients, Zorn),
`math-number-systems` (`R` as a complete ordered field, `C`),
`math-logic-and-proof` (induction, proof by contradiction),
`math-real-analysis` (continuity and compactness — used *only* for the
Rayleigh-quotient existence argument behind the real spectral theorem; an
alternative algebraic route via `C` and self-adjointness is recorded as a
`proof_routes` alternative, so the analysis dependency is a choice this release
documents rather than an unavoidable one).

The discharge of `math-statistics:linear_algebra_background` is recorded as
metadata in [`edges/cross-capsule.md`](edges/cross-capsule.md), **not** as a
`tsort` edge — the same pattern `math-sets-functions-cardinality` Release 0.2
and `physics-thermoacoustics` use, because each capsule's `graph-check.sh` only
knows its own `nodes.tsv`.
