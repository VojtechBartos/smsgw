# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw import factory
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = factory.create_app()    
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# import all models
from smsgw.models import *