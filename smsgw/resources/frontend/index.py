# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import render_template
from flask.ext.classy import FlaskView, route

class IndexResource(FlaskView):
    """ Index resource for frontend """

    route_base = '/'

    @route('/')
    def index(self):
        """
        """

        return render_template('index.html')
