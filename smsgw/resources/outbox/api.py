# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from copy import deepcopy
from flask import request
from flask.ext.classy import FlaskView, route

from smsgw.models import Outbox, Contact, Tag
from smsgw.lib.utils import response, str_to_datetime, random_string
from smsgw.resources import decorators
from smsgw.resources.outbox.schemas import post, external, validate
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class OutboxResource(FlaskView):
    """ Outbox endpoints """

    route_base = '/'

    @route('/users/<uuid:user_uuid>/outbox/', methods=['GET'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/outbox/',
           methods=['GET'])
    @decorators.auth()
    def index(self, **kwargs):
        """
        Getting list of outbox messages
        """
        user = kwargs.get('user')
        app = kwargs.get('application')
        groups = Outbox.get_all(user_id=user.id,
                                application_id=app.id if app else None)

        return response(groups)

    @route('/users/<uuid:user_uuid>/outbox/<string:group>/', methods=['GET'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/outbox/<string:group>/',
           methods=['GET'])
    @decorators.auth()
    def get(self, group, **kwargs):
        """
        Getting outbox group
        """
        user = kwargs.get('user')
        app = kwargs.get('application')
        group = Outbox.get(group=group,
                           user_id=user.id,
                           application_id=app.id if app else None)
        if group is None:
            raise ErrorResource(message='Outbox group not found.',
                                status_code=404)

        return response(group)


    @route('/users/<uuid:user_uuid>/outbox/', methods=['POST'])
    @decorators.auth()
    @decorators.jsonschema_validate(post.schema)
    def post(self, **kwargs):
        """
        Creating new message in outbox
        """
        user = kwargs.get('user')
        data = request.json
        group = random_string(8)
        contacts = []
        tags = []

        # extract data from post payload
        message = data.get('message')
        phone_numbers = data.get('phoneNumbers', [])
        contacts_uuid = data.get('contacts', [])
        tags_uuid = data.get('tags', [])
        send = str_to_datetime(data.get('send'))

        # load contacts
        if contacts_uuid:
            contacts.extend(user.contacts \
                                .filter(Contact.uuid.in_(contacts_uuid)) \
                                .all())

        # load tags and load all contacts for them to on single list
        if tags_uuid:
            tags = user.tags.filter(Tag.uuid.in_(tags_uuid)).all()
            for tag in tags:
                contacts.extend(tag.contacts)

        # extracting phone numbers from contacts
        phone_numbers.extend([contact.phoneNumber for contact in contacts])
        # making contacts and phone numbers uniques, also if there are no
        # numbers we need to trigger error
        phone_numbers = list(set(phone_numbers))
        if len(phone_numbers) == 0:
            raise ErrorResource(
                message='Needs to be provided valid phone number(s)',
                status_code=400
            )

        # add all messages to queue per phone number
        outboxes = []
        for phone_number in phone_numbers:
            # NOTICE(vojta) should not happend, but just in case i should be
            # let known
            if not phone_number:
                raise ErrorResource(
                    message='Needs to be provided valid phone number',
                    status_code=400
                )

            outbox = Outbox.send(
                user_id=user.id,
                group=group,
                destination_number=phone_number,
                message=message,
                send=send
            )
            outboxes.append(outbox)
            db.session.add(outbox)

        db.session.commit()

        return response([outbox.to_dict() for outbox in outboxes],
                        status_code=201)


    @route('/outbox/validate/', methods=['POST'])
    @decorators.jsonschema_validate(validate.schema)
    def validate_phone_number(self, **kwargs):
        """
        Validate phone number
        """
        return response(payload=None, status_code=200)


    @route('/outbox/', methods=['POST'])
    @decorators.auth_external()
    @decorators.jsonschema_validate(external.schema)
    def external(self, application):
        """
        Creating new message in outbox via application token key
        """
        data = request.json

        # put message to queue
        outbox = Outbox.send(
            user_id=application.userId,
            application_id=application.id,
            destination_number=data.get('phoneNumber'),
            message=data.get('message'),
            send=str_to_datetime(data.get('send'))
        )

        return response(outbox.to_dict(), status_code=201)


    @route('/users/<uuid:user_uuid>/outbox/<string:group>/', methods=['DELETE'])
    @route('/users/<uuid:user_uuid>/applications/<uuid:application_uuid>/outbox/<string:group>/',
           methods=['DELETE'])
    @decorators.auth()
    def delete(self, group, **kwargs):
        """
        Delete outbox message
        """
        app = kwargs.get('application')
        app_id = app.id if app else None

        Outbox.query \
              .filter(Outbox.group == group) \
              .filter(Outbox.applicationId == app_id) \
              .delete()
        db.session.commit()

        return response({
            'id': group
        })
