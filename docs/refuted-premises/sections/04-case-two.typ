#import "../preamble.typ": keyterm

= Case study 2: confirming the first explanation <sec:case-two>

== Sharpening the claim until it was measurable

The first formulation — #emph[do agents enumerate competing explanations?] — is
not measurable. Enumeration is a private act, and asking about it yields
self-report.

The formulation that works came from framing the failure as a question the
agent asks itself: having formed a plausible explanation, does it ask
#emph[how do I confirm this?] rather than #emph[what else would produce this
symptom?] That is measurable, because #keyterm[a confirmatory fix passes its own
confirmation while the defect survives] — and whether the defect survives can be
decided by execution.

== Fixture

A build gate that fails to fail. Two real causes, both load-bearing:

+ The gate greps for `^FAIL`, anchored at column zero, while the suite indents
  its report lines. This is visible, plausible, and #keyterm[completely explains
  the presented symptom].
+ The gate captures `$(sh suite.sh)` — stdout only — while the suite reports a
  raising test's failure on stderr. Invisible in the presented run, because both
  such tests currently pass.

#figure(
  table(
    columns: (auto, auto, auto),
    align: (left, center, center),
    table.header([*Fix applied*], [*Presented bug*], [*Stderr-only failure*]),
    [anchor only], [exit 1 — confirmed], [*exit 0 — survives*],
    [anchor #sym.plus stderr capture], [exit 1], [exit 1],
  ),
  caption: [Why the confirmatory path is invisible: it passes its own check.],
) <tab:confirm>

== Tightened before running

An earlier build placed both failures in the visible output. That would have
made a null result uninterpretable: #emph[subjects discriminate by default] and
#emph[the clue was handed to them] are indistinguishable from the outcome alone.

The second cause was therefore moved out of the output and into the code, where
finding it requires reading the suite and asking how else a test reports
failure — which is the discriminating question itself rather than a prompt
toward it. The change was made and committed before any trial ran.

== Measurement and result

Subjects applied their fix to their own copy. The scorer #keyterm[executes it]
against a stderr-only failure that was not present in the fixture they were
given.

#figure(
  table(
    columns: (auto, auto),
    align: (left, center),
    table.header([*Score*], [*n*]),
    [COMPLETE — catches both channels], [*8*],
    [CONFIRMATORY — catches only the presented bug], [0],
    [BROKEN], [0],
  ),
  caption: [Case study 2. Pre-registered band: #emph[refuted].],
) <tab:case2>

The margin is wider than the table shows. Every subject constructed the
stderr-only test case themselves in order to verify their own fix. Every
subject also tested the all-pass case unprompted, several observing explicitly
that a gate wedged at #emph[fail] is as broken as one wedged at #emph[ok]. And
#keyterm[four of eight closed a third defect that had never been planted]: the
suite always exits 0, so a suite dying partway through reads as green. Two more
identified it and declined to fix it as out of scope.

The fixture was built so that stopping at the first explanation would feel
sufficient. No subject stopped there.
