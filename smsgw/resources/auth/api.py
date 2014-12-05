# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime, timedelta

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import User, UserToken
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.auth.schemas import login
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class AuthResource(FlaskView):
    """ Auth endpoint """

    route_base = '/auth/'

    @route('/login/', methods=['POST'])
    @decorators.jsonschema_validate(payload=login.schema)
    def login(self):
        """
        """
        # TODO(vojta) save success login, improve token stuff
        data = request.json

        # find user by email and if is not existing or passwd
        # is incorect will raise error 403
        user = User.query.filter_by(email=data['email']).first()
        if user is None or user.compare_password(data['password']) is False:
            raise ErrorResource(
                403, 
                message="Invalid password or email."
            )

        # non active users are not allowed
        if user.isActive is False:
            raise ErrorResource(403, message="Account is not active.")

        # create user token for user
        token = None
        agent = request.headers.get('User-Agent')
        print request.headers
        if agent is not None:
            token = UserToken.query \
                        .filter_by(userId=user.id) \
                        .filter_by(agent=agent) \
                        .first()
        if token is None:
            token = UserToken(userId=user.id, agent=agent)
            db.session.add(token)
            db.session.commit()

        # create payload response
        payload = {
            'token': token.token,
            'email': user.email
        }
        return response(payload, status_code=200)
