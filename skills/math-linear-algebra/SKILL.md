---
name: math-linear-algebra
description: >
  Linear algebra as a curated, dependency-ordered knowledge capsule — the layer
  below math-statistics and beside math-real-analysis. Vector spaces, bases and
  dimension (with the Steinitz exchange lemma making dimension a theorem rather
  than an assumption); linear maps, rank–nullity, duality and the canonical
  V → V** isomorphism; matrices, elimination, the RREF canonical form, the four
  fundamental subspaces, and row rank = column rank; the determinant DEFINED as
  the unique normalised alternating multilinear form on columns, with the
  Leibniz formula as a theorem; eigentheory with eigenvalues defined
  independently of the determinant, Cayley–Hamilton, the minimal polynomial,
  Schur triangularisation, and the primary decomposition; inner product spaces
  through Cauchy–Schwarz, Gram–Schmidt, orthogonal projection, least squares and
  QR; and spectral theory through the real symmetric and normal spectral
  theorems, Courant–Fischer, positive definiteness, Sylvester's law of inertia,
  the SVD, the Moore–Penrose pseudoinverse, Eckart–Young, and the condition
  number. A 198-node acyclic graph. Every result carries the FIELD it actually
  needs (any_field / char_not_2 / ordered_field / real_or_complex /
  algebraically_closed) and its CHOICE GRADE, plus a typed statement, full
  hypotheses, a specialisation, a hypothesis-dropped counterexample, an explicit
  Lean status, and a source. Use when you need to know which hypothesis a matrix
  result actually rests on, over which field it holds, the minimum prerequisite
  chain for a theorem, or what breaks without finite-dimensionality. Built with
  the math-theorem-tree method; discharges math-statistics' linear_algebra_background.
version: 2.0.1
---

# Linear algebra — a dependency-ordered knowledge capsule

**Release 0.1.** 198 nodes, 599 `tsort` edges, acyclic (BSD stderr-checked),
0 isolated, 19 roots.

## Why this capsule exists

`math-statistics` Release 0.1 shipped with a single cited node,
`linear_algebra_background`, carrying eleven assumed facts and the note
"**FLAGGED for a future math-linear-algebra capsule**". This is that capsule.
All eleven are developed here, and all ten of that node's `tsort` consumers are
supplied — see [`edges/cross-capsule.md`](edges/cross-capsule.md) for the
discharge table and the per-consumer check.

## What is distinctive about this release

**Field scope is a first-class tag.** Every result records the field it actually
needs. This is not decoration: rank–nullity holds over any field, the
polarisation identity needs `char ≠ 2`, Sylvester's law of inertia needs an
order, Cauchy–Schwarz needs `R` or `C`, and the existence of an eigenvalue needs
algebraic closure. `indexes/field-scope-index.md` groups all 198 nodes by it.
Most textbook errors in applied linear algebra are field-scope errors made
silently.

**Finite-dimensionality is a hypothesis node, not an ambient assumption.** Eight
of the capsule's sharpest theorems fail without it, each with a standing
counterexample; `infinite_dimensional_boundary` catalogues them in one place.

**The foundational orderings are chosen, stated, and defended.** Eigenvalues are
defined by `Av = λv`, independently of the determinant. The determinant is
defined as the unique normalised alternating multilinear form on columns, with
Leibniz a theorem. Rank is `dim(im T)`, with the minor characterisation
downstream. Dimension is defined only *after* Steinitz proves it well-defined.
Five would-be cycles, all recorded with their resolutions in
[`edges/cycles.md`](edges/cycles.md).

**Three validation layers, each honest about its dimension.** Mathlib-free Lean
caps at `dim_core` (universal in the entries, n = 2); `bc` has no matrices at
all. So `validation/matrix-checks.m` (GNU Octave, 120 assertions) runs the
headline results at **n = 5, 6 square, 6×4 / 6×3 / 7×4 rectangular,
rank-deficient and defective** — where they stop being degenerate. Built with
the [`octave`](../octave/SKILL.md) skill's discipline: independent routes,
tolerances derived from conditioning, negative contrasts. It changes no
`lean_status` and proves nothing; see
[`validation/proof-checks.md`](validation/proof-checks.md) for the split.

**Lean overclaiming is structurally prevented.** A new `lean_status` value,
`dim_core`, marks results proved **universally in the matrix entries at a fixed
dimension** — stronger than a numeric instance, weaker than the theorem. One
authoritative map (`build/leanmap.py`) overrides every spec claim and forces
unmapped nodes to `cited`; `build/check-lean-refs.py` then verifies that every
named declaration exists in the `.lean` file. See
[`validation/proof-checks.md`](validation/proof-checks.md).

## Using it

| you want | look at |
|---|---|
| the prerequisite chain for a theorem | `indexes/prerequisite-paths.md` (87 headline results) |
| which field a result needs | `indexes/field-scope-index.md` |
| what breaks if a hypothesis is dropped | `indexes/counterexample-index.md`, or any node's `counterexamples_when_dropped` |
| every result depending on a hypothesis | `indexes/hypothesis-index.md` |
| where a symbol is used | `indexes/symbol-index.md` (`ptx` KWIC, `rg`-confirmed) |
| one result in full | `nodes/<id>.md` (readable) or `results/<id>.yaml` (structured) |
| what Lean actually verified | `validation/proof-checks.md` |
| the numbers | `validation/instance-checks.bc` (12 sections, `bc -l`) |
| the matrix results at realistic size | `validation/matrix-checks.m` (120 assertions, Octave) |

## Scope boundary

Finite-dimensional linear algebra over a field, through the SVD. **Excluded:**
infinite-dimensional functional analysis, modules over a ring, tensor and
exterior algebra, representation theory, and numerical linear algebra as a
discipline (conditioning and the LU pivoting caveat are in, as `diagnostic` and
`regime` nodes; stability analysis is cited, never proved). The Jordan normal
form is **stated, not proved** — a `draft` boundary node, with its prerequisites
(primary decomposition, nilpotent structure) developed. Full statement in
[`scope.md`](scope.md).

## Build and validation

```sh
sh build/all.sh
```

Runs the graph check and `tsort` with the BSD stderr cycle guard, regenerates
all 198 YAMLs and node pages from the specs (dependency lists read from the
graph, so they cannot drift), runs three consistency checkers, regenerates seven
indexes, type-checks the Lean file, and runs the `bc` instance checks —
**failing the build if any check reports a FAIL**, which requires inspecting the
output rather than the exit status, since `bc`'s `quit` always exits 0.

Current state: `tsort` clean, 0 isolated; `check-consistency` green;
`check-lean-refs` resolves 55 references against 87 declarations; Lean exits 0
with no `sorry`, no `axiom`, no warnings; all 12 `bc` sections pass; all 120
Octave matrix assertions pass. The Octave step **skips** (does not fail) when
`octave` is absent — it is a heavier dependency than `bc` and `lean`, and the
rest of the build must not depend on it.

## Standing limitations

A curated graph, not a complete account of the field. A valid `tsort` order
confirms only the encoded constraints, and is neither proof order nor
pedagogical order. A type check plus passing instances is not a proof; a
`dim_core` proof at n = 2 is evidence, not a theorem. Lean verified only the
formalised statements. Every result stays conditional on its hypotheses, the
foundational stance in [`conventions.md`](conventions.md), the notation
conventions, and its cited source.
