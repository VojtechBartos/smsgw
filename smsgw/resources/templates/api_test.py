# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.models import Template
from smsgw.resources.templates import datasets
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class TemplatesResourceTest(SmsgwIntegrationTestCase):
    
    INDEX_URN = '/api/1.0/users/@me/templates/'
    POST_URN = '/api/1.0/users/@me/templates/'
    GET_URN = '/api/1.0/users/@me/templates/{uuid}/'
    PUT_URN = '/api/1.0/users/@me/templates/{uuid}/'
    DELETE_URN = '/api/1.0/users/@me/templates/{uuid}/'

    def test_index_endpoint(self):
        """ Testing user template GET index endpoint """

        # nothing in db
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        self.assertEqual(len(res.json['data']), 0)

        # import template datasets to DB
        templates = [Template(**item) for item in datasets.index.TEMPLATES]
        db.session.add_all(templates)
        db.session.commit()

        # already something in DB
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        for index, item in enumerate(res.json['data']):
            self.assertIsNotNone(item['uuid'])
            self.assertIsNotNone(item['createdAt'])
            self.assertEqual(item['label'], templates[index].label)
            self.assertEqual(item['text'], templates[index].text)

    def test_get_endpoint(self):
        """ Testing user template GET get endpoint """

        # not found 
        res = self.get(self.GET_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # adding datesets to db
        templates = [Template(userId=self.user.id, **item)
                     for item in datasets.get.TEMPLATES]
        db.session.add_all(templates)
        db.session.commit()

        # getting template
        for template in templates:
            res = self.get(self.GET_URN.format(uuid=template.uuid))
            data = res.json['data']
            self.assert200(res)
            self.assertEqual(data['uuid'], template.uuid)
            self.assertEqual(data['label'], template.label)
            self.assertEqual(data['text'], template.text)
            self.assertIsNotNone(data['createdAt'])

    def test_post_endpoint(self):
        """ Testing user template POST endpoint """

        # no label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_NOLABEL)
        self.assert400(res)

        # short label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_SHORTLABEL)
        self.assert400(res)

        # long label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_LONGLABEL)
        self.assert400(res)

        # no text
        res = self.post(self.POST_URN, data=datasets.post.INVALID_NOTEXT)
        self.assert400(res)

        # short text
        res = self.post(self.POST_URN, data=datasets.post.INVALID_SHORTTEXT)
        self.assert400(res)

        # success
        res = self.post(self.POST_URN, data=datasets.post.VALID)
        self.assert201(res)
        self.assertIsNotNone(res.json['data']['uuid'])
        self.assertEqual(res.json['data']['label'], datasets.post.VALID['label'])
        self.assertEqual(res.json['data']['text'], datasets.post.VALID['text'])
        self.assertIsNotNone(res.json['data']['createdAt'])
        # check if its really in DB
        templates = Template.query.filter_by(userId=self.user.id).all()
        self.assertEqual(len(templates), 1)

    def test_put_endpoint(self):
        """ Testing user template PUT endpoint """

        # no found
        res = self.put(self.PUT_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # insert dataset
        template = Template(userId=self.user.id, **datasets.put.VALID)
        db.session.add(template)
        db.session.commit()

        # short label
        res = self.put(self.PUT_URN.format(uuid=template.uuid), 
                       data=datasets.put.INVALID_SHORTLABEL)
        self.assert400(res)

        # long label
        res = self.put(self.PUT_URN.format(uuid=template.uuid), 
                       data=datasets.put.INVALID_LONGLABEL)
        self.assert400(res)

        # no text
        res = self.put(self.PUT_URN.format(uuid=template.uuid), 
                       data=datasets.put.INVALID_NOTEXT)
        self.assert400(res)

        # short text
        res = self.put(self.PUT_URN.format(uuid=template.uuid), 
                       data=datasets.put.INVALID_SHORTTEXT)
        self.assert400(res)

        # successfull update
        res = self.put(self.PUT_URN.format(uuid=template.uuid),
                       data=datasets.put.VALID_UPDATE)
        data = res.json['data']
        db.session.refresh(template)
        self.assert200(res)
        self.assertEqual(data['label'], datasets.put.VALID_UPDATE['label'])
        self.assertEqual(data['text'], datasets.put.VALID_UPDATE['text'])
        self.assertEqual(data['label'], template.label)
        self.assertEqual(data['text'], template.text)

    def test_delete_endpoint(self):
        """ Testing user template DELETE endpoint """

        # not found
        res = self.delete(self.DELETE_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import datasets
        templates = [Template(userId=self.user.id, **item) 
                     for item in datasets.delete.TEMPLATES]
        db.session.add_all(templates)
        db.session.commit()

        # success delete
        res = self.delete(self.DELETE_URN.format(uuid=templates[0].uuid))
        templates = Template.query.filter_by(userId=self.user.id).all()
        self.assert200(res)
        self.assertEqual(len(templates), 1)

        # success delete
        res = self.delete(self.DELETE_URN.format(uuid=templates[0].uuid))
        templates = Template.query.filter_by(userId=self.user.id).all()
        self.assert200(res)
        self.assertEqual(len(templates), 0)
        self.assertIsNotNone(res.json['data']['uuid'])
        self.assertIsNotNone(res.json['data']['label'])
        self.assertIsNotNone(res.json['data']['text'])
        self.assertIsNotNone(res.json['data']['createdAt'])
