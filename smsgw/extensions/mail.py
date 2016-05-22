# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import requests as req
import traceback
from flask import request


class Mail(object):

    API_URL = 'https://api.mailgun.net/v3/{domain}/messages'


    def ___init__(self, app):
        """Initialization of app
        :param app: {Flask}
        """
        if app:
            self.init_app(app)


    def init_app(self, app):
        """Initialization of app
        :param app: {Flask}
        """
        self.app = app
        self.domain = app.config.get('MAILGUN_DOMAIN')
        self.api_key = app.config.get('MAILGUN_API_KEY')


    def send(self, from_address, to_addresses, subject, body, html=False):
        """Sending email
        :param from_address: {str} respondent email address
        :param to_addresses: {str} emails of destination users
        :param subject: {str} subject of email
        :param body: {str} body of email
        :param html: {bool} if email is plain text or html
        :return: {bool} has benn successfull or not
        """
        if self.app.config('TESTING', False):
            return

        assert self.domain is not None, "Missing Mailgun domain."
        assert self.api_key is not None, "Missing Mailgun API KEY"

        res = None
        payload = {
            'from': from_address,
            'to': to_addresses,
            'subject': subject
        }
        payload['html' if html else 'text'] = body

        try:
            response = req.post(self.API_URL.format(domain=self.domain),
                                auth=('api', self.api_key),
                                data=payload,
                                timeout=10)
            response.raise_for_status()
        except Exception:
            self.app.logger.error(traceback.format_exc())

        return res.status_code == 200 if res else False
