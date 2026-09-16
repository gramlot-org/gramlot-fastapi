# gramlot-fastapi

Read README.md and SPECIFICATION.md before working. This is a pre-alpha
FastAPI adapter extracted from Gramlot and based on the genro-asgi repository layout.

- Keep code and maintained documentation in English.
- Use main for the baseline and develop for new development.
- Preserve copyright and Apache 2.0 notices.
- Keep secrets, virtualenvs, temp files and local worktrees out of Git.
- Use Python-first Gramlot declarations for applications; expose framework gaps
  instead of bypassing them with application-local DOM, events or fetch calls.
- Extract the existing gramlot.contrib.fastapi and gramlot.contrib.fastapi_genropy integrations here. Keep SQLAlchemy and Genropy (GnrApp) as independent optional database profiles; plain FastAPI hosting requires neither. Preserve host-independent facilities shared with other adapters in Gramlot.
- Run scripts/check.py before commits/pushes; add behavior tests with implementation.
- Ruff and test failures block delivery; mypy is advisory.
- Do not add assistant co-author trailers to commit messages.
- Keep documentation aligned with implemented behavior; no speculative API claims.
- Do not introduce automatic package publication or deployment without authorization.
