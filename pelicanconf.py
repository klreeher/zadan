#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# About Site
AUTHOR = 'Ziya Adan'
SITENAME = 'Ziya Adan'
SITEURL = ''

PATH = 'content' # where the content lives
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ziya_adan'),
         ('Instagram', 'https://twitter.com/ziya_adan/following'),
         ('GoodReads', 'https://twitter.com/ziya_adan/following'),)

DEFAULT_PAGINATION = 10


# plugins and plugin config

PLUGIN_PATHS = ['/pelican/pelican-plugins']
PLUGINS = ['better_figures_and_images', 'i18n_subsites']

RESPONSIVE_IMAGES = True # better fig and img

# themes and config

THEME_PATHS = ['/pelican/pelican-themes/']
THEME = (''.join(THEME_PATHS)+('pelican-bootstrap3'))

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']} # this is for bootstrap3
BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

ABOUT_ME = 'WRITER OF ROMANCES, BREAKER OF HEARTS'
AVATAR = 'images/avi.jpg'
TWITTER_USERNAME = 'ziya_adan'
TWITTER_CARDS = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
