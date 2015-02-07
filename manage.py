#!venv/bin/python
# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
from smsgw import factory
from smsgw.manage import *

manager = Manager(factory.create_app)
manager.add_option("-e", "--env", dest="env", required=False, 
                   default="development")
manager.add_command('sync', queries.SyncCommand)
manager.add_command('alembic', MigrateCommand)
manager.add_command('gammu', gammu.ReceiveHookCommand)

if __name__ == "__main__":
    manager.run()