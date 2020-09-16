Sample Element Styles
=====================

This document provides a sampling of commonly used reStructuredText directives
and elements for testing out and viewing the theme.

See the full `reStructuredText Markup Specification
<https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_.


Ligatures & Kerning
-------------------

Ligatures and kerning: field, fjord, The, Taft, past, act, Quick, waffle, oooh,
aaah.


Admonitions
-----------

.. attention::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. caution::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. danger::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. error::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. hint::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. important::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. note::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. tip::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. warning::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.


Asides
------

Epigraph:

.. epigraph::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

    -- Julius Caesar

Highlights:

.. highlights::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

Pull quote:

.. pull-quote::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

    -- Julius Caesar

Quote:

    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo."

    -- Julius Caesar

Sidebar:

.. sidebar:: Optional title
    :subtitle: Optional subtitle

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

Topic:

.. topic:: Required title

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.


Source Code
-----------

Lorem ``ipsum`` dolor ``sit amet``, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.

.. code-block:: python

    from docutils.readers import standalone

    class SphinxBaseReader(standalone.Reader):
    """
    A base class of readers for Sphinx.
    This replaces reporter by Sphinx's on generating document.
    """

    transforms = []  # type: List[Type[Transform]]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        from sphinx.application import Sphinx
        if len(args) > 0 and isinstance(args[0], Sphinx):
            self._app = args[0]
            self._env = self._app.env
            args = args[1:]

        super().__init__(*args, **kwargs)

    @property
    def app(self) -> "Sphinx":
        warnings.warn('SphinxBaseReader.app is deprecated.',
                      RemovedInSphinx40Warning, stacklevel=2)
        return self._app

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.


Images
------

Images, C/O https://placeholder.com/.

Image:

.. image:: https://via.placeholder.com/300.png?text=Placeholder

Figure:

.. figure:: https://via.placeholder.com/300.png?text=Placeholder
   :alt: Placeholder

   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
   tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
   quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.


Tables
------

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====


Headings: Heading 2 Lorem Ipsum Dolor sit Amet Consectetur Adipiscing
---------------------------------------------------------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

Laoreet id donec ultrices tincidunt. Nulla aliquet porttitor lacus luctus
accumsan tortor posuere. Nibh ipsum consequat nisl vel pretium lectus quam.
Morbi tempus iaculis urna id volutpat lacus laoreet. Mi ipsum faucibus vitae
aliquet nec ullamcorper. Nisl tincidunt eget nullam non nisi est sit amet. Ac ut
consequat semper viverra nam libero justo.

* **Laoreet id donec** --- Laoreet id donec ultrices tincidunt.

* **Nulla aliquet porttitor** --- Nulla aliquet porttitor lacus luctus accumsan
  tortor posuere. Odio ut sem nulla pharetra diam sit. Ac ut consequat semper
  viverra nam libero justo. Aliquet sagittis id consectetur purus.

  * Convallis aenean et tortor at.

  * Sit amet consectetur adipiscing elit ut aliquam purus sit.

  * Varius morbi enim nunc faucibus a pellentesque.

* **Nisl tincidunt eget** --- Nisl tincidunt eget nullam non nisi est sit amet.

Orci eu lobortis elementum nibh tellus. Etiam sit amet nisl purus in mollis nunc
sed. Convallis aenean et tortor at. Sit amet consectetur adipiscing elit ut
aliquam purus sit. Varius morbi enim nunc faucibus a pellentesque sit amet
porttitor.

Heading 3 Porttitor Rhoncus Dolor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Porttitor rhoncus dolor purus non enim praesent elementum facilisis. Molestie
nunc non blandit massa enim. Tempor id eu nisl nunc mi ipsum faucibus vitae.
Ornare arcu dui vivamus arcu felis. Augue lacus viverra vitae congue eu
consequat ac felis. Sit amet dictum sit amet justo donec enim diam. Augue lacus
viverra vitae congue eu consequat.

#. **Laoreet id donec** --- Laoreet id donec ultrices tincidunt.

#. **Nulla aliquet porttitor** --- Nulla aliquet porttitor lacus luctus accumsan
   tortor posuere. Odio ut sem nulla pharetra diam sit. Ac ut consequat semper
   viverra nam libero justo. Aliquet sagittis id consectetur purus.

   #. Convallis aenean et tortor at.

   #. Sit amet consectetur adipiscing elit ut aliquam purus sit.

   #. Varius morbi enim nunc faucibus a pellentesque.

#. **Nisl tincidunt eget** --- Nisl tincidunt eget nullam non nisi est sit amet.

Heading 4 Velit Scelerisque in Dictum
'''''''''''''''''''''''''''''''''''''

Velit scelerisque in dictum non consectetur a. Vulputate ut pharetra sit amet
aliquam. Justo laoreet sit amet cursus sit amet dictum sit. Aliquam eleifend mi
in nulla posuere sollicitudin. Enim nulla aliquet porttitor lacus luctus
accumsan tortor.

Heading 5 Purus ut Faucibus Pulvinar
""""""""""""""""""""""""""""""""""""

Purus ut faucibus pulvinar elementum integer enim neque volutpat ac. Vitae et
leo duis ut. Leo urna molestie at elementum. Ipsum nunc aliquet bibendum enim
facilisis. Sit amet cursus sit amet. Dolor magna eget est lorem ipsum dolor sit.

Heading 6 Nunc id Cursus Metus Aliquam
**************************************

Nunc id cursus metus aliquam eleifend mi in. Egestas tellus rutrum tellus
pellentesque eu tincidunt tortor aliquam. Tellus in hac habitasse platea
dictumst vestibulum rhoncus est. Volutpat commodo sed egestas egestas fringilla.
