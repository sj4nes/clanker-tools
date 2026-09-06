# Master symbol list — Release 0.1

| Symbol | Meaning | Type | Area |
|---|---|---|---|
| `∈`, `∉` | membership | relation | sets |
| `∅` | the empty set | set | sets |
| `{a, b}`, `{x : φ(x)}` | pairing; separation (`{x ∈ X : φ}`) | set | sets |
| `⊆`, `⊊` | subset, strict subset | relation | sets |
| `𝒫(X)` | power set | set | sets |
| `X ∪ Y`, `X ∩ Y`, `X ∖ Y` | binary union, intersection, difference | set | sets |
| `⋃ 𝓕`, `⋂ 𝓕` | union / intersection of a family (`⋂` needs `𝓕 ≠ ∅`) | set | sets |
| `⋃_{i∈I} A_i`, `⋂_{i∈I} A_i` | indexed union / intersection | set | sets |
| `Xᶜ` | complement relative to an ambient `U` (`Xᶜ = U ∖ X`) | set | sets |
| `(a, b)` | Kuratowski ordered pair `{{a},{a,b}}` | set | sets |
| `X × Y` | Cartesian product | set | sets |
| `X ⊔ Y` | disjoint union `(X×{0}) ∪ (Y×{1})` | set | sets |
| `R`, `x R y` | a relation; `(x,y) ∈ R` | set of pairs | relations |
| `dom R`, `ran R` | domain, range | set | relations |
| `R⁻¹`, `S ∘ R` | inverse and composite relations | relation | relations |
| `∼`, `[x]`, `[x]_∼` | an equivalence relation; the class of `x` | relation; set | equivalence |
| `X/∼` | quotient set | set | equivalence |
| `π : X → X/∼` | canonical projection `x ↦ [x]` | function | equivalence |
| `f : X → Y` | a function with fixed codomain `Y` | function | functions |
| `f[A]`, `f '' A` | image `{ f(x) : x ∈ A }` | set | functions |
| `f⁻¹[B]`, `f ⁻¹' B` | preimage `{ x : f(x) ∈ B }` — defined for every `f` | set | functions |
| `id_X` | the identity function on `X` | function | functions |
| `f⁻¹` (function) | the inverse function — exists iff `f` is a bijection | function | functions |
| `g ↾ A` | restriction of `g` to `A` | function | functions |
| `Y^X`, `2^X` | the set of functions `X → Y` (resp. `X → {0,1}`) | set | functions |
| `1_A`, `χ_A` | characteristic / indicator function `X → {0,1}` | function | functions |
| `≤`, `<`, `⊑` | a partial / strict / abstract order | relation | orders |
| `sup S`, `inf S`, `max S`, `min S` | least upper bound, etc. | element | orders |
| `ω` | the smallest inductive set `= ℕ` | set (ordinal) | naturals |
| `0`, `S` | `∅` and `x ↦ x ∪ {x}` | element of ω; function | naturals |
| `α`, `β`, `λ` | ordinals; `λ` a limit ordinal | set (ordinal) | ordinals |
| `\|X\|` | cardinality | — | cardinality |
| `\|X\| = \|Y\|`, `X ≈ Y` | equinumerous (a bijection exists) | — | cardinality |
| `\|X\| ≤ \|Y\|`, `\|X\| < \|Y\|` | an injection exists; injection but no bijection | — | cardinality |
| `ℵ₀` | `\|ℕ\|` | cardinal | cardinality |
| `ℵ_α` | the `α`-th infinite well-ordered cardinal | cardinal | cardinality |
| `𝔠` | `2^ℵ₀ = \|ℝ\| = \|𝒫(ℕ)\|`, the continuum | cardinal | cardinality |
| `ℶ_α` | the beth numbers (`ℶ₀ = ℵ₀`, `ℶ_{α+1} = 2^{ℶ_α}`) | cardinal | cardinality |

## Structure names (the `structure` nodes)

`zf` (the nine ZF axioms) ⊂ `zfc` (ZF + Choice). `partial_order` ⊂
`total_order` ⊂ `well_order`; `strict_order` is the irreflexive counterpart.

Identifier-atomicity note for the `ptx` symbol index: `preimage`, `injective`,
`aleph_0`, `x_i`, `csb` are indexed whole via `ptx -W '[A-Za-z_][A-Za-z0-9_]*'`.
Confirm every hit with `rg`.
