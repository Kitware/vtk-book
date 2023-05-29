# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import date

project = "VTK Book"
copyright = f"1993-{date.today().year}, VTK Book Authors and Contributors"
author = "VTK Book Authors and Contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "myst_parser",
]

myst_enable_extensions = [
    "amsmath",
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
