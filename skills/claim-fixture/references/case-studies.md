# Four runs: two refutations, two invalid

Case studies 1 and 2 are refutations and are written up in full below. Case
studies 3 and 4 are the **invalid** runs, summarised at the end — they are the
reason behaviour 3 and [`pre-flight.md`](pre-flight.md) exist, and they belong
in the record precisely because a method's failures are what calibrate trust in
its successes.

Cases 1 and 2 ran on 2026-09-15 against `role-deck`, a skill whose author (me) had
spent a day building it and was invested in the claims being true. Both came
back negative. The full records are in
[`../../role-deck/verification/premise-fixture/`](../../role-deck/verification/premise-fixture/)
and [`../../role-deck/verification/ordering-fixture/`](../../role-deck/verification/ordering-fixture/).

---

## 1. "An agent will skip the expensive hat"

The founding claim of `role-deck`: an agent left to sequence its own work will
skip the costly step, so the sequence must be imposed externally.

**Split (behaviour 1).** Two halves. *Does a deck make skipping impossible?* —
already proven by an exhaustive gate over the reachable state space, so it left
the experiment. *Would an unconstrained agent skip?* — behavioural, and the only
thing to measure. One arm, not two.

**Fixture (behaviour 6).** A real bug from the repo's own history: a harness
whose `grep -q '*** FAIL'` guard is dead because the leading `*` is an invalid
repetition operator, so grep exits 2 and shell `if` reads that as false.
Reading the source yields a confident wrong answer — `set -e`, the pipe, stderr
capture. Running it prints `repetition-operator operand invalid`.

**Measurement (behaviour 4).** That stderr string occurs **zero times in the
source**. Naming it, or prescribing the fixed-string fix it implies, is an
artefact of execution that cannot be reached from the material handed over.

**Result.** 8 fresh agents, no deck, no prompt to run anything. **8/8 executed.
0/8 read-only.** Pre-registered band: *premise refuted — strike the founding
justification.*

**Bycatch.** Subjects who ran both greps found the repo's own documentation
attributed the error message to the wrong binary.

---

## 2. "An agent confirms rather than discriminates"

The successor claim, sharpened by the user from a vague "do they enumerate
alternatives" — unmeasurable, because considering an alternative is
self-report — into something testable:

> Having formed a plausible explanation, does an agent ask *"how do I confirm
> this?"* rather than *"what else would produce this symptom?"*

**Fixture (behaviour 6).** A build gate with two real causes: an anchored
`grep -q '^FAIL'` against indented report lines, which **fully explains the
presented symptom**, and a stdout-only capture while the suite reports parse
failures on stderr. Fix the anchor alone and the presented bug is caught —
**the confirmation succeeds** — while a stderr-reported failure still passes.

**Tightened before running (behaviour 7's cousin).** The first build put both
failures in the visible output, which would have made a null result
uninterpretable: *"they discriminate"* and *"the clue was handed to them"* were
indistinguishable. The second cause moved out of the output and into the code.
Changed before any trial; recorded as such.

**Measurement (behaviour 4).** Subjects applied their fix; the scorer
**executes it** against a stderr-only failure that was not in the fixture they
were given. Reasoning is not scored.

**Result.** **8/8 COMPLETE. 0/8 CONFIRMATORY.** Every subject built the
stderr-only test case themselves and also tested the all-pass case unprompted.
**4/8 closed a third hole that was never planted.**

---

## What the two together cost and bought

16 agents, about four minutes of wall time, two afternoons of fixture design.
They removed both behavioural justifications from a skill built over a full day
and left it honestly scoped to what its structural gates prove.

**The discipline that made the negative results usable** was behaviour 7:
striking rather than rewording. The reflex on the first refutation was to
substitute *"well, but agents don't enumerate alternatives"* — which is how a
methodology survives forever on a rotating cast of untested premises. Turning
that into case study 2 killed it too.

**The lapse worth copying from, in the bad sense.** Case study 1's scorer was
written before its results and committed *alongside* them. It really was
pre-registered; the record cannot show it. `verification/` fails on it
permanently for that reason.


---

## Case studies 3 and 4 — the invalid runs

Both are attempts to fixture `directed-verification` behaviour 1: *an agent
asked to "verify this" produces a weaker artifact than one asked to "make this
able to fail"*. Records in
[`../../directed-verification/verification/b1-fixture/`](../../directed-verification/verification/b1-fixture/).
The claim remains **unmeasured**.

### 3 — the subject was buggy (run 1)

The subject function used `int()`, which truncates toward zero, so it was wrong
on negative ties. A harness good enough to test negative ties therefore failed
on the *clean* implementation and scored `BROKEN`. **The measurement inverted
quality**: the better the subject's work, the worse it scored. Four of five
arm-B agents also died on a session limit, leaving n=1.

Gates now derived from it: **G3** (verify the subject by independent oracle; the
scorer re-asserts it as a precondition) and **G6** (interleave the arms so
truncation costs both equally).

### 4 — the control arm received the treatment (run 2)

Every run-1 fix held. The subject was verified over 28,824 cases; the plant
differed from correct code only at negative ties; arms were interleaved; n=5 per
arm, both complete. Both arms scored 5/5 and Δ = 0.

It was reported first as *no headroom* under a pre-registered ceiling rule, and
that was wrong. Every arm-A subject had **`test-writing` in context** — a skill
that prescribes the discipline under test — and their transcripts quote it
verbatim. The arms were one condition. Δ = 0 was structural and no sample size
would have changed it.

Two lessons, and the second is the sharper one:

- **Naive about the hypothesis ≠ clean of the intervention.** Behaviour 2 was
  satisfied; the run was still ruined. A corpus of installed skills contaminates
  any fixture asking whether its own behaviours need teaching, and skills load
  from the session rather than the working directory — changing directory is not
  isolation. Hence **G1** and **G2a**.
- **A pre-registered reading of a null result can conceal a broken experiment.**
  The ceiling rule was a good-faith guard against over-claiming, and it worked
  too well: it supplied a respectable account of Δ = 0 and stopped the author
  looking for the cause. Hence **G2b** — the manipulation check is scored
  *before* the bands are consulted, and a failure voids rather than annotates.

The tell was visible and missed: five arm-A reports shared a near-identical
"Risky area and targeted mistake" heading. Five independent agents do not
converge on a section heading. It was a prompt echo, and one `grep` would have
caught it.

## What four runs say about the method

Two refutations, two invalid, **zero positives**. The method has never been
shown to detect an effect it knew was present, so its sensitivity is untested —
which makes its two refutations weaker evidence than they appear. G4 demands a
positive control of every fixture; `claim-fixture` still owes one of itself.
