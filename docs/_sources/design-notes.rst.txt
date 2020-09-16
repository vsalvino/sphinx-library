Design Notes
============

While bold colors, shadows, "materials", and heavy syntax highlighting are "in"
right now, there is something to be said for the simplicity of a black-and-white
printed book. Even programming books are somehow highly legible despite the lack
of colors and UI chrome that adorn our editors.

How can it be that a black and white book is equally or sometimes more legible
than a richly formatted web page? This theme is partly a personal project to
explore that question.

My answer is the use of whitespace and good typography.


Use of Whitespace
-----------------

The theme was initially laid out to mimic metrics commonly used in a small
paperback or hardback novel. This means a relatively small page size and
surprisingly ample margin on all sides of the page. In order to better simulate
a "page", or focused area of content, the sidebar and non-content areas have
been dimmed slightly but not so much as to be distracting. This helps to create
a "page" rather than a sea of white.

The second use of whitespace is in the type itself --- in between the lines.
Line and paragraph spacing is ample. The goal is not to cram too much within the
focus area (we have an infinite amount of web page so there is no point trying
to cram dozens of lines together).


Use of Color
------------

Choosing fonts featuring interesting italics enabled a unique way to implement
admonitions, quotes, etc. using only type and white space --- no colors, boxes,
or borders. This practice also aligns with the simple look of the printed page.

While highly saturated syntax highlighting of code snippets is often sought out
by developers, this theme takes the opposite approach instead using muted drab
colors sparingly. Syntax highlighting does aid readability in longer code
snippets, so it shouldn't necessarily be disabled. I think the muted colors
strike a good balance between readability without being distracting. Thanks to
the Trac project for providing inspiration based on their color scheme included
with Pygments.

If you find that you prefer candy-colored syntax highlighting and color-coded
admonitions, then this theme is certainly not for you.


Ligatures, Kerning, Punctuation
-------------------------------

Special care has been taken to configure the theme to maximize use of the
typeface's features. This includes enabling automatic hyphenation at line breaks
to keep the flow and rhythm of the text moving and enabling both common and
contextual ligatures using the browser's font rendering abilities. Both of these
are common in print, but for some reason have been mostly forgotten in the
electronic realm.

Sphinx also excellently converts punctuation such as "smart quotes", en-- and
em--- dashes, etc. The browser additionally allows finely controlling the
underline using OpenType features --- so we can create faint underlines which
become bolder upon hover, and underlines that leave space around descenders to
create an appearance more pleasing to the eye.



Choosing the Typefaces
----------------------

The specific typefaces chosen have been vetted among hundreds of freely
available alternatives, each selected for being the highest performing across
many areas including: legibility, metrics, kerning abilities, ligatures,
contrast between weights, quality of italics, and general appearance.

Special care has been taken to ensure the ``-native`` stacks look equally good
on Windows, macOS, and various GNU/Linux distributions. Often times this means
at least a dozen fallbacks are specified to match up to all sorts of conditions
including which applications are installed (MS Office, LibreOffice, Gnome, KDE),
common font packages (Bitstream, URW, Ghostscript, GNU fonts), and even distro
specifics such as the branded Ubuntu or Red Hat fonts.


Typeface Notes
--------------

**Academy** --- "Computer Modern" is the gold standard here, and frankly a
beautiful typeface. In order to facilitate this I have created a `web font
version <https://github.com/vsalvino/computer-modern>`_ distributed via
jsDeliver CDN.  "Computer Modern Typewriter" is used for monospace needs as it
has a uniquely ornate appearance despite being a fixed width type. The fallback
and native version uses a similar modernist (early 20th-century) typeface,
Century (and various similar fallbacks).

**Book** --- "Crimson Pro" was the font that opened the rabbit hole. Many
characteristics of this type make it totally reminiscent of a printed book.
After all, it was quite literally designed to be an on-screen font for textbooks
and editorial content. "Courier Prime", a fantastic rendition of Courier with
script-like italics, is used for monospace needs. The native version uses
Georgia (or Georgia Pro, a *much* nicer version of Georgia included with Windows
10) which provide a similar reading experience.

**Engineer** --- "IBM Plex Serif" provides a really unique cross between a
traditional serif and a slab serif, which makes for a more practical alternative
to the flowery Computer Modern, without losing the air of formality.
Corresponding "IBM Plex Mono" is used for monospace needs. Cambria and Charter
are used for the fallback and native version as they both have a sturdy upright
appearance with clean cut serifs.

**Humanist** --- "Fira Sans" was selected due to its unique but very legible
appearance. Softer alternatives such as Source Sans Pro were considered, but
Fira Sans has a slightly darker weight which helps it look good even on
low-resolution low-contrast screens. I think its unique glyphs nicely accentuate
the "human" part of "humanist". Corresponding "Fira Mono" is used for monospace
needs. The fallback and native version uses Trebuchet MS due to it being a
web-safe font, and also having a similar dark weight with good legibility.

**Swiss** --- "Inter" is an excellent choice here, due to its clear inspiration
from Helvetica, but actually made more legible thanks to its wider characters
and looser spacing. "Robot Mono" is used for monospace needs as it has a
similarly geometric appearance. Fallbacks and native version ranges from
Helvetica Neue, Arial Nova (a *much* nicer version of Arial included with
Windows 10), Roboto, and Nimbus Sans (a forgotten but quite good Helvetica
alternative which is commonly available in various GNU/Linux operating systems).
