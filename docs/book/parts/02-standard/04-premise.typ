#import "../../preamble.typ": keyterm, headline, practice, chref

// DRAFT 2026-09-16. Ledger rows: C-I-12, C-II-19..24.

= Measure the premise before you build on it <ch-premise>

#headline[5 runs, 0 positives][
  Every behavioural experiment this corpus has run. Two refuted the claim they
  tested, three were invalid, and none has ever confirmed anything.
]

== The half the table cannot give you

A displacement table ends with a column of defaults, and a covered row proves
that each default goes wrong #emph[if] an agent does it. It does not prove that
agents do it. That was the limit #chref(<ch-default>) left open.

// intro: premise
The sentence that fills the gap is the skill's #keyterm[premise]: the claim
about what agents or people do by default that makes the skill worth having.
#emph[Agents skip verification. Reviewers rubber-stamp. Developers do not read
the spec.] Premises sound obviously true, which is why they go unchecked, and
checking one risks learning that the skill was unnecessary. That risk is the
reason to check.

This corpus has one worked answer. `role-deck` rested on two premises: that an
agent left alone skips the expensive step, and that an agent with a plausible
explanation looks for confirmation instead of alternatives. Both were measured,
and both were false, 8 of 8 each time. #chref(<ch-premises>) tells that story.
This chapter is about the method, and about the three experiments that did not
get as far as a result.

== Six moves

// intro: claim-fixture
The method is a skill in this corpus, `claim-fixture`, the corpus's skill for
measuring a claimed default before anything is built on it. It comes down to
six moves.

*Split the claim.* Most premises are two claims. #emph[An agent will skip the
step, so the process must force it] contains a structural half — does the
process in fact make skipping impossible? — which an inspection or a gate can
settle, and a behavioural half — would anyone skip? — which needs subjects.
For `role-deck`, the structural half was already proven by a check over every
reachable state, so the experiment shrank to a single arm.

// intro: naive-subject
*Use subjects who cannot know the hypothesis.* A #keyterm[naive subject] is a
fresh agent with no shared context, or a person who has not been told what is
being measured. You are never one. Knowing the hypothesis ruins the
measurement, and no amount of discipline repairs it.

// intro: unforgeable-measurement
*Make the measurement unforgeable.* Ask a subject whether they considered
alternatives and they will say yes. An #keyterm[unforgeable measurement]
is one the subject cannot produce without doing the work. In the first
`role-deck` fixture, the evidence of having run the code was an error string
that appeared nowhere in the source. In the second, the scorer applied each
subject's fix and ran it against a failure they had never been shown.

// intro: pre-registration
*Commit the scorer before any result exists, in a separate commit.* This is
#keyterm[pre-registration]: the scoring and the interpretation of every
outcome, including the ones that refute you, written down first. The separate
commit is not pedantry. `claim-fixture` ships a check that reads the commit
history. It passes one of the corpus's fixtures, whose scorer landed twelve
minutes before its results. It fails the other, permanently. That scorer
#emph[was] written first, but it was committed with the results, and the
record cannot show the difference.

*Build the fixture from a real failure, and let the shortcut pass its own
check.* If the subject who cuts a corner gets an obviously wrong answer, you
have measured competence, not the default. In the second `role-deck` fixture,
fixing the obvious cause made the visible symptom go away. Only a second,
hidden cause separated a confirmer from a discriminator.

*Strike a refuted premise; do not reword it.* The reflex after a refutation is
to put a similar-sounding claim in its place. The second `role-deck` premise
was exactly that reflex, and it was tested instead of believed. It died too.

== Three ways an experiment dies

The refutations are the part of the record that reads well. The other three
runs are the part that teaches. All three tried to measure one claim, from the
skill about directing verification work: that an agent asked to #emph[verify
this] builds a weaker check than one asked to #emph[make this able to fail].

*Run 1: the instrument rewarded worse work.* The function under test contained
a bug of its own: it rounded negative ties the wrong way. A subject whose checks
were thorough enough to test negative ties saw the #emph[correct] implementation
fail, and scored as broken. The better the work, the worse the score. A session
limit also removed four of five subjects in one arm.

*Run 2: the control arm received the treatment.* Every fix from run 1 held.
Both arms scored 5 of 5, a difference of zero, and it was first reported as
#emph[no headroom] under a pre-registered ceiling rule. It was not. Every
control subject had `test-writing` loaded, a skill that prescribes the very
behaviour under test, because skills load from the session and not from the
directory the subject works in. The arms were one condition. There was a clue:
five supposedly independent reports shared a nearly identical section heading,
and one `grep` would have caught it. But the pre-registered reading of a null
result fired first, and it supplied a respectable explanation that stopped
anyone looking.

*Run 3: the treatment could not be delivered.* The contamination was fixed and
proven fixed: a probe showed the subjects' environment was clean. But the
treatment arm's instruction was to run the check against a wrong
implementation, and the subjects had been launched with no permission to run
anything. All fifteen scored #emph[no harness]. The environment was clean.
Nothing had checked that it was capable.

Each failure was knowable before a single subject was spawned. That is the
useful fact, and `claim-fixture` now carries a pre-flight gate built from all
three: is there a real contrast, can you prove the control stayed clean, can a
subject actually produce the artifact, is there an arm where an effect is known
to exist. Run against run 2 as it was actually designed, the gate blocks it at
five separate points.#footnote[Gates G2a, G2b, G4, G8 and G9, per
`claim-fixture`'s `verification/run.sh`, 16 September 2026. The gates were
derived from these failures, so catching them shows the gate is consistent with
its sources, not that it catches failures nobody has had yet.]

== What a null is worth

Five runs, and #emph[zero positives]. The method has never been shown to detect
an effect that was known to be there. Its sensitivity is untested, so its two
refutations are weaker evidence than 8 of 8 makes them look: they mean
#emph[no effect was detected], by an instrument nobody has yet seen detect one.

That does not rescue either `role-deck` premise. They were struck, and they stay
struck until something else is measured. It does mean the method owes the same
thing it demands of every fixture: a positive control, a claim known to be true,
run to see whether the instrument says so.

#emph["I cannot run experiments on people."]

You probably do not need to. The two `role-deck` fixtures used sixteen fresh
agents and about four minutes of wall time. That cheapness cuts both ways. The
three invalid runs were cheap too, and cheap to waste. The expensive part of an
experiment is not the subjects. It is the design, and the design is where all
three failures lived.

#practice[Before the first subject, prove the experiment can come out either way.][
  Find the sentence that justifies your document — the one asserting what goes
  wrong without it — and write it down as a claim. Split off its structural
  half, which inspection can usually settle.

  Then, before spawning anyone, answer four questions with evidence rather than
  confidence. #emph[Is the control clean?] List strings or files whose presence
  in a control transcript would mean it received the treatment, and plan to
  check for them before reading any outcome. #emph[Is the treatment
  deliverable?] Confirm a subject in that environment can actually produce the
  artifact you will score. #emph[Can the instrument see an effect?] Include a
  case where the effect is known to exist. #emph[Is the interpretation
  committed?] Commit the scorer and the outcome bands, alone.

  Use subjects who cannot know the hypothesis, which means not you, and score
  an artifact of doing the work or an execution of the subject's own output,
  never what they say they did.

  Only then run it. If a premise is refuted, strike it, and resist the sentence
  that wants to replace it.
] <pr-premise>

A refuted premise changes what a skill is, and someone who relied on the old
version needs to know. How to record that is the next chapter.
