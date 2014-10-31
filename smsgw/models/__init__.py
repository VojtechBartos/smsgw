# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.extensions import db
from sqlalchemy.ext.declarative import AbstractConcreteBase


class BaseModel(AbstractConcreteBase, db.Model):
    
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    def to_dict(self, properties):
        return {key: getattr(self, key) for key in properties}


# list of models
from smsgw.models.user import User