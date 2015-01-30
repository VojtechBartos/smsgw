# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.models import BaseModel

class PhoneBookGroup(BaseModel):
    """ PhoneBookGroup model """

    __tablename__ = "pbk_groups"

    id = db.Column('ID', mysql.INTEGER(11), primary_key=True)
    name = db.Column('Name', mysql.TEXT, nullable=False)
