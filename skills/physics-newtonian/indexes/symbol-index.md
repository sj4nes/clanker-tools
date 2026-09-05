# Symbol index (Release 0.1)

Formula-statement symbol occurrences. Discovery: `ptx -A -W '[A-Za-z_][A-Za-z0-9_]*' formulas/newtonian.md`; results confirmed by whole-token match against each `## node — statement` line.

### `K`
  - `kinetic_energy` — `K = (1/2) m v^2`
  - `work_energy_theorem` — `W_net = Delta K`
  - `mechanical_energy` — `E = K + U`
  - `conservation_of_mechanical_energy` — `E = K + U = const`

### `U`
  - `potential_energy` — `Delta U = - W_cons`
  - `gravitational_pe_uniform` — `U = m g h`
  - `elastic_pe` — `U = (1/2) k x^2`
  - `mechanical_energy` — `E = K + U`
  - `conservation_of_mechanical_energy` — `E = K + U = const`
  - `gravitational_pe_general` — `U = - G m_1 m_2 / r`

### `E`
  - `mechanical_energy` — `E = K + U`
  - `conservation_of_mechanical_energy` — `E = K + U = const`

### `P`
  - `power` — `P = dE/dt`  (and `P = F v` for a force on a particle)

### `p`
  - `momentum` — `p = m v`
  - `impulse_momentum_theorem` — `J = Delta p`
  - `conservation_of_momentum` — `sum p = const`

### `J`
  - `impulse` — `J = integral F dt`
  - `impulse_momentum_theorem` — `J = Delta p`

### `F_net`
  - `newton_first_law` — `F_net = 0  ⇒  a = 0`
  - `newton_second_law` — `F_net = m a`

### `F`
  - `hookes_law` — `F = - k x`
  - `work` — `W = integral F dx`  (component along displacement)
  - `force_from_potential` — `F = - dU/dx`
  - `power` — `P = dE/dt`  (and `P = F v` for a force on a particle)
  - `impulse` — `J = integral F dt`
  - `newton_gravitation` — `F = G m_1 m_2 / r^2`

### `N`
  - `normal_force` — `N` (contact reaction, perpendicular to surface)
  - `friction_kinetic` — `f_k = mu_k N`

### `W_net`
  - `work_energy_theorem` — `W_net = Delta K`

### `W`
  - `weight` — `W = m g`
  - `work` — `W = integral F dx`  (component along displacement)

### `G`
  - `newton_gravitation` — `F = G m_1 m_2 / r^2`
  - `gravitational_field` — `g = G M / r^2`
  - `gravitational_pe_general` — `U = - G m_1 m_2 / r`

### `g`
  - `weight` — `W = m g`
  - `gravitational_pe_uniform` — `U = m g h`
  - `simple_pendulum` — `T = 2 pi sqrt(L/g)`
  - `gravitational_field` — `g = G M / r^2`

### `k`
  - `hookes_law` — `F = - k x`
  - `elastic_pe` — `U = (1/2) k x^2`
  - `angular_frequency_shm` — `w = sqrt(k/m)`

### `m`
  - `newton_second_law` — `F_net = m a`
  - `weight` — `W = m g`
  - `kinetic_energy` — `K = (1/2) m v^2`
  - `gravitational_pe_uniform` — `U = m g h`
  - `momentum` — `p = m v`
  - `angular_frequency_shm` — `w = sqrt(k/m)`

### `v`
  - `velocity` — `v = dx/dt`
  - `speed` — `speed = |v|`
  - `kinetic_energy` — `K = (1/2) m v^2`
  - `power` — `P = dE/dt`  (and `P = F v` for a force on a particle)
  - `momentum` — `p = m v`

### `a`
  - `acceleration` — `a = dv/dt`
  - `newton_first_law` — `F_net = 0  ⇒  a = 0`
  - `newton_second_law` — `F_net = m a`
  - `power` — `P = dE/dt`  (and `P = F v` for a force on a particle)

### `r`
  - `newton_gravitation` — `F = G m_1 m_2 / r^2`
  - `gravitational_field` — `g = G M / r^2`
  - `gravitational_pe_general` — `U = - G m_1 m_2 / r`

### `h`
  - `gravitational_pe_uniform` — `U = m g h`

### `x`
  - `displacement` — `Delta x = x - x_0`
  - `hookes_law` — `F = - k x`
  - `elastic_pe` — `U = (1/2) k x^2`
  - `simple_harmonic_motion` — `x(t) = A cos(w t + phi)`

### `t`
  - `simple_harmonic_motion` — `x(t) = A cos(w t + phi)`

### `L`
  - `simple_pendulum` — `T = 2 pi sqrt(L/g)`

### `A`
  - `newton_third_law` — `F_(A on B) = - F_(B on A)`
  - `simple_harmonic_motion` — `x(t) = A cos(w t + phi)`

### `phi`
  - `simple_harmonic_motion` — `x(t) = A cos(w t + phi)`

### `mu_k`
  - `friction_kinetic` — `f_k = mu_k N`

