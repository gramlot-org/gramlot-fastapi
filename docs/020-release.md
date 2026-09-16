# Experimental preview preparation

Document ID: **GF-020**.

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/020-release.md).

<a id="1-status-and-dependency"></a>
<a id="gf-020-005"></a>

## 005 · Status and dependency

Block ID: **GF-020-005**.

The FastAPI candidate is **0.1.0a1**, pinned to **gramlot 0.1.5**. It is a POC,
not the forthcoming consolidated product. The source preview is installable from this repository on `main`;
no tagged FastAPI wheel or PyPI release is claimed. The matching core wheel is already distributed in Django's
`v0.1.0-preview.1` GitHub release. Its SHA-256 is
`63466802618c8cbd3fed0a83e1072556085a31bd522477dbcfe1122417a26f4a`.
The adapter declares that URL and checksum as a direct dependency, so normal pip
installation resolves it automatically. Version 0.1.5 identifies this wheel's
experimental snapshot; it does not require a matching core source release.
No editable checkout or Node.js is needed. Described behavior is intended behavior;
these previews may contain bugs and exist to evaluate APIs and design choices.

<a id="2-build-and-verify"></a>
<a id="gf-020-010"></a>

## 010 · Build and verify

Block ID: **GF-020-010**.

Run `python scripts/check.py`, `python -m build`, and
`python -m twine check --strict dist/*` in the prepared development environment.
Then create a separate Python 3.11+ environment:

```sh
python -m venv temp/consumer
temp/consumer/bin/python -m pip install \
  'https://github.com/gramlot-org/gramlot-django/releases/download/v0.1.0-preview.1/gramlot-0.1.5-py3-none-any.whl#sha256=63466802618c8cbd3fed0a83e1072556085a31bd522477dbcfe1122417a26f4a' \
  dist/gramlot_fastapi-0.1.0a1-py3-none-any.whl httpx
python scripts/verify_installation.py --python temp/consumer/bin/python
```

On Windows use `temp/consumer/Scripts/python.exe`. HTTPX is for the verification
client, not a runtime dependency of ordinary applications. The probe runs outside
checkouts with isolated imports; it verifies a Python-authored page, recipe,
prebuilt runtime delivery at a nested prefix, CLI and plain hosting without Genropy.
CI tests Python 3.11/3.12 on Linux, Windows and macOS using packages, with no sibling
checkout. `install_core_candidate.py` validates the exact core version and provenance;
its optional HTTPS URL and SHA-256 inputs must be supplied together. Browser visual
verification and real legacy Genropy installation are separate acceptance checks.

<a id="3-manual-distribution-gate"></a>
<a id="gf-020-015"></a>

## 015 · Manual distribution gate

Block ID: **GF-020-015**.

Review the adapter changes and choose the release commit/tag; run remote CI and
publish only the verified wheel and sdist with SHA256SUMS. A GitHub prerelease can
carry the exact compatible core wheel beside the adapter, following Django's
preview model. Record core provenance, checksums and adapter commit in release notes;
do not silently rebuild or replace a core wheel with different contents at the
same version. Add the concrete tag-based pip installation command only once the
tag and assets exist. No automatic publishing workflow is added here.
PyPI publication and repository visibility changes are separate owner actions.
Until then install the source preview from main or use locally verified wheels.
The adapter repository and core release assets are public; anonymous downloads are supported.

<a id="4-architecture-limits"></a>
<a id="gf-020-020"></a>

## 020 · Architecture limits

Block ID: **GF-020-020**.

Server and database adapters are independent responsibilities. Preview packaging
must not force a database migration. SQLite belongs to Gramlot/gramlot-poc; any
temporary legacy placement is tolerated. The shared database contract and eventual
consolidated core release remain separate reviewed work.
