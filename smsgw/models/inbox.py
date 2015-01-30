# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from smsgw.extensions import db
from smsgw.models import BaseModel


class Inbox(BaseModel):
    """ Inbox model """

    id = db.Column('ID', mysql.INTEGER(10, unsigned=True), primary_key=True)
    text = db.Column('Text', mysql.TEXT, nullable=False)
    udh = db.Column('UDH', mysql.TEXT, nullable=False)
    senderNumber = db.Column('SenderNumber', db.String(20), nullable=False, 
                             server_default='')
    smscNumber = db.Column('SMSCNumber', db.String(20), nullable=False, 
                            server_default='')
    klass = db.Column('Class', mysql.INTEGER, nullable=False, server_default='-1')
    recipientId = db.Column('RecipientID', mysql.TEXT, nullable=False)
    textDecoded = db.Column('TextDecoded', mysql.TEXT, nullable=False)
    coding = db.Column('Coding', 
                        db.Enum('Default_No_Compression','Unicode_No_Compression',
                                '8bit','Default_Compression','Unicode_Compression'), 
                        server_default='Default_No_Compression', nullable=False)
    processed = db.Column('Processed', db.Enum("false", "true"), 
                          server_default='false', nullable=False)

    updatedAt = db.Column('UpdatedInDB', db.TIMESTAMP, 
                          server_default=dbtext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    receivingAt = db.Column('ReceivingDateTime', db.TIMESTAMP, nullable=False, 
                             server_default='0000-00-00 00:00:00')