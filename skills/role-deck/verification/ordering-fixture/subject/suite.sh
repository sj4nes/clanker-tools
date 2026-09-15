#!/bin/sh
# Test suite for the widget module.
# Reports each test as "  PASS: <name>" or "  FAIL: <name> ...".

run_test() {
    if [ "$2" = "$3" ]; then
        printf '  PASS: %s\n' "$1"
    else
        printf '  FAIL: %s (expected %s, got %s)\n' "$1" "$2" "$3"
    fi
}

# A test whose subject raises rather than returning a value. The widget module
# writes its diagnostics to stderr, so this path reports there.
run_raising_test() {
    printf '  FAIL: %s (subject raised: unterminated token)\n' "$1" >&2
}

run_test addition        4 $((2 + 2))
run_test division        5 $((10 / 2))
run_test subtraction     3 $((1 + 1))
run_raising_test parser
printf 'suite complete\n'
