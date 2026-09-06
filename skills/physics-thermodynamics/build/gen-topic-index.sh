#!/bin/sh
# Topic index: nodes grouped by a coarse topic, derived from the registry so it
# stays in sync. Topic = a keyword match on id/title; unmatched nodes go to
# "other". Full statements live in formulas/thermodynamics.md.
set -eu
cd "$(dirname "$0")/.."
tsv=nodes/nodes.tsv

emit() {                       # $1 = heading, $2... = egrep pattern on id
  pat=$2
  printf '## %s\n' "$1"
  awk -F '\t' -v p="$pat" 'NR>1 && $1 ~ p { printf "%s%s", sep, $1; sep=" \xc2\xb7 " }
                           END { print "" }' "$tsv"
  echo
}

{
  echo "# Topic index (Release 0.1)"
  echo
  echo "Browse nodes by area. Full statements: \`../formulas/thermodynamics.md\`."
  echo "Prerequisite order: \`tsort-order.txt\`."
  echo
  emit "Math & conventions" '^(real_numbers|function|derivative|partial_derivative|integral|exact_differential|logarithm|SI_units|dimension_analysis|mass|length|time|energy|extensive_intensive|work_sign_convention|gas_constant)$'
  emit "System, state, process" '^(thermodynamic_system|state_variable|thermodynamic_equilibrium|state_function|process|thermodynamic_cycle)$'
  emit "Assumptions & regimes (first-class nodes)" '^(energy_conservation|quasistatic|reversible|irreversible|closed_system|isolated_system|ideal_gas)$'
  emit "Named processes" '_process$'
  emit "State variables" '^(pressure|volume|amount_of_substance|temperature|thermal_equilibrium|internal_energy|enthalpy)$'
  emit "Zeroth law & temperature" '^(zeroth_law|temperature|thermodynamic_temperature_scale)$'
  emit "Ideal gas" '^(ideal_gas|ideal_gas_law|ideal_gas_internal_energy|mayer_relation|heat_capacity_ratio|adiabatic_reversible_ideal_gas|entropy_ideal_gas)$'
  emit "First law, heat, work" '^(work_thermodynamic|first_law_thermodynamics|heat|heat_capacity|heat_capacity_cv|heat_capacity_cp|joule_free_expansion|joule_thomson_coefficient)$'
  emit "Second law" '^(kelvin_planck_statement|clausius_statement|second_law_equivalence|carnot_cycle|carnot_theorem|carnot_efficiency|carnot_cop|clausius_inequality|heat_engine|refrigerator)$'
  emit "Entropy" '^(entropy|entropy_increase_principle|entropy_free_expansion|tds_relations)$'
  emit "Potentials" '^(fundamental_relation_u|helmholtz_free_energy|gibbs_free_energy|free_energy_extremum|maxwell_relations)$'
  emit "Third law" '^third_law_thermodynamics$'
} > indexes/topic-index.md
echo "wrote indexes/topic-index.md"
