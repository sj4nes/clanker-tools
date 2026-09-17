// GENERATED FILE — DO NOT EDIT.
//   source:    skills/*/SKILL.md, skills/*/CHANGELOG.md,
//              skills/*/verification/README.md
//   generator: docs/book/tools/gen-catalogue.py
//   gate:      docs/book/tools/check-book.sh  (regenerates and diffs)
// Edit the repository, or the generator; an edit here is reverted by the gate.

#import "../../preamble.typ": note, skillentry

= Behaviour skills

Each claims to displace a default the agent already has. The standard of Part II applies to these in full: the displacement table is the deliverable, and a skill with no table has not yet been held to it.

#note[21 skills. 21 carry a verification directory; 7 report displacement counts.]

#skillentry("agent-automation", "1.2.0", "behaviour",
  [Turn "have an agent do X automatically" into a controlled workflow where a language model only PROPOSES typed actions and deterministic code authorizes, executes, verifies, and logs them.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/agent-automation/verification/") — #raw("run.sh"), #emph[no README]]),
    ([wrong], [3 versions held, none MAJOR (at 1.2.0, 2026-09-09)]),
  ))
#skillentry("citation-check", "1.0.0", "behaviour",
  [Verify that a citation, reference, or bibliographic claim is real and correctly stated by treating it as a record-linkage and evidence problem, not a web search.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/citation-check/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-07)]),
  ))
#skillentry("claim-fixture", "3.0.0", "behaviour",
  [Measure whether a claimed default behaviour is real, before building a methodology on top of it.],
  (
    ([displaces], [4 covered #sym.dot.c 2 judgement #sym.dot.c 2 gaps, the 2 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/claim-fixture/verification/") — #raw("run.sh"), README]),
    ([wrong], [2 MAJOR of 7 versions held: \
#h(0.6em) 2.0.0 (2026-09-15) — the method was missing a step, and a run was lost to it \
#h(0.6em) 3.0.0 (2026-09-17) — an omission in G5 let a forgeable measurement through, so a result produced under the old text may be wrong]),
  ))
#skillentry("control-systems", "1.0.0", "behaviour",
  [Turn a system, an objective, and a set of constraints into a feedback controller that keeps the system stable, safe, performant, and robust under disturbance, uncertainty, actuator and sensor limits, and real-time implementation constraints — then verify it, validate it to the intended use, and stage its deployment.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/control-systems/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-06)]),
  ))
#skillentry("design-of-experiments", "1.0.0", "behaviour",
  [Turn a vague causal or optimization question — "what changes the outcome, by how much, under what conditions?" — into a defensible experiment charter, design, sample-size / power plan, pre-registered analysis plan, execution protocol, and decision report.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/design-of-experiments/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-06)]),
  ))
#skillentry("directed-verification", "1.4.0", "behaviour",
  [Direct an agent to do verification work in a way that lets it disagree with you, and lets you tell when it is wrong.],
  (
    ([displaces], [1 covered #sym.dot.c 4 judgement #sym.dot.c 2 gaps, the 2 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/directed-verification/verification/") — #raw("run.sh"), README]),
    ([wrong], [7 versions held, none MAJOR (at 1.4.0, 2026-09-17)]),
  ))
#skillentry("evaluator-integrity", "1.0.0", "behaviour",
  [Keep a measurement trustworthy while something is optimizing against it.],
  (
    ([displaces], [5 covered #sym.dot.c 4 judgement #sym.dot.c 5 gaps, the 5 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/evaluator-integrity/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-14)]),
  ))
#skillentry("experience-library", "1.0.0", "behaviour",
  [Govern a growing store of retained artifacts — agent memories, distilled rules, skill or playbook libraries, reusable prompts, learned tool definitions, runbook entries, "lessons learned" notes — so that adding to it keeps making the system better instead of quietly making it worse.],
  (
    ([displaces], [5 covered #sym.dot.c 4 judgement #sym.dot.c 4 gaps, the 4 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/experience-library/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-14)]),
  ))
#skillentry("hypergraph-reasoning", "1.0.0", "behaviour",
  [Build, retrieve, verify, and revise a provenance-aware multi-entity situation model — a typed, role-labelled, time-scoped knowledge hypergraph — and make an action contingent on the exact combination of facts that authorizes it.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/hypergraph-reasoning/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-08)]),
  ))
#skillentry("local-first-backup", "1.0.0", "behaviour",
  [Turn "back up my computers" into a recoverable process: inventory what matters, classify it by cost-of-loss and required restore speed, design a layered local-first topology (fast snapshots + an independent encrypted repository + an offline or off-site copy), set a retention, encryption, and key-custody policy, separate credentials so a compromised everyday machine cannot erase history, monitor for staleness and silence, and PROVE recovery with scheduled restore drills.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/local-first-backup/verification/") — #raw("run.sh"), #emph[no README]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-09)]),
  ))
#skillentry("role-deck", "2.5.0", "behaviour",
  [Run a goal-directed process as an executable rulebook whose next step is drawn EXTERNALLY, so the run is auditable and repeatable rather than improvised.],
  (
    ([displaces], [7 covered #sym.dot.c 5 judgement #sym.dot.c 1 tool-fact #sym.dot.c 4 gaps, the 4 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/role-deck/verification/") — #raw("run.sh"), README]),
    ([wrong], [1 MAJOR of 7 versions held: \
#h(0.6em) 2.0.0 (2026-09-15) — the skill was wrong]),
  ))
#skillentry("simple-technical-english", "1.0.0", "behaviour",
  [Rewrite instructions, prompts, tool descriptions, runbooks, and procedures into controlled technical English so a literal reader performs the intended action.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/simple-technical-english/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-07)]),
  ))
#skillentry("simulation", "1.1.0", "behaviour",
  [Build and run a surrogate model to answer a question about a real or hypothetical system without operating on the system itself.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/simulation/verification/") — #raw("run.sh"), README]),
    ([wrong], [2 versions held, none MAJOR (at 1.1.0, 2026-09-13)]),
  ))
#skillentry("skill-authoring", "1.2.0", "behaviour",
  [Author a new agent skill, or bring an existing one up to standard, so that it makes a claim something could disagree with.],
  (
    ([displaces], [4 covered #sym.dot.c 2 judgement #sym.dot.c 2 gaps, the 2 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/skill-authoring/verification/") — #raw("run.sh"), README]),
    ([wrong], [3 versions held, none MAJOR (at 1.2.0, 2026-09-17)]),
  ))
#skillentry("skill-evolution", "1.0.0", "behaviour",
  [Improve a natural-language instruction document — an agent skill, a system prompt, a runbook, a tool contract, a policy doc — by iterating it against a task evaluator, so that effective corrections accumulate across rounds instead of being overwritten and each revision is scoped to how reliable the recent evidence is.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/skill-evolution/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-09)]),
  ))
#skillentry("statistics", "1.0.0", "behaviour",
  [Turn a question about data that has ALREADY been collected — "what is this quantity, how sure are we, and what would change the answer?" — into a defensible inference: a formal estimand, a data-provenance audit, an explicit statistical model with its assumptions listed as first-class items, an estimator with its bias / variance / efficiency properties, an uncertainty statement whose coverage regime (exact / asymptotic / distribution-free / Bayesian) is named, pre-specified tests with multiplicity handled, model checking, and a report that states the effect with its interval and the conditions that reverse the conclusion.],
  (
    ([displaces], [7 covered #sym.dot.c 5 judgement #sym.dot.c 5 gaps, the 5 logged in #raw("BACKLOG.md")]),
    ([harness], [#raw("skills/statistics/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-08)]),
  ))
#skillentry("temporal-data-modeling", "1.1.0", "behaviour",
  [Model time-varying data as a system of relations across time intervals — not a sequence of snapshots — so the cross-time facts survive: whether an entity at one time is the same one seen earlier, whether a group split or was merely re-measured, whether a link disappeared or was never observed.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/temporal-data-modeling/verification/") — #raw("run.sh"), README]),
    ([wrong], [2 versions held, none MAJOR (at 1.1.0, 2026-09-13)]),
  ))
#skillentry("test-writing", "1.2.0", "behaviour",
  [Write tests that can actually fail on the bug you have not thought of yet.],
  (
    ([displaces], [a displacement table, but its counts are stated in prose rather than reported]),
    ([harness], [#raw("skills/test-writing/verification/") — #raw("run.sh"), README]),
    ([wrong], [3 versions held, none MAJOR (at 1.2.0, 2026-09-17)]),
  ))
#skillentry("unattended-automation", "1.1.0", "behaviour",
  [Turn "make this run automatically" into a controlled workflow that is safe to run with nobody watching: validate inputs, plan, apply guards, execute through narrow interfaces, verify postconditions, and record an audit-quality event trail — so a bad input, a flaky dependency, or a half-finished run cannot quietly corrupt state or go unnoticed.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/unattended-automation/verification/") — #raw("run.sh"), #emph[no README]]),
    ([wrong], [2 versions held, none MAJOR (at 1.1.0, 2026-09-13)]),
  ))
#skillentry("unknown-discovery", "1.0.0", "behaviour",
  [Turn a decision or a system into a repeatable discovery process that expands the search space, surfaces hidden assumptions, generates competing explanations, scans for weak signals and anomalies, and converts the resulting uncertainty into safe, prioritized learning — then keeps an uncertainty register alive with indicators, thresholds, and a calibration ledger.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/unknown-discovery/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-06)]),
  ))
#skillentry("visualization-design", "1.0.0", "behaviour",
  [Turn an audience, a message, and data or structure into the simplest visual artifact that lets that audience accurately perceive, compare, question, and act on the information — then generate it, audit it for integrity and accessibility, critique it against a rubric, and revise.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/visualization-design/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-06)]),
  ))
= Meta skills

These orchestrate other skills. Their default is displaced at the level of the workflow, so their harnesses verify a produced artefact rather than a single prescribed check.

#note[6 skills. 2 carry a verification directory; 0 report displacement counts.]

#skillentry("causal-sandbox", "1.0.0", "meta",
  [Build a small, executable, authored-rule state-transition sandbox that an agent DRIVES to observe cause and effect — run the rules forward from initial conditions to a traced outcome, or search backward from an unwanted outcome for the minimal earlier change that avoids it — instead of predicting consequences in its head.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/causal-sandbox/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-09)]),
  ))
#skillentry("formula-tree-tutorial", "1.0.0", "meta",
  [Turn a physics-formula-tree knowledge capsule (its tsort prerequisite order, node entries, and validation scripts) into a tutorial FOR PEOPLE: a plain Markdown document that runs under #raw("upmd") (upmd.dev) so the reader executes each formula's dimensional check, limiting case, and worked example interactively in a real terminal.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-05)]),
  ))
#skillentry("math-theorem-tree", "1.2.0", "meta",
  [Build, validate, and maintain a curated mathematics knowledge package: a dependency-ordered graph of primitives, notation conventions, definitions, axioms, structures, first-class hypotheses, theorems, lemmas, constructions, identities, algorithms, and counterexamples, linearized with #raw("tsort") so every prerequisite precedes what uses it.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [3 versions held, none MAJOR (at 1.2.0, 2026-09-14)]),
  ))
#skillentry("nonfiction-book", "1.0.0", "meta",
  [Produce a high-quality nonfiction book as five linked systems — positioning, research, architecture, drafting, and editorial production — rather than "writing chapters" from a vague idea.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#raw("skills/nonfiction-book/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-08)]),
  ))
#skillentry("physics-formula-tree", "1.2.0", "meta",
  [Build, validate, and maintain a curated physics knowledge package: a dependency-ordered graph of primitives, definitions, conventions, assumptions, laws, derivations, and canonical formulas, linearized with #raw("tsort") so every prerequisite precedes what uses it.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [3 versions held, none MAJOR (at 1.2.0, 2026-09-14)]),
  ))
#skillentry("theorem-tree-tutorial", "1.0.0", "meta",
  [Turn a math-theorem-tree knowledge capsule (its tsort prerequisite order, node entries, results YAML, and validation scripts) into a tutorial FOR PEOPLE: a plain Markdown document that runs under #raw("upmd") (upmd.dev) so the reader executes each definition's instance check, each theorem's specialization, and each hypothesis-dropped counterexample interactively in a real terminal, and runs the capsule's Lean cores through a shell wrapper.],
  (
    ([displaces], [#emph[no displacement table]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-06)]),
  ))
= Tool-fact skills

These carry facts an agent cannot derive — which #raw("bc") identifiers are legal, which exit code a cycle produces. The displacement rule does not apply: there is no wrong default to displace, only an absent fact, and the harness runs the real binary.

#note[11 skills. 4 carry a verification directory; 0 report displacement counts.]

#skillentry("bc", "2.0.0", "tool-fact",
  [Perform exact, reproducible, reviewable calculations with the Unix #raw("bc") calculator language instead of shell arithmetic, #raw("expr"), #raw("awk"), or Python.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 2 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The #raw("x / 1") truncation idiom does not truncate on the #raw("bc") that ships with macOS, so the prescribed rounding helper silently returned the unrounded value.]),
  ))
#skillentry("csplit", "2.0.0", "tool-fact",
  [Use #raw("csplit") to split text files into context-defined sections by line number, regex boundary, or repeated marker — producing reviewable, independently processable excerpts from large logs, reports, concatenated documents, fixtures, changelogs, SQL bundles, or generated output.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 2 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The transactional template used #raw("{*}"), #raw("-b") and #raw("--suppress-matched"), none of which exist on BSD #raw("csplit").]),
  ))
#skillentry("ed", "1.0.0", "tool-fact",
  [Edit source and config files (YAML, Rust, TOML, JSON, shell, Markdown) with the #raw("ed") line editor using a controlled inspect → target → change → verify → validate → write transaction.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-05)]),
  ))
#skillentry("knap-markdown-rendering", "2.1.0", "tool-fact",
  [Render structured data into deterministic Markdown with the #raw("knap") CLI (templates, filters, YAML front matter, tables, batch output) instead of assembling strings in code or prose.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#raw("skills/knap-markdown-rendering/verification/") — #raw("run.sh"), README]),
    ([wrong], [1 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-16) — the skill was wrong, and it was wrong about the thing it was most likely to be used for]),
  ))
#skillentry("lean", "1.0.0", "tool-fact",
  [Use Lean 4 (with Lake and, where available, Mathlib) to state, develop, check, and explain machine-verified proofs: mathematical theorems, algebraic identities and inequalities, correctness of pure functions, inductive proofs over lists/trees/syntax/traces, state-machine invariants, and specification-level claims about protocols, authorization rules, and configuration constraints.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-05)]),
  ))
#skillentry("octave", "1.0.0", "tool-fact",
  [Verify matrix and linear-algebra claims numerically with GNU Octave: check a stated formula against an independently computed reference, at realistic dimension, with a tolerance derived from conditioning rather than guessed.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#raw("skills/octave/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-13)]),
  ))
#skillentry("ptx", "1.1.0", "tool-fact",
  [Use #raw("ptx") to build a keyword-in-context (permuted) index of curated project text for fast project discovery, terminology mapping, and exact-word navigation when ordinary search is too narrow or the relevant file/phrase is unknown.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [2 versions held, none MAJOR (at 1.1.0, 2026-09-13)]),
  ))
#skillentry("tla-checker", "1.0.0", "tool-fact",
  [Use #raw("tla-checker") / #raw("tla-rs") (a lightweight Rust TLA+ checker for a supported TLA+ subset) to model bounded concurrent, distributed, transactional, or protocol-like systems, exhaustively explore reachable states, check safety invariants and deadlocks, run bounded liveness analysis, and inspect counterexample traces.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-05)]),
  ))
#skillentry("tsort", "2.0.0", "tool-fact",
  [Use #raw("tsort") to construct, validate, and explain dependency-respecting execution orders for tasks where items must occur before other items: schema/data migrations, staged config rollouts, build and code-generation phases, package installation, deployment stages, and multi-file edit plans.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 2 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The skill said to detect a cycle by checking #raw("tsort")'s exit status.]),
  ))
#skillentry("typst", "1.0.0", "tool-fact",
  [Produce a typeset PDF (or PNG/SVG) from prose and structure using the Typst markup language and its CLI, with a fast compile–preview–revise loop.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#raw("skills/typst/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-08)]),
  ))
#skillentry("uv", "1.0.0", "tool-fact",
  [Manage Python interpreters, virtual environments, dependencies, locked projects, one-file scripts, and CLI tools with Astral's #raw("uv") as deterministic, declarative commands — no manual #raw("venv") activation.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#raw("skills/uv/verification/") — #raw("run.sh"), README]),
    ([wrong], [never revised (at 1.0.0, 2026-09-08)]),
  ))
= Knowledge capsules

Dependency-ordered graphs of a domain's results, verified by their own graph, Lean and #raw("bc") harnesses rather than by a displacement table. Part III's audits are audits of these.

#note[15 skills. 0 carry a verification directory; 0 report displacement counts.]

#skillentry("bayes-bridge", "2.0.0", "capsule",
  [The Bayesian inferential apparatus as a bridge between the #raw("math-probability") capsule's Bayes' theorem and the #raw("math-statistics") skill's estimation machinery — priors/likelihood/posterior, worked conjugate families (Beta-Bernoulli, Normal-Normal, Gamma-Poisson), Bayes factors and marginal likelihood, Bayesian model comparison with Lindley's paradox as its hypothesis-dropped counterexample, and a credible-vs-confidence-interval contrast on the same worked example.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 2 versions held: \
#h(0.6em) 2.0.0 (2026-09-14) — 1 prerequisite edge the node text uses were missing from the graph.]),
  ))
#skillentry("chemistry-electrochemistry", "3.0.0", "capsule",
  [Electrochemistry for making substances and storing energy, as a curated, dependency-ordered knowledge capsule — the Faraday charge/electron/mass bookkeeping (m = ItM/zF), current efficiency and specific energy consumption, electrochemical cells and the anode/cathode convention, standard reduction potentials and the SHE, E°\_cell and ΔG = -zFE and ΔG° = -RT ln K, the Nernst equation, overpotential (activation/concentration/ohmic) and why real electrolysis costs more than E°, product selectivity (Cl2 vs O2), electrolyte transport (molar conductivity, mobility, transport number, Kohlrausch), seven named production processes (water electrolysis, chlor-alkali, chlorate, Hall-Heroult, copper refining, zinc electrowinning, reversible fuel cell), and redox flow batteries (energy-power decoupling, state of charge, the coulombic / voltage / energy efficiencies, crossover, capacity fade, the low-cost all-iron chemistry and the all-vanadium reference).],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [2 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The capsule README documented #raw("bc -q -l validation/…bc") with no stdin redirect, so the capsule's own validation command #strong[hung] when run as written — for 8 days. \
#h(0.6em) 3.0.0 (2026-09-14) — 3 prerequisite edges the node text uses were missing from the graph.]),
  ))
#skillentry("chemistry-foundations", "3.0.0", "capsule",
  [Quantitative general chemistry (general chem I) as a curated, dependency-ordered knowledge capsule — the mole and atomic bookkeeping, formulas and percent composition, balancing equations, limiting reagent and yield, solution and gas stoichiometry, thermochemistry through Hess's law and formation enthalpies, chemical equilibrium (K, Q, Kp/Kc, ICE tables, the reaction isotherm), acid–base equilibria (Kw, pH, Ka, Ka·Kb=Kw, Henderson–Hasselbalch, buffers), and redox balancing.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [2 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The capsule README documented #raw("bc -q -l validation/…bc") with no stdin redirect, so the capsule's own validation command #strong[hung] when run as written — for 8 days. \
#h(0.6em) 3.0.0 (2026-09-14) — 2 prerequisite edges the node text uses were missing from the graph.]),
  ))
#skillentry("math-linear-algebra", "2.0.1", "capsule",
  [Linear algebra as a curated, dependency-ordered knowledge capsule — the layer below math-statistics and beside math-real-analysis.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-14) — 19 prerequisite edges were missing]),
  ))
#skillentry("math-logic-and-proof", "2.1.0", "capsule",
  [Logic and proof as a curated, dependency-ordered knowledge capsule — the deepest floor under the set / number-system / analysis stack.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-14) — 4 prerequisite edges the node text uses were missing from the graph.]),
  ))
#skillentry("math-number-systems", "4.0.0", "capsule",
  [The number systems as a curated, dependency-ordered knowledge capsule: ℕ → ℤ → ℚ → ℝ, constructed and characterized.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [3 MAJOR of 4 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — An unquoted comma in a #raw("{ … }") flow scalar #strong[silently truncated] the #raw("meaning") field in three #raw("results/*.yaml") (#raw("integer"), #raw("rational_number"), #raw("lub_property")) for two days. \
#h(0.6em) 3.0.0 (2026-09-14) — 3 prerequisite edges the node text uses were missing from the graph. \
#h(0.6em) 4.0.0 (2026-09-14) — Two nodes carried #raw("lean_status: instance") whose only evidence was #raw("validation/instance-checks.bc") — bc arithmetic, not Lean.]),
  ))
#skillentry("math-probability", "4.0.0", "capsule",
  [Probability theory as a curated, dependency-ordered knowledge capsule — the missing foundational floor under design-of-experiments, simulation, and unknown-discovery.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [3 MAJOR of 4 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — #raw("validation/proof-checks.lean") named #raw("Prob.markov_finite") in its header while the theorem body was missing — a claim of machine verification for something no longer verified. \
#h(0.6em) 3.0.0 (2026-09-14) — 9 prerequisite edges the node text uses were missing from the graph. \
#h(0.6em) 4.0.0 (2026-09-14) — 12 nodes claimed Lean verification that nothing backed]),
  ))
#skillentry("math-real-analysis", "2.1.0", "capsule",
  [Real Analysis I as a curated, dependency-ordered knowledge capsule — the real line as a complete ordered field, sequences and series, the topology of the reals, limits and continuity, differentiation, Riemann integration, and uniform convergence.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-14) — 1 prerequisite edge the node text uses were missing from the graph.]),
  ))
#skillentry("math-sets-functions-cardinality", "3.0.0", "capsule",
  [Sets, functions, orders, and cardinality as a curated, dependency-ordered knowledge capsule — the layer below the number systems.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [2 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-14) — 5 prerequisite edges the node text uses were missing from the graph. \
#h(0.6em) 3.0.0 (2026-09-14) — #raw("countable_closure_properties") carried #raw("lean_status: instance") whose only evidence was #raw("validation/instance-checks.bc") — bc arithmetic, not Lean.]),
  ))
#skillentry("math-statistics", "3.0.0", "capsule",
  [Mathematical statistics as a curated, dependency-ordered knowledge capsule — the theorem layer on top of math-probability, and the floor under a future statistics analysis-methodology skill and the bayes-bridge connector.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [2 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-14) — 17 prerequisite edges were missing \
#h(0.6em) 3.0.0 (2026-09-14) — 16 nodes claimed Lean verification that nothing backed]),
  ))
#skillentry("physics-acoustics", "1.0.0", "capsule",
  [Linear (small-signal) acoustics in fluids as a curated, dependency-ordered knowledge capsule -- the floor physics-thermoacoustics needs and previously lacked.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-11)]),
  ))
#skillentry("physics-formula-atlas", "1.0.0", "capsule",
  [A bridge capsule connecting physics-newtonian, physics-thermodynamics, physics-thermoacoustics, and physics-acoustics with real cross-capsule requires edges (not prose-only discharge -- this hierarchy has no mutual-grounding cycle), plus a working prereq-path.py tool that walks any formula's full prerequisite chain backward across capsule boundaries down to its terminal primitives, axioms, assumptions, and conventions.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-11)]),
  ))
#skillentry("physics-newtonian", "2.1.0", "capsule",
  [Newtonian point-particle mechanics as a curated, dependency-ordered knowledge capsule — kinematics, Newton's three laws, work/energy and its conservation, momentum/impulse, simple harmonic motion, and Newtonian gravitation.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [1 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The capsule README documented #raw("bc -q -l validation/…bc") with no stdin redirect, so the capsule's own validation command #strong[hung] when run as written — for 8 days.]),
  ))
#skillentry("physics-thermoacoustics", "3.0.0", "capsule",
  [Linear thermoacoustics as a curated, dependency-ordered knowledge capsule — the coupling of acoustic oscillations and heat transport in thermoacoustic engines and refrigerators.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [2 MAJOR of 3 versions held: \
#h(0.6em) 2.0.0 (2026-09-13) — The capsule README documented #raw("bc -q -l validation/…bc") with no stdin redirect, so the capsule's own validation command #strong[hung] when run as written — for 8 days. \
#h(0.6em) 3.0.0 (2026-09-14) — 1 prerequisite edge the node text uses were missing from the graph.]),
  ))
#skillentry("physics-thermodynamics", "1.0.0", "capsule",
  [Classical equilibrium thermodynamics as a curated, dependency-ordered knowledge capsule — the zeroth/first/second/third laws, the ideal-gas model, heat capacities and enthalpy, reversible adiabats, the Carnot results and the thermodynamic temperature scale, entropy and the entropy-increase principle, and the thermodynamic potentials with the Maxwell relations.],
  (
    ([displaces], [#emph[not applicable to this archetype]]),
    ([harness], [#emph[no verification directory]]),
    ([wrong], [never revised (at 1.0.0, 2026-09-06)]),
  ))
