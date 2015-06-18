# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.resources.auth import datasets
from smsgw.models import User
from smsgw.extensions import db


class AuthResourceTest(SmsgwIntegrationTestCase):

    LOGIN_URN = '/api/1.0/auth/login/'

    def test_login_endpoint(self):
        """ Testing auth login POST endpoint """

        # invalid empty payload
        res = self.post(self.LOGIN_URN, data={})
        self.assert400(res)

        # invalid email format
        res = self.post(self.LOGIN_URN,
                        data=datasets.login.INVALID_EMAIL_FORMAT)
        self.assert400(res)

        #  no password
        res = self.post(self.LOGIN_URN, data=datasets.login.NO_PASSWORD)
        self.assert400(res)

        # create users
        db.session.add_all([User(**item) for item in datasets.login.USERS])
        db.session.commit()

        # success login
        res = self.post(self.LOGIN_URN, data=datasets.login.VALID)
        self.assert200(res)
        self.assertIsNotNone(res.json['data']['token'])

        # wrong password
        res = self.post(self.LOGIN_URN, data=datasets.login.INVALID)
        self.assert403(res)

        # not active
        res = self.post(self.LOGIN_URN, data=datasets.login.NOT_ACTIVE)
        self.assert403(res)
