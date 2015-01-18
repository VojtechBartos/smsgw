# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.models import Contact
from smsgw.resources.contacts import datasets
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class TemplatesResourceTest(SmsgwIntegrationTestCase):
    
    INDEX_URN = '/api/1.0/users/@me/contacts/'
    GET_URN = '/api/1.0/users/@me/contacts/{uuid}/'

    def test_index_endpoint(self):
        """ Testing user contacts GET index endpoint """

        # nothing in db
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        self.assertEqual(len(res.json['data']), 0)

        # import contacts datasets to DB
        contacts = [Contact(userId=self.user.id, **item) 
                    for item in datasets.index.CONTACTS]
        db.session.add_all(contacts)
        db.session.commit()

        # already something in DB
        res = self.get(self.INDEX_URN)
        self.assert200(res)
        for index, item in enumerate(res.json['data']):
            self.assertIsNotNone(item['id'])
            self.assertIsNotNone(item['uuid'])
            self.assertEqual(item['firstName'], contacts[index].firstName)
            self.assertEqual(item['lastName'], contacts[index].lastName)
            self.assertEqual(item['phoneNumber'], contacts[index].phoneNumber)
            self.assertEqual(item['email'], contacts[index].email)
            self.assertIsNotNone(item['createdAt'])

    def test_get_endpoint(self):
        """ Testing user contact GET get endpoint """

        # not found 
        res = self.get(self.GET_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # adding datesets to db
        contacts = [Contact(userId=self.user.id, **item)
                    for item in datasets.get.CONTACTS]
        db.session.add_all(contacts)
        db.session.commit()

        # getting template
        for contact in contacts:
            res = self.get(self.GET_URN.format(uuid=contact.uuid))
            data = res.json['data']
            self.assert200(res)
            self.assertIsNotNone(data['id'])
            self.assertIsNotNone(data['uuid'])
            self.assertEqual(data['firstName'], contact.firstName)
            self.assertEqual(data['lastName'], contact.lastName)
            self.assertEqual(data['phoneNumber'], contact.phoneNumber)
            self.assertEqual(data['email'], contact.email)
            self.assertIsNotNone(data['createdAt'])
