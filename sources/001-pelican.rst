Generate a weblog with pelican
##############################

:date: 2011-01-16
:tags: pelican
:category: geek
:author: Florent Lebreton (fle)

I'm testing pelican, a static blog generator written in python. From simple rst or markdown files (your blog entries), pelican can produce a nice blog with just a cli-tool command. Sources can be managed with your favourite DVCS and final site is easily hosted on any web server.

It seems to be nice so I try this tool, discover at he same time reStructuredText and blog it on the fly!

1 - Start with install pelican from pypi:

.. code-block:: console

        $ easy_install pelican

Note : Pelican has `some dependancies`_ so it could be better to install it in virtualenv.

2 - Simply create a minimal filesystem:

.. code-block:: console

        blog/sources       -- to store blog entry .rst files
        blog/www           -- final web site directory
        blog/settings.py   -- settings file

3 - Just edit settings.py to add general settings like title, author, URL and other stuff. Mine is very simple for now:
        
.. code-block:: python

        # -*- coding: utf-8 -*-
        AUTHOR = u'Florent Lebreton (fle)'
        SITENAME = u"/home/fle"
        SITEURL = 'http://blog.fle.org'

        PDF_GENERATOR = False

        LINKS = (('planet django', 'http://planetdjango.org'),)

        SOCIAL = (('viadeo', 'http://www.viadeo.com/fr/profile/florent.lebreton'),)
 
4 - Then, write my first blog entry in sources/01-test.rst:

.. code-block:: rst

        Hello world
        ###########

        :date: 2011-01-16
        :tags: test, pelican
        :category: python
        :author: Florent Lebreton (fle)

        Hello !

5 - Finally, just run the cli-tool like this:

.. code-block:: console

        $ cd blog
        $ pelican -s settings.py -o www/ sources/


Pelican manages syndication, PDF generation, theming and other cool stuff. Take a look at `Pelican page`_ for more information.

.. _`some dependancies`: http://docs.notmyidea.org/alexis/pelican/getting_started.html#dependencies
.. _`Pelican page`: http://alexis.notmyidea.org/pelican/

