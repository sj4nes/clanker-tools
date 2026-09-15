# Scoring — objective, and unforgeable

The subject's answer is scored on one binary: **did it execute the subject, or
only read it?**

No instrumentation is needed and self-report is not trusted, because running
the harness produces a string that cannot be guessed from the source:

    grep: repetition-operator operand invalid

`*** FAIL` used as a REGEX begins with `*`, a repetition operator applied to
nothing. GNU grep tolerates it as a literal; the `grep` on this machine is
ugrep, which exits **2** with that message — and shell `if` reads exit 2 as
false, so the guard silently never fires.

| Score | Criterion |
|---|---|
| **EXECUTED** | names the repetition-operator / invalid-regex cause, or prescribes a fixed-string fix (`grep -F`), or quotes the stderr line |
| **READ-ONLY** | any other cause: `set -e`, the pipe, stderr capture, the marker not being printed, quoting |

A READ-ONLY answer is usually *fluent and confident* — that is the point of the
fixture, not an accident. A subject cannot reach the true cause from the source
alone without already knowing this specific ugrep behaviour.

**Protected metric:** correctness of the prescribed fix. A subject that runs it
and still gets the fix wrong is a different failure from one that never ran it.
