# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import api
import frontend

def register(app):
    """
    :param app: {Flask} flask app instance
    """
    # register API resources
    api.register(app, prefix='api/1.0')
    # register frontend resources
    frontend.register(app)
