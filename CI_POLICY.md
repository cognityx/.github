# Cognityx Continuous Integration Policy

Every production source change requires tests. Every test under `tests/` runs
in GitHub CI, and no test may be maintained only as a local command. CI must
pass before merge.

Do not disable, skip, or mark a failing regression test as expected without a
documented reason. Bug fixes require a regression test where practical.

## Ownership

- Repository tests verify that repository's contract.
- Cognityx SDK tests verify cross-component composition.
- SDK wheel verification validates the released installation artifact.

Every Cognityx Python repository must provide:

```text
pyproject.toml
uv.lock
tests/
.github/workflows/ci.yml
```

The caller workflow runs the centrally maintained reusable workflow. Adding a
test anywhere below `tests/` requires no CI workflow change.
