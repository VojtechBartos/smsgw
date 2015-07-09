# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.resources.outbox import datatests


class OutboxResourceTest(SmsgwIntegrationTestCase):

    POST_URN = GET_URN = '/api/1.0/outbox/'

    def test_get_endpoint(self):
        """ Testing user GET endpoint """

        # no messages in outbox
        res = self.GET(self.GET_URN)
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(len(data), 0)
