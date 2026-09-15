#!/bin/sh
# Arithmetic checks for the `widget` module.
# Each check prints "*** FAIL: <claim>" when it does not hold.
a=$((2 + 2))
if [ "$a" -ne 4 ]; then printf '*** FAIL: addition\n'; fi

b=$((10 / 2))
if [ "$b" -ne 5 ]; then printf '*** FAIL: division\n'; fi

# PLANTED: this check is deliberately false. The harness must catch it.
c=$((3 * 3))
if [ "$c" -ne 10 ]; then printf '*** FAIL: multiplication says 3*3 is not 10\n'; fi

printf 'ALL CHECKS PASSED\n'
