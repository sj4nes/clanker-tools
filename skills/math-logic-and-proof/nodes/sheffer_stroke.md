# sheffer_stroke

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`)

## Statement
The single connective `↑` (**NAND**, Sheffer stroke: `p ↑ q ≡ ¬(p ∧ q)`) is
**functionally complete** — every Boolean function is expressible using `↑`
alone. Likewise `↓` (**NOR**, Peirce arrow / Quine dagger: `p ↓ q ≡ ¬(p ∨ q)`).
These are the **only** binary connectives that are complete singletons.

## Symbols
- `↑`: NAND; `↓`: NOR.

## Prerequisites (tsort edges into this node)
`functional_completeness`, `de_morgan_prop`, `binary_boolean_functions_16`.

## Proof
Express a complete basis from `↑`:
- `¬p ≡ p ↑ p`;
- `p ∧ q ≡ ¬(p ↑ q) ≡ (p ↑ q) ↑ (p ↑ q)`;
- `p ∨ q ≡ ¬p ↑ ¬q ≡ (p ↑ p) ↑ (q ↑ q)` (De Morgan).
Since `{¬, ∧, ∨}` is complete (`functional_completeness`), so is `{↑}`.
Dually for `↓`. That no **other** binary connective is a complete singleton:
each of the other 14 either preserves `T` (`p ∧ q`, `p ∨ q`, `p → q`, `↔`, …) or
preserves `F`, or is affine/monotone/self-dual — falling in a maximal Post class
(`functional_completeness` type check).

## Constructive grade
`intuitionistic` — the reductions are equivalences of `Bool` expressions,
`by cases <;> rfl`.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`nand a b := ! (a && b)`, and
`not_from_nand : (!a) = nand a a`,
`and_from_nand : (a && b) = nand (nand a b) (nand a b)`,
`or_from_nand : (a || b) = nand (nand a a) (nand b b)`
— each `by cases a <;> cases b <;> rfl`. Together with `binary_dnf` (every
binary `f` has a `{¬,∧,∨}` form) this gives `{↑}`-completeness for the binary
case.

## Type / well-formedness check
`well_formed`. `↑` is a genuine binary connective (`p ↑ q ≡ ¬(p ∧ q)`), not an
abbreviation-only device. Every `↑`-formula built from `n` atoms computes some
`n`-ary Boolean function; completeness says *all* of them are reached.

## Specialization / boundary cases
- `p ↑ p ≡ ¬p`; `p ↑ (q ↑ q) ≡ p ↑ ¬q ≡ ¬(p ∧ ¬q) ≡ p → q` — implication in 2
  strokes.
- `(p ↑ q) ↑ (p ↑ q) ≡ p ∧ q`.
- **hardware**: a NAND (or NOR) gate is *universal* — every combinational
  circuit is a NAND network; this theorem is why.
- **only these two**: no unary connective is complete (`¬` gives only `id`/`¬`);
  among binary, exactly `↑` and `↓`.

## Hypothesis-dropped counterexamples
- **`{→}` alone**: not complete — every `→`-formula is `T` when all atoms are
  `T` (preserves `T`), so `⊥` is inexpressible.
- **`{↔, ¬}`**: affine only — `∧` inexpressible.
- **`{∧, ∨}`**: monotone only — `¬` inexpressible.
- **`{↑, ↓}` together** is complete but redundant; neither is redundant alone.

## Common misuse
Believing `→` or `↔` alone is complete; thinking you need both `↑` and `↓`;
miscounting stroke depth (`¬` is `p↑p`, not `p↑⊥`); assuming a NAND network is
automatically minimal (universality ≠ minimality — Quine–McCluskey).

## Related nodes (non-prerequisite)
- `special_case_of`: `functional_completeness`.
- `uses`: `de_morgan_prop`.
- `related`: NAND/NOR gate universality (digital design); Post's lattice (why
  only `↑`, `↓`).

## Sources
[enderton_logic_2e] §1.5; Sheffer (1913); Peirce (1880, unpublished);
[chiswell_hodges] ch. 3.
