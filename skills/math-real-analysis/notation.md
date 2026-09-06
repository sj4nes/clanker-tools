# Master symbol list — Release 0.1

`type` is the mathematical type of the object the symbol usually denotes in this
capsule. `area` groups it. Where a symbol is overloaded, the dominant use is
listed first.

| Symbol | Meaning | Type | Area |
|---|---|---|---|
| `ℕ` | natural numbers {1,2,…} (excludes 0; `ℕ₀` includes it) | set | foundations |
| `ℚ` | rational numbers, as an ordered field | ordered field | foundations |
| `ℝ` | real numbers, the complete ordered field | ordered field | reals |
| `n, m, k, j, N` | natural-number indices; `N` a threshold | element of ℕ | sequences |
| `x, y, z, t` | real numbers / real variable | element of ℝ | reals |
| `a, b` | endpoints of an interval, `a ≤ b` | element of ℝ | reals |
| `c` | a fixed point (of evaluation, of a limit, from the MVT) | element of ℝ | analysis |
| `ε` (eps) | an arbitrary positive tolerance | positive real | analysis |
| `δ` (delta) | a positive number chosen in response to `ε` | positive real | analysis |
| `M` | a bound (`|x_n| ≤ M`), or an upper bound for `Σ|a_n|` | positive real | sequences/series |
| `(x_n)`, `(a_n)`, `(s_n)` | a sequence; `(s_n)` often a partial-sum sequence | function ℕ → ℝ | sequences |
| `L` | the limit of a sequence or function | element of ℝ | analysis |
| `(x_{n_j})` | a subsequence, `n_j` strictly increasing in ℕ | function ℕ → ℝ | sequences |
| `Σ a_n`, `Σ_{n=1}^∞ a_n` | an infinite series | formal object / its sum in ℝ | series |
| `s_n = Σ_{k=1}^n a_k` | the nth partial sum | element of ℝ | series |
| `r` | ratio of a geometric series; radius of convergence | element of ℝ, `r ≥ 0` | series |
| `limsup`, `liminf` | upper / lower limit of a bounded sequence | element of ℝ (or ±∞) | sequences |
| `sup A`, `inf A` | least upper bound / greatest lower bound of `A ⊆ ℝ` | element of ℝ | reals |
| `f, g, h` | real functions `D → ℝ`, `D ⊆ ℝ` | function | analysis |
| `D` | the domain of a function, `D ⊆ ℝ` | subset of ℝ | analysis |
| `f'`, `f''`, `f^{(k)}` | first / second / kth derivative of `f` | function | differentiation |
| `f ∘ g` | composition | function | analysis |
| `U`, `V` | open subsets of ℝ | subset of ℝ | topology |
| `K` | a compact subset of ℝ | subset of ℝ | topology |
| `𝒰 = {U_α}` | an open cover | family of open sets | topology |
| `A'` | the set of limit points of `A` | subset of ℝ | topology |
| `Ā` | the closure of `A` | subset of ℝ | topology |
| `P = {a = t_0 < … < t_n = b}` | a partition of `[a,b]` | finite subset of `[a,b]` | integration |
| `L(f,P)`, `U(f,P)` | lower / upper Darboux sum | element of ℝ | integration |
| `∫_a^b f`, `∫_a^b f(x) dx` | the Riemann integral of `f` over `[a,b]` | element of ℝ | integration |
| `F` | an antiderivative of `f` (`F' = f`) | function | integration |
| `f_n → f` | pointwise convergence of a function sequence | — | function sequences |
| `f_n ⇉ f` | uniform convergence | — | function sequences |
| `‖f‖_∞`, `‖f‖_{sup}` | `sup_{x∈D} |f(x)|` | nonnegative real (or +∞) | function sequences |
| `Σ M_n` | the majorant series in the Weierstrass M-test | series of nonnegative reals | function sequences |
| `R` | radius of convergence of a power series | element of `[0,∞]` | function sequences |

Identifier-atomicity note for the `ptx` symbol index: multi-character
identifiers (`limsup`, `sup`, `eps`, `x_n`, `f_n`, `t_0`) are indexed whole via
`ptx -W '[A-Za-z0-9_]+'`. Confirm every hit with `rg`.
