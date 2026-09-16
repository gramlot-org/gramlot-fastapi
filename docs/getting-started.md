# Getting started

This preview evaluates APIs and design choices; bugs and incomplete behavior are
expected. In a Python 3.11+ virtual environment, install the adapter from GitHub:

```sh
python -m pip install 'git+https://github.com/gramlot-org/gramlot-fastapi.git@main'
```

Git and access to this repository are required. The dependency declaration fetches
the checksummed experimental Gramlot 0.1.5 wheel automatically. No core source tag,
sibling checkout or Node.js is required. The version names a packaged POC snapshot,
not a consolidated release in the clean `gramlot` repository.

For a minimal example, create `pages/hello.py`:

```python
from gramlot.page import WebPage

class Page(WebPage):
    def main(self, root):
        root.h1("Hello from Gramlot")
```

Run `gramlot-fastapi serve .` and open `http://127.0.0.1:8000/page/hello/`.
See [artifact provenance](release.md) and the [inspector guide](inspector.md).

Create an application directory containing `pages/`, then run:

```sh
gramlot-fastapi serve /path/to/application
```

From the repository root:

```sh
uv sync --extra dev --extra docs
uv run python scripts/check.py
uv run python -m build
```

The public namespace is `gramlot_fastapi`. Plain hosting has no database dependency.
Import `gramlot_fastapi.genropy` only for a host backed by an initialized Genropy
`GnrApp`; that legacy dependency must be installed by the application environment.
