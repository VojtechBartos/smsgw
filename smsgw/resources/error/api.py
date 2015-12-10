# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.

import traceback
from jsonschema import ValidationError
from sqlalchemy.exc import IntegrityError
from flask import current_app

from smsgw.resources.error.helpers import get_validation_data
from smsgw.lib.utils import response
from smsgw.core import db


class ErrorResource(Exception):
    status_code = 400

    def __init__(self, status_code=None, payload=None, message=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    @staticmethod
    def register(app, **kwargs):

        @app.errorhandler(400)
        def on_bad_requests(error):
            return response(None, status_code=400, message=error.message)

        @app.errorhandler(401)
        def on_unauthorized(error):
            return response(None, status_code=401, message="Unauthorized.")

        @app.errorhandler(404)
        def on_page_not_found(error):
            return response(None, status_code=404, message="Not found.")

        @app.errorhandler(ErrorResource)
        def on_error_resource(error):
            """ Error handler for ErrorResource exception """
            return response(None, error.status_code, error.message)

        @app.errorhandler(IntegrityError)
        def on_sql_alchemy_error(error):
            """ Error handler for sqlalchemy IntegrityError exception """
            # do rollback
            db.session.rollback()
            # log it
            current_app.logger.error(traceback.format_exc())

            return response(None, status_code=500)

        @app.errorhandler(ValidationError)
        def on_validation_error(error):
            payload = None
            message, errors = get_validation_data(error)
            if errors is not None:
                payload = { 'errors': errors }

            return response(payload, status_code=400, message=message)

        @app.errorhandler(Exception)
        def on_unhandled_exception(error):
            """ Error handler for unhandled exceptions """
            current_app.logger.error(traceback.format_exc())

            return response(None, status_code=500)
