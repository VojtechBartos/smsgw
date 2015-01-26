# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.

import traceback
from jsonschema import ValidationError
from smsgw.lib.utils import response
from flask import current_app


class ErrorResource(Exception):
    status_code = 400

    def __init__(self, status_code=None, payload=None, message=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    @staticmethod
    def register(app, **kwargs):

        @app.errorhandler(404)
        def on_unauthorized(error):
            return response(None, status_code=401, message="Unauthorized.")

        @app.errorhandler(404)
        def on_page_not_found(error):
            return response(None, status_code=404, message="Not found.")

        @app.errorhandler(ErrorResource)
        def on_error_resource(error):
            """ Error handler for ErrorResource exception """
            return response(None, error.status_code, error.message)

        @app.errorhandler(ValidationError)
        def on_validation_error(error):
            message = error.schema.get('message') or error.message
            return response(None, status_code=400, message=message)

        @app.errorhandler(Exception)
        def on_unhandled_exception(error):
            """ Error handler for unhandled exceptions """
            current_app.logger.error(traceback.format_exc())            

            return response(None, status_code=500)