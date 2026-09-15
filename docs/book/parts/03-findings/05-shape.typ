#import "../../preamble.typ": keyterm

= The shape they share

Four audits, four unrelated technologies — an arbitrary-precision calculator, a
proof assistant, a topological sort, and a methodology's own justification — and
one defect.

== The check was reading the tool's opinion of itself

In every case the harness asked the tool whether *it* was upset, and treated
silence as evidence about the claim.

#table(
  columns: (auto, 1fr, 1fr),
  align: (left, left, left),
  table.header([*tool*], [*exits 0 on*], [*what the check thought it meant*]),
  [`bc`], [a false claim — it is a value, not an error], [the arithmetic holds],
  [`lean`], [`sorry`, `axiom`, a numeral-only proof], [the theorem is proved],
  [`tsort` (BSD)], [a cycle in the input], [the graph is acyclic],
  [a premise], [never being tested], [the methodology is needed],
)

The tools are not at fault. `bc` is a calculator and a wrong answer is a number;
Lean is a proof assistant and `sorry` is a legitimate placeholder. Each exit
code means exactly what its manual says. The defect is in the inference — and it
is the same inference four times.

== Three properties of the family

#keyterm[It is silent by construction.] A check that cannot fail looks
identical, in every log, to a check that passes. There is no symptom. The bc
harnesses ran green for weeks.

#keyterm[Partial protection is what hides it.] `bc` does catch a syntax error.
`lean` does catch a genuinely false closed statement. `tsort` does catch an
unregistered node. That partial coverage is precisely why nobody looked
further — the check demonstrably worked, on the cases it worked on.

#keyterm[It is only ever found by deliberate breakage.] Not one of these was
found by a failing build, because a failing build was the impossible event. Each
was found by planting a defect and noticing that nothing complained. The
practice has a name in this corpus — negative-contrast testing, or mutation —
and it is now a required line in the checklist: #emph[an assertion never seen to
fail is not known to be an assertion.]

== The recursion, which is the honest part

The harness built to catch missing graph edges contained a mutation that
#emph[reported itself as surviving] — it matched its target line literally, so a
trailing comment made the deletion do nothing. The fixture built to test whether
agents skip verification had a scorer that could not prove its own
pre-registration. The skill built to force disciplined process was justified by
two claims that had never been measured.

The defect appeared inside every attempt to fix the defect. That is not irony
for its own sake; it is the practical content of this part. #keyterm[There is no
level at which you stop having to plant a defect and check that something
screams.] The discipline does not terminate in a tool that is finally
trustworthy. It terminates in the habit of breaking the thing on purpose,
applied one level up, every time.
