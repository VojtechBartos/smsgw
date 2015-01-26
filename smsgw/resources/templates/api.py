# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import request, current_app
from flask.ext.classy import FlaskView, route

from smsgw.models import Template
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.templates.schemas import post, put
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

    @route('/users/<uuid:user_uuid>/templates/<uuid:template_uuid>/', 
            methods=['GET'])
    @decorators.auth()
    def get(self, user, template, **kwargs):
        """

        """
        return response({
            'uuid': template.uuid,
            'label': template.label,
            'text': template.text,
            'createdAt': template.createdAt.isoformat(sep=' ')
        }, status_code=200)

    @route('/users/<uuid:user_uuid>/templates/', methods=['POST'])
    @decorators.auth()
    @decorators.jsonschema_validate(payload=post.schema)
    def post(self, user, **kwargs):
        """

        """
        data = request.json

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
        return response(payload, status_code=201)

    @route('/users/<uuid:user_uuid>/templates/<uuid:template_uuid>/', 
            methods=['PUT'])
    @decorators.auth()
    @decorators.jsonschema_validate(payload=put.schema)
    def put(self, user, template, **kwargs):
        """

        """
        data = request.json
        
        # save to db
        template.update(data)
        db.session.commit()
 
        return response({
            'uuid': template.uuid,
            'label': template.label,
            'text': template.text,
            'createdAt': template.createdAt.isoformat(sep=' ')
        }, status_code=200)

    @route('/users/<uuid:user_uuid>/templates/<uuid:template_uuid>/',
            methods=['DELETE'])
    @decorators.auth()
    def delete(self, user, template, **kwargs):
        """

        """        
        # delete template
        db.session.delete(template)
        db.session.commit()

        return response({
            'uuid': template.uuid,
            'label': template.label,
            'text': template.text,
            'createdAt': template.createdAt.isoformat(sep=' ')
        }, status_code=200)
