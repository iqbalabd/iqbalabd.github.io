#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'iqbalabd'
SITENAME = 'The Fortunate | A blog by Iqbal Abdullah'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
            ('linkedin', 'https://www.linkedin.com/in/iqbalabd'),
            ('github', 'https://github.com/iqbalabd'),
            ('twitter', 'https://twitter.com/iqbalabd'),
         )

DEFAULT_PAGINATION = 3

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', ]

I18N_UNTRANSLATED_PAGES = 'hide'
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'ja': {
        'SITENAME': 'ザ・フォチャネット',
        'STATIC_PATHS': STATIC_PATHS,
    },
    'en': {
        'SITENAME': SITENAME,
        'STATIC_PATHS': STATIC_PATHS,
    },
}


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
