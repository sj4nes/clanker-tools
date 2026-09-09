#!/bin/sh
# Assumption / regime / convention index: each governing node -> the nodes that
# name it as a DIRECT prerequisite (from the reverse-dependency view built by
# build-tree.sh). Transitive reach is noted in prose in the generated file.
set -eu
cd "$(dirname "$0")/.."

direct() {
  line=$(grep -E "^$1:" indexes/reverse-dependencies.txt || true)
  deps=${line#*:}
  echo "$deps" | tr ' ' '\n' | grep -v '^$' | sort | sed 's/^/  - /'
}

{
  echo "# Assumption / regime / convention index (Release 0.1)"
  echo
  echo "Each node below governs how a relation may be used; every node listed"
  echo "under it names it as a **direct** prerequisite edge. Source:"
  echo "\`indexes/reverse-dependencies.txt\` (regenerate with \`build/build-tree.sh\`"
  echo "then \`build/gen-assumption-index.sh\`)."
  echo
  echo "## \`dilute_ideal_solution\` (type: assumption, imported)"
  echo "Activity approximated by concentration. Direct dependents:"
  direct dilute_ideal_solution
  echo
  echo "**Transitive reach:** every \`E\`, \`Q\`, \`K\`, and \`Lambda_m\` expression"
  echo "in the capsule rests on this. It fails first for the multiply-charged"
  echo "ions at flow-battery concentrations (1-2 M) -- real cells use empirical"
  echo "corrections. Debye-Huckel-Onsager (\`debye_huckel_onsager\`) is the named"
  echo "conductivity correction; it is not applied."
  echo
  echo "## \`standard_state\` (convention, imported) -- unit activity, 1 bar, 298.15 K"
  direct standard_state
  echo
  echo "## \`standard_hydrogen_electrode\` (convention) -- E0(SHE) = 0"
  direct standard_hydrogen_electrode
  echo
  echo "Every \`standard_reduction_potential\` value, and therefore every"
  echo "\`E0_cell\`, \`dG\`, \`K\`, and Nernst \`E\`, is a difference from this"
  echo "chosen zero."
  echo
  echo "## \`butler_volmer_equation\` (principle_law -- STATED, NOT DERIVED)"
  echo "The current-overpotential law is a boundary node: its microkinetic"
  echo "derivation, and the meaning of the transfer coefficient alpha, are out"
  echo "of scope. Direct dependents:"
  direct butler_volmer_equation
  echo
  echo "## Embedded assumptions (not their own nodes -- Release 0.2 candidates)"
  echo
  echo "- **298.15 K** -- every quoted \`E0\`, \`K\`, \`RT/F = 0.02569 V\`, and the"
  echo "  \`0.05916 V\` Nernst prefactor. \`temperature_coefficient_emf\` is the"
  echo "  node that handles the \`T\`-dependence explicitly."
  echo "- **ideal gas** for electrolysis products (H2, O2, Cl2) -- carried by"
  echo "  \`gas_volume_electrolysis\` via the imported \`ideal_gas_law\`."
  echo "- **alpha ~ 0.5** (symmetric transfer coefficient) in \`butler_volmer_equation\`"
  echo "  and the \`tafel_equation\` slope."
  echo "- **ideal membrane selectivity** as the reference against which"
  echo "  \`crossover\` and \`shunt_current\` are the deviations."
} > indexes/assumption-index.md
echo "wrote indexes/assumption-index.md"
