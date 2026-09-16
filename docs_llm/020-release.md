# Experimental preview preparation

Document ID: **GF-020**.

[Expanded version and commands](../docs/020-release.md).

<a id="1-status-and-dependency"></a>
<a id="gf-020-005"></a>

## 005 · Status and dependency

Block ID: **GF-020-005**.

Unpublished adapter candidate 0.1.0a1; exact core 0.1.5 from Django's GitHub
v0.1.0-preview.1. SHA-256:
`63466802618c8cbd3fed0a83e1072556085a31bd522477dbcfe1122417a26f4a`.
POC, not consolidated product; wheel consumption needs no editable checkout/Node.

<a id="2-build-and-verify"></a>
<a id="gf-020-010"></a>

## 010 · Build and verify

Block ID: **GF-020-010**.

Run check.py, build and strict Twine; install core+adapter wheels in clean Python
3.11+ venv, add HTTPX for verification only. verify_installation.py runs isolated
outside checkouts: Python page, recipe, nested prebuilt assets, CLI, no Genropy.
CI: Python 3.11/3.12 × Linux/Windows/macOS. Candidate helper enforces exact version,
URL/hash provenance; HTTPS wheel override requires both inputs. Browser visual and
real Genropy acceptance remain separate checks. See expanded commands and Windows path.

<a id="3-manual-distribution-gate"></a>
<a id="gf-020-015"></a>

## 015 · Manual distribution gate

Block ID: **GF-020-015**.

Review commit/tag and remote CI; publish verified wheel/sdist plus SHA256SUMS.
GitHub prerelease may pair exact core wheel with adapter, as Django does. Record
core provenance/hash and adapter commit; never replace same-version core silently.
Add real tag-based install command after assets/tag exist. No automatic publication.
PyPI/visibility are separate owner actions; currently use local wheels or siblings.

<a id="4-architecture-limits"></a>
<a id="gf-020-020"></a>

## 020 · Architecture limits

Block ID: **GF-020-020**.

Server/DB roles independent. No forced migration for packaging; SQLite belongs in
core/POC, temporary legacy location tolerated. Shared DB contract and consolidated
core remain separate reviewed work.

The main source preview declares the checksummed core wheel directly: pip fetches
it automatically. Version 0.1.5 denotes that POC wheel, not a required source tag.
The adapter and core assets are public; anonymous downloads are supported. Preview descriptions are
intended behavior, with bugs possible; no FastAPI wheel release or PyPI release is claimed.
