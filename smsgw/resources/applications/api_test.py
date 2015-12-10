# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.models import Application
from smsgw.resources.applications import datasets
from smsgw.core import db
from smsgw.lib.utils import generate_uuid


class TagsResourceTest(SmsgwIntegrationTestCase):
    
    INDEX_URN = '/api/1.0/users/@me/applications/'
    POST_URN = '/api/1.0/users/@me/applications/'
    GET_URN = '/api/1.0/users/@me/applications/{uuid}/'
    PUT_URN = '/api/1.0/users/@me/applications/{uuid}/'
    DELETE_URN = '/api/1.0/users/@me/applications/{uuid}/'
    REG_URN = '/api/1.0/users/@me/applications/{uuid}/regenerate/'

    def test_index_endpoint(self):
        """ Testing user application GET index endpoint """

        # nothing in db
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        self.assertEqual(len(res.json['data']), 0)

        # import datasets to DB
        apps = [Application(userId=self.user.id, **item) 
                for item in datasets.index.APPS]
        db.session.add_all(apps)
        db.session.commit()

        # already something in DB
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        for index, item in enumerate(res.json['data']):
            self.assertIsNotNone(item.get('id'))
            self.assertIsNotNone(item.get('uuid'))
            self.assertEqual(item.get('label'), apps[index].label)
            self.assertEqual(item.get('prefix'), apps[index].prefix)
            self.assertEqual(item.get('token'), apps[index].token)
            self.assertEqual(item.get('callbackUrl'), apps[index].callbackUrl)
            self.assertEqual(item.get('note'), apps[index].note)

    def test_get_endpoint(self):
        """ Testing user application GET get endpoint """

        res = self.get(self.GET_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import template datasets to DB
        app = Application(userId=self.user.id, **datasets.get.APP)
        db.session.add(app)
        db.session.commit()
        db.session.refresh(app)

        res = self.get(self.GET_URN.format(uuid=app.uuid))
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(data['id'], app.id)
        self.assertEqual(data['uuid'], app.uuid)
        self.assertEqual(data['label'], app.label)
        self.assertEqual(data['prefix'], app.prefix)
        self.assertEqual(data['token'], app.token)
        self.assertEqual(data['callbackUrl'], app.callbackUrl)
        self.assertEqual(data['note'], app.note)

    def test_post_endpoint(self):
        """ Testing user tag POST endpoint """

        # import  datasets to DB
        apps = [Application(userId=self.user.id, **item) 
                for item in datasets.post.APPS]
        db.session.add_all(apps)
        db.session.commit()

        # no label
        res = self.post(self.POST_URN, data={})
        self.assert400(res)

        # short label
        res = self.post(self.POST_URN, data=datasets.post.INVALID_LABEL)
        self.assert400(res)

        # invlid code
        res = self.post(self.POST_URN, data=datasets.post.INVALID_CODE)
        self.assert400(res)

        # invalid url
        res = self.post(self.POST_URN, data=datasets.post.INVALID_URL)
        self.assert400(res)

        # already existing code
        res = self.post(self.POST_URN, data=datasets.post.DUPLICATED_CODE)
        self.assert409(res)

        # success
        res = self.post(self.POST_URN, data=datasets.post.VALID)
        data = res.json['data']
        self.assert201(res)
        self.assertIsNotNone(data['id'])
        self.assertIsNotNone(data['uuid'])
        self.assertIsNotNone(data['token'])
        self.assertEqual(data['label'], datasets.post.VALID['label'])
        self.assertEqual(data['prefix'], datasets.post.VALID['prefix'])
        self.assertEqual(data['callbackUrl'], datasets.post.VALID['callbackUrl'])
        self.assertIsNone(data['note'])
        apps = Application.query.filter_by(userId=self.user.id).all()
        self.assertEqual(len(apps), 4)

    def test_put_endpoint(self):
        """ Testing user application PUT update endpoint """

        res = self.put(self.PUT_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import  datasets to DB
        apps = [Application(userId=self.user.id, **item) 
                for item in datasets.put.APPS]
        db.session.add_all(apps)
        db.session.commit()

        # no label
        res = self.put(self.PUT_URN.format(uuid=apps[0].uuid), 
                       data={})
        self.assert400(res)

        # short label
        res = self.put(self.PUT_URN.format(uuid=apps[0].uuid), 
                       data=datasets.put.INVALID_LABEL)
        self.assert400(res)

        # invlid code
        res = self.put(self.PUT_URN.format(uuid=apps[0].uuid), 
                       data=datasets.put.INVALID_CODE)
        self.assert400(res)

        # invalid url
        res = self.put(self.PUT_URN.format(uuid=apps[0].uuid), 
                       data=datasets.put.INVALID_URL)
        self.assert400(res)

        # already existing code
        res = self.put(self.PUT_URN.format(uuid=apps[0].uuid), 
                       data=datasets.put.DUPLICATED_CODE)
        self.assert409(res)

        # success
        res = self.put(self.PUT_URN.format(uuid=apps[0].uuid), 
                       data=datasets.put.VALID)
        data = res.json['data']
        self.assert200(res)
        self.assertIsNotNone(data['id'])
        self.assertIsNotNone(data['uuid'])
        self.assertIsNotNone(data['token'])
        self.assertEqual(data['label'], datasets.put.VALID['label'])
        self.assertEqual(data['prefix'], datasets.put.VALID['prefix'])
        self.assertEqual(data['callbackUrl'], datasets.put.VALID['callbackUrl'])
        self.assertIsNone(data['note'])
        apps = Application.query.filter_by(userId=self.user.id).all()
        self.assertEqual(len(apps), 3)


    def test_regenerate_endpoint(self):
        """ Testing user application PUT regenerate endpoint """

        res = self.put(self.REG_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import template datasets to DB
        app = Application(userId=self.user.id, **datasets.regenerate.APP)
        db.session.add(app)
        db.session.commit()

        res = self.put(self.REG_URN.format(uuid=app.uuid))
        db.session.refresh(app)
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(data['uuid'], app.uuid)
        self.assertEqual(data['token'], app.token)

    def test_delete_endpoint(self):
        """ Testing user application DELETE remove endpoint """

        res = self.delete(self.DELETE_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # import template datasets to DB
        app = Application(userId=self.user.id, **datasets.delete.APP)
        db.session.add(app)
        db.session.commit()
        db.session.refresh(app)

        res = self.delete(self.DELETE_URN.format(uuid=app.uuid))
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(data['id'], app.id)
        self.assertEqual(data['uuid'], app.uuid)
        self.assertEqual(data['label'], app.label)
        self.assertEqual(data['prefix'], app.prefix)
        self.assertEqual(data['token'], app.token)
        self.assertEqual(data['callbackUrl'], app.callbackUrl)
        self.assertEqual(data['note'], app.note)
        apps = Application.query.filter_by(userId=self.user.id).all()
        self.assertEqual(len(apps), 0)
