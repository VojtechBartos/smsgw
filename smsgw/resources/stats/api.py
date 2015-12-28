# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from datetime import datetime, timedelta
from flask.ext.classy import FlaskView, route
from sqlalchemy import Date, cast, func

from smsgw.core import db
from smsgw.models import Outbox, SentItem, Inbox
from smsgw.lib.utils import response
from smsgw.resources import decorators
from smsgw.resources.error.api import ErrorResource


class StatsResource(FlaskView):
    """ Statistics endpoints """

    route_base = '/users/<uuid:user_uuid>/'

    @route('/stats/')
    @route('/applications/<uuid:application_uuid>/stats/')
    @decorators.auth()
    def messages(self, **kwargs):
        """
        GET stats count for inbox, sent and outbox
        """
        user = kwargs.get('user')
        app = kwargs.get('application')
        payload = {}
        elements = {
            'sent': SentItem,
            'inbox': Inbox,
            'outbox': Outbox
        }

        for key, model in elements.iteritems():
            query = model.query.filter_by(userId=user.id)
            if app:
                query = query.filter_by(applicationId=app.id)
            payload[key] = query.count()

        return response(payload)


    @route('/stats/<any(lastweek,lastmonth):interval>/')
    @route('/applications/<uuid:application_uuid>/stats/<any(lastweek,lastmonth):interval>/')
    @decorators.auth()
    def messages_range(self, interval, **kwargs):
        """
        GET stats count for inbox, sent and outbox per time intervals
        """
        user = kwargs.get('user')
        app = kwargs.get('application')
        utcnow = datetime.utcnow()
        payload = {}
        elements = {
            'sent': SentItem,
            'inbox': Inbox,
            'outbox': Outbox
        }
        intervals = {
            'lastweek': 7,
            'lastmonth': 31
        }

        # looking for each date stats
        for x in range(0, intervals[interval]):
            date = utcnow.date() - timedelta(days=x)

            # constructing query to get stats for 3 tables at query
            queries = []
            for key, model in elements.iteritems():
                query = db.session \
                          .query(func.count()) \
                          .filter(getattr(model, 'userId') == user.id) \
                          .filter(cast(getattr(model, 'created'), Date) == date)
                if app:
                    query = query.filter(getattr(model, 'applicationId') == app.id)

                query = query.limit(1).label(key)
                queries.append(query)

            counts = db.session.query(*tuple(queries)).one()

            payload[date.isoformat()] = {
                'sent': counts.sent,
                'inbox': counts.inbox,
                'outbox': counts.outbox,
            }

        return response(payload)
