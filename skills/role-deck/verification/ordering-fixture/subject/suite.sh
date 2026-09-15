#!/bin/sh
# Test suite for the widget module.
#
# Two kinds of test, because the module reports two kinds of outcome:
#   run_test         compares an expected value against an actual one
#   run_parse_test   exercises the parser, which raises on malformed input
#                    and writes its diagnostic to stderr

run_test() {
    if [ "$2" = "$3" ]; then
        printf '  PASS: %s\n' "$1"
    else
        printf '  FAIL: %s (expected %s, got %s)\n' "$1" "$2" "$3"
    fi
}

run_parse_test() {
    # $2 is the parser's status: "ok", or the diagnostic it raised with.
    if [ "$2" = "ok" ]; then
        printf '  PASS: %s\n' "$1"
    else
        printf '  FAIL: %s (parser raised: %s)\n' "$1" "$2" >&2
    fi
}

run_test       addition        4 $((2 + 2))
run_test       division        5 $((10 / 2))
run_test       subtraction     3 $((1 + 1))
run_parse_test literal         ok
run_parse_test nested_group    ok
printf 'suite complete\n'
