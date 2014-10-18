# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import uuid


def underscore_to_camelcase(value):
    """
    Transformation string from underscore to camelcase
    :param value: {str} underscored string
    :return: {str} camelcased string
    """
    def camelcase(): 
        yield str.lower
        while True:
            yield str.capitalize
    c = camelcase()
    value = "".join(c.next()(x) if x else '_' for x in value.split("_"))
    return value[0].upper() + value[1:]

def generate_uuid():
    """
    Generate new uuid
    :return: {string} uuid
    """
    return str(uuid.uuid4())
