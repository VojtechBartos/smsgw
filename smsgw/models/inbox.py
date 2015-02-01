# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from smsgw.extensions import db
from smsgw.models import BaseModel


class Inbox(BaseModel):
    """ Inbox model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    applicationId = db.Column(mysql.INTEGER(10, unsigned=True), 
                              ForeignKey('application.id'))
    recipient = db.Column(db.String(64))
    senderNumber = db.Column(db.String(20))
    smscNumber = db.Column(db.String(20))

    processed = db.Column(db.Boolean, server_default='0')
    coding = db.Column(db.Enum('Default_No_Compression','Unicode_No_Compression',
                               '8bit','Default_Compression','Unicode_Compression'), 
                        server_default='Default_No_Compression', nullable=False)
    text = db.Column(mysql.TEXT, nullable=False)
    textEncoded = db.Column(mysql.TEXT, nullable=False)
    udh = db.Column(mysql.TEXT, nullable=False)
    klass = db.Column('class', mysql.INTEGER, nullable=False, server_default='-1')

    received = db.Column(db.TIMESTAMP)
    created = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        server_default=dbtext('CURRENT_TIMESTAMP')
    )
    updated = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )