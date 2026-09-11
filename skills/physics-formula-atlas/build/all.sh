#!/bin/sh
set -eu
cd "$(dirname "$0")/.."

echo "== combined graph + tsort =="
sh validation/graph-check.sh

echo ""
echo "== worked traces =="
echo "-- physics-newtonian:newton_second_law (in-capsule only) --"
python3 build/prereq-path.py physics-newtonian:newton_second_law --roots-only
echo ""
echo "-- physics-thermodynamics:ideal_gas_law (crosses into physics-newtonian) --"
python3 build/prereq-path.py physics-thermodynamics:ideal_gas_law --roots-only
echo ""
echo "-- physics-thermoacoustics:specific_heat_cv (crosses thermo AND newtonian) --"
python3 build/prereq-path.py physics-thermoacoustics:specific_heat_cv --roots-only
echo ""
echo "-- physics-acoustics:acoustic_wave_equation_1d (crosses into newtonian AND thermodynamics) --"
python3 build/prereq-path.py physics-acoustics:acoustic_wave_equation_1d --roots-only

echo ""
echo "ALL OK"
