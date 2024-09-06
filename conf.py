# SPDX-FileCopyrightText: Copyright 2023 VTK Book Authors and Contributors
# SPDX-License-Identifier: Apache-2.0

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import date

project = "VTK Book"
copyright = f"2006-{date.today().year}, VTK Book Authors and Contributors"
author = "VTK Book Authors and Contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# Define the canonical URL if you are using a custom domain on Read the Docs
import os
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "myst_parser",
]

myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "dollarmath",  # support latex equation inside $ $
    "linkify",  # convert bare links to hyperlinks
]
myst_heading_anchors = 7

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "README.md",
    "VTKBook/Figures/README.md",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/Kitware/vtk-book",
    "use_repository_button": True,
}
html_title = "VTK Book"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]
