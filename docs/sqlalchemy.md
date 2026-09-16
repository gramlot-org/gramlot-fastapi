# SQLAlchemy: scope and status

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/sqlalchemy.md).

## 1. What this repository hosts for now

This repository hosts the FastAPI server adapter and explanations of database
integration, including SQLAlchemy. It currently implements HTTP hosting, page and
service invocation, runtime delivery and an optional legacy Genropy profile.
It does not provide a ready-made FastAPI SQLAlchemy profile or a SQLAlchemy page
mixin. Documentation of a direction does not establish a shipped API.

Server adaptation and database adaptation are independent responsibilities.
SQLAlchemy translates database operations; FastAPI handles web requests. A
database adapter should implement the Gramlot database contract without depending
on a particular web server. See [architecture](architecture.md).

## 2. Existing SQLAlchemy experiment

The local core POC implementation lives in
`src/gramlot/contrib/sqlalchemy/sqlite.py`. At the 2026-09-16 check, this directory
was still untracked in the core checkout, so no published GitHub source link is
claimed. The module is included in the pinned core wheel described below. It exports `SqliteDbHandler` and
`TableConfig` through `gramlot.contrib.sqlalchemy`.

This is a bounded, read-only SQLite experiment using SQLAlchemy. It opens an
existing database, exposes explicitly configured logical tables, and maps each
to identity and caption columns. The initial reader supports identity lookup and
literal prefix/substring searches, bounded results and optional Unicode casefold
matching. It acquires a connection for an operation and releases it afterward.

The inspected implementation requires a single string/integer primary key and a
text caption. It does not establish a general CRUD interface, automatic model
forms, migration management or support for every SQLAlchemy database dialect.
SQLite is the database backend; SQLAlchemy is the library used to access it.

## 3. Source experiments versus the installable preview

The adapter's normal installation fetches one checksummed experimental Gramlot
0.1.5 wheel. That number identifies the packaged snapshot, not all subsequent
work in `gramlot-poc`. The presence of a module in a development checkout does not
guarantee that it is included in the distributed wheel.

The public-installation check on 2026-09-16 verified that the pinned wheel does
contain `contrib/sqlalchemy/sqlite.py`. Its metadata declares SQLAlchemy as an
optional `sqlalchemy` extra (`>=2.0,<3`); plain FastAPI installation does not install
that dependency. Presence of the reader is therefore distinct from an enabled,
configured and verified FastAPI database profile.

Do not assume that installing SQLAlchemy alone enables a FastAPI database profile.
A compatible core, the adapter's connection to the invocation lifecycle, and
verified configuration and examples must be delivered together before a supported
installation recipe for that profile can be documented here.

For now, use [getting started](getting-started.md) for the verified plain FastAPI
preview. The Genropy profile is separately documented and optional.

## 4. Open work and experimental limits

The remaining SQLAlchemy work includes defining the intended supported operations,
connecting database resources to page invocations, documenting configuration and
verifying the resulting package installation. Write operations, transaction policy
and any model-derived forms require explicit decisions and their own checks.

These are previews for evaluating APIs and design choices. Descriptions express
intended behavior; bugs, incomplete paths and behavior changes may exist. Passing
checks cover particular scenarios and do not guarantee a bug-free product.
