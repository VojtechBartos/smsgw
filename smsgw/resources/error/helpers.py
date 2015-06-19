# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.

def get_validation_data(error):
    """
    Returns custom validation message based on error
    :param error: {ValidationError} error
    :return: {tuple} messsage, errors
    """
    errors = None
    message = error.schema.get('message') or error.message
    messages = error.schema.get('messages')
    if messages is not None:
        validator = error.validator if error.validator in messages else 'default'
        if messages.get(validator) is not None and error.path[0]:
            message = messages.get(validator)
            errors = { error.path[0]: [ messages.get(validator) ] }

    return message, errors