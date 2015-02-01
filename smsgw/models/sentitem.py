# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.schema import Index
from smsgw.extensions import db
from smsgw.models import BaseModel


class SentItem(BaseModel):
    """ SentItem model """

    __tablename__ = 'sentitems'

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    applicationId = db.Column(mysql.INTEGER(10, unsigned=True), 
                              ForeignKey('application.id'))

    creator = db.Column(mysql.TEXT, nullable=False)
    phone = db.Column(db.String(255))

    destinationNumber = db.Column(db.String(20), nullable=False)
    smscNumber = db.Column(db.String(20), nullable=False)

    coding = db.Column(db.Enum('Default_No_Compression','Unicode_No_Compression',
                                '8bit','Default_Compression','Unicode_Compression'), 
                       server_default='Default_No_Compression', nullable=False)
    text = db.Column(mysql.TEXT, nullable=False)
    textEncoded = db.Column(mysql.TEXT, nullable=False)
    udh = db.Column(mysql.TEXT, nullable=False)
    klass = db.Column('class', mysql.INTEGER, server_default='-1', nullable=False)
    
    status = db.Column(db.Enum('SendingOK','SendingOKNoReport','SendingError',
                                'DeliveryOK','DeliveryFailed','DeliveryPending',
                                'DeliveryUnknown','Error'), 
                       server_default='SendingOK', nullable=False)
    statusError = db.Column(mysql.INTEGER, nullable=False, server_default='-1')

    tpmr = db.Column(mysql.INTEGER, nullable=False, server_default='-1')
    relativeValidity = db.Column(mysql.INTEGER, nullable=False, server_default='-1')
    sequencePosition = db.Column(mysql.INTEGER, server_default='1', nullable=False)

    delivery = db.Column(db.TIMESTAMP)
    send = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    created = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        server_default=dbtext('CURRENT_TIMESTAMP')
    )
    updated = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


Index('sentitem_date', SentItem.delivery)
Index('sentitem_tpmr', SentItem.tpmr)
Index('sentitem_destination', SentItem.destinationNumber)
Index('sentitem_phone', SentItem.phone)