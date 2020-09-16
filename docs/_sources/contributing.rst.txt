Contributing
============

Clone from the git repo at: https://github.com/vsalvino/sphinx-library.

Create a virtual environment and install the dev dependencies:

.. code-block:: console

    $ pip install -r requirements-dev.txt

All theme styling is done via SCSS, which is compiled into CSS before publishing
the package. Do not edit the theme's CSS files directly.

Pygments styling is handled directly in ``sphinx_library.themes``. These themes
generate SCSS files which are then compiled into CSS files and included with
the theme.

The ``build.py`` script handles all of the SCSS compilation, and also builds the
project documentation.

.. code-block:: console

    $ python build.py

Docs hosting is handled by GitHub pages, so the source RST files are in
``docs-source`` and the built HTML output is in ``docs/``. Due to the nature of
GitHub pages the built HTML should be committed whenever it changes.

Finally, to build a package and upload to PyPI:

.. code-block:: console

    $ python setup.py sdist bdist_wheel
    $ twine upload dist/*
