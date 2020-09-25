Installation
============

Install the package, and add it to your ``requirements.txt``:

.. code-block:: text

    pip install sphinx-library

Next, edit the ``conf.py`` file in your Sphinx project to use the Library theme:

.. code-block:: python

    # conf.py
    html_theme = "library"

Also set the appropriate sidebars in your ``conf.py`` file. Library comes with
a few to enable various navigation elements in the sidebar; add, remove, or
reorder them as you see fit:

.. code-block:: python

    # conf.py
    html_sidebars = {
        "**": [
            "about.html",         # Project name, description, etc.
            "searchbox.html",     # Search.
            "extralinks.html",    # Links specified in theme options.
            "globaltoc.html",     # Global table of contents.
            #"localtoc.html",     # Contents of the current page.
            "readingmodes.html",  # Light/sepia/dark color schemes.
            "sponsors.html",      # Fancy sponsor links.
        ]
    }

Additional sidebars are built-in to Sphinx. See `html_sidebars documentation
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars>`_.

Finally, it is important to specify the language of your documentation. This is
not only an HTML best practice --- it also enables additional typographic
features of the theme, such as the ability to automatically hyphenate words
when wrapping lines (just like a printed book).

.. code-block:: python

    # conf.py
    language = "en"
