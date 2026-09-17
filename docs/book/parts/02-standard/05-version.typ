#import "../../preamble.typ": keyterm, headline, practice, chref

// DRAFT 2026-09-16. Ledger rows: C-II-32..42.

= Version what you got wrong <ch-version>

#headline[27 corrections, 24 of them in two days][
  Every major-version bump across the corpus's 53 skills. Almost all were
  recorded on the two days someone went looking.
]

== Two copies, one number

On 13 September there were two copies of the `bc` skill. One lived in the
repository. The other had been copied out for use on 5 September, and the two
had drifted apart by 29 lines. One of those differences was a correctness fix
that the repository's own verification had forced. Both copies said
`version: 1.0.0`. Their descriptions were byte-identical. Nothing a reader or an
agent could see told the copy with the broken rounding idiom from the copy
with the fixed one.

The version field was decoration. It had been filled in because skills have
version fields, and it said nothing about the difference that mattered.

The chapters so far have been about finding out that a skill is wrong. This one
is about what happens next. Somebody may already be holding the old text, and
that person needs to know how much the new text matters to them.

== What a reader has to do

Software versioning answers #emph[will my code still build?] A skill is not an
API. It is an instruction document, so the question it has to answer is
different: #emph[what do I have to do about the difference?] This corpus gives
each digit one answer.

#figure({
  set par(justify: false)
  table(
    columns: (auto, 1fr, 1fr),
    align: left,
    stroke: 0.5pt + luma(180),
    inset: 6pt,
    table.header[*Digit*][*What changed*][*What the reader must do*],
    [MAJOR], [The skill was wrong. It prescribed something that does not work,
      or that produces an incorrect result.],
      [Re-do work done under the old text. It may be wrong.],
    [MINOR], [A statement changed or grew: a behaviour added, guidance
      reworded to ask for something different, a threshold moved.],
      [Re-read before relying on it. Nothing to re-do.],
    [PATCH], [Nothing a reader acts on: a typo, a repaired link.],
      [Nothing.],
  )},
  caption: [The three digits, by the reader's obligation.],
)

// intro: version-as-wrongness
Read that way, the leading digit has an unusual property. `MAJOR − 1` is the
number of times the skill has been wrong since release. That is
#keyterm[version as wrongness]: a number that records how often you misled
someone, and one you should be reluctant to increment. Reluctant is not the
same as unwilling. A MAJOR bump you avoid is a false statement about the
skill's past.

Both halves of the MAJOR definition count. A skill can be #emph[silently
wrong]: `bc` prescribed a rounding idiom that, on the `bc` shipped with macOS,
returned the unrounded value without complaint. It can also be #emph[loudly
broken]: `tsort` told readers to check the exit status for a cycle, and BSD
`tsort` exits 0 on one. The silent kind is more dangerous, and it is tempting
to bump only for that kind. But "was it loud?" is a judgement that different
people will make differently. "Did the prescribed thing work?" can be checked.

== Published, not drafted

Most skills in this corpus were fixed during their own authoring. If those
fixes counted, skills would start at 2.0.0 or 3.0.0, and the number would
record how messy the drafting was. So the corpus draws the line somewhere else.

#emph[A correction is MAJOR only if a published state carried the error]: a
commit someone could have read, copied, or been served.

`bc` shows where that line falls. The skill was committed at 13:38 on 5
September. At 13:44 it was copied out for use. At 14:10 its portability bugs
were fixed. By intent, those fixes were a release pass. But a reader was already
holding the broken text, and the copy went on serving the broken idiom for a
week. The fix is MAJOR, by six minutes.

The same test cuts the other way. Several other skills were fixed on the way to
release as well. Their verification ran inside the release commit, so no wrong
state was ever published, and they stayed at 1.0.0 however much was fixed.

It is also how `role-deck` came to be wrong within six hours. It was released
as 1.0.0 at 02:43 on 15 September, verified, with 73 assertions. At 08:56 it
became 2.0.0. Its `verify` command reported #emph[run completed without wearing
required roles] on a perfectly valid run of any deck that listed its required
roles per exit. The code called `set()` on a dictionary, which yields the keys,
and compared card identifiers with role names. No such deck had ever been
played to the end, so nothing had exercised the path. Anyone who ran one under
1.0.0 got a spurious failure and had to check it again.

== A wrong reason is not a wrong prescription

The previous chapter ended with a promise: a refuted premise changes what a
skill is, and whoever relied on the old version needs to know. The corpus's
answer is more modest than that promise, and it is worth stating exactly.

When `role-deck`'s founding premise was measured and refuted, the skill went
from 2.1.0 to 2.2.0. That is a MINOR bump. The note recording the bump calls it a
judgement call, because it was one: #emph[the skill's stated reason was wrong;
none of its prescriptions were.] Every mechanism still worked as documented.
Anyone who had followed the skill had built a working deck, and there was
nothing to re-do. What had changed was why you would adopt it, and that
calls for re-reading. When the second premise fell, the bump was MINOR again.

Compare `claim-fixture` 2.0.0. That was MAJOR, for an omission. The method had
no step that proved the control arm had not already received the treatment,
and one run had been lost to exactly that. Nothing it prescribed was false, but
a result produced by following it could be. So its note tells the reader
to re-check any fixture designed under 1.0.0 before believing its result. An
omission is MAJOR when work done under the old text may be wrong.

The distinction has a cost, and it should be named. The version number tracks
wrong #emph[prescriptions]. It does not track wrong #emph[justifications]. A
reader holding `role-deck` 2.1.0 believed something false about agents, and the
digit that moved told them to re-read, not that they had been misled. If your
skill's value rests on its premise, a MINOR bump will undersell a refutation.
The words recorded with the bump have to carry what the digit cannot.

// intro: changelog
== The changelog travels with the skill

A number says that two texts differ and how much to care. It does not say what
changed. That is the job of the #keyterm[changelog]: in this corpus, one file
beside every skill, with one entry per version the skill has held. Each entry
opens with its level and says what a reader has to do.

The file is per skill rather than per repository for the reason this chapter
started with. A skill copied out for use travels alone, and a changelog at the
root of the repository would not go with it.

The contract has several clauses. When this chapter was drafted,
`tools/check-skills.sh` gated one of them: the newest entry must match the
version field. A bump with no entry failed the build, and that clause held
across all 53 skills.

The other clauses were written down and not checked, so a script was written
for this chapter to check them. Over 51 version changes, no entry declared a
level different from the digit that moved. But three entries did not open with
their level at all, and three changelogs had no entry for 1.0.0: two kept their
release notes under an older heading, and one never recorded 1.0.0 anywhere.
This was small, cosmetic decay. What mattered was where it was: entirely in the
clauses nothing checked. That is #chref(<ch-harness>)'s lesson again, in a file
written about honesty.

The fix took two steps, and the order matters. The six entries were corrected,
and the script was then promoted into `tools/check-skills.sh`, so each clause now
fails the build on its own. Correcting the entries without the gate would only
have reset the decay to zero.

== What the count is worth

Twenty-seven corrections sounds like a record of failure. Look at when they
happened. Nine were recorded on 13 September, when every skill's version was
rebuilt from its git history. Fifteen were recorded on 14 September, the day of
two audits that asked whether the dependency graphs and proof claims in the corpus's
mathematics and science skills
could be wrong. Three came afterwards.

The count does not measure how often skills were wrong. It measures how often
someone looked. Thirty-five skills are still at major version 1. Some of them
are right. Others have simply never been examined the way those were,
and the number cannot tell you which kind a given skill is. A clean 1.0.0 is not
evidence. A 4.0.0 is at least evidence that someone checked.

#emph["Nobody will trust a skill at 4.0.0."]

Then they will trust the wrong ones. Two skills in this corpus are at 4.0.0.
Each was found wrong three times across 13 and 14 September: once when its
history was re-read, and once by each of two audits that went looking for
claims nothing backed. A reader who prefers the skill at 1.0.0
is preferring the one nobody has checked. The number is only worth reading if
it is allowed to be embarrassing.

#practice[Bump for what the reader must do, and gate the record.][
  For each change to a skill, answer two questions before choosing a digit.
  #emph[Was the old text ever published?] If no reader could have held it, the
  fix is part of authoring and moves nothing. #emph[What must someone holding
  the old text do?] Re-do work: MAJOR. Re-read: MINOR. Nothing: PATCH. An
  omission that could have produced a wrong result is MAJOR.

  If the change refutes the skill's reason rather than its instructions, say so
  in the entry's first line. The digit will read MINOR, so the words have to
  carry the refutation.

  Write the changelog entry in the same commit as the bump. It should open with
  the level and state what the reader must do. Then look at your changelog
  contract and find every clause that no check enforces. Those are the clauses
  that are already decaying. Fix what has decayed, then gate the clause, or it
  will decay again.
] <pr-version>

Everything so far — the table, the harness, the oracle, the fixture, the
changelog — describes what to check. None of it says who does the checking. In
this corpus, it was almost always the agent. That is the next chapter.
