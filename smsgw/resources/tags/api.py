# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import Tag
from smsgw.lib.utils import response
from smsgw.resources import decorators
# from smsgw.resources.contacts.schemas import post, put
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


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
            tags = tags.filter(Tag.label.like(like))

        return response([tag.to_dict() for tag in tags.all()])