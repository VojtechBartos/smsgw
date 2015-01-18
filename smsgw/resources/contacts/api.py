# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import Contact
from smsgw.lib.utils import response
from smsgw.resources import decorators
# from smsgw.resources.templates.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class ContactsResource(FlaskView):
    """ Contacts endpoints """

    route_base = '/'

    @route('/users/<uuid:user_uuid>/contacts/', methods=['GET'])
    @decorators.auth()
    def index(self, user, **kwargs):
        """

        """
        # if requested user is not logged in, he needs to be 
        # user with admin role or will be sent 403
        if request.user.uuid != user.uuid:
            if request.user.role is not User.ROLE_ADMIN:
                raise ErrorResource(403)

        return response([contact.to_dict() 
                         for contact in user.contacts.all()])

    @route('/users/<uuid:user_uuid>/contacts/<uuid:contact_uuid>/', 
            methods=['GET'])
    @decorators.auth()
    def get(self, user, contact, **kwargs):
        """

        """
        # if requested user is not logged in, he needs to be 
        # user with admin role or will be sent 403
        if request.user.uuid != user.uuid:
            if request.user.role is not User.ROLE_ADMIN:
                raise ErrorResource(403)

        return response(contact.to_dict())