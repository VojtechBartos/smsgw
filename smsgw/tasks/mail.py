# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tasks.base import BaseTask


class MailTask(BaseTask):
    """ Sending mail """

    routing_key = 'mails'

    def run(self, url, message, **kwargs):
        
        
        

        return None
