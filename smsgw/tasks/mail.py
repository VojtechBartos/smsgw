# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from flask import render_template, current_app as app

from smsgw.tasks.base import BaseTask
from smsgw.core import mail


class MailTask(BaseTask):
    """ Task for sending emails """

    routing_key = 'mails'

    DEBUG = 'debug'
    ERROR = 'error'


    @classmethod
    def send(cls, to, template, params, sender=None):
        """Helper for async sending of emails
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
            'sender': sender,
            'type': type
        })


    @classmethod
    def send_debug(cls, environ, lcls, type=None):
        """Sending debug mail
        :param environ: {dict} environment variables
        :param lcls: {dict} local variables
        :param type: {str} type of the email
        :return: {celery.AsyncResult}
        """
        type = type or cls.DEBUG
        if not app.config.get('LOGGING', False):
            return None

        return cls().apply_async(kwargs={
            'to': app.config['MAIL_DEBUG'],
            'template': 'mail/debug',
            'params': {
                'type': type,
                'server_name': app.config['SERVER_NAME'],
                'environ': {k: str(v) for k, v in dict(environ).iteritems()},
                'lcls': lcls or {}
            },
            'sender': app.config['MAIL_DEBUG']
        })


    @classmethod
    def send_error(cls, environ, lcls):
        """Sending error mail
        :param environ: {dict} environment variables
        :param lcls: {dict} local variables
        :return: {celery.AsyncResult}
        """
        return cls.send_debug(lcls, cls.ERROR)


    def run(self, to, template, params, sender=None, **kwargs):
        """Send email from template
        :param to: {list} list of recipients
        :param template: {str} email template file path
        :param params: {dict} dict of values which should be passed to template
        :param sender: {str} sender email
        """
        # render subject and body from template files
        subject = render_template("{0}-subject.html".format(template),
                                  **params)
        body = render_template("{0}.html".format(template), **params)

        # send email
        mail.send(
            from_address=sender or app.config['MAIL_DEFAULT'],
            to_addresses=[to],
            subject=subject,
            body=body
        )

        return {'to': to,
                'template': template,
                'params': params}
