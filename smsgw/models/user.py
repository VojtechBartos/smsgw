# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from smsgw.models import BaseModel
from smsgw.lib.utils import generate_uuid
from smsgw.extensions import bcrypt, db


class User(BaseModel):
    """ User model """

    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False, 
                     default=generate_uuid)
    email = db.Column(db.String(128), unique=True, nullable=False,
                      server_default="")
    _password = db.Column('password', db.String(60), nullable=False)
    firstName = db.Column(db.String(16))
    lastName = db.Column(db.String(16))
    company = db.Column(db.String(32))
    role = db.Column('role', db.Enum("user", "admin"), default='user', 
                     nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    tokens = relationship("UserToken", backref='user')


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
        self._password = bcrypt.generate_password_hash(password, 12)

    def compare_password(self, password):
        """
        Comparing bcrypt hash with specified password
        :param password: {str} password
        :retur: {bool}
        """
        return bcrypt.check_password_hash(self.password.encode('utf8'), 
                                          password)

    def is_admin(self):
        """
        Returning if user has administration role
        """
        return (self.role == User.ROLE_ADMIN)

    @classmethod
    def is_exists_by_email(cls, email):
        """
        Checking if user with specified emails is exists
        :param email: {str} user email
        """
        return cls.query \
                .with_entities(cls.id) \
                .filter_by(email=email) \
                .first()
