# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from smsgw.models import BaseModel
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class Contact(BaseModel):
    """ Contact model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))

    firstName = db.Column(db.String(16), nullable=False)
    lastName = db.Column(db.String(16), nullable=False)
    phoneNumber = db.Column(db.String(14))
    email = db.Column(db.String(128))
    note = db.Column(db.String(255))


    def to_dict(self, properties=None):
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'phoneNumber': self.phoneNumber,
            'email': self.email,
            'note': self.note,
            'createdAt': self.createdAt.isoformat(sep=' ')
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}
