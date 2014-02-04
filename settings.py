# -*- coding: utf-8 -*-
AUTHOR = u'Florent Lebreton (fle)'
SITENAME = u"Florent Lebreton @ /home/fle"
SITEURL = 'http://fle.github.io'

PATH = 'sources/'
OUTPUT_PATH = 'www/'

THEME = "/home/florent/dev/perso/pelican/pelican-simplegrey"

TIMEZONE = 'Europe/Paris'

LINKS = (
    ('Makina Corpus', 'http://makina-corpus.com/blog'),
    ('Planet Django', 'http://planetdjango.org'),
)

SOCIAL = (
    ('linkedin', 'http://www.linkedin.com/pub/florent-lebreton/30/4a8/7a'),
    ('twitter', 'https://twitter.com/__fle__'),
    ('google', 'https://plus.google.com/114836609462836450047'),
    ('github', 'https://github.com/fle')
)

PAGE_DIR = 'pages'

STATIC_PATHS = (['images', 'documents'])

DEFAULT_PAGINATION = 3

GOOGLE_ANALYTICS = 'UA-18281356-9'

PELICAN_SIMPLEGREY_FIXED_SIDEBAR = True