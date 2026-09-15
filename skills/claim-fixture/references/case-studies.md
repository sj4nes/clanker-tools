# Two case studies, both refutations

Both ran on 2026-09-15 against `role-deck`, a skill whose author (me) had
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

**Fixture (behaviour 5).** A real bug from the repo's own history: a harness
whose `grep -q '*** FAIL'` guard is dead because the leading `*` is an invalid
repetition operator, so grep exits 2 and shell `if` reads that as false.
Reading the source yields a confident wrong answer — `set -e`, the pipe, stderr
capture. Running it prints `repetition-operator operand invalid`.

**Measurement (behaviour 3).** That stderr string occurs **zero times in the
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

**Fixture (behaviour 5).** A build gate with two real causes: an anchored
`grep -q '^FAIL'` against indented report lines, which **fully explains the
presented symptom**, and a stdout-only capture while the suite reports parse
failures on stderr. Fix the anchor alone and the presented bug is caught —
**the confirmation succeeds** — while a stderr-reported failure still passes.

**Tightened before running (behaviour 6's cousin).** The first build put both
failures in the visible output, which would have made a null result
uninterpretable: *"they discriminate"* and *"the clue was handed to them"* were
indistinguishable. The second cause moved out of the output and into the code.
Changed before any trial; recorded as such.

**Measurement (behaviour 3).** Subjects applied their fix; the scorer
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

**The discipline that made the negative results usable** was behaviour 6:
striking rather than rewording. The reflex on the first refutation was to
substitute *"well, but agents don't enumerate alternatives"* — which is how a
methodology survives forever on a rotating cast of untested premises. Turning
that into case study 2 killed it too.

**The lapse worth copying from, in the bad sense.** Case study 1's scorer was
written before its results and committed *alongside* them. It really was
pre-registered; the record cannot show it. `verification/` fails on it
permanently for that reason.
