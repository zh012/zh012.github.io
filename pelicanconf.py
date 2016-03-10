#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'zh012'
SITENAME = 'zh012'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

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
SOCIAL = (('linkedin', 'https://ca.linkedin.com/in/zh012'),
          ('github', 'https://github.com/zh012'),)

PLUGIN_PATHS = ['plugins', 'plugins/pelican-gist']
PLUGINS = ['liquid_tags.notebook', 'render_math', 'pelican_gist']

NOTEBOOK_EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
MATH_JAX = {'tex_extensions': ['color.js', 'mhchem.js']}

THEME = 'themes/clean-blog'
COLOR_SCHEME_CSS = 'github.css'
GITHUB_URL = 'http://github.com/zh012'
LINKEDIN_URL = 'https://ca.linkedin.com/in/zh012'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = ['images']
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
