# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import time
from flask import current_app as app
from flask.ext.script import Command, Option
from sqlalchemy import inspect
from sqlalchemy.exc import OperationalError

from smsgw.models import Gammu
from smsgw.core import db


class InitCommand(Command):
    """
    Initialization command for setting up models into
    database and prepare it for smooth run
    """

    def run(self):
        while True:
            try:
                app.logger.info("Init: waiting for database to be started.")

                # trying out connection
                db.engine.connect()

                # if its successfully connected, continue with initialization
                break
            except OperationalError:
                time.sleep(3)

        # detecting how many tables are in db, if there is anything, skip init
        inspector = inspect(db.engine)
        if len(inspector.get_table_names()) > 0:
            app.logger.info("Init: database already initializated!")
            return

        # creating all tables
        db.create_all()

        # inserting necessary gammu database version
        Gammu.update_version(version=app.config['GAMMU_DATABASE_VERSION'],
                             library_version=app.config['GAMMU_VERSION'])

        db.session.commit()

        app.logger.info("Init: database initialization done!")


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

        app.logger.info("Sync: done!")
