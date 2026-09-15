#!/bin/sh
# Check the diagnose deck, then assert every gate can actually fire.
set -e
cd "$(dirname "$0")"
python3 check_deck.py decks/diagnose.json
echo
sh mutation-check.sh
