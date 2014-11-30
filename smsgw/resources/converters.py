# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.uuid import UUIDConverter


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
