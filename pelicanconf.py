#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'drinkingkazu'
SITEURL = 'https://deeplearnphysics.org/Blog'
#SITEURL = '' # uncomment this line for local dev
SITENAME = 'DeepLearnPhysics Blog'
SITETITLE = 'DeepLearnPhysics Blog'
SITESUBTITLE = 'subtitle'
SITEDESCRIPTION = 'description!'
#SITELOGO = SITEURL + '/images/profile.png'
#FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR='#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
    }
COPYRIGHT_YEAR = 2017

MAIN_MENU = True
MENUITEMS = (('Home','index.html'),
	('Category','categories.html'),
	('Archives','archives.html'),
	('Tags','tags.html'))

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Theme
THEME = 'theme'

# Plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['keyboard.kb','render_math','ipynb.markup']

# Scripts
SCRIPTS = ['https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js','main.js']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About Group', 'http://deeplearnphysics.org'),)

# Social widget
SOCIAL = (('home','https://deeplearnphysics.org'),
          ('github','https://github.com/DeepLearnPhysics'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
