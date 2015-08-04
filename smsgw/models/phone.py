# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime
from sqlalchemy.dialects import mysql
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.extensions import db
from smsgw.lib.utils import generate_uuid
from smsgw.models import BaseModel, DateMixin


class Phone(BaseModel, DateMixin):
    """ Phone model """

    id = db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    uuid = db.Column(mysql.CHAR(36), unique=True, nullable=False,
                     default=generate_uuid)
    hostname = db.Column(db.String(64))
    imei = db.Column(db.String(35), nullable=False)
    netCode = db.Column(db.String(10))
    netName = db.Column(db.String(35))
    battery = db.Column(mysql.INTEGER)
    signal = db.Column(mysql.INTEGER)
    client = db.Column(mysql.TEXT)

    sent = db.Column(mysql.INTEGER, nullable=False, server_default='0')
    received = db.Column(mysql.INTEGER, nullable=False, server_default='0')
    send = db.Column(db.Enum("yes", "no"), default='no', nullable=False)
    receive = db.Column(db.Enum("yes", "no"), default='no', nullable=False)
    timeout = db.Column(db.TIMESTAMP)


    def to_dict(self, properties=None):
        """
        To dictionary
        :param properties: {list} of required properties
        :return: {dict}
        """
        dict = {
            'id': self.id,
            'uuid': self.uuid,
            'hostname': self.hostname,
            'imei': self.imei,
            'netCode': self.netCode,
            'netName': self.netName,
            'battery': self.battery,
            'signal': self.signal,
            'client': self.client,
            'sent': self.sent,
            'received': self.received,
            'sendEnabled': True if self.send == 'yes' else False,
            'receiveEnabled': True if self.receive == 'yes' else False,
            'lastActivity': self.timeout.isoformat(sep=' ') if self.timeout \
                                                            else None,
            'created': self.created.isoformat(sep=' ') if self.created \
                                                       else None,
            'updated': self.updated.isoformat(sep=' ') if self.updated \
                                                       else None
        }

        if properties is None:
            properties = dict.keys()

        return {key: dict.get(key) for key in properties}
