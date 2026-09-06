# Bibliography — Release 0.1

- **[landau]** E. Landau, *Foundations of Analysis* (*Grundlagen der Analysis*),
  1930; AMS Chelsea transl. 1951. The spine: Peano → ℕ arithmetic → ℚ (as pairs)
  → ℝ (Dedekind cuts) → ℂ, in ~130 pages of pure theorem–proof. This capsule's
  ℤ/ℚ constructions follow Landau's pair formulation.
- **[rudin_principles]** W. Rudin, *Principles of Mathematical Analysis*, 3rd
  ed., 1976. Chapter 1 + the Appendix: the Dedekind-cut construction of ℝ, the
  least-upper-bound property, ℝ Archimedean, ℚ dense, `nth_root_exists`
  (Theorem 1.21), and (ch. 2) countability, `nat × nat` countable, ℚ countable,
  ℝ uncountable. The `real_number`, `real_is_ordered_field`, `lub_property`,
  `nth_root_exists` nodes follow Rudin's Appendix.
- **[tao_analysis_I]** T. Tao, *Analysis I*, 4th ed., 2022. Chapters 2–5: Peano
  axioms and the recursion theorem stated carefully (ch. 2), ℤ and ℚ by
  equivalence classes with explicit well-definedness obligations (ch. 4), ℝ by
  **Cauchy sequences** of rationals (ch. 5), and an explicit treatment of AC /
  countable choice. The `cauchy_completion` node and the choice bookkeeping
  follow Tao.
- **[enderton]** H. Enderton, *Elements of Set Theory*, 1977. Chapters 4–5: the
  von Neumann construction of ℕ from ∅ and Infinity (the model this capsule
  **cites** for `peano_axioms`), the recursion theorem in set-theoretic form,
  and the constructions of ℤ, ℚ, ℝ. Also the cardinality chapter: Cantor's
  theorem, Schröder–Bernstein, countable unions.
- **[spivak_calculus]** M. Spivak, *Calculus*, 4th ed., 2008. The epilogue
  ("Dedekind cuts", "construction of the real numbers", "uniqueness of the real
  numbers") — a leisurely version of `real_uniqueness`.
- **[dedekind_1872]** R. Dedekind, *Stetigkeit und irrationale Zahlen*, 1872 —
  the original cut construction. **[dedekind_1888]** *Was sind und was sollen
  die Zahlen?*, 1888 — the recursion theorem and the categoricity of ℕ.
- **[cantor_1874]**, **[cantor_1891]** — G. Cantor's 1874 uncountability of ℝ
  and the 1891 diagonal argument.
- **[peano_1889]** G. Peano, *Arithmetices principia*, 1889 — the axioms.
- **[hardy_wright]** Hardy & Wright, *An Introduction to the Theory of Numbers*,
  6th ed. — `sqrt2_irrational` and its generalisations, unique factorisation.
- **[jech_set_theory]** T. Jech, *Set Theory*, 3rd ed. — the Feferman–Levy model
  where ℝ is a countable union of countable sets (why `countable_union_countable`
  needs countable choice).

## Convention clashes

- **ℕ from 0 or 1**: Landau, Tao start at... Landau starts at 1; Tao at 0;
  Enderton at 0. This capsule uses **0** (`peano_axioms` with `0, S`).
  `math-real-analysis` uses 1 — the embedding note in `conventions.md` records
  the shift.
- **ℝ via cuts (Landau, Rudin, Dedekind) vs Cauchy sequences (Tao, Cantor)**:
  this capsule makes **cuts canonical** (the `lub_property` proof is one line)
  and records the Cauchy completion as an equivalent construction
  (`dedekind_cauchy_equivalent`).
- **Second-order vs first-order induction**: this capsule uses the second-order
  Peano axiom (so ℕ is categorical); first-order PA and its non-standard models
  are out of scope.
