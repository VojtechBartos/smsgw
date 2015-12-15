# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import current_app as app
from flask.ext.script import Command, Option

from smsgw.models import Gammu
from smsgw.core import db


class SyncCommand(Command):
    """ Synchronize models with database """

    option_list = (
        Option('--force', '-f', dest='force', default=False),
    )

    def run(self, force, **kwargs):
        if force:
            # drop all tables
            db.drop_all()
        # check if tables exist, if not create them
        db.create_all()

        # inserting necessary gammu database version
        Gammu.update_version(version=app.config['GAMMU_DATABASE_VERSION'],
                             library_version=app.config['GAMMU_VERSION'])

        # actually do sql actions
        db.session.commit()
        print 'Done'
