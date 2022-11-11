#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DeepLearnPhysics'
GITHUBURL = 'https://github.com/DeepLearnPhysics'
CONTACT = 'mailto:contact@deeplearnphysics.org'
GROUPURL = 'https://deeplearnphysics.org'
TWITTERURL = 'https://twitter.com/dlphysics'
DATAURL = GROUPURL + '/DataChallenge'

SITENAME = 'DeepLearnPhysics Blog'
SITETITLE = 'Blog'
SITESUBTITLE = 'DeepLearnPhysics Group'
SITEDESCRIPTION = 'description!'
SITELOGO = 'profile.png'
SITEURL = GROUPURL + '/Blog'
#SITEURL = '' # uncomment this line for local dev
#FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR='#333'
ROBOTS = 'index, follow'

STATIC_PATHS=['img','tutorials']

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
	('Tags','tags.html'),
	('Authors','authors.html'))

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Theme
THEME = 'theme'

# Custom CSS
CUSTOM_CSS = ['kazunotebook.css']

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
#LINKS = (('About Group', 'http://deeplearnphysics.org'),)

# Social widget
SOCIAL = (('home','http://deeplearnphysics.org'),
		  ('twitter',TWITTERURL),
          ('github',GITHUBURL))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disable default ipython notebook css
#IPYNB_IGNORE_CSS = True
IPYNB_USE_META_SUMMARY=True
