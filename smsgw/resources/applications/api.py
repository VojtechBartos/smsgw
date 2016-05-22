# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from sqlalchemy.exc import IntegrityError

from smsgw.models import Application
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.applications.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.core import db


class ApplicationsResource(FlaskView):
    """ Applications endpoints """

    route_base = '/users/<uuid:user_uuid>/applications/'

    @decorators.auth()
    def index(self, **kwargs):
        """
        Returning list of applications for specific user
        """
        user = kwargs.get('user')
        applications = user.applications.order_by(Application.label.asc()).all()

        return response([app.to_dict() for app in applications])


    @route('/<uuid:application_uuid>/')
    @decorators.auth()
    def get(self, **kwargs):
        """
        Get user application
        """
        application = kwargs.get('application')
        return response(application.to_dict())


    @decorators.auth()
    @decorators.jsonschema_validate(post.schema)
    def post(self, **kwargs):
        """
        Creating new user application
        """
        try:
            # create and save application
            user = kwargs.get('user')
            application = Application(**request.json)
            application.userId = user.id
            db.session.add(application)
            db.session.commit()
        except IntegrityError, e:
            db.session.rollback()
            raise ErrorResource(409, message="Prefix is already exists.")

        return response(application.to_dict(), status_code=201)


    @route('/<uuid:application_uuid>/', methods=['PUT'])
    @decorators.auth()
    @decorators.jsonschema_validate(put.schema)
    def put(self, **kwargs):
        """
        Updateing existing application
        """
        try:
            application = kwargs.get('application')
            application.update(request.json)
            db.session.commit()
        except IntegrityError, e:
            db.session.rollback()
            raise ErrorResource(409, message="Prefix is already exists.")

        return response(application.to_dict())


    @route('/<uuid:application_uuid>/regenerate/', methods=['PUT'])
    @decorators.auth()
    def regenerate(self, **kwargs):
        """
        Regenerate API token
        """
        application = kwargs.get('application')
        application.regenerate_token()
        db.session.commit()

        return response(application.to_dict(['uuid', 'token']))


    @route('/<uuid:application_uuid>/', methods=['DELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete user application
        """
        application = kwargs.get('application')

        # delete template
        db.session.delete(application)
        db.session.commit()

        return response(application.to_dict())
