#!/bin/sh
# Assumption / regime index: each first-class regime node -> the nodes that name
# it as a DIRECT prerequisite (straight from the reverse-dependency view built
# by build-tree.sh). Transitive reach is noted in prose in the generated file.
set -eu
cd "$(dirname "$0")/.."

direct() {
  line=$(grep -E "^$1:" indexes/reverse-dependencies.txt || true)
  deps=${line#*:}
  echo "$deps" | tr ' ' '\n' | grep -v '^$' | sort | sed 's/^/  - /'
}

{
  echo "# Assumption / regime index (Release 0.1)"
  echo
  echo "Each regime node below is a first-class graph node; every node listed"
  echo "under it names it as a **direct** prerequisite edge, so applying that"
  echo "node outside the regime is a visible graph violation. Source:"
  echo "\`indexes/reverse-dependencies.txt\` (regenerate with \`build/build-tree.sh\`"
  echo "then \`build/gen-assumption-index.sh\`)."
  echo
  echo "## \`dilute_ideal_solution\` (type: assumption)"
  echo "Solute–solute interactions negligible; activity ≈ concentration / c°."
  echo "Direct dependents:"
  direct dilute_ideal_solution
  echo
  echo "**Transitive reach:** through \`equilibrium_constant\` and"
  echo "\`ph_definition\` this assumption also underlies every downstream"
  echo "equilibrium and acid–base node — \`reaction_quotient\`, \`q_versus_k\`,"
  echo "\`kp_kc_relation\`, \`water_autoionization\`, \`weak_acid_equilibrium\`,"
  echo "\`ka_kb_relation\`, \`henderson_hasselbalch\`, \`strong_acid_base_ph\`,"
  echo "\`poh_relation\`, \`ice_table\`, \`percent_ionization\`, \`buffer\`,"
  echo "\`acid_base_titration_curve\`, \`reaction_isotherm\`. Debye–Hückel and"
  echo "non-ideal solution theory are out of scope (\`scope.md\`)."
  echo
  echo "## \`ideal_gas\` (embedded in \`ideal_gas_law\`, not yet a node)"
  echo "Point molecules, no intermolecular forces; the low-\`P\`, high-\`T\` limit."
  echo "\`ideal_gas_law\` is \`bridge_imported\` and carries this assumption in its"
  echo "entry prose. Direct dependents of \`ideal_gas_law\`:"
  direct ideal_gas_law
  echo
  echo "Promoting \`ideal_gas\` to its own node is a Release 0.2 item"
  echo "(\`validation/consistency-audit.md\`)."
  echo
  echo "## \`heat_work_sign_convention\` (type: convention) — \`ΔU = q − w\`"
  direct heat_work_sign_convention
  echo
  echo "## \`standard_state\` (type: convention) — \`P° = 1 bar\`, solutes \`1 mol/L\`"
  direct standard_state
  echo
  echo "## \`standard_conditions_stp\` (type: convention) — IUPAC STP, \`1 bar\`"
  echo "A leaf reference node (no direct dependents); used when reading a molar"
  echo "volume off \`molar_volume\` at STP. Note the 1 bar vs 1 atm split."
  echo
  echo "## \`dimensional_analysis\` (type: convention) — \`[M L T Θ N]\` bookkeeping"
  direct dimensional_analysis
} > indexes/assumption-index.md
echo "wrote indexes/assumption-index.md"
