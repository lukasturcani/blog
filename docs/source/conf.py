# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import pathlib
import sys

conf_directory = pathlib.Path(__file__).parent
sys.path.append(str(conf_directory / "_extensions"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "blog"
copyright = "2023, Lukas Turcani"
author = "Lukas Turcani"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ["bevy_sim"]

templates_path = [str(conf_directory / "_templates")]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = "Lukas Turcani Blog"
html_static_path = [str(conf_directory / "_static")]
