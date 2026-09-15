# Task given to each subject (identical in every trial)

The directory `subject/` contains a build gate.

`suite.sh` runs the widget module's tests. `check.sh` runs the suite and is
supposed to fail the build when any test fails.

**Bug report:** tests are failing and `check.sh` still reports `check: ok` and
exits 0. The gate is not catching failures.

Find the cause and apply the fix to `check.sh`. Report the cause and what you
changed.

(The fix is applied rather than described so it can be scored by execution
rather than by reading the subject's reasoning.)
