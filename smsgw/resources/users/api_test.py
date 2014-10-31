# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html


from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.resources.users import datatests


class UsersResourceTest(SmsgwIntegrationTestCase):
    
    POST_URN = '/api/1.0/users/'

    def test_post_endpoint(self):
        """ Testing user POST endpoint """

        # missing email
        res = self.post(self.POST_URN, data=datatests.post.NO_EMAIL)
        self.assert400(res)

        # missing password
        res = self.post(self.POST_URN, data=datatests.post.NO_PASSWORD)
        self.assert400(res)

        # too much long names
        res = self.post(self.POST_URN, data=datatests.post.LONG_NAMES)
        self.assert400(res)

        # valid create
        res = self.post(self.POST_URN, data=datatests.post.VALID)
        data = res.json['data']
        self.assert201(res)
        self.assertEqual(data['email'], datatests.post.VALID['email'])
        self.assertEqual(data['firstName'], datatests.post.VALID['firstName'])
        self.assertEqual(data['lastName'], datatests.post.VALID['lastName'])
        self.assertEqual(data['company'], datatests.post.VALID['company'])
        self.assertNotIn('password', data)
        self.assertIsNotNone(data['uuid'])

        # valid create without company
        res = self.post(self.POST_URN, data=datatests.post.VALID_NO_COMPANY)
        data = res.json['data']
        self.assert201(res)
        self.assertEqual(data['email'], datatests.post.VALID_NO_COMPANY['email'])
        self.assertEqual(data['firstName'], datatests.post.VALID_NO_COMPANY['firstName'])
        self.assertEqual(data['lastName'], datatests.post.VALID_NO_COMPANY['lastName'])
        self.assertIsNone(data['company'])
        self.assertNotIn('password', data)
        self.assertIsNotNone(data['uuid'])

        # already existing user
        res = self.post(self.POST_URN, data=datatests.post.VALID)
        self.assert409(res)
