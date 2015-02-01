# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.models import BaseModel


class Gammu(BaseModel):
    """ Gammu model """

    id = db.Column(mysql.INTEGER(10), primary_key=True)
    version = db.Column('Version', mysql.INTEGER, nullable=False,
                        server_default='0')
    info = db.Column('Info', mysql.TEXT, nullable=False)