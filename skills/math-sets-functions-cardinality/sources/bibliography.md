# Bibliography — Release 0.1

- **[enderton]** H. Enderton, *Elements of Set Theory*, Academic Press, 1977.
  The spine. Ch. 2–3 (sets, relations, functions), ch. 4 (`ω` from Infinity,
  the recursion theorem, `peano_holds_in_omega`), ch. 5 (ℤ, ℚ, ℝ — the part
  this capsule *hands off* to `math-number-systems`), ch. 6 (cardinality:
  equinumerosity, CSB, Cantor's theorem, countable sets), ch. 7 (orderings,
  ordinals), ch. 8 (AC, its equivalents, cardinal arithmetic). Convention: `ℕ`
  from 0; von Neumann ordinals.
- **[halmos]** P. Halmos, *Naive Set Theory*, Van Nostrand, 1960. The prose
  companion — the axioms stated informally, Zorn's lemma and the well-ordering
  theorem, the arithmetic of `ℵ₀`. Used for the order-theory framing.
- **[jech_set_theory]** T. Jech, *Set Theory*, 3rd millennium ed., Springer,
  2003. Ch. 1–5 for the harder results: Hartogs' number, the aleph hierarchy,
  cardinal arithmetic (`κ·κ = κ`), the Feferman–Levy model (why
  `countable_union_countable` needs countable choice), and the *statements* of
  Gödel's and Cohen's independence results for CH and AC.
- **[kunen_set_theory]** K. Kunen, *Set Theory* (2011). Cross-check for the ZF
  axiom schema formulations (Separation, Replacement) and the forcing statement
  for `¬CH` (cited, not developed).
- **[enderton_logic]** H. Enderton, *A Mathematical Introduction to Logic*, 2nd
  ed. The logic floor: propositional and predicate logic, quantifier rules,
  classical vs intuitionistic (for `quantifier_negation`'s classicality note).
  This capsule *uses* this material; `math-logic-and-proof` would develop it.
- **[dedekind_1888]** R. Dedekind, *Was sind und was sollen die Zahlen?*, 1888
  — the recursion theorem and the categoricity of `ℕ` (via minimality).
- **[cantor_1891]** G. Cantor, *Über eine elementare Frage der
  Mannigfaltigkeitslehre*, 1891 — the diagonal argument and `|X| < |𝒫(X)|`.
- **[zermelo_1904]** E. Zermelo, *Beweis, dass jede Menge wohlgeordnet werden
  kann*, 1904 — AC and the well-ordering theorem.
- **[zorn_1935]** M. Zorn, *A remark on method in transfinite algebra*, 1935.
- **[godel_1940]** K. Gödel, *The Consistency of the Continuum Hypothesis*,
  1940 — `L ⊨ ZFC + GCH`. **[cohen_1966]** P. Cohen, *Set Theory and the
  Continuum Hypothesis*, 1966 — forcing, `Con(ZFC) → Con(ZFC + ¬CH)`.
- **[herrlich_axiom_of_choice]** H. Herrlich, *Axiom of Choice*, Springer LNM
  1876, 2006 — the catalogue of what breaks in ZF without AC (used for the
  `axiom_of_choice` counterexamples).
- **[munkres]** J. Munkres, *Topology*, 2nd ed. — ch. 1–2, the working
  set-theory / function chapter that downstream topology (and
  `math-real-analysis`'s topology area) assumes; source for the
  `preimage_algebra` framing.

## Convention clashes

- **`ℕ` from 0 or 1**: Enderton, this capsule — **0**. `math-real-analysis` —
  1. Recorded in `conventions.md`.
- **ℝ construction**: out of scope here — this capsule stops at `ω` and hands
  the number-system constructions to `math-number-systems` (Dedekind cuts) /
  cites Enderton ch. 5.
- **Separation / Replacement as schemas**: this capsule treats them as `axiom`
  nodes representing the schema, used only at named instances — it does not
  develop the metatheory of schemas (that is `math-logic-and-proof`).
- **"countable" includes finite**: Enderton, Jech, this capsule. Some analysis
  texts mean "countably infinite" — recorded on `countable_set`.
