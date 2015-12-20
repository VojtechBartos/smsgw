# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import render_template, current_app
from flask.ext.mail import Message

from smsgw.tasks.base import BaseTask
from smsgw.core import mail


class MailTask(BaseTask):
    """ Task for sending emails """

    routing_key = 'mails'


    @classmethod
    def send(cls, to, template, params, sender=None):
        """
        Helper for async sending of emails
        :param to: {list} list of recipients
        :param template: {str} email template file path
        :param params: {dict} dict of values which should be passed to template
        :param sender: {str} sender email
        :return: {celery.AsyncResult}
        """
        return cls().apply_async(kwargs={
            'to': to,
            'template': template,
            'params': params,
            'sender': sender
        })

    def run(self, to, template, params, sender=None, **kwargs):
        """
        Send email from template
        :param to: {list} list of recipients
        :param template: {str} email template file path
        :param params: {dict} dict of values which should be passed to template
        :param sender: {str} sender email
        """

        # render subject and body from template files
        subject = render_template("{0}-subject.html".format(template),
                                  **params)
        body = render_template("{0}.html".format(template), **params)

        # create message
        msg = Message(subject)
        msg.sender = sender or current_app.config.get('DEFAULT_MAIL_SENDER')
        msg.recipients = [to]
        msg.body = body

        # send mail
        mail.send(msg)

        return {'to': to,
                'template': template,
                'params': params}
