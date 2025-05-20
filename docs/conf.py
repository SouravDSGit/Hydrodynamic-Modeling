# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Hydrodynamic Modeling'
copyright = '2025, Sourav Mukherjee'
author = 'Sourav Mukherjee, Earth Scientist'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',              # Markdown support
    'sphinxcontrib.mermaid',    # Mermaid diagrams
    'sphinx_copybutton',        # Copy button for code blocks
    'sphinx_design',            # Cards, grids, badges
    'sphinx.ext.intersphinx',   # Cross-reference other docs
    'sphinx.ext.viewcode',      # Add source code links
]

# MyST configuration
myst_enable_extensions = [
    'colon_fence',      # ::: fences
    'deflist',          # Definition lists
    'html_image',       # HTML images
    'linkify',          # Auto-link URLs
    'replacements',     # Smart quotes
    'smartquotes',      # Smart quotes
    'substitution',     # Variable substitution
    'tasklist',         # Task lists
]

myst_heading_anchors = 3  # Generate anchors for h1-h3

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'

html_theme_options = {
    'repository_url': 'https://github.com/SouravDSGit/Hydrodynamic-Modeling',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_download_button': True,
    'launch_buttons': {},  # Optional, can be removed
    'show_toc_level': 2,
    'navigation_with_keys': True,
}
html_context = {
    "display_github": True,
    "github_user": "SouravDSGit",
    "github_repo": "Hydrodynamic-Modeling",
    "github_version": "main",
    "conf_py_path": "/docs/",  # adjust if your conf.py is in root
}
# Static files
# Uncomment and create files if needed:
# html_static_path = ['_static']
# html_css_files = ['custom.css']  # Optional custom CSS
# html_favicon = '_static/favicon.ico'  # Optional

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# -- Mermaid configuration ---------------------------------------------------
mermaid_version = 'latest'
mermaid_init_js = """
mermaid.initialize({
    startOnLoad: true,
    theme: 'neutral'
});
"""