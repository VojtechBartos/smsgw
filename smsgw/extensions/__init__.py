# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.uuid import FlaskUUID

db = SQLAlchemy()
bcrypt = Bcrypt()
uuid = FlaskUUID()
