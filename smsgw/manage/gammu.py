# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import re
import os
from flask import render_template, current_app
from flask.ext.script import Command, Option
from sqlalchemy import func

from smsgw.core import db
from smsgw.models import Inbox, Application
from smsgw.tasks.callback import CallbackTask


class ReceiveHookCommand(Command):
    """ Receive hook for gammu """

    def run(self, **kwargs):
        # getting all text messages which they have not been processed
        inbox = Inbox.query.filter_by(processed=False).all()
        for message in inbox:
            # find prefix
            m = re.search("^([a-zA-Z0-9]{2,5}).*$", message.text)
            if not m or m.group(1) is None:
                # if prefix does not found we can continue
                # nothing to parse
                message.processed = True
                continue

            # first match is prefix, keeping prefix upper case
            prefix = m.group(1).upper()

            # find application by prefix
            application = Application.query \
                            .filter(func.lower(Application.prefix)==prefix) \
                            .first()
            if application is not None:
                # assign user id and application id
                message.userId = application.userId
                message.applicationId = application.id

                # if there is set callback url, we put to
                # queue task which let now customer api
                # about new recevied text message
                if application.callbackUrl:
                    kwargs = {
                        'kwargs': {
                            'url': application.callbackUrl,
                            'message': {
                                'senderNumber': message.senderNumber,
                                'text': message.text,
                                'received': message.received.isoformat(' ')
                            },
                            'contact': message.contact.to_dict() \
                                       if message.contact else None
                        }
                    }
                    # add task to message queue
                    CallbackTask().apply_async(**kwargs)

            # message has been processed
            message.processed = True

        db.session.commit()


class GenerateConfigCommand(Command):
    """ Generating gammurc daemon config """

    option_list = (
        Option('--destination', '-d', dest='destination', default=None),
    )

    def run(self, destination=None):
        assert isinstance(destination, (unicode, str)), \
            "Missing destination parameter."

        # generating config
        config = render_template('gammu/gammurc', **{
            'GAMMU_DEVICE_ID': current_app.config['GAMMU_DEVICE_ID'],
            'GAMMU_DEVICE_PIN': current_app.config['GAMMU_DEVICE_PIN'],
            'DATABASE_USERNAME': current_app.config['DATABASE_USERNAME'],
            'DATABASE_PASSWORD': current_app.config['DATABASE_PASSWORD'],
            'DATABASE_HOST': current_app.config['DATABASE_HOST'],
            'DATABASE_NAME': current_app.config['DATABASE_NAME']
        })

        # saving template
        with open(os.path.join(destination), 'w+') as f:
            f.write(config)

        print "Saved in destination: %s" % destination
