# Contributing to gramlot-fastapi

Keep the compatible Gramlot checkout at `../gramlot-poc`, then run
`uv sync --extra dev --extra docs` and `git config core.hooksPath hooks`.
Use `develop` for new development and keep changes focused on SPECIFICATION.md.

Before a commit or push, run `uv run python scripts/check.py` and inspect
`git diff --check`. Run `uv run mypy src/` as a non-blocking advisory check.
Validate distribution changes with `uv run python -m build` and
`uv run python -m twine check dist/*`.

Add behavior tests for host changes and use real integration infrastructure when
available. Plain-host tests must run without Genropy; Genropy lifecycle tests use
an explicit GnrApp-like object and the live database check remains opt-in.
Document public behavior and runtime dependencies in the same change.

Keep code, documentation and commit messages in English. Use focused conventional
commit messages and preserve Softwell copyright; do not add assistant authorship
trailers. Contributions are licensed under Apache 2.0.
