# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.models import BaseModel


class Phone(BaseModel):
    """ Phone model """

    __tablename__ = "phones"

    id = db.Column('ID', mysql.TEXT, nullable=False)
    imei = db.Column('IMEI', db.String(35), nullable=False, primary_key=True)
    client = db.Column('Client', mysql.TEXT, nullable=False)
    netCode = db.Column('NetCode', db.String(10), server_default='ERROR')
    netName = db.Column('NetName', db.String(35), server_default='ERROR')
    battery = db.Column('Battery', mysql.INTEGER, nullable=False, 
                        server_default='-1')
    signal = db.Column('Signal', mysql.INTEGER, nullable=False, 
                        server_default='-1')
    sent = db.Column('Sent', mysql.INTEGER, nullable=False, 
                     server_default='0')
    received = db.Column('Received', mysql.INTEGER, nullable=False, 
                         server_default='0')
    send = db.Column('Send', db.Enum("yes", "no"), default='no', 
                     nullable=False)
    receive = db.Column('Receive', db.Enum("yes", "no"), default='no', 
                        nullable=False)
    timeout = db.Column('TimeOut', db.TIMESTAMP, 
                          server_default='0000-00-00 00:00:00')
    createdAt = db.Column('InsertIntoDB', db.TIMESTAMP, 
                          server_default='0000-00-00 00:00:00')
    updatedat = db.Column('UpdatedInDB', db.TIMESTAMP, 
                          server_default=dbtext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))