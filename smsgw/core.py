# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.migrate import Migrate

from smsgw.extensions.mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
mail = Mail()
