# Integration architecture

Document ID: **GF-010**.

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/010-architecture.md).

<a id="1-product-boundary"></a>
<a id="gf-010-005"></a>

## 005 · Product boundary

Block ID: **GF-010-005**.

The [Gramlot constitution](https://github.com/gramlot-org/gramlot/blob/main/docs/00-constitution.md)
separates server and database adapters. FastAPI owns HTTP routing, request context,
TYTX invocation and runtime asset delivery. Gramlot owns Python page declarations,
shared hosting contracts, transport and JavaScript assets. Applications use Gramlot
Source, Data, bindings and services; reusable browser behavior belongs in the core.

<a id="2-current-implementation"></a>
<a id="gf-010-010"></a>

## 010 · Current implementation

Block ID: **GF-010-010**.

`gramlot_fastapi.application` owns routing and invocation, using `gramlot.hosting`
and `gramlot.transport`. `gramlot_fastapi.runtime` serves the prebuilt core assets.
A browser manifest is required by default; `development=True` explicitly enables
source-runtime development. The candidate pins the tested Gramlot 0.1.5 API.
`gramlot_fastapi.genropy` supplies invocation-scoped `GnrApp` access with database
work and cleanup on the same worker thread. Plain hosting requires no Genropy.

<a id="3-database-ownership-and-open-work"></a>
<a id="gf-010-015"></a>

## 015 · Database ownership and open work

Block ID: **GF-010-015**.

Shared database areas are `common`, `fake`, `genropy` and `sqlalchemy`; SQLite is a
SQLAlchemy backend. Server-independent database code belongs in Gramlot, currently
explored in `gramlot-poc`. SQLite already lives there in
`src/gramlot/contrib/sqlalchemy/sqlite.py`, not in this FastAPI package. Temporary
legacy placement is acceptable and is not a prerequisite for preview distribution.
The existing FastAPI Genropy profile has not yet been separated into that final
shared boundary. The [earlier design](040-server-and-database-integration.md) records
open operations, capabilities and resource policies, not a finalized portable API.
POC code and tests do not establish compatibility across all hosts and databases.

See [SQLAlchemy scope and status](035-sqlalchemy.md) for the current read-only SQLite
experiment, its location in the core POC, and the difference between checkout
capabilities and the installed preview wheel.
