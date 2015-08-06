# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from pytz import timezone, utc

from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from smsgw.models import BaseModel, DateMixin
from smsgw.lib.utils import generate_uuid
from smsgw.extensions import bcrypt, db


class User(BaseModel, DateMixin):
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
    _timeZoneCode = db.Column("timeZoneCode", db.String(100),
                              default='Europe/Prague')
    role = db.Column('role', db.Enum("user", "admin"), default='user',
                     nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    tokens = relationship("UserToken", backref='user')
    templates = relationship("Template", backref='user', lazy='dynamic')
    contacts = relationship("Contact", backref='user', lazy='dynamic')
    tags = relationship("Tag", backref='user', lazy='dynamic')
    applications = relationship("Application", backref='user', lazy='dynamic')
    outbox = relationship("Outbox", backref='user', lazy='dynamic')
    inbox = relationship("Inbox", backref='user', lazy='dynamic')
    sent_items = relationship("SentItem", backref='user', lazy='dynamic')


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
        if password is not None:
            self._password = bcrypt.generate_password_hash(password, 12)

    @property
    def timeZoneCode(self):
        """
        Get user timezone code
        :return: {str} Region/Location
        """
        return self._timeZoneCode if self._timeZoneCode is not None else "UTC"

    @timeZoneCode.setter
    def timeZoneCode(self, value):
        """
        Set user timezone code
        :param value: {str} Region/Location
        :raise: {UnknownTimeZoneError} when timezone code is invalid
        """
        self._timeZoneCode = timezone(value).zone

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

    def to_dict(self, properties=None):
        """
        To dictionary
        :param properties: {list} of required properties
        :return: {dict}
        """
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'email': self.email,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'company': self.company,
            'role': self.role,
            'isActive': self.isActive,
            'numbers': {
                'contacts': self.contacts.count(),
                'sent': self.sent_items.count(),
                'tags': self.tags.count(),
                'outbox': self.outbox.count(),
                'inbox': self.inbox.count(),
                'templates': self.templates.count(),
                'applications': self.applications.count()
            },
            'created': self.created.isoformat(sep=' ') if self.created \
                                                       else None,
            'updated': self.updated.isoformat(sep=' ') if self.updated \
                                                       else None
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}
