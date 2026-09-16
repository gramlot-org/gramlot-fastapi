# FastAPI POC overview

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/overview.md).

## 1. Status and repositories

This is a POC under review, intended to become a consolidated prerelease after
review. No release date or stable API is promised. `gramlot-poc` is the executable
experimental core; the clean `gramlot` repository defines the constitution and
will contain the first consolidated product. Passing POC tests is evidence, not
acceptance of a port. The adapter candidate is 0.1.0a1; no publication is implied.

The preview evaluates APIs and design choices. Descriptions express intended
behavior; bugs and incomplete cases may exist. The adapter automatically installs
the checksummed experimental core wheel; no matching core source tag is needed.

## 2. Responsibilities

FastAPI supplies server adaptation: requests, routing, invocation and asset delivery.
Database adapters supply backend access and metadata independently of the server.
Django can supply both roles, but the responsibilities remain distinct. Gramlot
owns Python declarations, shared services, transport and reusable browser behavior.

## 3. Trying and maintaining the POC

See [release procedure](release.md) for a checksummed core candidate and clean
wheel installation. Development can use sibling `gramlot-poc`. Plain hosting and
legacy Genropy integration exist; portable database contracts remain under review.
The paired documentation follows [documentation policy](documentation.md).
