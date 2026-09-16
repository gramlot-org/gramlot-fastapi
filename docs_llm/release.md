# Experimental preview preparation

[Expanded version and commands](../docs/release.md).

## 1. Status and dependency

Unpublished adapter candidate 0.1.0a1; exact core 0.1.5 from Django's GitHub
v0.1.0-preview.1. SHA-256:
`63466802618c8cbd3fed0a83e1072556085a31bd522477dbcfe1122417a26f4a`.
POC, not consolidated product; wheel consumption needs no editable checkout/Node.

## 2. Build and verify

Run check.py, build and strict Twine; install core+adapter wheels in clean Python
3.11+ venv, add HTTPX for verification only. verify_installation.py runs isolated
outside checkouts: Python page, recipe, nested prebuilt assets, CLI, no Genropy.
CI: Python 3.11/3.12 × Linux/Windows/macOS. Candidate helper enforces exact version,
URL/hash provenance; HTTPS wheel override requires both inputs. Browser visual and
real Genropy acceptance remain separate checks. See expanded commands and Windows path.

## 3. Manual distribution gate

Review commit/tag and remote CI; publish verified wheel/sdist plus SHA256SUMS.
GitHub prerelease may pair exact core wheel with adapter, as Django does. Record
core provenance/hash and adapter commit; never replace same-version core silently.
Add real tag-based install command after assets/tag exist. No automatic publication.
PyPI/visibility are separate owner actions; currently use local wheels or siblings.

## 4. Architecture limits

Server/DB roles independent. No forced migration for packaging; SQLite belongs in
core/POC, temporary legacy location tolerated. Shared DB contract and consolidated
core remain separate reviewed work.
