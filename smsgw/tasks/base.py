# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.tasks import celery


class TaskInvalidArgumentException(Exception):
    pass


class BaseTask(celery.Task):
    """
    Custom BaseTask for better handling routing keys from subclass
    """

    abstract = True

    def _prepare_options(self, options):
        # set up routing key
        routing_key = options.get('routing_key')
        default_key = getattr(self, 'routing_key', None)
        if routing_key is None and default_key is not None:
            options['routing_key'] = default_key
        return options

    def apply(self, *args, **kwargs):
        """ Adding automatic handling routing_key from subclass """
        kwargs = self._prepare_options(kwargs)
        return super(BaseTask, self).apply(*args, **kwargs)

    def apply_async(self, *args, **kwargs):
        """ Adding automatic handling routing_key from subclass """
        kwargs = self._prepare_options(kwargs)
        return super(BaseTask, self).apply_async(*args, **kwargs)
