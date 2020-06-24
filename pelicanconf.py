#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'iqbalabd'
SITENAME = 'The Fortunate'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'
THEME = 'themes/blue-penguin'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (
            ('linkedin', 'https://www.linkedin.com/in/iqbalabd'),
            ('github', 'https://github.com/iqbalabd'),
            ('twitter', 'https://twitter.com/iqbalabd'),
         )

DEFAULT_PAGINATION = 1

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', ]

# i18n settings
I18N_UNTRANSLATED_PAGES = 'hide'
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'ja': {
        'SITENAME': SITENAME,
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
    },
    'en': {
        'SITENAME': SITENAME,
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
    },

#    'ms': {
#        'SITENAME': "Yang Bertuah",
#        'STATIC_PATHS': STATIC_PATHS,
#        'THEME': THEME,
#    },

}

# blue-penguin template variables
# provided as examples, they make clean urls. used by MENU_INTERNAL_PAGES.
TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags/index.html'
AUTHORS_URL = 'authors'
AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

MENUITEMS = (
    ('Xoxzo Inc. Blog', 'https://blog.xoxzo.com/author/iqbal-abdullah.html'),
)

DISQUS_SITENAME = 'the-fortunate'
DISQUS_DISPLAY_COUNTS = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
