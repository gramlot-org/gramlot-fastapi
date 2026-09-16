# Integration architecture

[Expanded version](../docs/architecture.md).

## 1. Product boundary

Gramlot constitution separates host/DB adaptation. FastAPI owns HTTP, context,
TYTX invocation and asset delivery. Core owns declarations, hosting contracts,
transport and JS. Applications use Source/Data/bindings/services; no local bypasses.

## 2. Current implementation

`application`: routing via `gramlot.hosting`/`gramlot.transport`. `runtime`: core's
prebuilt assets; manifest required unless explicit `development=True`. Core pin:
0.1.5. `genropy`: invocation-scoped GnrApp, DB work and cleanup in one worker thread.
Plain host needs no Genropy.

## 3. Database ownership and open work

Areas: common/fake/genropy/sqlalchemy; SQLite is a SQLAlchemy backend. Shared code
belongs in core/POC. SQLite exists in POC's `contrib/sqlalchemy/sqlite.py`, not here.
Temporary legacy placement is acceptable for preview. FastAPI Genropy separation,
portable operations/capabilities/lifecycles remain open. Prior design is not a final
API; passing POC tests does not establish all host/backend compatibility.
