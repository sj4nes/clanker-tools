#import "../../preamble.typ": keyterm, headline, practice, chref
#import "../../corpus-facts.typ": corpus-asof, n-commits

// DRAFT 2026-09-17. Ledger rows: C-II-43..52.

= Work with the agent, not at it <ch-agent>

// REWRITE-PASS (drift-check.md §4): the 181 is still hand-counted -- no
// generator counts agent-co-authored commits yet. The denominator and date are
// now from the registry, so only this one number can drift.
#headline[181 of #n-commits commits][
  As of #corpus-asof, that many commits in this repository name an agent as
  co-author. The one skill about working that way has a single covered row, and
  that row's count was wrong.
]

== The check that disagreed

// intro: experience-library
The `experience-library` skill makes an arithmetic claim. A library of stored
examples gets more useful as it grows, until its entries start to compete with
each other, and there is a size where the benefit is largest. The agent
building the skill wrote the check first, in `bc`. The first draft of that check
stated the best size as 54.

`bc` printed a `FAIL` line and exited 1. The true best size is 55: the
crossover sits at 54.05, and the draft had stated the wrong side of it. The
failure came through the `1/0` backstop from #chref(<ch-harness>), which exists
because a check that only prints its failures is a check nobody reads.

Look at who did what. The agent stated the number. The agent wrote the check.
The check disagreed with the agent, and the agent reported the disagreement and
rewrote the section. It now #emph[finds] the best size by a scan, and it does
not assert a remembered constant. The record of this is the skill's own
verification notes: the failing draft was never committed.

The agent was not trustworthy in that story. It got the number wrong. What was
trustworthy was the arrangement. The claim and the check were separate objects,
and the check could come out the other way.

== Fluency is present in every case

Ask an agent to verify something and it will report that it verified it. The
report will be clear and well organised, and it will agree with you. All of
that is true whether the work was done well, done badly, or not done at all. A
signal that is present in every case carries no information.

// intro: directing-verification
So the useful question is never #emph[did it verify this?] It is #emph[what did
it produce that could have come out the other way?] Arranging the work so that
you can answer that question is #keyterm[directing verification]. The corpus
has a skill for it, `directed-verification`, first met in #chref(<ch-default>)
as the skill that reports its own table as weak. It has six behaviours. Each is a
move this book has already made, aimed at a collaborator instead of at a
document.

#figure({
  set par(justify: false)
  table(
    columns: (1fr, 1fr),
    align: left,
    stroke: 0.5pt + luma(180),
    inset: 6pt,
    table.header[*Behaviour*][*The same move, earlier*],
    [Ask for what would prove you wrong, not for confirmation.],
      [The default a skill displaces, #chref(<ch-default>): name what failure
      looks like before you look.],
    [Demand an artifact that can fail, not prose.],
      [A harness that can fail, #chref(<ch-harness>).],
    [Suspect the test before the subject.],
      [Break each guard alone, and then break the check on the check,
      #chref(<ch-harness>).],
    [Keep proposing separate from deciding.],
      [An independent oracle, #chref(<ch-oracle>): the expected value does not
      come from the thing that produced the answer.],
    [Re-run what you were told.],
      [An unforgeable measurement, #chref(<ch-premise>).],
    [Check what the command was aimed at, not that it ran.],
      [The stale source, #chref(<ch-oracle>): every fact true, the conclusion
      wrong.],
  )},
  caption: [`directed-verification`'s six behaviours, and where this book has
  already made each move.],
)

The last row points at an open problem, not a solved one. The corpus has no
answer to it yet. Grounding proves that a
command ran. It says nothing about whether the command read anything still in
use.

== The report you want is the one against you

// intro: agent-as-collaborator
In this corpus the agent did not only write text. It built the harnesses,
planted the defects, ran the fixtures, and wrote up what they found. That is
the #keyterm[agent as collaborator]: a participant in the quality of the work,
whose most valuable output is a result that disagrees with the person directing
it.

Three records show what that looks like.

The first is a premise. `role-deck`'s founding claim, that an agent left alone
will skip the expensive step, was written in commits the agent co-authored. It
was fixtured and struck in commits the agent co-authored. #chref(<ch-premises>)
tells that story: all 8 fresh agents reported doing the work unprompted, 3 with
proof, and then 8 of 8 did it again, provably, for the second claim. The collaboration asserted something about agents,
built the test that could refute it, and published the refutation.

The second is an experiment. In the first attempt to measure
`directed-verification`'s own behaviour 1, the function given to the subjects
was itself wrong. The subjects found it. Their harnesses were good enough to
fail on the "clean" code, and the scorer marked them `BROKEN` for doing the job
correctly. The commit that reported this opens its first reason with #emph["it
is mine"]. It also names the episode as another case where the test was wrong
and the subject was fine.

The third is a mistake, and it matters most. On the second attempt, both arms
scored 5 of 5. The agent's first reading was the agreeable one: #emph[no
headroom], and five near-identical report headings read as five agents
independently converging on good practice. Thirty-five minutes later the next
version withdrew that. Every control subject had `test-writing` loaded, which
prescribes the behaviour under test, so the two arms were one condition.
Independent agents do not converge on a section heading.

The agent agreed with itself first. What corrected it was not better judgement.
It was a record precise enough, the headings themselves, for the agreeable
reading to be checked against.

== Suspect the test, including this one

`directed-verification` has one covered row. Behaviour 3, #emph[suspect the test
before the subject], leaves a trace in a repository that records its
corrections, because the corrections are in the commit messages. A detector
searches the history for admissions that the harness was wrong. The skill
reported #emph[at least three], and called the number a lower bound. The
detector was self-tested in both directions: four real admissions it had to
match, and four ordinary messages it had to reject.

While this chapter was being drafted, the detector reported five. Read the five
sentences it matched, one at a time, and two of them were not admissions.

One is a hypothetical. The versioning commit says that where the record does
not show #emph[whether the instruction content or the harness was wrong], the
skill stays at 1.0.0. The other is the release commit of
`directed-verification` itself, describing what the detector counts. The
detector counts descriptions of itself, so the act of explaining the evidence
added to it.

Replay the scan as it stood at release, and it finds three. One of those three
is the hypothetical. The #emph[at least three] that shipped rested on two real
matches.

The detector also misses. The marker grep that could never match, from
#chref(<ch-bc>), was a harness that was wrong, and its commit says so in other
words. A count that includes false matches and also misses real ones is not a
lower bound. It is not any kind of bound.

The conclusion happens to survive. Read by hand, the history holds at least
three real cases. But the instrument that was cited for it did not show that.
The self-test could not have caught this. Its four negatives were sentences the
author wrote, and none came from the repository the detector reads. This is
#chref(<ch-harness>)'s lesson in its smallest form: the check proved it could
say no to sentences chosen for it, and it was never tested on the text it
actually reads.

The fix belonged to the skill, not to this book, so it went there, as
`directed-verification` 1.3.0. The claim of at least three now rests on the three
commits read by hand. A new check makes the detector find those three and
reject the two known false matches, and one real sentence it miscounted joined
its negatives. The word #emph[bound] is gone. It is worth saying where this was
found. It was found in the evidence for the one behaviour
about suspecting evidence. That is not irony. That is the behaviour working, a
day late.

== What the evidence does and does not say

#emph["It will just agree with me."]

Sometimes it will. The run-2 reading shows that. The answer is not to find a
less agreeable agent. The answer is #chref(<ch-premise>)'s, applied to your
collaborator: if the measurement is unforgeable, agreement cannot pass as
evidence. If the measurement is not unforgeable, the result is worth nothing
whoever produced it.

Be exact about what this corpus has shown. It has #emph[not] shown that
directing an agent makes the agent more careful. Behaviour 1 is the most
testable claim in the skill, and it has been fixtured three times. All three
runs were invalid, for the reasons #chref(<ch-premise>) gives. The two clean
measurements this corpus does have point the other way: agents left alone did
the expensive work, provably in 8 of 8 on one claim and in at least 3 of 8 on
the other.

So the case for directing verification cannot rest on the idea that agents cut
corners. It rests on something smaller, and better supported. Agreeable prose
is present whether or not the work is good. So the only way #emph[you] can tell
good work from bad is an artifact that could have come out the other way. The
skill says this about itself: it changes what you can check, and it does not
change how good the thinking was.

That makes the valuable case easy to recognise, and it feels bad. It is the
`FAIL` line on a number the agent had stated. It is a subject harness marked
`BROKEN` that turns out to be right. It is a withdrawn reading, 35 minutes
after an agreeable one. Each of them disagreed with whoever was directing the
work. If your collaboration never produces one, the likely reason is not that
you are always right. The likely reason is that nothing you asked for could
disagree.

#practice[Ask for what could come out the other way, and audit that too.][
  Before you accept a verification result from an agent, name the artifact
  that could have disagreed with you: a failing line, an exit status, a scored
  run, a patch re-run. If no such artifact exists, you have a report, not a
  result. Ask again for the case that would prove you wrong.

  When a result does disagree with you, suspect the check first. Then treat the
  disagreement as the most valuable thing the session produced, and record it
  in words someone can find later.

  Then turn the same suspicion on the evidence for your own practice. If you
  count your good behaviour, read what the counter matched. Test it on the text
  it will really read, not on examples you wrote for it. Check that it does not
  count the documents that describe it.
] <pr-agent>

Each chapter so far has been one move, made on a skill someone had already
written. The next chapter starts from a blank page and makes all of them, in
order.
