#!/bin/sh
# Check the deck, assert every gate can fire, then exercise the runner and
# assert every refusal and every tamper case is caught.
set -e
cd "$(dirname "$0")"
python3 check_deck.py decks/diagnose.json
echo
python3 simulate.py decks/diagnose.json 2000
echo
python3 check_deck.py decks/decide.json
echo
python3 simulate.py decks/decide.json 800
echo
echo "=== conditional-requirement property test ==="
python3 condition-check.py 300
echo
sh mutation-check.sh
echo
sh runner-check.sh
