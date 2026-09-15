# `experience-library` skill — verification run

`experience-library` is a *nudge away from known library-governance failure
modes*, not a tutorial. So verification cannot mean "re-solve a case with a
closed form". It means the thing the skill is actually claiming:

> **build a library whose true value is a parameter of the fixture, run the
> default governance over it, and confirm the default makes the system worse
> while reporting that it is getting better.**

**Fixture-first.** This directory was built before `SKILL.md`, so the prose
quotes the harness rather than the harness illustrating the prose.

## Run

```
sh skills/experience-library/verification/run.sh
```

Tooling: `bc` 7.x (`-lq`), Python 3 (stdlib only), macOS `/bin/sh`. ~3 s wall.
Monte Carlo: 60 000 draws (drift curve), 30 000 (policy comparison), 600
trials × 100 tasks (admission and power). Every RNG stream is seeded from an
argument; re-running reproduces the numbers below exactly.

## Model / case, and why this one

The whole harness rests on one model, stated once so it can be argued with:

```
coverage(n)  = 1 - (1-c)^n        each entry is relevant to a fraction c of tasks
retrieval(n) = (1-q)^(n-1)        each other entry outranks the right one w.p. q
benefit(n)   = coverage(n) * retrieval(n)
```

with `c = 0.02`, `q = 0.01`. This is the **Library Drift mechanism in closed
form**: an entry useful in isolation still costs every *other* entry some
retrieval probability, so the library has an interior optimum that unbounded
growth walks straight past.

It was chosen because it makes "is the library healthy?" answerable
independently of any score — and because the two effects are **separately
falsifiable**: setting `q = 0` removes the decay and the interior optimum
must disappear, which is one of the planted defects below.

| Section | Setup | True answer, by construction |
|---|---|---|
| bc §1–3 / sim §1–2 | the curve above, swept over n | optimum at **n = 55**; 200 entries **worse** than 10 |
| sim §3 | candidates with true effect 0.00 and 0.05, both "reading well" | one is worthless, one is real |
| bc §4 / sim §4 | task difficulty sd 0.30 shared, noise sd 0.10 independent | pairing cancels difficulty; ratio is exactly 10 |
| bc §5 | three libraries at (0.3, 1, 1), (1, 0.3, 1), (1, 1, 0.3) | identical product, three different faults |

## What each step demonstrates

| `SKILL.md` step | Prescribed check | Result |
|---|---|---|
| b2 paired admission | run the same tasks twice, control vs +candidate | inspection admits the **zero-effect** candidate **0.828** and the real one **0.833** — *indistinguishable*. The paired gate: **0.027** and **0.938**. |
| b2 why paired | pair, don't just compare | at an identical budget, paired detects **0.938**, unpaired **0.197**, both at a **0.030** false-admit rate. `bc` §4: variance ratio exactly **10×**, detectable effect **√10 = 3.162×** smaller, so unpaired needs **10× the tasks**. |
| b3 cap the library | a new entry displaces rather than appends | n=200 benefit **0.1330** < n=10 benefit **0.1671**, despite **5×** the coverage (0.982 vs 0.183). Optimum **n=55, 0.3899**, found by scan *and* by the analytic crossover at n = 54.05. Capped:unbounded = **2.93×**. |
| b3 the stall is invisible | don't read a rising score as health | at n=100 benefit is **0.3207** — still above n=10, still "improving" — and already past the peak. |
| b4 don't over-retire | cap on measured contribution, defended | governed **0.3899** > ungoverned **0.1330** > aggressive **0.0923**. The curve is a **U**: over-retirement is *worse than no policy*. |
| b5 three factors | instrument retention, activation, execution separately | three libraries realise an identical **0.300**. Raising retention to 1.0 takes the first to **1.000** and the second to **0.300** — no change. |

The Monte Carlo drift curve is an **independent oracle** for `checks.bc` §1:
it draws relevance per entry and resolves retrieval as an actual contest
against distractors, never evaluating `(1-c)^n` or `(1-q)^(n-1)`. Agreement
is within 0.008 at every n tested. The optimum in `bc` is likewise found two
independent ways — a scan over n = 1..300, and the analytic crossover
`f(n+1)/f(n) = 1` — which is what caught the error below.

## Negative-contrast testing

Run end to end, and **each `bc` signal in isolation**:

| Planted defect | Signal that should catch it | `run.sh` exit |
|---|---|---|
| argmax asserted as 42 instead of 55 | all three | **1** ✓ |
| `*** FAIL` marker only, `fails` untouched — banner printed, `bc` exits **0** | `grep -qF '*** FAIL'` **alone** | **1** ✓ |
| syntax error mid-file (`bc` status 2) | exit-status clause | **1** ✓ |
| banner condition falsified, nothing else | missing-banner clause | **1** ✓ |
| pairing removed — difficulty no longer shared between arms | python assertions | **1** ✓ (2 FAIL lines) |
| `q = 0` — retrieval decay removed, so no interior optimum exists | python assertions | **1** ✓ (4 FAIL lines) |

The last two are the ones worth having: they falsify the **premises** of the
model rather than its arithmetic. If pairing did not cancel difficulty, or if
a library's entries did not compete for retrieval, behaviours 2 and 3 would
be advice.

## Findings folded back into the skill

- **The backstop caught a real error in the first draft.** `checks.bc` §1
  hard-coded the optimum at **n = 54**; the true integer argmax is **55**
  (the crossover sits at 54.05). `bc` printed `*** FAIL: n=54 should beat
  n=55` and exited 1 via the `1/0` backstop. The section was rewritten to
  **find** the optimum by scan and cross-check it against the analytic
  crossover, rather than asserting a remembered constant — which is both
  correct and states the claim the section is actually making (*a maximum
  exists, and it is interior*) instead of one that silently rots if `c` or
  `q` is retuned. Every "55" in `SKILL.md` postdates this.
- **The policy section originally cheated.** `run_policy` computed the final
  benefit by calling `closed_form(size)`, so §2 was only testing the
  policy → size mapping and re-reading `bc`'s answer. It now **draws** the
  benefit on the library each policy actually produced.
- No correctness fix was needed in the skill body, which is a consequence of
  building fixture-first rather than evidence the prose is right. The
  displacement table below is where that is tested.

## The gates are necessary, not sufficient

- **Whether the lesson is true.** The gate measures whether an artifact helps
  on *your task set*. A wrong generalization that helps on those tasks passes.
- **What the task set contains.** Every number here is relative to it.
- **Where the cap belongs.** The fixture has a computable optimum because `c`
  and `q` are parameters. Yours are not.
- **Whether an entry should exist at all.** Often the right move is fixing
  the thing the entry works around.

## Displacement table

Per `docs/verifying-skills.md` §7.

| `SKILL.md` section | Default behaviour it displaces | Where the default visibly fails |
|---|---|---|
| b1 rung + promotion gate | write every lesson at the richest form available; promote on enthusiasm | `judgement` — no fixture supplies whether a lesson *warranted* its rung |
| b2 paired admission | admit the artifact because it reads well | sim §3: inspection admits 0.828 (null) vs 0.833 (real) — no discrimination |
| b2 pairing specifically | compare the treatment run to a historical average | sim §4: 0.938 paired vs 0.197 unpaired at equal budget; bc §4: 10× variance |
| b3 cap + displacement | append; the store only grows | bc §1–2 / sim §1: n=200 (0.137) below n=10 (0.166) |
| b4 contribution log, don't over-retire | retire by age, authorship, or tidiness — or prune hard to be safe | bc §3 / sim §2: aggressive 0.092 **below** ungoverned 0.133 |
| b5 three factors | read one end-to-end task score as a diagnosis | bc §5: three libraries, identical 0.300, three repairs |
| b6 applicability + cross-executor | assume an artifact that helped its author helps anyone | `judgement` |
| whether the lesson is true | treat "it helped" as "it is correct" | `judgement` |
| where the cap belongs | adopt a round number | `judgement` |

**5 covered · 4 judgement · 4 gaps.**

### Gaps — logged in [`BACKLOG.md`](../../../BACKLOG.md)

1. **Cross-executor transfer** (b6). The skill says an artifact validated for
   one executor must be re-gated for another. Nothing plants an entry that
   helps executor A and *hurts* executor B, which is the claim.
2. **The promotion gate** (b1). "A tool is admitted only after it compiles
   and runs" has no fixture — no executable artifact is built, gated, or
   seen failing its gate. The recurrence criterion is likewise unmodelled.
3. **Activation and execution as interventions** (b5). `bc` §5 shows the
   three factors *multiply* and that one score cannot separate them. It does
   not show a realistic retrieval or instruction-following failure producing
   those factors — the numbers are supplied, not generated.
4. **Staged admission** (b2, `references/distillation-ladder.md` §2). HDSO
   runs the comparison in **stages of increasing size**; the harness runs one
   fixed-n comparison. Sequential stages have their own multiplicity problem,
   unmodelled here, and `evaluator-integrity`'s look-count result suggests it
   is not small.

A green harness with four gaps is the honest state. The first three are
concrete enough to write as harness sections; the fourth needs a sequential
design this fixture does not have.
