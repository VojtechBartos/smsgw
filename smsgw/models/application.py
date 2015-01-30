# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from smsgw.models import BaseModel, DateMixin
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class Application(BaseModel, DateMixin):
    """ Application model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    label = db.Column(db.String(32), nullable=False)
    token = db.Column(db.String(32), unique=True, nullable=False)
    prefix = db.Column(db.String(5), unique=True)
    callbackUrl = db.Column(db.String(128))
    note = db.Column(db.String(255))


    def __init__(self, **kwargs):
        """ 
        Create token on inicialization
        """
        super(Application, self).__init__(**kwargs)
        # generate token
        self.regenerate_token()

    def regenerate_token(self):
        """
        Regenerate token for API access
        """
        self.token = os.urandom(16).encode('hex')

    def to_dict(self, properties=None):
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'label': self.label,
            'token': self.token,
            'prefix': self.prefix,
            'callbackUrl': self.callbackUrl,
            'note': self.note
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}