# Backlog

Lightweight, repo-native task tracker. No external issue tracker yet — this file
is it. One `##` section per skill / area. Keep entries short; lead each with the
**skill** it concerns (bold), then link to the file or node it touches.

Format:

```
- [ ] **skill-name:** short description  (context / where)
- [x] **skill-name:** done thing  (2026-09-06)
```

---

## math-logic-and-proof

- [ ] **math-logic-and-proof:** Mathlib-backed completeness formalisation — connect
      `godel_completeness_theorem` to `Mathlib.ModelTheory` (`FirstOrder.Language` +
      its completeness development) and upgrade `lean_status` from `cited` to
      `mathlib_cited` where the kernel actually verifies the link. Also
      `post_completeness_theorem` for a countable atom set is feasible in plain
      Lean (Lindenbaum by `Nat`-recursion + LEM, truth lemma by structural
      induction — no Mathlib).  (`validation/proof-checks.lean`, `validation/proof-checks.md`)
- [ ] **math-logic-and-proof:** `ptx` symbol / KWIC index — a keyword-in-context
      index over the corpus so every result mentioning `sup`, `epsilon`,
      `sigma_algebra`, … is findable; confirm every lead with `rg`.  (would live at
      `indexes/symbol-index.md`; see the sibling
      `math-sets-functions-cardinality/build/gen-symbol-index.sh`)
- [ ] **math-logic-and-proof:** Promote `draft` nodes to `reviewed` — most of the
      130 registry rows are still `status: draft`. Walk the math-theorem-tree
      step-7 validations per node (type check, ≥1 specialisation, ≥1
      hypothesis-dropped counterexample, Lean/bc cross-check) and bump `status` in
      `nodes/nodes.tsv` + `results/*.yaml` as each passes.  (`nodes/nodes.tsv`)
- [ ] **math-logic-and-proof:** Formalise the `Deriv ↔ H` round trip (currently
      `nd_hilbert_equivalence` is `lean_status: partial` — only the deduction
      theorem + `H.self` are checked). Needs a weakening lemma for `Deriv` and
      Hilbert derivations of the `∧`/`RAA` schemas.  (`validation/proof-checks.lean`)
- [ ] **math-logic-and-proof:** Add the remaining `validation/` worksheet files the
      result YAMLs point at: `type-checks.md`, `specialization-cases.md`,
      `instance-checks.md` (only `proof-checks.md` and the `.lean` / `.bc` exist so far).
- [ ] **math-sets-functions-cardinality:** Release 0.2 — replace its five logic
      primitives (`proposition_logic`, `predicate_logic`, `quantifier_negation`,
      `quantifier_order`, `proof_methods`) with `requires` edges into the
      corresponding developed nodes in `math-logic-and-proof`.  (cross-capsule; see
      `math-logic-and-proof/edges/cross-capsule.md`)

## simulation

- [ ] **simulation:** Consider a `templates/` charter + reporting skeleton the skill
      can emit (currently the templates live inline in `references/workflow.md`).
- [ ] **simulation:** Extend `verification/` beyond the M/M/1 DES case — one
      continuous-time (analytic ODE benchmark) and one Monte Carlo (dependence /
      tail-risk) worked check would cover more of the paradigm table.

## Done

- [x] **math-logic-and-proof:** capsule — 130-node acyclic graph, detail page for
      every node, 21 headline result YAMLs, Lean + bc validation, generated
      indexes; `sh build/all.sh` green.  (2026-09-06)
- [x] **simulation:** new skill — SKILL.md + 4 references + M/M/1 DES verification
      run; merged to main.  (2026-09-06)
