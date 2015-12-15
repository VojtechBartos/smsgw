#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
from smsgw import factory
from smsgw.manage import *


manager = Manager(factory.create_app)
manager.add_command('sync', queries.SyncCommand)
manager.add_command('alembic', MigrateCommand)
manager.add_command('gammu_hook', gammu.ReceiveHookCommand)
manager.add_command('gammu_generate_config', gammu.GenerateConfigCommand)

if __name__ == "__main__":
    manager.run()
