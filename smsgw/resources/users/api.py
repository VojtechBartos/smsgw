# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime, timedelta

from flask import request
from flask.ext.classy import FlaskView, route

from sqlalchemy.exc import IntegrityError

from smsgw.models import User, UserForgotPassword
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.users.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class UsersResource(FlaskView):
    """ Users endpoints """

    route_base = '/users/'

    @decorators.auth(User.ROLE_ADMIN)
    def index(self, **kwargs):
        """
        Getting list of all users, only with admin privileges
        """
        return response([user.to_dict() for user in User.query.all()])

    @route('/<uuid:user_uuid>/', methods=['GET'])
    @decorators.auth()
    def get(self, user, **kwargs):
        """
        Getting user by uuid
        """
        return response(user.to_dict())

    @decorators.jsonschema_validate(post.schema)
    def post(self):
        """
        Creating new user
        """
        data = request.json

        # check existence of user by email
        if User.is_exists_by_email(data['email']):
            raise ErrorResource(409, message="Email already exits.")

        # create user
        user = User(**data)
        db.session.add(user)
        db.session.commit()

        return response(user.to_dict(), status_code=201)

    @route('/reset-password/', methods=['POST'])
    @route('/reset-password/<uuid:token>/', methods=['POST'])
    def resetPassword(self, token=None, **kwargs):
        """
        Reseting user password
        """
        # get data from payload
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # user
        payload = None
        message = None
        user = None
        if email is not None:
            # find user
            user = User.get_one(email=email)
            if user is None:
                raise ErrorResource(404, message="Invalid email address.")

            # delete all existing tokens
            UserForgotPassword.query.filter_by(userId=user.id).delete()

            # create new token
            expired = datetime.utcnow() + timedelta(minutes=30)
            forgot_password = UserForgotPassword(userId=user.id,
                                                 expired=expired)
            db.session.add(forgot_password)
            db.session.commit()

            # send email
            from smsgw.tasks.mail import MailTask
            MailTask().apply_async(**{
                'kwargs': {
                    'to': [user.email],
                    'template': 'mail/forgotten_password',
                    'params': {
                        'first_name': user.firstName,
                        'last_name': user.lastName,
                        'token': forgot_password.token
                    }
                }
            })

            # set up payload
            message = "On your email has been sent link for change passowrd."

        elif token is not None and password is not None:
            # find request for user password
            forgot_password = UserForgotPassword.get_one(token=token)
            if forgot_password is None:
                raise ErrorResource(404, message="Invalid token.")

            # update password
            user = forgot_password.user
            user.password = password

            # delete token
            db.session.remove(forgot_password)
            db.session.commit()

            # set up payload
            message = "Your passsword has been successfuly changed."

        else:
            # we dont have email, token or password, so we are not
            # able to reset password
            raise ErrorResource(400, message="Not able to reset password.")

        return response(payload, message=message)


    @route('/<uuid:user_uuid>/', methods=['PUT'])
    @decorators.auth()
    @decorators.jsonschema_validate(put.schema)
    def put(self, user, **kwargs):
        """
        Updating exiting user
        """
        try:
            # save to db
            user.update(request.json)
            db.session.commit()
        except IntegrityError, e:
            db.session.rollback()
            raise ErrorResource(409, message="Email already exits.")

        return response(user.to_dict())

    @route('/<uuid:user_uuid>/', methods=['DELETE'])
    @decorators.auth(User.ROLE_ADMIN)
    def delete(self, user, **kwargs):
        """
        Delete user
        """
        db.session.delete(user)
        db.session.commit()

        return response(user.to_dict())
