# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

import requests, json
from datetime import datetime, timedelta
from smsgw.tasks.base import BaseTask


class CallbackTask(BaseTask):
    """ Hitting 3rd party callback api """

    routing_key = 'callbacks'

    def run(self, url, message, contact, attempt=1, **kwargs):
        """
        """

        task = None
        status_code = None
        headers = {'content-type': 'application/json'}
        payload = {
            'message': message,
            'contact': contact
        }

        try:
            # make request to 3rd party url
            r = requests.post(url, data=json.dumps(payload),
                              headers=headers, timeout=30)

            # saving status code for task return
            status_code = r.status_code
        except Exception, e:
            # received error, we need to queue another tasks
            # if it is not already 3rd attempt
            if attempt < 3:
                delay = attempt * 10 * 30
                task = CallbackTask().apply_async(**{
                    'kwargs': {
                        'url': url,
                        'attempt': attempt + 1,
                        'message': message,
                        'contact': contact
                    },
                    'eta': datetime.utcnow() + timedelta(seconds=delay)
                })

        return {
            'callback': {
                'url': url,
                'status_code': status_code,
                'attempt': attempt
            },
            'schedule_next': task.id,
            'inbox_id': None
        }
