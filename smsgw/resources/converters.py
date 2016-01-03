# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.uuid import UUIDConverter
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class MeUUIDConverter(UUIDConverter):
    """ Me or UUID converter """
    def to_python(self, value):
        if value != "@me":
            return super(MeUUIDConverter, self).to_python(value)
        return value



def register(app):
    """
    Registration custom url map converters
    :param app: {Flask} flask app instance
    """
    app.url_map.converters['uuid'] = MeUUIDConverter
    app.url_map.converters['regex'] = RegexConverter
