#!/bin/sh
# Assert that a fixture's SCORER was committed before its RESULTS existed.
#
# This is the one part of the method that a machine can settle. Everything else
# in claim-fixture -- naive subjects, an unforgeable measurement, a fixture
# built from a real failure -- is judgement, and this skill says so. But
# "pre-registered" is either provable from the record or it is a claim the
# reader has to take on faith, which is precisely what pre-registration exists
# to avoid.
#
# Usage:  sh check_preregistration.sh <scorer-path> <first-result-path>
#
# Passes when the scorer's ADDING commit strictly precedes the result's.
# Same commit is a FAILURE: it proves nothing about the order they were written.
set -e
cd "$(git rev-parse --show-toplevel)"

added_commit() { git log --diff-filter=A --format='%H' -- "$1" | tail -1; }
commit_time()  { git show -s --format='%ct' "$1"; }

scorer=$1
result=$2
sc=$(added_commit "$scorer")
rc=$(added_commit "$result")

[ -n "$sc" ] || { echo "*** FAIL scorer '$scorer' is not committed"; exit 1; }
[ -n "$rc" ] || { echo "*** FAIL result '$result' is not committed"; exit 1; }

st=$(commit_time "$sc")
rt=$(commit_time "$rc")

if [ "$sc" = "$rc" ]; then
    echo "*** FAIL same commit ${sc%${sc#???????}} -- scorer and results landed"
    echo "         together, so the record cannot show which was written first."
    exit 1
elif [ "$st" -lt "$rt" ]; then
    echo "    ok   scorer ${sc%${sc#???????}} precedes results ${rc%${rc#???????}}"
    echo "         ($(( (rt - st) / 60 )) min apart)"
    exit 0
else
    echo "*** FAIL scorer was committed AFTER the results"
    exit 1
fi
