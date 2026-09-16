# Copyright 2026 Softwell S.r.l. - SPDX-License-Identifier: Apache-2.0
"""Build the guides without installing FastAPI or the experimental core."""
from pathlib import Path
import os
import tomllib

project = "Gramlot FastAPI"
author = "Genropy Team"
copyright = "2026, Softwell S.r.l."
release = tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())["project"]["version"]
version = release
language = "en"
extensions = ["myst_parser"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", ".DS_Store"]
nitpicky = True
html_theme = "furo"
html_title = f"Gramlot FastAPI {release} — POC documentation"
html_logo = "_static/gramlot-logo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "announcement": "Experimental POC — APIs and examples are being reviewed and consolidated.",
    "light_css_variables": {
        "color-brand-primary": "#1643c5",
        "color-brand-content": "#1643c5",
        "color-sidebar-background": "#f5f7fc",
    },
    "dark_css_variables": {
        "color-sidebar-background": "#161a24",
        "color-brand-primary": "#ffcc43",
        "color-brand-content": "#8fb2ff",
    },
}
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
