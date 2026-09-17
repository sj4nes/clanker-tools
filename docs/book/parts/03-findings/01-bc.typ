#import "../../preamble.typ": keyterm, headline, practice, chref

= A harness that could not fail <ch-bc>

#headline[4 of 24][
  `bc` verification harnesses could catch a wrong number. The other twenty
  reported success on any input, including one where every assertion was false.
]

== The tool's opinion of itself

`bc` is the Unix arbitrary-precision calculator, used across this corpus to
check formulas exactly — a dimensional identity, a closed form against an
independent oracle, a rounding boundary. A harness ran `bc` over a file of
checks and failed the build on a nonzero exit.

That is the defect, and it is invisible until stated precisely: #keyterm[`bc`'s
exit status reports interpreter errors, never a false claim.] It exits 2 on a
syntax error, 3 on an undefined function, 4 on a missing file, 1 on a math
error. A claim that is simply *wrong* is a value to a calculator, not an error.
And `quit` takes no status argument — `quit 1` exits 0.

So `set -e; bc checks.bc` catches a *broken* file and never a *wrong* one. That
partial protection is exactly what made it look safe.

== Annotating instead of asserting

The second finding compounded the first. Fifteen of the twenty-four files did
not assert at all. They computed a number and printed it beside prose:

```
print "  dimensional check: ", lhs, " (want 4.5)\n"
```

Nothing fails when the formula drifts. The file reads as verification and
// intro: knowledge-capsule
provides none. Worse, several #emph[capsules] — the corpus's
packaged bodies of domain knowledge, described properly in #chref(<ch-graph>) — had
already computed an #emph[independent
oracle] — the quantity derived a second way — and simply never compared the two.

Two checks were vacuous in a sharper sense: `statistics` had a Cramér–Rao bound
check where the two sides were the same expression, and the Poisson line read
literally `(lam/n)/(lam/n)`. It printed the expected `1` by construction.
// intro: visualization-design
So did a check in `visualization-design`, the corpus's skill for designing
charts: its zero-baseline lie-factor check had the identical shape.

== The guard that could never fire

The remediation added a failure marker — assertions print `*** FAIL: <claim>` —
and a runner that greps the output for it. That grep turned out to match nothing, ever, in
#keyterm[eight of nine harnesses, plus the template they were all copied from]:

```sh
if printf '%s\n' "$out" | grep -q '*** FAIL'; then
```

As a regular expression, `*** FAIL` opens with a repetition operator applied to
nothing. GNU grep tolerates it as a literal; the `grep` on this machine is
ugrep, which exits 2 with `error at position 4 … empty (sub)expression`. Shell
`if` reads any nonzero status as false. The clause could not fire.

It had been masked by the other two signals — a missing pass banner, and a
deliberate `1/0` backstop added to force a nonzero exit — which is why a
corrupted value still failed the run and nobody noticed the third guard was
inert. A marker planted on its own, with the other two signals left passing,
went through with exit 0.

== What changed

All twenty-four harnesses now assert every claim, print the marker on failure,
and are grepped with `grep -qF` — fixed-string, nothing to get wrong. Each was
negative-contrast tested: corrupt a value, confirm a nonzero exit, revert.

The checklist gained a line that reads oddly until you have been here:
#keyterm[test each signal in isolation]. A marker planted with the failure
counter untouched — banner still printed, `bc` still exiting 0 — must make the
run fail. That is the only way to see the grep clause work, and it is how the
broken form hid in eight files.

The practice for this finding is @pr-harness, in #chref(<ch-harness>).
