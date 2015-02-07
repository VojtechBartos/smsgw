# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from copy import deepcopy
from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import Outbox
from smsgw.lib.utils import response
from smsgw.resources import decorators
# from smsgw.resources.users.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class OutboxResource(FlaskView):
    """ Outbox endpoints """

    route_base = '/users/<uuid:user_uuid>/outbox/'

    @decorators.auth()
    def index(self, **kwargs):
        """
        Getting list of outbox messages
        """
        user = kwargs.get('user')

        return response([message.to_dict() for message in user.outbox.all()])


    @route('/<int:outbox_id>/', methods=['DELETE'])
    @decorators.auth()
    def delete(self, outbox, **kwargs):
        """
        Delete outbox message
        """        
        paylod = deepcopy(outbox.to_dict())
        db.session.delete(outbox)
        db.session.commit()

        return response(paylod)
