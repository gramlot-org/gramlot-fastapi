# SQLAlchemy: scope and status

[Expanded counterpart](../docs/sqlalchemy.md).

## 1. What this repository hosts for now

FastAPI server adapter plus database-integration explanations, including SQLAlchemy.
Implemented: host, page/services, runtime delivery, optional legacy Genropy profile.
No ready-made FastAPI SQLAlchemy profile or page mixin. Host and DB contracts are
independent; documentation is not proof of a shipped API.

## 2. Existing SQLAlchemy experiment

Local core POC: `src/gramlot/contrib/sqlalchemy/sqlite.py`, exporting
`SqliteDbHandler`/`TableConfig`. Read-only SQLite via SQLAlchemy; explicit logical
tables, scalar string/integer primary key, text caption. Lookup and bounded literal
prefix/contains searches, optional Unicode casefold. Operation-scoped connections.
No general CRUD, model forms, migrations or all-dialect support established.

## 3. Source experiments versus the installable preview

Checksummed core 0.1.5 wheel is a specific POC snapshot, not every later checkout
feature. Public-install verification (2026-09-16): pinned wheel includes the SQLite
reader, with SQLAlchemy >=2,<3 as an optional core extra; plain hosting does not
install it. Installing SQLAlchemy alone does not enable a FastAPI profile. Compatible
core, lifecycle integration, configuration and package examples need verification.
Use getting-started for the verified plain host; Genropy remains separate/optional.

## 4. Open work and experimental limits

Set supported operations, lifecycle/configuration and installation tests. Writes,
transactions and model forms need explicit design. Descriptions are intended
preview behavior for API/design evaluation; bugs and incomplete cases may exist.

Source audit (2026-09-16): the local core SQLAlchemy directory is untracked;
its presence in the pinned wheel does not imply published GitHub source.
