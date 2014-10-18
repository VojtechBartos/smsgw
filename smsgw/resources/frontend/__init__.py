# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.resources.frontend.index import IndexResource

def register(app, prefix=None):
    """
    :param app: {Flask} flask app instance
    """
    IndexResource.register(app, route_prefix=prefix)
    