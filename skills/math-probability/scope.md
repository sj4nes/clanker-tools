# Scope — Release 0.1

**Probability theory from the Kolmogorov axioms to the classical limit theorems
and conditional expectation — the missing foundational floor under
`design-of-experiments`, `simulation`, and `unknown-discovery`.**

Built with the [`math-theorem-tree`](../math-theorem-tree/SKILL.md) method. Sits
on top of two capsules and discharges their downstream primitives:

- [`math-sets-functions-cardinality`](../math-sets-functions-cardinality/SKILL.md)
  supplies `set_algebra`, the **preimage algebra**, `countable_set`, indexed
  unions/intersections, and De Morgan — everything a σ-algebra is built from.
- [`math-real-analysis`](../math-real-analysis/SKILL.md) supplies the complete
  ordered field ℝ, sequence and series convergence, `limsup`/`liminf`, and the
  integral. The **abstract Lebesgue integral against a measure** is *cited, not
  constructed* (see foundational stance).

## Included

- **Measure-theoretic foundation (the σ-algebra/measure entry).** σ-algebra,
  generated σ-algebra, the Borel σ-algebra on ℝ; measurable space; measure
  (countable additivity, `μ(∅)=0`); continuity of measure from below/above;
  the **π–λ (Dynkin) theorem** as the uniqueness engine; Carathéodory extension
  and the existence of Lebesgue measure **cited**; null sets and the
  "almost surely" convention.
- **Kolmogorov's axioms** as first-class `axiom` nodes: nonnegativity,
  normalization `P(Ω)=1`, countable additivity. The probability space
  `(Ω, 𝓕, P)`.
- **Elementary consequences**: complement, finite additivity, monotonicity,
  inclusion–exclusion, Boole's inequality (union bound), continuity of
  probability, the **first and second Borel–Cantelli lemmas**.
- **Random variables**: measurable function; random variable and random vector;
  the distribution (pushforward) `P∘X⁻¹`; the CDF and its four characterizing
  properties; discrete r.v. and pmf; absolutely continuous r.v. and pdf
  (**Radon–Nikodym cited**); the quantile function; the **probability integral
  transform** (`F(X) ~ Uniform`, and its inverse — the simulation bridge); the
  univariate and Jacobian change-of-variables formulas; joint, marginal, and
  conditional distributions.
- **Expectation and moments**: expectation as `∫ X dP`; the **law of the
  unconscious statistician**; linearity and monotonicity; MCT / DCT / Fatou /
  Fubini–Tonelli **cited** as the exchange-of-limit toolkit; variance, the
  computational formula `Var(X)=E[X²]−E[X]²`, affine scaling; covariance,
  correlation, variance of a sum; `L^p` spaces and the moment
  ladder `L^p ⊆ L^q` (`p>q`, finite measure); moment generating and
  characteristic functions, the moment and uniqueness theorems, `|φ|≤1`.
- **Independence and conditional probability**: `P(A|B)`; the multiplication
  rule; the law of total probability; **Bayes' theorem** as a node;
  independence of events, of σ-algebras, and of random variables; the
  factorization theorem; `E[XY]=E[X]E[Y]` for independent `X,Y` (independent ⇒
  uncorrelated); `iid`; the convolution formula and the "MGFs/CFs multiply"
  identity. Two counterexamples: **pairwise ≠ mutual** independence, and
  **uncorrelated ≠ independent**.
- **Distribution families** (each with pmf/pdf, support, mean, variance, MGF/CF,
  and its characterizing property): Bernoulli, binomial, geometric, Poisson
  (with the **Poisson limit theorem**), discrete uniform; continuous uniform,
  exponential (**memorylessness**), gamma, beta, and the **normal** family
  (standard normal, affine closure, the CLT limit). **Cauchy** is included as a
  `counterexample` node — the distribution with no mean.
- **Inequalities**: Markov, Chebyshev (from Markov), the Chernoff bound, Jensen,
  Cauchy–Schwarz for `E[XY]` (hence `|ρ|≤1`), Hölder, the Hoeffding lemma, and
  **Hoeffding's inequality**.
- **Modes of convergence and the limit theorems.** Four convergence modes as
  `definition` nodes — **almost sure, in probability, in `L^p`, in
  distribution** — each result below is *tagged with the mode it delivers* (the
  `choice_grade` analogue of the sibling capsules). The implication lattice
  (`a.s. ⇒ p`, `L^p ⇒ p`, `p ⇒ d`, and the partial converses); the portmanteau
  theorem; the continuous mapping theorem; Slutsky; the **weak** (in
  probability) and **strong** (almost sure) laws of large numbers; **Lévy's
  continuity theorem**; the classical **i.i.d. central limit theorem** (in
  distribution) and the Lindeberg CLT; the delta method.
- **Conditional expectation**: the elementary `E[X|Y=y]`; the abstract `E[X|𝓖]`
  (existence **cited** — Radon–Nikodym / `L²` projection); the tower property
  (law of total expectation); conditional Jensen; the law of total variance;
  and `E[X|𝓖]` as the `L²`-best predictor.
- **Boundary nodes, stated not proved**: martingale, stochastic process, and
  the Kolmogorov extension theorem — the doorway to Release 0.2 / a future
  stochastic-processes capsule.

## Excluded (out of scope for 0.1)

- **The construction of the abstract integral.** Simple functions → MCT →
  general `∫ f dμ`, and the proofs of MCT/DCT/Fatou/Fubini/Radon–Nikodym, are
  **cited to a measure-theory reference**, not built. This capsule *uses* the
  integral and its convergence theorems; it does not develop them. (A future
  `math-measure-and-integration` capsule is the natural floor below this one.)
- **Measure-theoretic probability beyond the σ-algebra/measure entry**: regular
  conditional distributions, disintegration, weak convergence on general Polish
  spaces, tightness/Prokhorov, the full theory of `L^p` as Banach spaces.
- **Stochastic processes**: martingales (beyond the boundary node), Markov
  chains, Poisson processes, Brownian motion, stochastic calculus, ergodic
  theory.
- **Statistical inference**: estimation, hypothesis testing, confidence sets,
  the bootstrap, Bayesian posterior computation, regression. That is a separate
  skill sitting *on top of* this capsule.
- **Information theory** (entropy, KL divergence, mutual information) beyond
  what a single `illustrated_by` note mentions.
- **Combinatorial probability** as a subject (generating functions, the
  probabilistic method) — counting is assumed, not developed.

## Size

**131 nodes** (0.1). The initial sketch aimed at ~90–110, but probability at
this level carries an irreducibly high concept load — four convergence modes,
~11 distribution families each with its characterizing property and moments,
eight inequalities, the measure-theoretic entry — and collapsing those would
lose exactly the dependency distinctions the capsule exists to record. The
target for the domain is therefore ~130; a release is judged by selection and
dependency clarity, not by hitting a node budget.

## Level and audience

A first rigorous, measure-based probability course: Billingsley *Probability and
Measure*; Durrett *Probability: Theory and Examples*; Williams *Probability with
Martingales*; Grimmett–Stirzaker *Probability and Random Processes*; Çınlar
*Probability and Stochastics*. Roughly first-year-graduate, or a strong
senior-undergraduate course that takes the integral as given.

## Foundational stance

- **ZFC + classical logic**, inherited through the two capsules below. Excluded
  middle is used freely (every "not a.s. convergent", every counterexample is a
  `¬∀`).
- **The measure and its integral are the floor.** `measure` and `∫ · dμ` (with
  MCT, DCT, Fatou, Fubini–Tonelli, Radon–Nikodym) are taken as **cited
  primitives** — `bridge` nodes with `lean_status: cited` and a named source
  section. Everything probabilistic is built above that line.
- **`countable additivity`, not finite.** Kolmogorov's third axiom is countable
  additivity; finite additivity is a *derived* proposition. Continuity of
  probability and both Borel–Cantelli lemmas depend on the countable form —
  edged so.
- **The Axiom of Choice** enters only through cited measure-theory results
  (existence of non-measurable sets is *mentioned*; Lebesgue measure's
  existence via Carathéodory is cited). No probabilistic theorem in this
  release needs AC in its own proof; the SLLN proof route used
  (Etemadi / fourth-moment) is choice-free.

## Proof policy

Proofs are **sketched**, with the key algebraic identity or inequality
**Lean-checked** where feasible (Markov, Chebyshev-from-Markov, Jensen for a
convex combination, linearity of expectation, `Var(X)=E[X²]−E[X]²`, Bayes as an
identity, binomial mean/variance, the union bound). Deep analytic theorems
(CLT, SLLN, Lévy continuity, Radon–Nikodym, MCT/DCT) are **cited** with an
explicit `lean_status: cited` — never labelled `proved_*` beyond what the kernel
or a cited checked proof establishes. `bc` worksheets carry the distribution
moment formulas and a numerical CLT convergence demonstration.

## Epistemic-status policy

Every result node carries one status label from the `math-theorem-tree` list.
`definition` / `axiom` nodes carry `well_definedness` instead of a proof.
`cited` analytic theorems are labelled `proved_theorem` **with
`lean_status: cited`** and a source — the proof exists and is checked in the
literature, just not re-formalized here. Boundary nodes are `stated_not_proved`.
