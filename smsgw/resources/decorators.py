# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import re
import jsonschema
from functools import update_wrapper
from flask import request, abort


def jsonschema_validate(payload=None, **options):
    """
    Apply json validation on payload or function arguments
    :param payload: {dict|list} payload response
    :param options: {dict} of function parameters
    """
    def decorator(fn):
        def wrapped_function(*args, **kwargs):
            # validate request payload
            if payload:
                jsonschema.validate(request.json, schema=payload)

            # validate arguments
            for key, schema in options.iteritems():
                argument = kwargs.get(key)
                if argument:
                    jsonschema.validate(argument, schema=schema)

            return fn(*args, **kwargs)
        return update_wrapper(wrapped_function, fn)
    return decorator
