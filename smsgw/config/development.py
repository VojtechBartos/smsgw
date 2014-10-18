# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

""" Development config """
from smsgw.config.default import Default


class Development(Default):
    
    DEBUG = True
    LOGGING = False

    SQLALCHEMY_DATABASE_URI = "mysql://smsgw:smsgw@192.168.50.20:3306/smsgw"