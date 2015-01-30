# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.schema import Index
from smsgw.extensions import db
from smsgw.models import BaseModel


class SentItem(BaseModel):
    """ SentItems model """

    __tablename__ = 'senditems'

    id = db.Column('ID', mysql.INTEGER(unsigned=True), primary_key=True)
    creatorId = db.Column('CreatorID', mysql.TEXT, nullable=False)
    text = db.Column('Text', mysql.TEXT, nullable=False)
    senderId = db.Column('SenderID', db.String(255), nullable=False)
    udh = db.Column('UDH', mysql.TEXT, nullable=False)
    klass = db.Column('Class', mysql.INTEGER, server_default='-1', nullable=False)

    textDecoded = db.Column('TextDecoded', mysql.TEXT, nullable=False)
    coding = db.Column('Coding', 
                        db.Enum('Default_No_Compression','Unicode_No_Compression',
                                '8bit','Default_Compression','Unicode_Compression'), 
                        server_default='Default_No_Compression', nullable=False)
    smscNumber = db.Column('SMSCNumber', db.String(20), nullable=False, 
                            server_default='')

    destinationNumber = db.Column('DestinationNumber', db.String(20), 
                                  nullable=False, server_default='')
    sequencePosition = db.Column('SequencePosition', mysql.INTEGER,
                                 server_default='1', nullable=False)

    status = db.Column('Status', 
                        db.Enum('SendingOK','SendingOKNoReport','SendingError',
                                'DeliveryOK','DeliveryFailed','DeliveryPending',
                                'DeliveryUnknown','Error'), 
                        server_default='SendingOK', nullable=False)
    statusError = db.Column('StatusError', mysql.INTEGER, nullable=False,
                            server_default='-1')
    tpmr = db.Column('TMPR', mysql.INTEGER, nullable=False,
                      server_default='-1')
    relativeValidity = db.Column('RelativeValidity', mysql.INTEGER, 
                                 nullable=False, server_default='-1')


    sendingDateTime = db.Column('SendingDateTime', db.TIMESTAMP, 
                                server_default='0000-00-00 00:00:00')
    deliveryDateTime = db.Column('DeviveryDateTime', db.TIMESTAMP)
    createdAt = db.Column('InsertIntoDB', db.TIMESTAMP, 
                          server_default='0000-00-00 00:00:00')
    updatedat = db.Column('UpdatedInDB', db.TIMESTAMP,
                          server_default=dbtext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


Index('sentitems_date', SentItem.deliveryDateTime)
Index('sentitems_tpmr', SentItem.tpmr)
Index('sentitems_dest', SentItem.destinationNumber)
Index('sentitems_sender', SentItem.senderId)