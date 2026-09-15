# gramlot-fastapi

Read README.md and SPECIFICATION.md before working. This is a pre-alpha
boilerplate based on genro-asgi; no runtime host API has been implemented.

- Keep code and maintained documentation in English.
- Use main for the baseline and develop for new development.
- Preserve copyright and Apache 2.0 notices.
- Keep secrets, virtualenvs, temp files and local worktrees out of Git.
- Use Python-first Gramlot declarations for applications; expose framework gaps
  instead of bypassing them with application-local DOM, events or fetch calls.
- Use the existing gramlot.contrib.fastapi adapter. Keep Genropy database integration optional and separate from the plain FastAPI profile.
- Run scripts/check.py before commits/pushes; add behavior tests with implementation.
- Ruff and test failures block delivery; mypy is advisory.
- Do not add assistant co-author trailers to commit messages.
- Keep documentation aligned with implemented behavior; no speculative API claims.
- Do not introduce automatic package publication or deployment without authorization.
