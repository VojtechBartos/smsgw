# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import Inbox, User
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.error.api import ErrorResource
from smsgw.core import db


class InboxResource(FlaskView):
    """ Inbox endpoints """

    route_base ='/'

    @route('/inbox/', methods=['GET'])
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
        query = None

        if user is None:
            query = Inbox.query
            if not request.user.is_admin():
                raise ErrorResource(
                    message='Not have permissions.',
                    status_code=403
                )
        else:
            query = app.inbox if app else user.inbox

        messages = query.order_by(Inbox.received.desc()).all()

        return response([message.to_dict() for message in messages])


    @route('/inbox/<uuid:inbox_uuid>/', methods=['DELETE'])
    @route('/users/<uuid:user_uuid>/inbox/<uuid:inbox_uuid>/', methods=['DELETE'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/inbox/<uuid:inbox_uuid>/',
           methods=['DELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete user contact
        """
        user = kwargs.get('user', request.user)
        inbox = kwargs.get('inbox')

        # admin check, to be sure that non admin users can delete inboxes
        if inbox.userId != user.id and not user.is_admin():
            raise ErrorResource(message='Not have permissions.', status_code=403)

        db.session.delete(inbox)
        db.session.commit()

        return response(inbox.to_dict())
