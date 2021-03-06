# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import AbstractConcreteBase
from smsgw.core import db
from smsgw.models import BaseModel


class Gammu(BaseModel):
    """ Gammu model """

    id = db.Column(mysql.INTEGER(10), primary_key=True)
    version = db.Column('Version', mysql.INTEGER, nullable=False,
                        server_default='0')
    info = db.Column('Info', mysql.TEXT)

    @classmethod
    def update_version(cls, version, library_version=None):
        """
        Updating gammu version
        :param version: {str} gammu db version
        :param library_version: {str} gammu library version
        """
        versions = cls.query.all()

        assert version is not None
        assert len(versions) <= 1, 'Gammu cannot have set multiple DB version'

        if not len(versions):
            gammu = Gammu()
            db.session.add(gammu)
        else:
            gammu = versions[0]

        gammu.version = version
        gammu.info = library_version
