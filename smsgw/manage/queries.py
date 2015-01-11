# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask.ext.script import Command, Option
from smsgw.extensions import db


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
        # actually do sql actions
        db.session.commit()
        print 'Done'
