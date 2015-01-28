# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from slugify import slugify
from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.schema import Index
from smsgw.models import BaseModel
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class Tag(BaseModel):
    """ Tag model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    reference = db.Column(db.String(32), nullable=False)
    _label = db.Column("label", db.String(32), nullable=False)
    note = db.Column(db.String(255))


    @property
    def label(self):
        """
        Getting label
        :return: {str} label
        """
        return self._label

    @label.setter
    def label(self, value):
        """
        Setter for label which automatically set reference
        :param value: {str} label
        """
        self._label = value
        self.reference = slugify(value, to_lower=True)

    def to_dict(self, properties=None):
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'reference': self.reference,
            'label': self.label,
            'note': self.note,
            'numberOfContacts': len(self.contacts) # TODO(vojta) lazy dynamic
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}


Index(Tag.userId, Tag.reference, unique=True)