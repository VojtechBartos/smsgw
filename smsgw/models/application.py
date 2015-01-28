# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
from sqlalchemy.dialects import mysql
from smsgw.models import BaseModel
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class Application(BaseModel):
    """ Application model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    label = db.Column(db.String(32), nullable=False)
    token = db.Column(db.String(32), unique=True, nullable=False)
    prefix = db.Column(db.String(5))
    callbackUrl = db.Column(db.String(128))
    note = db.Column(db.String(255))


    def __init__(self, **kwargs):
        """ 
        Create token on inicialization
        """
        if kwargs.get('token') is None:
            kwargs['token'] = os.urandom(32).encode('hex')

        super(Application, self).__init__(**kwargs)