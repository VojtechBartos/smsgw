# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import json
import os
from unittest import TestCase as UnitTestCase
from mock import MagicMock
from flask.ext.testing import TestCase as FlaskTestCase

from smsgw import factory
from smsgw.models import User, UserToken
from smsgw.core import db, mail
from smsgw.tests import datasets


class SmsgwUnitTestCase(UnitTestCase):
    pass


class SmsgwIntegrationTestCase(FlaskTestCase):

    def create_app(self):
        return factory.create_app()

    def setUp(self):
        super(SmsgwIntegrationTestCase, self).setUp()
        # flask instance
        self.app = self.create_app()

        # prepare DB. first dump DB afterwards re-create it,
        # because if tests are gonna fail in DB will stay latest
        # state
        db.drop_all()
        db.create_all()

        # mocking
        mail = MagicMock()

        # import base datesets
        self.user = User(**datasets.user.USER)
        db.session.add(self.user)
        db.session.commit()
        token = UserToken(agent="Command-line", userId=self.user.id)
        db.session.add(token)
        db.session.commit()

    def tearDown(self):
        super(SmsgwIntegrationTestCase, self).tearDown()
        db.session.remove()

    def _request(self, method, path, **kwargs):
        headers = kwargs.get('headers', {'content-type': 'application/json'})
        data = kwargs.get('data')
        if headers.get('content-type') == 'application/json' and data:
            kwargs['data'] = json.dumps(data)
        if headers.get('Authorization') is None:
            headers['Authorization'] = "Token {0}".format(
                self.user.tokens.first().token
            )
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
