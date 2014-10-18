# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime, timedelta
import jsonschema

from flask import request, current_app
from flask.ext.classy import FlaskView, route


class UsersResource(FlaskView):
    """ Users endpoint """

    route_base = '/users/'

    def index(self):
        """
        """

        return 'ahoj'
