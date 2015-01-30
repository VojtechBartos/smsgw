# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.models import BaseModel

class PhoneBook(BaseModel):
    """ Phone book model """

    __tablename__ = "pbk"

    id = db.Column('ID', mysql.INTEGER, primary_key=True)
    groupId = db.Column('GroupID', mysql.INTEGER, nullable=False,
                        server_default='-1')
    info = db.Column('Info', mysql.TEXT, nullable=False)
    name = db.Column('Name', mysql.TEXT, nullable=False)
    number = db.Column('Number', mysql.TEXT, nullable=False)