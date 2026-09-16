# Backlog

Lightweight, repo-native task tracker for **near-term, actionable** work on
skills that already exist. No external issue tracker yet — this file is it.

Organised by domain, then by skill. Keep entries short; lead each with the
**skill** it concerns (bold), then link to the file or node it touches.

Format:

```
- [ ] **skill-name:** short description  (context / where)
- [x] **skill-name:** done thing  (2026-09-06)
```

For the **speculative, long-horizon roadmap** of candidate new skills and
capsules — organised by domain, low confidence, no commitments — see
[`BACKLOG-BACKLOG.md`](BACKLOG-BACKLOG.md).

---

## Physics

### physics-formula-atlas  (new bridge capsule — Release 0.1 COMPLETE, 2026-09-11)

- [x] **physics-formula-atlas:** Release 0.1 built 2026-09-11. Bridge capsule
      connecting `physics-newtonian`, `physics-thermodynamics`,
      `physics-thermoacoustics` with 15 real cross-capsule `requires` edges
      (unlike `bayes-bridge`, this hierarchy has no mutual-grounding cycle,
      so the edges are real `tsort` edges, not prose). Discharge audit
      (`validation/duplicate-primitives.md`) found `physics-thermodynamics`'s
      5-primitive root set 100% duplicates `physics-newtonian`, and
      `physics-thermoacoustics` re-declares 6 `physics-thermodynamics`-
      developed concepts (incl. the first law of thermodynamics, restated
      from scratch) as disconnected roots. `build/prereq-path.py` walks any
      formula's prerequisite chain backward across capsule boundaries to its
      terminal roots — worked example:
      `physics-thermoacoustics:specific_heat_cv` crosses two capsule
      boundaries down to 5 `physics-newtonian` primitives. Combined graph
      (3 capsules + bridge): 239 nodes, 634 edges, `tsort`-clean, acyclic.
- [x] **physics-formula-atlas:** extended same-day (2026-09-11) to cover the
      new `physics-acoustics` capsule (see below): 11 new edges discharging
      all 7 of `physics-acoustics`'s roots against `physics-newtonian`/
      `physics-thermodynamics`, plus 2 more retrofitting
      `physics-thermoacoustics`'s previously-undischarged `small_amplitude`/
      `time_harmonic` roots against `physics-acoustics`. 28 cross-capsule
      edges total; combined graph now 289 nodes, 732 edges, `tsort`-clean.
      `physics-thermoacoustics` discharge rate up from 10/25 to 12/25 (13
      remaining are genuine fluid-mechanics gaps — no capsule in the stack
      develops viscosity/laminar flow — not missed discharges).
- [ ] **physics-formula-atlas:** Release 0.2 — extend to
      `chemistry-foundations` and `chemistry-electrochemistry` (both already
      claim `physics-thermodynamics` as background in prose; roughly doubles
      the capsule count and the discharge-audit work).
- [ ] **physics-formula-atlas:** discharge each physics capsule's bare
      `derivative`/`integral` math primitives against `math-real-analysis`
      (flagged in `validation/duplicate-primitives.md`'s "Known limitation"
      — mirrors what the `math-*` capsule stack already does internally).

### physics-acoustics  (new capsule — Release 0.1 COMPLETE, 2026-09-11)

- [x] **physics-acoustics:** Release 0.1 built 2026-09-11. Linear
      (small-signal) acoustics in fluids — the floor `physics-thermoacoustics`
      assumed in prose but had no real capsule for (its `small_amplitude`/
      `time_harmonic` roots were undischarged, per `physics-formula-atlas`'s
      audit). 50 nodes (18 roots/local-floor copies, 32 native), 85 `tsort`
      edges, acyclic, 0 isolated, 7 genuine roots — **all 7 discharged
      against `physics-newtonian`/`physics-thermodynamics` in the same
      session** via `physics-formula-atlas` (built to discharge itself from
      the start, unlike the two older physics capsules). Continuity +
      linearized Euler + adiabatic bulk modulus → the linear acoustic wave
      equation → plane waves, dispersion relation, impedance, intensity,
      decibels → superposition, standing waves, pipe resonance →
      reflection/transmission → the Doppler effect. `bc`-verified: speed of
      sound in dry air (343.25 m/s), the dispersion relation, SPL at 2 Pa
      (≈100 dB), pipe resonance (343 Hz / 171.5 Hz symmetric vs. mixed
      boundary), Doppler shift (767/644 Hz), air-water reflection
      coefficient (0.9994). No Lean cores this release (algebraic
      derivations + `bc` instances, same proof-policy call `bayes-bridge`
      made). Deliberately inviscid — viscosity/thermal dissipation stay
      `physics-thermoacoustics`'s territory.
- [x] **physics-acoustics:** two `upmd`-executable tutorials, built
      2026-09-11 with `formula-tree-tutorial`:
      `tutorial/how-fast-does-sound-travel.md` (minimal path to
      `speed_of_sound_ideal_gas`, capstone estimates a lightning strike's
      distance from a thunder delay) and
      `tutorial/designing-an-organ-pipe.md` (continuity + Euler → the wave
      equation → dispersion relation → pipe resonance, capstone solves for
      the pipe length that plays concert A). Both verified: `upmd --ci --all`
      exits 0 on every block, capstone and a mid-chain check both run
      standalone with their full `deps:` chain, no non-runnable fences. All
      numbers reused from `validation/instance-checks.bc` — no new physics
      introduced. Decibel scale, Doppler effect, impedance/intensity, and
      reflection/transmission left for a future tutorial (noted in both
      files' "Where to go next").
- [x] **physics-acoustics:** `physics-thermoacoustics` updated 2026-09-11 to
      document the discharge. **Not** a real `requires` edge spliced into
      `physics-thermoacoustics/edges/dependencies.plan` — that would break
      its own `graph-check.sh` (which only knows its own `nodes.tsv`) and
      contradicts the whole reason the atlas keeps cross-capsule edges in a
      separate layer. Instead: `physics-thermoacoustics/nodes/nodes.tsv`'s
      `small_amplitude`/`time_harmonic` rows gain a "discharged by
      physics-acoustics:… (physics-formula-atlas cross-capsule edge)" note
      (mirrors the `math-sets-functions-cardinality` Release 0.2 pattern);
      `scope.md`'s "Assumed background" and `README.md` both point at the
      atlas discharge explicitly. `physics-thermoacoustics`'s own graph
      unchanged and still green (104 nodes, 253 edges, 0 isolated/root-only).
- [x] **physics-acoustics:** reciprocity + horn-equation addition,
      2026-09-11, answering "are a megaphone and a long-range microphone
      symmetric devices?" with real capsule content. New nodes:
      `acoustic_reciprocity_theorem`, `webster_horn_equation`,
      `exponential_horn` (53 nodes total now, up from 50; 92 edges, still
      acyclic, 0 isolated, still 7 roots — no new roots introduced).
      `bc`-verified: the power transmission coefficient across the
      capsule's air/water boundary is exactly symmetric under swapping
      source/receiver side (reciprocity's specialization); an exponential
      horn with flare constant `m=2/m` has cutoff frequency ≈109 Hz, a
      realistic bass-horn figure. Third tutorial:
      `tutorial/horns-and-reciprocity.md`, verified the same way as the
      first two (`upmd --ci --all` exits 0 on all 4 blocks, capstone and a
      mid-chain check run standalone). Explicitly does **not** cover
      parabolic-dish directivity — a genuinely different diffraction-limited
      mechanism, noted as excluded in `scope.md` rather than conflated with
      the horn case.

### physics-thermodynamics

- [ ] **physics-thermodynamics:** Release 0.2 scope expansion — open systems and
      chemical potential (`dG = −S dT + V dP + μ dN`), phase equilibria +
      Clausius–Clapeyron, a real-gas node (van der Waals) as the correction the
      ideal-gas model omits.  (`scope.md` "Excluded" list)
- [ ] **physics-thermodynamics:** per-node detail pages (`nodes/<id>.md`) — the
      capsule currently collapses to the formula view; promote the 15 `draft`
      derived-formula nodes to `reviewed` with per-node `bc`/`lean` cross-checks.
- [x] **physics-thermodynamics:** `upmd` tutorial built 2026-09-11 —
      `tutorial/why-heat-engines-have-a-ceiling.md`, `zeroth_law` →
      `carnot_efficiency`, trimmed from the full 42-node prerequisite path
      to the physically load-bearing steps (zeroth law → first law/heat →
      reversible/isothermal/adiabatic → cycles/engines/refrigerators →
      second law (Kelvin-Planck/Clausius + their equivalence) → Carnot
      cycle → Carnot's theorem → thermodynamic temperature scale → Carnot
      efficiency). `chk_carnot_efficiency` reuses the capsule's own
      `dimensional-checks.bc` numeric case (Tc=300K, Th=600K -> eta=.5
      exactly). Capstone: Carnot ceiling for a real coal-fired steam plant
      (Th≈838K, Tc≈298K -> ~64%), contrasted with real plants' 35-40%.
      Verified: `upmd --ci --all` exits 0 on all 3 blocks, capstone and the
      mid-chain check both run standalone with their full `deps:` chain, no
      non-runnable fences. Linked from SKILL.md and README.md.
- [ ] **physics-thermodynamics:** cross-capsule — `physics-thermoacoustics`
      re-declares ideal-gas + first/second-law + entropy primitives; replace with
      `requires` edges into this capsule's developed nodes (0.2, mirrors the
      `math-*` stack pattern).

## Mathematics

### math-probability  (new capsule — Release 0.1 COMPLETE, 2026-09-06; polish pending)

The missing foundational floor under `design-of-experiments`, `simulation`,
`unknown-discovery` (forecast ledger + calibration), and any future statistics /
ML skill. Built with [`math-theorem-tree`](skills/math-theorem-tree/SKILL.md);
sits on top of `math-sets-functions-cardinality` (σ-algebras, measures) and
`math-real-analysis` (limits, integration).

**Done (2026-09-06):** `scope.md`, `conventions.md`, `objects.md`, `notation.md`,
`SKILL.md`, `README.md`; the **131-node registry** (`nodes/nodes.tsv`) and the
fully-evidenced **399-edge DAG** (`edges/dependencies.plan`) — `tsort` clean,
acyclic (BSD stderr-checked), 0 isolated; `edges/cycles.md` (4 would-be cycles
resolved: independence↔conditional via factorization def, expectation↔integral
via cited integral, + 2 modelling slips); generated indexes (hypothesis, status,
prereq-paths, counterexample, symbol/KWIC, reverse-deps); `validation/proof-checks.lean`
(Mathlib-free, **exit 0** — genuine: union bound, finite-support expectation
additivity by induction, Markov by induction; `decide` instances: Bayes,
Var=E[X²]−E[X]², binomial(4,½) mean/var, Jensen φ=square);
`validation/instance-checks.bc` (**exit 0** — Bernoulli/binomial/Poisson/exp/normal
moments, Poisson limit, memorylessness, standardized-binomial → Φ(1) CLT trend);
`sources/bibliography.md`. Convergence-mode tag defined in `conventions.md` (the
choice_grade analogue). 6 headline `results/*.yaml` written (kolmogorov_axioms,
bayes_theorem, markov_inequality, chebyshev_inequality, expectation_linearity,
central_limit_theorem).

**Added 2026-09-06 (session 2):** ALL 131 `results/<id>.yaml` + ALL 131
`nodes/<id>.md` — generated from one spec table `build/gen-results.py` (deps read
from the graph, so no drift), 6 headline entries hand-written.
`edges/relations.tsv` (45 non-prerequisite relations incl. `P(A|B)=P(A)` as
`equivalent_to` on `independence_events`). `build/check-consistency.py` (YAML↔graph
deps, source keys, relation endpoints — **all green**). New bibliography keys.
128 nodes promoted `draft`→`reviewed` in `nodes.tsv` (3 boundary nodes stay
`draft`). `build/all.sh` green end to end.

**Added 2026-09-06 (session 3 — polish):** rewrote `validation/proof-checks.lean`
using Lean 4.33 core `grind`/`omega` (still **no Mathlib, exit 0, no warnings**):
**15 genuine universal cores** now — union bound, incl-excl 2/3, Bayes
denominator, indicator algebra (`ind_and/or/compl`), `wsum_const` (E[c]=c),
`expectation_linearity` (universal in a,b, list induction), `centid` (the
centered-moment identity behind `Var=E[X²]−E[X]²` and `law_of_total_variance`),
`var_affine`, `markov_finite`, `chebyshev_reduction_fwd`, `jensen_sq` (universal
via the `t(n−t)(x−y)²` factorization), `cov_bilinear_raw`, `var_of_sum_raw`,
`corr_bound_iff` — plus `decide` instance grids. **36 nodes now `lean_status:
core`** (was ~15), 41 `cited`; every `lean_ref` points at a real declaration.
`proof-checks.md` rewritten with the genuine-vs-instance table keyed to nodes.
New `build/gen-validation-md.py` renders `validation/{type-checks,
specialization-cases,instance-checks}.md` (131 `## <node>` sections each) from
the YAMLs, so every `checks:` anchor resolves; wired into `build/all.sh`.

**Remaining for 0.1 / 0.2:** a `math-measure-and-integration` capsule as the
floor below (would discharge the 6 cited integration bridges); Release 0.2
martingales + stochastic processes (the 3 boundary nodes). *(The `upmd` tutorial
shipped: `tutorial/three-axioms.md`, 2026-09-06.)*

- [x] **math-probability:** `Prob.incl_excl_2/3` in `validation/proof-checks.lean`
      were near-vacuous (`h : s = f a b ⊢ s = f a b` — just type-checks).
      Rewritten as genuine derivations: 2- and 3-event inclusion–exclusion now
      follow (by `omega`) from finite additivity on the 3 / 7 disjoint Venn
      regions, with the alternating-sum identity as the conclusion, not a
      hypothesis. `proof-checks.md` table updated; `lean_ref`s still valid.
      Lean file checks clean (exit 0, no `sorry`/warnings). (2026-09-08)
- [x] **math-probability:** `Prob.markov_finite` was referenced in
      `proof-checks.lean`'s header + `proof-checks.md` but the theorem body was
      missing (dropped in the 0.1 polish rewrite) — restored the genuine
      list-induction proof; `sh build/all.sh` green. (surfaced building
      `concentration-ladder.md`, 2026-09-06)

**Target ~130 nodes** (2026-09-06, user): probability at this level is a
naturally high concept-load domain; 131 stays. No trim.

- [x] **math-probability:** `scope.md` — Kolmogorov axioms; σ-algebras and
      probability measures (discharge from `math-sets-functions-cardinality`);
      random variables, distribution / density / CDF; expectation, variance,
      moments, MGF/characteristic function; independence and conditional
      probability; **Bayes' theorem** as a node; joint / marginal / conditional
      distributions; covariance and correlation; key families (Bernoulli,
      binomial, Poisson, geometric, uniform, normal, exponential, gamma, beta);
      transformations and the change-of-variables formula; **inequalities**
      (Markov, Chebyshev, Jensen, Cauchy–Schwarz, Hoeffding); **limit theorems**
      (WLLN, SLLN, CLT, continuity theorem); conditional expectation as a
      projection; a stated-not-proved boundary node for martingales / stochastic
      processes (out of scope for 0.1).  Exclude: measure-theoretic
      probability *beyond* the σ-algebra/measure entry, stochastic processes,
      statistical inference (its own skill).
- [x] **math-probability:** graph + `tsort` — 131 nodes, 399 edges, acyclic,
      0 isolated; both would-be cycles resolved (see `edges/cycles.md`).
      Target revised to ~130 (high concept-load domain — kept, no trim).
      (2026-09-06)
- [x] **math-probability:** Lean validation — 15 genuine universal `grind`/`omega`
      cores + `decide` instance grids (Mathlib-free, Lean 4.33, exit 0, no
      warnings); 36 nodes `lean_status: core`, every `lean_ref` points at a real
      declaration; `proof-checks.md` rewritten. (2026-09-06)
- [x] **math-probability:** all 131 result YAMLs + 131 node pages +
      `relations.tsv` + `check-consistency.py`; `nodes.tsv` statuses promoted;
      `validation/{type-checks,specialization-cases,instance-checks}.md`
      generated (131 sections each) via `gen-validation-md.py`. (2026-09-06)
- [x] **math-probability:** `every_choice_grade` analogue — convergence-mode tag
      table in `conventions.md`; each limit-theorem YAML carries
      `convergence_mode:` (see `central_limit_theorem.yaml`). (2026-09-06)

### math-statistics  (Release 0.1 COMPLETE, 2026-09-08)  +  statistics

- [ ] **statistics → verification: the 5 gaps from the §7 displacement table**
      (2026-09-13). The table came out **7 covered / 5 judgement / 5 gaps**; no
      `SKILL.md` claim was found *wrong*, but five rest on the skill's authority
      where the harness could carry them. Each is a concrete section, cheap:
      - **CI/test duality** — the `n = 5` t-interval must exclude `mu_0` exactly
        when the level-α test rejects, over many samples. Exact; reuses step 2's
        sampler. (Principle: *report the interval, not a bare p*.)
      - **p-value uniformity under the null** + power ≈ 0.2 at a plausible
        effect at small `n`. One MC loop. (Principle: *a non-significant result
        is not evidence of no effect* — currently the skill's strongest claim
        with no local evidence at all.)
      - **pseudoreplication** — clustered data analysed at the observation level
        inflates the FPR. **Already demonstrated in `design-of-experiments`**
        (`0.29` vs `0.06`) and never ported; cite it or port it.
      - **prior sensitivity** — the same data under two defensible priors at
        small `n`, posterior interval moving materially. Conjugate
        Beta–Binomial, closed form.
      - **regression as projection** — there is no regression case anywhere in
        the harness. The one row at risk of being tutorial prose rather than a
        gap: if no case is added, shrink the principle to a pointer into the
        capsule.
      Table lives in the new `skills/statistics/verification/README.md` (which
      did not exist — a §6 violation, now fixed).

**Decision 2026-09-08: build both, the theorem-tree capsule FIRST, the
methodology skill second (it will cite the capsule).**

**`math-statistics`** — a `math-theorem-tree` capsule: mathematical statistics
as a dependency graph rooted in `math-probability`'s primitives (the
inference-layer analogue of `math-real-analysis` on `math-number-systems`). The
model / likelihood / regularity block; exponential families; sufficiency –
completeness – Basu; the optimality theorems (Cramér–Rao, Rao–Blackwell,
Lehmann–Scheffé); MLE / MoM / M-estimators / Bayes estimators; decision theory
(admissibility, minimax, James–Stein); the exact Gaussian core (`t`/`χ²`/`F`
constructed here, the sampling-distribution theorems); interval estimation and
the test/CI duality; Neyman–Pearson / Karlin–Rubin / LRT / Wald / score / Wilks;
the nonparametric glue (ECDF, Glivenko–Cantelli, bootstrap, KDE); the Gaussian
linear model with Gauss–Markov. Per-result `regime:` tag
{exact | asymptotic | distribution_free | bayesian}.

- [x] **math-statistics:** Stage 1 — `scope.md`, `conventions.md`,
      `nodes/nodes.tsv` (205 nodes: 58 cited roots + 147 capsule nodes),
      `edges/dependencies.plan` (394 evidence-commented edges),
      `edges/relations.tsv`, `edges/cycles.md` (acyclic, BSD stderr-checked),
      `indexes/tsort-order.txt`. `graph-check` clean. (2026-09-08)
- [x] **math-statistics:** Stage 2 — all 206 `nodes/<id>.md` + `results/<id>.yaml`
      authored via `build/specs/spec_*.py` -> `build/gen-results.py` (dependency
      lists pulled from the graph so they cannot drift). `notation.md`,
      `objects.md`, `sources/bibliography.md` (~90 refs), and the generated
      indexes (regime, hypothesis, counterexample, status, symbol-KWIC,
      prerequisite-paths, reverse-deps) done. (2026-09-08)
- [x] **math-statistics:** Stage 3 — `validation/proof-checks.lean` (Lean 4.33,
      no Mathlib, exit 0, no `sorry`/`axiom`/warnings): **26 GENUINE universal
      cores** (`score_mean_zero`, `information_equality`, `centid`, `mse_decomp`
      = `posterior_mean_completes_square`, `ssq_expand`/`bias_sample_var`,
      `anova_cross_term_zero`, `crlb_cauchy_schwarz`, `neyman_pearson_swap`,
      `rao_blackwell_var`, `factorization_discrete`, `basu_step`,
      `bonferroni_bound`, `consistency_chebyshev`, `chisq_mgf_add`,
      `interior_max_stationary`, `mle_invariance_monotone`, `pivot_coverage`,
      `ci_test_duality`, `sandwich_reduces_when_info_equality`,
      `kde_amise_optimal_h`, `mlr_power_monotone`, `expfam_grad_A`,
      `sample_mean_linear`, `bayes_rule_pointwise` + support lemmas) plus **8
      `decide` INSTANCE checks** over one fixed 3×2 design (`hat_matrix_idempotent`,
      `rss_expectation`, `centering_projection_rank`, `cochran_idempotent`,
      `normal_equations_stationary`, `gauss_markov_cross_term`,
      `fwl_block_elimination`, `gaussian_orthogonal_independent`).
      `lean_status` reconciled: 38 `core`, 6 `instance`, 103 `cited`; new
      `lean_status: instance` value for decide-instance-backed nodes.
      `proof-checks.md` written with the genuine-vs-instance table keyed to nodes.
      `build/all.sh` green end to end. (2026-09-08)
- [x] **math-statistics:** Stage 4 — `validation/instance-checks.bc` (bc -l, exit 0,
      8 sections): CRLB at Bernoulli/Poisson/Normal-mean (attained) vs Normal-variance
      (not attained); the n-1 divisor by full n=3 die enumeration (E[S^2] = 35/12);
      t-density-at-0 -> 1/sqrt(2pi), chi^2 d.o.f. additivity, F_{1,k} = t_k^2;
      Neyman-Pearson threshold N(0,1) vs N(1,1) (size 0.05, one-sided power 0.2595 >
      two-sided); Rao-Blackwell variance drop (ratio 0.158 < 1); OLS on the 3-point
      design (beta_hat = 7/6, 1/2; residuals orthogonal; R^2); Wald-interval coverage
      for Binom(20, 0.2) = 0.921 < 0.95 (undercoverage); Benjamini-Hochberg step-up
      rejects 4 vs Bonferroni 1. `build/all.sh` green (lean + bc). (2026-09-08)
- [x] **math-statistics:** Stage 5 — `SKILL.md` (front-door, full description),
      `CHANGELOG.md` (Release 0.1 summary); 201 nodes promoted `draft`->`reviewed`
      in `nodes.tsv` (wired through `build/nodespec.py` so the YAML `status:`
      mirrors the registry), 5 boundary nodes (`le_cam_lan_theory`,
      `hajek_convolution_theorem`, `local_asymptotic_minimax`, `donsker_theorem`,
      `minimax_rate`) kept `draft` for 0.2. `build/all.sh` green end to end.
      **Release 0.1 published.** (2026-09-08)

**Release 0.2 territory:** a `math-linear-algebra` capsule below (discharges
`linear_algebra_background`); LAN/Hajek/LAM proved not stated; martingale +
sequential methods; deeper empirical-process layer; GLMs beyond the exp-family
mention.
- [x] **math-statistics:** acknowledged gap CLOSED — `math-linear-algebra`
      Release 0.1 built 2026-09-13 (see its own section below). All 11 items
      `linear_algebra_background` enumerated are developed nodes there, and all
      10 `tsort` consumers of that node inside `math-statistics` are supplied.
      Discharge recorded as metadata in
      `math-linear-algebra/edges/cross-capsule.md` (11-row item table + 10-row
      per-consumer table), NOT as a graph edge — the
      `math-sets-functions-cardinality` 0.2 / `physics-thermoacoustics` pattern.
      `math-statistics` side updated the same day: the `nodes.tsv` row, the
      `spec_roots.py` ROOT stub (the "FLAGGED for a future capsule" note
      replaced by the citation), `scope.md` (both passages), and
      `sources/bibliography.md`. `sh build/all.sh` still green for
      `math-statistics` — its graph is untouched.

### math-linear-algebra  (new capsule — Release 0.1 COMPLETE, 2026-09-13)

The floor under `math-statistics`, built to discharge its
`linear_algebra_background` node. 198 nodes, 599 `tsort` edges, **acyclic on
the first pass**, 0 isolated, 19 roots.

- [x] **math-linear-algebra:** Release 0.1 — graph, all 198 entries, Lean, `bc`,
      seven indexes, `SKILL.md`/`README.md`/`CHANGELOG.md`. Areas: matrices 39,
      vector spaces 28, spectral 27, inner product 25, eigentheory 24, linear
      maps 20, determinants 17, foundations 16, boundary 2. Coverage runs from
      the vector-space axioms through rank-nullity and duality, elimination and
      the four subspaces, the determinant, eigentheory (Cayley-Hamilton, minimal
      polynomial, Schur, primary decomposition), inner product spaces
      (Gram-Schmidt, projection, least squares, QR) to spectral theory (both
      spectral theorems, Courant-Fischer, definiteness, Sylvester inertia, SVD,
      pseudoinverse, Eckart-Young, condition number).
- [x] **math-linear-algebra:** **`field_scope`** as the headline per-result tag
      (`any_field` 121 / `real_or_complex` 45 / `algebraically_closed` 8 /
      `ordered_field` 5 / `char_not_2` 3; 16 untagged roots+conventions) — the
      analogue of `math-statistics`'s `regime`, and the tag that does the most
      work in this domain. Plus `choice_grade` inherited from
      `math-sets-functions-cardinality`: 197 `choice_free`,
      `basis_existence_general` the sole `needs_full_AC` (Blass 1984).
- [x] **math-linear-algebra:** five would-be cycles designed out during edge
      derivation, not discovered afterwards (`edges/cycles.md`):
      determinant↔eigenvalue (eigenvalue defined by `Av=λv`, determinant as the
      unique normalised alternating form), determinant↔its own existence theorem
      (the theorem is stated about alternating forms WITHOUT naming det),
      rank↔determinant (rank = `dim im T`; minors downstream), basis↔dimension
      (Steinitz first), Gram-Schmidt↔orthogonal projection.
- [x] **math-linear-algebra:** **new `lean_status` value `dim_core`** —
      universal in the matrix entries at a FIXED dimension. Stronger than a
      numeric instance (every entry is a bound variable), weaker than the
      theorem (which quantifies over n). 13 `core`, 19 `dim_core`, 8 `instance`,
      1 `partial`, 110 `cited`, 2 `stated_not_proved`. Lean 4.33 Mathlib-free,
      exit 0, no `sorry`/`axiom`/warnings, 87 declarations.
- [x] **math-linear-algebra:** **three build guards** added, each answering a
      problem the sibling capsules had to be audited for retrospectively:
      (1) `build/leanmap.py` is the single authoritative lean_status/lean_ref
      table, applied OVER spec claims, forcing unmapped nodes to `cited` — a
      spec cannot overclaim; (2) `build/check-lean-refs.py` verifies every
      `LinAlg.*` named actually exists in the `.lean` (55 refs / 87
      declarations) and that no `cited` node names one; (3) the `bc` step
      INSPECTS ITS OUTPUT rather than its exit status — `bc`'s `quit` always
      exits 0, so the sibling capsules' `all.sh` would pass a run whose checks
      had failed. Negative-contrast tested by corrupting a check.
- [x] **math-linear-algebra:** `bc` instance checks, 12 sections, all passing.
      Section 6 reproduces **`math-statistics`'s own OLS design exactly**
      (β̂ = (7/6, 1/2), tr H = 2, residual orthogonality) as an arithmetic check
      on the cross-capsule discharge. Also the `det(kA) = kⁿ det A` trap, and
      the condition-number-vs-determinant trap (`10⁻⁵·I₄` has a vanishing
      determinant and κ = 1; `diag(1,10⁻⁵)` has a larger determinant and
      κ = 10⁵). Portability find recorded in the file header: **`abs` is a
      RESERVED name in macOS `bc`** — `define abs(x)` fails with "bad function
      definition" even without `-l`; the helper is called `aval`.
- [ ] **math-linear-algebra:** Release 0.2 — prove the Jordan normal form via
      cyclic subspaces (currently a `draft` boundary node, prerequisites
      developed); tensor/exterior algebra (which would demote the determinant's
      alternating-form definition from definition to consequence); modules over
      a PID.
- [ ] **math-linear-algebra:** discharge the three stack-internal cited roots —
      `real_number` against `math-number-systems`, `compactness_cited` and
      `extreme_value_cited` against `math-real-analysis`. (`complex_number`,
      `polynomial_ring`, and `fundamental_theorem_of_algebra` are genuine gaps
      with no capsule in the stack; FTA is the capsule's largest cited
      dependency.)
- [ ] **math-linear-algebra:** `upmd` tutorial via `theorem-tree-tutorial` —
      the `field_scope` tag is a natural beat (run the same statement over R and
      over F_2 and watch it break), as is the paired orthogonal-vs-oblique
      projection Lean check.

**`statistics`** — analysis-methodology skill (sibling of
`design-of-experiments`, `unknown-discovery`), **not** a capsule: the
disciplined workflow for inference on data *already collected*. Will cite
`math-statistics` for the theorems and keep only the workflow + a
`verification/` Monte Carlo harness.

- [x] **statistics:** (2026-09-08) `SKILL.md` + `verification/` + 3 templates.
      `verification/run.sh` (7 sections, exit 0): `bc` CRLB efficiency +
      multiplicity arithmetic; Monte Carlo of t-vs-z interval coverage, Wald-vs-
      Wilson proportion coverage, bootstrap regular-vs-non-regular, FWER
      unadjusted-vs-Bonferroni, Rao–Blackwell variance drop, normal-variance MLE
      bias. Every theorem cited to a `math-statistics` node. Mirrors the
      `design-of-experiments` verification pattern.
- [x] **statistics:** (2026-09-08) `references/` split — six files
      (`regime-and-assumptions`, `estimators-and-optimality`, `interval-estimation`,
      `hypothesis-testing-and-multiplicity`, `model-checking`, `bayesian-track`),
      each cited to `math-statistics` nodes; SKILL.md gains a "References"
      section and per-step links. The at-a-glance tables stay inline (matches
      `design-of-experiments`).

### bayes-bridge  (sidebar — planned, needs both endpoints)

A `bridge`-archetype connector once `math-probability` **and** `statistics`
exist: the Bayesian inferential apparatus as the link between the probability
capsule's Bayes' theorem and the statistics skill's estimation — priors /
likelihood / posterior, conjugacy, credible vs confidence intervals, posterior
predictive, Bayesian model comparison (Bayes factors, marginal likelihood), and
the decision-theory / calibration tie-in to `unknown-discovery`'s forecast
ledger. Named for the *correspondence*, not for "Bayes". See the "Cross-domain
bridges" section of [`BACKLOG-BACKLOG.md`](BACKLOG-BACKLOG.md).

- [x] **bayes-bridge:** Release 0.1 built 2026-09-11. 24 nodes (15 cited
      `bridge` roots from `math-probability`/`math-statistics` + 9 native:
      `prior`, `posterior_prop_prior_times_likelihood`, `conjugate_families`
      [one node, three worked instances: Beta-Bernoulli, Normal-Normal
      known-variance, Gamma-Poisson], `marginal_likelihood`, `bayes_factor`,
      `jeffreys_scale`, `bayesian_model_comparison`, `lindleys_paradox`,
      `credible_vs_confidence`), 28 `tsort` edges acyclic, 0 isolated.
      `bayesian_model_comparison` ↔ `likelihood_ratio_test_cited` and
      `credible_vs_confidence` ↔ `normal_mean_ci_known_variance_cited` linked
      via a `contrasts_with` relation (not a `requires` edge — resolves the
      backlog's open scoping question). `bc`-verified: three conjugate
      updates, Lindley's paradox (`BF_01 approx 46.3` at the classical
      alpha=0.05 rejection boundary), the flat-prior credible/confidence
      coincidence. No Lean cores this release (proofs are cited restatements
      or direct algebra — see `scope.md`'s proof policy).

### math-logic-and-proof

- [ ] **math-logic-and-proof:** Mathlib-backed completeness formalisation — connect
      `godel_completeness_theorem` to `Mathlib.ModelTheory` (`FirstOrder.Language` +
      its completeness development) and upgrade `lean_status` from `cited` to
      `mathlib_cited` where the kernel actually verifies the link. Also
      `post_completeness_theorem` for a countable atom set is feasible in plain
      Lean (Lindenbaum by `Nat`-recursion + LEM, truth lemma by structural
      induction — no Mathlib).  (`validation/proof-checks.lean`, `validation/proof-checks.md`)
- [x] **math-logic-and-proof:** `ptx` symbol / KWIC index — `build/gen-symbol-index.sh`
      (adapted from the sibling capsules) does a `ptx -A` discovery pass over
      `results/*.yaml` + `notation.md` and emits `indexes/symbol-index.md` with
      27 `rg`-confirmed keyword buckets (tautology, satisfiab, Henkin, Lindenbaum,
      compactness, Löwenheim, Gödel, Tarski, …). Wired into `build/all.sh`;
      SKILL.md + README point at it. This was the last math capsule without a
      symbol index. `sh build/all.sh` green. (2026-09-08)
- [x] **math-logic-and-proof:** Promote `draft` nodes to `reviewed` — added
      `build/audit-pages.py` (wired into `build/all.sh`): checks every node page
      for the step-7 elements (typed statement, type-check status, ≥1
      specialisation, ≥1 hypothesis-dropped counterexample/limits, Lean status,
      sources) — all 130 pass. Bumped `nodes/nodes.tsv` to the sibling-capsule
      vocab: **8 `active`** (6 syntax primitives + `first_order_logic_with_equality`
      + `equality_axioms`), **122 `reviewed`**, 0 `draft`; the 21 `results/*.yaml`
      likewise. `gen-indexes.sh` now emits a "by review status" block. README +
      SKILL "draft" wording dropped. `sh build/all.sh` green. (2026-09-08)
- [x] **math-logic-and-proof:** Formalise the `Deriv ↔ H` round trip
      (`validation/proof-checks.lean` §5–5b). Extended `H` to a classical
      calculus matching the `Deriv` fragment rule for rule (added `andI`/`andEl`/
      `andEr`/`efq`/`raaAx`, the last `(¬p→⊥)→p`); proved `Deriv.weaken`
      (context monotone under `⊆`), `H_of_deriv` (→I case = the deduction
      theorem; ∧/⊥E/RAA cases one `H.mp` each), `deriv_of_H` (each axiom a short
      `impI`-built `Deriv` theorem), and `deriv_iff_H : Deriv Γ φ ↔ H Γ φ`.
      All genuine/universal; `#print axioms deriv_iff_H` → `propext` only.
      `nd_hilbert_equivalence` + `derivability` bumped `lean_status: partial` →
      `core`. `sh build/all.sh` green. (2026-09-08)
- [x] **math-logic-and-proof:** Add the remaining `validation/` worksheet files
      the result YAMLs point at — `build/gen-validation-md.py` (adapted from the
      math-probability sibling, wired into `build/all.sh`) renders
      `type-checks.md` / `specialization-cases.md` / `instance-checks.md` from
      `results/*.yaml`, one `## <node>` section per headline result so every
      `checks:` anchor resolves. Surfaced + fixed two `lean_status` overclaims:
      `post_completeness_theorem` and `compactness_prop` claimed `core`/`partial`
      Lean proofs that don't exist in the Mathlib-free `.lean` (their own node
      pages already said `cited`) — corrected to `cited`. `sh build/all.sh`
      green. (2026-09-08)
- [x] **math-logic-and-proof:** Audited the FOL-metatheory `lean_status:
      partial` YAMLs, 2026-09-11. Confirmed against `proof-checks.lean`
      (its own header says it is "not the place for the Henkin
      construction" — no `Formula`/`Term`/`Structure`/`satisfaction`
      formalised) and against `proof-checks.md`'s own "Cited only" section,
      which already listed all 5 nodes as not formalised — the YAMLs had
      simply drifted out of sync with that ground truth. All 5 corrected
      `partial` → `cited` in both `results/*.yaml` and `nodes/*.md`:
      `soundness_fol` (the FOL-specific quantifier/eigenvariable cases are
      cited; the propositional core it reduces to genuinely is proved,
      that distinction now stated explicitly), `godel_completeness_theorem`
      (the old `lean_ref` described an aspirational Formula/Term/Structure
      plan that was never executed — preserved as a labelled "Release 0.2
      target, not a current claim" rather than deleted), `compactness_fol`
      and `lowenheim_skolem_down` (both correctly inherit
      `godel_completeness_theorem`'s corrected status), and
      `substitution_lemma_semantic` (its universal lemma is cited; the
      genuinely Lean-checked `free_for_matters` instance demonstrates the
      capture-bug mechanism but belongs to the sibling `free_for` node,
      which was already correctly labelled `core` — no change needed
      there). `sh build/all.sh` still green (130 nodes, 312 edges, 0 gaps,
      `check-yaml.py`'s 21-YAML consistency check passing) — the fix only
      touched `lean_status`/`lean_ref` text, not the dependency graph.

### math-number-systems

- [x] **math-number-systems:** fixed a pre-existing YAML parse bug —
      `results/cantor_diagonal_argument.yaml` had unquoted `[0,1]` inside a flow
      mapping (`type: real in [0,1]`). Quoted it. (2026-09-07, surfaced building
      the √2 tutorial)
- [x] **math-number-systems:** audited the other 14 `results/*.yaml` for the same
      flow-scalar bug class. Found 3 more — an **unquoted comma** inside a `{ ... }`
      symbol value split the scalar into a spurious null key, silently truncating
      `meaning`: `integer.yaml` (`its equivalence class, an integer` → key
      `an integer: null`), `rational_number.yaml` (`its class, a rational`),
      `lub_property.yaml` (`a set of reals, i.e. a set of cuts`). Quoted all three
      `meaning`/`type` values; `sh build/all.sh` green. Node pages are
      hand-authored and were unaffected. (2026-09-08)
- [x] **math-number-systems:** `tutorial/building-the-number.md` — added
      `### In the wild` + `app_sqrt2_irrational` to §3 (2026-09-08). The block
      runs the p-adic valuation criterion — `√n ∈ ℚ ⟺ vₚ(n) even for every
      prime p` — at p = 2, 3 over a sample of n and checks it against brute
      square-testing (agrees on every n); calls out n=2 (v₂=1, odd), n=4
      (v₂=2), n=12 (v₃=1). Pure-shell `bc`, no new mathematics — it is the
      `sqrt2_irrational` proof's `2|p² ⇒ 2|p` step read as a valuation-parity
      statement, and the YAML's third `applications` bullet. 24 blocks now;
      `upmd --ci --all` green.

### math-sets-functions-cardinality

- [x] **math-sets-functions-cardinality:** Release 0.2 — done 2026-09-11.
      Discharged its five logic primitives (`proposition_logic`,
      `predicate_logic`, `quantifier_negation`, `quantifier_order`,
      `proof_methods`) against the corresponding developed nodes in
      `math-logic-and-proof`. No `tsort`/`requires` edge added: the two
      capsules' foundations are mutually grounding (this capsule assumes logic
      to state ZFC; `math-logic-and-proof` assumes naive set talk for its
      semantics), so the discharge is recorded as metadata in
      `math-sets-functions-cardinality/edges/cross-capsule.md` (mirrored in
      `math-logic-and-proof/edges/cross-capsule.md`), not as a graph edge.
      `proposition_logic`/`predicate_logic` promoted `active` → `reviewed`.

## Analysis & inference methodology

### simulation

- [x] **simulation:** `templates/` extracted — `model-charter.md`,
      `experiment-design.md`, `reporting.md` lifted from `references/workflow.md`
      into an emit-ready `templates/` dir (matches `design-of-experiments` /
      `unknown-discovery` layout). SKILL.md steps 2 / 9 / 10 link the skeletons;
      `workflow.md` keeps the fidelity ladder, spec checklist, reproducibility
      manifest, and the worked example (which now fills in the templates). README
      row + `## Templates` section updated. `sh verification/run.sh` exit 0.
      (2026-09-08)
- [ ] **simulation:** Extend `verification/` beyond the M/M/1 DES case — one
      continuous-time (analytic ODE benchmark) and one Monte Carlo (dependence /
      tail-risk) worked check would cover more of the paradigm table.
- [x] **simulation:** Cross-link with `design-of-experiments` — step-9 "design the
      experiment" now points at `design-of-experiments/SKILL.md` +
      `references/simulation-doe.md` for designed multi-factor comparisons /
      power / pre-registered analysis, instead of restating. Reciprocal link
      (DOE step-6 → `simulation`) already existed. (2026-09-08)

### design-of-experiments

- [x] **design-of-experiments:** Cross-link with `simulation` — done from the
      `simulation` side (step-9 → `simulation-doe.md`); DOE step-6 →
      `simulation` link already present. (2026-09-08)

### visualization-design

- [x] **visualization-design:** cross-link with `simulation` and
      `design-of-experiments` — their report steps (simulation step 10, DOE
      step 7 visualization plan) now point at
      `visualization-design/references/evidence-and-domains.md`
      §"Simulation and DOE visualization" for the figure catalogue + labelling
      rules instead of restating. The reference already declares it "pairs with"
      both skills. (2026-09-08)
- [ ] **visualization-design:** extend `verification/` with a diagram-grammar
      check (parse a Mermaid/DOT source, confirm every edge style has a declared
      meaning in a legend node).

### unknown-discovery

- [x] **unknown-discovery:** cross-link done — the charter templates of
      `simulation` (`model-charter.md`), `design-of-experiments` (`charter.md`),
      `control-systems` (`control-charter.md`), and `tla-checker`'s completion
      requirements now point at `unknown-discovery/templates/assumption-register.md`
      for a load-bearing premise that needs a triage score + disconfirming
      signal, instead of expanding their local `assumptions_made` lists. UD step
      6 notes the register is the shared format. All 4 verifications exit 0.
      (2026-09-08)
- [ ] **unknown-discovery:** worked end-to-end example — take one messy decision
      (capacity commitment or a post-release metric drop) through steps 1–9:
      charter → epistemic map → ranked assumptions → premortem + ACH → signal
      cards → VoI-ranked backlog → forecast ledger → monitoring plan; `check.py`
      recomputes the EVPI / Brier / diagnosticity claims, wired into `run.sh`.

## Engineering practice

### test-writing  (new skill — promoted 2026-09-08 from BACKLOG-BACKLOG)

Promoted on the strength of danluu's "How well do agents use test/verification
techniques?" eval (Sept 2026): given only the name of a technique or library,
agents fall back to poor default testing across all 26 conditions tested — the
gap is real and a nudge-style skill is the thing that helped (the author's
5-bullet skill beat every tutorial-style skill, including ones with 250k GitHub
stars). Analysis-methodology archetype; a *nudge away from known failure modes*,
not a tutorial.

- [x] **test-writing:** first deliverable DONE (2026-09-13) —
      `skills/test-writing/verification/`, `sh run.sh` exits 0 in ~2 s
      (`bc -lq` + Python 3 stdlib, runs from any directory). Five subjects in
      `subjects.py`, each with one planted bug and a `buggy=True|False` switch,
      covering all four documented shapes:
      - **A** `net_cents` truncates instead of rounding half-up — the naive
        suite's expected values were **captured from the buggy run**, so it
        passes the bug *and fails the fix*: the test certifies the bug
        (Kreinin, now executable as the matrix's fourth cell)
      - **B** `unpack` forgets the back-to-front read of a Zstd-style stream —
        masked by palindromic buffers; **C** `step` transposes
        `table[state][symbol]` — masked by a symmetric jump table driven by
        identical streams
      - **D** `parse_kv` keeps the first value on a repeated key instead of the
        last — the branch sits past two guards, so uniform random bytes reach it
        in **0.0000%** of 20 000 inputs while the grammar-driven steered
        generator reaches it in **72.3%** (coverage is the measurable, not the
        adjective "structured")
      - **E** `median` returns the lower middle for even n — `min <= m <= max`
        passes it; metamorphic negation symmetry plus a symmetric-multiset
        oracle catch it
      `matrix.py` asserts three cells per bug — prescribed **detects** the bug,
      prescribed stays **green on the fixed code** (a vacuous `return False`
      would otherwise score as a perfect detector), naive **misses** it.
      `checks.bc` holds the independent half-up oracle derived from the spec
      sentence and asserts the masking premise itself (truncation and half-up
      **disagree** at 1990c/15% and **agree** at 1999c/15%, with the
      `remainder >= 50` relation swept over 2000 amounts). Negative-contrast
      audited with three corruptions, each caught by a *different* cell.
      Two findings for `SKILL.md`: (i) run a new check against code you believe
      correct, not only against the bug; (ii) ask for the branch-coverage
      number, not for the adjective.
- [x] **test-writing:** SKILL.md DONE (2026-09-13) — 125 lines, six numbered
      behaviours and nothing else: name the risky area → state the likely mistake
      and the alternative interpretation *before* the assertion → get the expected
      value from somewhere other than the code → break fixture symmetry and assert
      you did (both sides of each boundary, plus the boundary) → randomize
      structurally and report the branch-coverage fraction → run the new check
      against code you believe correct. Behaviours 5 and 6 came out of building the
      fixture, not from the eval. Plus a short "properties must discriminate"
      section (name one wrong implementation the property rejects; prefer
      metamorphic relations to bounds), a 6-item pre-ship checklist, and a
      completion report. Detail is deliberately pushed to
      `verification/README.md`; the skill states *why* it is short and cites the
      eval's meta-finding. README catalogue + Verification rows added.
      **`references/` decided (2026-09-13): none, deliberately.**
      `docs/verifying-skills.md` §7 gives the test — `references/` earns its
      place when the agent's prior is genuinely empty and the facts are not
      derivable (BSD `bc` rejecting `_`, BSD `tsort` exiting 0 on a cycle).
      `test-writing` carries no such facts: no framework API, no runner flags,
      no portability quirks. Everything it knows is a *displacement*, and
      displacements belong in the 148-line body where they are actually read —
      a `references/` file here would be the tutorial the eval warns about, one
      directory further away. The fixture is the reference: an agent wanting
      detail runs `verification/run.sh` and reads six planted bugs.
      Revisit only for a genuine tool-fact payload — a specific ecosystem's
      generator/shrinker API (`hypothesis` strategies, `proptest`, `jqwik`) or a
      mutation-testing runner's flags. That would be column two of §7, and would
      justify a file then.
- [x] **test-writing:** `test-oracle-design` decided (2026-09-13) — **ONE SKILL,
      not two.** Folded into `test-writing` behaviour 3 and the candidate row in
      `BACKLOG-BACKLOG.md` retired. The deciding evidence was the two entries'
      *Verify* columns: the fixture `test-oracle-design` proposed (planted bugs
      of the masking shapes, prescribed oracle catches each, negative-contrast
      naive test misses each) is the fixture already shipped here, subject for
      subject. Two skills cannot share one verification fixture and stay
      independently falsifiable — and a second short document overlapping this
      one would put an agent facing a testing task in front of a routing choice,
      which is the cost the eval's meta-finding says to avoid.
      What the fold-in added: behaviour 3 now names the four places a real
      expectation comes from (spec re-derivation / model-based reference oracle /
      metamorphic relation / differential testing against a genuinely
      independent implementation) and ends on the **independence test** — *does
      my oracle share code with the thing it is judging?* — because
      "two implementations" is not the property that matters. Made falsifiable
      by new fixture **subject F**: two renderers with different algorithms
      (division loop vs recursion) sharing one defective `digit_char` helper are
      wrong identically, so the differential test is green over the bug, while
      the stdlib `int(s, b)` round trip catches it. Fourth negative-contrast
      corruption added — give the recursive renderer its own correct helper and
      the `naive misses` cell fires, so the fixture guards F's *premise* too.
      SKILL.md 125 → 148 lines; the checklist gains "no oracle shares code with
      what it judges". `simulation` and `design-of-experiments` links sharpened:
      `simulation` is where the model-based oracle becomes a whole model with its
      own V&V problem; `design-of-experiments` is where the randomized comparison
      is the deliverable rather than the test.
- [x] **test-writing → docs/verifying-skills.md:** meta-finding folded in
      (2026-09-13) as new **§7, "What the document itself must be: a nudge, or a
      reference"**, with §7 renumbering the checklist to §8. Made *checkable*
      rather than advisory: for a behaviour-modification skill, **every
      `SKILL.md` section must name the default behaviour it displaces, and the
      verification must show that default failing** — authored as a
      **displacement table** kept with the verification, not in `SKILL.md`. An
      empty "default" cell means tutorial material (move to `references/` or
      `verification/README.md`); an empty "where it fails" cell means advice,
      *unless* the row is marked `judgement` (choosing what is risky, choosing
      the estimand, adjudicating evidence — unfalsifiable by a fixture, which
      hands you the subject). Unmarked rows are the thing forbidden.
      §7 also draws the distinction that keeps the rule honest: this repo has
      **behaviour-modification** skills (the eval's finding applies) and
      **tool-fact** skills (`bc`, `ed`, `tsort`, `octave`, …) where the
      reference table *is* the payload and the agent's prior is genuinely empty
      — BSD `tsort` exiting 0 on a cycle is not something a model can derive.
      Length is named as a symptom, not the metric, and the finding is
      calibrated (one eval, on testing tasks; the mechanism generalises, the
      effect size does not automatically).
      `skills/test-writing/verification/README.md` now carries the worked
      table — and it surfaced a real finding: **2 of 8 rows are `judgement`**,
      both behaviours 1 and 2, i.e. exactly the "choose what to test" half. The
      closing "gates are necessary, not sufficient" section now names those two
      rows instead of gesturing at judgement in general. §6's
      `verification/README.md` section list gains the table as item 7, and §8's
      checklist gains two items.
- [ ] **methodology-skill-builder (BACKLOG-BACKLOG):** when built, it must
      *emit* the §7 displacement table as a required artifact, and refuse a
      section that neither displaces a nameable default nor declares itself
      judgement. Row annotated.

## Tutorials

### theorem-tree-tutorial  (new meta skill — started 2026-09-06)

Math analogue of `formula-tree-tutorial`. `skills/theorem-tree-tutorial/`:
SKILL.md + `references/{upmd-mechanics,authoring-from-nodes,document-structure}.md`
drafted. Adds over the physics version: the **Lean-beat wrapper** (heredoc +
`lean` + exit check + `SKIP` guard — `upmd` has no Lean runner), the
**hypothesis-dropped-counterexample beat** (`cx_<id>` from each result YAML's
`counterexamples_when_dropped`), and **grade surfacing**
(`choice_grade` / `constructive_grade` / `convergence_mode`).

- [x] **theorem-tree-tutorial:** VERIFIED by generating
      `skills/math-probability/tutorial/three-axioms.md` (Kolmogorov axioms →
      `boole_inequality`, 17 blocks, `upmd --ci --all` green, standalone runs
      confirmed). Fixes folded into `references/`: `bc` fractions truncate → use
      integer "k out of N" counts; check a `lean_ref` is substantive before
      featuring it. README Verification-status row updated. (2026-09-06)
- [x] **theorem-tree-tutorial:** 2nd tutorial —
      `skills/math-probability/tutorial/concentration-ladder.md` (Markov →
      Chebyshev → Jensen → Chernoff → Hoeffding; now 21 blocks, `upmd --ci --all`
      green). Surfaced + fixed a missing `Prob.markov_finite` in the capsule
      Lean file. (2026-09-06)
- [x] **theorem-tree-tutorial + math-theorem-tree + math-probability:**
      `applications` field added to the result schema; "In the wild" milestone
      beat (`### In the wild` + optional runnable `app_<id>`) added to the skill;
      backfilled for 24 `math-probability` headline nodes (each cited); both
      shipped tutorials gained the beats. Fold-back: `bc` multiplication
      truncates intermediate products to `scale` (compute `app_` formulas at
      high scale, truncate at the end). (2026-09-07)
- [x] **theorem-tree-tutorial:** 3rd tutorial, different capsule shape —
      `skills/math-number-systems/tutorial/building-the-number.md` ("Building the
      number that isn't there": `integer` → … → `nth_root_exists`; 23 blocks,
      `upmd --ci --all` green). The `cx_` beat became "a broken operation on
      classes"; `applications` backfilled for 5 number-systems nodes; fixed a
      pre-existing parse bug in `cantor_diagonal_argument.yaml`. (2026-09-07)
- [x] **theorem-tree-tutorial:** "What counts as a proof" from
      `math-logic-and-proof` — shipped 2026-09-08 as
      `tutorial/what-counts-as-a-proof.md` (597bece). 17 blocks (8 `lean_`,
      4 `chk_`, 3 `cx_`); `upmd --ci --all` green, standalone runs pass.
      **New beat pattern:** `lean_` runs `#print axioms` and greps for
      `Classical.choice` to *show* each method's `constructive_grade` — the
      kernel as referee (direct / cases / induction → constructive;
      contrapositive / contradiction / "a counterexample must exist" /
      well-ordering-for-arbitrary-P → classical). Building it added a
      `§10 Proof methods` section to the capsule's `proof-checks.lean`
      (`direct_example`, `parity_dichotomy`, `sq_parity` + `#print axioms`
      battery) and a `proof_methods` worksheet to `instance-checks.bc`, and
      caught two stale `lean_status` overclaims (`post_completeness_theorem`,
      `compactness_prop` → `cited`).
- [ ] **theorem-tree-tutorial:** decide the "one skill or two" question
      (`docs/tutorial-map.md` §7) — whether to merge with `formula-tree-tutorial`
      into `capsule-tutorial` once both are exercised.
- [ ] **theorem-tree-tutorial:** settle the cross-capsule `deps:` convention
      before any Tier-4 (discharge-chain) tutorial — `docs/tutorial-map.md` §7.

### physics-thermodynamics

- [x] **physics-thermodynamics:** (duplicate of the entry above — built
      2026-09-11, see the `physics-thermodynamics` section near the top of
      this file for the full record.)

## Cross-cutting

- [x] **verification harnesses:** `docs/verifying-skills.md` written — the shared
      `verification/` contract (run.sh shape, the "re-solve a known-answer case
      with the skill's own workflow + negative-contrast guardrail" bar) plus the
      `bc` / Python / `tsort` / `lean` / `upmd` / `ptx` portability rules distilled
      from the 16 README Verification rows. Skeletons in `templates/verification/`
      (`run.sh`, `checks.bc`, `README.md`). README Verification section links both.
      (2026-09-08)
- [x] **bc marker grep was broken in 8 of 9 harnesses + the template** — found
      2026-09-13 while building the second §7 displacement table (`statistics`),
      from a stray `grep: repetition-operator operand invalid` on stderr in an
      otherwise-passing run. `grep -q '*** FAIL'` reads its argument as a BRE
      whose leading `*` is a repetition operator applied to nothing: GNU `grep`
      tolerates it, **`ugrep` (what `grep` resolves to here) exits 2**, and
      shell `if` reads 2 as false — so the clause could never fire. Proved on
      `skills/statistics`: a `*** FAIL` marker planted with the `fails` counter
      left at 0 (banner still printed, `bc` still exit 0) passed the gate with
      **exit 0**; exits 1 after the fix. Switched all nine harnesses plus
      `templates/verification/run.sh` to the fixed-string form
      `grep -qF '*** FAIL'`; all nine re-run green.
      Root cause is one level up from the original audit: it asked "can this
      assertion fail?" of every `bc` claim but never of the **runner's own
      clauses**, and three signals tested *together* always look healthy because
      the two working ones cover for the third. New §8 checklist item requires
      each of the three `bc` signals to be tested **in isolation**; recorded as
      an addendum in `docs/bc-verification-audit.md` and as a §3 row.
- [x] **skill wiring audited** (2026-09-13, d62e2e9) — `.claude/skills/` holds
      symlinks into `../../skills/` and that is the only mechanism by which a
      built skill becomes a loadable one. Two defects: `math-probability`'s link
      was **broken since the capsule shipped** (`../math-probability`, one `../`
      short), so the skill has never been loadable; and **16 of 46 repo skills
      had no link at all**. Repaired `math-probability` and wired
      `test-writing`, `statistics`, `octave`.
      Also fixed **outside the repo**: `~/.claude/skills/` held five stale
      *copies* (not symlinks) of `bc`, `csplit`, `ed`, `ptx`, `tsort` frozen at
      Sep 5; four had drifted, and the `bc` copy still taught the `x / 1`
      truncation idiom this repo's verification **disproved on macOS bc** — while
      carrying the same `version: 1.0.0` and a byte-identical description, so
      nothing distinguished it from the fixed one. Now symlinks into this repo.
      Backed up and diffed first; no content existed only in the copies.
- [x] **skill wiring COMPLETE** (2026-09-13) — the remaining 12 wired:
      `agent-automation`, `unattended-automation`, `local-first-backup`,
      `hypergraph-reasoning`, `nonfiction-book`, `bayes-bridge`,
      `math-statistics`, `math-linear-algebra`, `chemistry-foundations`,
      `chemistry-electrochemistry`, `physics-acoustics`,
      `physics-formula-atlas`. **All 46 repo skills now resolve**, every link
      uniform (`../../skills/<name>`), every target carrying a `SKILL.md` whose
      `name:` matches its directory. The earlier "deliberately unwired" reading
      was wrong — the deferral was only a usage-limit interruption.
      **A built skill nobody wired in is shelfware**, which is what the dangling
      `math-probability` link taught: a 131-node capsule with a full tutorial
      that had never once been loadable. Worth a standing check — a link-health
      sweep is three lines of shell and belongs in whatever runs the harnesses.
- [x] **version semantics defined + corpus re-based** (2026-09-13) —
      `docs/skill-versioning.md`. The field's job is to let a reader tell
      whether the text in front of them is current *and how much it matters if
      it is not*, so the levels are blast-radius, not semver's API break:
      **MAJOR = the skill was WRONG** (re-do work done under the old text),
      **MINOR = a statement changed or grew** (re-read; nothing to re-do,
      additions included), **PATCH = nothing semantic**. `MAJOR − 1` is
      therefore the number of times the skill has been wrong since release.
      Two rules make the number readable rather than a drafting log:
      *verification-only changes do not bump* (the harness is how we find out
      whether the content is right, not the content), and **release-pass fixes
      do not bump** — everything fixed during a skill's first verification is
      how it *reached* `1.0.0`, and the README Verification table is its record.
      Without that second rule every skill would start at 2.0.0–3.0.0 from
      authoring mess alone.
      All 46 re-based to `1.0.0` = "as verified at release", which also retires
      the old accidental convention where the leading digit encoded *kind*
      (1.0.0 = CLI-primitive, 0.1.0 = methodology) and four skills had no field
      at all. Then applied to documented post-release history: **MAJOR** for
      `bc` (the `x / 1` idiom), `tsort` (cycle-by-exit-status), `csplit`
      (GNU-only flags in the template), `math-probability`
      (`Prob.markov_finite`'s body missing behind a header claiming it);
      **MINOR** for `ptx`, `test-writing`, `simulation`,
      `unattended-automation`, `temporal-data-modeling` and `agent-automation`
      (1.2.0 — two recorded revisions). 14 skills are marked "verified,
      **fixed**" in the README but only 4 bump, because the other 10 were fixed
      during their release pass. **The backfill deliberately under-counts**:
      where the record does not say clearly whether the *instruction content* or
      the *harness* was wrong, the skill stays `1.0.0`. An inflated MAJOR is a
      false claim, and this field exists to stop those.
- [x] **the 4 ambiguous version cases adjudicated from git history**
      (2026-09-13). The first backfill left `ptx`, `physics-newtonian`,
      `physics-thermoacoustics` and `math-number-systems` unresolved because the
      README's prose did not say whether the *instruction content* or the
      *harness* had been wrong. Verdicts, on evidence:
      - **`math-number-systems` → 2.0.0.** `b2cc9ae`: an unquoted comma inside a
        `{ … }` flow scalar split the value into a spurious null key and
        **silently truncated** `meaning` in `integer.yaml`,
        `rational_number.yaml`, `lub_property.yaml`. Silently wrong capsule
        content, published 2026-09-06, fixed 2026-09-08.
      - **`physics-newtonian`, `physics-thermoacoustics` → 2.0.0**, and the same
        evidence caught **`chemistry-foundations`, `chemistry-electrochemistry`
        → 2.0.0** (not in the original four): each capsule README documented
        `bc -q -l validation/…bc` with no stdin redirect, so the capsule's own
        validation command **hung** when run as written, for 8 days. Fixed in
        `735a81a` with `</dev/null`.
      - **`ptx` → 1.1.0 confirmed.** `6fa714f` replaced a hedged "may split / do
        not assume" with the verified letters-only regex fact and added
        `-W`/`-A`. Additions and a confirmation, not a correction.
      Two of `docs/skill-versioning.md`'s own rules changed as a result:
      (1) "release-verification fixes do not count" was the wrong cut — the test
      is **whether a published state ever carried the error**. `bc`'s margin was
      **six minutes**: committed 13:38, copied into `~/.claude/skills` 13:44,
      fixed 14:10 — so those *are* MAJOR, while capsules whose verification ran
      inside their release commit never exposed a wrong state and stay `1.0.0`.
      (2) the capsule's own `README.md` joined the files that count, since it is
      how a reader runs the capsule. Also recorded: a loud break (hang, error) is
      still MAJOR, because "loud or silent" is a judgement call while "did the
      prescribed thing work?" is checkable.
      **A version backfill is a git-history question, not a changelog-prose
      question** — prose records what the author noticed, history records what a
      reader could have been holding. Nine skills now carry a `2.0.0`.
- [x] **`tools/check-skills.sh`** (2026-09-13) — the gate that makes the above
      more than a convention: every skill has exactly one semver `version:`
      inside its frontmatter, `name:` matches the directory, and every
      `.claude/skills` entry resolves and points at `../../skills/<name>`.
      Negative-contrast tested with five corruptions, one per check, all caught.
      Distinguishes **absent** from **DANGLING** — a dangling link looks wired
      and is the worse failure, and is exactly what `math-probability` was.
      Wired into `docs/verifying-skills.md` §8. **A field nothing checks is
      decoration** — that is the whole lesson of the `bc` fork.
- [ ] **user-level symlinks are absolute** (`/Users/sjanes/work26/clanker-tools/...`)
      because `~/.claude/skills` cannot use a relative path into the repo. They
      break if the repo moves or is renamed. Note it in the README's setup
      section, or provide an install script that rewrites them.
- [ ] **displacement tables, retro-fit:** `docs/verifying-skills.md` §7 now
      requires one per behaviour-modification skill, and exactly one skill has
      one (`test-writing`, where the rule was derived). A repo-wide rule that
      only the newest skill follows is not a rule.
      `statistics` done 2026-09-13 (**7 covered / 5 judgement / 5 gaps**; gap
      list in the math-statistics section). n=2 changed the rule twice: §7 now
      classifies **sections, not skills** (`statistics` is a nudge skill holding
      two legitimate reference tables), and requires the
      covered/judgement/gaps counts as the reportable output. Building it also
      found the dead `grep -q '*** FAIL'` clause, so the table doubles as a
      review of the harness.
      Retro-fit the rest, in descending order of expected yield — the long ones
      are where tutorial prose hides:
      `nonfiction-book`, `agent-automation`,
      `unattended-automation`, `local-first-backup`, `simulation`,
      `design-of-experiments`, `control-systems`, `unknown-discovery`,
      `temporal-data-modeling`, `hypergraph-reasoning`, `causal-sandbox`,
      `skill-evolution`, `citation-check`, `simple-technical-english`.
      Expect the table to surface (a) sections displacing nothing nameable →
      move to `references/`, and (b) `judgement` rows currently written as
      though the harness covered them. Do **not** apply it to the tool-fact
      skills (`bc`, `ed`, `csplit`, `tsort`, `ptx`, `octave`, `uv`, `typst`) —
      §7's two-column distinction exists precisely to protect their reference
      tables, which are the payload, not padding.
### octave  (new skill — built 2026-09-13)

- [x] **octave:** new CLI-primitive skill scoped to **matrix verification** —
      the gap `bc` (no matrices, 2x2 hand-rolled) and Mathlib-free Lean
      (`dim_core`, n = 2) structurally cannot reach. SKILL.md + 3 references
      (`independence`, `tolerance-and-conditioning`, `octave-gotchas`) +
      `verification/` (27 assertions against REAL math-linear-algebra claims at
      n = 4-5, rectangular and rank-deficient; negative-contrast tested twice).
      Deliberately NOT a bc successor: Octave is IEEE double and one existing
      capsule check brackets a quantity to 1e-25, which is inexpressible there.
      Scope table in SKILL.md; contract updated in `docs/verifying-skills.md`
      Section 6b.
- [x] **octave -> math-linear-algebra:** DONE 2026-09-13.
      `validation/matrix-checks.m`, **120 assertions**, wired into
      `build/all.sh` (SKIPS rather than fails when octave is absent, since it is
      a heavier dependency than bc/lean). Raises the capsule from 2x2 — where
      most of its headline results are degenerate — to n = 5, 6 square, 6x4 /
      6x3 / 7x4 rectangular, rank-deficient and defective (Jordan blocks 3+2).
      New evidence for `spectral_decomposition` (resolution of the identity +
      functional calculus), `courant_fischer` (Cauchy interlacing, all 6
      principal submatrices), `moore_penrose_pseudoinverse` (four Penrose
      conditions on a RANK-DEFICIENT matrix where (A'A)^-1 does not exist),
      `eckart_young` (k=1,2,3 both norms + 300 perturbed competitors),
      `simultaneous_diagonalisation`, `schur_triangularisation`. Section H
      DEMONSTRATES that the Jordan form is numerically uncomputable rather than
      asserting it away: perturbing a 5x5 block by 1e-14 moves the eigenvalues
      by 1.59e-3, matching the predicted eps^(1/5). All 8 sections
      negative-contrast tested. No `lean_status` changed, graph untouched;
      Release 0.1a in the CHANGELOG.
- [ ] **octave:** consider a second consumer — `math-statistics`' Gaussian
      linear model block (hat matrix, Cochran, ANOVA decomposition) is matrix
      content currently checked only at the 3-point design in `bc`.

- [x] **bc verification audit** — all 24 `.bc` harnesses across 20 skills
      re-checked 2026-09-13; results in [`docs/bc-verification-audit.md`](docs/bc-verification-audit.md).
      **Only 4 of 24 would catch a wrong number.** 1 outright broken
      (`hypergraph-reasoning` computed PASS/FAIL verdicts that no one read —
      FIXED + negative-contrast tested), 15 "unasserted" (print a number beside
      a prose `(want ...)`; nothing compares them), 4 never invoked by any
      script. Each category was demonstrated by corrupting a value and
      confirming the harness still reported success; all corruptions reverted
      and every harness re-verified green. `docs/verifying-skills.md` updated
      with the two `bc` facts (`quit` always exits 0; `abs` is reserved on
      macOS), the BSD numeric-args-only and multi-line-`define` rules, a new
      "Assert, do not annotate" section, and two new checklist items.
      `templates/verification/` rewritten to the asserting pattern (it was the
      source propagating the weakness) and negative-contrast tested.

- [x] **bc harnesses — all 15 "unasserted" files now assert** (2026-09-13,
      commits 7b7a3e3 / d863651 / this one). Every claim prints a `*** FAIL`
      marker on mismatch and every runner greps for it. Each file
      negative-contrast tested; all 24 harnesses verified green afterwards.
      Seven further defects surfaced in the process — two VACUOUS checks
      (`statistics` CRLB, `visualization-design` lie factor: expected value and
      computed value were the same expression), a false claim in
      `control-systems` (0.8 s called "far outside" a ceiling of 1.0 s), four
      dimensional-check helpers that printed without returning a status, two
      `.bc` files with no trailing `quit` that HUNG when run as documented, a
      bare `grep -q FAIL` false-positiving on descriptive text, and tolerances
      tighter than the next Taylor term. All recorded in
      `docs/bc-verification-audit.md`.

- [x] **bc harnesses — the 4 unautomated capsules are now automated**
      (2026-09-13). `chemistry-foundations`, `chemistry-electrochemistry`,
      `physics-newtonian`, `physics-thermoacoustics` each gained a
      `build/all.sh` on the sibling pattern (graph → views → lean → asserted
      bc, failing the run on any failure) and their READMEs now lead with it
      instead of listing hand-run commands.

- [x] **capsule build dedup:** hoisted the identical `validation/graph-check.sh`
      + `build/build-tree.sh` (canonical variants: the comment-stripping
      graph-check from `math-logic-and-proof`, the `node-deps.txt` build-tree
      from `math-statistics`) into `skills/math-theorem-tree/lib/`. All 6 math
      capsules now carry a two-line `exec` shim; `build/all.sh` green for each.
      `references/package-layout.md` notes the shim/canonical split.
      (2026-09-08)

---

## Done

- [x] **physics-thermodynamics:** new capsule (Release 0.1) — 77-node acyclic
      graph (four laws, ideal gas, Carnot, entropy, potentials), `[M L T Θ N]`
      basis, `dU = δQ − δW` convention; scope/conventions/units, formula view,
      `edges/cycles.md` (5 cycles designed out), `build/run.sh` green (10 `bc`
      dimensional + 6 numeric checks, 8 Lean instance checks), registry-derived
      topic / assumption / prerequisite-path indexes.  (2026-09-06)

- [x] **unknown-discovery:** new skill — SKILL.md + 6 references
      (epistemic-map-and-assumptions, alternatives-and-challenge,
      signals-and-surprise, probes-and-value-of-information,
      forecasting-and-calibration, governance-and-failure-modes) + 3 templates
      (discovery-charter, assumption-register, discovery-report) + `verification/`
      (EVPI in `bc`; Monte-Carlo calibration / Brier floor; ACH diagnosticity;
      residual regime-shift masking; `P = I·U·(1−R)·D` triage); `sh run.sh` green.  (2026-09-06)

- [x] **visualization-design:** new skill — SKILL.md + 7 references
      (visual-selection, graphical-integrity, perception-and-hierarchy,
      accessibility, diagrams, evidence-and-domains, critique-engine) + 3
      templates + `verification/` (WCAG contrast + Tufte lie factor in `bc`,
      Okabe–Ito vs bad-palette CVD/grayscale check, rainbow-ramp failure);
      `sh run.sh` green.  (2026-09-06)

- [x] **visualization-design:** worked end-to-end example —
      `examples/support-contact-rate/` takes a messy monthly CSV + a loaded
      "make it go up and to the right" request through steps 1–9 (brief → job →
      Vega-Lite spec → integrity audit → a11y package → critique); `check.py`
      recomputes every claim, wired into `verification/run.sh`.  (2026-09-06)

- [x] **design-of-experiments:** `verification/` worked check — `bc` sample-size
      + adjustments, Monte Carlo power / design-effect / pseudoreplication-FPR /
      ANCOVA, and the 2^(4-1) alias structure two ways; `sh run.sh` green.  (2026-09-06)

- [x] **math-logic-and-proof:** capsule — 130-node acyclic graph, detail page for
      every node, 21 headline result YAMLs, Lean + bc validation, generated
      indexes; `sh build/all.sh` green.  (2026-09-06)
- [x] **simulation:** new skill — SKILL.md + 4 references + M/M/1 DES verification
      run; merged to main.  (2026-09-06)

- [ ] **evaluator-integrity:** five harness gaps from the displacement table
      (`skills/evaluator-integrity/verification/README.md`) — (1) an
      evaluator-CALL budget section, showing a loop that wins on query count
      alone at equal compute (b2 claims call-matching; only attempt-matching
      is demonstrated); (2) early stopping on the reporting set, a different
      leak channel from the argmax selection already covered (b3); (3) coupled
      solver+evaluator co-evolution, where BOTH move and attribution fails —
      the paper's central L5 problem, and b5's "hold one fixed" has no fixture;
      (4) anchor noise, a small/noisy anchor producing a wrong ACCEPT, where
      the harness supplies a perfect anchor by construction; (5) protocol-link
      families (`references/headroom-index.md` §1) — the rule gating whether
      two scores may be pooled at all is unchecked and sits upstream of every
      verified formula.  (2026-09-14)

- [ ] **experience-library:** four harness gaps from the displacement table
      (`skills/experience-library/verification/README.md`) — (1) cross-executor
      transfer (b6): no fixture plants an artifact that helps executor A and
      HURTS executor B, which is exactly the claim; (2) the promotion gate
      (b1): "a tool is admitted only after it compiles and runs" has no
      fixture, and the recurrence criterion is unmodelled; (3) activation and
      execution as interventions (b5): `bc` §5 supplies the three factors
      rather than generating them from a realistic retrieval or
      instruction-following failure; (4) staged admission (b2): HDSO runs the
      comparison in stages of increasing size, the harness runs one fixed-n
      comparison, and the sequential multiplicity is unmodelled —
      `evaluator-integrity`'s look-count sweep suggests it is not small.
      (2026-09-14)

- [x] **role-deck: the `invent` deck.** DONE 2026-09-15. The missing legality
      primitive is `unlock`, keying on resources only — plays, spend, remaining
      budget, per-card counts. It cost NO state-space growth, because all four
      are already functions of the counts vector (conditions needed a flag
      dimension; per-option cards needed expansion). The design question is
      settled in favour of resources: a judgement-gated terminal hands back the
      one decision the external draw exists to remove. But the claim recorded
      here when the deck was deferred — "terminating by exhaustion is at least
      incorruptible" — was WRONG, and the deck proved it: gated on exhaustion
      alone, the laziest legal run padded six `generate` plays to burn budget
      down to the unlock and ran exactly ONE trial. Exhaustion measures SPEND,
      NOT WORK. Fixed by pairing `remaining_at_most` with `played_at_least`.
      (`skills/role-deck`, v2.0.0)

- [ ] **role-deck: the `improve` deck (TBD).** The RSI loop — diagnose the
      bottleneck, propose, verify, retain, revise the improver — is the one
      goal shape this machinery structurally CANNOT express. L5 means the
      process revises itself, and every gate assumes the deck is fixed for the
      duration of a run: exhaustive enumeration, exact path probability, the
      budget look-ahead and `preserve_exit` all depend on a static rulebook.
      Supporting it is not a feature but a different architecture (a deck that
      emits a successor deck, with the gates re-run on the successor and some
      inheritance rule between them). Note the irony for the record: this whole
      line of work started from an RSI survey, and the RSI loop is the shape it
      cannot model.  (2026-09-15)

- [x] **role-deck: the founding premise — FIXTURED AND REFUTED 2026-09-15.**
      The claim "an agent left to choose its own sequence will skip the
      expensive hat" was the reason the skill existed and the largest gap in its
      displacement table. Eight fresh agents were handed a harness whose true
      cause is reachable only by executing it, with no deck, no prompt to run,
      and no knowledge of what was measured. **8/8 ran it unprompted.** Scored
      by `score.py`, committed before any result was seen, against bands
      pre-registered in `design.md`. The claim was STRUCK from `SKILL.md` and
      the description rather than reworded into a similar-sounding untested one
      — that substitution is exactly what `evaluator-integrity` exists to catch.
      role-deck now claims auditability and repeatability, which the structural
      gates actually prove. See `skills/role-deck/verification/premise-fixture/`.

- [ ] **role-deck: four remaining verification gaps** (was five; the founding
      premise closed above) — (1) the reroll log is claimed as a behavioural
      signal and never exercised; (2) `terminal-live` and `options-sweep` have
      no isolating mutation, so neither has been seen to fail alone; (3) the
      `die` gate has never fired on a real bias; (4) `decide`'s `expected_order`
      has no regression mutation, where `diagnose`'s does.  (2026-09-15)

- [x] **role-deck: does an agent skip the ORDERING discipline? — FIXTURED AND
      REFUTED 2026-09-15.** Sharpened from "do they enumerate" (unmeasurable,
      self-report) to the user's framing: having formed a plausible
      explanation, does an agent ask "how do I confirm this?" rather than "what
      else would produce this symptom?" That version IS measurable, by executing
      the subject's own fix. 8 agents, a gate with a visible cause that fully
      explains the symptom and a second cause invisible in the output: **8/8
      found both**, 8/8 constructed the stderr-only test case themselves, 8/8
      also tested the all-pass case unprompted, and **4/8 closed a third hole
      that was never planted**. Both behavioural justifications for this skill
      are now measured and false; what survives is auditability and
      repeatability. See `verification/ordering-fixture/RESULT.md`.

- [x] **role-deck: the laziness search.** DONE 2026-09-15 as the `work-floor`
      gate (role-deck 2.1.0). It is the only gate in the skill that is not a
      safety property: the others ask whether anything bad happens on any path,
      this asks what the LEAST work a run can do is while breaking none of
      them. `coverage` turns out to be its n=1 case. `check_deck.py` always
      prints min..max plays per card -- that line is the laziest run the deck
      permits -- and `minimum_work` (per deck or per exit) asserts intent with
      a laziest witness path on failure. Found two further holes on first
      application: invent could trial the same development twice, and decide
      could commit on one round of evidence.

- [ ] **role-deck: nothing sizes the question to the budget.** Found by the first
      real run of the `diagnose` deck (StructOrder drift, 2026-09-15). The `open`
      card asks for a `stop_condition` and nothing anywhere checks it is
      REACHABLE within the budget. The run scoped "a per-capability inventory
      across all the brief's must-ship claims" and 11 budget bought depth on one
      capability; the mismatch only became visible at the exit, where it had to
      be confessed in `residual_uncertainty` rather than fixed. Mostly a
      judgement gap — a stop condition is prose and no gate can read it — but
      two parts are mechanical and worth doing: (a) `next` already prints
      `spent`/`budget` and should also print the FLOOR and the remaining play
      headroom, so the author sizes the question against what is actually left;
      (b) the `open` card's brief should say so explicitly. Note the shape: this
      is the same class as the founding-premise gap — the deck constrains
      execution well and says nothing about whether the question was the right
      size to ask.  (2026-09-15)

- [ ] **role-deck: an instrument can be aimed at a corpse, and nothing catches it.**
      Found by the first real `diagnose` run (StructOrder, 2026-09-15), where it
      cost the entire recommendation. Grounding worked perfectly: three commands
      ran, output captured, hashed, replay-verified, nothing fabricable. And it
      was worthless, because the WHITE hat gathered
      `_bmad-output/sprint-status.yaml` (last touched 2026-07-29, commit message
      "wip lots of weird lol") and the brief's Current Build State block —
      both artifacts of a process the project had ABANDONED in favour of `kata`.
      The code they described was a month newer. The facts gathered were true
      and the conclusion drawn from them ("the tracker is stale, update it") was
      wrong, because the tracker had already been replaced. An authoritative-
      LOOKING dead file is indistinguishable from a live one at the instrument
      layer.

      This is the skill's own documented "a command is not the right command"
      limitation, which was filed as a mild caveat about relevance and is not
      mild. Unlike relevance, though, part of this IS mechanizable, which is why
      it is worth building rather than just noting: a deck should be able to
      declare its AUTHORITATIVE SOURCES (paths, globs, a command that lists
      them), and a grounded card should warn — or refuse — when its command
      reads outside that set. A staleness check is a cheap second gate: warn
      when a gathered path's mtime or last-commit date predates the code it
      purports to describe. Neither is a judgement call.

      One part of the design did hold up and should not be lost in the fix: the
      LEDGER DID NOT LIE ABOUT WHAT WAS DONE. It recorded exactly which sources
      were read, so the error was diagnosable in seconds rather than mysterious.
      That is the audit trail earning its keep in failure, which is the only
      time it matters.  (2026-09-15)

- [ ] **claim-fixture: the method has never returned a POSITIVE.** Both case
      studies refuted their claims (8/8 each). Nothing demonstrates the method
      can confirm a true claim rather than being biased toward refutation —
      possibly because the fixtures are built by someone motivated to be
      thorough, possibly because both claims were simply false. The control is
      a fixture against a default that is already known real: danluu's eval
      (cited by `test-writing`) found agents fall back to poor default testing
      across all 26 conditions, so a fixture reproducing that shape SHOULD come
      back positive. If it does not, the method is broken rather than the
      claims being false, and every result from it is suspect.  (2026-09-15)

- [ ] **claim-fixture: subject naivety is asserted, not verified.** Both case
      studies used fresh agents with filesystem access to a repo documenting
      the hypotheses under test. Unforgeable scoring means priming could not
      fake a result, but nothing measured whether subjects read that material,
      and a primed subject inflates a positive. Options: run subjects in a
      directory with no repo access, or instrument what they read.
      (2026-09-15)

- [ ] **NEW SKILL: `skill-authoring` — the standard this corpus enforces is not
      itself invocable.** Found by building the book's fat outline as a concept
      dependency graph (`docs/book/outline/`): of the 23 concepts the book
      needs, **10 are backed only by `docs/`** — displacement table, judgement
      row, harness shape, negative contrast, guard isolation, skill taxonomy,
      version-as-wrongness, changelog. 889 lines of standard governing 50
      skills, cited by 3 of them and loadable by none. There is a meta-skill for
      building a physics capsule, a math capsule and a tutorial from a capsule,
      and none for authoring a skill to the standard every skill here is held
      to. `tsort` puts `authoring-to-the-standard` at position 21 of 23 — it
      depends on nearly everything, which is why it keeps being re-explained by
      hand. Absorbing the ten docs-only concepts is the largest single payoff
      available in the corpus.  (2026-09-15)

- [ ] **NEW SKILL (or a section of the above): the collaboration itself.**
      Three concepts have no source at all and they cluster on the book's own
      stated differentiator: `agent-as-collaborator` (the agent as participant
      in quality, not producer of text), `directing-verification` (getting an
      agent to build the harness, plant the defect, run the fixture, and report
      what it found AGAINST you), and `authoring-to-the-standard`. Fifty skills,
      every one of them produced by a human and an agent working together, and
      not one skill about doing that. Same shape as the refuted premises: the
      thing most relied on was the thing never written down. Decide whether it
      is a distinct workflow or a chapter of `skill-authoring`.  (2026-09-15)

- [ ] **Corpus remediation: 35 archetype-standard failures across 29 skills.**
      Found by `skills/skill-authoring/verification/check_authoring.py` on its
      first run, and gated by a RATCHET (`baseline.txt`) so the count cannot
      grow while remediation proceeds. By gate:
      **13 `scope`** — descriptions stating no boundary at all, so nothing says
      where the skill stops applying (ed, tsort, uv, math-linear-algebra,
      math-real-analysis, math-sets-functions-cardinality, math-theorem-tree,
      physics-acoustics, physics-formula-tree, physics-newtonian,
      physics-thermoacoustics, formula-tree-tutorial, theorem-tree-tutorial);
      **10 `displacement`** — behaviour skills with no displacement table,
      because §7 was applied going forward and never backfilled;
      **9 `frontmatter`** — missing `author:` or `tags:`;
      **3 `harness`** — verification/ with a run.sh and no README.md, which is
      a §6 violation of the same kind `statistics` had.
      Remediation lowers baseline.txt. Note the ratchet's known weakness: it
      cannot distinguish "fixed two, broke two".  (2026-09-15)

- [ ] **`directed-verification` b1: RERUN REQUIRED — first attempt INVALID
      2026-09-15.** The claim (an agent asked to "verify this" produces a weaker
      artifact than one asked to "make this able to fail") is still unmeasured.
      The first run failed for two independent reasons, both recorded in
      `skills/directed-verification/verification/b1-fixture/RESULT.md`: the
      SUBJECT WAS BUGGY, so a good harness failed on the clean implementation
      and scored BROKEN — the measurement inverted quality for the best
      subjects; and four of five arm-B agents died on an API session limit,
      leaving n=1. Three fixes before rerunning: (1) assert `clean=0` as a
      PRECONDITION verified by an independent oracle before any subject sees
      the file, rather than assuming it; (2) run subjects OUTSIDE this
      repository, since all 52 skills including `test-writing` are wired into
      `.claude/skills` and the six behaviours the subjects exhibited mirror it
      closely — a confound the two earlier fixtures escaped only because they
      scored unforgeable artifacts; (3) n>=5 per arm, both arms completing.
      Still `claim-fixture`'s best candidate for a first POSITIVE, which is the
      control that method lacks.  (2026-09-15)
