"""Sphinx configuration."""
project = "Hypermodern Python Waxc"
author = "Manchi L."
copyright = "2024, Manchi L."
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
