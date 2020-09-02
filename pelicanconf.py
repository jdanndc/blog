#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Team Mikinaak'
SITENAME = 'Our Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# https://rasor.github.io/using-pelican-themes.html
#THEME = '/Users/jdann/dev/pelican/pelican-themes/franticworld'
#THEME = '/Users/jdann/dev/pelican/pelican-themes/gum'
#THEME = '/Users/jdann/dev/pelican/pelican-other-themes/minimalX'
DISPLAY_CATEGORIES_ON_MENU = True
#STATIC_PATHS = ['img', 'static']
#FAVICON = 'img/favicon.ico'
#CUSTOM_CSS = 'static/custom.css'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

USE_FOLDER_AS_CATEGORY = 'True'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
