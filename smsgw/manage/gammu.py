# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import re
from flask.ext.script import Command, Option
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
            prefix = m.group(1)
            if prefix is None:
                # if prefix does not found we can continue
                # nothing to parse
                message.processed = True
                continue

            # find application by prefix
            application = Application.query \
                            .filter_by(prefix=prefix) \
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
