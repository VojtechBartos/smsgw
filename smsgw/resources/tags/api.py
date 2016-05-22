# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request
from flask.ext.classy import FlaskView, route

from sqlalchemy.exc import IntegrityError

from smsgw.models import Tag
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.tags.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.core import db


class TagsResource(FlaskView):
    """ Tags endpoints """

    route_base = '/users/<uuid:user_uuid>/tags/'

    @decorators.auth()
    def index(self, **kwargs):
        """
        Returning list of tags for specific user
        """
        user = kwargs.get('user')

        # search or not
        search = request.args.get('search')
        tags = user.tags
        if search is not None:
            like = "%{0}%".format(search)
            tags = tags.filter(Tag._label.like(like))

        tags = tags.order_by(Tag._label.asc())

        return response([tag.to_dict() for tag in tags.all()])


    @route('/<uuid:tag_uuid>/')
    @decorators.auth()
    def get(self, **kwargs):
        """
        Get user tag
        """
        tag = kwargs.get('tag')
        return response(tag.to_dict())


    @decorators.auth()
    @decorators.jsonschema_validate(post.schema)
    def post(self, **kwargs):
        """
        Creating user tag
        """
        try:
            # save tag
            user = kwargs.get('user')
            tag = Tag(userId=user.id, **request.json)
            db.session.add(tag)
            db.session.commit()
        except IntegrityError, e:
            db.session.rollback()
            raise ErrorResource(409, message="Tag is already exists.")

        return response(tag.to_dict(), status_code=201)


    @route('/<uuid:tag_uuid>/', methods=['PUT'])
    @decorators.auth()
    @decorators.jsonschema_validate(put.schema)
    def put(self, **kwargs):
        """
        Updating user tag
        """
        try:
            # save to db
            tag = kwargs.get('tag')
            tag.update(request.json)
            db.session.commit()
        except IntegrityError, e:
            db.session.rollback()
            raise ErrorResource(409, message="Tag is already exists.")

        return response(tag.to_dict())


    @route('/<uuid:tag_uuid>/', methods=['DELETE'])
    @decorators.auth()
    def delete(self, **kwargs):
        """
        Delete user contact
        """
        tag = kwargs.get('tag')

        # delete template
        db.session.delete(tag)
        db.session.commit()

        return response(tag.to_dict())
