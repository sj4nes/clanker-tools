# Cycles found and how they were resolved — Release 0.1

The `tsort` skill's protocol: on a cycle, stop, translate every cycle edge to
plain language, classify each (true prerequisite / equivalent-definition /
alternative-proof-route / explanatory / historical / duplicate), and move the
non-prerequisites out to metadata — or, for a genuine foundational choice,
declare one concept primitive for the release.

## 1. independence ↔ conditional probability (structural, anticipated)

**The tension.** The textbook order often introduces `P(A|B)` first and then
*defines* "A independent of B" as `P(A|B) = P(A)`. But `P(A|B)` needs
`P(B) > 0`, while independence is wanted for null events too (and for
sigma-algebras, and as the hypothesis of the second Borel–Cantelli lemma, which
is upstream of most conditioning machinery).

**Resolution — declared modelling choice.** `independence_events` is defined by
the **factorization rule over every finite subfamily**
(`P(cap_{i in S} A_i) = prod_{i in S} P(A_i)`), requiring only
`probability_measure` and `finite_additivity`. `conditional_probability` is a
separate later node. `P(A|B) = P(A)` becomes a **theorem** (recorded as an
`equivalent_to` relation on `independence_events`, note: "where `P(B) > 0`"),
not the definition. No `tsort` edge runs from `conditional_probability` to
`independence_events`.

Edge kept: `independence_events conditional_probability`? — **no**. They are
independent in the graph; `borel_cantelli_second` depends on
`independence_events`, and `conditional_probability` depends on
`complement_rule`, and neither depends on the other.

## 2. expectation ↔ integral (foundational choice)

**The tension.** `E[X]` *is* `integral X dP`; but one can also build `E` first
for simple r.v.s and define the integral from it.

**Resolution — the integral is the cited primitive.** Per `conventions.md`,
`abstract_integral` (with MCT/DCT/Fatou/Fubini/Radon–Nikodym) is a cited
`bridge`. Every edge runs `abstract_integral -> expectation`,
`abstract_integral -> expectation_linearity`, etc. "Linearity / monotonicity /
MCT for expectation" are the integral's theorems specialised to `(Omega, F, P)`;
they are **not** re-derived, and no edge runs from `expectation` back into the
integration bridge.

## 3. conditional_probability ↔ multiplication_rule (modelling slip)

Both `conditional_probability multiplication_rule` and
`multiplication_rule conditional_probability` were encoded in the first draft.
`P(A cap B) = P(A|B) P(B)` is a **rearrangement of the definition** of
`P(A|B)` — the definitional direction is `conditional_probability ->
multiplication_rule`. The reverse edge was deleted (line removed from
`dependencies.plan`).

## 4. cdf ↔ distribution_pushforward (modelling slip)

First draft encoded both directions. The CDF is *computed from* the law
(`F_X(x) = P_X((-inf, x])`), so the edge is
`distribution_pushforward -> cdf`. That the CDF **determines** the law is the
separate theorem `cdf_determines_law` (via `dynkin_pi_lambda`), an
`equivalent_to`-flavoured result with its own node — not a reverse prerequisite
edge. The reverse edge was deleted.

## Non-cycles worth noting (checked, no edge needed)

- **variance ↔ moment**: `variance` is defined directly as `E[(X - EX)^2]`, not
  as "the 2nd central moment via the `moment` node". `moment` requires
  `variance`-free machinery (`expectation`, `lotus`); `variance` does not
  require `moment`. Both depend on `expectation`.
- **mgf ↔ characteristic_function**: neither requires the other; both require
  `expectation` and `lotus`. `cf_properties` and `mgf_sum_independent` reference
  both, downstream.
- **WLLN ↔ SLLN**: SLLN does **not** depend on WLLN (Etemadi's proof is
  self-contained). They share `iid`, `borel_cantelli_first` (SLLN only),
  `chebyshev_inequality` (WLLN only). `strengthens` relation recorded in
  `relations.tsv`.
- **CLT ↔ Lévy continuity**: `central_limit_theorem` *uses* the cited
  `levy_continuity_theorem`; the reverse is false. Edge is
  `levy_continuity_theorem -> central_limit_theorem`.
