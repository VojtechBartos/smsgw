# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.schema import Index
from smsgw.extensions import db
from smsgw.models import BaseModel

class OutboxMultipart(BaseModel):
    """ PhoneBookGroup model """

    __tablename__ = "outbox_multipart"

    id = db.Column('ID', mysql.INTEGER(unsigned=True), primary_key=True)
    text = db.Column('Text', mysql.TEXT)
    klass = db.Column('Class', mysql.INTEGER, server_default='-1')
    udh = db.Column('UDH', mysql.TEXT)
    textDecoded = db.Column('TextDecoded', mysql.TEXT)
    coding = db.Column('Coding', 
                        db.Enum('Default_No_Compression','Unicode_No_Compression',
                                '8bit','Default_Compression','Unicode_Compression'), 
                        server_default='Default_No_Compression', nullable=False)
    sequencePosition = db.Column('SequencePosition', mysql.INTEGER,
                                 server_default='1', primary_key=True)