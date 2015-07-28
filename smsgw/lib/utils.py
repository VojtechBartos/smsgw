# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import uuid
import pytz
import random
import string
from flask import jsonify
from dateutil.parser import parse as dtparse
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


def random_string(length=6):
    """
    Generate random string from ASCII characters and digits
    :param lentgh: {str} length of random string
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(length))


def str_to_datetime(string, timezone=pytz.utc):
    """
    Convert string to datetime.datetime
    :param string: {str} datetime in string
    :param timezone: {pytz.timezone}
    :return: {datetime.datetime} datetime
    """
    dt = dtparse(string)

    return timezone.localize(dt) if dt is not None else None


def is_special_char(char):
    """
    TODO(vojta) diacriticts and etc
    :param char: {str}
    """
    char = str(char)
    # GSM Default 7-bit special character (count as 2 char)
    special = ['^', '{', '}', '[', ']', '~', '|', '€', '\\']

    # GSM Default 7-bit character (count as 1 char)
    default = ['@', '£', '$', '¥', 'è', 'é', 'ù', 'ì', 'ò', 'Ç', 'Ø', 'ø', 'Å',
               'å', 'Δ', '_', 'Φ', 'Γ', 'Λ', 'Ω', 'Π', 'Ψ', 'Σ', 'Θ', 'Ξ', 'Æ',
               'æ', 'É', '!', '"', '#', '¤', '%', '&', '\'', '(',')', '*', '+',
               ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
               '9', ':', ';', '<', '=', '>', '?', '¡', 'A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ñ', '§', '¿', 'a', 'b',
               'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ñ',
               'à']

    return char in special
