# equality_axioms

## Type
axiom  (epistemic status: `axiom` — logical axioms; `constructive_grade:
intuitionistic`)

## Statement
The **logical axioms of equality** (valid in every structure because `=` is
identity — `first_order_logic_with_equality`):
- **reflexivity**: `x = x` (equivalently `∀x (x = x)`);
- **substitution schema**: `x = y → (φ → φ')` where `φ'` is `φ` with **some**
  free occurrences of `x` replaced by `y` (both free for the substitution).

Derived: symmetry `x = y → y = x`, transitivity `x = y ∧ y = z → x = z`, and the
function/relation congruences `x⃗ = y⃗ → f x⃗ = f y⃗`, `x⃗ = y⃗ → (R x⃗ ↔ R y⃗)`.

## Symbols
- `x`, `y`: variables; `φ`, `φ'`: wffs.

## Prerequisites (tsort edges into this node)
`first_order_logic_with_equality`, `substitution`.

## Content
These are **logical** axioms (part of the calculus, valid in every structure),
not axioms of a particular theory. They are what let `=` behave like identity in
*proofs*, and they are precisely what makes the **`term_model` quotient**
well-defined (`t ≈ u :⟺ (t = u) ∈ T` is a congruence — `equality_congruence`).

## Constructive grade
`intuitionistic` — reflexivity and the substitution schema are Horn / positive;
Lean's `rfl` and `▸` are exactly these.

## Lean status
`lean_status: core` (the mechanism). Lean: `Eq.refl` / `rfl` (reflexivity),
`Eq.subst` / `▸` / `congrArg` / `congrFun` (the substitution schema and its
instances) — used pervasively in `validation/proof-checks.lean`. The FOL
object-level axioms are `cited`.

## Type / well-formedness check
`well_formed`. The substitution schema needs the replacements to be at **free**
occurrences and `y` **free for** the replaced `x` (`free_for`) — capture would
break it. "Some" occurrences (not necessarily all) may be replaced.

## Specialization / boundary cases
- symmetry: instantiate the schema with `φ = (x = x)`, `φ' = (y = x)`; combine
  with reflexivity.
- Leibniz: `x = y → (P(x) ↔ P(y))` is the schema for `φ = P(x)`.
- in **arithmetic**: `x = y → S x = S y`, `x = y → x + z = y + z`, etc. are the
  congruence instances used constantly.
- **theory-level equality axioms** are unnecessary — equality is logical here;
  in equality-free FOL you *add* them as non-logical axioms and work up to the
  quotient.

## Hypothesis-dropped counterexamples
- **drop reflexivity**: `x = x` unprovable; nothing forces `=` to relate an
  element to itself.
- **substitution schema without `free_for`**: `x = y → (∃y (y ≠ x) → ∃y (y ≠
  y))` — capture makes an invalid "axiom".
- **`=` not identity** (equality-free FOL): these become *non-logical* axioms
  that a structure may or may not satisfy; `equality_congruence` is then not
  automatic.

## Common misuse
Adding equality axioms as theory axioms when `=` is already logical; skipping
the `free_for` guard on the schema; replacing bound occurrences; assuming
symmetry/transitivity are separate primitives (they are derived).

## Related nodes (non-prerequisite)
- `entailed_by`: `first_order_logic_with_equality`.
- `yields`: `equality_congruence`, symmetry, transitivity.
- `enables`: the `term_model` quotient.
- `part_of`: `derivability_fol`.

## Sources
[enderton_logic_2e] §2.4; [mendelson_6e] ch. 2; [chiswell_hodges] ch. 5.
