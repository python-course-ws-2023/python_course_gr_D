# Configuration file for the Sphinx documentation builder.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../example"))
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Retail analysis'
copyright = '2024, Emona Bakalova, Mariia Hrechyn, Alican Ohkay'
author = 'Emona Bakalova, Mariia Hrechyn, Alican Ohkay'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",     # Support automatic documentation
    "sphinx.ext.coverage",    # Automatically check if functions are documented
    "sphinx.ext.mathjax",     # Allow support for algebra
    "sphinx.ext.viewcode",    # Include the source code in documentation
    "numpydoc",               # Support NumPy style docstrings
    "sphinx.ext.autosummary", # Generates function/method/attribute summary lists
    "sphinx.ext.napoleon",    # Enables Sphinx to parse both NumPy and Google style docstrings
    "myst_nb",                # For compiling Jupyter Notebooks into high quality documentation formats
]

templates_path = ['_templates']
exclude_patterns = []

language = 'english'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
