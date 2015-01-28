# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel, Tag, relations


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

    _tags = db.relationship("Tag", secondary=relations.contactTags,
                            backref="contacts", lazy="dynamic")

    @property
    def tags(self):
        """
        Return list of the tags
        :return: {list}
        """
        return [tag.label for tag in self._tags.all()]

    @tags.setter
    def tags(self, items):
        """
        Saves list of tags
        :param items: {list} list of tags
        """
        if items is None:
            items = []

        tags = []
        for label in items:
            dummy = Tag(label=label)
            tag = Tag.get_or_create(reference=dummy.label)
            tag.label = label
            tags.append(tag)

        self._tags = tags
    
    def to_dict(self, properties=None):
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'phoneNumber': self.phoneNumber,
            'email': self.email,
            'note': self.note,
            'tags': self.tags,
            'createdAt': self.createdAt.isoformat(sep=' ')
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}
