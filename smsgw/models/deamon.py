# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.models import BaseModel


class Deamon(BaseModel):
    """ Deamon model """

    __tablename__ = 'deamons'

    id = db.Column('ID', mysql.INTEGER(10), primary_key=True)
    start = db.Column('Start', mysql.TEXT, nullable=False)
    info = db.Column('Info', mysql.TEXT, nullable=False)