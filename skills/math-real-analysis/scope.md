# Scope — Release 0.1

**Real Analysis I: the real line, sequences, series, continuity, differentiation,
Riemann integration, and uniform convergence.**

## Included

- The real numbers as a **complete ordered field**. The least-upper-bound
  property is taken as the completeness **axiom** (`lub_axiom`); a construction
  of ℝ (Dedekind cuts / Cauchy completion of ℚ) is **cited, not built**. ℚ is
  taken as a given ordered field. ℕ is primitive with the Peano axioms;
  induction is a derived principle node.
- Consequences of completeness: Archimedean property, density of ℚ, the
  nested-interval theorem.
- **Sequences** in ℝ: convergence (ε–N), uniqueness of limits, boundedness,
  the algebra of limits, the squeeze theorem, monotone convergence,
  subsequences, Bolzano–Weierstrass, Cauchy sequences and the Cauchy
  convergence criterion, `limsup`/`liminf`.
- **Series** of real numbers: partial sums, convergence, the geometric series,
  the nth-term test, the Cauchy criterion, the comparison / ratio / root tests,
  absolute vs conditional convergence, the alternating series test, the
  p-series.
- **Topology of ℝ** (subsets only): open sets, closed sets, limit points,
  closure, open covers, compactness, Heine–Borel, sequential compactness,
  connectedness, "connected ⟺ interval".
- **Limits and continuity** of functions ℝ ⊇ D → ℝ: ε–δ limits, the sequential
  criterion, continuity, the algebra and composition of continuous functions,
  continuous image of a compact set, the extreme value theorem, the
  intermediate value theorem, uniform continuity, Heine–Cantor.
- **Differentiation** on ℝ: the derivative, differentiable ⇒ continuous, the
  sum/product/quotient rules, the chain rule, Fermat's interior-extremum
  theorem, Rolle's theorem, the mean value theorem, monotonicity from the sign
  of the derivative, the Cauchy mean value theorem, L'Hôpital's rule, Taylor's
  theorem with the Lagrange remainder.
- **Riemann integration** on a compact interval via Darboux sums: the integral,
  the Riemann (Cauchy) criterion, integrability of continuous and of monotone
  functions, linearity, interval additivity, monotonicity, the integral mean
  value theorem, both parts of the fundamental theorem of calculus, integration
  by parts, the substitution rule.
- **Sequences and series of functions**: pointwise vs uniform convergence, the
  uniform Cauchy criterion, the Weierstrass M-test, the uniform limit of
  continuous functions is continuous, interchange of uniform limit with
  integral and with derivative, power series and the radius of convergence.

## Excluded (out of scope for 0.1)

- Metric-space or general-topological generality beyond subsets of ℝ.
- ℝⁿ, multivariable limits / continuity / differentiation, line and surface
  integrals.
- Lebesgue measure and integration; ℒ^p spaces.
- Complex analysis; Fourier series and transforms.
- Functional analysis (Banach / Hilbert spaces, operator theory).
- The construction of ℝ, ℚ, ℤ from ℕ or from sets; formal logic and model
  theory; ordinals and cardinals beyond "countable".
- Numerical analysis (error bounds of specific quadrature / root-finding
  schemes) — a later applied release.

## Level and audience

Upper-undergraduate / first-graduate real analysis (Rudin *Principles* ch. 1–8;
Abbott *Understanding Analysis*; Tao *Analysis I*). The reader knows
naive set theory, functions, induction, and basic ℚ arithmetic.

## Foundational stance

- Working foundation: **ZFC**, used informally. Sets and functions are
  primitive-level; we do not unfold them to the axioms of ZFC.
- **ℕ** primitive (Peano). **ℚ** primitive as an ordered field. **ℝ** primitive,
  characterized by the ordered-field axioms plus `lub_axiom`; its existence and
  uniqueness-up-to-isomorphism are **cited**.
- **Choice**: the capsule is written to *avoid* the axiom of choice where a
  choice-free proof of equal strength exists (the ℝ¹ Bolzano–Weierstrass proof
  is by bisection, not by "pick a point in each"). Where a standard proof uses
  **countable choice** (e.g. extracting a sequence witnessing a limit point,
  or the sequential characterization of closure), the result carries a
  prerequisite edge to `countable_choice` and the alternative choice-free route
  (if any) is noted. `axiom_of_choice` and `countable_choice` are first-class
  axiom nodes so every use is visible in the graph.

## Proof policy

Proofs are **sketched** in each node's detail page (technique + the results the
sketch invokes). Purely algebraic / arithmetic steps inside a proof are
checked with the `lean` skill; because **no Mathlib is available** in this
environment, Lean checks are kernel-`decide`d **instance checks over ℤ/ℕ at
sample values** (labelled as such — an instance check is not a universal
proof), plus a handful of `Nat`/`List` inductions in plain Lean. Any node whose
`lean_status` is not `proved` keeps an epistemic label no stronger than the
sketch and cited source support. `bc` worksheets compute specializations and
**hypothesis-dropped counterexamples**.

## Epistemic-status policy

Every result node carries one label from: `axiom`, `definition`,
`mathematical_identity`, `proved_theorem`, `proved_lemma`, `proposition`,
`corollary`, `constructive_result`, `nonconstructive_result`. No `conjecture` /
`open_problem` nodes — everything in scope is classical and settled. A result
is labelled `proved_theorem` / `proved_lemma` only on the strength of a cited,
standard, checked proof; `lean_status` records separately what *this capsule's*
Lean file actually verified. `nonconstructive_result` marks the results whose
standard proof uses `lub_axiom` non-constructively or uses `countable_choice`.
