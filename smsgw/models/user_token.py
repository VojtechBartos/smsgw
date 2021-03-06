# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql

from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel, DateMixin
from smsgw.core import db


class UserToken(BaseModel, DateMixin):
    """ User token model """

    token = db.Column(mysql.CHAR(64), nullable=False,
                     default=generate_uuid, primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    info = db.Column(mysql.TEXT)
    agent = db.Column(mysql.VARCHAR(128))
