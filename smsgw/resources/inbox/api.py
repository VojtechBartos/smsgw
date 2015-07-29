# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import Inbox, User
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.extensions import db


class InboxResource(FlaskView):
    """ Inbox endpoints """

    route_base ='/'

    @route('/users/<uuid:user_uuid>/inbox/', methods=['GET'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/inbox/',
           methods=['GET'])
    @decorators.auth()
    def index(self, **kwargs):
        """
        Returning list items in inbox
        """
        user = kwargs.get('user')
        app = kwargs.get('application')

        # make query
        query = app.inbox if app else user.inbox
        query = query.order_by(Inbox.received.desc())

        return response([message.to_dict() for message in query.all()])


    @route('/users/<uuid:user_uuid>/inbox/<uuid:inbox_uuid>/', methods=['DELETE'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/inbox/<uuid:inbox_uuid>/',
           methods=['DELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete user contact
        """
        inbox = kwargs.get('inbox')
        db.session.delete(inbox)
        db.session.commit()

        return response(inbox.to_dict())
