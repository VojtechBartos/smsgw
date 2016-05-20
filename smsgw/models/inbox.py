# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from smsgw.core import db
from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel, DateMixin


class Inbox(BaseModel, DateMixin):
    """ Inbox model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False,
                     default=generate_uuid)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    applicationId = db.Column(mysql.INTEGER(10, unsigned=True),
                              ForeignKey('application.id'))
    recipient = db.Column(db.String(64))
    senderNumber = db.Column(db.String(20))
    smscNumber = db.Column(db.String(20))

    processed = db.Column(db.Boolean, server_default='0')
    coding = db.Column(db.Enum('Default_No_Compression','Unicode_No_Compression',
                               '8bit','Default_Compression','Unicode_Compression'),
                        server_default='Default_No_Compression', nullable=False)
    text = db.Column(mysql.TEXT, nullable=False)
    textEncoded = db.Column(mysql.TEXT, nullable=False)
    udh = db.Column(mysql.TEXT, nullable=False)
    klass = db.Column('class', mysql.INTEGER, nullable=False, server_default='-1')

    received = db.Column(db.TIMESTAMP)

    contact = db.relationship(
        'Contact',
        primaryjoin="Contact.phoneNumber==Inbox.senderNumber",
        foreign_keys=[senderNumber]
    )


    def to_dict(self, properties=None):
        """
        To dictionary
        :param properties: {list} of required properties
        :return: {dict}
        """
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'senderNumber': self.senderNumber,
            'processed': bool(self.processed),
            'contact': self.contact.to_dict() if self.contact else None,
            'application': self.application.to_dict() if self.application \
                                                      else None,
            'text': self.text,
            'received': self.received.isoformat(sep=' ') if self.received else None,
            'created': self.created.isoformat(sep=' ') if self.created \
                                                       else None,
            'updated': self.updated.isoformat(sep=' ') if self.updated \
                                                       else None
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}


    @classmethod
    def convert_multipart_messages(cls):
        """
        Converting multipart messages to single row in table
        """
        # looking for distinct UDHs
        udhs = db.session.query(func.substr(cls.udh, 1, 10)) \
                         .filter(cls.udh.like("%01")) \
                         .filter(cls.processed==False) \
                         .all()
        udhs = [udh[0] for udh in udhs]

        # iterating over UDHs, looking for messages and merging that to single
        # one row
        for udh in udhs:
            messages = cls.query.filter(cls.udh.like("%s%%" % udh)) \
                                .filter(cls.processed==False) \
                                .order_by(cls.udh.asc()) \
                                .all()
            if not len(messages):
                break

            # creating new single message instead of multiple messages
            inbox = cls(text="".join([m.text for m in messages]),
                        textEncoded="".join([m.textEncoded for m in messages]),
                        recipient=messages[0].recipient,
                        senderNumber=messages[0].senderNumber,
                        smscNumber=messages[0].smscNumber,
                        processed=False,
                        udh="",
                        klass=messages[0].klass,
                        received=messages[0].received)
            db.session.add(inbox)

            # delete multiparts messages
            for message in messages:
                db.session.delete(message)
