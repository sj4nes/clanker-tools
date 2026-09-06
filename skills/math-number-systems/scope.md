# Scope — Release 0.1

**The number systems: ℕ → ℤ → ℚ → ℝ, constructed and characterized.**

The capsule that discharges what [`math-real-analysis`](../math-real-analysis/SKILL.md)
takes on faith. Real Analysis I begins with "ℝ is a complete ordered field,
construction cited". This capsule *is* that construction: it builds ℤ from ℕ,
ℚ from ℤ, ℝ from ℚ, and proves the least-upper-bound property as a **theorem**
rather than assuming it as an axiom.

## Included

- **ℕ**: the Peano axioms (as `axiom` nodes); the **recursion theorem**;
  induction, strong induction, and the well-ordering principle and their
  equivalence; addition, multiplication, exponentiation, and order defined by
  recursion; the semiring and ordered-semiring laws; cancellation; no zero
  divisors; trichotomy; division with remainder.
- **ℤ**: the construction ℤ = (ℕ×ℕ)/∼ with (a,b) ∼ (c,d) iff a+d = b+c;
  operations well-defined on the quotient; ℤ as an **ordered integral domain**;
  ℕ embeds as a sub-semiring; cancellation; the well-ordering of sets bounded
  below; division with remainder in ℤ; gcd and Bézout.
- **ℚ**: the construction ℚ = (ℤ×ℤ\*)/∼ with (a,b) ∼ (c,d) iff ad = bc;
  operations well-defined; ℚ as an **ordered field** and the field of fractions
  of ℤ; lowest-terms representatives; the Archimedean property; density of the
  order; the absolute value and its triangle inequality; **√2 is irrational**;
  and the two forms of the incompleteness of ℚ — a bounded set with no
  supremum, and a Cauchy sequence with no limit.
- **ℝ (Dedekind cuts, canonical)**: a cut is a proper, downward-closed subset of
  ℚ with no greatest element; ℝ is the set of cuts; order by inclusion;
  addition and (sign-cased) multiplication of cuts; ℝ as an **ordered field**;
  ℚ embeds densely; the **least-upper-bound property** (the payoff: sup = union
  of cuts); the Archimedean property of ℝ; density of ℚ in ℝ; existence and
  uniqueness of nth roots of positives; **ℝ is uncountable**; and the
  **uniqueness theorem** — any two Dedekind-complete ordered fields are uniquely
  order-isomorphic.
- **ℝ (Cauchy completion)**: ℝ as Cauchy sequences of rationals modulo null
  sequences, recorded as an equivalent construction with the isomorphism
  theorem.
- **Cardinality** (the thread real analysis reuses): finite, countable,
  countably infinite; the pairing bijection ℕ×ℕ ≅ ℕ; ℤ and ℚ countable;
  countable unions of countable sets (via countable choice); Cantor's theorem
  (no surjection X → 𝒫(X)); the diagonal argument; ℝ uncountable;
  Schröder–Bernstein (stated).

## Excluded (out of scope for 0.1)

- The set-theoretic construction of ℕ itself (0 = ∅, n⁺ = n ∪ {n}, Infinity).
  This capsule takes the **Peano axioms as its floor**; a model is cited, not
  built. Formal logic, model theory, the ZFC axiom list, ordinals and cardinals
  beyond "countable / uncountable".
- ℂ and beyond (quaternions, p-adics, hyperreals, surreal numbers) — mentioned
  only as contrast (ℂ is a field that cannot be ordered).
- Everything downstream in analysis: limits, continuity, calculus. `ℝ`'s
  order-completeness is where this capsule stops and `math-real-analysis`
  starts.
- Category-theoretic universal properties beyond a one-line statement (field of
  fractions, completion).
- Nonstandard constructions of ℝ (Eudoxus reals / "almost homomorphisms",
  Conway's surreals).

## Level and audience

A "foundations of analysis" / "number systems" course: Landau *Grundlagen der
Analysis*; Rudin *Principles* ch. 1 + the appendix; Tao *Analysis I* ch. 2–5;
Enderton *Elements of Set Theory* ch. 4–5. The reader knows naive set theory,
functions and relations, and how to read a proof by induction.

## Foundational stance

- Working foundation: **ZFC**, used informally. `set`, `function`, `relation`,
  `equivalence_relation`, and the formation of **quotient sets** are
  primitive-level and not unfolded to the ∈-axioms.
- **ℕ** is characterized by the **Peano axioms** (`peano_axioms`), taken as
  `axiom` nodes; `natural_number` is "a system (N, 0, S) satisfying them". Any
  two such systems are uniquely isomorphic (a corollary of the recursion
  theorem) — so "the" natural numbers is well-posed. A set-theoretic model
  (finite von Neumann ordinals) exists and is **cited** ([enderton] ch. 4).
- **ℤ, ℚ, ℝ are constructed**, not assumed: each is a specific quotient set with
  specific operations, and each construction step carries an explicit
  well-definedness obligation (`well_defined_on_quotient`).
- **ℝ is built via Dedekind cuts** (canonical for this release — the
  least-upper-bound proof is shortest and is the point). The Cauchy-sequence
  completion is recorded as an `equivalent_to` construction with the
  isomorphism theorem `dedekind_cauchy_equivalent`.
- **Choice**: `axiom_of_choice` and `countable_choice` are first-class `axiom`
  nodes. Countable choice is used once essentially — "a countable union of
  countable sets is countable" — and that use is edged. The construction of ℝ,
  the field laws, and the least-upper-bound property are **choice-free**.
- **Numeral `0` vs `1`**: ℕ starts at **0** in this capsule (`peano_axioms`
  uses `0` and `S`), because the recursion theorem and the ℤ construction read
  more cleanly. `math-real-analysis` starts ℕ at 1; the embedding note in
  `conventions.md` records the shift.

## Proof policy

Proofs are **sketched** per node (technique + what it invokes). Purely
arithmetic / algebraic cores are checked with the `lean` skill. Because **no
Mathlib is available** here, Lean checks are either genuine `omega` / induction
proofs over `Nat` / `Int` (the ℕ and ℤ arithmetic and the quotient-relation
transitivity go through universally this way) or kernel-`decide`d instance
checks (√2-irrationality, the pairing bijection). `bc` worksheets compute the
constructions concretely and exhibit the incompleteness of ℚ.

## Epistemic-status policy

Labels: `axiom`, `definition`, `mathematical_identity`, `proved_theorem`,
`proved_lemma`, `proposition`, `corollary`, `constructive_result`. The
constructions of ℤ, ℚ, ℝ and the least-upper-bound property are
`constructive_result` (choice-free, and the objects are exhibited). `real_uncountable`
and `real_uniqueness` rest on a cited diagonal / back-and-forth argument.
`lean_status` per node records what this capsule's Lean file verified
(`core-arith` / `instance` / `cited` / `none`), separate from the epistemic
label.
