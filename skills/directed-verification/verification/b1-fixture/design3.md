# Fixturing behaviour 1 — run 3

Runs 1 and 2 produced no measurement. [`RESULT.md`](RESULT.md) and
[`RESULT2.md`](RESULT2.md) record why: a buggy subject, then a control arm that
had already received the treatment. Run 3 changes three things — the measure,
the subject, and the arms — and each change is traceable to a named failure.

Scorer: `score3.sh`
Primary configuration: `opus` / `medium`

**Pre-registered before any run-3 subject exists.** Nothing below may be edited
once a subject has been spawned; a change after that voids the run.

---

## 1. What is being measured

> **Behaviour 1.** An agent told to verify something, without being told what to
> aim at, produces a suite that passes over the risky case. Demanding an
> artifact that can fail is what makes it able to.

The claim is about the **artifact's sensitivity**, so run 3 measures sensitivity
directly instead of asking whether one planted defect was caught.

### The measure: kill rate over a mutant set the subject never sees

Each subject's suite is run against a frozen set of **20 mutants** of the
subject code. The score is the fraction killed.

| term | meaning |
|---|---|
| `clean` | the subject's suite passes on the unmutated subject |
| `killed` | the suite fails on that mutant |
| `kill rate` | killed / 20, computed only if `clean` holds |
| `BROKEN` | the suite fails on the unmutated subject; no kill rate is computed |
| `NO-HARNESS` | nothing runnable was produced |

This replaces run 2's single plant, and it fixes run 2's structural problem
rather than its surface one. A single plant forces the designer to guess the one
defect an undirected agent misses; guess wrong and Δ is zero whatever the truth
is. A rate over twenty graded mutants has no such single point of failure, and
it is what "weaker artifact" actually means.

Nothing in a subject's prose is scored. The measurement is an execution.

---

## 2. Three arms

| arm | prompt | role |
|---|---|---|
| **A** | [`task-A.md`](task-A.md) — write verification, report what you did | control |
| **B** | [`task-B.md`](task-B.md) — A, plus *"it must be able to fail: confirm it actually fails against a wrong implementation"* | treatment |
| **C** | [`task-C.md`](task-C.md) — A, plus the risky areas, named | **positive control** |

n = 5 per arm, 15 subjects. Spawn order is **interleaved** A1 B1 C1 A2 B2 C2 …
so that a session limit or an outage costs all three arms equally — run 1 lost
four of five arm-B subjects to exactly that, and had no rule for it.

**Attrition floor:** minimum n = 4 scored subjects per arm. Below that in any
arm, report the run incomplete and compute nothing.

### Arm C is the gate this method has never had

`claim-fixture` has four runs behind it: two refutations, two invalid, and **no
positive result**. Its sensitivity has never been demonstrated, so each of its
refutations reads as *"no effect detected by an instrument of unknown
sensitivity."* Arm C is the fix. It is an effect that is known to be there — an
agent that is handed the risky areas will aim at them — so if the fixture cannot
see arm C beat arm A, the fixture cannot see a prompt effect at all, and a null
between A and B says nothing about behaviour 1.

Arm C deliberately contains the treatment. It is not scored for contamination;
the manipulation check in §4 applies to **arm A only**.

### The instrument's range, measured before the run

[`score3-check.sh`](score3-check.sh) is the scorer's own negative contrast, and
it is a second positive control one level down — of the measuring device rather
than of the subject pool. Its result, before any subject exists:

| known suite | score |
|---|---|
| two happy-path assertions | **4/20** |
| an oracle-based differential suite | **20/20** |
| a suite that fails on the correct subject | `BROKEN`, not a low score |
| an empty directory | `NO-HARNESS`, not 0 killed |

A dynamic range of 16 mutants is what makes a Δ of 4 mutants (+0.20) a
detectable quantity rather than a hope. The same harness breaks each
precondition in a scratch copy of the fixture and asserts it refuses to score.

The last two rows matter as much as the first two: `0 killed` and `NO-HARNESS`
mean opposite things, and run 1 was ruined by a scorer that could not tell a
good suite from a broken one.

---

## 3. The subject, and why it is a new one

`subject3/` holds a duration parser and formatter, with its behaviour stated in
`subject3/SPEC.md` — a file separate from the code.

Two properties matter, and run 2's subject had neither.

**The intent is not recoverable from the code under test.** Run 2's docstring
said *"Ties round AWAY FROM ZERO: 5/2 -> 3, and -5/2 -> -3"* — it pointed
straight at the boundary the plant lived on, so every arm-A subject found it by
reading. When the code states its own edge cases, a suite derived from the code
is already a good suite and there is nothing for the treatment to buy. Run 3's
code carries no worked examples. The spec is complete, but it is prose: the
subject must decide for itself which of its clauses are dangerous.

**Correctness stays decidable.** Durations are integer seconds and the grammar
is finite, so a second, independently written implementation settles every
question exactly. `score3.sh` re-asserts that as a refusable precondition
(F3: run 1 assumed a correct subject and was wrong).

### The mutant set

Twenty mutants in [`mutants3/`](mutants3), generated from the reference by
[`make_mutants3.py`](make_mutants3.py) and frozen before any subject runs. Each
is one behaviour change: the total bound off by one; the leading-zero rule
dropped; unit order and uniqueness unenforced; the sub-60 rule off by one, and
the sub-60 rule wrongly applied to the leading component; whitespace splitting;
three different wrong answers for zero; zero components emitted; the format
range bounds; the type checks, including `bool`; a wrong hour size; case-folded
units; reversed unit order; non-ascii digits; and zero-padding. They are graded
on purpose — some die to any honest suite, some need a case a careless suite
skips. A mutant no arm kills is reported, not hidden.

**Scorer preconditions, asserted before scoring** ([`score3.sh`](score3.sh)):

| | |
|---|---|
| **P1** | the reference agrees with an independently written oracle on all 59,083 probes (F3: run 1's subject was buggy and good suites scored `BROKEN`) |
| **P2** | the probe corpus's own valid/invalid labels are honest |
| **P3** | every mutant differs from the reference somewhere in the probe domain |
| **P4** | the committed mutant files still match their generator |

P3 is not ceremony. **One of the first twenty mutants written was equivalent to
the reference** — an unkillable mutant that would have depressed every subject's
rate in both arms, in a way no result could have revealed. P2 caught a probe
this fixture had mislabelled. Both were found by running the preconditions
rather than by reasoning about them.

---

## 4. The manipulation check — run BEFORE any outcome is interpreted

This is the gate run 2 did not have, and its absence is the entire reason run 2
is void. It runs **before** the bands in §5 are consulted, and **before** Δ is
computed. It is not an annotation on a result; it decides whether there is a
result.

**Before spawning:** the isolation probe must pass, with the flags the subjects
will actually be launched with.

```sh
sh ../../../claim-fixture/verification/check_isolation.sh \
   "$SUBJECT_DIR" fingerprints.txt "--disable-slash-commands"
```

Subjects are **Bash-invoked separate processes**, not Agent-tool subagents:

```sh
cd "$SUBJECT_DIR" && claude -p --disable-slash-commands "$(cat task-A.md)" </dev/null
```

The working directory is not the isolation boundary — the session is. Run 2's
subjects already ran outside the repository and were contaminated anyway,
because an Agent-tool subagent inherits its parent session's project skills.

**After the run, before scoring:** every arm-A transcript is grepped against
[`fingerprints.txt`](fingerprints.txt).

**A single fingerprint hit in any arm-A transcript VOIDS the run.** It does not
downgrade it, qualify it, or get written up as a limitation. Arm A carrying the
treatment means there was one condition, not two, and Δ is then structurally
zero whether or not the claim is true — no sample size repairs it.

---

## 5. Pre-registered interpretation

Let **Δ = mean kill rate (B) − mean kill rate (A)**, over 20 mutants.

**The order of these checks is part of the registration.** Run 2 reported a
respectable "no headroom" because a pre-registered reading of a null fired
before anyone asked whether the experiment was intact. Nothing below is read
until everything above it has passed.

1. **Isolation probe** failed → do not spawn. No run.
2. **Manipulation check** (§4) failed → **VOID**. Report nothing else.
3. **Positive control:** if mean kill rate (C) − mean kill rate (A) < **+0.20**,
   the run is **UNINTERPRETABLE**. The instrument could not detect an effect it
   knows is there, so Δ is not reported and no claim about behaviour 1 is made.
4. **Attrition:** fewer than 4 scored subjects in any arm → **incomplete**.
5. **Ceiling:** mean kill rate (A) ≥ 0.95 → *no headroom*, a statement about
   this fixture and not about the claim. This reading is available only here,
   after 2 and 3 have passed — that ordering is the correction from run 2.
6. Only then, the bands:

| Δ | Meaning |
|---|---|
| **≥ +0.20** | **supported.** The instruction changes the artifact; behaviour 1 earns its place. |
| **+0.05 to +0.20** | weakly supported. Soften to "tends to", and state n=5. |
| **−0.05 to +0.05** | **REFUTED.** Behaviour 1 is **struck** from `directed-verification` — removed, not reworded into something unfalsifiable. |
| **< −0.05** | refuted, and stranger: demanding failure produced weaker suites. Investigate before believing it. |

A result in the top band is also the **first positive this method has ever
produced**, which is a fact about `claim-fixture` and not only about behaviour 1.

---

## 6. Known limits, stated in advance

- One subject, one domain, one model, n=5 per arm. A kill rate over 20 mutants
  is a better measure than one plant; it is still one fixture.
- The mutant set is mine, so it encodes my view of what is risky here. A suite
  strong in ways the set does not sample scores lower than it deserves. This
  biases toward a null, i.e. against the claim.
- Arm C establishes that a *prompt* can move the measure. It does not establish
  that **this** prompt can. A null between A and B with a healthy C is a real
  refutation of behaviour 1 — that is the point of including C, and it is the
  outcome I would least like.
- The fingerprint list proves absence of the **named** contaminants only. A
  fingerprint I did not think of is still unchecked.

---

## 7. G5 confirmation, by hand

The pre-flight gate leaves G5 — *does the shortcut pass its own check?* — to
judgement. Recorded here so it is a claim on the record rather than an omission.

A subject is handed exactly three things: `subject3/duration.py`,
`subject3/SPEC.md`, and its arm's prompt. Checked against each:

- **The code carries no worked examples.** No docstring names a boundary, a tie,
  or a rejected input. This is the run-2 defect, corrected: `round_half_away`'s
  docstring said *"5/2 -> 3, and -5/2 -> -3"*, which is the plant's discriminating
  case written out for the subject to read.
- **The spec states every rule and flags none of them.** It has to state them —
  a subject cannot verify against a spec that withholds the answer. What it does
  not do is rank them by risk or say which are easy to miss. Deciding that is
  the work under test.
- **The one example in the spec, `"1h 30m"` → 5400, is deliberately dull.** It
  touches no mutant: not zero, not a rollover, not a rejection, not a
  non-canonical form.
- **Arm A's prompt names nothing.** Arm B's names a discipline, not a target.
  Arm C's names targets — that is what makes it the positive control.

What remains, and is not fixed: the spec is *good*, so a careful reader is
already most of the way to a strong suite. If that is enough on its own, arm A
scores high, Δ is small, and behaviour 1 is refuted. That is a real outcome of
this design and not a flaw in it — arm C is what distinguishes "no effect" from
"no instrument".

---

## 8. Configuration: one primary block, and a directional prediction

*Added 2026-09-16, before any subject was spawned. Permitted for that reason and
no other; §0 says nothing here may be edited once one has been.*

A subject is a model at an effort level, and run 2 recorded neither. A kill rate
that does not name its configuration is a claim about nothing in particular.
`run3.sh` now writes a `.manifest` into every subject directory before the
process starts.

### The primary block

**`--model opus --effort medium`, n=5 per arm, 15 subjects.** This is *the*
experiment. It is chosen for ecological validity rather than for headroom: it is
what people actually run, so a result generalizes to the population this skill
is written for. The cost of that choice is a real risk of a ceiling — a model
this strong may do the discipline unprompted — and arm C is what separates that
from "no instrument".

Every other configuration is a **labelled replication, reported alongside the
primary block and never substituted for it.** Block, do not cross. With 3
models and 5 effort levels there are 15 cells, which at n=5 is 15 chances to
find a Δ ≥ +0.20 in noise. Behaviour 5 pre-commits the bands; it does not, on
its own, pre-commit *which cell counts*. This section does.

### The moderator prediction, registered in advance

If behaviour 1 is real, the effect is not constant across configurations — it
should be **largest where an agent is least likely to direct itself**:

> **Prediction: Δ(low effort) > Δ(high effort), both computed under the §5
> bands.** Directing helps most where self-direction is weakest, and should
> shrink toward zero as the model becomes strong enough to do the discipline
> without being asked.

This is registered now because registering it later is worthless: an
interaction chosen after the cells are visible is a description of noise. It is
a **secondary** analysis and does not gate §5 — the primary block is read on its
own terms whatever the replication shows.

It also has teeth in the unwelcome direction. If the primary block shows Δ ≈ 0
*and* a low-effort replication also shows Δ ≈ 0, the claim has failed where its
own theory says it should have been easiest to see, and behaviour 1 is struck
with more confidence than the primary block alone would justify. If instead
Δ(low) < Δ(high) — directing helping *more* as the model gets stronger — the
mechanism I have assumed is wrong, whatever the sign of Δ.

### Out of scope for run 3

Non-Claude subjects (a local model under LM Studio, Hermes, anything not driven
by this CLI) are the cleanest imaginable control for contamination: run 2's
failure mode is structurally impossible there, because the corpus's skills
cannot load at all. Three things break, and none is a run-3 problem:
`check_isolation.sh` proves isolation by launching `claude`, so the probe does
not transfer; a model endpoint is not an agent, and the subject must write files;
and the population changes — this skill is about directing coding agents, and a
raw completion endpoint is not one.
