# Getting started

The FastAPI preview candidate is not published yet. Its exact Gramlot 0.1.5
core wheel is available from the Django GitHub preview; see the
[wheel installation and verification procedure](release.md). For development
from sibling source checkouts, install both editable packages:

```sh
python -m pip install -e ../gramlot-poc
python -m pip install -e .
```

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
