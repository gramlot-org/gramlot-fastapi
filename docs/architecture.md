# Integration architecture

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/architecture.md).

## 1. Product boundary

The [Gramlot constitution](https://github.com/gramlot-org/gramlot/blob/main/docs/00-constitution.md)
separates server and database adapters. FastAPI owns HTTP routing, request context,
TYTX invocation and runtime asset delivery. Gramlot owns Python page declarations,
shared hosting contracts, transport and JavaScript assets. Applications use Gramlot
Source, Data, bindings and services; reusable browser behavior belongs in the core.

## 2. Current implementation

`gramlot_fastapi.application` owns routing and invocation, using `gramlot.hosting`
and `gramlot.transport`. `gramlot_fastapi.runtime` serves the prebuilt core assets.
A browser manifest is required by default; `development=True` explicitly enables
source-runtime development. The candidate pins the tested Gramlot 0.1.5 API.
`gramlot_fastapi.genropy` supplies invocation-scoped `GnrApp` access with database
work and cleanup on the same worker thread. Plain hosting requires no Genropy.

## 3. Database ownership and open work

Shared database areas are `common`, `fake`, `genropy` and `sqlalchemy`; SQLite is a
SQLAlchemy backend. Server-independent database code belongs in Gramlot, currently
explored in `gramlot-poc`. SQLite already lives there in
`src/gramlot/contrib/sqlalchemy/sqlite.py`, not in this FastAPI package. Temporary
legacy placement is acceptable and is not a prerequisite for preview distribution.
The existing FastAPI Genropy profile has not yet been separated into that final
shared boundary. The [earlier design](server-and-database-integration.md) records
open operations, capabilities and resource policies, not a finalized portable API.
POC code and tests do not establish compatibility across all hosts and databases.

See [SQLAlchemy scope and status](sqlalchemy.md) for the current read-only SQLite
experiment, its location in the core POC, and the difference between checkout
capabilities and the installed preview wheel.
