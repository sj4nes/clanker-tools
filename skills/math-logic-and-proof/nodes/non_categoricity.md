# non_categoricity

## Type
example  (epistemic status: `metatheorem` consequence; `constructive_grade:
needs_full_classical`)

## Statement
No first-order theory `T` that has an **infinite** model is **categorical**
(i.e. has, up to isomorphism, exactly one model). More precisely:
- `T` with an infinite model has models of every cardinality `≥ max(ℵ₀, |ℒ|)`
  (`lowenheim_skolem_up` + `lowenheim_skolem_down`), and models of different
  cardinalities cannot be isomorphic — so `T` has `≥ 2` non-isomorphic models.
- Even **`κ`-categoricity** (unique model of size `κ`) does not give full
  categoricity, and by Łoś–Vaught a theory `κ`-categorical for some infinite
  `κ` with no finite models is **complete** — but still not categorical.

## Symbols
- `T`: a first-order `ℒ`-theory with an infinite model.
- "categorical": all models isomorphic.
- "`κ`-categorical": all models of cardinality `κ` isomorphic.

## Prerequisites (tsort edges into this node)
`compactness_fol`, `lowenheim_skolem_up`.

## Why it matters
First-order logic **cannot uniquely describe** any infinite structure:
- **`(ℕ, 0, S, +, ·, <)`** — `PA` has non-standard models (countable ones by
  compactness, and of every infinite cardinality). No first-order theory has
  `ℕ` as its only model.
- **`(ℝ, +, ·, <)`** — real closed field theory is complete but has countable
  models and huge models; "the reals" are not first-order-pinnable.
- **`(ℂ, +, ·)`** — ACF₀ is `κ`-categorical for every uncountable `κ` (Steinitz:
  transcendence degree determines the field), hence complete — the cleanest
  example of uncountable categoricity **without** full categoricity (the
  countable models, of transcendence degree `0, 1, 2, …, ℵ₀`, are not all
  isomorphic).

Contrast **second-order** logic: second-order `PA` **is** categorical (Dedekind)
— but SOL has no complete proof system (`godel_completeness_theorem` fails for
SOL). You get categoricity **or** a complete calculus, not both.

## Constructive grade
`needs_full_classical` — via the LS theorems.

## Lean status
`lean_status: cited`. Mathlib has the Łoś–Vaught test and `κ`-categoricity
infrastructure for some theories.

## Type / well-formedness check
`well_formed`. Needs `T` to have an **infinite** model (theories with only
finite models — "exactly `n` elements" — are trivially categorical in each
finite size, and can even be categorical outright). "Isomorphic" is the
structure-preserving bijection, not elementary equivalence.

## Specialization / boundary cases
- **finite models**: "the theory of a 5-element set with no structure" is
  categorical — the infinite-model hypothesis is what forces non-categoricity.
- **countably categorical theories** (Ryll-Nardzewski): dense linear orders
  without endpoints, the random graph, `(ℤ, S)` — unique *countable* model, but
  uncountable models exist and differ.
- **strongly minimal / uncountably categorical**: ACF₀, vector spaces over a
  fixed field, `(ℤ, +)` — Morley's theorem: `κ`-categorical for one uncountable
  `κ` ⟹ for all.

## Hypothesis-dropped counterexamples
- **drop "infinite model"**: theories axiomatising a single finite structure are
  categorical — the phenomenon is entirely about infinite models.
- **switch to second-order logic**: second-order `PA`, second-order real-closed
  fields, second-order `ZFC` (with a caveat) **are** categorical / quasi-
  categorical — at the cost of completeness.
- **switch to `L_{ω₁,ω}`**: `ℕ` **is** the unique model of a single
  `L_{ω₁,ω}`-sentence ("every element is `0` or `S0` or `SS0` or …").

## Common misuse
Believing a first-order theory "defines" `ℕ` or `ℝ`; conflating completeness
(decides every sentence) with categoricity (one model); thinking uncountable
categoricity implies categoricity; forgetting the second-order categoricity
results come with no proof system.

## Related nodes (non-prerequisite)
- `consequence_of`: `lowenheim_skolem_up` + `lowenheim_skolem_down`.
- `contrast_with`: second-order `godel_completeness_theorem` failure; `L_{ω₁,ω}`.
- `related`: Morley's categoricity theorem, Łoś–Vaught test, Ryll-Nardzewski
  (all out of scope — model theory proper).

## Sources
[chiswell_hodges] ch. 6; [hodges_shorter] §§2.3, 4.2; [enderton_logic_2e] §2.6;
[bbj_5e] ch. 12.
