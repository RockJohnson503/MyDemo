# encoding: utf-8
# flake8: NOQA

"""
File: develop.py
Author: Rock Johnson
"""
from .base import *


DEBUG = True

INSTALLED_APPS.extend([
    'debug_toolbar',
])

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = ['127.0.0.1']
