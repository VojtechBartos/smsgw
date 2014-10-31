# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.config.ci import Ci

__all__ = ['environments']

environments = {
    'ci': Ci,
    'development': None,
    'test': None,
    'production': None
}

for env, class_ref in environments.iteritems():
    if class_ref is None:
        try:
            module = "smsgw.config.{}".format(env)
            class_name = env.title()
            class_ref = getattr(__import__(module, fromlist=[class_name]), 
                        class_name)

            environments[env] = class_ref
        except ImportError, e:
            pass