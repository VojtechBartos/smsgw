# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import uuid
import pytz
import random
import string
import importlib
from flask import jsonify
from dateutil.parser import parse as dtparse
from smsgw.constants.http_status_codes import STATUS_CODES


def register_module(app, module):
    """
    Registering module on fly
    :param app: {Flask} instance
    :param module: {str} module path
    """
    m = importlib.import_module('%s.%s' % (app.name, module))
    if hasattr(m, 'register'):
        m.register(app)


def get_rabbitmq_uri(**kwargs):
    """
    Helper function to get proper rabbitmq uri
    :param kwargs: {dict} rabbitmq settings
    :return: {string} rabbitmq uri
    """
    return "amqp://{user}:{password}@{host}:5672/{vhost}".format(
        host=kwargs['host'],
        vhost=kwargs['vhost'],
        user=kwargs['user'],
        password=kwargs['password']
    )


def get_sql_alchemy_db_uri(**kwargs):
    """
    Helper function to get proper database uri
    :param kwargs: {dict} db settings
    :return: {string} sql alchemy db uri
    """
    if kwargs.get('driver'):
        kwargs['dialect'] = '{}+{}'.format(kwargs['dialect'], kwargs['driver'])
    uri = '{dialect}://{username}:{password}@{host}:{port}/{database}'

    return uri.format(**kwargs)


def response(payload, status_code=200, message=None):
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
    char = unicode(char)
    # GSM Default 7-bit special character (count as 2 char)
    special = [u'^', u'{', u'}', u'[', u']', u'~', u'|', u'€', u'\\']

    # GSM Default 7-bit character (count as 1 char)
    default = [u'@', u'£', u'$', u'¥', u'è', u'é', u'ù', u'ì', u'ò', u'Ç', u'Ø',
               u'ø', u'Å', u'å', u'Δ', u'_', u'Φ', u'Γ', u'Λ', u'Ω', u'Π', u'Ψ',
               u'Σ', u'Θ', u'Ξ', u'Æ', u'æ', u'É', u'!', u'"', u'#', u'¤', u'%',
               u'&', u'\'', u'(',u')', u'*', u'+', u',', u'-', u'.', u'/', u'0',
               u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u':', u';',
               u'<', u'=', u'>', u'?', u'¡', u'A', u'B', u'C', u'D', u'E', u'F',
               u'G', u'H', u'I', u'J', u'K', u'L', u'M', u'N', u'O', u'P', u'Q',
               u'R', u'S', u'T', u'U', u'V', u'W', u'X', u'Y', u'Z', u'Ñ', u'§',
               u'¿', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j',
               u'k', u'l', u'm', u'n', u'o', u'p', u'q', u'r', u's', u't', u'u',
               u'v', u'w', u'x', u'y', u'z', u'ä', u'ñ', u'à']

    return char in special
