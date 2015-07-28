# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView

from smsgw.models import Phone, User
from smsgw.lib.utils import response
from smsgw.resources import decorators
# from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class PhonesResource(FlaskView):
    """ Phones endpoints """

    route_base = '/phones/'

    @decorators.auth(User.ROLE_ADMIN)
    def index(self, **kwargs):
        """
        Returning list of active phones
        """
        return response([phone.to_dict() for phone in Phone.query.all()])
