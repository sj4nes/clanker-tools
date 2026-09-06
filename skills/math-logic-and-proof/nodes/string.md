# string

## Type
primitive  (a root; `constructive_grade: intuitionistic`)

## Statement
A **string** (word, expression) is a **finite sequence of symbols** from the
alphabet. Strings are compared for equality, concatenated, and inspected
position by position. Wffs and terms are distinguished strings.

## Symbols
- a string `s = s₀ s₁ … s_{n−1}`; `|s| = n` its length; `ε` the empty string.

## Prerequisites (tsort edges into this node)
`symbol`, `finite_sequence`.

## Why primitive here
`string` = `finite_sequence` over the alphabet `symbol`; both are primitive
(finitistic metatheory, `conventions.md`). Everything syntactic is a string or a
finite tree of strings. Concatenation makes strings a **free monoid** on the
alphabet — the setting for the parenthesis-counting lemma of
`wff_unique_readability`.

## Constructive grade
`intuitionistic` — a finite list over a decidable set; all operations
(equality, length, prefix, concatenation) are computable.

## Lean status
`lean_status: core` (modelled). `validation/proof-checks.lean` skips the string
layer entirely by using the **abstract syntax tree** (`inductive Wff`) — which
is *equivalent* to strings-modulo-parsing, and avoids the parenthesis grammar.
The string↔AST correspondence is `wff_unique_readability` (cited for the string
direction).

## Type / well-formedness check
`well_formed`. A string is **finite** (definitional) — there are no infinite
expressions. Position access needs `0 ≤ i < |s|`. Concatenation is associative
with unit `ε`. "Substring", "prefix", "occurrence" are all defined on strings
and lift to wffs via `subformula` once unique readability holds.

## Specialization / boundary cases
- `|s| = 0`: the empty string `ε` (not a wff).
- `|s| = 1`: a single symbol; a wff iff that symbol is an atom.
- **prefixes**: the parenthesis lemma is a statement about *proper prefixes* of
  wff-strings.
- **AST view**: a wff-string ↔ its parse tree, bijectively, given
  `wff_unique_readability`.

## Hypothesis-dropped counterexamples
- **infinite string**: not a string here; `L_{ω₁,ω}` (infinitary logic) allows
  infinite conjunctions — out of scope, and it breaks `compactness` and
  `tautology_decidable`.
- **string over an undecidable alphabet**: equality/parsing not effective.
- **strings modulo an equivalence** (e.g. up to renaming): a *different* object
  — `alpha_equivalence` is that quotient for wffs, handled separately.

## Common misuse
Allowing infinite expressions; conflating a wff-string with its parse tree
before unique readability is established; treating concatenation as commutative;
assuming every string is a wff.

## Related nodes (non-prerequisite)
- `is`: `finite_sequence` over `symbol`; the free monoid on the alphabet.
- `builds`: `wff_syntax`, `term_syntax`, and derivations (`finite_sequence` of
  wff-strings).
- `quotiented_by`: `alpha_equivalence` (for wffs).

## Sources
[enderton_logic_2e] §1.1; [chiswell_hodges] ch. 2; [shoenfield] ch. 2.
