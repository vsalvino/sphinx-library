from datetime import datetime


source_suffix = ".rst"
master_doc = "index"

project = "sphinx-library"
year = datetime.now().year
copyright = f"{year} Vince Salvino"

language = "en"

html_theme = "library"

html_sidebars = {
    "**": [
        "about.html",
        "searchbox.html",
        "globaltoc.html",
        "readingmodes.html",
    ]
}

html_theme_options = {
    "description": "The typography-centric Sphinx theme that reads like a good book.",
}
