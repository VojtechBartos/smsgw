# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.models import Tag
from smsgw.resources.tags import datasets
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class TagsResourceTest(SmsgwIntegrationTestCase):
    
    INDEX_URN = '/api/1.0/users/@me/tags/'
    POST_URN = '/api/1.0/users/@me/tags/'
    GET_URN = '/api/1.0/users/@me/tags/{uuid}/'
    PUT_URN = '/api/1.0/users/@me/tags/{uuid}/'
    DELETE_URN = '/api/1.0/users/@me/tags/{uuid}/'

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

    def test_get_endpoint(self):
        """ Testing user tag GET get endpoint """

        res = self.get(self.GET_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import template datasets to DB
        tag = Tag(userId=self.user.id, **datasets.get.TAG)
        db.session.add(tag)
        db.session.commit()
        db.session.refresh(tag)

        res = self.get(self.GET_URN.format(uuid=tag.uuid))
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(data['id'], tag.id)
        self.assertEqual(data['uuid'], tag.uuid)
        self.assertEqual(data['label'], tag.label)
        self.assertEqual(data['reference'], tag.reference)
        self.assertEqual(data['note'], tag.note)

    def test_post_endpoint(self):
        """ Testing user tag POST endpoint """

        # import template datasets to DB
        tags = [Tag(userId=self.user.id, **item) 
                for item in datasets.post.TAGS]
        db.session.add_all(tags)
        db.session.commit()

        # no label
        res = self.post(self.POST_URN, data={})
        self.assert400(res)

        # short label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_LABEL)
        self.assert400(res)

        # long label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_LONGLABEL)
        self.assert400(res)

        # already existing label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_EXISTS)
        self.assert409(res)

        # success
        res = self.post(self.POST_URN, data=datasets.post.VALID)
        data = res.json['data']
        self.assert201(res)
        self.assertIsNotNone(data['id'])
        self.assertIsNotNone(data['uuid'])
        self.assertEqual(data['label'], datasets.post.VALID['label'])
        self.assertIsNotNone(data['reference'])
        self.assertEqual(data['note'], datasets.post.VALID['note'])
        self.assertEqual(len(Tag.query.filter_by(userId=self.user.id).all()), 4)

    def test_put_endpoint(self):
        """ Testing user tag PUT update endpoint """

        res = self.put(self.PUT_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import template datasets to DB
        tags = [Tag(userId=self.user.id, **item) 
                for item in datasets.put.TAGS]
        db.session.add_all(tags)
        db.session.commit()

        # no label
        res = self.put(self.PUT_URN.format(uuid=tags[0].uuid), data={})
        self.assert400(res)

        # short label
        res = self.put(self.PUT_URN.format(uuid=tags[0].uuid), 
                       data=datasets.put.INVALID_LABEL)
        self.assert400(res)

        # long label
        res = self.put(self.PUT_URN.format(uuid=tags[0].uuid), 
                       data=datasets.put.INVALID_LONGLABEL)
        self.assert400(res)

        # already existing label
        res = self.put(self.PUT_URN.format(uuid=tags[0].uuid), 
                       data=datasets.put.INVALID_EXISTS)
        self.assert409(res)

        # success
        res = self.put(self.PUT_URN.format(uuid=tags[0].uuid), 
                       data=datasets.put.VALID)
        data = res.json['data']
        self.assert200(res)
        self.assertIsNotNone(data['id'])
        self.assertIsNotNone(data['uuid'])
        self.assertEqual(data['label'], datasets.put.VALID['label'])
        self.assertIsNotNone(data['reference'])
        self.assertEqual(data['note'], datasets.put.VALID['note'])
        self.assertEqual(len(Tag.query.filter_by(userId=self.user.id).all()), 3)

    def test_delete_endpoint(self):
        """ Testing user tag DELETE remove endpoint """

        res = self.delete(self.DELETE_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import template datasets to DB
        tag = Tag(userId=self.user.id, **datasets.delete.TAG)
        db.session.add(tag)
        db.session.commit()
        db.session.refresh(tag)

        res = self.delete(self.DELETE_URN.format(uuid=tag.uuid))
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(data['id'], tag.id)
        self.assertEqual(data['uuid'], tag.uuid)
        self.assertEqual(data['label'], tag.label)
        self.assertEqual(data['reference'], tag.reference)
        self.assertEqual(data['note'], tag.note)
        self.assertEqual(len(Tag.query.filter_by(userId=self.user.id).all()), 0)
