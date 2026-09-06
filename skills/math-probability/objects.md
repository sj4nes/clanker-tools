# The type vocabulary — Release 0.1

Which sets / spaces / structures the objects of this capsule inhabit, and the
well-formedness rules used in every result's `type_check_status`.

## The spaces

| Object | Inhabits | Notes |
|---|---|---|
| outcome `omega` | the sample space `Omega` (an arbitrary nonempty set) | no structure assumed |
| event `A` | `F`, a **sigma-algebra** on `Omega` | *not* `2^Omega` in general — non-measurable sets exist for `Omega = [0,1]` |
| probability `P(A)` | the real interval `[0,1]` | `P: F -> [0,1]`; `P(Omega)=1`, countably additive |
| measure value `mu(A)` | `[0, inf]` (extended reals) | `mu(empty)=0`; `sigma`-finite for Radon–Nikodym |
| random variable `X` | the function space of **measurable** maps `(Omega,F) -> (R, B(R))` | or `(R^d, B(R^d))` for a random vector |
| law `P_X` | the set of probability measures on `(R, B(R))` | `P_X = P o X^{-1}` |
| CDF `F_X` | the set of nondecreasing right-continuous `R -> [0,1]` with limits `0, 1` | bijection with laws (`cdf_properties`) |
| pmf `p_X` | `{ g: S -> [0,1] : sum_S g = 1 }`, `S` countable | discrete case |
| pdf `f_X` | `{ g: R -> [0,inf) measurable : integral g = 1 }` mod Lebesgue-null | `dP_X/d(Leb)` |
| `E[X]`, moments | `R` (or `[0,inf]` for `X >= 0`); **may not exist** | `X in L^1` is the precondition |
| `M_X(t)` | `(0, inf]` — a value in the extended positive reals | finite only on an interval around 0 (maybe just `{0}`) |
| `phi_X(t)` | the closed complex unit disk `{ z : |z| <= 1 }` | always defined for all `t in R` |
| `E[X | G]` | `L^1(Omega, G, P)` — a **random variable**, defined up to a.s. equality | not a number (contrast `E[X | Y=y]`) |
| a convergence mode | one of `{a.s., p, L^p, d}` | the per-result tag; see `conventions.md` |

## Well-formedness rules

1. **Every probability is of an event.** `P(...)` is only well-formed when its
   argument is shown to be in `F` (for r.v. statements: a preimage
   `X^{-1}(B)`, `B in B(R)` — legitimate because `X` is measurable).
2. **`E[X]` is not automatic.** A statement using `E[X]`, `Var(X)`, `Cov(X,Y)`,
   `rho`, `M_X` must carry the integrability / moment precondition that makes it
   exist. "`X ~ Cauchy`" fails rule 2 for `E[X]`.
3. **`P(A | B)` presupposes `P(B) > 0`.** Every conditional statement carries
   this as a precondition; the abstract `E[X | G]` is the tool when conditioning
   on probability-zero events.
4. **Countable vs finite.** A step invoking countable additivity, continuity of
   `P`, or Borel–Cantelli must genuinely use a *countable* family; a finite
   family only licenses `finite_additivity`.
5. **The limit in `-->^{d}` is a law, not a variable.** `X_n -->^{d} N(0,1)`
   type-checks as convergence of `F_{X_n}` to `Phi` at continuity points; it
   says nothing about the `X_n` converging pointwise.
6. **Independence is a property of a whole family.** "`X_1,...,X_n` independent"
   is the factorization over *every* subset; checking pairs (rule-of-thumb
   error, `pairwise_not_mutual`) is not enough.
7. **Densities are mod null sets.** An `f_X` equality means "Lebesgue-a.e."; a
   pointwise claim about a density is not well-formed without a continuity
   hypothesis.
8. **A well-typed statement can still be false.** The type check is necessary,
   not sufficient — a missing hypothesis, a strictness, or a quantifier-order
   slip (`for all eps exists N` vs `exists N for all eps` in the convergence
   modes) still makes a well-typed statement wrong.
