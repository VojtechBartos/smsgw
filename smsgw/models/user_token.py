# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql

from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel
from smsgw.extensions import db


class UserToken(BaseModel):
    """ User token model """

    token = db.Column(mysql.CHAR(36), nullable=False, 
                     default=generate_uuid, primary_key=True)
    user_id = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    info = db.Column(mysql.TEXT)
