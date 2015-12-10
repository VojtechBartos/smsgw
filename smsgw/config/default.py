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
    STATIC_FOLDER = os.path.join('static')
    SECRET_KEY = os.urandom(24)

    # Database
    SQLALCHEMY_DATABASE_URI = None

    # Mail
    # MAIL_SERVER = "localhost"
    # MAIL_PORT = 25
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = False
    # MAIL_USERNAME = None
    # MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "info@vojtechbartos.cz"

    # CELERY
    CELERY_IMPORTS = ("smsgw.tasks.callback", "smsgw.tasks.mail")
    CELERY_TIMEZONE = 'UTC'
    CELERY_BROKER_URL = "amqp://"
    CELERY_RESULT_BACKEND = None
    CELERY_IGNORE_RESULT = True
    CELERY_QUEUES = (Queue('callbacks', routing_key='callbacks'),
                     Queue('mails', routing_key='mails'))
    CELERYBEAT_SCHEDULE = None
    CELERYD_POOL_RESTARTS = True

    # Gammu
    GAMMU_VERSION = os.environ.get('GAMMU_VERSION', "1.34.0")
    GAMMU_DATABASE_VERSION = os.environ.get('GAMMU_DATABASE_VERSION', 14)
