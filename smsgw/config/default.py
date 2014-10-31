# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
import multiprocessing


class Default(object):
    """ Default config """

    WORKERS = multiprocessing.cpu_count() * 2 + 1

    DEBUG = False
    LOGGING = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = None
    STATIC_FOLDER = os.path.join('static')
    SECRET_KEY = os.urandom(24)