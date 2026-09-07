# Tutorial map — teaching the curated knowledge to people

A survey of the **human-facing tutorials** that could be cut from the knowledge
capsules in this repo: what each one would teach, which capsule nodes it covers,
what infrastructure builds it, and where to start.

Companion to [`BACKLOG-BACKLOG.md`](../BACKLOG-BACKLOG.md) (the speculative
skill roadmap) and [`BACKLOG.md`](../BACKLOG.md) (near-term work). This file is a
**map, not a queue** — low commitment, revised as capsules and infrastructure
grow.

Related skills: [`formula-tree-tutorial`](../skills/formula-tree-tutorial/SKILL.md)
(builds physics tutorials today); the planned `theorem-tree-tutorial` and
`explain-a-capsule` (see the roadmap).

---

## 1. What "curated knowledge" is, right now

Eight [`*-theorem-tree`](../skills/math-theorem-tree/SKILL.md) /
[`*-formula-tree`](../skills/physics-formula-tree/SKILL.md) capsules — **815
dependency-ordered nodes** with typed statements, hypotheses, specializations,
hypothesis-dropped counterexamples, `bc` worksheets, and Lean cores.

### The mathematics stack (576 nodes) — each capsule discharges the one above

| Capsule | Nodes | What it establishes | Discharges into |
|---|---:|---|---|
| [`math-logic-and-proof`](../skills/math-logic-and-proof/SKILL.md) | 130 | propositional & first-order logic, natural deduction + Hilbert, soundness/completeness/compactness, the proof-method block, the metatheory boundary | the logic primitives of `math-sets-…` |
| [`math-sets-functions-cardinality`](../skills/math-sets-functions-cardinality/SKILL.md) | 106 | ZF(C), set & preimage algebra, quotients, order theory + Zorn, `ω` from Infinity, cardinality through Cantor; per-result **choice grade** | `set` / `function` / `AC` / **the Peano axioms** of `math-number-systems` |
| [`math-number-systems`](../skills/math-number-systems/SKILL.md) | 100 | ℕ→ℤ→ℚ→ℝ as constructions; ℚ incomplete; ℝ via Dedekind cuts with the **lub property proved** | `lub_axiom` / `real_number` of `math-real-analysis` |
| [`math-real-analysis`](../skills/math-real-analysis/SKILL.md) | 109 | completeness and its consequences, sequences/series, topology of ℝ, continuity, differentiation, Riemann integration, uniform convergence | limits / integration of `math-probability` |
| [`math-probability`](../skills/math-probability/SKILL.md) | 131 | Kolmogorov axioms, random variables, expectation, independence, the inequalities, the four convergence modes + limit theorems, conditional expectation; per-result **convergence-mode tag** | (floor under `design-of-experiments`, `simulation`, `unknown-discovery`) |

### The physics capsules (239 nodes)

| Capsule | Nodes | What it establishes |
|---|---:|---|
| [`physics-newtonian`](../skills/physics-newtonian/SKILL.md) | 58 | kinematics, Newton's three laws, work/energy + conservation, momentum/impulse, SHM, gravitation |
| [`physics-thermodynamics`](../skills/physics-thermodynamics/SKILL.md) | 77 | the four laws, ideal gas, heat capacities, reversible adiabats, Carnot + the temperature scale, entropy, the potentials + Maxwell relations |
| [`physics-thermoacoustics`](../skills/physics-thermoacoustics/SKILL.md) | 104 | linear acoustics, penetration depths, Rott's wave equation with the `f`-functions, the short-stack results, standing- vs traveling-wave devices, the Carnot limit |

---

## 2. How a tutorial is cut from a capsule

The capsule did the hard part — a correct prerequisite order and validated
content. A tutorial **linearizes a slice of that graph into a lesson** where
every concept the reader meets comes with a calculation they run.

- **The spine is a `tsort` slice.** Three grain sizes:
  1. **single-target** — the minimal prerequisite closure of one headline node
     (`indexes/prerequisite-paths.md` gives these directly);
  2. **thematic band** — one horizontal layer (e.g. "the inequalities");
  3. **whole-capsule tour** — the full `tsort` order, one check per concept.
- **Every concept gets a runnable check**, reused from the capsule's own
  `validation/`: a `bc` numeric beat, a limiting/specialization case, a Lean
  instance check. No new mathematics in the tutorial.
- **Prose is compressed from the node entry** — what it says, what the symbols
  mean, when it is valid, what must be known first, what breaks it.
- **Delivery is `upmd`** (`upmd.dev`): named fenced blocks with `deps:` mirroring
  the capsule edges; `upmd --ci --all` must exit 0, and every check runs
  standalone with `-b`.

---

## 3. Infrastructure status

| Builder | Covers | Status |
|---|---|---|
| [`formula-tree-tutorial`](../skills/formula-tree-tutorial/SKILL.md) | physics capsules → `upmd` `.md` | **exists**, verified via `pendulum.md` |
| `theorem-tree-tutorial` (planned) | math capsules → `upmd` `.md` — the `bc`+`Lean-via-bash` variant `hole-in-the-rationals.md` was hand-built with | roadmap (`BACKLOG-BACKLOG.md` → Meta/builders) |
| `explain-a-capsule` (planned) | any capsule → a linear reader's path, one check per concept (the Tier-3 rows) | roadmap (`BACKLOG-BACKLOG.md` → Human-facing lane) |
| cross-capsule convention (none yet) | tutorials that span two capsule dirs — `deps:` across directories, citing two `validation/` sets | needs a first example |

**Math-tutorial mechanics already worked out** (from `hole-in-the-rationals.md`):
`upmd` has no native Lean runner, so proof beats are `bash` blocks that invoke
`lean` on a heredoc and check exit 0 (print `SKIP` + exit 0 if `lean` is
missing); `bc` numeric beats carry the `bc`-identifier rules; `upmd` runs
*every* fenced block, so prose formulas stay inline, not in fenced examples.

---

## 4. The map

### Tier 0 — shipped

| Tutorial | Capsule | Target | Blocks |
|---|---|---|---|
| [`hole-in-the-rationals.md`](../skills/math-real-analysis/tutorial/hole-in-the-rationals.md) | `math-real-analysis` | `lub_axiom` → `cauchy_convergence_criterion` (the completeness thread), each step shown failing in ℚ | 13 (`bc` + Lean-via-bash) |
| [`pendulum.md`](../skills/physics-newtonian/tutorial/pendulum.md) | `physics-newtonian` | `newton_second_law` → `simple_pendulum` | 9 (`bc`) |

### Tier 1 — single-target tutorials (one headline, its minimal prerequisite path)

Numbers in parentheses are the prerequisite-closure size from each capsule's
`indexes/prerequisite-paths.md` — a rough length proxy. **★** marks a strong
first candidate (accessible hook, small closure, checks ready).

#### `math-logic-and-proof`

| Working title | Target node(s) | Hook |
|---|---|---|
| **What counts as a proof** ★ | the 15-node `proof_methods` block → `induction_equivalence` | direct / contrapositive / contradiction / cases / weak-strong-structural induction / well-ordering — with the constructive grade on each |
| Truth tables to functional completeness | `functional_completeness` | every Boolean function is `{¬,∧,∨}` — and `{NAND}` alone suffices |
| Two calculi, one theorem | `nd_hilbert_equivalence` | natural deduction vs a Hilbert system + the deduction theorem, proved equivalent |
| Why the rules don't lie | `soundness_prop`, `soundness_fol` | every derivable sequent is valid — the easy half of the metatheory |
| Compactness and its payoff | `compactness_prop`, `compactness_fol` | finite satisfiability ⇒ satisfiability; non-standard models fall out |
| Gödel's completeness theorem | `godel_completeness_theorem` | the Henkin term-model construction (deep — a long lesson) |
| The limits | `godel_incompleteness_first/second`, `undecidability_fol_validity` | a *reading* not a *run* — these nodes are stated-not-proved |

#### `math-sets-functions-cardinality`

| Working title | Target | Hook |
|---|---|---|
| **The preimage algebra** ★ | `preimage_algebra` (28) | `f⁻¹` commutes with `⋃`, `⋂`, complement — machine-checked as `rfl`; the engine every continuity/compactness proof runs on |
| Quotients and well-definedness | `equivalence_partition_correspondence` → `well_defined_on_quotient` → `universal_property_quotient` (30) | "is this map on classes actually a function?" — the check that recurs in ℤ, ℚ, and everywhere |
| One axiom, three faces ★ | `zorn_lemma`, `well_ordering_theorem`, `cardinal_comparability` (37) | AC ⟺ Zorn ⟺ well-ordering ⟺ comparability — with the choice grade |
| Building ℕ from ∅ | `omega_construction` → `peano_holds_in_omega` (16) | the Axiom of Infinity gives a set that satisfies the Peano axioms |
| More reals than rationals ★ | `cantor_theorem` → `cantor_diagonal` (37) | `|X| < |𝒫(X)|`, unconditionally, no choice |
| The arithmetic of infinity | `infinite_cardinal_arithmetic` → `continuum_hypothesis` (60) | `ℵ₀+ℵ₀ = ℵ₀·ℵ₀ = ℵ₀`; `2^ℵ₀`; CH is independent (stated) |

#### `math-number-systems`

| Working title | Target | Hook |
|---|---|---|
| **√2 is irrational — and that's a crisis** ★ | `sqrt2_irrational` → `rational_incomplete_lub` (59) | a bounded set of rationals with no rational least upper bound |
| ℤ and ℚ as quotients | `integer` → `rational_number` → `rational_is_ordered_field` (47) | pairs mod an equivalence, with every well-definedness obligation discharged |
| Dedekind cuts fill the holes ★ | `dedekind_cut` → `real_number` → `real_is_ordered_field` → `lub_property` (52) | ℝ as downward-closed sets of rationals; the lub property proved as a **theorem** |
| ℝ is essentially unique | `real_uniqueness` (65) | any two complete ordered fields are isomorphic |
| ℚ is countable, ℝ is not | `rational_countable`, `cantor_diagonal_argument` → `real_uncountable` (68) | the pairing bijection, then the diagonal argument |

#### `math-real-analysis` (completeness thread shipped as Tier 0)

| Working title | Target | Hook |
|---|---|---|
| Compactness on the line | `heine_borel` (14) → `extreme_value_theorem` (22) | closed + bounded ⟺ every open cover has a finite subcover; continuous functions attain their bounds |
| The Mean Value Theorem and what it buys ★ | `mean_value_theorem` (29) → `taylor_theorem` (32) | Rolle → MVT → monotonicity from `f'` → Taylor with the Lagrange remainder |
| The Fundamental Theorem of Calculus, proved ★ | `riemann_integral` (14) → `ftc_part1` (44) → `ftc_part2` (49) | Darboux sums → integrability of continuous functions → both halves of the FTC |
| Swapping limit and integral | `uniform_limit_continuous` (16) → `weierstrass_m_test` (32) | why pointwise convergence is not enough, and the M-test that rescues series |
| Intermediate values | `intermediate_value_theorem` (13) | a short, self-contained lesson straight off completeness |

#### `math-probability`

| Working title | Target | Hook |
|---|---|---|
| **Three axioms, ten lines of consequences** ★ | `kolmogorov_axioms` (7) → `boole_inequality` (10) | complement, monotonicity, inclusion–exclusion, the union bound — everything before random variables |
| Bayes' theorem, properly ★ | `conditional_probability` (11) → `law_of_total_probability` → `bayes_theorem` (14) | the partition must be exhaustive; `P(A\|B)` vs `P(B\|A)`; the odds form |
| How to sample any distribution ★ | `probability_integral_transform` (32) | `F(X) ~ Uniform`, and `F⁻¹(U) ~ F` — the inversion-sampling bridge to `simulation` |
| Expectation is linear (independence not required) | `expectation` (16) → `lotus` (24) → `expectation_linearity` (17) | LOTUS, then linearity — the single most useful fact; mean of a count with no combinatorics |
| The concentration ladder ★ | `markov_inequality` (21) → `chebyshev_inequality` (25) → `chernoff_bound` → `hoeffding_inequality` (47), plus `jensen_inequality` (22) | polynomial tails → exponential tails; each step is the previous one applied to a cleverer function |
| The four modes of convergence ★ | `convergence_implications` (48) | a.s. / in probability / in `L^p` / in distribution — the lattice, and the counterexample that separates each pair |
| The Law of Large Numbers, weak and strong | `weak_law_large_numbers` (46) vs `strong_law_large_numbers` (44) | same finite-mean hypothesis, different convergence mode; Cauchy breaks both |
| The Central Limit Theorem | `characteristic_function` → `levy_continuity_theorem` (35) → `central_limit_theorem` (52) | the CF of the standardized sum → `e^{-t²/2}`; deep, a capstone lesson |
| Conditioning as projection | `conditional_expectation_abstract` → `tower_property` (33) → `law_of_total_variance` (36) → `conditional_expectation_l2_projection` (32) | `E[X\|𝓖]` as the `L²`-best predictor; total variance = within + between |
| Which distribution, and why | `binomial_distribution` (43), `normal_distribution` (24), + `poisson_limit_theorem`, `cauchy_no_mean` | each family's characterizing property; Cauchy as the no-mean warning label |

#### `physics-newtonian` (pendulum shipped)

| Working title | Target |
|---|---|
| Energy conservation from F = ma ★ | `work_energy_theorem` → `conservation_of_mechanical_energy` |
| Momentum and collisions | `conservation_of_momentum` |
| Kepler from Newton | `newton_gravitation` |

#### `physics-thermodynamics`

| Working title | Target |
|---|---|
| The ideal gas law from three experiments ★ | `ideal_gas_law` (13) |
| The first law: energy has a bank account | `first_law_thermodynamics` (25) |
| **Why heat engines have a ceiling** ★ (already wanted — `BACKLOG.md`) | `carnot_efficiency` (42) |
| Entropy and the arrow of time | `entropy` (43) → `entropy_ideal_gas` (55) |
| Four equations from one idea | `maxwell_relations` (49), `gibbs_free_energy` (47) |

#### `physics-thermoacoustics`

| Working title | Target |
|---|---|
| Sound as a heat engine ★ | `adiabatic_sound_speed` → penetration depths → `critical_temperature_gradient` |
| Rott's wave equation | `rott_momentum_equation` → `rott_wave_equation` *(draft)* |
| Standing wave vs Stirling | `travelling_wave_engine` → `relative_carnot_performance` |

### Tier 2 — thematic band tutorials (one horizontal layer, several headlines)

| Working title | Capsule | Band |
|---|---|---|
| The equivalence catalogue | `math-logic-and-proof` | the ~15 propositional equivalences + normal forms + duality, each with its constructive grade |
| The ZF axioms, one at a time | `math-sets-…` | each axiom as a node, what it lets you build, what breaks without it |
| The construction chain ℕ→ℤ→ℚ | `math-number-systems` | all three quotient constructions side by side, the same well-definedness ritual each time |
| The topology of ℝ | `math-real-analysis` | open / closed / limit point / closure / compact / connected — the `preimage_algebra` payoff |
| The distribution families | `math-probability` | Bernoulli / binomial / geometric / Poisson / uniform / exponential / gamma / beta / normal — pmf/pdf, moments, MGF, the characterizing property, and how they limit into each other |
| The reversible-process toolkit | `physics-thermodynamics` | isothermal / adiabatic / isobaric / isochoric — `W`, `Q`, `ΔU`, `ΔS` for each on the ideal gas |

### Tier 3 — whole-capsule tours (the `explain-a-capsule` pattern)

One linear pass through the full `tsort` order, one runnable check per concept.
Cheap to generate once `explain-a-capsule` exists; long to read. One per capsule
(8 total). Best framed as **reference walk-throughs**, not lessons.

### Tier 4 — cross-capsule tutorials (the stack's distinctive payoff)

These walk a **discharge edge** — the thing no single capsule shows.

| Working title | Spans | Thread |
|---|---|---|
| **From the empty set to the real line** ★ | sets → numbers → analysis | `omega_construction` → `peano_holds_in_omega` → ℕ→ℤ→ℚ → `dedekind_cut` → `lub_property` → (becomes `lub_axiom` upstairs) — the full foundational descent, ~6 checks |
| √2 doesn't exist, until it does | numbers → analysis | `sqrt2_irrational` → `rational_incomplete_lub` → `dedekind_cut` → `nth_root_exists` → the Babylonian sequence converging in ℝ (ties into `hole-in-the-rationals`) |
| Cantor's diagonal, three times | sets → numbers → probability | the same argument as `cantor_theorem`, then `real_uncountable`, then *why* `𝒫(ℝ)` forces `math-probability` to use a σ-algebra instead of `2^Ω` |
| From measure to the Central Limit Theorem | sets → probability | `sigma_algebra` (discharged from sets) → `measure` → `kolmogorov_axioms` → … → `central_limit_theorem` — the probability capsule's entire vertical, ~10 checks |
| What classical logic buys you | logic → everywhere | `quantifier_negation` (`¬∀ ⟺ ∃¬`) as the engine of every "counterexample" / "not compact" / "discontinuous" downstream; the three per-result grades (`constructive` / `choice` / `convergence-mode`) as one story about *which assumption a result rests on* |
| Bayes, end to end | probability → (future) | `conditional_probability` → `bayes_theorem` → conjugate updating → `unknown-discovery`'s forecast ledger + Brier calibration (partially a bridge — see Tier 5) |

### Tier 5 — bridge tutorials (need a future bridge capsule first)

From [`BACKLOG-BACKLOG.md`](../BACKLOG-BACKLOG.md) → Cross-domain bridges. A
bridge capsule imports its roots from two existing capsules; its tutorial then
teaches the correspondence.

| Working title | Bridge capsule | Needs |
|---|---|---|
| Priors, likelihoods, posteriors | `bayes-bridge` | `math-probability` ✓ + `statistics` |
| Entropy: Clausius ↔ Boltzmann ↔ Shannon | `entropy-bridge` | `math-probability` ✓ + information-theory + statistical-mechanics capsules |
| Least action: F=ma ↔ Lagrange ↔ Hamilton ↔ Fermat | `least-action-bridge` | `physics-newtonian` ✓ + a Lagrangian-mechanics capsule |
| Noether: symmetry ↔ conservation | `symmetry-conservation-bridge` | `physics-newtonian` ✓ + a Lagrangian-mechanics capsule |

---

## 5. Coverage

Cutting single-target tutorials (Tier 1) to every headline result would touch,
per capsule, roughly the union of those prerequisite closures — which for the
deepest headline in each capsule (`continuum_hypothesis` 60, `real_uncountable`
68, `ftc_part2` 49, `central_limit_theorem` 52) is already most of the graph. A
well-chosen **4–6 targets per capsule covers ~70–85% of its nodes.**

**Nodes that stay cold** under any reasonable tutorial set, and why:

- **Stated-not-proved boundary nodes** — Gödel I/II, the halting problem, Tarski
  undefinability (`math-logic`); `martingale`, `stochastic_process`,
  `kolmogorov_extension_theorem` (`math-probability`). These get a *mention*, not
  a runnable beat — there is nothing to execute.
- **Deep cardinal / ordinal arithmetic** past `infinite_cardinal_arithmetic`.
- **`draft` nodes** — the 15 derived-formula nodes in `physics-thermodynamics`,
  10 in `physics-thermoacoustics`, `rott_wave_equation`. Promote the node first.
- **Pure plumbing** — `notation_convention` nodes, a few `support`-role lemmas
  that exist only to keep an edge honest.

---

## 6. Where to start — a recommended first six

Ranked by (reader value × small prerequisite closure × checks already in the
capsule × infrastructure readiness):

1. **Three axioms, ten lines of consequences** (`math-probability`, → `boole_inequality`) — closure of 10, every check is a Lean core or a one-line `bc`, immediately useful.
2. **√2 is irrational — and that's a crisis** (`math-number-systems`, → `rational_incomplete_lub`) — the best hook in the whole stack; `bc` exhibits the incompleteness directly.
3. **Why heat engines have a ceiling** (`physics-thermodynamics`, → `carnot_efficiency`) — already wanted in `BACKLOG.md`; `formula-tree-tutorial` builds it today, no new infrastructure.
4. **The concentration ladder** (`math-probability`, Markov → … → Hoeffding) — one idea (Markov) applied four times; the Lean file already has the Markov and Chebyshev cores.
5. **What counts as a proof** (`math-logic-and-proof`, the `proof_methods` block) — the most broadly useful lesson in the repo; needs `theorem-tree-tutorial` or a hand build in the `hole-in-the-rationals` style.
6. **From the empty set to the real line** (cross-capsule: sets → numbers → analysis) — the flagship that shows why the *stack* exists; needs the cross-capsule convention (Tier 4) sorted out first.

Items 1, 2, 4 need the `theorem-tree-tutorial` skill (or a hand build); item 3
is buildable now; items 5–6 need new infrastructure. **The highest-leverage
single move is building `theorem-tree-tutorial`** — it unlocks every Tier-1 math
row.

---

## 7. Open questions

- **One skill or two?** `theorem-tree-tutorial` (math) and `formula-tree-tutorial`
  (physics) share ~80% of their method. Merge into `capsule-tutorial`, or keep
  the domain-specific check vocabulary (dimensional check vs type check)
  separate?
- **Cross-capsule `deps:` convention.** A Tier-4 tutorial references blocks and
  `validation/` scripts in two capsule directories. Relative paths from the
  tutorial's own location? A manifest? This blocks all of Tier 4.
- **Static companions.** Each `upmd` tutorial can have a browse-only Artifact
  with outputs pre-baked. Publish per-tutorial, or one gallery?
- **Where do tutorials live?** Currently `skills/<capsule>/tutorial/`. Tier-4
  cross-capsule tutorials have no single home — `docs/tutorials/`? A
  `tutorials/` top-level?
- **Audience labelling.** "What counts as a proof" and "The Central Limit
  Theorem" are worlds apart in required background. Tag each tutorial with a
  prerequisite level (what the *reader* needs, not what the capsule needs)?
