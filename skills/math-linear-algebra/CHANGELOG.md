# Changelog — math-linear-algebra

## 2.0.0 — 2026-09-14

**MAJOR: 19 prerequisite edges were missing.** `build/check-edge-evidence.py`
(new; see [`docs/verifying-skills.md` §5a](../../docs/verifying-skills.md)) read
each node's proof prose and found 19 results the proofs cite that the graph did
not carry — among them `subspace_criterion -> kernel` / `image_subspace` /
`span_is_smallest_subspace` / `subspace_intersection`, `trace_cyclic ->
hat_matrix`, `orthogonal_decomposition -> adjoint_kernel_image`,
`rref_uniqueness -> gaussian_elimination`, and `spectral_theorem_normal ->
spectral_radius`. Any prerequisite chain queried before this commit was
incomplete, silently. Now 618 edges; still acyclic; `results/` and `nodes/`
regenerated from the graph.

Four soft hits adjudicated in `validation/edge-evidence-ignore.txt` (three
English-word matches, one route the prose itself marks as not-an-edge).
`validation/mutation-check.sh` (new) plants five graph defects per build and
asserts each is caught: 5/5, at 198 of 198 nodes falsifiable.

## Release 0.1 — 2026-09-13

First release. Built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method.

### Graph

- **198 nodes**, **599 `tsort` edges**, acyclic (BSD stderr-checked via the
  shared `lib/build-tree.sh` guard), **0 isolated**, **19 roots**.
- Areas: matrices (39), vector spaces (28), spectral (27), inner product (25),
  eigentheory (24), linear maps (20), determinants (17), foundations (16),
  boundary (2).
- **Acyclic on the first `tsort` pass** — the five would-be cycles were designed
  out during edge derivation rather than discovered afterwards. All five are
  recorded with their plain-language reading, classification, and resolution in
  `edges/cycles.md`: determinant ↔ eigenvalue, determinant ↔ its own existence
  theorem, rank ↔ determinant, basis ↔ dimension, Gram–Schmidt ↔ orthogonal
  projection.
- `edges/relations.tsv`: 37 non-prerequisite relations (`generalizes`,
  `special_case_of`, `equivalent_to`, `dual_of`, `contrasts_with`,
  `approximates`, `illustrated_by`, `proved_using`, `historically_precedes`),
  all endpoints registry-checked.

### Entries

- All **198** `results/<id>.yaml` and `nodes/<id>.md`, generated from eight spec
  modules under `build/specs/` via `build/gen-results.py`. Dependency lists are
  read from `build/node-deps.txt` (derived from the graph), so a YAML cannot
  drift from the edges.
- `scope.md`, `conventions.md`, `notation.md`, `objects.md`, `SKILL.md`,
  `README.md`, `sources/bibliography.md` (21 keys: 7 textbooks, 3 numerical
  references, 4 papers, 3 application sources, 4 sibling capsules).
- Seven generated indexes: field-scope, hypothesis, status, counterexample,
  symbol/KWIC (`ptx`, 57,618 rotations, `rg`-confirmed), prerequisite paths (87
  headline results), reverse dependencies.

### Two per-result tags

- **`field_scope`** — `any_field` / `char_not_2` / `ordered_field` /
  `real_or_complex` / `algebraically_closed`. This capsule's analogue of
  `math-statistics`'s `regime` and `math-probability`'s `convergence_mode`, and
  the tag that carries the most weight here: it is what distinguishes
  rank–nullity (any field) from the polarisation identity (`char ≠ 2`), from
  Sylvester's law of inertia (ordered), from Cauchy–Schwarz (`R` or `C`), from
  the existence of an eigenvalue (algebraically closed).
- **`choice_grade`** — inherited from `math-sets-functions-cardinality`. 197
  nodes are `choice_free`; `basis_existence_general` is `needs_full_AC`, and is
  the only one, with the ZF-equivalence cited to Blass (1984).

### Validation

- **`validation/proof-checks.lean`** — Lean 4.33, Mathlib-free, **exit 0, no
  `sorry`, no `axiom`, no warnings**. 87 declarations across 10 sections.
  - **13 `core`** nodes: the general statement is proved (dimension arithmetic
    via `omega`; the no-zero-divisors clause via `Int.mul_eq_zero`; uniqueness
    of the inverse and `(XY)⁻¹ = Y⁻¹X⁻¹` as **monoid** arguments).
  - **19 `dim_core`** nodes — a **new `lean_status` value** for statements
    proved *universally in the matrix entries at a fixed dimension*: stronger
    than a numeric instance (every entry is a bound variable), weaker than the
    theorem (which quantifies over n). Includes `det(AB) = det(A)det(B)`,
    `det(kX) = k²det X`, `tr(XY) = tr(YX)`, the adjugate identity (proved for
    **singular** `X` too), Cayley–Hamilton at n = 2, the Lagrange identity at
    n = 2 and 3 exhibiting the Cauchy–Schwarz defect as a sum of squares, and
    the symmetric-discriminant-is-a-sum-of-squares core of the real spectral
    theorem.
  - **8 `instance`** nodes, several deliberately **paired** with their
    dropped-hypothesis counterexample in the same declaration: orthogonal vs
    oblique projection, and the fact that `tr P = rank P` holds for the oblique
    one too, so the trace identity does not certify orthogonality.
  - **1 `partial`**, **110 `cited`**, **2 `stated_not_proved`**.
- **`validation/instance-checks.bc`** — 12 sections, `bc -l`, all passing.
  Determinant multiplicativity and the `det(kA) = kⁿ det A` trap; Cramer vs
  elimination with substitution as an independent oracle; Lagrange/Cauchy–Schwarz
  with both the strict and the equality case; Gram–Schmidt with `A = QR`
  reconstruction; orthogonal vs oblique projection distances; **the
  `math-statistics` OLS design reproduced exactly** (β̂ = (7/6, 1/2), tr H = 2,
  residual orthogonality) as an arithmetic check on the cross-capsule discharge;
  the 2×2 spectral theorem with `QDQᵀ` reconstruction and the rotation's negative
  discriminant as the dropped-hypothesis witness; Sylvester's criterion and the
  leading-vs-all-principal-minors trap; Cholesky; **the condition-number vs
  determinant trap** (`10⁻⁵·I₄` has a vanishing determinant and κ = 1, while
  `diag(1, 10⁻⁵)` has a larger determinant and κ = 10⁵); congruence vs
  similarity; Vandermonde; the four subspaces.

### Guards added in this release

Three, all wired into `build/all.sh`, and all responses to problems the sibling
capsules had to be audited for after the fact:

1. **`build/leanmap.py`** is the single authoritative `lean_status` / `lean_ref`
   table, applied by `nodespec.py` *over* whatever a spec module claims. A node
   absent from the map is **forced to `cited`** — the default is the weakest
   status, so a spec cannot overclaim.
2. **`build/check-lean-refs.py`** verifies that every `LinAlg.*` named in a
   `lean_ref` exists in the `.lean` file, that every non-`cited` node names at
   least one, and that no `cited` node names any. Currently 55 references
   against 87 declarations.
3. **The `bc` step inspects its output, not its exit status.** `bc`'s `quit`
   always exits 0, so the sibling capsules' `all.sh` would pass a run whose
   checks had failed. This one greps for the pass banner and for `FAIL` lines
   and exits 1 on either problem. Verified by deliberately corrupting a check.

### Cross-capsule

- `edges/cross-capsule.md` records the discharge of
  `math-statistics:linear_algebra_background`: an 11-row table mapping each
  assumed fact to the node developing it, plus a per-consumer table checking all
  ten `tsort` consumers of that node inside `math-statistics`. **All 11
  discharged, all 10 consumers supplied.** Recorded as metadata, not as a graph
  edge, so `math-statistics`'s own build is untouched — the same pattern
  `math-sets-functions-cardinality` 0.2 and `physics-thermoacoustics` use.

### Known gaps, stated rather than hidden

- **`complex_number` and `polynomial_ring` are cited roots with no capsule
  beneath them.** No capsule in the stack constructs `C` or develops `F[t]`.
- **`fundamental_theorem_of_algebra` is the capsule's largest cited gap.** Every
  proof needs analysis or topology the stack does not develop. It is what
  `schur_triangularisation` and `spectral_theorem_normal` rest on.
- **`real_number`, `compactness_cited`, `extreme_value_cited`** *are* developed
  in the stack (`math-number-systems`, `math-real-analysis`) and could be
  discharged the same way in a Release 0.2.
- **The general `spectral_theorem_symmetric` is `cited`**, not `core`: its
  Rayleigh-quotient existence step needs real analysis, unavailable
  Mathlib-free. The n = 2 case is worked explicitly.

## Release 0.1a — 2026-09-13 (validation layer added, no graph change)

### `validation/matrix-checks.m` — numerical matrix checks at realistic size

Built with the new [`octave`](../octave/SKILL.md) skill. **120 assertions**,
wired into `build/all.sh` (skipped, not failed, when `octave` is absent).

The motivation is a dimension gap, not a coverage gap in the usual sense.
Mathlib-free Lean cannot quantify over n, so this capsule's strongest matrix
proofs are `dim_core` — universal in the **entries** at a **fixed n = 2**. And
`bc` has no matrices, so every matrix claim in `instance-checks.bc` is
hand-rolled 2×2 scalar arithmetic. At 2×2 most of the capsule's headline
results are degenerate: every 2×2 symmetric matrix is diagonalisable, rank is
0/1/2, and there is exactly one way to be defective.

Dimensions now exercised: **n = 5, 6 square; 6×4, 6×3, 7×4 rectangular;
rank-deficient (rank 3 of 4); defective (Jordan blocks 3+2)**.

Results that gained genuinely new evidence:

- `spectral_decomposition` as a real resolution of the identity — `sum P_i = I`,
  `P_i P_j = 0`, functional calculus `S^3 = sum λ³ P_i`.
- `courant_fischer` via Cauchy interlacing for **all six** principal
  submatrices — a statement with no content at n = 2.
- `moore_penrose_pseudoinverse` — all four Penrose conditions on a
  **rank-deficient** matrix, where `(A'A)^{-1}` does not exist, plus 200 samples
  confirming the minimum-norm property.
- `eckart_young` at k = 1, 2, 3 in both norms, with 300 perturbed rank-k
  competitors none of which beats the truncated SVD.
- `algebraic_geometric_multiplicity` on Jordan blocks 3+2, so the bookkeeping
  has room to be wrong (geometric 2 < algebraic 5).
- `simultaneous_diagonalisation`, `sylvester_law_of_inertia` (inertia (3,2,1)
  preserved under congruence while the eigenvalues are not), `schur_triangularisation`
  over ℂ, `spectral_theorem_normal` with a non-normal negative contrast.
- `condition_number`'s sharpest claim at n = 6: `1e-5·I₆` has determinant
  **1e-30** and condition number **exactly 1**, while `diag(1,…,1e-10)` has the
  *larger* determinant 1e-10 and condition number **1e10**.

Method (from the `octave` skill): every claim computed by **two routes sharing
no code path**; tolerances **derived** (residual ~ `n·eps·‖A‖`, forward error
~ `cond(A)·eps`) and printed next to the achieved residual with the margin, so
a guessed tolerance is visible; a **negative contrast** in every section. All
eight sections were negative-contrast tested — corrupting any one makes
`build/all.sh` exit 1.

One deliberate non-assertion, recorded as section H: the **Jordan form is
numerically uncomputable**. Perturbing a 5×5 Jordan block by 1e-14 in a single
entry moves its eigenvalues by **1.59e-3**, matching the predicted ε^(1/5) =
1.59e-3 rather than ε, and the perturbed matrix is no longer defective. The
section demonstrates this instead of asserting it away; `jordan_normal_form`
stays a `stated_not_proved` boundary node.

**No `lean_status` changed and the graph is untouched.** This is evidence at
particular matrices over ℝ and ℂ, not proof.

A precise statement of the field limitation, since it is the largest one:
Octave has ℝ and ℂ and nothing else. So of the 182 `field_scope`-tagged nodes,
the **121 tagged `any_field`** have their *generality* untested — Octave can
only exercise the ℝ instance and fail to refute the rest — and the **3 tagged
`char_not_2`** cannot be tested in their *failing* direction at all, since
there is no characteristic-2 field available to witness the breakdown. The 45
`real_or_complex`, 5 `ordered_field` and 8 `algebraically_closed` nodes are
tested at a genuine instance of the field they require. Stated in the file's
own closing report and in `validation/proof-checks.md`.

### Release 0.2 territory

Jordan normal form proved via cyclic subspaces; tensor and exterior algebra
(which would make the determinant's alternating-form definition a *consequence*
rather than a definition); modules over a PID; discharging the three
stack-internal roots above; an `upmd` tutorial via `theorem-tree-tutorial`.
