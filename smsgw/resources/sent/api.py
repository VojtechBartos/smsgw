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

    route_base = '/'

    @route('/users/<uuid:user_uuid>/sent/', methods=['GET'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/sent/',
           methods=['GET'])
    @decorators.auth()
    def index(self, **kwargs):
        """
        Returning list of sent items
        """
        user = kwargs.get('user')
        application = kwargs.get('application')
        messages = SentItem.get_grouped(
            user_id=user.id,
            application_id=application.id if application else None
        )

        return response(messages)


    @route('/users/<uuid:user_uuid>/sent/<int:sentitem_id>/', methods=['GELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete sent message
        """
        sent_item = kwargs.get('sentitem')
        db.session.delete(sent_item)
        db.session.commit()

        return response(sent_item.to_dict())
