# Building and hosting the documentation

[Expanded counterpart](../docs/readthedocs.md).

## 1. Build and theme

- Sphinx + MyST + Furo; Gramlot logo/palette, light/dark mode, POC announcement.
- Version from pyproject.toml; no FastAPI/core/adapter installation needed.
- Install `docs/requirements.txt`; build:
  `python -m sphinx -n -W --keep-going -b html docs docs/_build/html`.
- Warnings and unresolved references fail; preview `docs/_build/html/index.html`.

## 2. CI

- Documentation workflow: main/develop/codex pushes, PRs to main/develop, manual dispatch.
- Docs-only dependencies; `documentation-html` artifact. Regular checks also build docs.
- Verification only: Actions workflow does not publish a site.

## 3. Read the Docs

- `.readthedocs.yaml`: Ubuntu 24.04, Python 3.12, docs requirements/conf, warnings fatal.
- Maintainer imports GitHub repo, selects main, enables versions and verifies webhook/build.
- External project connection remains separate;
  no live site claimed until a hosted build succeeds. Canonical URL comes from RTD environment.

## 4. Maintenance

- Update paired guides together; see [policy](documentation.md) for incomplete mirror coverage.
- Separate POC records from user navigation; synchronize docs requirements and pyproject extra.
- Official RTD/Furo references are in the expanded guide.
