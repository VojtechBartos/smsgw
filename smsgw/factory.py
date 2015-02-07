# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
from flask import Flask
from celery import Celery

from smsgw import resources
from smsgw.extensions import db, bcrypt, migrate, mail
from smsgw.config import environments


def create_app(name='smsgw', env=None):
    """
    :param name: {str} name of package app
    """
    if env is None:
        env = os.environ.get('SMSGW_ENV') or 'development'

    # flask app inicialization
    app = Flask(name, static_url_path='')
    app.config.from_object(environments[env])

    # extensions inicializatioon
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # register resources
    resources.register(app)

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
