# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import Phone, User
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.core import db


class PhonesResource(FlaskView):
    """ Phones endpoints """

    route_base = '/phones/'

    @decorators.auth(User.ROLE_ADMIN)
    def index(self, **kwargs):
        """
        Returning list of active phones
        """
        return response([phone.to_dict() for phone in Phone.query.all()])


    @route('/<uuid:phone_uuid>/', methods=['GET'])
    @decorators.auth(User.ROLE_ADMIN)
    def get(self, phone, **kwargs):
        """
        Getting phone by uuid
        """

        return response(phone.to_dict())
