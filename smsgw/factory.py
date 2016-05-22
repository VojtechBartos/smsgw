# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
import traceback
from flask import Flask, request
from celery import Celery

from smsgw import settings
from smsgw.core import db, bcrypt, migrate, mail
from smsgw.models import Gammu
from smsgw.lib.utils import register_module, should_be_reported


def create_app():
    # flask app inicialization
    app = Flask("smsgw", static_url_path='')
    app.config.from_object(settings)

    # extensions inicializatioon
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # register resources
    register_module(app, 'resources')

    # TODO(vojta) move it to separate function
    @app.after_request
    def after_request(response):
        """
        """
        from smsgw.tasks.mail import MailTask

        status_code = response.status_code
        if app.config['LOGGING'] and status_code >= 400:
            black_list = app.config['LOGGING_EMAIL_BLACKLIST']
            endpoint = request.url_rule.endpoint if request.url_rule else None
            if should_be_reported(black_list, status_code, endpoint):
                kwargs = {
                    'environ': request.environ if request.environ else {},
                    'lcls': {
                        'Response payload': response.get_data(),
                        'Traceback': traceback.format_exc()
                    }
                }
                if status_code >= 500:
                    MailTask.send_error(**kwargs)
                else:
                    MailTask.send_debug(**kwargs)

        return response


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
