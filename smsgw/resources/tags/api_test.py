# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.models import Tag
from smsgw.resources.tags import datasets
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class TagsResourceTest(SmsgwIntegrationTestCase):
    
    INDEX_URN = '/api/1.0/users/@me/tags/'

    def test_index_endpoint(self):
        """ Testing user tag GET index endpoint """

        # nothing in db
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        self.assertEqual(len(res.json['data']), 0)

        # import template datasets to DB
        tags = [Tag(userId=self.user.id, **item) 
                for item in datasets.index.TAGS]
        db.session.add_all(tags)
        db.session.commit()

        # already something in DB
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        for index, item in enumerate(res.json['data']):
            self.assertIsNotNone(item['uuid'])
            self.assertEqual(item['label'], tags[index].label)
            self.assertEqual(item['reference'], tags[index].reference)

        # testing search
        res = self.get("{0}?search=goo".format(self.INDEX_URN))
        self.assert200(res)
        data = res.json['data']
        self.assertEqual(len(data), 2)
        for index, item in enumerate(data):
            self.assertIsNotNone(item['uuid'])
            self.assertEqual(item['label'], tags[index + 1].label)
            self.assertEqual(item['reference'], tags[index + 1].reference)
