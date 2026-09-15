# Scoring — by executing the subject's own fix

The claim under test is about **confirmatory versus discriminating testing**:
having formed a plausible explanation, does the subject ask *"how do I confirm
this?"* — or *"what else would produce this symptom?"*

Reasoning is not scored. The subject's prescribed change is **applied to a
clean copy and executed** against two inputs.

| | Presented case (a stdout `FAIL`) | Stderr-only case |
|---|---|---|
| **COMPLETE** | exit 1 | **exit 1** |
| **CONFIRMATORY** | exit 1 | **exit 0** — bug survives |
| **BROKEN** | exit 0 | — |

## Why this is unforgeable

The subject cannot pass by describing good practice. Either their edit makes
the gate catch a stderr-reported failure or it does not, and that is decided by
running it, not by reading them.

## The two causes

Both are real, both are visible, and both are load-bearing:

1. `grep -q '^FAIL'` is anchored, while the suite indents its report lines.
   This is the **visible, plausible** cause — it explains the presented symptom
   completely, and fixing it alone makes the presented symptom go away.
2. `out=$(sh suite.sh)` captures stdout only. The suite reports a raising
   test's failure on **stderr**, so that failure never reaches the grep no
   matter how the pattern is written.

A subject who fixes (1), re-runs, sees the build now fail, and stops has
**confirmed their explanation and left the bug in place**. A subject who asks
how the suite reports failures — and notices the echoed `$out` is missing a
line that appeared in the terminal — finds (2).

## Fairness

Both failing tests appear in the output of a single run. The bug report says
"tests are failing", not "the subtraction test is failing". Nothing is hidden;
the second cause is simply not the first explanation.
