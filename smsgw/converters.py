# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def register(app):
    """
    Registration custom url map converters
    :param app: {Flask} flask app instance
    """
    app.url_map.converters['regex'] = RegexConverter
