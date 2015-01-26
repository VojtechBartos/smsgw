# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime, timedelta

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import User
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.users.schemas import post
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class UsersResource(FlaskView):
    """ Users endpoints """

    route_base = '/users/'

    @decorators.auth(User.ROLE_ADMIN)
    def index(self, **kwargs):
        """
        """
        # find all users
        users = User.query.all()

        # send payload
        res_keys = ["uuid", "email", "firstName", "lastName", "company"]
        payload = [user.to_dict(res_keys) for user in users]
        return response(payload)

    @route('/<uuid:user_uuid>/', methods=['GET'])
    @decorators.auth()
    def get(self, user, **kwargs):
        """
        """
        # send payload
        res_keys = ["uuid", "email", "firstName", "lastName", "company"]
        payload = user.to_dict(properties=res_keys)
        return response(payload)

    @decorators.jsonschema_validate(payload=post.schema)
    def post(self):
        """
        """
        data = request.json

        # check existence of user by email
        if User.is_exists_by_email(data['email']):
            raise ErrorResource(
                409, 
                message="Email '{0}' is already exits.".format(data['email'])
            )

        # create user
        user = User(**data)
        db.session.add(user)
        db.session.commit()

        # send payload
        res_keys = ["uuid", "email", "firstName", "lastName", "company"]
        payload = user.to_dict(properties=res_keys)
        return response(payload, status_code=201)
