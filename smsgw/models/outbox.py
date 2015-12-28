# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from random import randint

from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKey, distinct, func
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.expression import text as dbtext
from sqlalchemy.schema import Index

from smsgw.core import db
from smsgw.models import BaseModel, DateMixin
from smsgw.models.application import Application
from smsgw.models.outbox_multipart import OutboxMultipart
from smsgw.lib.utils import is_special_char, generate_uuid


class Outbox(BaseModel, DateMixin):
    """ Outbox model """

    EIGHT_BIT = '8bit'
    DEFAULT_COMPRESSION = 'Default_Compression'
    DEFAULT_NO_COMPRESSION = 'Default_No_Compression'
    UNICODE_COMPRESSION = 'Unicode_Compression'
    UNICODE_NO_COMPRESSION = 'Unicode_No_Compression'

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False,
                     default=generate_uuid)
    userId = db.Column(mysql.INTEGER(10, unsigned=True), ForeignKey('user.id'))
    applicationId = db.Column(mysql.INTEGER(10, unsigned=True),
                              ForeignKey('application.id'))

    group = db.Column(db.String(8))

    creator = db.Column(mysql.TEXT, nullable=False)
    phone = db.Column(db.String(255))

    destinationNumber = db.Column(db.String(20), nullable=False)

    coding = db.Column(db.Enum('Default_No_Compression','Unicode_No_Compression',
                               '8bit','Default_Compression','Unicode_Compression'),
                        server_default='Default_No_Compression', nullable=False)
    text = db.Column(mysql.TEXT, nullable=False)
    textEncoded = db.Column(mysql.TEXT)
    multipart = db.Column(db.Enum("false", "true"), server_default='false')
    udh = db.Column(mysql.TEXT)
    klass = db.Column('class', mysql.INTEGER, server_default='-1')

    deliveryReport = db.Column(db.Enum("default", "yes", "no"), server_default='default')
    relativeValidity = db.Column(mysql.INTEGER, server_default='-1')

    sent = db.Column("send", db.TIMESTAMP, default=datetime.utcnow)
    sendTimeout = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    sendBefore = db.Column(db.TIME, nullable=False, server_default='23:59:59')
    sendAfter = db.Column(db.TIME, nullable=False, server_default='00:00:00')

    contact = db.relationship(
        'Contact',
        primaryjoin="Contact.phoneNumber==Outbox.destinationNumber",
        foreign_keys=[destinationNumber],
        uselist=False
    )

    multiparts = db.relationship(
        'OutboxMultipart',
        primaryjoin="OutboxMultipart.id==Outbox.id",
        foreign_keys=[id],
        uselist=True
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
            'application': self.application.to_dict() if self.application \
                                                      else None,
            'text': self.text,
            'multiparts': [multipart.to_dict() for multipart in self.multiparts],
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
    def get_all(cls, user_id, application_id=None):
        """
        Get grouped messages
        :param user_id: {int} user identifier
        :param application_id: {int} application identifier
        :return: {list}
        """
        groups = cls.query \
                  .with_entities(
                    cls.id,
                    cls.applicationId,
                    cls.group,
                    cls.text,
                    cls.sent,
                    cls.created,
                    cls.updated,
                    func.count(cls.id)
                  ) \
                  .filter(cls.group != None) \
                  .filter(cls.userId == user_id) \
                  .filter(cls.applicationId == application_id) \
                  .order_by(cls.sent.desc()) \
                  .group_by(cls.group) \
                  .all()

        payload = []
        for identifier, appId, group, message, send, created, updated, respondents in groups:
            multiparts = OutboxMultipart.query.filter_by(id=identifier).all()
            app = Application.get_one(id=appId) if appId else None
            message = "%s%s" % (message, "".join([m.text for m in multiparts]))

            payload.append({
                'id': group,
                'text': message,
                'multiparts': [multipart.to_dict() for multipart in multiparts],
                'application': app.to_dict() if app else None,
                'countOfRespondents': respondents,
                'send': send.isoformat(sep=' ') if send else None,
                'created': created.isoformat(sep=' ') if created else None,
                'updated': updated.isoformat(sep=' ') if updated else None
            })

        return payload


    @classmethod
    def get(cls, group, user_id, application_id=None):
        """
        :param group: {str} group id
        :param user_id: {int} user identifier
        :param application_id: {int} application identifier
        :return: {list}
        """
        items = cls.query \
                 .filter(cls.group == group) \
                 .filter(cls.userId == user_id) \
                 .filter(cls.applicationId == application_id) \
                 .order_by(cls.sent.desc()) \
                 .all()
        if not items:
            return None

        app = items[0].application
        send = items[0].sent
        created = items[0].created
        updated = items[0].updated
        contacts =  [i.contact.to_dict() for i in items if i.contact]
        phone_numbers = [i.destinationNumber for i in items if not i.contact]
        multiparts = OutboxMultipart.query.filter_by(id=items[0].id).all()
        message = "%s%s" % (items[0].text, "".join([m.text for m in multiparts]))

        return {
            'id': group,
            'application': app.to_dict() if app else None,
            'contacts': contacts,
            'phoneNumbers': phone_numbers,
            'text': message,
            'multiparts': [multipart.to_dict() for multipart in multiparts],
            'send': send.isoformat(sep=' ') if send else None,
            'countOfRespondents': len(contacts) + len(phone_numbers),
            'created': created.isoformat(sep=' ') if created else None,
            'updated': updated.isoformat(sep=' ') if updated else None
        }


    @classmethod
    def send(cls, destination_number, message, user_id=None, application_id=None,
             group=None, send=datetime.utcnow(), send_timeout=None,
             send_before=None, send_after=None,
             flash=False, coding=DEFAULT_NO_COMPRESSION):
        """
        Put to queue message to send
        :param destination_number: {str} phone number
        :param message: {str} body of text message
        :param user_id: {int} user identifier
        :param application_id: {int} application identifier
        :param send: {datetime.datetime} when message should be dispatched
        :param send_timeout: {datetime.datetime} datetime for how long it should
                             be timeouted
        :param send_before: {datetime.datetime} send before
        :param send_after: {datetime.datetime} send after
        :param flash: {boolean} if message is type flash or not
        :param coding: {str} coding of text message
        """
        assert message is not None
        assert destination_number is not None
        assert type(message) == str or type(message) == unicode
        assert type(destination_number) == str or type(destination_number) == unicode

        # defining if message is type of flash or not, 0 flash, 1 not flash
        klass = str(int(not flash))

        # get max message length depends by coding
        udh_length = 7
        if coding == cls.DEFAULT_NO_COMPRESSION:
            max_msg_length = 160
        elif coding == cls.UNICODE_NO_COMPRESSION:
            max_msg_length = 60
        else:
            raise Exception('Not supported coding') # TODO(vojta) better exp

        # get message length depends by coding
        msg_length = cls.get_message_length(message, coding)

        # if message length is greater then max length, we need to split it
        # to multiparts
        # NOTICE(vojta) inspired by Kalkun
        # https://github.com/back2arie/Kalkun/blob/master/application/models/gateway/gammu_model.php
        if msg_length > max_msg_length:
            multipart_length = max_msg_length - udh_length
            udh = "050003{hex}".format(
                hex=str(hex(randint(0, 255)).split('x')[1]).ljust(2, "0")
            )
            multiparts = cls.get_message_multipart(message, multipart_length)
            part = str(len(multiparts)).rjust(2, "0")

            outbox = Outbox(
                userId=user_id,
                applicationId=application_id,
                group=group,
                coding=coding,
                text=multiparts[0],
                udh="{udh}{part}01".format(udh=udh, part=part),
                klass=klass,
                multipart="true",
                deliveryReport="no",
                destinationNumber=destination_number,
                relativeValidity=-1,
                creator=user_id if user_id is not None else '',
                sent=send,
                sendTimeout=send_timeout,
                sendBefore=send_before,
                sendAfter=send_after
            )
            # TODO(vojta) is there better way how to get ID of new inserted item ?
            db.session.add(outbox)
            db.session.commit()
            db.session.refresh(outbox)

            # add other parts of the message to database
            for index, message in enumerate(multiparts[1:]):
                position = index + 2
                multipart = OutboxMultipart(
                    id=outbox.id,
                    sequencePosition=position,
                    coding=coding,
                    text=message,
                    klass=klass,
                    udh="{udh}{part}{position}".format(
                        udh=udh,
                        part=part,
                        position=str(position).rjust(2, "0")
                    )
                )

                db.session.add(multipart)
            db.session.commit()

        else:
            # message with length lower or equal max length
            outbox = Outbox(userId=user_id,
                            applicationId=application_id,
                            group=group,
                            coding=coding,
                            text=message,
                            klass=klass,
                            deliveryReport="no",
                            destinationNumber=destination_number,
                            relativeValidity=-1,
                            sent=send,
                            creator=user_id if user_id is not None else '',
                            sendTimeout=send_timeout,
                            sendBefore=send_before,
                            sendAfter=send_after)
            db.session.add(outbox)
            db.session.commit()
            db.session.refresh(outbox)

        return outbox


    @classmethod
    def get_message_multipart(cls, message, length, coding=DEFAULT_NO_COMPRESSION):
        """
        :param message: {str} message text
        :param length: {int} length of multipart message
        :param coding: {str} coding of the message
        :return: {list} list of multipart messages
        """
        multiparts = []

        if coding == cls.DEFAULT_NO_COMPRESSION:
            multiparts = [""]
            part = 0
            char_left = length

            for char in message:
                value = 2 if is_special_char(char) else 1
                if value <= char_left:
                    multiparts[part] = "{0}{1}".format(multiparts[part], char)
                    char_left = char_left - value
                else:
                    part = part + 1
                    multiparts.append(char)
                    char_left = length - value

        else: # TODO(vojta) handle unicode
            pass

        return multiparts


    @classmethod
    def get_message_length(cls, message, coding=DEFAULT_NO_COMPRESSION):
        """
        :param message: {str} message text
        :param coding: {str} coding of the message
        :return: {int} length of message depends by chars type
        """
        length = 0
        if coding == cls.DEFAULT_NO_COMPRESSION:
            for char in message:
                if is_special_char(char):
                    length = length + 2
                else:
                    length = length + 1
        else: # TODO(vojta) handle unicode
            pass

        return length


Index('outbox_date', Outbox.sent, Outbox.sendTimeout)
Index('outbox_phone', Outbox.phone)
