# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from smsgw.lib.utils import generate_uuid
from smsgw import bcrypt, db



class User(db.Model):
    """ User model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    email = db.Column(db.String(128), unique=True, nullable=False,
                      server_default="")
    _password = db.Column('password', db.String(60), nullable=False)
    firstName = db.Column(db.String(16))
    lastName = db.Column(db.String(16))
    company = db.Column(db.String(32))


    @property
    def password(self):
        """
        Get user password
        :return: {str} hash
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Set user password as bcrypt hash
        :param password: {str}
        """
        self._password = bcrypt.generate_password_hash(pwd, 12)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password.encode('utf8'), 
                                          password)