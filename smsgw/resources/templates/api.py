# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import Template
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.templates.schemas import post
from smsgw.resources.error.api import ErrorResource
from smsgw.extensions import db


class TemplatesResource(FlaskView):
    """ Templates endpoints """

    route_base = '/'

    @route('/users/<uuid:user_uuid>/templates/', methods=['GET'])
    @decorators.auth()
    def index(self, user, **kwargs):
        """

        """
        # if requested user is not logged in, he needs to be 
        # user with admin role or will be sent 403
        if request.user.uuid != user.uuid:
            if request.user.role is not User.ROLE_ADMIN:
                raise ErrorResource(403)

        # load user templates 
        payload = []
        for template in user.templates:
            payload.append({
                'uuid': template.uuid,
                'label': template.label,
                'text': template.text,
                'createdAt': template.createdAt.isoformat(sep=' ')
            })

        return response(payload, status_code=200)

    @route('/users/<uuid:user_uuid>/templates/', methods=['POST'])
    @decorators.auth()
    @decorators.jsonschema_validate(payload=post.schema)
    def post(self, user, **kwargs):
        """

        """
        data = request.json

        # if requested user is not logged in, he needs to be 
        # user with admin role or will be sent 403
        if request.user.uuid != user.uuid:
            if request.user.role is not User.ROLE_ADMIN:
                raise ErrorResource(403)
        
        # create and save template
        template = Template(**data)
        template.userId = user.id
        db.session.add(template)
        db.session.commit()

        # create payload
        payload = {
            'uuid': template.uuid,
            'label': template.label,
            'text': template.text,
            'createdAt': template.createdAt.isoformat(sep=' ')
        }
        return response(payload, status_code=200)

    @route('/users/<uuid:user_uuid>/templates/<uuid:template_uuid>/',
            methods=['DELETE'])
    @decorators.auth()
    def delete(self, user, template, **kwargs):
        """

        """
        # if requested user is not logged in, he needs to be 
        # user with admin role or will be sent 403
        if request.user.uuid != user.uuid:
            if request.user.role is not User.ROLE_ADMIN:
                raise ErrorResource(403)
        
        # delete template
        db.session.delete(template)
        db.session.commit()

        return response({}, status_code=200)
