# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.config.default import Default


class Ci(Default):
    """ Ci config """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://travis:@localhost:3306/smsgw_test"