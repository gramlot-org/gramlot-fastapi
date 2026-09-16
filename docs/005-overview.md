# FastAPI POC overview

Document ID: **GF-005**.

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/005-overview.md).

<a id="1-status-and-repositories"></a>
<a id="gf-005-005"></a>

## 005 · Status and repositories

Block ID: **GF-005-005**.

This is a POC under review, intended to become a consolidated prerelease after
review. No release date or stable API is promised. `gramlot-poc` is the executable
experimental core; the clean `gramlot` repository defines the constitution and
will contain the first consolidated product. Passing POC tests is evidence, not
acceptance of a port. The adapter candidate is 0.1.0a1; no publication is implied.

The preview evaluates APIs and design choices. Descriptions express intended
behavior; bugs and incomplete cases may exist. The adapter automatically installs
the checksummed experimental core wheel; no matching core source tag is needed.

<a id="2-responsibilities"></a>
<a id="gf-005-010"></a>

## 010 · Responsibilities

Block ID: **GF-005-010**.

FastAPI supplies server adaptation: requests, routing, invocation and asset delivery.
Database adapters supply backend access and metadata independently of the server.
Gramlot owns Python declarations, shared services, transport and reusable browser behavior.

<a id="3-trying-and-maintaining-the-poc"></a>
<a id="gf-005-015"></a>

## 015 · Trying and maintaining the POC

Block ID: **GF-005-015**.

See [release procedure](020-release.md) for a checksummed core candidate and clean
wheel installation. Development can use sibling `gramlot-poc`. Plain hosting and
legacy Genropy integration exist; portable database contracts remain under review.
The paired documentation follows [documentation policy](015-documentation.md).

This repository currently hosts the FastAPI server adapter and explains the
SQLAlchemy integration boundary. The core POC has an experimental read-only SQLite
reader, now connected to FastAPI through the optional `db_handler` parameter.
See [SQLAlchemy status](035-sqlalchemy.md).
