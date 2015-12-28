# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from sqlalchemy import or_

from smsgw.models import Contact, Tag
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.contacts.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.core import db


class ContactsResource(FlaskView):
    """ Contacts endpoints """

    route_base = '/users/<uuid:user_uuid>/contacts/'

    @decorators.auth()
    def index(self, **kwargs):
        """
        Returning list of contacts for specific user
        """
        user = kwargs.get('user')

        # search or not
        search = request.args.get('search')
        contacts = user.contacts
        if search is not None:
            like = "%{0}%".format(search)
            contacts = contacts.filter(or_(Contact.firstName.ilike(like),
                                           Contact.lastName.ilike(like)))


        return response([contact.to_dict() for contact in contacts.all()])


    @route('/<uuid:contact_uuid>/')
    @decorators.auth()
    def get(self, **kwargs):
        """
        Returning specific contact for user
        """
        contact = kwargs.get('contact')
        return response(contact.to_dict())


    @decorators.auth()
    @decorators.jsonschema_validate(post.schema)
    def post(self, **kwargs):
        """
        Creating user contact
        """
        user = kwargs.get('user')

        # create and save contact
        # TODO(vojta) handling unique contacts ?
        contact = Contact(userId=user.id, **request.json)
        db.session.add(contact)
        db.session.commit()

        return response(contact.to_dict(), status_code=201)


    @route('/<uuid:contact_uuid>/', methods=['PUT'])
    @decorators.auth()
    @decorators.jsonschema_validate(put.schema)
    def put(self, **kwargs):
        """
        Updating user contact
        """
        contact = kwargs.get('contact')

        # save to db
        contact.update(request.json)
        db.session.commit()

        return response(contact.to_dict())


    @route('/<uuid:contact_uuid>/', methods=['DELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete user contact
        """
        contact = kwargs.get('contact')

        # delete template
        db.session.delete(contact)
        db.session.commit()

        return response(contact.to_dict())
