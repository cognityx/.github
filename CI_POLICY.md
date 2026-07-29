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
test anywhere below `tests/` requires no CI workflow change. Repositories whose
tests exercise optional runtime features set `install-all-extras: true`.

## Pull request merge gate

The CI workflow must run for every pull request targeting `main` and for every
push to `main`. Repository branch protection must require the workflow's test,
documentation, and build checks before a pull request can merge. Repositories
may add stricter lint, formatting, type, integration, or release checks.

## Documentation publication

Every repository with a root `mkdocs.yml` must install the
`publish-cognityx-docs` workflow template. A push to `main` dispatches a
`documentation-updated` event to `cognityx/cognityx.github.io`. The portal
then fetches documentation from repository default branches, builds component
sites, checks links, assembles the portal, and deploys GitHub Pages.

The `COGNITYX_DOCS_DISPATCH_TOKEN` Actions secret must be available to every
component repository. The portal requires `COGNITYX_DOCS_READ_TOKEN` when it
must discover or clone private repositories.

## New repository checklist

When creating a Cognityx Python repository:

1. Use `main` as the default protected branch and `devbb` for development.
2. Add `pyproject.toml`, `uv.lock`, `tests/`, and `.github/workflows/ci.yml`.
3. Configure pytest with `testpaths = ["tests"]`; never list individual tests.
4. Install the documentation workflow when `mkdocs.yml` exists.
5. Grant the documentation dispatch secret.
6. Require all CI checks on pull requests targeting `main`.
