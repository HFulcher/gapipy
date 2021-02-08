from datetime import date
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


project = "gapipy"
author = "Huw Fulcher"
copyright = f"{date.year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme"
]

html_theme = "sphinx_rtd_theme"
