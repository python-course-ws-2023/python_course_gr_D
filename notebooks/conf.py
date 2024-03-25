import os
import sys
sys.path.insert(0, os.path.abspath('../../functions'))

project = 'My Python Project'
author = 'Your Name'

extensions = [
    'sphinx_rtd_theme',
    'nbsphinx',
    'sphinx.ext.autodoc',
]

html_theme = 'sphinx_rtd_theme'
