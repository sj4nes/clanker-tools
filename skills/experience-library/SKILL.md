---
name: experience-library
description: >-
  Govern a growing store of retained artifacts — agent memories, distilled
  rules, skill or playbook libraries, reusable prompts, learned tool
  definitions, runbook entries, "lessons learned" notes — so that adding to
  it keeps making the system better instead of quietly making it worse. Use
  when an agent or team accumulates reusable knowledge across tasks or
  sessions; when deciding whether a distilled lesson is worth keeping; when
  a memory store, skill library, or rules file has grown and results have
  stalled; or when asked to design, audit, or prune such a store. Six
  behaviours that displace the known default failure modes: admitting an
  artifact because it reads well, appending without a cap, retiring by age
  or vibes, reading one end-to-end task score as a diagnosis, and treating
  an artifact that helped its author as one that will help a different
  executor. NOT a vector-database or retrieval-tuning guide, and not a
  method for writing the artifacts themselves.
version: 1.0.0
author: Simon Janes
tags: [memory, skill-library, agents, retention, distillation, retrieval, rsi]
---

# Governing a store that grows

Every retained artifact is admitted because it helped once. The store grows,
each addition is locally justified, and the system gets worse — because an
entry that is useful in isolation still **costs every other entry some
retrieval probability**, and nothing in the usual workflow ever charges it
for that.

This skill is short on purpose. It is a **nudge away from documented default
behaviour**, not a tutorial. Every number below comes from
[`verification/`](verification/), where the library's true value is a
parameter of the fixture.

## The six behaviours

1. **Name the artifact's form, and promote only on evidence.** There is a
   ladder — **text note → structured record → procedure → executable tool** —
   and each rung costs more to maintain and pays more when retrieved. Write
   at the cheapest rung that captures the lesson, and promote a rung only
   when the entry has actually **recurred across tasks** and the higher form
   **passes its own gate**: a procedure must be followable as written, and a
   tool is admitted only after it compiles and runs in a sandbox. Promoting
   on enthusiasm produces a library of executable artifacts nobody invokes.
   The forms and their gates are in
   [`references/distillation-ladder.md`](references/distillation-ladder.md).

2. **Admit on a paired run over the same tasks — never on inspection.**
   Run the task set twice: **control = the current library, treatment =
   library + candidate**, same tasks, same order, same budget. Admit only if
   the paired difference supports a hypothesis you wrote down *before* the
   run, then confirm on tasks that were not used to propose it. Inspection
   cannot do this job: in the fixture a candidate with **zero true effect**
   that merely reads well is admitted **82.8%** of the time, against
   **83.3%** for a genuinely useful one — *the default gate cannot tell them
   apart at all*. The paired gate admits the useless candidate **2.7%** of
   the time and the real one **93.8%**. And the pairing is not a detail: at
   an identical task budget, an **unpaired** comparison detects the same real
   effect only **19.7%** of the time at the same false-admit rate, because
   per-task difficulty no longer cancels. It needs **10× the tasks** to match.

3. **Cap the library. A new entry displaces an existing one; it does not
   append.** Growth is not subject to diminishing returns — it goes
   *negative*. In the fixture a 200-entry library scores **0.137**, below a
   10-entry library's **0.166**, despite covering five times as many tasks;
   the optimum sits at **55 entries and 0.390**. So the cap is the mechanism,
   and admission becomes a competition against the weakest entry already
   present rather than against zero. **The stall is invisible while it
   happens**: at 100 entries the score is **0.328** — still well above the
   10-entry library, still rising against last quarter — and the store is
   already past its peak. "Results are still improving" is not evidence the
   library is healthy.

4. **Retire on measured contribution from an append-only log — and do not
   over-retire.** Each entry carries a running record of the tasks it was
   retrieved for and what happened; retirement is what that record says, not
   age, not authorship, not tidiness. **Retire too hard and you do worse than
   having no policy at all**: governed **0.390** > ungoverned **0.133** >
   aggressive **0.092** in the fixture. The governance curve is a **U, not a
   slope**, so "prune more" is not the safe direction to err in, and a
   retirement rule needs a defended cap rather than a reflex. Retire to an
   archive with the reason recorded; a retired entry that keeps being
   re-derived is evidence the cap is wrong.

5. **Measure retention, activation, and execution separately.** An artifact
   helps only if it is **kept**, then **retrieved**, then **followed** —
   three independent failures that produce **identical end-to-end scores**.
   In the fixture, three libraries all realise **0.300**: one keeps too
   little, one keeps everything but retrieves it 30% of the time, one
   retrieves everything and is followed 30% of the time. The usual repair —
   "improve the library", meaning write and keep more — takes the first from
   0.300 to **1.000** and moves the second **not at all**. One task score
   cannot tell you which one you have, so instrument all three or you will
   be guessing at which lever to pull.

6. **Record applicability conditions and provenance; cross-executor reuse is
   a separate claim.** Every entry carries what produced it, the conditions
   under which its evidence holds, and what it depends on — so a later reader
   can tell whether it still applies after the tasks, tools, or model
   changed. **An artifact validated for one executor is not validated for
   another**: a skill useful to its author may be unsuitable for a different
   model, a different agent harness, or a human. Re-run the behaviour-2 gate
   under the new executor before inheriting it, and record the answer rather
   than assuming transfer.

## What the gates do not cover

- **Whether the lesson is true.** The admission gate measures whether an
  artifact *helps on your task set*. A wrong generalization that happens to
  help on those tasks passes cleanly.
- **What the task set should contain.** Every number here is relative to it.
  A library governed perfectly against an unrepresentative task set is
  governed toward the wrong shape.
- **Where the cap belongs.** The fixture has a computable optimum because
  coverage and retrieval decay are parameters. Yours are not; the cap is a
  calibrated judgement, revisited as retrieval improves.
- **Whether an entry should exist at all.** Some lessons belong in the code,
  the schema, or the tool — not in a store that has to be retrieved and
  followed at the right moment. The best entry is often the one deleted by
  fixing the thing it works around.

## Before you add to the store

- [ ] The artifact is written at the cheapest rung that holds the lesson.
- [ ] A hypothesis was written before the run, and the run was **paired** —
      same tasks, control vs library+candidate — then confirmed on tasks not
      used to propose it.
- [ ] The library has a **cap**, and this entry displaced a named weaker one.
- [ ] The entry opens an append-only contribution record.
- [ ] Retention, activation, and execution are instrumented separately.
- [ ] Applicability conditions, provenance, and dependencies are recorded.
- [ ] If this entry came from elsewhere, it was re-gated under **this**
      executor.

## Verification

[`verification/`](verification/) builds library dynamics whose true value is
a parameter of the fixture: a coverage/retrieval curve with an interior
optimum at 55 entries (found by scan **and** by the analytic crossover, then
drawn independently in Monte Carlo), the three retention policies, an
admission gate on a useless-but-appealing candidate, and paired vs unpaired
power at an identical budget. `sh verification/run.sh`, ~3 s.

## Related skills

- **`evaluator-integrity`** — the measurement side of behaviour 2: matched
  budgets, a protected reporting set, and what makes the admission gate's
  numbers mean anything in the first place.
- **`skill-evolution`** — improving **one** instruction document against an
  evaluator. This skill governs the **library** those documents live in;
  the two compose, and its issue tracker is the per-document analogue of
  behaviour 4's contribution log.
- **`design-of-experiments`** — when the admission gate deserves a real
  design: blocking, power, and pre-registration for behaviour 2.
- **`test-writing`** — behaviour 1's promotion gate for an executable
  artifact is a test that has to be able to fail.
- **`temporal-data-modeling`** — for the contribution log as an
  interval-indexed record rather than a mutable field.
- **`agent-automation`** — when the entries drive real side effects, not
  just advice.

## Completion report

State, briefly:

- what the store holds, at which rung, and how large it is against its cap;
- for each admitted entry: the hypothesis, the paired result, and the
  independent confirmation;
- what was displaced, and on what measured contribution;
- the retention / activation / execution numbers, separately;
- which entries have not been re-gated under the current executor;
- what you did **not** verify, and what it would take to.
