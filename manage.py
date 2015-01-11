#!venv/bin/python
# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.script import Manager
from smsgw import factory
from smsgw.manage import *

manager = Manager(factory.create_app)
manager.add_option("-e", "--env", dest="env", required=False, 
                   default="development")
manager.add_command('sync', SyncCommand)
if __name__ == "__main__":
    manager.run()