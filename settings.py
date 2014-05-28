# -*- coding: utf-8 -*-
AUTHOR = u'Florent Lebreton (fle)'
SITENAME = u"Florent Lebreton"
SITEURL = 'http://fle.github.io'

PATH = 'sources/'
OUTPUT_PATH = 'www/'

TIMEZONE = 'Europe/Paris'

LINKS = (
    ('Makina Corpus', 'http://makina-corpus.com/blog'),
    ('Planet Django', 'http://planetdjango.org'),
    ('Regliero\'s blog', 'http://regilero.github.io'),
)

SOCIAL = (
    ('linkedin', 'http://www.linkedin.com/in/florentlebreton'),
    ('twitter', 'https://twitter.com/__fle__'),
    ('google', 'https://plus.google.com/114836609462836450047'),
    ('github', 'https://github.com/fle')
)

PAGE_DIR = 'pages'

STATIC_PATHS = ['images', 'documents']

#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = 5

GOOGLE_ANALYTICS = 'UA-18281356-9'

DISQUS_SITENAME = 'flegithubio'

PELICAN_SOBER_STICKY_SIDEBAR = True
PELICAN_SOBER_ABOUT = "Software engineer and trainer at Makina Corpus Nantes. Python, Django and GIT addict. Dance, sail, take photos."
PELICAN_SOBER_TWITTER_CARD_CREATOR = '__fle__'
PELICAN_SOBER_TWITTER_CARD_SITE = '__fle__'
