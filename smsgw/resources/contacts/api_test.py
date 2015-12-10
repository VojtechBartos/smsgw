# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tests import SmsgwIntegrationTestCase
from smsgw.models import Contact
from smsgw.resources.contacts import datasets
from smsgw.core import db
from smsgw.lib.utils import generate_uuid


class TemplatesResourceTest(SmsgwIntegrationTestCase):

    INDEX_URN = '/api/1.0/users/@me/contacts/'
    POST_URN = '/api/1.0/users/@me/contacts/'
    GET_URN = '/api/1.0/users/@me/contacts/{uuid}/'
    PUT_URN = '/api/1.0/users/@me/contacts/{uuid}/'
    DELETE_URN = '/api/1.0/users/@me/contacts/{uuid}/'

    def test_index_endpoint(self):
        """ User's contacts GET index endpoint """

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
            self.assertIsNotNone(item['created'])

    def test_get_endpoint(self):
        """ User's contact GET get endpoint """

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
            self.assertIsNotNone(data['created'])

    def test_post_endpoint(self):
        """ User's contact POST create endpoint """

        # no data
        res = self.post(self.POST_URN, data={})
        self.assert400(res)

        # invalid email
        res = self.post(self.POST_URN, data=datasets.post.INVALID_EMAIL)
        self.assert400(res)

        # invalid number
        res = self.post(self.POST_URN, data=datasets.post.INVALID_NUMBER)
        self.assert400(res)

        # missing field
        res = self.post(self.POST_URN, data=datasets.post.MISSING_FIELD)
        self.assert400(res)

        # success
        res = self.post(self.POST_URN, data=datasets.post.VALID)
        self.assert201(res)
        data = res.json['data']
        self.assertIsNotNone(data['id'])
        self.assertIsNotNone(data['uuid'])
        self.assertEqual(data['firstName'], datasets.post.VALID['firstName'])
        self.assertEqual(data['lastName'], datasets.post.VALID['lastName'])
        self.assertEqual(data['phoneNumber'], datasets.post.VALID['phoneNumber'])
        self.assertEqual(data['email'], datasets.post.VALID['email'])
        self.assertEqual(data['note'], datasets.post.VALID['note'])
        self.assertIsNotNone(data['created'])
        contact = Contact.query \
                    .filter_by(email=datasets.post.VALID['email']) \
                    .first()
        self.assertEqual(contact.email, datasets.post.VALID['email'])
        self.assertEqual(contact.phoneNumber, datasets.post.VALID['phoneNumber'])
        self.assertEqual(contact.firstName, datasets.post.VALID['firstName'])
        self.assertEqual(contact.lastName, datasets.post.VALID['lastName'])
        self.assertEqual(contact.userId, self.user.id)


    def test_put_endpoint(self):
        """ User's contact PUT update endpoint"""

        # not found
        res = self.put(self.PUT_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # adding contact to DB
        contact = Contact(userId=self.user.id, **datasets.put.VALID)
        db.session.add(contact)
        db.session.commit()

        # invalid email
        res = self.put(self.PUT_URN.format(uuid=contact.uuid),
                       data=datasets.put.INVALID_EMAIL)
        self.assert400(res)

        # invalid number
        res = self.put(self.PUT_URN.format(uuid=contact.uuid),
                       data=datasets.put.INVALID_NUMBER)
        self.assert400(res)

        # missing field
        res = self.put(self.PUT_URN.format(uuid=contact.uuid),
                       data=datasets.put.MISSING_FIELD)
        self.assert400(res)

        # success
        res = self.put(self.PUT_URN.format(uuid=contact.uuid),
                       data=datasets.put.UPDATE)
        self.assert200(res)
        db.session.refresh(contact)
        data = res.json['data']
        self.assertEqual(data['id'], contact.id)
        self.assertEqual(data['uuid'], contact.uuid)
        self.assertEqual(data['firstName'], contact.firstName)
        self.assertEqual(data['lastName'], contact.lastName)
        self.assertEqual(data['phoneNumber'], contact.phoneNumber)
        self.assertEqual(data['email'], contact.email)
        self.assertIsNone(data['note'])
        self.assertIsNotNone(data['created'])

    def test_delete_endpoint(self):
        """ User's contact DELETE delete endpoint """

        # not found
        res = self.get(self.DELETE_URN.format(uuid=generate_uuid()))
        self.assert404(res)

        # adding datesets to db
        contacts = [Contact(userId=self.user.id, **item)
                    for item in datasets.delete.CONTACTS]
        db.session.add_all(contacts)
        db.session.commit()

        # success delete
        res = self.get(self.DELETE_URN.format(uuid=contacts[0].uuid))
        self.assert200(res)
        data = res.json['data']
        self.assert200(res)
        self.assertEqual(data['id'], contacts[0].id)
        self.assertEqual(data['uuid'], contacts[0].uuid)
        self.assertEqual(data['firstName'], contacts[0].firstName)
        self.assertEqual(data['lastName'], contacts[0].lastName)
        self.assertEqual(data['phoneNumber'], contacts[0].phoneNumber)
        self.assertEqual(data['email'], contacts[0].email)
        self.assertIsNotNone(data['created'])
