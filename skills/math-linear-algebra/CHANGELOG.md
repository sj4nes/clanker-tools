# Changelog — math-linear-algebra

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

### Release 0.2 territory

Jordan normal form proved via cyclic subspaces; tensor and exterior algebra
(which would make the determinant's alternating-form definition a *consequence*
rather than a definition); modules over a PID; discharging the three
stack-internal roots above; an `upmd` tutorial via `theorem-tree-tutorial`.
