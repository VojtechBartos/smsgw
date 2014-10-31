# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import json
import os
from unittest import TestCase as UnitTestCase
from flask.ext.testing import TestCase as FlaskTestCase

from smsgw import factory
from smsgw.extensions import db


class SmsgwUnitTestCase(UnitTestCase):
    pass


class SmsgwIntegrationTestCase(FlaskTestCase):
    
    def create_app(self):
        ci = os.environ.get('SMSGW_CI', False)
        env = 'ci' if ci is True else 'test'
        return factory.create_app(name="smsgw_testing", env=env)

    def setUp(self):
        super(SmsgwIntegrationTestCase, self).setUp()
        # flask instance
        self.app = self.create_app()

        # prepare DB. first dump DB afterwards re-create it, 
        # because if tests are gonna fail in DB will stay latest 
        # state
        db.drop_all()
        db.create_all()

    def tearDown(self):
        super(SmsgwIntegrationTestCase, self).tearDown()
        db.session.remove()

    def _request(self, method, path, **kwargs):
        headers = kwargs.get('headers', {'content-type': 'application/json'})
        data = kwargs.get('data')
        if headers.get('content-type') == 'application/json' and data:
            kwargs['data'] = json.dumps(data)
        kwargs['headers'] = headers
        return method(path=path, **kwargs)

    def get(self, path, **kwargs):
        return self._request(self.client.get, path, **kwargs)

    def post(self, path, **kwargs):
        return self._request(self.client.post, path, **kwargs)

    def put(self, path, **kwargs):
        return self._request(self.client.put, path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request(self.client.delete, path, **kwargs)

    def assert201(self, response):
        return self.assertStatus(response, 201)

    def assert409(self, response):
        return self.assertStatus(response, 409)
