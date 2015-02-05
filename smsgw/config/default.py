# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
import multiprocessing
from kombu import Queue


class Default(object):
    """ Default config """

    WORKERS = multiprocessing.cpu_count() * 2 + 1

    DEBUG = False
    LOGGING = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = None
    STATIC_FOLDER = os.path.join('static')
    SECRET_KEY = os.urandom(24)

    # CELERY
    CELERY_IMPORTS = ("smsgw.tasks.callback", "smsgw.tasks.mail")
    CELERY_TIMEZONE = 'UTC'
    CELERY_BROKER_URL = "amqp://"
    CELERY_RESULT_BACKEND = "amqp"
    CELERY_QUEUES = (Queue('callbacks', routing_key='callbacks'), 
                     Queue('mails', routing_key='mails'))
    CELERYBEAT_SCHEDULE = None
    CELERYD_POOL_RESTARTS = True
