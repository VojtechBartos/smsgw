# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import SentItem
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class SentResource(FlaskView):
    """ Sent endpoints """

    route_base = '/users/<uuid:user_uuid>/sent/'

    @decorators.auth()
    def index(self, **kwargs):
        """
        Returning list of sent items
        """
        user = kwargs.get('user')

        return response([message.to_dict() for message in user.sent_items.all()])


    @route('/<uuid:sentitem_uuid>/', methods=['DELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete sent message
        """
        sent_item = kwargs.get('sentitem')
        db.session.delete(sent_item)
        db.session.commit()

        return response(sent_item.to_dict())
