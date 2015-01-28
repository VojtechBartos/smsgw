# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import re
from copy import deepcopy
import jsonschema
from functools import update_wrapper
from flask import request, abort
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from smsgw.extensions import db
from smsgw.models import User, UserToken, Template, Contact, Tag, Application


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

def auth(role=User.ROLE_USER):
    """
    Authentification decorator
    :param role: {str} user role
    """

    def decorator(fn):

        routing = {
            'user': User,
            'template': Template,
            'contact': Contact,
            'tag': Tag,
            'application': Application
        }

        def unauthorized():
            abort(401)

        def forbidden():
            abort(403)

        def not_found():
            abort(404)

        def wrapped_function(*args, **kwargs):
            # get authorization content
            authorization = request.headers.get('Authorization')
            if authorization is None:
                unauthorized()

            # get token by regex from authorization header
            token = None
            token_search = re.search('Token\ ([a-zA-Z0-9\-]{36})', authorization)
            if token_search:
                token = token_search.group(1)
            if token is None:
                unauthorized()

            try:
                # find user by token
                user = UserToken.query \
                        .filter_by(token=token) \
                        .one() \
                        .user
            except (NoResultFound, MultipleResultsFound):
                unauthorized()

            # checking role
            if not user.is_admin() and user.role != role and user.isActive:
                forbidden()

            # saving user instance to request
            request.user = user

            # TODO(vojta)
            updates = {}
            for key, value in kwargs.iteritems():
                if hasattr(value, 'replace'):
                    value = value.replace('@me', user.uuid)
                name = key.split('_')
                if len(name) > 1:
                    route, field = name
                    if route == 'user' and value == user.uuid:
                        updates['user'] = user
                    elif route in routing:
                        try:
                            filter_by = {}
                            filter_by[field] = value
                            updates[route] = routing[route].query \
                                                .filter_by(**filter_by) \
                                                .one()
                        except (NoResultFound, MultipleResultsFound):
                            not_found()
            kwargs.update(updates)

            # if requested user is not logged in, he needs to be 
            # user with admin role or will be sent 403
            requested_user = kwargs.get('user')
            if requested_user is not None:
                if request.user.uuid != requested_user.uuid:
                    if request.user.role is not User.ROLE_ADMIN:
                        forbidden()

            return fn(*args, **kwargs)
        return update_wrapper(wrapped_function, fn)
    return decorator
