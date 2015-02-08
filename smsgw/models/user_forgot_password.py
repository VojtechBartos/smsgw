# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import mysql

from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel, DateMixin
from smsgw.extensions import db


class UserForgotPassword(BaseModel, DateMixin):
    """ User forgot passowrd model """

    __tablename__ = "user_forgotPassword"

    # TODO(vojta) replace uuid by some generated hash
    token = db.Column(mysql.CHAR(64), nullable=False,
                     default=generate_uuid, primary_key=True)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    expired = db.Column(db.TIMESTAMP)
