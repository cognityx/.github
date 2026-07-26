# Cognityx organization defaults

Shared GitHub organization metadata and workflow templates.

Repositories containing a root `mkdocs.yml` can install the **Publish Cognityx
documentation** workflow template to request an immediate rebuild of the
public documentation portal after each push to their default branch.

The portal also discovers documentation repositories automatically every two
hours.

Component MkDocs navigation should begin with:

```yaml
nav:
  - Cognityx Home: https://cognityx.github.io/
```

This gives every generated component site a consistent route back to the
public documentation root.
