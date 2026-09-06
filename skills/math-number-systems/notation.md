# Master symbol list — Release 0.1

| Symbol | Meaning | Type | Area |
|---|---|---|---|
| `∅` | empty set | set | foundations |
| `𝒫(X)` | power set of `X` | set | foundations |
| `X × Y` | Cartesian product | set | foundations |
| `∼` | an equivalence relation (subscripted by construction: `∼_ℤ`, `∼_ℚ`) | relation | foundations |
| `[x]`, `[x]_∼` | equivalence class of `x` | set | foundations |
| `X/∼` | quotient set | set | foundations |
| `f : X → Y` | a function | function | foundations |
| `f ↾ A` | restriction of `f` to `A` | function | foundations |
| `ℕ` | natural numbers, **including 0** | set (Peano system) | naturals |
| `0`, `S` | zero and successor | element of ℕ; function ℕ→ℕ | naturals |
| `n⁺` | `S n`, the successor of `n` | element of ℕ | naturals |
| `a + b`, `a · b`, `aᵇ` | ℕ operations, defined by recursion | element of ℕ | naturals |
| `a ≤ b` | `∃ c, a + c = b` | proposition | naturals |
| `ℕ⁺` | `ℕ ∖ {0}` | set | naturals |
| `ℤ` | integers, `(ℕ × ℕ)/∼_ℤ` | set (ordered integral domain) | integers |
| `[(a,b)]_ℤ` | the integer "`a − b`" | element of ℤ | integers |
| `−x` | additive inverse in ℤ (or ℚ, ℝ) | element | integers |
| `ℤ*` | nonzero integers | set | integers |
| `a ∣ b` | `a` divides `b` | proposition | integers |
| `gcd(a,b)` | greatest common divisor | element of ℕ | integers |
| `q, r` | quotient and remainder in `a = bq + r`, `0 ≤ r < b` | element of ℤ | integers |
| `ℚ` | rationals, `(ℤ × ℤ*)/∼_ℚ` | set (ordered field) | rationals |
| `[(a,b)]_ℚ`, `a/b` | the rational "`a` over `b`" | element of ℚ | rationals |
| `\|x\|` | absolute value | element (≥ 0) | rationals/reals |
| `ℚ⁺` | positive rationals | set | rationals |
| `(x_n)` | a sequence, `x : ℕ → ℚ` (or `→ ℝ`) | function | rationals/reals |
| `A`, `B` | Dedekind cuts (lower subsets of ℚ) | subset of ℚ | reals |
| `ℝ` | reals, the set of Dedekind cuts | set (complete ordered field) | reals |
| `q*` | the rational cut `{p ∈ ℚ : p < q}` | element of ℝ | reals |
| `0*`, `1*` | the cuts of `0` and `1` | element of ℝ | reals |
| `sup S`, `inf S` | least upper / greatest lower bound of `S ⊆ ℝ` | element of ℝ | reals |
| `⋃ 𝒮` | union of a family of sets (here: of cuts) | set | reals |
| `\|X\|`, `\|X\| = \|Y\|` | cardinality; equinumerosity (a bijection exists) | — | cardinality |
| `\|X\| ≤ \|Y\|` | an injection `X → Y` exists | — | cardinality |
| `ℵ₀` | `\|ℕ\|` | cardinal | cardinality |
| `π(m,n)` | the Cantor pairing `(m+n)(m+n+1)/2 + n` | element of ℕ | cardinality |

## Structure names (the `structure` nodes)

`commutative_monoid` ⊂ `commutative_semiring` ⊂ `commutative_ring` ⊂
`integral_domain` ⊂ `field`; orthogonally `ordered_ring`, `ordered_field`. Each
is a signature + axioms; `⊂` here means "every model of the right is a model of
the left plus more axioms".

Identifier-atomicity note for the `ptx` symbol index: multi-character
identifiers (`gcd`, `sup`, `pi`, `x_n`, `q_star`) are indexed whole via
`ptx -W '[A-Za-z_][A-Za-z0-9_]*'`. Confirm every hit with `rg`.
