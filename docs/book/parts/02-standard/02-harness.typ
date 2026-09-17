#import "../../preamble.typ": keyterm, headline, practice, chref, sidebar

// DRAFT 2026-09-16. Ledger rows: C-II-01..04, C-II-14..18.

// not-a-use: harness — the chapter title names what the chapter introduces
= Build a harness that can fail <ch-harness>

#headline[exit 0][
  From a check whose claim was false. It printed its own failure message, and
  then reported success.
]

== Red, green, and wrong

Here is a check written the way the textbooks say to write one.

It is a shell script that runs `bc` over a file of claims and stops on any
error. Before the file exists, the script fails: `bc` exits 4, missing file.
That is the red step. Write the file, asserting that two plus two is four, and
the script passes. Green. A test that was seen to fail and then seen to pass,
in that order.

Now change the claim to say two plus two is five. The script prints
`*** FAIL: two plus two is five` — and exits 0.#footnote[Measured on
`bc` 7.0.3, macOS, 16 September 2026. `bc`'s exit status reports interpreter
errors: 4 for a missing file, 2 for a syntax error. A false claim is a value,
not an error.]

The red step happened. It proved the check could fail, and it could: when there
was #emph[nothing]. It never showed the check failing when there was something
#emph[wrong]. Those are different transitions, and a defect lives on the second
one.

// intro: harness
This chapter is about the #keyterm[harness]: the script that runs your checks
and turns their results into one verdict, pass or fail. The previous chapter
asked for a run in which a default visibly fails. That run is only as good as
the harness under it. A harness that cannot fail certifies everything it is
pointed at, including the claims that are false.

== Assert; do not annotate

The first way a harness fails to fail is the plainest. It computes a number
and prints it next to what the number should be:

```
print "  dimensional check: ", lhs, " (want 4.5)\n"
```

That line is documentation. Nothing compares `lhs` with 4.5, so nothing goes
red when the formula drifts. A person reading the output would notice. The
harness will not, and nobody reads the output of a green run.

In this corpus, 15 of 24 `bc` check files looked like that, and only 4 of the
24 could have caught a wrong number. #chref(<ch-bc>) tells the whole story. The
rule it produced is short: every claim is an assertion that prints one failure
marker, and the harness fails when the marker appears.

== Break something you know is right

Asserting is necessary and not enough, because an assertion you have never seen
fail is only believed to be an assertion. So the next move is to make it fail
on purpose.

// intro: negative-contrast
Take an artifact you believe is correct, with a harness that passes. Change one
true thing to a false one: a constant, a sign, a dependency, an expected value.
Run the harness. It must go red. Then revert, and it must go green again. This
is a #keyterm[negative contrast]: the same harness, on a correct artifact and on
a broken one, giving opposite answers.

The point is the direction of the change. The red step in test-driven
development moves from #emph[nothing] to #emph[something], so it proves only
that a missing thing is noticed. A negative contrast moves from #emph[right] to
#emph[wrong], which is where the bugs you care about live. The two-plus-two
script passes the first test and fails the second.

// not-a-use: guard-isolation — the section heading names what the section introduces
== Break each guard alone

A serious harness has more than one guard. A typical `bc` harness in this corpus
ended up with three: the tool's exit status, a pass banner that must be
printed, and a failure marker that must not be. Three guards sounds robust.
It is also how a dead one hides.

When this corpus added a failure-marker check, the `grep` that looked for the
marker could never match: its pattern began with `*`, which the `grep` on that
machine rejected with an error, and the shell read the error as "no match". It
was dead in 8 of 9 harnesses and in the template all nine were copied from.
A corrupted value still turned the run red, because a wrong value also stopped
the pass banner and tripped the backstop. Nobody could see that the third guard
did nothing. Only a marker planted on its own, with everything else left
passing, could show it — and when that was finally tried, the run passed.

// intro: guard-isolation
So the rule is #keyterm[guard isolation]: break each guard alone. Plant a failure
marker while leaving the failure count at zero, so the banner still prints and
the tool still exits 0. If the run stays green, that guard never worked. A guard
that has only ever failed alongside another guard has not been tested.

#emph["My check is simple enough that it obviously works."]

The dead check was one line of shell. It was simple enough that it obviously
worked, in nine files, and it had never worked in eight of them.

== And then break the breaker

A negative contrast is itself a check, and it can fail to fail in the same way.

This corpus has a script that deletes a real edge from a dependency graph and
confirms the graph checker notices. It found the edge to delete by matching the
text of its line exactly. Some lines ended with a comment giving the evidence
for the edge. On those lines the match failed, nothing was deleted, and the
checker, handed an untouched graph, correctly said it was fine. The script
recorded the mutation as #emph[surviving], which read as a finding about the
checker. It was a finding about the script.

The fix is the same move one level up: confirm that the mutation actually
changed the artifact, and confirm that the mutation script goes red when the
checker is broken. This book's own chapter-order check is tested that way.
Its mutation script breaks each gate alone. With one gate disabled in the
checker, that mutation is reported as not caught. Put the gate back, and every
mutation is caught.

The recursion has to stop somewhere, and it stops quickly in practice: one
level of "does the breaker break?" catches most of what hides at that level.
What it must not do is stop at zero.

== None of this is new

Deliberately breaking a correct program to see whether its tests notice has a
name and a history. It is #emph[mutation testing]. Jia and Harman's survey
traces the idea to a 1971 student paper by Richard Lipton, and places the
field's birth in papers by DeMillo, Lipton and Sayward, and by Hamlet, in the
late 1970s.#footnote[Y. Jia and M. Harman, "An Analysis and Survey of the
Development of Mutation Testing," #emph[IEEE Transactions on Software
Engineering] 37(5):649–678, 2011; R. A. DeMillo, R. J. Lipton and F. G. Sayward,
"Hints on Test Data Selection: Help for the Practicing Programmer,"
#emph[Computer] 11(4):34–41, 1978; R. G. Hamlet, "Testing Programs with the Aid
of a Compiler," #emph[IEEE Transactions on Software Engineering]
SE-3(4):279–290, 1977.] What this chapter adds is not the idea. It is where the
idea has to be applied: to the checking scripts around agent skills, which are
rarely thought of as programs that need testing at all.

== "Isn't this just TDD?"

It is the same instinct: never trust a test you have not seen fail.#footnote[
Kent Beck, #emph[Test-Driven Development: By Example] (Addison-Wesley).] It is
not the same practice, in four ways.

+ *Red proves the test can fail, not that it fails for the reason you care
  about.* The two-plus-two script had a textbook red step and still passed a
  false claim.
+ *One red per test says nothing about guards masking each other.* The dead
  `grep` sat behind nine harnesses that went red when broken.
+ *Most checks come after the artifact.* Almost every harness in this corpus
  was written around a document, a proof or a graph that already existed.
  There was never a red step to take. Planting a defect creates one.
+ *It recurses.* A red step happens once, when the test is written. The check on
  the check needs the same treatment, as the mutation script showed.

There is also direct evidence that telling an agent to "use TDD" does not get
you there. In Luu's experiment, agents prompted to use TDD did write failing
tests before the code in 67 of 160 runs, against 0 of 160 with no
instructions. They still produced worse tests: many small trivial ones, with the
hard cases avoided. Luu adds that iterating to green tended to make agents write
incorrect tests that enforced incorrect behaviour.#footnote[Luu, "How well do
agents use test/verification techniques?" The finding is about prompting agents
with TDD, not about TDD as people practise it; Luu notes that a TDD advocate
would say the agents did not really do TDD, and that why they behaved this way
is "not obvious from the outside". The remark about incorrect tests is made
across conditions, not about TDD alone.] The red step happened. It was not
aimed at the defect.

#practice[Plant a defect in something you know is right.][
  Treat a check as broken until you have seen it fail. A passing check and an
  impossible one look identical in every log, and reading the check will not
  tell them apart.

  Pick a check that currently passes, on an artifact you believe is correct.
  Change one true thing in the artifact to a false one. Do not delete a file or
  empty a section: that tests absence, and absence is the easy case. Run the
  check. If it stays green, the check never covered that claim.

  If it goes red, look at which guard caught it. List the guards the harness
  actually has — typically the tool's exit status, a pass banner and a failure
  marker — and break each of the others alone. Plant a failure marker without
  touching the failure counter, so the banner still prints and the tool still
  exits zero. A guard you have only seen fail alongside another guard has not
  been tested.

  Revert, confirm green, and write down what you planted and what caught it.
  If the planting is scripted, run the script once against a checker you have
  deliberately broken, and watch the script fail.
] <pr-harness>

#sidebar[The control that caught the fixture, twice][
  The last clause of the practice above — run the planting script against a
  checker you have deliberately broken — was added to this book's own toolchain
  as an afterthought, and has since been the only thing standing between it and
  two false results.

  Parts IV to VI of this book are generated from the repository, and a script
  breaks each of that generator's gates in turn on a scratch copy, requiring
  each to fail alone. Alongside the deliberate breakages it runs one case with
  #emph[no] mutation at all, which must pass.

  Twice in two days, that unmutated case was the only one that failed
  correctly. The first time, the scratch copy was missing a directory the
  generator reads, so thirteen mutations reported "caught" while proving
  nothing — every one of them was failing on the missing directory rather than
  on the defect it had planted. The second time, a new generator called #raw("git")
  unconditionally and could not run outside a checkout, which is exactly what a
  scratch copy is.

  Neither defect was in the thing under test. Both were in the fixture, and in
  both cases the mutations all said #emph[caught]. A suite where every case
  fails is indistinguishable from a suite where every case is broken, unless one
  case is supposed to pass.
]

A harness that can fail still has to be told what #emph[right] looks like.
Where that expected value comes from is the next chapter.
