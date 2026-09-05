# `tsort` planning patterns

## Staged Rust release plan

```text
generate_sources cargo_check
cargo_check cargo_test
cargo_test cargo_fmt_check
cargo_fmt_check build_release
build_release verify_artifact
verify_artifact sign_artifact
sign_artifact publish_release
publish_release postpublish_smoke_test
```

Enforces: generate sources → compile-check → tests → formatting → build release artifact → verify artifact contents/digest → sign the verified artifact → publish → post-publication smoke test.

Do not assume the order between `cargo_test` and `cargo_fmt_check` is inherently required unless project policy says so. If both only need `cargo_check` and both precede `build_release`, model them as independent to preserve parallel validation:

```text
generate_sources cargo_check
cargo_check cargo_test
cargo_check cargo_fmt_check
cargo_test build_release
cargo_fmt_check build_release
```

## Expand-contract database migration plan

Compatibility-safe schema deployment:

```text
backup_verified add_nullable_column
add_nullable_column deploy_compatible_app
deploy_compatible_app backfill_data
backfill_data validate_backfill
validate_backfill enforce_constraint
enforce_constraint remove_legacy_path
remove_legacy_path postdeploy_check
```

1. Verify backup.
2. Add a backward-compatible schema extension.
3. Deploy software compatible with both old and new forms.
4. Backfill data.
5. Validate the backfill.
6. Enforce a stronger constraint.
7. Remove legacy application behavior.
8. Final health check.

If the graph produces a cycle between an application deployment and a migration, investigate whether the migration can be made backward-compatible or whether a staged release is required.

## Configuration rollout plan

```text
validate_config stage_config
stage_config deploy_canary
deploy_canary observe_canary
observe_canary approve_rollout
approve_rollout deploy_fleet
deploy_fleet verify_fleet
verify_fleet archive_previous_config
```

Human approval is made explicit (`observe_canary approve_rollout`, `approve_rollout deploy_fleet`) rather than implied. Do not execute `deploy_fleet` merely because `tsort` ordered it after the canary — human approval remains a real-world gate.

## Code-refactor plan

Introduce a new API, then later remove the old one:

```text
add_new_api add_compatibility_tests
add_new_api migrate_callers
add_compatibility_tests validate_migration
migrate_callers validate_migration
validate_migration remove_old_api
remove_old_api final_test_suite
```

1. Add the new API.
2. Add compatibility tests.
3. Migrate callers.
4. Verify both the API and callers.
5. Remove the old API only after migration verification.
6. Run final tests.

Do not encode `remove_old_api` before all known callers and consumers have migrated.
