# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import os
import glob
import importlib
from smsgw.lib.utils import underscore_to_camelcase


def register(app, prefix=None):
    """
    :param app: {Flask} flask app instance
    """
    directory = os.path.dirname(os.path.realpath(__file__))
    resources = [os.path.basename(os.path.normpath(i)) \
                 for i in glob.glob(os.path.join(directory, '*/'))]
    for resource in resources:
        module_path = "{0}.{1}.api".format(__name__, resource)
        class_name = "{0}Resource".format(underscore_to_camelcase(resource))
        try:
            module = importlib.import_module(module_path)
            if module:
                class_ref = getattr(module, class_name)
                class_ref.register(app, route_prefix=prefix)

        except ImportError:
            print "Resource '{0}' does not exists".format(module_path)
        except AttributeError as e:
            print "Resource class '{0}' does not exists".format(class_name)