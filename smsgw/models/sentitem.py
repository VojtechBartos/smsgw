# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import aliased
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.schema import Index
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel, Contact


class SentItem(BaseModel):
    """ SentItem model """

    __tablename__ = 'sentitems'

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), nullable=False, default=generate_uuid)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    applicationId = db.Column(mysql.INTEGER(10, unsigned=True),
                              ForeignKey('application.id'))

    group = db.Column(db.String(8))

    creator = db.Column(mysql.TEXT, nullable=False)
    phone = db.Column(db.String(255))

    destinationNumber = db.Column(db.String(20), nullable=False)
    smscNumber = db.Column(db.String(20), nullable=False)

    coding = db.Column(db.Enum('Default_No_Compression','Unicode_No_Compression',
                                '8bit','Default_Compression','Unicode_Compression'),
                       server_default='Default_No_Compression', nullable=False)
    text = db.Column(mysql.TEXT, nullable=False)
    textEncoded = db.Column(mysql.TEXT, nullable=False)
    udh = db.Column(mysql.TEXT, nullable=False)
    klass = db.Column('class', mysql.INTEGER, server_default='-1', nullable=False)

    status = db.Column(db.Enum('SendingOK','SendingOKNoReport','SendingError',
                                'DeliveryOK','DeliveryFailed','DeliveryPending',
                                'DeliveryUnknown','Error'),
                       server_default='SendingOK', nullable=False)
    statusError = db.Column(mysql.INTEGER, nullable=False, server_default='-1')

    tpmr = db.Column(mysql.INTEGER, nullable=False, server_default='-1')
    relativeValidity = db.Column(mysql.INTEGER, nullable=False, server_default='-1')
    sequencePosition = db.Column(mysql.INTEGER, server_default='1', nullable=False)

    delivery = db.Column(db.TIMESTAMP)
    sent = db.Column("send", db.TIMESTAMP, default=datetime.utcnow)

    contact = db.relationship(
        'Contact',
        primaryjoin="Contact.phoneNumber==SentItem.destinationNumber",
        foreign_keys=[destinationNumber],
        uselist=True
    )

    created = db.Column(
        db.TIMESTAMP, default=datetime.utcnow,
        server_default=dbtext('CURRENT_TIMESTAMP')
    )

    updated = db.Column(
        db.TIMESTAMP, default=datetime.utcnow,
        onupdate=datetime.utcnow
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
            'destinationNumber': self.destinationNumber,
            'contact': self.contact.to_dict() if self.contact else None,
            'status': self.status,
            'application': self.application.to_dict() if self.application \
                                                      else None,
            'text': self.text,
            'send': self.sent.isoformat(sep=' ') if self.sent else None,
            'created': self.created.isoformat(sep=' ') if self.created \
                                                       else None,
            'updated': self.updated.isoformat(sep=' ') if self.updated \
                                                       else None
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}


    @classmethod
    def get(cls, user_id, application_id=None):
        """
        :param user_id: {int} user identifier
        :param application_id: {int} application identifier
        """
        alias = aliased(cls)
        query = db.session.query(
            cls.id,
            cls.uuid,
            cls.destinationNumber,
            cls.sent,
            cls.created,
            db.session.query(func.group_concat(alias.text)) \
                      .filter(alias.group == cls.group) \
                      .filter(alias.destinationNumber == cls.destinationNumber) \
                      .order_by(alias.sequencePosition.desc())
                      .label('message'),
            func.count(cls.id).label('multiparts'),
            Contact.uuid,
            Contact.firstName,
            Contact.lastName
        ) \
        .outerjoin(Contact, Contact.phoneNumber==cls.destinationNumber) \
        .filter(cls.userId == user_id) \
        .filter(cls.applicationId == application_id) \
        .group_by(cls.group, cls.destinationNumber) \
        .order_by(cls.sent.desc())

        payload = []
        for i, uuid, number, s, c, text, multiparts, cuuid, fn, ln in query.all():
            contact = None
            if uuid is not None:
                contact = {
                    'uuid': cuuid,
                    'phoneNumber': number,
                    'firstName': fn,
                    'lastName': ln
                }

            payload.append({
                'id': i,
                'uuid': uuid,
                'destinationNumber': number,
                'text': text,
                'multiparts': multiparts,
                'contact': contact,
                'send': s.isoformat(sep=' ') if s else None,
                'created': c.isoformat(sep=' ') if c else None
            })

        return payload


    @classmethod
    def remove(cls, uuid, user_id, application_id=None):
        """
        Removing message with multiparts
        :param user_id: {int} user identifier
        :param uuid: {int} uuid identifier
        """
        db.session.query(cls).filter(cls.uuid == uuid) \
                             .filter(cls.userId == user_id) \
                             .filter(cls.applicationId == application_id) \
                             .delete(synchronize_session=False)


Index('sentitem_date', SentItem.delivery)
Index('sentitem_tpmr', SentItem.tpmr)
Index('sentitem_destination', SentItem.destinationNumber)
Index('sentitem_phone', SentItem.phone)
