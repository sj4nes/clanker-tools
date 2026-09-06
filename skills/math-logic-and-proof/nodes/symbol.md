# symbol

## Type
primitive  (a root of the capsule; `constructive_grade: intuitionistic`)

## Statement
A **symbol** is an element of a fixed **countable alphabet**. The alphabet
partitions into: logical symbols (`¬ ∧ ∨ → ↔ ∀ ∃ =`), punctuation (`( )` `,`),
a countable supply of **variables** `v₀, v₁, …`, and — for a first-order
language — the non-logical symbols of a `signature` (constants, function
symbols, relation symbols).

## Symbols
- the alphabet: a fixed countable set, with **decidable equality** of symbols.

## Prerequisites (tsort edges into this node)
none — **primitive**.

## Why primitive here
Symbols are the atoms of syntax. The capsule's foundational stance
(`conventions.md`) takes finite combinatorics — symbols, strings, finite
sequences — as the true floor: it is finitistic and uncontroversial, and it is
*below* everything the number-systems / set capsules construct. A symbol has no
internal structure the metatheory needs; only "which symbol is it" (decidable)
and "is it logical / a variable / from the signature".

## Constructive grade
`intuitionistic` — a symbol is drawn from a decidable countable set.

## Lean status
`lean_status: core` (modelled). `validation/proof-checks.lean` uses `Nat` for
atoms/variables (`Wff.atom : Nat → Wff`, `v : Nat → Bool`) — `Nat` is the
concrete countable alphabet, with `DecidableEq`.

## Type / well-formedness check
`well_formed`. Requirements: the alphabet is **countable** (so there are
countably many wffs, hence `tautology_decidable` per wff and a Lindenbaum
enumeration for a countable language); symbol equality is **decidable** (so
parsing is effective); the logical / variable / signature classes are disjoint
and recognisable.

## Specialization / boundary cases
- **propositional**: alphabet = `{¬, ∧, ∨, →, ↔, (, )}` ∪ `{p₀, p₁, …}` (atoms).
- **first-order**: add `{∀, ∃, =, ,}` and the signature symbols.
- **uncountable languages** (used in `lowenheim_skolem_up`, some completeness
  arguments): the alphabet is a countable *template* plus an index set of
  cardinality `κ` — the "countable" requirement is relaxed there, and the
  Lindenbaum step correspondingly needs choice.

## Hypothesis-dropped counterexamples
- **uncountable alphabet with no structure**: syntax is no longer effectively
  enumerable; `lindenbaum_lemma_prop`'s "enumerate the wffs" fails and needs
  Zorn.
- **undecidable symbol equality**: parsing is not effective; `tautology_decidable`
  breaks.
- **overlapping classes** (a symbol that is both a connective and a variable):
  the case analysis in `wff_unique_readability` collapses.

## Common misuse
Treating symbols as having semantic content (they are marks; meaning is assigned
by `truth_assignment` / `structure`); assuming an infinite *string* is allowed
(only the alphabet is infinite, each string is finite); forgetting the
countability assumption when moving to uncountable languages.

## Related nodes (non-prerequisite)
- `builds`: `string`, and via it `wff_syntax`, `term_syntax`.
- `classified_by`: logical / variable / `signature`.
- `related`: Gödel numbering (an effective bijection alphabet-strings → `ℕ`,
  used in the boundary block — out of scope to build).

## Sources
[enderton_logic_2e] §1.1, §2.1; [chiswell_hodges] ch. 2; [shoenfield] ch. 2.
