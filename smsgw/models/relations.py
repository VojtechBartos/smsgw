# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.core import db
from sqlalchemy.dialects.mysql import INTEGER

contact_on_tags = db.Table(
    'contact_tag',
    db.Column('contactId', INTEGER(10, unsigned=True), db.ForeignKey('contact.id'),
              nullable=False, primary_key=True),
    db.Column('tagId', INTEGER(10, unsigned=True), db.ForeignKey('tag.id'),
              nullable=False, primary_key=True)
)
