# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.models import BaseModel, DateMixin


class Phone(BaseModel):
    """ Phone model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    hostname = db.Column(db.String(64))
    imei = db.Column(db.String(35), nullable=False)
    netCode = db.Column(db.String(10))
    netName = db.Column(db.String(35))
    battery = db.Column(mysql.INTEGER)
    signal = db.Column(mysql.INTEGER)
    client = db.Column(mysql.TEXT)
    
    sent = db.Column(mysql.INTEGER, nullable=False, server_default='0')
    received = db.Column(mysql.INTEGER, nullable=False, server_default='0')
    send = db.Column(db.Enum("yes", "no"), default='no', nullable=False)
    receive = db.Column(db.Enum("yes", "no"), default='no', nullable=False)
    timeout = db.Column(db.TIMESTAMP)

    created = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        server_default=text('CURRENT_TIMESTAMP')
    )
    updated = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )