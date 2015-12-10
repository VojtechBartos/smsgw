# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import SentItem
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.error.api import ErrorResource
from smsgw.core import db


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
        app = kwargs.get('application')
        messages = SentItem.get(user_id=user.id,
                                application_id=app.id if app else None)

        return response(messages)


    @route('/users/<uuid:user_uuid>/sent/<uuid:sentitem>/', methods=['DELETE'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/sent/<uuid:sentitem>/',
           methods=['DELETE'])
    @decorators.auth()
    def delete(self, sentitem, **kwargs):
        """
        Delete sent message
        """
        user = kwargs.get('user')
        app = kwargs.get('application')

        SentItem.remove(uuid=sentitem,
                        user_id=user.id,
                        application_id=app.id if app else None)

        db.session.commit()

        return response({
            'uuid': sentitem
        })
