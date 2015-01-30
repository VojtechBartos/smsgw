# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.schema import Index
from smsgw.extensions import db
from smsgw.models import BaseModel


class Outbox(BaseModel):
    """ Outbox model """

    id = db.Column('ID', mysql.INTEGER(10, unsigned=True), primary_key=True)
    text = db.Column('Text', mysql.TEXT)
    udh = db.Column('UDH', mysql.TEXT)
    klass = db.Column('Class', mysql.INTEGER, server_default='-1')
    textDecoded = db.Column('TextDecoded', mysql.TEXT, nullable=False)
    creatorId = db.Column('CreatorID', mysql.TEXT, nullable=False)
    senderId = db.Column('SenderID', db.String(255))
    destinationNumber = db.Column('DestinationNumber', db.String(20), 
                                  nullable=False, server_default='')
    coding = db.Column('Coding', 
                        db.Enum('Default_No_Compression','Unicode_No_Compression',
                                '8bit','Default_Compression','Unicode_Compression'), 
                        server_default='Default_No_Compression', nullable=False)
    multipart = db.Column('MultiPart', db.Enum("false", "true"), 
                          server_default='false')
    relativeValidity = db.Column('RelativeValidity', mysql.INTEGER, 
                                 server_default='-1')
    deliveryReport = db.Column('DeliveryReport', db.Enum("default", "yes", "no"), 
                               server_default='default')

    sendingDateTime = db.Column('SendingDateTime', db.TIMESTAMP, 
                                server_default='0000-00-00 00:00:00')
    sendBefore = db.Column('SendBefore', db.TIME, nullable=False,
                            server_default='23:59:59')
    sendAfter = db.Column('SendAfter', db.TIME, nullable=False,
                           server_default='00:00:00')
    sendingTimeout = db.Column('SendingTimeOut', db.TIMESTAMP, 
                                server_default='0000-00-00 00:00:00')

    createdAt = db.Column('InsertIntoDB', db.TIMESTAMP, 
                          server_default='0000-00-00 00:00:00')
    updatedat = db.Column('UpdatedInDB', db.TIMESTAMP, 
                          server_default=dbtext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


Index('outbox_date', Outbox.sendingDateTime, Outbox.sendingTimeout)
Index('outbox_sender', Outbox.senderId)