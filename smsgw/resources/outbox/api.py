# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from copy import deepcopy
from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import Outbox
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.outbox.schemas import post
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


    @decorators.jsonschema_validate(post.schema)
    def post(self):
        """
        Creating new message in outbox
        """
        user = kwargs.get('user')
        message = request.json.get('message')
        phone_number = request.json.get('phoneNumber')
        outbox = Outbox.send(phone_number=phone_number,
                             message=message)
        
        return response(outbox.to_dict(), status_code=201)


    @route('/<int:outbox_id>/', methods=['DELETE'])
    @decorators.auth()
    def delete(self, outbox, **kwargs):
        """
        Delete outbox message
        """
        payload = deepcopy(outbox.to_dict())
        db.session.delete(outbox)
        db.session.commit()

        return response(payload)
