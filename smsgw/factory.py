# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
from flask import Flask
from smsgw import resources

def create_app(name='smsgw', env=None):
    """
    :param name: {str} name of package app
    """
    # override env if its necessary 
    if env is not None: os.environ['SMSGW_ENV'] = env
    
    # flask app inicialization
    app = Flask(name, static_url_path='')
    app.config.from_object('smsgw.config.settings')

    # register resources
    resources.register(app)

    return app


def create_celery_app():
    pass