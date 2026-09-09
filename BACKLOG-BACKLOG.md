# Backlog-backlog

The **speculative, long-horizon** roadmap: candidate *new* skills and knowledge
capsules, organised by domain. Low confidence, no commitments, no dates. This is
a map of where the catalog *could* grow, not a plan.

For near-term actionable work on skills that already exist, see
[`BACKLOG.md`](BACKLOG.md).

---

## What this catalog is for

`clanker-tools` is **both a personal tool and a showcase**. The showcase angle is
deliberate: there are many agent-skill catalogs for *project building*, and few —
maybe none — aimed at the **research space**. The core intent is to have basic,
scientific, and methodological knowledge **pre-distilled and ready to employ
without re-researching it every time** — a dependency-ordered, verified body of
"already worked this out once".

That intent sets the boundary. The universe of *verifiable* knowledge is already
large and daunting; humanities and persuasion-style domains are real candidates
but are **parked behind** that universe (see the last section).

## What earns a place

A candidate domain belongs here only if it clears all four:

1. **Distillable stable core.** The knowledge is settled and slow-moving — not a
   fast-changing API, framework, or product surface.
2. **A verification method exists.** There is a way to *check* the distilled
   content mechanically — a Lean kernel, a `bc` numeric identity, a Monte Carlo
   against a closed form, a bounded model check, a worked example whose claims
   are recomputed, or two independent derivations that must agree.
3. **Saves real re-research.** Employing the skill is meaningfully cheaper than
   re-deriving or re-reading the primary sources each time.
4. **Fits an archetype** — *command-line tool* / *knowledge capsule* /
   *analysis methodology* / *meta-builder* / *human-facing tutorial* — or
   motivates a new one.

### Non-goals

- Project scaffolding, framework setup, deployment recipes (crowded elsewhere,
  and fast-moving).
- Anything needing runtime state, secrets, or network config — skills are
  procedural memory.
- Version-specific API knowledge that rots.
- Judgment-only domains with **no** verification path — until a suitable
  archetype variant exists (flagged `needs-archetype` below).

### Confidence markers

`near` — clear fit, low risk, would start today · `plausible` — fits, some
design work · `speculative` — interesting, unproven fit · `needs-archetype` —
wanted, but the current pattern can't verify it yet.

---

## Command-line tools

Extend the `ed` / `bc` / `tsort` / `ptx` / `csplit` archetype: one tool, its
footguns, its portability traps, a verification run that exercises the traps.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `jq` | JSON transform discipline — streaming, `//`, `?`, `@base64`, error semantics, `-e` exit codes | golden input/output pairs; BSD/`jq`-version differential | near |
| `git` (plumbing) | history surgery done safely — `bisect`, `rebase`, `reflog`, `worktree`, recovering lost commits | scripted repo fixtures with known-good end states | near |
| `find` + `xargs` | `-print0`/`-0`, `-exec … +` vs `\;`, `-prune`, arg-limit failures, traversal order | fixture trees; GNU vs BSD differential | plausible |
| `sed` / `awk` | the disciplined version of the tools the other skills say "don't reach for" — address ranges, in-place, field programs | known-answer transforms; BSD vs GNU differential | plausible |
| `sort` / `uniq` / `join` / `comm` / `paste` | relational algebra in coreutils — locale, `-u` stability, field separators, `join` pre-sort requirement | known-answer joins; locale-sensitivity demonstration | plausible |
| `curl` | request discipline — `--fail`, retries with backoff, redirect safety, `-w` timing, header handling | local HTTP fixture server; assert on exit codes | plausible |
| `openssl` (CLI) | cert / key inspection and generation — very high footgun surface | generate → inspect → verify round trips | plausible |
| `tar` | BSD vs GNU, extraction path-traversal safety, `--transform`, membership | archive round trips; a path-traversal payload that must be refused | plausible |
| `date` | epoch / ISO-8601 / timezone / `-d` vs `-v`, BSD vs GNU | known-instant conversions both directions | plausible |
| `make` | incrementality, `.PHONY`, pattern rules, order-only prereqs, parallel-build hazards | small Makefiles with observable rebuild behaviour | speculative |
| `sqlite3` (CLI) | transactions, `.mode`, `EXPLAIN QUERY PLAN`, `.dump` fidelity | fixture DBs; query results vs hand-computed | speculative |
| `ffmpeg` | filter-graph and codec discipline — when the defaults lie | tiny synthetic clips; assert on `ffprobe` output | speculative |

## Reference / conventions

A **new archetype**: not a methodology and not a single-tool skill, but a
distilled *spec + curated data + validator* — a lookup the agent generates
_from_, with a mechanical check that every entry still renders. The first
candidate motivates the archetype; `docs/tutorial-map.md` is the closest
existing precedent (a curated reference artifact), and `notation-and-units`
below is adjacent.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `math-notation-rosetta` | a canonical math-notation layer with three renderings — KaTeX (TeX-dialect), Typst-native math, and plain/portable Markdown — plus portability tiers (portable · markdown+katex · typst-native · extended-nonportable) and **one hard rule: generate from the canonical form into the requested target, never textually substitute between KaTeX and Typst** (Typst math is not "LaTeX with shorter commands"). v0.1 = the ~20-construct safe core (superscript, subscript, fraction, root, sum, integral, matrix, set-builder, function-map, blackboard-bold, …) as `entries/*.yaml` with per-entry `requires_grouping_when` and support-status fields; a spoken/accessibility reading per entry; defer the full precedence-aware canonical-AST emitter to v0.2. Absorbs the LaTeX-math→Typst-math map now in `skills/typst/references/markdown-migration.md`. Pairs with the `typst` skill and a future `katex` skill; feeds the `upmd` tutorial skills (math in Markdown). | every KaTeX example compiles under a pinned `katex` (needs Node); every Typst example compiles under `typst compile` (strong — binary already in use); a differential asserts the three targets of one entry are declared equivalent. **Gap:** the plain-Markdown fallback tier has no mechanical check — "legible as literal text" stays judgment, so the kernel is strong for 2 of 3 targets. | plausible |

## Mathematics — capsules

Complete the dependency towers. `math-theorem-tree` is the proven builder; Lean
is the kernel. **Linear algebra and probability are the two missing foundational
floors** under almost everything applied.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `math-linear-algebra` | vector spaces → linear maps → eigen-theory → spectral theorem → SVD; the floor under real-analysis, control, DOE, simulation, forecasting | Lean cores for the finite-dim identities; `bc` worked factorisations | near |
| `math-probability` | **promoted to near-term — see [`BACKLOG.md`](BACKLOG.md).** σ-algebras → measure → random variables → expectation → LLN / CLT → conditional expectation; the floor under DOE / simulation / forecasting / `unknown-discovery` | Lean for the discrete cores; Monte Carlo vs limit theorems in `bc`/Python | promoted |
| `math-numerical-analysis` | conditioning, stability, floating point, quadrature, root-finding, linear-solver error bounds | `bc` exact vs float; known error-bound cases | plausible |
| `math-ode-pde` | existence/uniqueness, linear systems, stability, separation of variables, weak solutions | closed-form benchmarks vs numerical integration | plausible |
| `math-group-theory` | groups → homomorphisms → quotients → Sylow → classification of finite abelian groups | Lean cores; `bc`/enumeration for small groups | plausible |
| `math-topology` | point-set (compactness, connectedness, separation) then a bridge to the analysis capsule's topology-of-ℝ | Lean for the set-theoretic cores (reuses the preimage algebra) | plausible |
| `math-complex-analysis` | holomorphy → Cauchy's theorem → residues → conformal maps | `bc` contour-integral numerics vs residue sums | speculative |
| `math-combinatorics-graphs` | counting, generating functions, extremal bounds, graph algorithms with proofs | `bc` exact counts; small-graph enumeration | speculative |
| `math-information-theory` | entropy → mutual information → source & channel coding theorems | `bc` entropy identities; simulated code rates vs bounds | speculative |
| `math-optimization-theory` | convexity → KKT → duality → gradient / Newton / interior-point convergence | known-optimum test functions; duality-gap checks | speculative |
| `math-category-theory` | objects/morphisms → functors → natural transformations → limits → adjunctions | Lean for the diagram-chase cores | speculative |
| `math-number-theory` | divisibility → congruences → quadratic reciprocity → basic analytic number theory | `bc` modular arithmetic; known reciprocity instances | speculative |

## Physical sciences — capsules

`physics-formula-tree` is the proven builder; `physics-newtonian` and
`physics-thermoacoustics` are the proof-of-method. The obvious next capsules:

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `physics-electromagnetism` | charges → fields → Maxwell's equations → waves → radiation; the biggest missing core domain | dimensional checks in `bc`; limiting cases (statics, plane waves) | plausible |
| ~~`physics-thermodynamics`~~ | **built — Release 0.1** (77-node capsule, four laws → potentials → Maxwell relations). See [`skills/physics-thermodynamics/`](skills/physics-thermodynamics/SKILL.md). 0.2: open systems / `μ`, phase equilibria, real-gas EoS. | — | done |
| `physics-statistical-mechanics` | microstates → ensembles → partition functions → the bridge to thermodynamics | `bc` for the ideal-gas and two-level-system closed forms | plausible |
| `physics-special-relativity` | postulates → Lorentz transforms → four-vectors → energy-momentum | `bc` invariant-interval and velocity-addition checks | plausible |
| `physics-fluid-dynamics` | continuity → Euler → Navier-Stokes → Bernoulli → dimensionless groups | `bc` dimensionless-number checks; pipe-flow / potential-flow limits | plausible |
| `physics-quantum-mechanics` | state space → operators → Schrödinger → measurement → harmonic oscillator / hydrogen | `bc` for the analytically solvable spectra; commutator identities | speculative |
| `physics-orbital-mechanics` | two-body → conic orbits → Kepler → transfers → perturbations | `bc` vis-viva, period, Hohmann-transfer Δv vs known missions | plausible |
| `physics-optics` | ray → wave → Fourier optics → polarisation → interferometry | `bc` thin-lens / grating / thin-film checks | speculative |
| `physics-continuum-mechanics` | stress/strain → constitutive laws → elasticity → beam theory | `bc` beam-deflection and stress closed forms | speculative |
| `physics-general-relativity` | manifolds → metric → geodesics → Einstein equations → Schwarzschild | `bc` for Schwarzschild observables (perihelion, deflection, redshift) | speculative |

## Life, earth & chemical sciences — capsules

More speculative — the "core" is less axiomatic, so the tree is more
"canonical relations" than "theorems". Still verifiable where it's quantitative.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| ~~`chemistry-foundations`~~ | **started 2026-09-09** — general chemistry I: atoms → the mole → formulas → balanced equations → limiting reagent/yield → solution & gas stoichiometry → thermochemistry (Hess) → equilibrium (K/Q/ICE) → acid–base (Ka/Kw/buffers) → redox balancing. See [`skills/chemistry-foundations/`](skills/chemistry-foundations/scope.md). **113-node acyclic graph, 215 edges, tsort clean.** Pending: detail pages, formula YAMLs, `bc`/`lean` checks. Kinetics + electrochem + orbitals explicitly deferred to the two capsules below. | `bc` mole/stoich/pH/K checks; `lean` for Hess, Ka·Kb=Kw, Henderson–Hasselbalch, Kp/Kc | in progress |
| `chemistry-reaction-thermo-kinetics` | rate laws → Arrhenius → mechanisms → catalysis (the *rate* half; equilibrium thermo already in `chemistry-foundations`) | `bc` rate-integration checks | speculative |
| `chemistry-quantum-and-bonding` | atomic orbitals → LCAO/MO → hybridisation → spectroscopy selection rules | `bc` for hydrogenic energies; symmetry/selection-rule tables | speculative |
| `synthesis-process-tree` (homesteading) | the "make everything for modern living" layer: product → route → feedstocks → unit operations → hazards, keyed by output, citing `chemistry-foundations` for the quantitative core. A **new archetype** (process/recipe DAG, not a formula tree). Motivating case for the homesteading self-sufficiency project. | mass-balance closure per route via `bc`; feedstock-reachability from a declared starting set | speculative / needs-archetype |
| `biology-population-and-evolution` | Hardy-Weinberg → selection → drift → Lotka-Volterra → epidemic (SIR) models | `bc`/simulation vs closed-form equilibria and R₀ | speculative |
| `biology-molecular-central-dogma` | replication → transcription → translation → regulation → the genetic code | reference-table checks; codon-table round trips | speculative |
| `earth-climate-and-geophysics` | radiative balance → greenhouse forcing → carbon cycle → plate kinematics → seismology basics | `bc` energy-balance-model and blackbody checks | speculative |
| `pharmacology-pk-pd` | compartment models → clearance → half-life → dose-response → therapeutic index | `bc` one/two-compartment closed forms vs numerical | speculative |

## Formal & computational — capsules and methods

Adapt the theorem-tree method to computer science's settled theory.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `cs-algorithms-and-complexity` | sorting / graph / DP / greedy with correctness proofs and bounds → P/NP/reductions → undecidability | Lean for the small correctness cores; `bc` recurrence solutions; runtime differential | plausible |
| `cs-data-structures` | amortised analysis → balanced trees → hashing → union-find → heaps, each with its invariant | Lean invariants; property tests on reference implementations | plausible |
| `crypto-primitives-tree` | hardness assumptions → one-way functions → PRGs/PRFs → symmetric & public-key → protocols, as a dependency graph | `tla-checker` for protocol cores; known-answer test vectors | plausible |
| `cs-type-systems` | STLC → System F → subtyping → progress & preservation (extends `math-logic-and-proof`) | Lean for progress/preservation on a toy calculus | speculative |
| `cs-concurrency-theory` | happens-before → linearizability → consensus (FLP, Paxos, Raft) → CRDTs | `tla-checker` bounded checks; counterexample traces | plausible |
| `formal-methods-practice` | when to reach for a model checker vs a proof vs a test; abstraction, invariants, refinement (methodology, not a capsule) | worked models in `tla-checker` / `lean`; claims recomputed | plausible |

## Analysis & inference methodology

Siblings of `simulation`, `design-of-experiments`, `visualization-design`,
`control-systems`, `unknown-discovery`. Each is a disciplined workflow with hard
guardrails and a `verification/` run whose claims are recomputed.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `statistics` (`statistical-analysis`) | **promoted to near-term (follows `math-probability`) — see [`BACKLOG.md`](BACKLOG.md).** Inference on data **already collected** — the gap `design-of-experiments` explicitly refuses; estimator choice, assumptions, multiplicity, effect sizes over p-values | Monte Carlo: coverage, error rates, the assumption-violation failures | promoted |
| `causal-inference` (observational) | DAGs → backdoor/frontdoor → IV → diff-in-diff → RDD → propensity; completes the causal-claims story `design-of-experiments` starts | simulated SCMs where the true effect is known; bias with/without adjustment | near |
| `forecasting` | time-series method behind `unknown-discovery`'s forecast ledger — decomposition, ARIMA/ETS, backtesting, drift, proper scoring | backtest vs held-out; calibration and CRPS/Brier checks | plausible |
| `optimization-modelling` | formulate → choose LP/MIP/convex/heuristic → *when not to trust the solver* (mirrors `control-systems`' "simulation ≠ proof") | known-optimum benchmarks; duality-gap and feasibility checks | plausible |
| `decision-analysis` | decision trees → expected utility → value of information → multi-criteria; the full method `unknown-discovery` only samples via VoI | `bc` EV/EVPI on trees with hand-computed answers | plausible |
| `reliability-engineering` | failure modes → fault trees → redundancy math → SLOs / error budgets → MTBF/MTTR | `bc` series/parallel reliability; simulated failure processes vs analytic | plausible |
| `root-cause-analysis` | incident investigation — timeline reconstruction, counterfactual testing, blameless postmortem, "5 whys" done without the fallacies | worked incident with a known cause; the method must recover it | plausible |
| `benchmarking` | statistically valid performance measurement — warmup, variance, common random numbers, regression detection | synthetic workloads with known distributions; false-positive rate on noise | plausible |
| `estimation` | Fermi / order-of-magnitude with every assumption explicit and a stated error band; pairs with `bc` | back-tested estimates vs known answers; interval calibration | plausible |
| `measurement-design` | operationalising a construct — validity, reliability, question wording, scale choice, index construction | simulated latent-variable recovery; reliability-coefficient checks | speculative |
| `model-evaluation` | ML eval discipline — leakage, split hygiene, metric choice, calibration, baseline comparison, subgroup performance | synthetic datasets with planted leakage; the checklist must catch it | plausible |
| `sensitivity-analysis` | local vs global (Sobol, Morris), tornado diagrams, when a result is fragile — standalone from `simulation`'s UQ step | test functions with known Sobol indices | plausible |

## Research practice

The layer that most distinguishes a *research-space* catalog from a
*project-building* one. Disciplined workflows for **doing research well**.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `evidence-synthesis` | systematic-review discipline — search strategy, inclusion criteria, risk-of-bias, GRADE, meta-analysis, heterogeneity | worked review over a fixture corpus; pooled estimate recomputed | plausible |
| `claim-appraisal` | reading a paper adversarially — spot p-hacking, HARKing, base-rate neglect, spin, underpowered designs, unsupported causal language | a fixture set of papers with planted flaws; the checklist must find them | plausible |
| `reproducibility-engineering` | making an analysis rerun — pinned environments, deterministic seeds, data provenance, `Makefile` DAGs, result diffing | a fixture analysis that must reproduce bit-for-bit on a second run | near |
| `literature-mapping` | building a citation / concept graph of a field — `tsort` for prerequisite order, `ptx` for terminology (the capsule-builder method, pointed at papers not textbooks) | graph acyclicity; every claimed edge traced to a source | plausible |
| `research-question-framing` | turning a vague interest into a sharp, answerable, falsifiable question with a stated method and a "what would change my mind" | worked examples; the PICO/estimand fields must all resolve | plausible |
| `data-provenance` | tracking where a number came from — lineage, transformations, units, as-of dates, reconciliation | a fixture pipeline; every output value traceable to inputs | plausible |
| `notation-and-units` | dimensional analysis discipline, unit systems, notation conventions, when a formula is regime-limited (generalises the physics capsules' unit checks) | `bc` dimensional checks; known unit-conversion round trips | near |

## Engineering practice

Stakeholder inversion: the catalog is ~90% *analyse / know*; agents spend most of
their time *making / doing*. High footgun surface, strong showcase value, and —
crucially — each has a verifiable core.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `debugging` | hypothesis-driven bug isolation — minimal repro, bisection, "change one thing", read the error, the scientific method applied to a defect | worked bug hunts in fixture repos; the method must localise the planted bug | near |
| `test-writing` | what to test and why — property vs example, the test pyramid, test smells, coverage ≠ confidence, mutation testing | a fixture with planted bugs; the prescribed tests must catch them, mutation score checked | near |
| `refactoring` | changing structure without changing behaviour — characterisation tests first, small reversible steps, the named refactorings | before/after fixtures; behaviour-equivalence tests must stay green | plausible |
| `code-review` | a review discipline — correctness first, then reuse/simplicity/efficiency; calibrated severity; what to skip | fixture diffs with planted issues at known severities | plausible |
| `reading-unfamiliar-code` | a systematic comprehension method — entry points, data flow, the "walking skeleton", note-taking | fixture codebase; comprehension questions with checkable answers | plausible |
| `dependency-migration` | upgrade discipline — changelog reading, staged rollout, characterisation tests, the bisect-the-upgrade trick | fixture with a breaking upgrade; the method must isolate the break | plausible |
| `sql` | query correctness — NULL three-valued logic, join multiplicity, window functions, `GROUP BY` traps, `EXPLAIN` | fixture DBs; results vs hand-computed; planted correctness traps | near |
| `api-design-review` | evaluating an interface — consistency, evolvability, failure modes, the principle of least astonishment | fixture APIs with planted design flaws | speculative |
| `commit-hygiene` | atomic, bisectable, revertable history — one logical change per commit, message discipline, when to squash | fixture histories; `git bisect` must land on the right commit | plausible |

## Meta / builders

The pattern behind the pattern. You have now hand-built the
charter → principles → workflow → guardrails → `verification/` shape six times.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `methodology-skill-builder` | the meta-skill for building an analysis-methodology skill — the shape `simulation` / `DOE` / `control-systems` / `unknown-discovery` all share, extracted | build a small new skill with it; it must pass the same checks the hand-built ones do | plausible |
| `theorem-tree-tutorial` | **STARTED 2026-09-06** — `skills/theorem-tree-tutorial/` SKILL.md + references drafted (Lean-beat wrapper, hypothesis-dropped-counterexample beat, grade surfacing). Needs a generated tutorial to verify. Tracked in [`BACKLOG.md`](BACKLOG.md). | `upmd --ci --all` green on a generated tutorial | — |
| `verification-harness-design` | the shared discipline every `verification/` reinvents — known-answer selection, BSD/GNU portability, `bc` flags, stdlib-only Python, the "folded back" write-up | apply it to an existing skill's harness; run stays green on Linux and macOS | near |
| `capsule-maintenance` | updating a knowledge capsule when a node changes — impact analysis on the `tsort` graph, re-validation scope, version bumps | change a node in a fixture capsule; the tool must identify exactly the affected downstream | plausible |
| `cross-capsule-linking` | discharging one capsule's primitives against another's developed nodes (the `math-*` stack does this by hand — see `BACKLOG.md`) | fixture capsule pair; edges must stay acyclic and every primitive covered | plausible |

## Cross-domain bridges

A `bridge`-archetype capsule connects the *developed nodes* of two or three
existing capsules and encodes the identifications, equivalences, and
regime-of-validity conditions between them. Roots are **imported** from the
capsules it joins — so a bridge is only worth building once ≥2 of its endpoints
exist. Named for the *correspondence*, never for a spanning quantity (an
"entropy" capsule would be an unbounded magnet; the method wants one bounded
domain).

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `bayes-bridge` | **queued in [`BACKLOG.md`](BACKLOG.md)** (needs `math-probability` + `statistics`). The Bayesian inferential apparatus linking the probability capsule's Bayes' theorem to the statistics skill's estimation — priors/likelihood/posterior, conjugacy, credible vs confidence intervals, Bayes factors, and the calibration tie-in to `unknown-discovery`'s forecast ledger | `bc` conjugate-update closed forms + a credible-vs-confidence contrast; Lean for `posterior ∝ prior × likelihood` | needs-endpoints |
| `entropy-bridge` | Clausius ↔ Boltzmann/Gibbs ↔ Shannon entropy: `S = k_B ln Ω`, the Gibbs/Shannon shared form, **Landauer's principle** (`k_B T ln 2` per bit), Maxwell's demon / Szilard engine, fluctuation theorems, the second law as an information statement — with each identity's assumptions (equilibrium, equal a priori probabilities) explicit | `bc` for Shannon `H`, `KL ≥ 0`, Sackur–Tetrode, Landauer energy; Lean instance checks for the Gibbs/Jensen concavity core | needs-endpoints (wait for `math-probability` / `math-information-theory` / `physics-statistical-mechanics`) |
| `least-action-bridge` | the variational thread across `physics-newtonian` (F=ma) → Lagrangian → Hamiltonian → optics (Fermat) → (later) field theory; `δS = 0` as the common root | `bc` on the Euler–Lagrange reduction for the pendulum / projectile; Lean for the `d/dt (∂L/∂q̇) − ∂L/∂q = 0 ⇔ F = ma` algebra | needs-endpoints (wait for a Lagrangian-mechanics capsule) |
| `symmetry-conservation-bridge` | Noether's theorem as the link between `physics-newtonian`'s conservation laws and continuous symmetries (time → energy, translation → momentum, rotation → angular momentum) | `bc` on the explicit invariance → conserved-quantity computation for each; instance checks in Lean | needs-endpoints |

## Human-facing lane

`formula-tree-tutorial` already crossed the line from "instruct an agent" to
"teach a person". If that lane grows it deserves its own conventions.

See [`docs/tutorial-map.md`](docs/tutorial-map.md) for the full survey of
tutorials cuttable from the eight capsules (815 nodes) — single-target,
thematic-band, whole-capsule, and cross-capsule — with a coverage estimate and a
recommended first six. Headline finding: **building `theorem-tree-tutorial` (the
math analogue of `formula-tree-tutorial`) is the highest-leverage single move**
— it unlocks every math Tier-1 row.

| Candidate | One line | Verify | Confidence |
|---|---|---|---|
| `explain-a-capsule` | generate a linear reader's path through any capsule — prerequisites first, one runnable check per concept | `upmd --ci` green; every concept's check executes | plausible |
| `worked-example-authoring` | the `check.py` pattern as a skill — take a real messy input through a methodology skill end-to-end, recompute every claim | the example's own checks pass; claims match the skill's formulas | plausible |
| `technical-writing` | structure, altitude, the inverted pyramid, precision without jargon — for docs an agent produces | rubric scoring; readability metrics; a fixture must improve on rewrite | needs-archetype |

## Humanities & persuasion — deferred

Real candidates, explicitly **parked** behind the verifiable universe above. The
blocker is archetype, not interest: these are judgment-heavy with weak
mechanical kernels. Revisit once a `needs-archetype` verification variant exists
(rubric + adversarial fixtures + human-in-the-loop calibration).

| Candidate | One line | Why it's hard to verify |
|---|---|---|
| `argumentation` | valid vs sound, the fallacy catalogue, steelmanning, burden of proof, argument mapping | the *form* is checkable (this overlaps `math-logic-and-proof`); *quality* is not |
| `persuasive-writing` | audience, rhetorical structure, ethos/pathos/logos, concision, the call to action | no ground truth for "persuasive"; needs A/B or rubric + panel |
| `rhetoric-analysis` | detecting persuasion techniques, framing, loaded language, statistical spin in a text | fixture texts with planted techniques give partial ground truth — closest to feasible |
| `negotiation` | BATNA, ZOPA, interests vs positions, anchoring, value creation vs claiming | outcomes depend on a counterparty; only simulatable |
| `narrative-structure` | story shape, tension, the promise/payoff, scene vs summary | aesthetic; no mechanical kernel |
| `pedagogy` | worked-example effect, spacing, retrieval practice, misconception targeting | learning-gain is measurable in principle, not in a repo |

---

## How to promote something off this list

1. Confirm it clears all four "what earns a place" criteria — especially #2, a
   real verification method.
2. Pick the archetype and draft the `SKILL.md` skeleton from
   `templates/skill-template`.
3. Write the `verification/` run **first** or alongside — if you can't state
   what a green run proves, the domain isn't ready.
4. Move it to `BACKLOG.md` as an active item with a concrete first deliverable.
