# FastAPI POC overview

Document ID: **GF-005**.

[Expanded version](../docs/005-overview.md).

<a id="1-status-and-repositories"></a>
<a id="gf-005-005"></a>

## 005 · Status and repositories

Block ID: **GF-005-005**.

POC under review; planned consolidated prerelease has no promised date or stable
API. Experimental runtime: `gramlot-poc`. Clean `gramlot`: constitution, ports,
future first product. Tests provide evidence, not port acceptance. Candidate
0.1.0a1 is not published by this work.

The preview evaluates APIs and design choices. Descriptions express intended
behavior; bugs and incomplete cases may exist. The adapter automatically installs
the checksummed experimental core wheel; no matching core source tag is needed.

<a id="2-responsibilities"></a>
<a id="gf-005-010"></a>

## 010 · Responsibilities

Block ID: **GF-005-010**.

FastAPI: server adaptation. Database adapters: backend/model adaptation.
Gramlot: Python declarations, shared
services, transport and reusable JavaScript.

<a id="3-trying-and-maintaining-the-poc"></a>
<a id="gf-005-015"></a>

## 015 · Trying and maintaining the POC

Block ID: **GF-005-015**.

[Release](020-release.md): checksummed core, isolated wheel verification. Development:
sibling POC. Plain host and legacy Genropy exist; shared DB contracts under review.
Maintain paired docs via [policy](015-documentation.md).

This repository currently hosts the FastAPI server adapter and explains the
SQLAlchemy integration boundary. The core POC has an experimental read-only SQLite
reader, now connected to FastAPI through the optional `db_handler` parameter.
See [SQLAlchemy status](035-sqlalchemy.md).
