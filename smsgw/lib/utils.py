# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import uuid
from flask import jsonify
from smsgw.constants.http_status_codes import STATUS_CODES


def response(payload, status_code=200, message='OK.'):
    """

    :param payload: {list|dict|str} response payload
    :param status_code: {int} http response status code
    :param message: {str} string message
    """
    # check validity of status code
    if status_code not in STATUS_CODES:
        raise Exception('Status code does not exist.')

    res = {
        'meta': {
            'code': status_code,
            'message': STATUS_CODES[status_code] if not message else message
        },
        'data': payload
    }
    return jsonify(res), status_code


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
