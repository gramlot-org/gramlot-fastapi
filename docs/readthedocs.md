# Building and hosting the documentation

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/readthedocs.md).

## 1. Sphinx and the Gramlot theme

The documentation uses Sphinx, MyST for Markdown, and Furo with Gramlot's logo
and light/dark palette. The POC notice appears on every page. The guides build
without installing FastAPI, Gramlot or this adapter; the version is read from
`pyproject.toml`, not from an installed package.

```sh
python -m venv .venv-docs
# Activate .venv-docs using your platform's usual command.
python -m pip install -r docs/requirements.txt
python -m sphinx -n -W --keep-going -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` to preview the result. Warning and unresolved
reference failures block the build. Requirements are shared by local builds,
the dedicated Documentation workflow and Read the Docs.

## 2. Continuous integration

`.github/workflows/docs.yml` builds on pushes to main/develop/codex branches,
pull requests targeting main/develop, and manual dispatch. It installs only the
documentation dependencies and uploads `documentation-html` as a downloadable
Actions artifact. The regular repository checks also build the documentation.
This workflow verifies HTML; it does not itself publish a documentation website.

## 3. Read the Docs setup

The repository is ready through `.readthedocs.yaml`: Ubuntu 24.04, Python 3.12,
`docs/requirements.txt`, `docs/conf.py`, and warnings treated as errors.
An authorized maintainer must import the GitHub repository into Read the
Docs, select `main` as the default branch, enable the desired versions, and
verify the GitHub webhook and first build.

External account/project setup is separate from these committed files. A live
Read the Docs site is not claimed until the project is connected and a build
succeeds. `READTHEDOCS_CANONICAL_URL` supplies the canonical URL when hosted.

## 4. Paired documentation and maintenance

Follow [the documentation policy](documentation.md). Expanded and concise guides
remain paired; detailed guides without mirrors are identified there. POC history
is separated from the installation and integration navigation. Keep theme
requirements in `pyproject.toml` and `docs/requirements.txt` aligned.

References: [Read the Docs configuration](https://docs.readthedocs.com/platform/stable/config-file/v2.html)
and [Furo customization](https://pradyunsg.me/furo/customisation/).
