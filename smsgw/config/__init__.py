# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
from smsgw.lib.utils import underscore_to_camelcase

__all__ = ['env', 'settings']

env = os.environ.get('SMSGW_ENV', 'development')
module = "{0}.{1}".format(__name__, env) 
class_name = underscore_to_camelcase(env)
settings = getattr(__import__(module, fromlist=[class_name]), 
                   class_name)

print "Running under `%s` environment" % env
