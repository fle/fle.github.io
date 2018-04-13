# -*- coding: utf-8 -*-
AUTHOR = u'Florent Lebreton (fle)'
SITENAME = u"Florent Lebreton"
SITEURL = 'https://fle.github.io'

PATH = 'sources/'
OUTPUT_PATH = 'www/'

TIMEZONE = 'Europe/Paris'

LINKS = (
    ('Makina Corpus', 'http://makina-corpus.com/blog'),
    ('Planet Django', 'http://planetdjango.org'),
    ('Python Nantes community', 'http://nantes.afpy.org'),
    ('Planet Django', 'http://planetdjango.org'),
    ('Regliero\'s blog', 'http://regilero.github.io'),
)

SOCIAL = (
    ('linkedin', 'http://www.linkedin.com/in/florentlebreton'),
    ('twitter', 'https://twitter.com/__fle__'),
    ('google', 'https://plus.google.com/114836609462836450047'),
    ('github', 'https://github.com/fle')
)

PAGE_PATHS = ['pages']

STATIC_PATHS = ['images', 'documents']

#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = 5

GOOGLE_ANALYTICS = 'UA-18281356-9'

DISQUS_SITENAME = 'flegithubio'

PELICAN_SOBER_STICKY_SIDEBAR = False
PELICAN_SOBER_ABOUT = "<img src=\"/images/avatar.jpg\" alt=\"Florent Lebreton\" class=\"avatar\" /><br />Software engineer and trainer &bullet; Technical head at j360.info &bullet; Python, Django and GIT addict &bullet; Dance, sail, take photos. <a href=\"/pages/about-me.html\">more</a>"
PELICAN_SOBER_TWITTER_CARD_CREATOR = '__fle__'
PELICAN_SOBER_TWITTER_CARD_SITE = '__fle__'
PELICAN_SOBER_HOME_LISTS_ARTICLES = True
