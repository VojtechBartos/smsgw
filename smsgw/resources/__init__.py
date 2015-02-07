# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
import glob
import importlib
from flask import render_template, current_app, request
from smsgw.lib.utils import underscore_to_camelcase
from smsgw.resources.users.api import UsersResource
from smsgw.resources.auth.api import AuthResource
from smsgw.resources import converters


def register(app):
    """
    Registration of resources modules
    :param app: {Flask} flask app instance
    """

    # register converters
    converters.register(app)

    @app.route('/')
    def index():
        """ Frontend handler, rendering index.html """
        params = {
            'title': "SMS gateway"
        }

        return render_template('index.html', **params)

    # API resources registration
    directory = os.path.dirname(os.path.realpath(__file__))
    resources = [os.path.basename(os.path.normpath(i)) \
                 for i in glob.glob(os.path.join(directory, '*/'))]
    for resource in resources:
        module = "{0}.{1}.api".format(__name__, resource)
        class_name = "{0}Resource".format(underscore_to_camelcase(resource))
        try:
            class_ref = getattr(__import__(module, fromlist=[class_name]),
                        class_name)
            class_ref.register(app, route_prefix='api/1.0')
        except ImportError, e:
            print "Resource '{0}' does not exists".format(module)
        except AttributeError as e:
            print "Resource class '{0}' does not exists".format(class_name)
