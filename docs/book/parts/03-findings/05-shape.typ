#import "../../preamble.typ": keyterm, practice, chref

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
level at which you stop having to plant a defect and check that the check
fails.] The discipline does not terminate in a tool that is finally
trustworthy. It terminates in the habit of breaking the thing on purpose,
applied one level up, every time.

== The four questions

Each audit produced one practice. Together they are four questions to ask of any
check you own, in the order that finds the most for the least effort.

#table(
  columns: (auto, 1fr),
  align: (left, left),
  table.header([*Ask*], [*Because*]),
  [Have I broken each guard #emph[alone]?],
    [guards mask each other, and one only ever seen to fail alongside another
     has not been tested],
  [Does every claim of verification #emph[resolve]?],
    [a compile checks the artifact, never the index that points at it],
  [What does this artifact state #emph[twice]?],
    [the duplicate written separately is a free independent oracle],
  [Has anyone measured the premise?],
    [the sentence justifying the whole thing is the one nobody checks],
)

The rule the four questions come from is to treat a check as broken until you
have seen it fail. None of the four defects in this part was found by reading
the check. The practice for it is @pr-harness, in #chref(<ch-harness>).
