# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.config.default import Default


class Test(Default):
    """ Test config """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://smsgw:smsgw@192.168.50.20:3306/smsgw_test"