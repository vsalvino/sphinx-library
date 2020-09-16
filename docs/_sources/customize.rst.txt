Customization
=============

Sphinx Options
--------------

In addition to theme options (below), some common Sphinx options (set in
``conf.py``) are also respected by the theme. See the full link of `Sphinx
configuration options
<https://www.sphinx-doc.org/en/master/usage/configuration.html>`_.

* **html_logo** --- Path to a logo image which will appear in the sidebar.

* **project** --- The name of your project. It appears in the sidebar and
  elsewhere in the docs.

* **copyright** --- String containing date and/or owner of the project.

* **html_last_updated_fmt** --- If not ``None``, adds a timestamp in the footer.

* **html_show_copyright** --- Show the ``copyright`` field in the footer.

* **html_show_sourcelink** --- Show the ``.rst`` source link in the footer.

* **html_show_sphinx** --- Show "Created using Sphinx" in the footer.


Theme Options
-------------

Options are set in the ``html_theme_options`` variable in ``conf.py``:

.. code-block:: python

    # conf.py
    html_theme_options = {
        "show_breadcrumbs": True,
    }

The following theme options are available:

* **description** --- Short text blurb about your project, to appear under the
  logo or project name.

* **extra_links** --- Dictionary mapping link names to link targets; these
  will be added in the sidebar (if you've set ``extralinks.html`` via the
  ``html_sidebars`` option). This is useful for adding GitHub links, donate
  links, etc. For example:

  .. code-block:: python

      # conf.py
      html_theme_options: {
          "extra_links": {
              "Source Code": "https://github.com/",
          }
      }

* **globaltoc_collapse** --- Boolean to only expand subsections of the current
  document in ``globaltoc.html``. Defaults to True.

* **globaltoc_includehidden** ---- Boolean to show even those subsections in
  ``globaltoc.html`` which have been included with the ``:hidden:``
  flag of the toctree directive. Defaults to True.

* **globaltoc_maxdepth** --- Integer of the maximum depth of the toctree in
  ``globaltoc.html``. Set it to -1 to allow unlimited depth.
  Defaults to the max depth selected in the toctree directive.

* **reading_mode** --- Set the default reading mode color scheme. One of
  ``light``, ``sepia``, or ``dark``. Set to ``None`` to use the browser's
  default styles. Defaults to light.

* **show_breadcrumbs** --- Boolean to show breadcrumb links of ancestors to the
  current document at the top of the page. Defaults to False.

* **show_project_name** --- Set to ``False`` to hide the project name in the
  sidebar.

* **show_version** --- Shows the project version below the logo/name in the
  sidebar.

* **show_relbar_bottom** --- Boolean to show Previous/Next links at the bottom
  of the page. Defaults to True.

* **show_relbar_top** --- Boolean to show Previous/Next links at the top of the
  page. Defaults to False.

* **typography** --- The typeface stack to use throughout the docs. One of the
  following values:

  * academy

  * academy-native

  * book

  * book-native

  * engineer

  * engineer-native

  * humanist

  * humanist-native

  * swiss

  * swiss-native

  For example:

  .. code-block:: python

     # conf.py
     html_theme_options = {
         "typography": "humanist",
     }

  See typography section below for more details.


Typography
----------

Several hand-tuned typography stacks are included to change the feel of your
documentation. Each features carefully selected typeface pairings which have
been balanced with the theme layout to create a book-like reading experience.

* **Book** --- Highly legible type inspired by printed books. The default, and
  good for general purpose use.

* **Humanist** --- Another highly legible type, with a fresh and more casual
  look.

* **Academy** --- An elegant and formal early 20th-century type favored by
  academic publications and legal documents.

* **Engineer** --- A semi-slab-serif type; formal but much cleaner and more
  modern than "academy".

* **Swiss** --- Sans-serif type providing an austere but clean look.

These stacks utilize the Google Fonts and jsDelivr CDN to load web fonts (and
include appropriate fallbacks). Each stack also includes a ``-native`` version,
which does not load any web fonts but instead uses fonts available from the
user's computer. Use this if you seek absolute minimal resource usage or plan to
primarily distribute the HTML offline.

For more details, see :doc:`design-notes`.

To implement your own custom type stack, set the ``typography`` option to
``None`` and then add your own styles following the Custom CSS instructions
below.


Custom CSS
----------

Library's CSS is designed to be easily overridden. This means it avoids complex
queries, and does not specify attributes more than once where possible (e.g.
color, font, font-size, etc. are only set on the ``body`` element, so changing
it once here will affect the whole document).

If you need to modify Library's default CSS styles, you may provide a custom
stylesheet as follows:

* Create a file named ``custom.css`` in your static folder (typically
  named ``_static/``).

* Set the Sphinx option `html_static_path
  <http://www.sphinx-doc.org/en/stable/config.html#confval-html_static_path>`_
  to either that file's path, or the directory it lives within (i.e.
  ``"_static"``).
