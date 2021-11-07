#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "iqbalabd"
SITENAME = "The Fortunate"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "en"
THEME = "themes/pelican-bootstrap3"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("LaLoka Labs", "https://lalokalabs.co/"),
    ("GetOTP, the OTP API", "https://otp.dev/"),
)

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/iqbalabd"),
    ("github", "https://github.com/iqbalabd"),
    ("twitter", "https://twitter.com/iqbalabd"),
)

DEFAULT_PAGINATION = 4

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "i18n_subsites",
]

# i18n settings
I18N_UNTRANSLATED_PAGES = "hide"
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    "ja": {
        "SITENAME": SITENAME,
        "STATIC_PATHS": STATIC_PATHS,
        "THEME": THEME,
    },
    "en": {
        "SITENAME": SITENAME,
        "STATIC_PATHS": STATIC_PATHS,
        "THEME": THEME,
    },
    #    'ms': {
    #        'SITENAME': "Yang Bertuah",
    #        'STATIC_PATHS': STATIC_PATHS,
    #        'THEME': THEME,
    #    },
}

MENUITEMS = (
    #    ('Xoxzo Inc. Blog', 'https://blog.xoxzo.com/author/iqbal-abdullah.html'),
)

# pelican-bootstrap3 template variables
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
TAG_CLOUD_MAX_ITEMS = 10

DISQUS_SITENAME = "the-fortunate"
DISQUS_DISPLAY_COUNTS = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
