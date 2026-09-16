# FastAPI POC overview

[Expanded version](../docs/overview.md).

## 1. Status and repositories

POC under review; planned consolidated prerelease has no promised date or stable
API. Experimental runtime: `gramlot-poc`. Clean `gramlot`: constitution, ports,
future first product. Tests provide evidence, not port acceptance. Candidate
0.1.0a1 is not published by this work.

The preview evaluates APIs and design choices. Descriptions express intended
behavior; bugs and incomplete cases may exist. The adapter automatically installs
the checksummed experimental core wheel; no matching core source tag is needed.

## 2. Responsibilities

FastAPI: server adaptation. Database adapters: backend/model adaptation.
Django can supply both, as distinct roles. Gramlot: Python declarations, shared
services, transport and reusable JavaScript.

## 3. Trying and maintaining the POC

[Release](release.md): checksummed core, isolated wheel verification. Development:
sibling POC. Plain host and legacy Genropy exist; shared DB contracts under review.
Maintain paired docs via [policy](documentation.md).

This repository currently hosts the FastAPI server adapter and explains the
SQLAlchemy integration boundary. The core POC has an experimental read-only SQLite
reader; a packaged FastAPI SQLAlchemy profile is not supplied here.
See [SQLAlchemy status](sqlalchemy.md).
