# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime, timedelta

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import User
from smsgw.lib.utils import response
from smsgw.resources.decorators import jsonschema_validate
from smsgw.resources.users.schemas import post
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class UsersResource(FlaskView):
    """ Users endpoints """

    route_base = '/users/'

    def index(self):
        """
        """
        return response({'data': True})

    @jsonschema_validate(payload=post.schema)
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
