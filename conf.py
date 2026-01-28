# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OER Educazione Aperta<br>Studiare le mafie'
copyright = '2025, Educazione Aperta'
author = 'Educazione Aperta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.bibtex',
]

# Configurazione bibliografia
bibtex_bibfiles = ['riferimenti.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'it'

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
 
html_theme_options = {
    # Link al repository
    'vcs_pageview_mode': 'view',  # o 'edit' se vuoi il link per editare
    
    # Altri link utili nella sidebar destra
    'display_version': True,  # Mostra la versione
    'prev_next_buttons_location': 'bottom',  # Posizione dei bottoni prev/next
    
    # Altre opzioni di navigazione
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Configura il repository (necessario per i link)
html_context = {
    'display_github': True,  # Per GitHub
    'github_user': 'educazioneaperta',
    'github_repo': 'oermafia',
    'github_version': 'main',  # o 'master'
    'conf_py_path': '/docs/',  # percorso del conf.py nel repo
}

# 1. Impostazioni del logo
html_logo = None


# 2. Rimuovi la scritta accanto al logo
html_theme_options = {
    'logo_only': False,
    'display_version': False,
}

# 3. UNICA funzione setup (unifica CSS e JS qui)
def setup(app):
    app.add_css_file('custom.css')


