# Specialization / boundary cases and hypothesis-dropped counterexamples

Per headline node: a **specialization** that must come out right, and a
**counterexample** showing a hypothesis (or a logic/axiom assumption) cannot be
dropped. Numeric parts are in `validation/instance-checks.bc`; abstract cores in
`validation/proof-checks.lean`.

## `quantifier_negation`
**Specializations:** negating an ε–δ statement produces exactly "discontinuous
at `c`" (`∃ε ∀δ ∃x …`); negating "`X` countable" gives "no injection `X → ω`".
**Counterexample:** drop **classical logic** — intuitionistically
`¬(∀x, P x ∨ ¬P x)` is refutable but `∀x, P x ∨ ¬P x` is unprovable; the
`¬∀ → ∃¬` form is strictly classical.

## `axiom_of_choice`
**Specializations:** a **finite** family — choice is provable in ZF by induction.
A family of nonempty subsets of a **well-ordered** set — pick the least element,
no AC. A family of nonempty finite sets of **reals** — still needs AC (no
definable selector).
**Counterexamples (drop full AC):** consistent with ZF that ℝ is a countable
union of countable sets; that an infinite set has no countably infinite subset
(amorphous set); that a vector space has no basis; that ℝ cannot be
well-ordered.

## `preimage_algebra`
**Specializations:** `f⁻¹[∅] = ∅`, `f⁻¹[Y] = X`; "continuous ⟺ preimage of open
is open" is well-posed precisely because of these identities.
**Counterexample (use the image instead):** `f(x) = x²`, `A = {−1}`, `B = {1}`:
`f[A ∩ B] = f[∅] = ∅` but `f[A] ∩ f[B] = {1}`. The image does **not** commute
with intersection — only the preimage algebra is clean.

## `image_algebra`
**Specialization:** `f` injective ⟹ `f[⋂ A_i] = ⋂ f[A_i]` (equality restored).
**Counterexample:** the `x²` example above — `⊆` holds, `⊇` fails.

## `equivalence_partition_correspondence`
**Specializations:** equality ↔ the singleton partition; `X × X` ↔ `{X}`;
`≡ mod n` on ℤ ↔ the `n` residue classes.
**Counterexamples:**
- drop **transitivity**: "differ by `< 1`" on ℝ — reflexive, symmetric, classes
  overlap without being equal, not a partition.
- drop **reflexivity**: the empty relation — symmetric, transitive, but some
  `x` is in no class; the "classes" do not cover `X`.

## `well_defined_on_quotient`
**Specializations:** `+` on `ℤ = (ℕ×ℕ)/∼` descends because `∼` is a congruence;
`h = π` always descends.
**Counterexample:** on `ℤ/6ℤ`, `[n] ↦ n mod 4` — `[0] = [6]` but `0 ≠ 2`. The
rule depends on the representative.

## `zorn_lemma`
**Specializations:** every ideal extends to a maximal ideal; every vector space
has a basis; every filter extends to an ultrafilter.
**Counterexamples:**
- drop "**every chain** bounded": `[0,1)` under `≤` — the chain `{1 − 1/n}` has
  no upper bound *in `[0,1)`*, and `[0,1)` has no maximal element.
- drop **`P` nonempty**: the empty poset.
- drop **full AC**: Zorn ⟺ AC, so it can fail in ZF.

## `well_ordering_theorem`
**Specializations:** `ω` is already well-ordered by `∈`; gives cardinal
comparability; gives "every infinite set has a countably infinite subset".
**Counterexample:** drop **full AC** — consistent with ZF that ℝ has no
well-ordering.

## `omega_construction` / `peano_holds_in_omega` / `recursion_theorem`
**Specializations:** `n = {0,…,n−1}`, so `m < n ⟺ m ∈ n`; `ω` is the first
limit ordinal; `recursion` with `g(n,x)=x+1`, `a=0` gives the identity.
**Counterexamples:**
- drop **Axiom of Infinity**: `V_ω` (hereditarily finite sets) models ZF −
  Infinity + "every set is finite"; `ω` does not exist.
- drop **minimality of `ω`**: a larger inductive set (with an extra ℤ-chain)
  satisfies Peano 1–4 but not induction; `recursion` is unconstrained on the
  chain.
- drop **Foundation / ordinal structure**: a Quine atom `x = {x}` has
  `S(x) = x`, so `S` is not injective.

## `cantor_theorem` / `cantor_diagonal`
**Specializations:** `X = ∅` gives `0 < 1`; `X = ω` gives `cantor_diagonal`;
iterating gives an unbounded cardinal chain.
**Counterexamples:**
- there is **no** `X` that escapes `cantor_theorem` — it is unconditional
  (`instance-checks.bc` shows `D` explicitly for `X = {0,1,2,3}`).
- `cantor_diagonal` over **decimal** digits needs the `0.999…` dodge; over
  `{0,1}` with the flip rule there is no collision.
- the diagonal of a list of **naturals** escapes into `2^ω`, not out of `ω` —
  `ω` is countable.

## `cantor_schroeder_bernstein`
**Specializations:** `|ω| = |ω×ω|`; `|(0,1)| = |[0,1]|` in ℝ (inclusion one
way, `x ↦ (x+1)/3` the other).
**Counterexample:** drop **one injection** — `ω ↪ ℝ` alone gives only
`|ω| ≤ |ℝ|`, and they are not equinumerous.

## `countable_closure_properties`
**Specializations:** `ℤ = ⋃_n {−n,n}` (given pieces, choice-free);
`ℚ = ⋃_n {a/n : a∈ℤ}` (given enumerations, choice-free); the algebraic numbers.
**Counterexamples:**
- drop **countable choice**: consistent (Feferman–Levy) that ℝ is a countable
  union of countable sets.
- drop **countably many pieces**: `⋃_{x∈ℝ} {x}` is uncountable.
- misuse: "ℝ is a countable union of countable sets" is **false**
  (`cantor_diagonal`) — some piece of any countable cover of ℝ is uncountable.

## `continuum_hypothesis`
**Specializations:** GCH (`2^{ℵ_α} = ℵ_{α+1}` for all `α`) — also independent,
holds in `L`.
**Counterexample:** CH **cannot** be dropped-or-assumed in general — any proof
using it yields only a conditional theorem. "`|ℝ| = 2^ℵ₀`" is a ZFC theorem
(`cantor_diagonal` + CSB); "`|ℝ| = ℵ₁`" is CH — do not conflate.
