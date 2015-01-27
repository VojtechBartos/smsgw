# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql
from smsgw.models import BaseModel
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid


class Tag(BaseModel):
    """ Tag model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    reference = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(16), nullable=False)
