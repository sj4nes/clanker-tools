# skolem_paradox

## Type
diagnostic  (epistemic status: `metatheorem` consequence / expository; **not a
paradox** — a resolved apparent contradiction; `constructive_grade: n/a`)

## Statement
If `ZFC` is consistent, it has a **countable** model `𝔐` (`lowenheim_skolem_down`).
Inside `𝔐` there is an element `𝔐 ⊨ "x is uncountable"` (e.g. `𝔐`'s version of
`ℝ` or of `𝒫(ω)`). Apparent contradiction: how can a *countable* model contain
an *uncountable* set?

**Resolution**: "`x` is uncountable" means "there is **no bijection** `ω → x`".
`𝔐` is countable *from outside* — an external bijection `ω → |𝔐|` exists — but
the bijection `ω → x^𝔐` that would witness `x^𝔐` countable is **not an element
of `𝔐`**. Countability is **not absolute** between `𝔐` and `V`.

## Symbols
- `𝔐`: a countable model of `ZFC`.
- `x^𝔐`: an element `𝔐` believes is uncountable.
- "absolute": a formula `φ(x)` is absolute for `𝔐` if `φ^𝔐(a) ⟺ φ(a)` for all
  `a ∈ 𝔐`.

## Prerequisites (tsort edges into this node)
`lowenheim_skolem_down`.

## What is going on
- `Δ₀` (bounded) formulas are absolute; "is a bijection" and "is uncountable"
  are **Σ₁ / Π₁ with unbounded quantifiers** and are **not** absolute.
- `𝔐` is missing witnesses: it has `x^𝔐` and it has `ω^𝔐`, but the *function*
  pairing them, though it exists in `V`, is not one of `𝔐`'s sets.
- So `𝔐 ⊨ "x^𝔐 is uncountable"` is true *in `𝔐`* and false *in `V`* — and both
  statements are consistent because they are about **different** collections of
  bijections.

## Constructive grade
`n/a` — a diagnostic node about a consequence of downward LS; no proof
obligation of its own.

## Lean status
`lean_status: none`. Expository.

## Type / well-formedness check
`well_formed` as an observation. The key type distinction: "countable" is a
predicate on sets **relative to a domain of candidate bijections** — `𝔐`'s
answer and `V`'s answer use different domains, so they can differ without
contradiction.

## Specialization / boundary cases
- the **transitive** countable models (given a stronger hypothesis than mere
  `Con(ZFC)`): even here `𝒫(ω)^𝔐 ⊊ 𝒫(ω)` — the model's power set of `ω` is a
  proper, countable subset of the real one.
- **forcing** exploits exactly this: start with a countable transitive model,
  add a generic subset of `ω` that codes a bijection collapsing a cardinal.
- non-standard models of `PA`: the analogous "there is a number bigger than
  every numeral" is the arithmetic cousin — non-absoluteness of "standard".

## Hypothesis-dropped / misreadings
- **"therefore ZFC is inconsistent"**: no — the two truth values are about
  different bijection-collections.
- **"therefore there is no such thing as uncountability"**: no — `V ⊨ "ℝ is
  uncountable"` still holds; `𝔐` is just an impoverished picture.
- **"the countable model is the real universe"**: `𝔐` is a set model; `V` is
  not a set.
- expecting `𝔐` to be **transitive** or **well-founded** — a bare LS model need
  not be.

## Common misuse
Citing it as evidence against set theory or against Cantor; conflating "`𝔐`
thinks `x` is uncountable" with "`x` is uncountable"; assuming `𝔐`'s ordinals /
cardinals match `V`'s; forgetting that the missing object is a *function*, not a
set of the right size.

## Related nodes (non-prerequisite)
- `consequence_of`: `lowenheim_skolem_down`.
- `related`: non-absoluteness, `forcing` (out of scope), the arithmetic analogue
  (non-standard models, `compactness_fol`).
- `contrast`: `cantor_theorem` / `cantor_diagonal`
  (`math-sets-functions-cardinality`) — still true; `𝔐` just cannot see the
  diagonal function.

## Sources
[bbj_5e] ch. 12; [enderton_logic_2e] §2.6; Skolem (1922);
[kunen_set_theory] ch. IV (absoluteness).
