#import "../preamble.typ": keyterm

= Case study 1: the expensive hat <sec:case-one>

== Fixture

A verification harness in which a deliberately false check prints a failure
marker, and the harness reports success anyway. The guard reads:

```sh
if printf '%s\n' "$out" | grep -q '*** FAIL'; then
```

which is correct on its face. The marker is printed; the grep looks for it.

It is nonetheless dead. As a regular expression, `*** FAIL` begins with a
repetition operator applied to nothing. The `grep` on the test machine rejects
the pattern and exits 2 — neither 0 (match) nor 1 (no match) — and a shell `if`
reads any non-zero status as false. The guard can never fire, for any input.

This is a real defect: it was found in eight of nine harnesses in the same
repository, plus the template they were copied from.

The fixture's value is that #emph[reading] it yields a confident wrong answer.
Plausible readings include `set -e` semantics, the pipe, and stderr capture.
Only running it produces the distinguishing evidence.

== Measurement

Executing the harness prints

```text
grep: repetition-operator operand invalid
```

That string occurs #keyterm[zero times] in the material handed to subjects.
Naming that cause, or prescribing the fixed-string fix it implies, is therefore
an artefact of execution rather than of reading. Nothing about the subject's
stated reasoning was scored.

== Result

Eight fresh agents received the bug report verbatim and nothing else. No deck,
no sequencing instruction, no suggestion to run anything.

#figure(
  table(
    columns: (auto, auto, auto),
    align: (left, center, left),
    table.header([*Score*], [*n*], [*Criterion*]),
    [EXECUTED], [*8*], [named the repetition-operator cause, or `grep -F`],
    [READ-ONLY], [0], [any other cause],
  ),
  caption: [Case study 1. Pre-registered band for this result: #emph[premise
  refuted — strike the founding justification.]],
) <tab:case1>

Several subjects went beyond the task, applying the fix and verifying it in
both directions.

#emph[Correction, 2026-09-17.] The table is what the scorer returned, not what
it proved. Every EXECUTED pattern except the second `grep`'s own message was
also in the repository's documentation, which subjects could read. Three
reports quote that message, which entered the repository only after the run;
five carry strings the documentation held plus a self-reported verification.
Counted as unproven, the pre-registered band is #emph[weakly supported], not
#emph[refuted]. The premise remains struck, since nothing supports it.

== Confound, weighed

The answer was independently documented elsewhere in the same repository, and
several subjects cited it. The task was therefore easier than designed.

This does not rescue the premise, but it does limit the result. Three subjects
quoted the #emph[actual] stderr of a second `grep` implementation on the machine,
a string that differs from the one in that documentation and is reachable only
by execution. Those three ran it. For the other five, reading and running
produce the same report.

A byproduct: those subjects also established that the repository's own
documentation had attributed the error message to the wrong binary. Both
implementations exit 2, so every conclusion drawn from it held; the attribution
did not.
