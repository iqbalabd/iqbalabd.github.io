AUTHOR = "Iqbal Abdullah"
SITENAME = "Iqbal's Weblog"
SITEURL = ""

OUTPUT_PATH = "output"
PATH = "content"

TIMEZONE = "Asia/Tokyo"


# ARTICLE_URL = "{lang}/{slug}/"
# ARTICLE_SAVE_AS = "{lang}/{slug}.html"
# PAGE_URL = "{lang}/{slug}/"

# PAGE_URL = "pages/{slug}/" # For some reason, this doesn't work on GitHub
# PAGE_SAVE_AS = "pages/{slug}.html"
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("LaLoka Labs", "https://lalokalabs.co/"),
    ("GetOTP", "https://otp.dev/"),
    ("Kafkai", "https://kafkai.com/"),
)

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/iqbalabd"),
    ("github", "https://github.com/iqbalabd"),
    ("twitter", "https://twitter.com/iqbalabd"),
)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "i18n_subsites",
]
THEME = "themes/tuxlite_zf"

# i18n settings
DEFAULT_LANG = "en"
I18N_UNTRANSLATED_PAGES = "hide"
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    "en": {
        "SITENAME": SITENAME,
        "STATIC_PATHS": STATIC_PATHS,
        "THEME": THEME,
    },
    "ja": {
        "SITENAME": SITENAME,
        "STATIC_PATHS": STATIC_PATHS,
        "THEME": THEME,
    },
    "ms": {
        "SITENAME": SITENAME,
        "STATIC_PATHS": STATIC_PATHS,
        "THEME": THEME,
    },
}
