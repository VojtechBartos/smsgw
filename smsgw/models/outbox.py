# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.schema import Index
from smsgw.extensions import db
from smsgw.models import BaseModel


class Outbox(BaseModel):
    """ Outbox model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    applicationId = db.Column(mysql.INTEGER(10, unsigned=True), 
                              ForeignKey('application.id'))

    creator = db.Column(mysql.TEXT, nullable=False)
    phone = db.Column(db.String(255))

    destinationNumber = db.Column(db.String(20), nullable=False)

    coding = db.Column(db.Enum('Default_No_Compression','Unicode_No_Compression',
                               '8bit','Default_Compression','Unicode_Compression'), 
                        server_default='Default_No_Compression', nullable=False)
    text = db.Column(mysql.TEXT, nullable=False)
    textEncoded = db.Column(mysql.TEXT)
    multipart = db.Column(db.Enum("false", "true"), server_default='false')
    udh = db.Column(mysql.TEXT)
    klass = db.Column('class', mysql.INTEGER, server_default='-1')

    deliveryReport = db.Column(db.Enum("default", "yes", "no"), server_default='default')
    relativeValidity = db.Column(mysql.INTEGER, server_default='-1')

    send = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    sendTimeout = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    sendBefore = db.Column(db.TIME, nullable=False, server_default='23:59:59')
    sendAfter = db.Column(db.TIME, nullable=False, server_default='00:00:00')

    created = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        server_default=dbtext('CURRENT_TIMESTAMP')
    )
    updated = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


Index('outbox_date', Outbox.send, Outbox.sendTimeout)
Index('outbox_phone', Outbox.phone)