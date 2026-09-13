# Cycle resolutions — math-linear-algebra Release 0.1

Per the `tsort` skill's cycle-resolution protocol: every would-be cycle found
while deriving `edges/dependencies.plan` is recorded here with its plain-language
reading, its classification, and the decision taken. **No edge was silently
deleted.** The released graph is acyclic — 198 nodes, 599 edges, `tsort` clean
with the BSD stderr guard (`validation/tsort-errors.txt` empty).

Five would-be cycles. Four are the classic linear-algebra foundational choices;
the fifth is a definitional-order artefact.

---

## 1. determinant ↔ eigenvalue

**The cycle.** The common presentation defines an eigenvalue as a root of
`det(tI - A)`, and motivates the determinant by "it detects singularity, i.e.
whether 0 is an eigenvalue". Encoding both gives
`determinant -> eigenvalue -> determinant`.

**Classification.** Alternative-definition cycle, not a genuine prerequisite
loop — each concept has a determinant-free and an eigenvalue-free definition
available.

**Resolution.** Both are defined independently:

- `eigenvalue` is defined by `Tv = lambda v` for some `v != 0` — no determinant
  appears, so its only prerequisites are `linear_operator` and `vector_space`.
- `determinant` is defined as the unique normalised alternating multilinear
  function of the columns — no eigenvalue appears.

`char_poly_roots_are_eigenvalues` is then a **theorem** joining them, with edges
from both. This is the Axler-style stance, and it is what lets the capsule state
honestly that eigenvalues are logically prior to the characteristic polynomial
and that the polynomial is a *computational device* for finding them.

**Visible consequence in the emitted order.** `determinant` lands at position 45
and `eigenvalue` at 146 — the determinant needs no basis theory at all, which
the graph now makes explicit rather than hiding behind a joint development.

---

## 2. determinant ↔ "the determinant exists"

**The cycle.** Defining `det` as *the* unique normalised alternating multilinear
form presupposes that exactly one exists; but the existence and uniqueness
theorem is naturally stated *about the determinant*.

**Classification.** Definitional-order defect (a definite description whose
justification was placed after it).

**Resolution.** `determinant_existence_uniqueness` is stated purely about
**normalised alternating multilinear forms on the columns of `F^{n x n}`**,
never naming "the determinant": *there is exactly one such form.* Existence is
proved by exhibiting the Leibniz sum, uniqueness by expanding the columns in the
standard basis and using alternation. `determinant` is then the definition that
*names* that unique form, with an edge from the theorem. `leibniz_formula` comes
after: the formula is identified as `det`, rather than being the definition.

---

## 3. rank ↔ determinant

**The cycle.** Rank is often introduced as "the size of the largest nonvanishing
minor", which needs determinants; determinants are then explained via rank and
singularity.

**Classification.** Alternative-definition cycle.

**Resolution.** `rank` is defined as `dim(im T)` and `matrix_rank` as
`dim col(A)` — no determinant. `determinant_rank_minors` (rank = the largest `r`
with a nonzero `r x r` minor) is a **downstream theorem**, explicitly labelled in
its node page as "a theorem, not the definition of rank".

---

## 4. basis ↔ dimension

**The cycle.** "A basis is a set of `dim V` independent vectors" and "the
dimension is the number of elements in a basis" is circular.

**Classification.** Genuine ordering question with a standard resolution.

**Resolution.** `basis` is defined without any number — an independent spanning
set. `steinitz_exchange` then bounds any independent list by any spanning list,
`dimension_well_defined` concludes that any two bases are equinumerous, and only
then is `dimension` defined. The chain in the graph is
`basis -> steinitz_exchange -> dimension_well_defined -> dimension`, so nothing
mentioning `dim V` can precede the theorem that makes `dim V` meaningful.

---

## 5. Gram–Schmidt ↔ orthogonal projection

**The cycle.** The projection formula `P_U v = sum_i <v, e_i> e_i` is stated
relative to an *orthonormal basis* of `U`, which Gram–Schmidt is what supplies;
meanwhile each Gram–Schmidt step is "subtract the projection onto the span so
far".

**Classification.** Explanatory cycle — the two statements are at different
levels (a formula given data, versus an algorithm producing that data).

**Resolution.** `orthogonal_projection` is stated **given** an orthonormal basis
of `U` (prerequisites: `orthonormal_basis`, `orthogonality`, `subspace`,
`linear_map`), with well-definedness — independence of which orthonormal basis is
used — as part of its own content. `gram_schmidt` then has an edge *from*
`orthogonal_projection`, because its recursion step is literally that formula
applied to the span of the preceding vectors, and it is what upgrades
"given an orthonormal basis" to "in any finite-dimensional inner product space".
`orthogonal_decomposition` sits downstream of both.

---

## Not cycles, recorded to prevent re-litigation

- **similarity vs congruence.** `B = P^{-1}AP` and `B = P^T A P` are different
  relations with different invariants (eigenvalues vs inertia). They are two
  nodes, related by a `contrasts_with` entry in `edges/relations.tsv`, not
  merged and not edged to each other.
- **spectral theorem before characteristic polynomial.** The emitted order puts
  `spectral_theorem_symmetric` (167) ahead of `characteristic_polynomial` (169).
  This is not an error: the release proves the real spectral theorem by the
  Rayleigh-quotient/compactness route, which never mentions the characteristic
  polynomial. The alternative complexify-and-use-FTA route is recorded as a
  `proof_routes` alternative on the node, not as an edge.
- **Cayley–Hamilton via the adjugate.** `cayley_hamilton` takes an edge from
  `adjugate` because the release's proof is the `adj(tI - A)(tI - A) = p_A(t)I`
  argument over `F[t]`. The "substitute `A` into `det(tI - A)`" pseudo-proof is
  recorded on the node page as a common misuse, not as a route.
