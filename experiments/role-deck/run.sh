#!/bin/sh
# Check the deck, assert every gate can fire, then exercise the runner and
# assert every refusal and every tamper case is caught.
set -e
cd "$(dirname "$0")"
python3 check_deck.py decks/diagnose.json
echo
sh mutation-check.sh
echo
sh runner-check.sh
