---
name: evaluator-integrity
description: >-
  Keep a measurement trustworthy while something is optimizing against it.
  Use when a score is being used to decide whether a change is an improvement
  — an agent or training loop selecting among candidates, a prompt or skill
  being tuned against an eval set, a judge or reward model scoring its own
  system's output, a leaderboard number, a benchmark table assembled from
  mixed sources, or any round-over-round comparison offered as evidence of
  progress. Six behaviours that displace the known default failure modes:
  comparing scores across unmatched budgets, steering and reporting on the
  same set, swapping an evaluator mid-run without re-scoring, accepting the
  judge that produces higher scores, and pooling raw percentages across
  benchmarks at different saturation. NOT a guide to picking a benchmark,
  not a statistics course, and not a substitute for deciding what capability
  you actually care about.
version: 1.0.0
archetype: behaviour
author: Simon Janes
tags: [evaluation, benchmarks, judges, reward-hacking, selection-bias, measurement, rsi]
---

# Measurement that survives an optimizer

You are using a number to decide whether something got better. Something else
is trying to make that number go up. **Every property that made the number
meaningful is now under pressure**, and the failure is silent: the score rises,
the capability does not, and nothing in the apparatus says so.

This skill is short on purpose. It is a **nudge away from documented default
behaviour**, not a tutorial. The numbers quoted below are produced by
[`verification/`](verification/), which builds each failure out of components
whose true answer is known by construction — so every "the score rose" claim
here is a score that rose over an ability that did not.

## The six behaviours

1. **Name what is optimizing against this number, and through which channel.**
   One line: what proposes candidates, what selects among them, and how the
   evaluator's output reaches the proposer. A human reading scores between
   runs *is* a channel. If genuinely nothing is optimizing against the
   measurement — a one-shot audit, a number nobody iterates on — most of what
   follows does not apply, and saying so is a real answer. If something is,
   the rest of this list is about that loop, not about the benchmark.

2. **Report a gain only under matched budgets.** Same attempts per item, same
   sample count, same token and wall-clock cost, **same number of evaluator
   calls**. A fixed-ability solver scored at pass@1 = 0.35 and again at
   pass@4 scores **0.82 — a 47-point "gain" with nothing changed but k**.
   That is larger than the 15-point real improvement it would be reported
   alongside. Any comparison that does not state both budgets is not a
   comparison, and "we also tried harder in round 2" is a confound, not a
   caveat.

3. **The set that steers must not be the set that reports — and count the
   looks.** Selection is not free: with every candidate at a true ability of
   0.60, reporting the best-of-N on the set used to choose it gives 0.60 at
   one look, **0.66 at five, 0.69 at twenty, 0.72 at a hundred**, while a
   held-out set returns 0.60 every time. Nothing overfit; nothing was even
   trained. So keep a **protected reference set the loop may never consult**,
   in either direction — not for steering, not for early stopping, not for
   "just checking" — and log how many times the steering set was queried.
   The look count is the exponent on this effect; an unlogged one is
   unbounded.

4. **Freeze the evaluator within an epoch. When you replace it, re-score
   everything that depended on the old one.** A run whose true ability falls
   by 15 points every round, scored by judge v1 for rounds 1–3 and a more
   lenient v2 for rounds 4–6, produces a table that **rises 8.3 points**.
   Re-scored end to end under a single judge, the same run **falls 23.9**.
   The two readings disagree in *sign*. Scores from different evaluators
   belong in different tables; a row's evaluator version is part of the
   number, and carrying an un-rescored row forward is how a regression gets
   reported as progress.

5. **Validate an evaluator change against an independent anchor — never
   against the scores it produces.** "Adopt the judge that gives higher
   scores" is **monotone in leniency**: it has no interior optimum, so it
   walks to the most permissive judge available, which scores a perfect 1.0
   and agrees with ground truth **50% of the time — a coin flip**. Anchor
   agreement has its maximum exactly at the truth. So a candidate evaluator
   is accepted on agreement with something it cannot influence — held-back
   human labels, execution outcomes, a formal check, a frozen prior judge —
   and the anchor's own budget is spent deliberately, because it is the only
   thing in the system that is not being optimized. When solver and judge
   improve together, **attribute before you celebrate**: hold one fixed and
   move the other.

6. **Report remaining headroom, and normalize before pooling.** A raw delta
   is not progress. Two benchmarks each moving +4 points differ by **7.5×**
   in what they actually closed when one sits at 92 and the other at 40 —
   half the remaining gap against a fifteenth of it. Near the ceiling a real
   improvement cannot show up at all. So state the headroom with the score,
   and when combining sources or families use the weighting in
   [`references/headroom-index.md`](references/headroom-index.md) rather
   than a mean: an unweighted mean over a pool containing a self-report runs
   **3 points high** in the worked case, and a naive mean across benchmark
   families lets a single-model family move the domain number by **9
   points**.

## What a score cannot tell you

A number that survives all six checks is *comparable*. It is still not
evidence that the thing you care about improved:

- **Construct validity stays human.** No gate here tests whether the
  benchmark measures the capability. A perfectly matched, perfectly
  held-out, perfectly anchored measurement of the wrong thing is still the
  wrong thing.
- **Anchor quality stays human.** Behaviour 5 moves trust from the judge to
  the anchor; it does not create trust. An anchor that is itself derived
  from the system under test is not an anchor.
- **Choosing what may be optimized stays human.** Which metrics are targets
  and which are protected is a decision, not a measurement.

## Before you report the number

- [ ] What is optimizing against this measurement is named, with its channel.
- [ ] Both budgets are stated; the comparison is at equal k, equal cost, and
      equal evaluator calls.
- [ ] The reporting set was never used for selection, early stopping, or
      "just checking" — and the steering set's query count is logged.
- [ ] Every row in the table was produced by the same evaluator version, or
      the table says which rows were not.
- [ ] Any evaluator change was accepted on agreement with an independent
      anchor, not on the scores it produced.
- [ ] Solver and evaluator changes are attributed separately.
- [ ] Remaining headroom is reported beside the score; pooled numbers say
      how they were weighted.

## Verification

[`verification/`](verification/) builds five measurement setups whose true
answer is known by construction and shows the default reading failing on each:
a fixed-ability solver whose score climbs 47 points on budget alone, a
best-of-N selection gap that grows with the look count while the held-out
score never moves, a declining run whose table rises 8.3 points across a judge
swap and falls 23.9 when re-scored, a judge-selection rule that walks to a coin
flip, and two identical raw deltas that differ 7.5× in real progress.
`sh verification/run.sh`, ~1 s.

## Related skills

- **`test-writing`** — the same discipline one level down: a test that can
  fail. Behaviour 3's independence rule is that skill's oracle-independence
  rule applied to an evaluator.
- **`design-of-experiments`** — when the comparison is the deliverable:
  power, blocking, pre-registration, and an estimand chosen before the data.
- **`statistics`** — inference on the scores once they are comparable.
- **`skill-evolution`** — the loop this skill measures: it prescribes paired
  evaluation and an acceptance gate; this prescribes what makes that gate's
  numbers mean anything.
- **`citation-check`** — for a reported number whose *source* is the question.
- **`docs/verifying-skills.md`** — the same argument about this repo's own
  harnesses: `bc` exits 0 on a false claim, `lean` exits 0 on a `sorry`.

## Completion report

State, briefly:

- what is optimizing against the measurement, and through which channel;
- the budgets both sides of the comparison were run at;
- which set steered, which set reported, and how many times the steering set
  was queried;
- the evaluator version behind every row, and what any replacement was
  validated against;
- the remaining headroom on each benchmark quoted;
- what the number still cannot support, and what it would take to support it.
