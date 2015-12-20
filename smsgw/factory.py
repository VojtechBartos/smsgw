# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
from flask import Flask
from celery import Celery

from . import config
from .core import db, bcrypt, migrate, mail
from .models import Gammu
from .lib.utils import register_module


def create_app(name='smsgw'):
    """
    :param name: {str} name of package app
    """
    # flask app inicialization
    app = Flask(name, static_url_path='')
    app.config.from_object(config)

    # extensions inicializatioon
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # register resources
    register_module(app, 'resources')

    return app


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super(ContextTask, self).__call__(*args, **kwargs)

    celery.Task = ContextTask
    return celery
