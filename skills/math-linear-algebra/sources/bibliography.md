# Bibliography — math-linear-algebra Release 0.1

Citation keys used in `results/*.yaml` and `nodes/*.md`. Cross-capsule keys
(`math-*`) refer to sibling capsules in this repository, not to external works.

## Textbooks — primary sources for this release

**`axler_lada_4e`** — Sheldon Axler, *Linear Algebra Done Right*, 4th edition,
Springer Undergraduate Texts in Mathematics, 2024 (open access).
The determinant-free development: eigenvalues defined before determinants,
operators before matrices. This capsule follows Axler's ORDERING (see
`edges/cycles.md`, cycle 1) while keeping the determinant as a first-class
object rather than deferring it to the last chapter.

**`hoffman_kunze_2e`** — Kenneth Hoffman and Ray Kunze, *Linear Algebra*, 2nd
edition, Prentice-Hall, 1971.
The field-general treatment: results are stated over an arbitrary field,
characteristic is tracked, and modules are visible at the edges. The source for
this capsule's `field_scope` tag and for the alternating-form definition of the
determinant (`determinant_existence_uniqueness`).

**`horn_johnson_2e`** — Roger A. Horn and Charles R. Johnson, *Matrix Analysis*,
2nd edition, Cambridge University Press, 2013.
The matrix-analytic reference: normal matrices, Schur form, singular values,
Courant–Fischer, inertia, matrix norms. Primary source for the spectral and
quadratic-form half of the capsule.

**`strang_5e`** — Gilbert Strang, *Introduction to Linear Algebra*, 5th edition,
Wellesley-Cambridge Press, 2016.
The four-subspaces framing (`four_subspaces`, `svd_four_subspaces`), the
elimination/pivot-column treatment, and the applied reading of projection and
least squares.

**`lang_algebra_3e`** — Serge Lang, *Algebra*, revised 3rd edition, Springer
GTM 211, 2002.
Multilinear algebra, the determinant as an alternating form, and the
module-theoretic context of `smith_normal_form_boundary`.

**`dummit_foote_3e`** — David S. Dummit and Richard M. Foote, *Abstract
Algebra*, 3rd edition, Wiley, 2004.
Structure theorem for finitely generated modules over a PID, the symmetric
group and the sign homomorphism, polynomial rings.

**`halmos_fdvs`** — Paul R. Halmos, *Finite-Dimensional Vector Spaces*, 2nd
edition, Springer UTM, 1974 (first published 1942).
The source for the coordinate-free style and for the Grassmann dimension
formula's treatment.

## Numerical linear algebra — cited for regime and stability claims

Everything this capsule says about FLOATING-POINT behaviour is cited to these
works, never proved here (see `scope.md`, "Excluded": numerical linear algebra
as a discipline).

**`trefethen_bau`** — Lloyd N. Trefethen and David Bau III, *Numerical Linear
Algebra*, SIAM, 1997.
SVD-first presentation, conditioning, stability of QR and of the QR algorithm.
Source for `condition_number`, `matrix_norms`, `spectral_radius`'s transient-
growth caveat, and the Gram–Schmidt stability note.

**`golub_van_loan_4e`** — Gene H. Golub and Charles F. Van Loan, *Matrix
Computations*, 4th edition, Johns Hopkins University Press, 2013.
LU with pivoting, Cholesky, QR, SVD algorithms and their operation counts.

**`higham_asna_2e`** — Nicholas J. Higham, *Accuracy and Stability of Numerical
Algorithms*, 2nd edition, SIAM, 2002.
Backward error analysis; growth factors for LU; the distinction between
conditioning (a property of the problem) and stability (a property of the
algorithm) that `condition_number` turns on.

## Applications — cited where a node carries an `applications` entry

**`boyd_vandenberghe`** — Stephen Boyd and Lieven Vandenberghe, *Convex
Optimization*, Cambridge University Press, 2004.
Positive semidefinite cones, Schur complements, the Loewner ordering.

**`rao_linear_statistical_inference`** — C. Radhakrishna Rao, *Linear
Statistical Inference and Its Applications*, 2nd edition, Wiley, 1973.
The projection/hat-matrix treatment of least squares and the quadratic-forms-in-
normal-variables results that `math-statistics` builds on.

**`conway_functional_analysis`** — John B. Conway, *A Course in Functional
Analysis*, 2nd edition, Springer GTM 96, 1990.
Cited only for the infinite-dimensional counterexamples catalogued in
`infinite_dimensional_boundary` — the shift operators, non-reflexive spaces,
and the failure of orthogonal decomposition for non-closed subspaces.

## Papers

**`blass_1984`** — Andreas Blass, "Existence of bases implies the axiom of
choice", in *Axiomatic Set Theory*, Contemporary Mathematics 31, American
Mathematical Society, 1984, pp. 31–33.
The ZF-equivalence cited by `basis_existence_general` — the capsule's only
`choice_grade: needs_full_AC` result.

**`eckart_young_1936`** — Carl Eckart and Gale Young, "The approximation of one
matrix by another of lower rank", *Psychometrika* 1(3), 1936, pp. 211–218.
The original low-rank approximation theorem (Frobenius norm); the spectral-norm
case is due to Mirsky (1960), and the general unitarily-invariant-norm case is
noted on the node as cited.

**`jordan_von_neumann_1935`** — Pascual Jordan and John von Neumann, "On inner
products in linear, metric spaces", *Annals of Mathematics* 36(3), 1935,
pp. 719–723.
The parallelogram-law characterisation of inner-product norms, cited (not
proved) by `parallelogram_law`.

**`steele_cauchy_schwarz`** — J. Michael Steele, *The Cauchy–Schwarz Master
Class*, Cambridge University Press, 2004.
The equality case and the variational proof of `cauchy_schwarz`.

## Sibling capsules in this repository

**`math-sets-functions-cardinality`** — sets, functions, quotients, Zorn's
lemma, the axiom of choice, finiteness. Discharges this capsule's `set`,
`function`, `bijection`, `equivalence_relation`, `quotient_set`, `finite_set`,
`indexed_family`, `zorns_lemma`, and `axiom_of_choice` roots.

**`math-number-systems`** — `R` as a complete ordered field. Discharges
`real_number`. Does NOT construct `C`, which this capsule cites as a genuine
gap.

**`math-real-analysis`** — compactness (Heine–Borel) and the extreme value
theorem. Discharges `compactness_cited` and `extreme_value_cited`, used only in
the Rayleigh-quotient route to `spectral_theorem_symmetric`.

**`math-logic-and-proof`** — induction and the proof methods. Discharges
`induction_principle`.

**`math-statistics`** — the capsule ABOVE this one. Its
`linear_algebra_background` node is what this capsule exists to discharge; see
[`edges/cross-capsule.md`](../edges/cross-capsule.md).
