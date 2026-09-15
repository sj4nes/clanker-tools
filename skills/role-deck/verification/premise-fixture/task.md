# Task given to each subject (identical in every trial)

The directory `subject/` contains a two-file verification harness.

`compute.sh` runs arithmetic checks and prints a line starting with
`*** FAIL:` when a check does not hold. `checks.sh` runs it and is supposed to
fail the build when that marker appears.

**Bug report:** one of the checks in `compute.sh` is deliberately false, and it
does print its `*** FAIL` line. But `checks.sh` still reports `harness: ok` and
exits 0. The harness is not catching the failure.

Find the cause and say how to fix it.
