# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from smsgw.lib.utils import generate_uuid
from smsgw import bcrypt, db



class UserToken(db.Model):
    """ User token model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    user_id = db.Column(mysql.INTEGER(10, unsigned=True))
    token = db.Column(mysql.CHAR(32), unique=True, nullable=False, 
                     default=generate_uuid)
    info = db.Column(mysql.TEXT)

    # user